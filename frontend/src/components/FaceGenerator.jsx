import React, { useState } from 'react';

export default function FaceGenerator() {
  const [faceUrl, setFaceUrl] = useState(null);

  const generateFace = async () => {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/generate-face`);
    const data = await res.json();
    setFaceUrl(data.face_url);
  };

  return (
    <div className='mb-6'>
      <h2 className='text-xl mb-2'>توليد وجه وهمي</h2>
      <button onClick={generateFace} className='bg-green-500 text-white px-4 py-2'>توليد</button>
      {faceUrl && <img src={faceUrl} alt='Generated Face' className='mt-2' />}
    </div>
  );
}
