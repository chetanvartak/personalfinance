// src/pages/Dashboard.jsx
import React from 'react';
import AccountList from '../components/AccountList';
import TransactionList from '../components/TransactionList';

const Dashboard = () => {
  return (
    <div>
      <h1>Personal Finance Dashboard</h1>
      <AccountList />
      <TransactionList />

    </div>
  );
};

export default Dashboard;
