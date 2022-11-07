# Prerequisites
Make sure you have the following installed on your system:
* Python
* [Pipenv](https://pypi.org/project/pipenv/)
* [NodeJS](https://github.com/nvm-sh/nvm)
## Development server
Run the following commands in your shell in the root directory of this repository:
1. `pipenv shell` (activates virtual environment)
2. `pipenv install` (install dependencies )
3. `python3 manage.py makemigrations` and `python3 manage.py migrate` (you won't need to run these every time, just the first time you're setting up the project and if you edit SQL model schema)
5. `python3 manage.py runserver`
This will open the server on http://localhost:8000

## Tailwind
If you're editing the frontend with Tailwind CSS classes, you'll need to have the tailwind listener running

Steps:
1. Activate your pipenv: `pipenv shell`
2. Run `python3 manage.py tailwind start`. This will start a listener which automatically configures the tailwind files

Refer to the [django-tailwind docs](https://django-tailwind.readthedocs.io/en/latest/installation.html) for more instructions and debugging help on using Tailwind with Django in this project.

## Python dependencies
Install python dependencies with `pipenv install packagename` instead of `pip install packagename`. This will automatically add the package to the `Pipfile`, which is what we're using for dependency management.

# Deploys
Pushes to the `origin/main` branch will automatically deploy the latest version of the main branch to the Heroku app. You can force a heroku deploy by running `git push heroku main`. 