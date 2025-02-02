import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AuthPage from './AuthPage'
import Dashboard from './Dashboard';

createRoot(document.getElementById('root')).render(
  <StrictMode>

<Router>
      <Routes>
        
        <Route path="/" element={<AuthPage />} />
        
        <Route path="/Dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
    
  </StrictMode>,
)
