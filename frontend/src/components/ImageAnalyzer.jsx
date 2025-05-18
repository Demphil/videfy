import React, { useState } from 'react';

export default function ImageAnalyzer() {
  const [caption, setCaption] = useState('');

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('image', file);

    const res = await fetch(`${import.meta.env.VITE_API_URL}/analyze-image`, {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    setCaption(data.caption);
  };

  return (
    <div className='mb-6'>
      <h2 className='text-xl mb-2'>تحليل الصورة</h2>
      <input type='file' accept='image/*' onChange={handleUpload} />
      {caption && <p className='mt-2'>{caption}</p>}
    </div>
  );
}
