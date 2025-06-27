Exec Docker

docker build -t simplecrm .
docker run -p 8000:8000 simplecrm


Populate data:

python manage.py populate_data