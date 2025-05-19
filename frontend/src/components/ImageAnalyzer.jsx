import React, { useState } from 'react'
import axios from 'axios'

const ImageAnalyzer = () => {
  const [file, setFile] = useState(null)
  const [description, setDescription] = useState(null)

  const handleAnalyze = async () => {
    if (!file) return
    const formData = new FormData()
    formData.append('image', file)

    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/analyze-image`, formData)
      setDescription(res.data.caption)
    } catch (err) {
      console.error(err)
    }
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">🔍 تحليل محتوى الصورة</h2>
      <input type="file" accept="image/*" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleAnalyze} className="mt-2 px-4 py-2 bg-gray-700 text-white rounded">
        تحليل
      </button>
      {description && <p className="mt-2 bg-gray-100 p-2">{description}</p>}
    </div>
  )
}

export default ImageAnalyzer
