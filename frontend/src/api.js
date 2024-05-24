import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  timeout: 500000,  // 5 minutes in milliseconds
});

export default api;