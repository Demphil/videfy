import React, { useState } from 'react';

function UploadForm() {
  const [videoURL, setVideoURL] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setVideoURL(null);

    const form = e.target;
    const formData = new FormData(form);

    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/create-video`, {
        method: 'POST',
        body: formData,
      });

      if (!res.ok) {
        throw new Error('فشل في إنشاء الفيديو');
      }

      const data = await res.json();
      setVideoURL(data.video_url);
    } catch (err) {
      setError(err.message || 'حدث خطأ غير متوقع');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto mt-10">
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md">
        <input type="file" name="image" required className="block mb-2" />
        <textarea name="text" placeholder="أدخل السكريبت" className="w-full mb-2 p-2 border rounded" required />
        
        <div className="flex items-center mb-4">
          <select name="language" className="mr-2 p-2 border rounded">
            <option value="en">English</option>
            <option value="ar">العربية</option>
            <option value="ma">الدارجة</option>
          </select>
          <select name="quality" className="p-2 border rounded">
            <option value="720p">720p</option>
            <option value="1080p">1080p</option>
          </select>
        </div>

        <button 
          type="submit"
          className={`bg-blue-600 text-white px-4 py-2 rounded ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
          disabled={loading}
        >
          {loading ? 'جاري المعالجة...' : 'إنشاء الفيديو'}
        </button>

        {error && <p className="text-red-500 mt-2">{error}</p>}
      </form>

      {videoURL && (
        <div className="mt-6">
          <h2 className="mb-2 font-semibold">📽️ فيديوك الجاهز:</h2>
          <video controls width="100%" src={videoURL} className="rounded border" />
        </div>
      )}
    </div>
  );
}

export default UploadForm;
