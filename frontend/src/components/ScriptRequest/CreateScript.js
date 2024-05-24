import React, { useState, useEffect} from 'react';
import api from '../../api';
import { Form, FormGroup, Label, Input, Textarea, Button, SmallHeading } from '../../styles';
import LoadingIndicator from './LoadingIndicator.js';
import AutoResizingTextarea from './CodeBox';
import { useNavigate } from 'react-router-dom';  // Import useNavigate

function CreateScriptForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [codeBody, setCodeBody] = useState('');
  const [formSubmitted, setFormSubmitted] = useState(false);
  const [formValid, setFormValid] = useState(false);
  const [activeTab, setActiveTab] = useState('index.html');
  const [fileContents, setFileContents] = useState({ 'index.html': '', 'style.css': '', 'script.js': '' });
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate(); 

  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormSubmitted(true);
    setLoading(true);

    const token = localStorage.getItem('token');
    if (!token) {
      console.error('No token found');
      setLoading(false);
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
      navigate(`/edit-script/${response.data.script_request.id}`);
    } catch (error) {
      console.error('Error:', error.response ? error.response.data : error);
      setFormValid(false);
    } finally {
      setLoading(false);
    }
  };
  const stripCodeBlocks = (code) => {
    return code.replace(/```(html|css|javascript)?\n/g, '').replace(/```/g, '');
  };

  const openInNewTab = (html, css, js) => {
      // Create a Blob for the CSS content
    const cssBlob = new Blob([css], { type: 'text/css' });
    const cssUrl = URL.createObjectURL(cssBlob);

    // Create a Blob for the JavaScript content
    const jsBlob = new Blob([js], { type: 'text/javascript' });
    const jsUrl = URL.createObjectURL(jsBlob);
    const fullHtml = `
      <!DOCTYPE html>
      <html>
      <head>
        <title>Preview</title>
        <style>${css}</style>
      </head>
      <body>
        ${html}
        <script>${js}</script>
      </body>
      </html>
    `;
    html = html.replace('style.css', cssUrl);
    html = html.replace('script.js', jsUrl);
    const blob = new Blob([html], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    window.open(url);
  };

  useEffect(() => {
    if (codeBody) {
      try {
        const codeObj = JSON.parse(codeBody);
        // const iframe = document.getElementById('webpage-iframe');
        const html = stripCodeBlocks(codeObj['index.html']);
        const css = stripCodeBlocks(codeObj['style.css']);
        const js = stripCodeBlocks(codeObj['script.js']);
        openInNewTab( html, css, js);
        setFileContents({ 'index.html': html, 'style.css': css, 'script.js': js });
      } catch (error) {
        console.error('Error parsing JSON:', error);
      }
    }
  }, [codeBody]);

  const handleFileContentChange = (e) => {
    const newFileContents = { ...fileContents, [activeTab]: e.target.value };
    setFileContents(newFileContents);
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
        <Button type="submit" disabled={loading}>
          {loading ? 'Submitting...This may take a few minutes' : 'Submit Script Request'}
        </Button>
      </Form>

      {loading && <LoadingIndicator>Loading...</LoadingIndicator>}

      {!loading && formSubmitted && (
        <div>
        <FormGroup>
          <SmallHeading>Code Body:</SmallHeading>
          <div>
              <button onClick={() => setActiveTab('index.html')}>index.html</button>
              <button onClick={() => setActiveTab('style.css')}>style.css</button>
              <button onClick={() => setActiveTab('script.js')}>script.js</button>
            </div>
            <AutoResizingTextarea
              id="code"
              value={fileContents[activeTab]}
              onChange={handleFileContentChange}

            ></AutoResizingTextarea>
        </FormGroup>
        </div>
      )}
    </div>
  );
}

export default CreateScriptForm;