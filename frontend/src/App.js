import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import UserManagement from './pages/UserManagement';
import Login from './pages/Login';
import AdminUserManagement from './pages/AdminUserManagement';
import ScriptRequest from './pages/ScriptRequest';
import UserDashboard from './pages/UserDashboard';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/register" element={<UserManagement />} />
            <Route path="/login" element={<Login />} />
            <Route path="/admin/users" element={<AdminUserManagement />} />
            <Route path="/script-request" element={<ScriptRequest />} />
            <Route path="/dashboard" element={<UserDashboard />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;