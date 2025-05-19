import React, { useState } from 'react'
import axios from 'axios'

const ImageToVideo = () => {
  const [result, setResult] = useState(null)

  const handleGenerate = async () => {
    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/image-to-video`)
      setResult(res.data)
    } catch (err) {
      console.error(err)
    }
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">🎥 تحويل صورة إلى فيديو</h2>
      <button onClick={handleGenerate} className="px-4 py-2 bg-green-600 text-white rounded">
        توليد الفيديو
      </button>
      {result && <video controls className="mt-4 w-full" src={result.video_url}></video>}
    </div>
  )
}

export default ImageToVideo
