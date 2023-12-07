### To work with script you need a database.
Just run:
- ***docker run --rm -p 5431:5432 -e POSTGRES_PASSWORD=password postgres***

In another terminal you can run:
- ***sudo docker exec -it <container_id> psql -U postgres -d postgres***

### Then you should migrate database:
- ***alembic init alembic***

In alembic.ini file there should be:
- ***sqlalchemy.url = postgresql://postgres:password@localhost:5431/postgres***

then:
- ***alembic revision -m "create account table"***

then, in the ***"alembic/versions"*** folder, find created script and replace upgrade and downgrade methods **upgrade** and **downgrade**<br>
Search methods in ***for_migration.py*** script

### Then up the server:
- ***python3 ../ex00/reporting_server.py***

### Then just run the script:
- ***python3 reporting_client_v3.py --scan --list_traitors 106.192 -28.032***
- ***python3 reporting_client_v3.py --scan 106.192 -28.032***

