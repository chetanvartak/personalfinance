import React from 'react';
import './Sidebar.css';

const Sidebar = ({ accounts }) => (
  <aside className="sidebar">
    <h2>Net Worth</h2>
    {accounts.map((group, idx) => (
      <div key={idx} className="account-group">
        <h4>{group.type}</h4>
        <ul>
          {group.items.map((acc, i) => (
            <li key={i} className="account-item">
              <div className="account-line">
                {acc.account_type && (
                  <span className="acc-type">{acc.account_type}</span>
                )}
                <span className="acc-name">{acc.name}</span>
                <span className="balance">${Number(acc.balance).toLocaleString(undefined, {minimumFractionDigits:2, maximumFractionDigits:2})}</span>
              </div>
            </li>
          ))}
        </ul>
      </div>
    ))}
  </aside>
);

export default Sidebar;
