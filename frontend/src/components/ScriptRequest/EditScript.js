import React, { useState, useEffect } from 'react';
import api from '../../api';
import { Form, FormGroup, Label, Input, Textarea, Button, SmallHeading } from '../../styles';
import AutoResizingTextarea from './CodeBox';
import { useParams } from 'react-router-dom';


function EditScriptForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [codeBody, setCodeBody] = useState('');
  const [formSubmitted, setFormSubmitted] = useState(false);
  const [formValid, setFormValid] = useState(false);
  const { scriptId } = useParams();

  useEffect(() => {
    const fetchScriptData = async () => {
      const token = localStorage.getItem('token');
      try {
        const response = await api.get(`/api/scripts/script-requests/${scriptId}/`, {
          headers: { Authorization: `Token ${token}` },
        });
        setTitle(response.data.script_request.title);
        setDescription(response.data.script_request.description);
        setCodeBody(response.data.generated_script.code)
      } catch (error) {
        console.error('Error fetching script:', error);
      }
    };

    fetchScriptData();
  }, [scriptId]);
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormSubmitted(true);

    const token = localStorage.getItem('token');
    if (!token) {
      console.error('No token found');
      return;
    }

    try {
      const response = await api.put(`/api/scripts/script-requests/${scriptId}/`, {
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

export default EditScriptForm;
