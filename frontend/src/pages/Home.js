import React from 'react';
import { Container, Title, Paragraph, Heading, List, ListItem, Link } from '../styles';

function Home() {
    return (
      <Container>
        <Title>Welcome to Web4All</Title>
        <Paragraph>
          Web4All allows users to generate and use websites created with the assistance of AI.
        </Paragraph>
        <Heading>Features</Heading>
        <List>
          <ListItem>AI-powered Website Script Generation</ListItem>
          <ListItem>Secure Website Execution</ListItem>
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