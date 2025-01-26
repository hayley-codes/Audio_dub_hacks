"use client"

import { useState } from "react"
import Link from "next/link"
import Image from "next/image"
import { motion } from "framer-motion"

const navItems = [
  { name: "Home", href: "/" },
  { name: "Business", href: "#business" },
  { name: "About Us", href: "#about" },
  { name: "How It Works", href: "#how-it-works" },
]

export function Header() {
  const [activeItem, setActiveItem] = useState("Home")

  return (
    <header className="fixed top-0 left-0 right-0 z-50 backdrop-blur-md">
      <nav className="container mx-auto px-4 py-4 flex items-center justify-between">
        <Link href="/" className="flex items-center">
          <Image
            src="/DubItLogo.png"
            alt="DubIT Logo"
            width={425}
            height={212}
            className="w-auto h-[4.25rem]"
            priority
          />
        </Link>
        <ul className="flex space-x-4">
          {navItems.map((item) => (
            <li key={item.name}>
              <Link
                href={item.href}
                className="relative px-3 py-2 text-sm font-medium text-gray-300 hover:text-white transition-colors"
                onClick={() => setActiveItem(item.name)}
              >
                {item.name}
                {activeItem === item.name && (
                  <motion.div className="absolute bottom-0 left-0 right-0 h-0.5 bg-accent" layoutId="underline" />
                )}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  )
}

