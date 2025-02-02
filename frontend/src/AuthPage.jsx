// src/components/AuthPage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'
import './AuthPage.css';
import Dashboard from './Dashboard';

function AuthPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();


  const handleSubmit = (event) => {
    event.preventDefault();

    // Mock login logic
    if (email === "test@test.com" && password === "12345") {
      
      navigate("/Dashboard"); // Redirect to dashboard
    } else {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="auth-container">
      <h2>Account Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Enter your password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default AuthPage;
