release: google/bin/cloud_sql_proxy -instances=data-class-1570673095864:us-west1:twitter-db=tcp:3306 -credential_file=credentials.json &
web: gunicorn app:app
