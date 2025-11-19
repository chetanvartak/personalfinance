import { netWorthHistory, accounts, transactions } from './mockData';

export const fetchNetWorthHistory = () => Promise.resolve(netWorthHistory);
export const fetchAccounts = () => Promise.resolve(accounts);
export const fetchTransactions = () => Promise.resolve(transactions);
