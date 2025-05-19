import React, { useState } from 'react'
import axios from 'axios'

const StyleTransfer = () => {
  const [file, setFile] = useState(null)
  const [styledImage, setStyledImage] = useState(null)

  const handleTransfer = async () => {
    if (!file) return
    const formData = new FormData()
    formData.append('image', file)

    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/style-transfer`, formData)
      setStyledImage(res.data.output_url)
    } catch (err) {
      console.error(err)
    }
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">🎨 تحويل الصورة بأسلوب فني</h2>
      <input type="file" accept="image/*" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleTransfer} className="mt-2 px-4 py-2 bg-indigo-600 text-white rounded">
        تطبيق النمط
      </button>
      {styledImage && <img src={styledImage} alt="Stylized" className="mt-4 w-full" />}
    </div>
  )
}

export default StyleTransfer
