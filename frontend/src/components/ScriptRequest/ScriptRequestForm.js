import React, { useState } from 'react';
import api from '../../api';

function ScriptRequestForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('token');  // Retrieve the stored token
    if (!token) {
      console.error('No token found');
      return;  // Optionally handle the lack of a token (e.g., redirect to login)
    }
  
    try {
      const response = await api.post('/api/scripts/script-requests/', {
        title,
        description,
      }, {
        headers: {
          'Authorization': `Bearer ${token}`  // Use the token in the Authorization header
        }
      });
      console.log(response.data);
      // TODO: Handle successful script request submission
    } catch (error) {
      console.error('Error:', error.response ? error.response.data : error);
      // TODO: Handle error during script request submission
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="title">Title:</label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="description">Description:</label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        ></textarea>
      </div>
      <button type="submit">Submit Script Request</button>
    </form>
  );
}

export default ScriptRequestForm;