import React from 'react';
import './Sidebar.css';

const Sidebar = ({ accounts }) => (
  <aside className="sidebar">
    <h2>Net Worth</h2>
    {accounts.map((group, idx) => (
      <div key={idx} className="account-group">
        <h4>{group.type}</h4>
        <ul>
          {group.items.map((acc, i) =>
            <li key={i}>{acc.name}: <span className="balance">${acc.balance.toLocaleString()}</span></li>)}
        </ul>
      </div>
    ))}
  </aside>
);

export default Sidebar;
