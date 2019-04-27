import redis

r=redis.Redis(host="hosta",port=6379,password=pword1)

data=1
score=1
while data < 101
    r.zadd("store",{data:score})
    score +=1
    data +=1

r2=redis.Redis(host="hostb",port=12345,password=pword2)

value = r2.zrange("store", 0, 100, desc=True)
print(value)
