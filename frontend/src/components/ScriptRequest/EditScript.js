import React, { useState, useEffect } from 'react';
import api from '../../api';
import { Form, FormGroup, Label, Input, Textarea, Button, SmallHeading } from '../../styles';
import AutoResizingTextarea from './CodeBox';
import { useParams } from 'react-router-dom';
import LoadingIndicator from './LoadingIndicator';

function EditScriptForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [codeBody, setCodeBody] = useState('');
  const [formSubmitted, setFormSubmitted] = useState(false);
  const [formValid, setFormValid] = useState(false);
  const [activeTab, setActiveTab] = useState('index.html');
  const [fileContents, setFileContents] = useState({ 'index.html': '', 'styles.css': '', 'script.js': '' });
  const [loading, setLoading] = useState(false);
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
        setCodeBody(response.data.generated_script.code);
      } catch (error) {
        console.error('Error fetching script:', error);
      }
    };
    fetchScriptData();
  }, [scriptId]);

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
    } finally {
      setLoading(false);
    }
  };

  const stripCodeBlocks = (code) => {
    return code.replace(/```(html|css|javascript)?\n/g, '').replace(/```/g, '');
  };
  const injectContent = (iframe, html, css, js) => {
    const doc = iframe.contentDocument || iframe.contentWindow.document;
    doc.open();
    doc.write(html);
    doc.close();
    
    const style = doc.createElement('style');
    style.innerHTML = css;
    doc.head.appendChild(style);
    
    const script = doc.createElement('script');
    script.innerHTML = js;
    doc.body.appendChild(script);
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
        setFileContents({ 'index.html': html, 'styles.css': css, 'script.js': js });
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
          {loading ? 'Submitting...' : 'Submit Script Request'}
        </Button>
      </Form>

      {loading && <LoadingIndicator />}

      {!loading && (
        <div>
          <FormGroup>
            <SmallHeading>Code Body:</SmallHeading>
            <div>
              <button onClick={() => setActiveTab('index.html')}>index.html</button>
              <button onClick={() => setActiveTab('styles.css')}>styles.css</button>
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

export default EditScriptForm;