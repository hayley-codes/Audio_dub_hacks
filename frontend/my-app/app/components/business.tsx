"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/react/24/solid';

export function Business() {
  const [openSection, setOpenSection] = useState<string | null>(null)

  const toggleSection = (section: string) => {
    setOpenSection(openSection === section ? null : section)
  }

  return (
    <section id="business" className="min-h-screen flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="container mx-auto px-4 text-center"
      >
        <h2 className="text-4xl font-bold mb-8">Business Solutions</h2>
        <p className="text-xl mb-4">Discover how DubIT can help your business reach a global audience.</p>

        {/* Our Inspiration Section */}
        <div className="mt-10">
          <h3 className="text-4xl font-semibold mb-12">Our Inspiration 💡</h3>
          <h4 className="text-xl font-semibold cursor-pointer flex items-center justify-center mb-12" onClick={() => toggleSection("languageGap")}>
            The Language Gap
            {openSection === "languageGap" ? <ChevronUpIcon className="h-5 w-5 ml-2" /> : <ChevronDownIcon className="h-5 w-5 ml-2" />}
          </h4>
          {openSection === "languageGap" && (
            <div className="mb-4">
              <ul className="list-disc list-inside">
                <li>40% of users report difficulty finding content available in their native language.</li>
                <li>65% of multilingual users say they watch content in non-native languages but prefer native-language experiences.</li>
                <li>30% of households indicate they would watch more international content if dubbing options were available.</li>
              </ul>
            </div>
          )}

          <h4 className="text-xl font-semibold cursor-pointer flex items-center justify-center mb-12" onClick={() => toggleSection("streamingEverywhere")}>
            Streaming is Everywhere
            {openSection === "streamingEverywhere" ? <ChevronUpIcon className="h-5 w-5 ml-2" /> : <ChevronDownIcon className="h-5 w-5 ml-2" />}
          </h4>
          {openSection === "streamingEverywhere" && (
            <div className="mb-4">
              <ul className="list-disc list-inside">
                <li>88% of households are subscribed to one or more streaming platforms, with the average number of services subscribed to being 4.1.</li>
                <li>As on-demand streaming continues to dominate the entertainment industry, there is a large market cap when considering the global market, and the opportunities for language expansion. Most media on Netflix, Prime Video, and Disney+ is only available in 2 or 3 language dubs. With DubIT, streaming giants can tap into this market growth potential.
                </li>
              </ul>
            </div>
          )}
        </div>

        {/* Benefits of DubIT Section */}
        <div className="mt-10">
          <h3 className="text-4xl font-semibold mb-12">Benefits of DubIT 💸</h3>
          <h4 className="text-xl font-semibold cursor-pointer flex items-center justify-center mb-12" onClick={() => toggleSection("unlockGlobalMarkets")}>
            Unlock Global Markets
            {openSection === "unlockGlobalMarkets" ? <ChevronUpIcon className="h-5 w-5 ml-2" /> : <ChevronDownIcon className="h-5 w-5 ml-2" />}
          </h4>
          {openSection === "unlockGlobalMarkets" && (
            <div className="mb-4">
              <p>
                Streaming giants can tap into <strong>under-served</strong> regions where content is limited. Imagine the potential for <strong>streaming in emerging markets</strong>. With DubIT dubbing, you can <strong>expand reach to non-English speaking markets</strong>.
              </p>
            </div>
          )}

          <h4 className="text-xl font-semibold cursor-pointer flex items-center justify-center mb-12" onClick={() => toggleSection("expandContentAccessibility")}>
            Expand Content Accessibility
            {openSection === "expandContentAccessibility" ? <ChevronUpIcon className="h-5 w-5 ml-2" /> : <ChevronDownIcon className="h-5 w-5 ml-2" />}
          </h4>
          {openSection === "expandContentAccessibility" && (
            <div className="mb-4">
              <p>
                Offering multiple dubbed languages enables streamers to cater to a <strong>larger, more diverse audience</strong>, and existing customers are more likely to stay with platforms offering <strong>enhanced viewing experiences</strong>.
              </p>
            </div>
          )}

          <h4 className="text-xl font-semibold cursor-pointer flex items-center justify-center mb-12" onClick={() => toggleSection("increaseCustomerSatisfaction")}>
            Increase Customer Satisfaction
            {openSection === "increaseCustomerSatisfaction" ? <ChevronUpIcon className="h-5 w-5 ml-2" /> : <ChevronDownIcon className="h-5 w-5 ml-2" />}
          </h4>
          {openSection === "increaseCustomerSatisfaction" && (
            <div className="mb-4">
              <p>
                Users who face language limitations will have the ability to enjoy a wider range of content, <strong>enhancing engagement</strong>. It allows users to explore content they may have otherwise ignored, <strong>boosting content consumption</strong>.
              </p>
            </div>
          )}

          <h4 className="text-xl font-semibold cursor-pointer flex items-center justify-center mb-12" onClick={() => toggleSection("contentLongevity")}>
            Content Longevity and Flexibility
            {openSection === "contentLongevity" ? <ChevronUpIcon className="h-5 w-5 ml-2" /> : <ChevronDownIcon className="h-5 w-5 ml-2" />}
          </h4>
          {openSection === "contentLongevity" && (
            <div className="mb-4">
              <p>
                Streaming giants can <strong>retroactively breathe life</strong> into older shows and movies by adding dubbing in high-demand languages. This will also allow platforms to <strong>release content quicker in new languages</strong>, increasing the velocity of content expansion globally.
              </p>
            </div>
          )}

          <h4 className="text-xl font-semibold cursor-pointer flex items-center justify-center mb-12" onClick={() => toggleSection("monetizationOpportunities")}>
            Monetization Opportunities
            {openSection === "monetizationOpportunities" ? <ChevronUpIcon className="h-5 w-5 ml-2" /> : <ChevronDownIcon className="h-5 w-5 ml-2" />}
          </h4>
          {openSection === "monetizationOpportunities" && (
            <div className="mb-4">
              <p>
                Streaming giants can offer AI dubbing as a <strong>premium service</strong>, leading to an <strong>increased ARPU</strong>. By making content accessible in new languages, platforms can partner with international content creators, creating <strong>new revenue streams</strong>.
              </p>
            </div>
          )}

          <h4 className="text-xl font-semibold cursor-pointer flex items-center justify-center mb-12" onClick={() => toggleSection("technologicalLeadership")}>
            Technological Leadership
            {openSection === "technologicalLeadership" ? <ChevronUpIcon className="h-5 w-5 ml-2" /> : <ChevronDownIcon className="h-5 w-5 ml-2" />}
          </h4>
          {openSection === "technologicalLeadership" && (
            <div className="mb-4">
              <p>
                By adopting and integrating an AI dubbing service, streaming giants serve to position themselves as <strong>leaders in innovation</strong> and <strong>technology-driven customer experience</strong>. Promoting content in multiple languages also aligns with corporate values around <strong>accessibility, diversity, and inclusion</strong>.
              </p>
            </div>
          )}
        </div>
      </motion.div>
    </section>
  )
}

