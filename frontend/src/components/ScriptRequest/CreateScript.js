import React, { useState } from 'react';
import api from '../../api';
import { Form, FormGroup, Label, Input, Textarea, Button, SmallHeading } from '../../styles';
import AutoResizingTextarea from './CodeBox';

function CreateScriptForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
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
          Authorization: `Token ${token}`,
        },
      });
      console.log(response.data);
      setFormValid(true);
      setCodeBody(response.data.generated_script.code);
    } catch (error) {
      console.error('Error:', error.response ? error.response.data : error);
      setFormValid(false);
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
      {/* Ensure the code body FormGroup is part of the overall structure */}
        <FormGroup>
          <SmallHeading>Code Body:</SmallHeading>
          <AutoResizingTextarea
            id="code"
            value={codeBody}
            readOnly // Set as readOnly if it's not meant to be edited
          ></AutoResizingTextarea>
        </FormGroup>
    </div>
  );
}

export default CreateScriptForm;
