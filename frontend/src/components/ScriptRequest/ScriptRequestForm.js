import React, { useState } from 'react';
import api from '../../api';
import { Form, FormGroup, Label, Input, Textarea, Button } from '../../styles';

function ScriptRequestForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [inputValues, setInputValues] = useState('');
  const [codeBody, setCodeBody] = useState('');
  const [formSubmitted, setFormSubmitted] = useState(false);
  const [formValid, setFormValid] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormSubmitted(true);

    const token = localStorage.getItem('token');
    if (!token) {
      console.error('No token found');
      return;
    }

    try {
      const response = await api.post('/api/scripts/script-requests/', {
        title,
        description,
      }, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      console.log(response.data);
      setFormValid(true);
    } catch (error) {
      console.error('Error:', error.response ? error.response.data : error);
      setFormValid(false);
    }
  };

  const fetchInputValues = async () => {
    try {
      const response = await api.get('/api/scripts/input-values/');
      setInputValues(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const fetchCodeBody = async () => {
    try {
      const response = await api.get('/api/scripts/code-body/');
      setCodeBody(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label htmlFor="title">Title:</Label>
          <Input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </FormGroup>
        <FormGroup>
          <Label htmlFor="description">Description:</Label>
          <Textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          ></Textarea>
        </FormGroup>
        <Button type="submit">Submit Script Request</Button>
      </Form>

      {formSubmitted && (
        <div>
          {formValid ? (
            <div>
              <p>Form submitted successfully!</p>
              <Button onClick={fetchInputValues}>Get Input Values</Button>
              <Button onClick={fetchCodeBody}>Get Code Body</Button>
            </div>
          ) : (
            <p>Form submission failed. Please try again.</p>
          )}
        </div>
      )}

      {inputValues && (
        <div>
          <h3>Input Values:</h3>
          <p>{inputValues}</p>
        </div>
      )}

      {codeBody && (
        <div>
          <h3>Code Body:</h3>
          <pre>{codeBody}</pre>
        </div>
      )}
    </div>
  );
}

export default ScriptRequestForm;