import { motion } from "framer-motion";

export const BackgroundGraphic = () => {
  return (
    <div className="fixed inset-0 -z-50 overflow-hidden pointer-events-none">
      <motion.div
        className="absolute inset-0 w-full h-full"
        style={{
          background: "linear-gradient(45deg, #FF8A65, #FF5722, #FF7043)",
          filter: "blur(100px)",
        }}
        animate={{
          scale: [1, 1.2, 1],
          rotate: [0, 90, 0],
        }}
        transition={{
          duration: 20,
          ease: "easeInOut",
          repeat: Infinity,
        }}
      />
      <motion.div
        className="absolute inset-0 w-full h-full opacity-50"
        style={{
          background: "radial-gradient(circle at 50% 50%, #FFA726, transparent)",
          filter: "blur(60px)",
        }}
        animate={{
          scale: [1.2, 1, 1.2],
          rotate: [90, 0, 90],
        }}
        transition={{
          duration: 15,
          ease: "easeInOut",
          repeat: Infinity,
        }}
      />
    </div>
  );
}; 