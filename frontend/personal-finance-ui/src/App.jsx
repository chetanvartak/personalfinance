// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <div style={{ padding: '20px', maxWidth: '1000px', margin: 'auto' }}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          {/* You can add more routes here later */}
          {/* <Route path="/accounts/:id" element={<AccountDetails />} /> */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
