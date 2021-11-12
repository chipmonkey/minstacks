curl -X POST "http://localhost:8000/notes/" \
 -H "accept: application/json" \
 -H "Content-Type: application/json" \
 -d "{\"text\":\"Get Groceries from the store\",\"completed\":false}"
