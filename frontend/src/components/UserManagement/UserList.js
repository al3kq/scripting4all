import React, { useEffect, useState } from 'react';
import api from '../../api';


function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await api.get('/api/users/');
        setUsers(response.data);
      } catch (error) {
        console.error('Error:', error);
        // TODO: Handle error while fetching users
      }
    };

    fetchUsers();
  }, []);

  return (
    <div>
      <h2>User List</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.username}</li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;