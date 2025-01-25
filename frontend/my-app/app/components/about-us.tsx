"use client"

import { motion } from "framer-motion"

export function AboutUs() {
  return (
    <section id="about" className="min-h-screen flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="container mx-auto px-4"
      >
        <h2 className="text-4xl font-bold text-center mb-8">About Us</h2>
        <p className="text-xl text-center">Learn about our mission to break language barriers in video content.</p>
      </motion.div>
    </section>
  )
}

