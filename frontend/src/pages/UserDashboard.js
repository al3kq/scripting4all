import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';
import Scripts from '../components/ScriptRequest/ScriptList';
import {ScriptList, Paragraph, Container, Title, Button, Heading } from '../styles'; // Ensure imports are correct

function UserDashboard() {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [subscriptionStatus, setSubscriptionStatus] = useState('');
  const [scripts, setScripts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const storedUsername = localStorage.getItem('username');
    setUsername(storedUsername);
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await api.get('/api/users/dashboard/', {
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      setSubscriptionStatus(response.data.user.subscription_status);
      setScripts(response.data.scripts);
      setIsLoading(false);
      setError(null);
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
      setError(`Failed to fetch dashboard data. ${error}`);
      setIsLoading(false);
    }
  };

  const handleCreateScriptClick = () => {
    navigate('/script-request');
  };

  const handleSubscribe = async () => {
    try {
      const token = localStorage.getItem('token');
      // Fetch the session ID from your backend
      const response = await api.post('/api/users/subscribe/', {}, {
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      const session = response.data;
      console.log(session.sessionId);
  
      if (response.status == 200) {
        // Assuming you have the Stripe.js script loaded and Stripe object initialized
        const stripe = window.Stripe('pk_test_51PBmJ2ETTXwHh2RAKSuQQNxe8A22g5FmrDJPB4Kg2jqIkZ65j2eJWMtpEOQZ9cur9FPPOFJ2dVsIlWcO7EMU4BS000AtfVGov2');  // Use your Stripe public key
        // Redirect to Stripe Checkout
        const { error } = await stripe.redirectToCheckout({
          sessionId: session.sessionId,
        });
        if (error) {
          console.error('Stripe Checkout error:', error);
          setError(`Stripe Checkout error: ${error.message}`);
        }
      } else {
        console.log(session.error)
        throw new Error(session.error || 'Failed to create checkout session.');
      }
    } catch (error) {
      console.error('Error subscribing:', error);
      setError(`Error subscribing: ${error.message}`);
    }
  };
  
  const handleUnsubscribe = async () => {
    try {
      const token = localStorage.getItem('token');
      await api.post('/api/users/subscribe/', null, {
        headers: {
          Authorization: `Token ${token}`,
        },
      });
      setSubscriptionStatus('active');
      setError(null);
    } catch (error) {
      setError('Error subscribing:', error);
    }
  };

  const handleOpenScript = scriptId => {
    navigate(`/edit-script/${scriptId}`);
  };

  const handleDeleteScript = async (event,scriptId) => {
    event.stopPropagation();
    try {
      const token = localStorage.getItem('token');
      await api.delete(`/api/scripts/${scriptId}`, {
        headers: { Authorization: `Token ${token}` },
      });
      setScripts(currentScripts => currentScripts.filter(script => script.id !== scriptId));
      fetchDashboardData();
    } catch (error) {
      console.error('Error deleting script:', error);
    }
  };

  const sortedScripts = scripts.sort((a, b) => {
    // Convert date strings to date objects for comparison
    return new Date(b.created_at) - new Date(a.created_at); // Sort descending
    // Use new Date(a.created_at) - new Date(b.created_at) to sort ascending
  });

  const redirectToStripe = () => {
    window.location.href = 'https://buy.stripe.com/test_7sI3ey9W5enG556144';
  }

  return (
    <Container>
      <Title>User Dashboard</Title>
      <Paragraph>Welcome, {username}!</Paragraph>
      <Paragraph>Subscription Status: {subscriptionStatus}</Paragraph>
      {subscriptionStatus !== 'active' ? (
        <Button onClick={handleSubscribe}>Subscribe</Button>
      ):
      (
        <a href="https://buy.stripe.com/test_7sI3ey9W5enG556144" target="_blank" rel="noopener noreferrer">
          <Button>Unsubscribe</Button>
        </a>
      )}
      <Button onClick={handleCreateScriptClick}>Create Script</Button>
      <Heading>Your Script Requests:</Heading>
      {isLoading ? (
        <Paragraph>Loading...</Paragraph>
      ) : error ? (
        <Paragraph>Error: {error}</Paragraph>
      ) : scripts.length === 0 ? (
        <Paragraph>No scripts found.</Paragraph>
      ) : (
        <ScriptList>
          {sortedScripts.map(script => (
            <Scripts 
              key={script.id} 
              script={script} 
              onOpen={handleOpenScript} 
              onDelete={handleDeleteScript}
            />
          ))}
        </ScriptList>
      )}
    </Container>
  );
}

export default UserDashboard;
