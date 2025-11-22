import { useState } from 'react';
import { Sidebar } from './components/Sidebar';
import { AccountsOverview } from './components/AccountsOverview';
import { TransactionsView } from './components/TransactionsView';
import { BudgetView } from './components/BudgetView';

export default function App() {
  const [currentView, setCurrentView] = useState<'accounts' | 'transactions' | 'budget'>('accounts');

  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar currentView={currentView} onViewChange={setCurrentView} />
      <main className="flex-1 overflow-auto">
        {currentView === 'accounts' && <AccountsOverview />}
        {currentView === 'transactions' && <TransactionsView />}
        {currentView === 'budget' && <BudgetView />}
      </main>
    </div>
  );
}
