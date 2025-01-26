import React from 'react';
import { motion } from "framer-motion";

export function IntegrationCollage() {
  const images = [
    { 
      src: "/ui-integration/NetflixDubIT.png", 
      style: { top: "10%", left: "10%", rotate: "-5deg" },
      size: "w-64"
    },
    { 
      src: "/ui-integration/HuluDubIT.png", 
      style: { top: "10%", right: "10%", rotate: "3deg" },
      size: "w-72"
    },
    { 
      src: "/ui-integration/MaxDubIT.png", 
      style: { bottom: "20%", right: "15%", rotate: "-3deg" },
      size: "w-60"
    },
    { 
      src: "/ui-integration/DisneyDubIT.png", 
      style: { bottom: "20%", left: "12%", rotate: "5deg" },
      size: "w-80"
    },
    { 
      src: "/ui-integration/PrimeDubIT.png", 
      style: { bottom: "5%", left: "30%", rotate: "-2deg" },
      size: "w-60"
    }
  ];

  return (
    <section className="min-h-screen flex items-center justify-center relative overflow-hidden">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="container mx-auto px-4"
      >
        <h2 className="text-4xl font-bold text-center mb-20">DubIT Integration with Streaming Services</h2>
        <div className="relative h-[700px] w-full">
          {images.map((image, index) => (
            <motion.img
              key={index}
              src={image.src}
              alt={`Service ${index + 1}`}
              className={`absolute h-auto rounded-xl shadow-xl ${image.size}`}
              style={image.style}
              initial={{ scale: 2, opacity: 0 }}
              whileInView={{ scale: 2, opacity: 1 }}
              whileHover={{ scale: 2.1, zIndex: 20 }}
              transition={{ duration: 0.3 }}
            />
          ))}
        </div>
      </motion.div>
    </section>
  );
}