import React from 'react';
import UserForm from '../components/UserManagement/UserForm';
import UserList from '../components/UserManagement/UserList';

function UserManagement({ onSignup }) {
  return (
      <UserForm onSignup={onSignup}/>
  );
}

export default UserManagement;