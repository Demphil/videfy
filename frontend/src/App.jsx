import React from 'react';
import ImageToVideo from './components/ImageToVideo';
import TextGenerator from './components/TextGenerator';
import StyleTransfer from './components/StyleTransfer';
import FaceGenerator from './components/FaceGenerator';
import ImageAnalyzer from './components/ImageAnalyzer';
import ImageAnalyzer from './components/UploadImage';

export default function App() {
  return (
    <div className='p-4'>
      <h1 className='text-2xl font-bold mb-4'>Videfy AI Tools</h1>
      <ImageToVideo />
      <TextGenerator />
      <StyleTransfer />
      <FaceGenerator />
      <ImageAnalyzer />
    </div>
  );
}
