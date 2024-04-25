import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/register">User Registration</Link>
          </li>
          <li>
            <Link to="/login">Login</Link>
          </li>
          <li>
            <Link to="/script-request">Script Request</Link>
          </li>
          {/* Add a conditional rendering for admin users */}
          {isAdmin && (
            <li>
              <Link to="/admin/users">Admin User Management</Link>
            </li>
          )}
        </ul>
      </nav>
    </header>
  );
}

export default Header;