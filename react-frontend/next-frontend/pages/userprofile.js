import React from 'react'
import Header from '../components/Header'

function userprofile() {
  return (
    <div className='bg-black'>
    <Header/>
    <div className="p-12 bg-[url('/coolspace.jpg')]  bg-cover bg-repeat-0 backdrop-blur-3xl h-screen w-full">
        
        <div className='flex backdrop-blur-2xl bg-white bg-opacity-25 rounded-2xl justify-between'>
        <h1 className="font-space text-5xl p-5 font-bold text-white shadow-2xl pb-2">MY PROFILE</h1>
        <div className='p-3 w-fit h-fit rounded-2xl align-middle m-5 bg-opacity-25 bg-white backdrop-blur-2xl'>🪙 50000</div>
        </div>
    <div className="inline-flex">

    <div class="m-20 left-20 bg-white bg-opacity-25 w-full max-w-sm rounded-lg backdrop-blur-2xl">
        <a href="#">
            <img class="p-8 w-80 rounded-t-lg" src="/nft3.png" alt="product image"/>
        </a>
        <div class="px-5 pb-5">
            <a href="#">
                <h5 class="text-xl p-2 font-semibold tracking-tight text-gray-900 dark:text-white">Sonic Engine Traveller</h5>
            </a>
            <h5 class="text-xl p-2 font-semibold tracking-tight text-gray-900 dark:text-white">Current bid:</h5>
            <div class="flex justify-between items-center">
                <span class="text-3xl font-bold text-gray-900 dark:text-white">35k Coins</span>
                <br/><br/>
                <a href="#" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Sell Now</a>
            </div>
        </div>
    </div>
   
    </div>
    </div>
    </div>
  )
}

export default userprofile