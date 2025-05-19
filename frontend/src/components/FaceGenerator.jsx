import React, { useState } from 'react'
import axios from 'axios'

const FaceGenerator = () => {
  const [faceUrl, setFaceUrl] = useState(null)

  const handleGenerate = async () => {
    try {
      const res = await axios.get(`${import.meta.env.VITE_API_URL}/generate-face`)
      setFaceUrl(res.data.image_url)
    } catch (err) {
      console.error(err)
    }
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">👤 توليد وجه وهمي</h2>
      <button onClick={handleGenerate} className="px-4 py-2 bg-rose-600 text-white rounded">
        توليد وجه
      </button>
      {faceUrl && <img src={faceUrl} alt="Generated Face" className="mt-4 w-full" />}
    </div>
  )
}

export default FaceGenerator
