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

## API Documentation
All endpoints below are relative to `/api`

- `/users`: 
  -   `GET` a list of users
  -   `POST`username and password
-   `/auth-token`:`POST` username and password and receive an authentication token in the response

All requests after this require the 'Authentication' header with the value 'Token abc1234...' (substitute your token in place of abc1234...)

- `/lootbox-tiers/` - GET a list of lootboxes. Supports a primary key at the end to get data for a specific lootbox
- - `/nft-collectibles/` - GET a list of possible NFT collectibles.  Supports a primary key at the end to get data for a specific collectible.
- `/open-lootbox` - POST to open a lootbox. Opens collectibles which no one has mined yet, adds them to an account, and sends them back in the response. Subtracts the cost of the lootbox from the account.
- `/make-purchase-request` - POST a request to purchase a collectible from someone who owns it, along with an amount for the bid.
- `/purchase-requests` - GET a list of bid (purchase requests).  Supports a primary key at the end to get data for a specific bid.
- `/accept-purchase-request` - If correct authorisation, allows the sender to POST an acceptance of the purchase request. Updates the status of other purchase requests.
