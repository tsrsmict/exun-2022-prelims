import React from 'react'

function marketplace() {
  return (
    <div>
    <div class="w-full max-w-sm bg-white rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-700">
        <a href="#">
            <img class="p-8 rounded-t-lg" src="/docs/images/products/apple-watch.png" alt="product image"/>
        </a>
        <div class="px-5 pb-5">
            <a href="#">
                <h5 class="text-xl font-semibold tracking-tight text-gray-900 dark:text-white">Exclusive Dumb NFT apple watch</h5>
            </a>
            <div class="flex justify-between items-center">
                <span class="text-3xl font-bold text-gray-900 dark:text-white">$599</span>
                <a href="#" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Add to cart</a>
            </div>
        </div>
    </div>
    </div>
  )
}

export default marketplace