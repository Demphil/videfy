import React, { useState } from 'react';
import axios from 'axios';

export default function UploadForm() {
  const [file, setFile] = useState(null);
  const [script, setScript] = useState('');
  const [mode, setMode] = useState('image'); // image or script
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const formData = new FormData();
    if (mode === 'image') {
      formData.append('image', file);
    } else {
      formData.append('script', script);
    }

    try {
      const response = await axios.post('http://localhost:8080/process', formData);
      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert('حدث خطأ أثناء المعالجة.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-6 rounded shadow-md w-full max-w-md">
      <h2 className="text-xl font-bold mb-4">🎬 Videfy</h2>

      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label className="mr-4">
            <input
              type="radio"
              value="image"
              checked={mode === 'image'}
              onChange={() => setMode('image')}
            />
            صور
          </label>
          <label className="ml-4">
            <input
              type="radio"
              value="script"
              checked={mode === 'script'}
              onChange={() => setMode('script')}
            />
            سكربت نصي
          </label>
        </div>

        {mode === 'image' ? (
          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
            className="mb-4"
            required
          />
        ) : (
          <textarea
            value={script}
            onChange={(e) => setScript(e.target.value)}
            className="w-full border p-2 mb-4"
            rows={5}
            placeholder="أدخل السكربت النصي..."
            required
          />
        )}

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {loading ? 'جارٍ المعالجة...' : 'ابدأ المعالجة'}
        </button>
      </form>

      {result && (
        <div className="mt-4">
          <h3 className="font-bold text-lg">النتيجة:</h3>
          <pre className="bg-gray-100 p-2 mt-2 text-sm">{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
