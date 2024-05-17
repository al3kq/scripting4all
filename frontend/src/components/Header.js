// Header.js
import React from 'react';
import { HeaderWrapper,LogoutItem, Nav, NavList, NavItem, NavLink } from '../styles';

function Header({ isLoggedIn, onLogout }) {
  return (
    <HeaderWrapper>
      <Nav>
          {isLoggedIn && (
            <>
            <NavList>
              <NavItem>
                <NavLink href="/">Home</NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="/dashboard">Dashboard</NavLink>
              </NavItem>
                <NavItem>
                <NavLink href="/script-request">Build a new Site</NavLink>
              </NavItem>
            </NavList>
            <LogoutItem>
              <NavLink onClick={onLogout} href="/">Logout</NavLink>
            </LogoutItem>
            </>
          )}
          {!isLoggedIn && (
            <>
            <NavList>
              <NavItem>
                <NavLink href="/">Home</NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="/register">Sign Up</NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="/login">Login</NavLink>
              </NavItem>
            </NavList>
            </>
          )}
      </Nav>
    </HeaderWrapper>
  );
}

export default Header;