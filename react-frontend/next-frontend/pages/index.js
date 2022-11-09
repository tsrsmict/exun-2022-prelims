import Header from "../components/Header";
import {
  FaXbox,
  FaPlaystation,
  FaWindows,
  FaSteam,
  FaGooglePlay,
} from "react-icons/fa";

export default function Home() {
  return (
    <div className={"h-full m-0 p-0 bg-white"}>
      <div data-aos="fade-in" className="snap-mandatory snap-y">
        <div className="bg-[url('/coolspace.jpg')] bg-cover bg-no-repeat backdrop-blur-sm w-full h-screen items-center text-center ">
          <Header className="fixed top-0 z-50" />
          <div className="w-60% items-center flex top-50 h-30 h-full  text-white text-3xl font-bold bg-black-chocolate">
            <div className="text-9xl tracking-widest justify-between text-center items-center bg-white bg-opacity-10 text-light-yellow rounded-2xl shadow-lg border-black border-opacity-25 border-4 font-space w-fit m-auto backdrop-blur-2xl p-20">
              <span className="text-3xl font-mono">
                BASED ON THE CLASSIC SHOOT 'EM UP GAME
              </span>
              <br />
              <span className="text-5xl font-mono font-bold">
                RE-IMAGINED FOR WEB3
              </span>
              <br />
              <span className="text-blue-400 p-5">Space </span>
              <span className="text-red-400 p-5">Legion</span>
              <br />
              <br />
              <p className="mx-96 my-5 items-center text-center text-5xl flex font-mono tracking-tight">
                Available on: <FaPlaystation className="mx-5 flex text-5xl" />
                <br />
                <span className="flex">
                  <FaSteam className="mx-5 flex text-5xl" />
                  <FaWindows className="mx-5 flex text-5xl" />
                  <FaXbox className="mx-5 flex text-5xl" />
                  <FaGooglePlay className="mx-5 flex text-5xl" />
                </span>
              </p>
            </div>
          </div>
        </div>
        <div className="bg-gradient-to-b from-purplish to-purplish-two h-screen w-full p-12">
          <div className="items-center text-center">
            <h1 className="text-7xl text-slate-blue font-bold font-space upper mb-5">
              A world of possibilities
            </h1>
            
          <table className="p-24 mt-48 w-full m-auto items-center text-center text-white">
            <tr className="w-27% p-5 m-auto">
              <td>
                <img src="SpaceCoin.png" className="w-64 m-auto" />
              </td>
              <td>
                <img src="SpaceBounty.png" className="w-64 mx-auto" />
              </td>
              <td>
                <img src="SpaceBucks.png" className="w-64 m-auto" />
              </td>
            </tr>
            <tr className="w-27% p-5 m-auto">
              <td>
                <h1 className="w3/4 text-5xl mt-5 m-auto font-mono tracking-widest font-bold">
                  EARN
                </h1>
              </td>
              <td>
                <h1 className="w-3/4 text-5xl mt-5 m-auto font-mono tracking-widest font-bold">
                  OPEN
                </h1>
              </td>
              <td>
                <h1 className="w-3/4 text-5xl mt-5 m-auto font-mono tracking-widest font-bold">
                  TRADE
                </h1>
              </td>
            </tr>
            <tr className="w-27% p-5 m-auto">
              <td>
                <h1 className="w-3/4 text-2xl mt-5 m-auto font-mono tracking-widest font-light">
                  Earn SpaceCoins™️ every time you smash those aliens and
                  destroy enemy artillery. No pay-to-win.
                </h1>
              </td>
              <td>
                <h1 className="w-3/4 text-2xl  mt-5 m-auto font-mono tracking-widest font-light">
                  Open SpaceBounties™️ reward boxes with your SpaceCoins™️ to
                  unlock NFT SpaceBits™️. They’re yours and yours alone.
                </h1>
              </td>
              <td>
                <h1 className="w-3/4 text-2xl mt-5 m-auto font-mono tracking-widest font-light">
                  Buy and sell SpaceBits™️ on an all-new SpaceBucks™️currency.
                  No fiat.
                </h1>
              </td>
            </tr>
          </table>
          </div>
        </div>
        <div className="bg-gradient-to-b from-purplish-two to-purplish-three h-screen w-full p-24">
          <div className=" items-center text-center">
            <h1 className="text-cute-pink text-7xl font-bold font-space upper mb-24">
              REAL VALUE. PERIOD.
            </h1>
          </div>
          <div>
          <h1 className="font-thin text-5xl font-mono w-3/5 text-pink-500">
            We don’t like Pay-to-Win games.
            <br />
            <br />
            <br />
            That’s why SpaceBits can only be earned in-game. Skins, cosmetics,
            and bragging rights - they’re <span className="font-bold">yours on the blockchain.</span>
            <br />
            <br />
            <br />
            You can earn <span className="font-bold">real crypto</span>, trading your SpaceBits on this website for
            SpaceBucks™️ - an all-new cryptocurrency.
          </h1>
          </div>
        </div>
        <div className="bg-gradient-to-b from-purplish-three to-purplish-four h-screen w-full p-24">
        <div className=" items-center text-center">
            <h1 className="text-cute-pink text-7xl font-bold font-space upper mb-24">
              REAL VALUE. PERIOD.
            </h1>
          </div>
        </div>
      </div>
    </div>
  );
}

// scene.js
