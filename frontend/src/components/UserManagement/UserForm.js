import React, { useState } from 'react';
import api from '../../api';
import { Form, FormGroup, Title, Container, Label, Input, Button } from '../../styles';

function UserForm() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/api/users/register/', {
        username,
        email,
        password,
      });
      console.log(response.data);
      // TODO: Handle successful user registration
    } catch (error) {
      console.error('Error:', error);
      // TODO: Handle error during user registration
    }
  };

  return (
    <Container>
        <Title>Sign Up</Title>
        <Form onSubmit={handleSubmit}>
        <FormGroup>
            <Label htmlFor="username">Username:</Label>
            <Input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            />
        </FormGroup>
        <FormGroup>
            <Label htmlFor="email">Email:</Label>
            <Input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
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
            required
            />
        </FormGroup>
        <Button type="submit">Register</Button>
        </Form>
    </Container>
  );
}

export default UserForm;