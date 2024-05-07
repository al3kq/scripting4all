import React, { useState } from 'react';
import api from '../api';
import { useNavigate } from 'react-router-dom';  // Import useNavigate
import { Container, Title, Form, FormGroup, Label, Input, Button } from '../styles';

function Login({ onLogin }) {
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
      onLogin();
      navigate('/dashboard');  // Navigate to UserDashboard upon successful login
    } catch (error) {
      console.error('Error:', error);
      // Handle login error (e.g., display error message)
    }
  };

  return (
    <Container>
      <Title>Login</Title>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label htmlFor="username">Username:</Label>
          <Input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            autocomplete="username"
            required
          />
        </FormGroup>
        <FormGroup>
          <Label htmlFor="password">Password:</Label>
          <Input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autocomplete="current-password"
            required
          />
        </FormGroup>
        <Button type="submit">Login</Button>
      </Form>
    </Container>
  );
}

export default Login;