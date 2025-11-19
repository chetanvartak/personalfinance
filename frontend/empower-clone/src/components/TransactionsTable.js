import React from 'react';
import './TransactionsTable.css';

const TransactionsTable = ({ transactions }) => (
  <table className="transactions-table">
    <thead>
      <tr>
        <th>Date</th>
        <th>Description</th>
        <th>Amount</th>
        <th>Account</th>
      </tr>
    </thead>
    <tbody>
      {transactions.map((tx, idx) => (
        <tr key={idx}>
          <td>{tx.date}</td>
          <td>{tx.description}</td>
          <td className={tx.amount < 0 ? 'negative' : 'positive'}>
            {tx.amount < 0 ? '-' : ''}${Math.abs(tx.amount).toFixed(2)}
          </td>
          <td>{tx.account}</td>
        </tr>
      ))}
    </tbody>
  </table>
);

export default TransactionsTable;
