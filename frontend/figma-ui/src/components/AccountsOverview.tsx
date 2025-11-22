import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { mockAccounts } from '../lib/mockData';
import { TrendingUp, TrendingDown, Wallet, CreditCard, Landmark, LineChart } from 'lucide-react';

export function AccountsOverview() {
  const totalBalance = mockAccounts.reduce((sum, account) => sum + account.balance, 0);
  const totalAssets = mockAccounts
    .filter(a => a.balance > 0)
    .reduce((sum, account) => sum + account.balance, 0);
  const totalLiabilities = Math.abs(
    mockAccounts
      .filter(a => a.balance < 0)
      .reduce((sum, account) => sum + account.balance, 0)
  );

  const getAccountIcon = (type: string) => {
    switch (type) {
      case 'checking':
      case 'savings':
        return <Wallet className="size-5 text-blue-600" />;
      case 'credit':
        return <CreditCard className="size-5 text-orange-600" />;
      case 'investment':
        return <LineChart className="size-5 text-green-600" />;
      default:
        return <Landmark className="size-5 text-gray-600" />;
    }
  };

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
    }).format(amount);
  };

  return (
    <div className="p-8">
      <div className="mb-8">
        <h1 className="text-3xl text-gray-900 mb-2">Accounts Overview</h1>
        <p className="text-gray-600">Manage and monitor all your financial accounts</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <Card>
          <CardHeader>
            <CardTitle className="text-sm text-gray-600">Total Net Worth</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl text-gray-900 mb-2">{formatCurrency(totalBalance)}</div>
            <div className="flex items-center gap-1 text-sm text-green-600">
              <TrendingUp className="size-4" />
              <span>+2.4% this month</span>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-sm text-gray-600">Total Assets</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl text-gray-900 mb-2">{formatCurrency(totalAssets)}</div>
            <div className="flex items-center gap-1 text-sm text-green-600">
              <TrendingUp className="size-4" />
              <span>+1.8% this month</span>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-sm text-gray-600">Total Liabilities</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl text-gray-900 mb-2">{formatCurrency(totalLiabilities)}</div>
            <div className="flex items-center gap-1 text-sm text-red-600">
              <TrendingDown className="size-4" />
              <span>+5.2% this month</span>
            </div>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>All Accounts</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {mockAccounts.map((account) => (
              <div
                key={account.id}
                className="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
              >
                <div className="flex items-center gap-4">
                  <div className="p-3 bg-gray-50 rounded-lg">
                    {getAccountIcon(account.type)}
                  </div>
                  <div>
                    <div className="text-gray-900">{account.name}</div>
                    <div className="text-sm text-gray-500 capitalize">{account.type} Account</div>
                  </div>
                </div>
                <div className="text-right">
                  <div className={`text-lg ${account.balance < 0 ? 'text-red-600' : 'text-gray-900'}`}>
                    {formatCurrency(Math.abs(account.balance))}
                  </div>
                  <div className="text-sm text-gray-500">
                    Updated {account.lastUpdated.toLocaleDateString()}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
