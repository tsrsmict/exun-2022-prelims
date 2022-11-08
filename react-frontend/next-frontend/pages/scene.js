import { Canvas } from "@react-three/fiber"
import { motion } from "framer-motion-3d"

export function Scene({ isHovered }) {
  return (
    <Canvas>
      <motion.group animate={isHovered ? "hover" : "rest"}>
        <motion.mesh variants={{ hover: { z: 1 } }} />
      </motion.group>
    </Canvas>
  )
}