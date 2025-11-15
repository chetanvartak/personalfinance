// src/components/AccountList.jsx
import React, { useState, useEffect } from 'react';
import { getAccounts } from '../api/financeApi';

const AccountList = () => {
  const [accounts, setAccounts] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAccounts = async () => {
      try {
        const response = await getAccounts();
        console.log('API Response:', response); // Log the whole response
        setAccounts(response.data);
      } catch (err) {
        setError('Failed to fetch accounts. Is the backend server running?');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchAccounts();
  }, []);

  if (loading) return <p>Loading accounts...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div>
      <h2>Accounts</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ borderBottom: '1px solid #ccc' }}>
            <th style={{ textAlign: 'left' }}>Name</th>
            <th style={{ textAlign: 'left' }}>Institution</th>
            <th style={{ textAlign: 'left' }}>Type</th>
            <th style={{ textAlign: 'right' }}>Balance</th>
          </tr>
        </thead>
        <tbody>
          {accounts.map((account) => (
            <tr key={account.id} style={{ borderBottom: '1px solid #eee' }}>
              <td>{account.account_name}</td>
              <td>{account.institution?.name || 'N/A'}</td>
              <td>{account.account_type?.name || 'N/A'}</td>
              <td style={{ textAlign: 'right' }}>
                {new Intl.NumberFormat('en-US', {
                  style: 'currency',
                  currency: account.currency,
                }).format(account.balance)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AccountList;
