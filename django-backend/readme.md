# Prerequisites
Make sure you have the following installed on your system:
* Python
* [Pipenv](https://pypi.org/project/pipenv/)
* [NodeJS](https://github.com/nvm-sh/nvm)

## Backend server
Run the following commands in your shell in the root directory of the django repository:
1. `pipenv shell` (activates virtual environment)
2. `pipenv install` (install dependencies )
3. `python manage.py migrate` (you won't need to run these every time, just the first time you're setting up the project and if you edit SQL model schema)
5. `python3 manage.py runserver`
This will open the dev server on http://localhost:8000

## Frontend server
1. `npm install`
2. `npm run dev`