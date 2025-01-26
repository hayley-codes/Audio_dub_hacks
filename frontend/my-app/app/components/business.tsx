"use client"

import { motion } from "framer-motion"

export function Business() {
  return (
    <section id="business" className="min-h-screen flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="container mx-auto px-4"
      >
        <h2 className="text-4xl font-bold text-center mb-8">Business Solutions</h2>
        <p className="text-xl text-center">Discover how  can help your business reach a global audience.</p>
      </motion.div>
    </section>
  )
}

