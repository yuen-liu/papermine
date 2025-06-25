import React, { useState } from 'react';
import UploadForm from './components/UploadForm';
import Summary from './components/Summary';
import Tables from './components/Tables';
import Figures from './components/Figures';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ maxWidth: 800, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>Papermine: PDF Research Paper Extractor</h1>
      <div style={{ marginBottom: '1.5rem', color: '#444', background: '#f8f8f8', padding: '1rem', borderRadius: 8, fontSize: '1rem' }}>
        Upload a PDF research paper. The system will extract a summary, tables, and figures, and display them below.
      </div>
      <UploadForm setResult={setResult} />
      {result && (
        <>
          <Summary summary={result.summary} keywords={result.keywords} />
          <Tables tables={result.tables} />
          <Figures figures={result.figures} />
        </>
      )}
    </div>
  );
}

export default App; 