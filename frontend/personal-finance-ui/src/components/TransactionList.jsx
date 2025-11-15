// src/components/TransactionList.jsx
import React, { useState, useEffect } from 'react';
import { getTransactions } from '../api/financeApi';

const TransactionList = () => {
  const [transactions, setTransactions] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTransactions = async () => {
      try {
        const response = await getTransactions();
        setTransactions(response.data);
      } catch (err) {
        setError('Failed to fetch transactions.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchTransactions();
  }, []);

  if (loading) return <p>Loading transactions...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div style={{ marginTop: '2rem' }}>
      <h2>Recent Transactions</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ borderBottom: '1px solid #ccc' }}>
            <th style={{ textAlign: 'left' }}>Date</th>
            <th style={{ textAlign: 'left' }}>Description</th>
            <th style={{ textAlign: 'left' }}>Category</th>
            <th style={{ textAlign: 'right' }}>Amount</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((tx) => (
            <tr key={tx.id} style={{ borderBottom: '1px solid #eee' }}>
              <td>{new Date(tx.date).toLocaleDateString()}</td>
              <td>{tx.description}</td>
              <td>{tx.category?.name || 'Uncategorized'}</td>
              <td style={{ textAlign: 'right', color: tx.transaction_type?.name === 'Debit' ? 'red' : 'green' }}>
                {new Intl.NumberFormat('en-US', {
                  style: 'currency',
                  currency: tx.currency || 'USD',
                }).format(tx.amount)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TransactionList;
