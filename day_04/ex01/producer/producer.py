import redis
import random
import json



r = redis.Redis(
    host = '127.0.0.1',
    port = 6379,
    decode_responses=True
)


for i in range(10):
    rand_first = random.randint(1000000000, 9999999999)
    rand_second = random.randint(1000000000, 9999999999)
    rand_amount = random.randint(1000, 100000)
    new_record = {'metadata':{'from':rand_first, 'to':rand_second}, 'amount':rand_amount}
    r.publish('transactions', json.dumps(new_record))

new_record = {'metadata':{'from':9999999999, 'to':1000000000}, 'amount': 100}
r.publish('transactions', json.dumps(new_record))
new_record = {'metadata':{'from':9999999999, 'to':1000000000}, 'amount': -100}
r.publish('transactions', json.dumps(new_record))
