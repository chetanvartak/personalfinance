// src/api/financeApi.js
import axios from 'axios';

// The backend is running on http://localhost:8000
// The API root is /api/v1
const financeApi = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
});

export const getAccounts = () => financeApi.get('/accounts/');
//export const getTransactions = () => financeApi.get('/transactions/');
export const getFilteredTransactions = (params) =>
  financeApi.get('/transactions/filtered/', { params });
// You can add more functions here as you build out the app
// export const searchTransactions = (params) => financeApi.post('/transactions/search', null, { params });
// export const createAccount = (accountData) => financeApi.post('/accounts/', accountData);

export default financeApi;
