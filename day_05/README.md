
## Simple server with wsgi

- run the server by ***python3 credentials.py***
- in another terminal run **python3 tests.py***

## Simple server for mp3-files storing on Flask

- to run server in development mode:<br>
  ***python3 first_steps.py***<br>
- to run server in production-simulation mode*<br>
  ***python3 -m gunicorn -b localhost:8888 --reload first_steps:app***<br>
- then just go in your browser to: localhost/8888<br>
- to interact by script:
  - if want to list:<br>***python3 screwdriver.py list***
  - if want to upload:<br>***python3 screwdriver.py upload path/to/file [path/to/file]***

## First steps in threads with "doctors and screwdrivers problem"
- just run ***python3 doctors.py***