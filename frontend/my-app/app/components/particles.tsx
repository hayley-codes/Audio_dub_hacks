"use client"

import { useEffect, useState } from "react"
import { motion, useMotionValue, useSpring } from "framer-motion"

interface Particle {
  initialX: number
  initialY: number
  color: string
}

export function Particles() {
  const [particles, setParticles] = useState<Particle[]>([])
  const mouseX = useMotionValue(0)
  const mouseY = useMotionValue(0)

  const springConfig = { damping: 50, stiffness: 100 }
  const springX = useSpring(mouseX, springConfig)
  const springY = useSpring(mouseY, springConfig)

  useEffect(() => {
    const colors = [
      "#FF6B6B", // coral
      "#4ECDC4", // turquoise
      "#45B7D1", // sky blue
      "#96CEB4", // mint
      "#FFEEAD", // cream
      "#FFD93D", // yellow
      "#FF8B94", // pink
    ]
    
    const newParticles = Array.from({ length: 50 }).map(() => ({
      initialX: Math.random() * window.innerWidth,
      initialY: Math.random() * window.innerHeight,
      color: colors[Math.floor(Math.random() * colors.length)],
    }))

    setParticles(newParticles)
  }, [])

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      // Divide by large numbers to make the movement very subtle
      mouseX.set(e.clientX / 50)
      mouseY.set(e.clientY / 50)
    }

    window.addEventListener("mousemove", handleMouseMove)
    return () => window.removeEventListener("mousemove", handleMouseMove)
  }, [mouseX, mouseY])

  return (
    <div className="fixed inset-0 -z-40 overflow-hidden pointer-events-none">
      {particles.map((particle, i) => (
        <motion.div
          key={i}
          className="absolute w-1 h-1 rounded-full"
          style={{
            backgroundColor: particle.color,
            filter: "blur(1px)",
            left: particle.initialX,
            top: particle.initialY,
          }}
          animate={{
            scale: [1, 1.5, 1],
            opacity: [0.3, 0.8, 0.3],
          }}
          transition={{
            scale: {
              duration: Math.random() * 2 + 2,
              repeat: Infinity,
              delay: Math.random() * 2,
            },
            opacity: {
              duration: Math.random() * 2 + 2,
              repeat: Infinity,
              delay: Math.random() * 2,
            },
          }}
        >
          <motion.div
            style={{
              width: "100%",
              height: "100%",
              x: springX,
              y: springY,
              position: 'absolute',
              left: 0,
              top: 0
            }}
            transition={{
              type: "spring",
              damping: 15,
              stiffness: 100,
            }}
          />
        </motion.div>
      ))}
    </div>
  )
}
