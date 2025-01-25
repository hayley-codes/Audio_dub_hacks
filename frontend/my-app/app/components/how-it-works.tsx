"use client"

import { motion } from "framer-motion"

export function HowItWorks() {
  return (
    <section id="how-it-works" className="min-h-screen flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="container mx-auto px-4"
      >
        <h2 className="text-4xl font-bold text-center mb-8">How It Works</h2>
        <p className="text-xl text-center">
          Explore the simple process of transforming your videos with AI-powered dubbing.
        </p>
      </motion.div>
    </section>
  )
}

