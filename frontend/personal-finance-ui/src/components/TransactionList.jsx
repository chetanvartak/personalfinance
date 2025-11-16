import React, { useState, useEffect } from 'react';
import { getFilteredTransactions } from '../api/financeApi';

const TransactionList = () => {
  const [transactions, setTransactions] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  // Add these state values for filters
  const [search, setSearch] = useState('');
  const [sortBy, setSortBy] = useState('date');
  const [sortOrder, setSortOrder] = useState('desc');
  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(25);

const fetchTransactions = async () => {
  setLoading(true);
  try {
      const params = {
        page,
        page_size: pageSize,
        sort_by: sortBy,
        sort_order: sortOrder,
        search: search || undefined,
        // Add other filters here, e.g. account_id, category_id, date_from, date_to
      };
      
      const response = await getFilteredTransactions(params);
    // Defensive assignment
    console.log('API Response:', response.data);

    const txlist = Array.isArray(response.data.transactions)
      ? response.data.transactions
      : (Array.isArray(response.data) ? response.data : []);
    setTransactions(txlist);
    setError(null);
  } catch (err) {
    setError('Failed to fetch transactions.');
    setTransactions([]); // clear out old data on error
    console.error(err);
  } finally {
    setLoading(false);
  }
};


  useEffect(() => {
    fetchTransactions();
    // eslint-disable-next-line
  }, [search, sortBy, sortOrder, page, pageSize]); // rerun when filter values change

  if (loading) return <p>Loading transactions...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div style={{ marginTop: '2rem' }}>
      <h2>Recent Transactions</h2>
      {/* Controls for search, sorting, paging */}
      <div style={{ marginBottom: '1rem' }}>
        <input
          type="text"
          placeholder="Search..."
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
        <select value={sortBy} onChange={e => setSortBy(e.target.value)}>
          <option value="date">Date</option>
          <option value="amount">Amount</option>
          <option value="account_name">Account Name</option>
          <option value="category">Category</option>
        </select>
        <select value={sortOrder} onChange={e => setSortOrder(e.target.value)}>
          <option value="desc">Descending</option>
          <option value="asc">Ascending</option>
        </select>
        <input
          type="number"
          min="1"
          max="100"
          value={pageSize}
          onChange={e => setPageSize(Number(e.target.value))}
        />
        <button onClick={() => setPage(page > 1 ? page - 1 : 1)}>Prev</button>
        <span> Page {page} </span>
        <button onClick={() => setPage(page + 1)}>Next</button>
      </div>
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
