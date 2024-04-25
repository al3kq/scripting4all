import React from 'react';
import ScriptRequestForm from '../components/ScriptRequest/ScriptRequestForm';

function ScriptRequest() {
  // TODO: Check if the user is logged in
  const isLoggedIn = true; // Replace with actual login check

  if (!isLoggedIn) {
    // TODO: Redirect to login page or display error message
    return <div>Please log in to submit a script request.</div>;
  }

  return (
    <div>
      <h1>Script Request</h1>
      <ScriptRequestForm />
    </div>
  );
}

export default ScriptRequest;