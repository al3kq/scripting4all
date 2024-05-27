// styles.js
import React, { useRef, useEffect } from 'react';
import styled from 'styled-components';

export const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px;
  background-color: #f8f9fa;
`;

export const Title = styled.h1`
  font-size: 48px;
  color: #2c3e50;
  margin-bottom: 30px;
  text-align: center;
  font-weight: bold;
`;

export const Paragraph = styled.p`
  font-size: 20px;
  line-height: 1.6;
  margin-bottom: 30px;
  color: #34495e;
`;

export const SmallParagraph = styled.p`
  font-size: 14px;
  line-height: 1.6;
  margin-bottom: 20px;
  color: #7f8c8d;
`;

export const Heading = styled.h2`
  font-size: 32px;
  color: #2c3e50;
  margin-bottom: 20px;
  font-weight: bold;
`;

export const SmallHeading = styled.h3`
  font-size: 24px;
  color: #34495e;
  margin-bottom: 15px;
  font-weight: bold;
`;

export const ScriptList = styled.ul`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
  list-style-type: none;
  padding: 0;
`;

export const ScriptItem = styled.li`
  position: relative;
  background-color: #fff;
  border: none;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  font-size: 18px;
  line-height: 1.6;
  cursor: pointer;
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
  }
`;

export const List = styled.ul`
  list-style-type: disc;
  margin-left: 30px;
  margin-bottom: 30px;
`;

export const ListItem = styled.li`
  font-size: 18px;
  line-height: 1.6;
  color: #34495e;
`;

export const Link = styled.a`
  color: #3498db;
  text-decoration: none;
  transition: color 0.3s ease;

  &:hover {
    color: #2980b9;
  }
`;

export const Form = styled.form`
  display: flex;
  flex-direction: column;
  max-width: 500px;
  margin: 0 auto;
  background-color: #fff;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
`;

export const FormGroup = styled.div`
  margin-bottom: 30px;
  display: flex;
  flex-direction: column;
`;

export const Label = styled.label`
  font-size: 18px;
  margin-bottom: 10px;
  color: #2c3e50;
`;

export const Input = styled.input`
  padding: 15px;
  font-size: 18px;
  border-radius: 6px;
  border: 1px solid #bdc3c7;
  transition: border-color 0.3s ease;

  &:focus {
    border-color: #3498db;
    outline: none;
  }
`;

export const PasswordInput = styled.input`
  padding: 15px;
  font-size: 18px;
  border-radius: 6px;
  border: 1px solid #bdc3c7;
  transition: border-color 0.3s ease;

  &:focus {
    border-color: #3498db;
    outline: none;
  }
`;
export const Button = styled.button`
  padding: 15px 30px;
  font-size: 18px;
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-right: 15px;

  &:hover {
    background-color: #2980b9;
  }

  &:last-child {
    margin-right: 0;
  }
`;

export const SmallButton = styled(Button)`
  padding: 10px 20px;
  font-size: 14px;
`;

export const DeleteButton = styled(Button)`
  background: transparent;
  border: none;
  cursor: pointer;
  position: absolute;
  right: 15px;
  top: 15px;
  color: #e74c3c;
  transition: color 0.3s ease;

  &:hover {
    color: #c0392b;
  }
`;

export const HeaderWrapper = styled.header`
  background-color: #2c3e50;
  padding: 30px;
`;

export const Nav = styled.nav`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

export const NavList = styled.ul`
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
`;

export const NavItem = styled.li`
  margin-right: 30px;

  &:last-child {
    margin-right: 0;
  }
`;

export const LogoutItem = styled.li`
  margin-left: auto;
`;

export const NavLink = styled.a`
  color: #fff;
  text-decoration: none;
  font-size: 20px;
  transition: color 0.3s ease;

  &:hover {
    color: #3498db;
  }
`;

export const Textarea = styled.textarea`
  padding: 15px;
  font-size: 18px;
  border-radius: 6px;
  border: 1px solid #bdc3c7;
  resize: none;
  min-height: 150px;
  transition: border-color 0.3s ease;

  &:focus {
    border-color: #3498db;
    outline: none;
  }
`;

export const ErrorMessage = styled.p`
  color: #e74c3c;
  font-size: 16px;
  margin-bottom: 15px;
`;