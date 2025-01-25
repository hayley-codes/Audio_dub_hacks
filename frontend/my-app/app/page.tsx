"use client"

import { useRef } from "react"
import { motion, useScroll, useTransform } from "framer-motion"
import { Header } from "./components/header"
import { Hero } from "./components/hero"
import { FileUpload } from "./components/file-upload"
import { Business } from "./components/business"
import { AboutUs } from "./components/about-us"
import { HowItWorks } from "./components/how-it-works"

export default function Home() {
  const containerRef = useRef<HTMLDivElement>(null)

  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"],
  })

  const heroOpacity = useTransform(scrollYProgress, [0, 0.2], [1, 0])
  const heroScale = useTransform(scrollYProgress, [0, 0.2], [1, 0.8])

  return (
    <main ref={containerRef} className="min-h-screen">
      <Header />
      <motion.div style={{ opacity: heroOpacity, scale: heroScale }}>
        <Hero />
      </motion.div>
      <FileUpload />
      <Business />
      <AboutUs />
      <HowItWorks />
    </main>
  )
}

