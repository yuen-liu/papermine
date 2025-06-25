import React from 'react';

function Figures({ figures }) {
  if (!figures || figures.length === 0) return null;
  return (
    <section style={{ marginBottom: '2rem', background: '#f4f7fa', borderRadius: 8, padding: '1rem 1.2rem' }}>
      <h2 style={{ marginTop: 0 }}>Extracted Figures</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 16 }}>
        {figures.map((fig, idx) => (
          <div
            key={idx}
            style={{
              border: '1.5px solid #dbeafe',
              padding: 8,
              textAlign: 'center',
              borderRadius: 8,
              background: '#fff',
              boxShadow: '0 1px 2px #eee',
              transition: 'box-shadow 0.2s',
              width: 200,
            }}
          >
            <img src={fig.dataUrl} alt={`figure-${idx}`} style={{ maxWidth: 180, maxHeight: 180, display: 'block', margin: '0 auto 8px', borderRadius: 4 }} />
            <div style={{ color: '#1976d2', fontWeight: 500 }}><strong>Type:</strong> {fig.type}</div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Figures; 