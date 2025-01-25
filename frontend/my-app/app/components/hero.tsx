"use client"

export function Hero() {
  return (
    <section className="h-screen flex items-center justify-center relative overflow-hidden bg-gradient-to-br from-gray-900 via-gray-800 to-orange-900">
      <div className="container mx-auto px-4 z-10">
        <h1 className="text-5xl md:text-7xl font-bold text-center mb-6">
          Transform Your Videos with <span className="text-[hsl(var(--blue-accent))]">AI-Powered Dubbing</span>
        </h1>
        <p className="text-xl md:text-2xl text-center mb-8">
          Upload your video and get it dubbed in any language instantly
        </p>
      </div>
    </section>
  )
}

