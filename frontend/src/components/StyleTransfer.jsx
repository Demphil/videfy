import React, { useState } from 'react';

export default function StyleTransfer() {
  const [image, setImage] = useState(null);
  const [styledImage, setStyledImage] = useState(null);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('image', file);

    const res = await fetch(`${import.meta.env.VITE_API_URL}/style-transfer`, {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    setStyledImage(data.styled_image_url);
  };

  return (
    <div className='mb-6'>
      <h2 className='text-xl mb-2'>نقل الأسلوب الفني</h2>
      <input type='file' accept='image/*' onChange={handleUpload} />
      {styledImage && <img src={styledImage} alt='Styled' className='mt-2' />}
    </div>
  );
}
