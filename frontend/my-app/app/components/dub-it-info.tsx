import { motion } from "framer-motion";

export function DubITInfo() {
  return (
    <section className="min-h-screen flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="container mx-auto px-4 text-center"
      >
        <h2 className="text-4xl font-bold mb-4">What is <strong>DubIT</strong>? 🎤</h2>
        <p className="text-xl mb-4">
          DubIT is our integrated AI-powered automatic video dubber, intended to be used by industry giants such as Netflix, Prime Video, Hulu, Disney+ and more. Have you ever felt frustrated that a show you wanted to watch wasn't presented in your native language, and you just didn't want to bother with subtitles? 
        </p>
        <p className="text-xl mb-4">
          With DubIT, all the end user would have to do is click a button, and you'll be able to watch <strong>any show or film</strong> in <strong>any language</strong>.
        </p>

        {/* Additional Features Section */}
        <h3 className="text-2xl font-semibold mt-8 mb-4">Key Features of DubIT</h3>
        <ul className="list-disc list-inside mb-4 text-lg">
          <li><strong>The first integrated solution</strong> for streaming giants. AI video dubbing exists, but not yet on the enterprise level as we are aiming for.</li>
          <li>Over <strong>100 languages supported</strong> via use of Google Cloud API.</li>
          <li>Trained with data from the <strong>integrated platform</strong>; if we partner with Netflix, DubIT will use actors from Netflix's database of films and TV shows, <strong>decreasing costs</strong>.</li>
          <li>The translated dub <strong>still sounds like the original voice</strong>.</li>
        </ul>
      </motion.div>
    </section>
  );
}