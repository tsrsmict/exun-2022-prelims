import Header from '../components/Header'
import { FaXbox, FaPlaystation, FaWindows, FaSteam, FaGooglePlay } from "react-icons/fa";

export default function Home() {
  return (
    <div className={'h-full m-0 p-0 bg-white'}>
      <div data-aos="fade-in" className='snap-mandatory snap-y'>
      <div className="bg-[url('/coolspace.jpg')] bg-cover bg-no-repeat backdrop-blur-sm w-full h-screen items-center text-center ">
      <Header className="fixed top-0 z-50"/>
        <div className='w-60% items-center flex top-50 h-30 h-full  text-white text-3xl font-bold bg-black-chocolate'>
          
          <h1 className='text-9xl tracking-widest justify-between text-center items-center bg-white bg-opacity-10 text-light-yellow rounded-2xl shadow-lg border-black border-opacity-25 border-4 font-space w-fit m-auto backdrop-blur-2xl p-20'>
            <span className='text-3xl font-mono'>BASED ON THE CLASSIC RETRO GAME</span><br/><span className='text-5xl font-mono font-bold'>RE-IMAGNED FOR WEB3</span><br/>
        <span className='text-blue-400 p-5'>Space </span><span className='text-red-400 p-5'>Legion</span><br/><br/>
          <p className='mx-96 my-5 items-center text-center text-5xl flex font-mono tracking-tight'>
          Available on: <FaPlaystation className='mx-5 flex text-5xl'/>
          <br/><span>
          <FaSteam className='mx-5 flex text-5xl'/>
          <FaWindows className='mx-5 flex text-5xl'/>
          <FaXbox className='mx-5 flex text-5xl'/><FaGooglePlay className='mx-5 flex text-5xl'/></span></p>
          
       </h1>
        
        </div>
        
        </div>
        <div className='bg-stone-300 h-screen w-full coin'>

        </div>
        </div>
    </div>
  )

}

// scene.js
