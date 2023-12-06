## ex 00
- simple injections in html pages

## ex 01
pub/sub emulation with redis-server, producer and consumer.
- launch consumer with arguments of *bad transaction recievers*,
for example ***python3 -e consumer.py 1000000000***.
- then launch producer. it will emulate publising of transactions.

Consumer will substitute data in transactions with bad recievers, if amount of transaction > 0
Also it will write records into logfile.