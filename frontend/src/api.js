import axios from 'axios';

const api = axios.create({
  baseURL: 'http://104.236.8.173:4242', // Replace with your backend API URL
});

export default api;