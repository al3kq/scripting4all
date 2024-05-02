import React from 'react';
import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe('your_publishable_key');

const PaymentForm = () => {
  const handleSubmit = async (event) => {
    event.preventDefault();

    const stripe = await stripePromise;

    try {
      const response = await fetch('/users/payments/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        console.log('Payment successful');
        // Handle successful payment
      } else {
        console.error('Payment failed');
        // Handle payment failure
      }
    } catch (error) {
      console.error('Error:', error);
      // Handle error
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Add your payment form fields here */}
      <button type="submit">Pay with Stripe</button>
    </form>
  );
};

export default PaymentForm;