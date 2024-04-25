import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

function UserDashboard() {
  const navigate = useNavigate(); // Initialize useNavigate
  const username = localStorage.getItem('username');

  // Function to handle button click
  const handleCreateScriptClick = () => {
    navigate('/script-request'); // Navigate to the script request page
  };

  return (
    <div>
      <h1>User Dashboard</h1>
      <p>Welcome, {username}!</p>
      <button onClick={handleCreateScriptClick}>Create Script</button> {/* Button for script creation */}
    </div>
  );
}

export default UserDashboard;
