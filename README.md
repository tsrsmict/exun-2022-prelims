# exun-prelims
Repo for Django app for the Exun 2022 Hackathon prelims

This repoistory contains the ReactJS Frontend and Django backend for the web app. The Django backend provides a REST API that the frontend can interface with currently, and which the 'game' can interface with later. 

The game, 'Space Legion', is a modernised 2030 version of the classic retro game 'Space Invaders'. The website is meant to:
1. Serve as a landing page / showcase for the game. This is achieved through the homepage of the web app.
2. Allow users to create accounts. This is achieved through pages that are available on the website.
3. Allow users to explore some of the functionality of the game. Users can open lootboxes, explore the marketplace, submit requests to buy and sell goods, and more.

Future features:
- Fully integrate the frontend and backend
- Develop more NFT ideas, going beyond skins for rockets. Prototype some 3D models to integrate into the game which require NFTs.
- Developing with web3 technologies, such as minting and securing NFT collections, requires startup capital. For now, ownership is simply guaranteed through an SQL database. Once the product has procured startup capital, we will be able to tie all collectibles to the blockchain as NFTs and guarantee ownership that way._


Navigate to `readme.MD` in the `django-backend` folder for instructions on how the API can be used and explored.
Navigate to `readme.MD` in the `react-frontend/next-frontend` folder for instructions on how to run the local webserver.
