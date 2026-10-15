import { Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import ProblemList from './pages/ProblemList';
import ProblemPage from './pages/ProblemPage';

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<ProblemList />} />
        <Route path="/lists/:listId" element={<ProblemList />} />
        <Route path="/problems/:slug" element={<ProblemPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  );
}
