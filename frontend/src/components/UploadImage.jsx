import React, { useState } from 'react';

function UploadImage({ onUpload }) {
  const [image, setImage] = useState(null);

  const handleChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
    onUpload(file);
  };

  return (
    <div className="upload-image">
      <input type="file" accept="image/*" onChange={handleChange} />
    </div>
  );
}

export default UploadImage;
