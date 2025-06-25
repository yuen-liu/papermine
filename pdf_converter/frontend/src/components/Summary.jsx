import React from 'react';

function Summary({ summary, keywords }) {
  return (
    <section style={{ marginBottom: '2rem', background: '#f4f7fa', borderRadius: 8, padding: '1rem 1.2rem' }}>
      <h2 style={{ marginTop: 0 }}>Summary</h2>
      <p style={{ fontSize: '1.08rem', color: '#222' }}>{summary}</p>
      {keywords && keywords.length > 0 && (
        <div style={{ marginTop: 8 }}>
          <strong>Keywords:</strong> <span style={{ color: '#1976d2' }}>{keywords.join(', ')}</span>
        </div>
      )}
    </section>
  );
}

export default Summary; 