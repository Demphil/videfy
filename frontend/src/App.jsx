import React from 'react'
import UploadImage from './components/UploadImage'
import ImageToVideo from './components/ImageToVideo'
import TextGenerator from './components/TextGenerator'
import StyleTransfer from './components/StyleTransfer'
import FaceGenerator from './components/FaceGenerator'
import ImageAnalyzer from './components/ImageAnalyzer'

const App = () => {
  return (
    <div className="p-4 max-w-5xl mx-auto space-y-6">
      <h1 className="text-3xl font-bold text-center">🎬 Videfy: AI Video Creator</h1>
      <UploadImage />
      <TextGenerator />
      <ImageToVideo />
      <StyleTransfer />
      <FaceGenerator />
      <ImageAnalyzer />
    </div>
  )
}

export default App

