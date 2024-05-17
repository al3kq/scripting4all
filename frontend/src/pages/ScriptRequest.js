import React from 'react';
import CreateScriptForm from '../components/ScriptRequest/CreateScript';
import {ScriptList, Paragraph, Container, Title, Button, Heading } from '../styles'; // Ensure imports are correct

function ScriptRequest() {
  // TODO: Check if the user is logged in
  const isLoggedIn = true; // Replace with actual login check

  if (!isLoggedIn) {
    // TODO: Redirect to login page or display error message
    return <div>Please log in to submit a script request.</div>;
  }

  return (
    <Container>
      <Title>New Site</Title>
      <CreateScriptForm />
    </Container>
  );
}

export default ScriptRequest;