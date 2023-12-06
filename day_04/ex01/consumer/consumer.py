import redis
import json
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e')
logging.basicConfig(filename='logfile.log', encoding='utf-8', level=logging.DEBUG)

bad_nums = parser.parse_args().e.split(',')

r = redis.Redis(
    host = 'localhost',
    port = 6379,
    health_check_interval=30
)

mob = r.pubsub()
mob.subscribe('transactions')
for message in mob.listen():
    if message['type'] == 'message':
        message = json.loads(message['data'])
        if str(message['metadata']['to']) in bad_nums and message['amount'] > 0:
            message['metadata']['from'], message['metadata']['to'] = \
                message['metadata']['to'], message['metadata']['from']
            logging.warning(json.dumps(message))
        else:
            logging.info(json.dumps(message))
