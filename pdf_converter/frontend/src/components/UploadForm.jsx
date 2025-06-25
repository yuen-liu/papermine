import React, { useRef, useState } from 'react';

function UploadForm({ setResult }) {
  const fileInput = useRef();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    const file = fileInput.current.files[0];
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    try {
      const res = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData,
      });
      if (!res.ok) throw new Error('Upload failed');
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: '2rem', display: 'flex', alignItems: 'center', gap: 12 }}>
      <input type="file" accept="application/pdf" ref={fileInput} required style={{ padding: '6px 0' }} />
      <button
        type="submit"
        disabled={loading}
        style={{
          padding: '8px 18px',
          background: '#1976d2',
          color: '#fff',
          border: 'none',
          borderRadius: 4,
          cursor: loading ? 'not-allowed' : 'pointer',
          fontWeight: 500,
          fontSize: '1rem',
          transition: 'background 0.2s',
        }}
      >
        {loading ? 'Uploading...' : 'Upload PDF'}
      </button>
      {error && (
        <div style={{ color: '#b00020', marginTop: 8, background: '#ffeaea', padding: '6px 12px', borderRadius: 4, fontSize: '0.97rem' }}>{error}</div>
      )}
    </form>
  );
}

export default UploadForm; 