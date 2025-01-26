"use client"

import { useState, useCallback } from "react"
import { useDropzone } from "react-dropzone"
import { motion } from "framer-motion"
import { Upload } from "lucide-react"

export function FileUpload() {
  const [file, setFile] = useState<File | null>(null)
  const [language, setLanguage] = useState<string>('es') // Default language

  const onDrop = useCallback((acceptedFiles: File[]) => {
    setFile(acceptedFiles[0])
  }, [])

  const handleLanguageChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setLanguage(event.target.value)
  }

  const handleSubmit = () => {
    // Logic to handle file upload along with the selected language
    // ...
  }

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "video/mp4": [".mp4"],
    },
    maxFiles: 1,
  })

  return (
    <section className="min-h-screen flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="container mx-auto px-4 text-center"
      >
        <h2 className="text-4xl font-bold mb-8">Upload Your Video</h2>
        
        {/* Demo Information */}
        <p className="text-lg mb-4">
          This is a demo showcasing the technology that streaming giants such as <strong>Netflix</strong> and <strong>Prime Video</strong> will use when they partner with us. 
          Please upload a video file to see how DubIT can enhance your viewing experience!
        </p>

        {/* Language Selection Dropdown */}
        <div className="mb-4">
          <label htmlFor="language" className="block text-lg mb-2">Select Language:</label>
          <select
            id="language"
            value={language}
            onChange={handleLanguageChange}
            className="border rounded p-2 bg-gray-200 text-gray-800"
          >
            <option value="es">Spanish</option>
            <option value="en">English</option>
            <option value="fr">French</option>
            <option value="de">German</option>
            <option value="it">Italian</option>
            <option value="pt">Portuguese</option>
            <option value="zh">Chinese</option>
            <option value="ja">Japanese</option>
            <option value="ko">Korean</option>
            {/* Add more languages as needed */}
          </select>
        </div>

        <div
          {...getRootProps()}
          className={`border-2 border-dashed rounded-lg p-12 text-center cursor-pointer transition-colors ${
            isDragActive ? "border-accent" : "border-gray-600 hover:border-gray-500"
          }`}
        >
          <input {...getInputProps()} />
          <Upload className="mx-auto h-12 w-12 text-gray-400 mb-4" />
          {file ? (
            <p className="text-lg">File selected: {file.name}</p>
          ) : isDragActive ? (
            <p className="text-lg">Drop the MP4 file here...</p>
          ) : (
            <p className="text-lg">Drag and drop an MP4 file here, or click to select a file</p>
          )}
        </div>
      </motion.div>
    </section>
  )
}

