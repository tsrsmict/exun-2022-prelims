import '../styles/globals.css'
import {motion} from 'framer-motion'
function MyApp({ Component, pageProps }) {
  const variants = {
    hidden: { opacity: 0, x: -200, y: 0 },
    enter: { opacity: 1, x: 0, y: 0 },
    exit: { opacity: 0, x: 0, y: -100 },
}
  return (
  <motion.div variants={variants} initial="hidden" // Set the initial state to variants.hidden
  animate="enter" // Animated state to variants.enter
  exit="exit" // Exit state (used later) to variants.exit
  transition={{ type: 'linear', delay: 1 }} // Set the transition to linear
  className="">
    <Component {...pageProps} />
    </motion.div>
  )
}

export default MyApp
