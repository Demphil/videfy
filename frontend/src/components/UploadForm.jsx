import React, { useState } from 'react';

function UploadForm() {
  const [videoURL, setVideoURL] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);

    const res = await fetch('https://your-backend-url.railway.app/process', {
      method: 'POST',
      body: formData,
    });

    const data = await res.json();
    setVideoURL(data.video_url);
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md">
        <input type="file" name="image" required />
        <textarea name="text" placeholder="Enter script" className="w-full my-2" required />
        <select name="language">
          <option value="en">English</option>
          <option value="ar">Arabic</option>
          <option value="ma">Darija</option>
        </select>
        <select name="quality" className="mx-2">
          <option value="720p">720p</option>
          <option value="1080p">1080p</option>
        </select>
        <button type="submit" className="bg-blue-500 text-white px-4 py-2">Generate</button>
      </form>
      {videoURL && (
        <div className="mt-4">
          <video controls width="640" src={videoURL}></video>
        </div>
      )}
    </div>
  );
}

export default UploadForm;
