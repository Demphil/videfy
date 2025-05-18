import React, { useState } from 'react';

export default function TextGenerator() {
  const [prompt, setPrompt] = useState('');
  const [output, setOutput] = useState('');

  const generateText = async () => {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/generate-text`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
    const data = await res.json();
    setOutput(data.output);
  };

  return (
    <div className='mb-6'>
      <h2 className='text-xl mb-2'>توليد نصوص</h2>
      <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} className='w-full p-2' rows='3'></textarea>
      <button onClick={generateText} className='bg-blue-500 text-white px-4 py-2 mt-2'>توليد</button>
      <p className='mt-2 whitespace-pre-wrap'>{output}</p>
    </div>
  );
}
