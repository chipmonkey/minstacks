import redis
myred = redis.Redis()
myred.mset({"Hello": "World"})
print(myred.get("Hello"))
