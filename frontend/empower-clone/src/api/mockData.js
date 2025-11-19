export const netWorthHistory = [
  { date: '2025-11-01', value: 100000 },
  { date: '2025-11-10', value: 105000 },
  { date: '2025-11-18', value: 107200 }
];

export const accounts = [
  {
    type: 'Cash',
    items: [
      { name: 'Checking', balance: 5000 },
      { name: 'Savings', balance: 12000 }
    ]
  },
  {
    type: 'Investment',
    items: [
      { name: '401k', balance: 54000 },
      { name: 'IRA', balance: 21000 }
    ]
  }
];

export const transactions = [
  {
    date: '2025-11-17',
    description: 'Target Purchase',
    amount: -72.50,
    account: 'Checking'
  },
  {
    date: '2025-11-15',
    description: 'Paycheck',
    amount: 3100,
    account: 'Checking'
  }
];
