// Header.js
import React from 'react';
import { HeaderWrapper, Nav, NavList, NavItem, NavLink } from '../styles';

function Header() {
  return (
    <HeaderWrapper>
      <Nav>
        <NavList>
          <NavItem>
            <NavLink href="/">Home</NavLink>
          </NavItem>
          <NavItem>
            <NavLink href="/dashboard">Dashboard</NavLink>
          </NavItem>
          <NavItem>
            <NavLink href="/register">Sign Up</NavLink>
          </NavItem>
          <NavItem>
            <NavLink href="/login">Login</NavLink>
          </NavItem>
          <NavItem>
            <NavLink href="/script-request">Script Request</NavLink>
          </NavItem>
        </NavList>
      </Nav>
    </HeaderWrapper>
  );
}

export default Header;