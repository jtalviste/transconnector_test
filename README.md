# TransConnector test assignment

To run you may need to activate a virtual python environment first.

To install, run
``` bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata office.json
python manage.py loaddata person.json
python manage.py loaddata workhistory.json
python manage.py crontab add
```

There is a utility in office_app\apikey.py.
It prints out how to set up the API key environment variable.
When not set, the API key defaults to "apikey", this must be in the "Apikey" header.

There is a management command "update_workhistory." If crontab doesn't work (e.g on Windows)
then it can be called at midnights.

To run the server, run 
``` bash
python manage.py runserver
```

To run the tests, run 
``` bash
python manage.py test
```



