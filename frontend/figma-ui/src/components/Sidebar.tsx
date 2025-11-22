import { Wallet, Receipt, PieChart, DollarSign } from 'lucide-react';

type SidebarProps = {
  currentView: 'accounts' | 'transactions' | 'budget';
  onViewChange: (view: 'accounts' | 'transactions' | 'budget') => void;
};

export function Sidebar({ currentView, onViewChange }: SidebarProps) {
  return (
    <div className="w-64 bg-white border-r border-gray-200 flex flex-col">
      <div className="p-6 border-b border-gray-200">
        <div className="flex items-center gap-2">
          <DollarSign className="size-8 text-blue-600" />
          <span className="text-xl text-gray-900">FinanceTracker</span>
        </div>
      </div>
      
      <nav className="flex-1 p-4">
        <ul className="space-y-2">
          <li>
            <button
              onClick={() => onViewChange('accounts')}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                currentView === 'accounts'
                  ? 'bg-blue-50 text-blue-700'
                  : 'text-gray-700 hover:bg-gray-50'
              }`}
            >
              <Wallet className="size-5" />
              <span>Accounts</span>
            </button>
          </li>
          <li>
            <button
              onClick={() => onViewChange('transactions')}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                currentView === 'transactions'
                  ? 'bg-blue-50 text-blue-700'
                  : 'text-gray-700 hover:bg-gray-50'
              }`}
            >
              <Receipt className="size-5" />
              <span>Transactions</span>
            </button>
          </li>
          <li>
            <button
              onClick={() => onViewChange('budget')}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                currentView === 'budget'
                  ? 'bg-blue-50 text-blue-700'
                  : 'text-gray-700 hover:bg-gray-50'
              }`}
            >
              <PieChart className="size-5" />
              <span>Budget</span>
            </button>
          </li>
        </ul>
      </nav>
      
      <div className="p-4 border-t border-gray-200">
        <div className="text-xs text-gray-500">
          Last updated: {new Date().toLocaleDateString()}
        </div>
      </div>
    </div>
  );
}
