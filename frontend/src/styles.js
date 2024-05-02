// styles.js
import React, { useRef, useEffect } from 'react';
import styled from 'styled-components';

export const Container = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
`;

export const Title = styled.h1`
  font-size: 36px;
  color: #333;
  margin-bottom: 20px;
  text-align: center; /* Center the text horizontally */
`;

export const Paragraph = styled.p`
  font-size: 18px;
  line-height: 1.5;
  margin-bottom: 20px;
`;

export const SmallParagraph = styled.p`
  font-size: 12px;
  line-height: 1.5;
  margin-bottom: 20px;
`;

export const Heading = styled.h2`
  font-size: 24px;
  color: #555;
  margin-bottom: 10px;
`;

export const SmallHeading = styled.h3`
  font-size: 18px;
  color: #555;
  margin-bottom: 10px;
`;

export const ScriptList = styled.ul`
display: grid;
grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); // Creates a responsive grid layout
gap: 20px; // Adds space between the grid items
list-style-type: none; // Removes bullet points
padding: 0;
`;

export const ScriptItem = styled.li`
  position: relative;
  background-color: #f4f4f4; // Gives a background color for better visibility
  border: 1px solid #ccc; // Adds a border
  padding: 20px;
  border-radius: 8px; // Rounds the corners
  box-shadow: 0 2px 5px rgba(0,0,0,0.1); // Adds a subtle shadow
  font-size: 16px;
  line-height: 1.5;

  cursor: pointer;
  &:hover {
    background-color: #f0f0f0; // Light grey background on hover for better UX
  }
`;

export const List = styled.ul`
  list-style-type: disc;
  margin-left: 20px;
  margin-bottom: 20px;
`;

export const ListItem = styled.li`
  font-size: 16px;
  line-height: 1.5;
`;

export const Link = styled.a`
  color: #007bff;
  text-decoration: none;

  &:hover {
    text-decoration: underline;
  }
`;

export const Form = styled.form`
  display: flex;
  flex-direction: column;
  max-width: 400px;
  margin: 0 auto;
`;

export const FormGroup = styled.div`
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
`;

export const Label = styled.label`
  font-size: 16px;
  margin-bottom: 5px;
`;

export const Input = styled.input`
  padding: 10px;
  font-size: 16px;
  border-radius: 4px;
  border: 1px solid #ccc;
`;

export const Button = styled.button`
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 10px; // Adds space to the right of each button

  &:hover {
    background-color: #0056b3;
  }

  &:last-child {
    margin-right: 0; // Removes margin from the last button
  }
`;

// Custom styled button for the delete action
export const DeleteButton = styled(Button)`
  background: transparent;
  border: none;
  cursor: pointer;
  position: absolute; // Position it relative to the parent if needed
  right: 10px; // Place it on the right
  top: 10px; // Place it on the top
  color: red; // Give it a red color or your choice

  &:hover {
    color: darkred; // Darken on hover
    background-color: red;
  }
`;


export const HeaderWrapper = styled.header`
  background-color: #333;
  padding: 20px;
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
  margin-right: 20px;

  &:last-child {
    margin-right: 0;
  }
`;

export const NavLink = styled.a`
  color: #fff;
  text-decoration: none;
  font-size: 18px;

  &:hover {
    text-decoration: underline;
  }
`;


export const Textarea = styled.textarea`
  padding: 10px;
  font-size: 16px;
  border-radius: 4px;
  border: 1px solid #ccc;
  resize: none;
  min-height: 100px;
`;

export const ErrorMessage = styled.p`
  color: red;
  font-size: 14px;
  margin-bottom: 10px;
`;