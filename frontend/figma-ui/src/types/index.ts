export type Account = {
  id: string;
  name: string;
  type: 'checking' | 'savings' | 'credit' | 'investment';
  balance: number;
  lastUpdated: Date;
};

export type TransactionCategory = 
  | 'Groceries'
  | 'Dining'
  | 'Transportation'
  | 'Entertainment'
  | 'Healthcare'
  | 'Shopping'
  | 'Utilities'
  | 'Housing'
  | 'Income'
  | 'Transfer'
  | 'Other';

export type Transaction = {
  id: string;
  accountId: string;
  accountName: string;
  date: Date;
  description: string;
  category: TransactionCategory;
  amount: number;
  type: 'debit' | 'credit';
};

export type Budget = {
  id: string;
  category: TransactionCategory;
  limit: number;
  spent: number;
  period: 'monthly' | 'yearly';
};
