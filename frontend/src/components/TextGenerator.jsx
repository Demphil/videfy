import React, { useState } from 'react'
import axios from 'axios'

const TextGenerator = () => {
  const [prompt, setPrompt] = useState('')
  const [generated, setGenerated] = useState('')

  const handleGenerate = async () => {
    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/generate-text`, { prompt })
      setGenerated(res.data.text)
    } catch (err) {
      console.error(err)
    }
  }

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">✍️ توليد سكربت فيديو من فكرة</h2>
      <input
        type="text"
        value={prompt}
        onChange={e => setPrompt(e.target.value)}
        placeholder="أدخل فكرتك..."
        className="border p-2 w-full"
      />
      <button onClick={handleGenerate} className="mt-2 px-4 py-2 bg-purple-600 text-white rounded">
        توليد
      </button>
      {generated && <p className="mt-2 bg-gray-100 p-2">{generated}</p>}
    </div>
  )
}

export default TextGenerator
