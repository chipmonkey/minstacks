import configure as cfg
import databases
import sqlalchemy
import logging
import os
from pydantic import BaseModel
from typing import List

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI(title="REST API using FastAPI PostgreSQL Async EndPoints")
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(CORSMiddleware,
    allow_origins=["localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(
    cfg.psql_username,
    cfg.psql_password,
    cfg.psql_host,
    cfg.psql_port,
    cfg.psql_dbname, 'prefer')

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
metadata.create_all(engine)

class NoteIn(BaseModel):
    text: str
    completed: bool

class Note(BaseModel):
    id: int
    text: str
    completed: bool

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/notes/", response_model=Note, status_code = status.HTTP_201_CREATED)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}

@app.put("/notes/{note_id}/", response_model=Note, status_code = status.HTTP_200_OK)
async def update_note(note_id: int, payload: NoteIn):
    query = notes.update().where(notes.c.id == note_id).values(text=payload.text, completed=payload.completed)
    await database.execute(query)
    return {**payload.dict(), "id": note_id}

@app.get("/notes/", response_model=List[Note], status_code = status.HTTP_200_OK)
async def read_notes(skip: int = 0, take: int = 20):
    query = notes.select().offset(skip).limit(take)
    return await database.fetch_all(query)

@app.get("/notes/{note_id}/", response_model=Note, status_code = status.HTTP_200_OK)
async def read_notes(note_id: int):
    query = notes.select().where(notes.c.id == note_id)
    return await database.fetch_one(query)

@app.delete("/notes/{note_id}/", status_code = status.HTTP_200_OK)
async def update_note(note_id: int):
    query = notes.delete().where(notes.c.id == note_id)
    await database.execute(query)
    return {"message": "Note with id: {} deleted successfully!".format(note_id)}

