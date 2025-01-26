import "./globals.css"
import { Inter, Space_Grotesk } from "next/font/google"

const inter = Inter({ subsets: ["latin"] })
const spaceGrotesk = Space_Grotesk({ 
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700"],
})

export const metadata = {
  title: "DubIt - AI-Powered Video Dubbing",
  description: "Upload your video and get it dubbed in any language instantly.",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} bg-gray-950 text-gray-100`}>{children}</body>
    </html>
  )
}

