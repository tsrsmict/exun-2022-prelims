import React from "react";
import { delay, motion } from 'framer-motion'
export default function lootbox() {
  const variants = {
    visible: { opacity: 1 },
    hidden: { opacity: 0 },
  }
  return (
    <div className="bg-black w-full bg-[url('/coolspace.jpg') items-center text-center text-white h-screen p-24">
      <div className="font-bold rounded-md text-7xl font-mono tracking-wide text-center m-auto p-4 bg-white bg-opacity-25 backdrop-blur-3xl">LOOTBOX</div>
      <a href="/userprofile">
      <img src="/SpaceBounty.png" className="m-auto hover:rotate-40deg hover:-translate-y-11"/></a>


    </div>
  );
}
