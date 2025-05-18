import React, { useState } from 'react';

export default function ImageToVideo() {
  const [image, setImage] = useState(null);
  const [videoUrl, setVideoUrl] = useState(null);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('image', file);

    const res = await fetch(`${import.meta.env.VITE_API_URL}/image-to-video`, {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    setVideoUrl(data.video_url);
  };

  return (
    <div className='mb-6'>
      <h2 className='text-xl mb-2'>تحويل صورة إلى فيديو</h2>
      <input type='file' accept='image/*' onChange={handleUpload} />
      {videoUrl && <video controls src={videoUrl} className='mt-2' />}
    </div>
  );
}
