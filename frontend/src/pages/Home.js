import React from 'react';
import { Container, Title, Paragraph, Heading, List, ListItem, Link } from '../styles';

function Home() {
    return (
      <Container>
        <Title>Welcome to Script4All</Title>
        <Paragraph>
          Script4All is a web application that allows users to generate and execute scripts based on their requirements.
        </Paragraph>
        <Heading>Features</Heading>
        <List>
          <ListItem>AI-powered Python Script Generation</ListItem>
          <ListItem>Secure Script Execution</ListItem>
        </List>
        <Heading>Get Started</Heading>
        <Paragraph>
          To get started, please <Link href="/register">register</Link> for an account or{' '}
          <Link href="/login">log in</Link> if you already have one.
        </Paragraph>
      </Container>
    );
  }
  
  export default Home;