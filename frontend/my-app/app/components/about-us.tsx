"use client"

import { motion } from "framer-motion"

export function AboutUs() {
  return (
    <section id="about" className="min-h-screen flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="container mx-auto px-4 text-center"
      >
        <h2 className="text-4xl font-bold text-center mb-8">About Us</h2>

        {/* Portraits Section */}
        <h3 className="text-2xl font-semibold mt-8 mb-8">
          Student hackers looking to expand content reach across the globe.
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="flex flex-col items-center">
            <img src="/portraits/TylerS.jpg" alt="Portrait 1" className="w-32 h-auto rounded-full mb-2" />
            <h2 className="text-xl font-bold mb-8">Tyler Steptoe</h2>
            <p className="text-lg">Cognitive Science Student @ University of Toronto.</p>
          </div>
          <div className="flex flex-col items-center">
            <img src="/portraits/HayleyC.jpg" alt="Portrait 2" className="w-32 h-auto rounded-full mb-2" />
            <h2 className="text-xl font-bold mb-8">Hayley Collins</h2>
            <p className="text-lg">Systems Design Engineering @ University of Waterloo</p>
          </div>
          <div className="flex flex-col items-center">
            <img src="/portraits/KiraR.jpg" alt="Portrait 3" className="w-32 h-auto rounded-full mb-2" />
            <h2 className="text-xl font-bold mb-8">Kira Rohra</h2>
            <p className="text-lg">Data Science Student @ Wilfrid Laurier University</p>
          </div>
        </div>
      </motion.div>
    </section>
  )
}

