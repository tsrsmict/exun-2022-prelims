git push heroku main
heroku run python3 manage.py makemigrations
heroku run python3 manage.py migrate
heroku open
git push origin main