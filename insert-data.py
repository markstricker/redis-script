import redis

r=redis.Redis(host=172.31.0.91,port=6379,password=Eagle1)

data=1
score=1
while data < 101
    r.zadd("store",{data:score})
    score +=1
    data +=1

r2=redis.Redis(host=172.31.12.196,port=6379,password=Eagle1)

value = r2.zrange("store", 0, 100, desc=True)
print(value)
