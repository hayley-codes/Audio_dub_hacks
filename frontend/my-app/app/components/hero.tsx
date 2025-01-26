"use client"

import { motion } from "framer-motion"
import { Space_Grotesk } from "next/font/google"

const spaceGrotesk = Space_Grotesk({ 
  subsets: ["latin"],
  weight: ["700"],
})

export function Hero() {
  return (
    <section className="h-screen flex items-center justify-center relative overflow-hidden">
      <div className="container mx-auto px-4 z-10">
        <motion.h1 
          className={`${spaceGrotesk.className} text-8xl md:text-[12rem] font-black text-center mb-8 bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-cyan-500`}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ 
            duration: 0.8,
            ease: "easeOut"
          }}
          whileHover={{ 
            scale: 1.05,
            transition: { duration: 0.2 }
          }}
        >
          DubIT
        </motion.h1>
        <motion.h2 
          className="text-4xl md:text-5xl font-bold text-center mb-6"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.3 }}
        >
          Transform Your Streaming Platform with <span className="text-[hsl(var(--blue-accent))]">AI-Powered Dubbing</span>
        </motion.h2>
        <motion.p 
          className="text-xl md:text-2xl text-center mb-8"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          Think Global, Speak Global.
        </motion.p>
      </div>
    </section>
  )
}

