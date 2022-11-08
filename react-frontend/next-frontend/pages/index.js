import Header from '../components/Header'

export default function Home() {
  return (
    <div className={'h-full m-0 p-0 bg-white'}>

      <div className="bg-[url('/coolspace.jpg')] bg-cover bg-no-repeat backdrop-blur-sm w-full h-screen items-center text-center ">
      <Header/>
        <div className='w-60% items-center flex top-50 h-30 h-full  text-white text-3xl font-bold bg-black-chocolate'>
          
          <h1 className='text-9xl tracking-widest bg-white bg-opacity-10 text-light-yellow rounded-2xl shadow-lg border-black border-opacity-25 border-4 font-space items-center m-auto backdrop-blur-2xl p-36'>
            <span className='text-3xl font-space'>BASED ON THE CLASSIC RETRO GAME</span><br></br><span className='text-5xl font-bold font-space'>RE-IMAGNED FOR WEB3</span><br></br>
        <span className='text-red-400'>Space </span><span className='text-blue-400'>Legion</span></h1>
        </div>
        <div className=''></div>
        </div>

    </div>
  )

}

// scene.js
