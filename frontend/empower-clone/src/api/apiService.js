import { netWorthHistory, accounts as mockAccounts, transactions } from './mockData';

export const fetchNetWorthHistory = () => Promise.resolve(netWorthHistory);

// Fetch accounts from backend REST endpoint and group by institution.name.
// Falls back to mock grouped data when fetch fails.
export const fetchAccounts = async () => {
	// Use relative URL in development so CRA proxy (package.json `proxy`) can avoid CORS.
	const url = process.env.NODE_ENV === 'development' ? '/api/v1/accounts/' : 'http://localhost:8000/api/v1/accounts/';
	try {
		const res = await fetch(url);
		if (!res.ok) throw new Error(`HTTP ${res.status}`);
		const data = await res.json();

		// group by institution.name
		const groupsMap = new Map();
		(data || []).forEach(acc => {
			const instName = (acc.institution && acc.institution.name) || 'Unknown';
			const item = {
				id: acc.id,
				name: acc.account_name,
				balance: Number(acc.balance) || 0,
				account_type: acc.account_type && acc.account_type.name ? acc.account_type.name : ''
			};
			if (!groupsMap.has(instName)) groupsMap.set(instName, []);
			groupsMap.get(instName).push(item);
		});

		return Array.from(groupsMap.entries()).map(([type, items]) => ({ type, items }));
	} catch (err) {
		// fallback: if mockAccounts already grouped by `type`, return as-is
		console.warn('fetchAccounts failed, falling back to mock accounts:', err);
		return Promise.resolve(mockAccounts);
	}
};

export const fetchTransactions = () => Promise.resolve(transactions);
