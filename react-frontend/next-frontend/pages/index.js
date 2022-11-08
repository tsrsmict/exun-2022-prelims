import Header from '../components/Header'

export default function Home() {
  return (
    <div className={'h-full m-0 p-0 bg-white'}>

      <div className="bg-[url('/coolspace.jpg')] bg-cover bg-no-repeat w-full h-screen items-center text-center ">
      <Header/>
        <div className='mt-1000px w-40 h-80 backdrop-blur- text-white text-3xl font-bold bg-black-chocolate'>
          <p className='text-light-yellow'>
        WHITE LIFE MATTER</p>
        </div></div>

    </div>
  )

}

// scene.js
