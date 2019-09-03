import redis
myred = redis.Redis()
print(myred.get("Hello"))
