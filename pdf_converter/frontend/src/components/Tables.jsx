import React from 'react';

function Tables({ tables }) {
  if (!tables || tables.length === 0) return null;
  return (
    <section style={{ marginBottom: '2rem', background: '#f9fafb', borderRadius: 8, padding: '1rem 1.2rem' }}>
      <h2 style={{ marginTop: 0 }}>Extracted Tables</h2>
      {tables.map((table, idx) => (
        <table key={idx} border="1" cellPadding="4" style={{ marginBottom: 16, width: '100%', borderCollapse: 'collapse', background: '#fff', boxShadow: '0 1px 2px #eee' }}>
          <tbody>
            {table.map((row, rIdx) => (
              <tr key={rIdx} style={{ background: rIdx === 0 ? '#e3eaf6' : 'inherit', fontWeight: rIdx === 0 ? 600 : 400 }}>
                {row.map((cell, cIdx) => (
                  <td key={cIdx} style={{ padding: '6px 10px', border: '1px solid #e0e0e0' }}>{cell}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      ))}
    </section>
  );
}

export default Tables; 