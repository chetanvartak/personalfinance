import React from 'react';
import NetWorthChart from './NetWorthChart';
import TransactionsTable from './TransactionsTable';
import './Overview.css';

const Overview = ({ netWorthData, transactions }) => (
  <main className="overview">
    <section className="net-worth-section">
      <h3>Net Worth Trend</h3>
      <NetWorthChart data={netWorthData}/>
    </section>
    <section className="transactions-section">
      <h3>Recent Transactions</h3>
      <TransactionsTable transactions={transactions}/>
    </section>
  </main>
);

export default Overview;
