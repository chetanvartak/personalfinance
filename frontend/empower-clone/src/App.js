import React, { useEffect, useState } from 'react';
import { fetchNetWorthHistory, fetchAccounts, fetchTransactions } from './api/apiService';
import Sidebar from './components/Sidebar';
import Overview from './components/Overview';
import './App.css';

function App() {
  const [netWorthData, setNetWorthData] = useState([]);
  const [accounts, setAccounts] = useState([]);
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetchNetWorthHistory().then(setNetWorthData);
    fetchAccounts().then(setAccounts);
    fetchTransactions().then(setTransactions);
  }, []);

  return (
    <div className="app-layout">
      <Sidebar accounts={accounts}/>
      <Overview netWorthData={netWorthData} transactions={transactions}/>
    </div>
  );
}

export default App;
