import React from 'react';

function Home() {
  return (
    <div>
      <h1>Welcome to Script4All</h1>
      <p>Script4All is a web application that allows users to generate and execute scripts based on their requirements.</p>
      <h2>Features</h2>
      <ul>
        <li>User Registration and Authentication</li>
        <li>Script Request Submission</li>
        <li>AI-powered Script Generation</li>
        <li>Secure Script Execution</li>
      </ul>
      <h2>Get Started</h2>
      <p>To get started, please <a href="/user-management">register</a> for an account or <a href="/user-management">log in</a> if you already have one.</p>
    </div>
  );
}

export default Home;