$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ pip install Flask
$ pip freeze > requirements.txt
$ heroku login
$ echo "web: gunicorn app:app" > Procfile
$ heroku create iris-cloud-sql-python-demo
$ echo "IRISUSERNAME=SQLAdmin" > .env
$ echo "IRISPASSWORD=@Cloud124" >> .env
$ heroku pipelines:create --app iris-cloud-sql-python-demo \
    --stage production \
    iris-cloud-sql-python-demo
heroku git:remote --app iris-cloud-sql-python-demo --remote prod

$ heroku pipelines:promote --remote prod

$ heroku config:set --remote prod \
  SECRET_KEY=the-prod-key \
  APP_SETTINGS=config.StagingConfig

  heroku config:set --remote prod \
  HOST=isc_cloudsql_host_url \
  IRIS_USERNAME=SQLAdmin \
  IRIS_PASSWORD=Password \
  APP_SETTINGS=config.StagingConfig

ps aux | grep flask
