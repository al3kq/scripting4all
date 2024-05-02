import React from 'react';
import EditScriptForm from '../components/ScriptRequest/EditScript';
import {ScriptList, Paragraph, Container, Title, Button, Heading } from '../styles'; // Ensure imports are correct
import { useParams } from 'react-router-dom';

function ScriptEdit() {
    const { scriptId } = useParams();
  // TODO: Check if the user is logged in
  const isLoggedIn = true; // Replace with actual login check

  if (!isLoggedIn) {
    // TODO: Redirect to login page or display error message
    return <div>Please log in to submit a script request.</div>;
  }

  return (
    <Container>
      <Title>Edit Script</Title>
      <EditScriptForm scriptId={scriptId}/>
    </Container>
  );
}

export default ScriptEdit;