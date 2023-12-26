# TransConnector test assignment

To run you may need to activate a virtual python environment first.

To install, run
``` bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata office.json
python manage.py loaddata person.json
python manage.py loaddata workhistory.json
```

Env var should be set TRANS_CONNECTOR_API_KEY_HASH=O6GFX73m4tIviuv8YtYcJwGy6awVSsb2QxG7iLjSfU8=
in case you want the API key to be just "apikey"

There is a utility in office_app\apikey.py.
It prints out how to set up the API key environment variable.

To run the server, do
run 
``` bash
python manage.py runserver
```



