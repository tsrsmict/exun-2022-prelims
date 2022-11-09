import Image from "next/image"
function Header() {
  return (
    <nav className="font-space border border-b-4 border-x-0 border-t-0 border-white backdrop-blur-3xl w-screen bg-black bg-opacity-30 shadow-sm sticky shadow-zinc-800 z-5 px-2 sm:px-4 py-2.5 rounded">
      <div className="container text-9xl flex flex-wrap mx-auto justify-between items-center w-screen">
        <a href="https://flowbite.com/" className="flex left-0">
            <span className="self-center text-3xl font-semibold whitespace-nowrap dark:text-white"><span className="text-blue-400">Space</span> <span className="text-red-400">Legion</span> </span>
        </a>
        <button data-collapse-toggle="navbar-default" type="button" className="inline-flex items-center p-2 ml-3 text-3xl text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-default" aria-expanded="false">
          <span className="sr-only">Open main menu</span>
          <svg className="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clipRule="evenodd"></path></svg>
        </button>
        <div className="text-2xl hidden w-full md:block md:w-auto right-0" id="navbar-default">
          <ul className="flex flex-col p-4 mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 ">
            <li>
              <a href="/" className="block py-2 pr-4 pl-3 text-gray-700 bg-blue-700 rounded md:bg-transparent md:p-0 text-2xl dark:text-gray-400" aria-current="page">Home</a>
            </li>
            <li>
              <a href="/marketplace" className="block py-2 pr-4 pl-3 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 text-2xl md:hover:text-blue-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Marketplace</a>
            </li>
            <li>
              <a href="/userprofile" className="block py-2 pr-4 pl-3 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 text-2xl md:hover:text-blue-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">My Profile</a>
            </li>
            <li>
              <a href="/store" className="block py-2 pr-4 pl-3 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 text-2xl md:hover:text-blue-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Store</a>
            </li>
            <li>
              <a href="/signin" className="block text-gray-700 rounded hover:bg-gray-400 md:hover:bg-transparent md:border-0 text-2xl md:hover:text-blue-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-300 dark:hover:text-white md:dark:hover:bg-transparent">Sign In</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Header