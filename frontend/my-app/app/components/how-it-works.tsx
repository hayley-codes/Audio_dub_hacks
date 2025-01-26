"use client"

import { motion } from "framer-motion"

export function HowItWorks() {
  return (
    <section id="how-it-works" className="min-h-screen flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="container mx-auto px-4 text-center"
      >
        <h2 className="text-4xl font-bold text-center mb-8">How It Works</h2>
        <p className="text-xl text-center mb-4">
          Explore the simple process of transforming your videos with AI-powered dubbing.
        </p>

        {/* Detailed Explanation */}
        <div className="mt-6">
          <h3 className="text-2xl font-semibold mb-4">Our Technology Stack</h3>
          <p className="text-lg mb-4">
            Our backend service is built in <strong>Python</strong>, utilizing <strong>Google Cloud APIs</strong> such as <strong>Speech</strong> and <strong>Translation</strong>. 
            Additionally, we use <strong>FFMpeg</strong> for audio and video file handling. This is not just an API wrapper; this is a custom solution intended for streaming giants.
          </p>
          <p className="text-lg mb-4">
            The frontend demo web app was created using <strong>Next.js</strong> and <strong>React</strong>, with Flask serving as the backend framework. We leverage libraries such as <strong>framer-motion</strong> to create smooth animations and enhance user experience.
          </p>
        </div>

        {/* Technology Stack Logos */}
        <div className="flex justify-center mt-8">
          <img src="/tech-stack-logos/python.png" alt="Python" className="h-16 mx-2" />
          <img src="/tech-stack-logos/GoogleCloud.png" alt="Google Cloud" className="h-16 mx-2" />
          <img src="/tech-stack-logos/typescript.png" alt="TypeScript" className="h-16 mx-2" />
          <img src="/tech-stack-logos/nextjs.png" alt="Next.js" className="h-16 mx-2" />
          <img src="/tech-stack-logos/React.png" alt="React" className="h-16 mx-2" />
          <img src="/tech-stack-logos/flask.png" alt="Flask" className="h-16 mx-2" />
        </div>
      </motion.div>
    </section>
  )
}

