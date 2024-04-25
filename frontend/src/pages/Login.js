import React, { useState } from 'react';
import api from '../api';
import { useNavigate } from 'react-router-dom';  // Import useNavigate

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();  // Initialize useNavigate

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/api/users/login/', {
        username,
        password,
      });
      localStorage.setItem('username', username);
      localStorage.setItem('token', response.data.token)
      // Handle successful login (e.g., store token)
      // Redirect to dashboard
      navigate('/dashboard');  // Navigate to UserDashboard upon successful login
    } catch (error) {
      console.error('Error:', error);
      // Handle login error (e.g., display error message)
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
