import React, { useState } from 'react'
import axios from 'axios'

const UploadImage = () => {
  const [file, setFile] = useState(null)
  const [response, setResponse] = useState(null)

  const handleUpload = async () => {
    if (!file) return
    const formData = new FormData()
    formData.append('image', file)

    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/upload`, formData)
      setResponse(res.data)
    } catch (err) {
      console.error(err)
    }
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">📤 تحميل صورة</h2>
      <input type="file" accept="image/*" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload} className="mt-2 px-4 py-2 bg-blue-600 text-white rounded">
        رفع
      </button>
      {response && <pre className="mt-2 bg-gray-100 p-2">{JSON.stringify(response, null, 2)}</pre>}
    </div>
  )
}

export default UploadImage
