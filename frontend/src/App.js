import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate, Outlet } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import UserManagement from './pages/UserManagement';
import Login from './pages/Login';
import AdminUserManagement from './pages/AdminUserManagement';
import ScriptRequest from './pages/ScriptRequest';
import ScriptEdit from './pages/ScriptEdit';
import UserDashboard from './pages/UserDashboard';

// PrivateRoute component
const PrivateRoute = () => {
  const token = localStorage.getItem('token');
  return token ? <Outlet /> : <Navigate to="/login" replace />;
};

const isLoggedIn = () => {
  const token = localStorage.getItem('token');
  return token ? true : false;
}


function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Check if the token exists in local storage
    const token = localStorage.getItem('token');

    if (token) {
      setIsLoggedIn(true);
    } else {
      setIsLoggedIn(false);
    }
  }, []);

  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    // Remove the token from local storage
    localStorage.removeItem('token');
    // Update the isLoggedIn state to false
    setIsLoggedIn(false);
  };
  return (
    <Router>
      <div className="App">
        <Header isLoggedIn={isLoggedIn} onLogout={handleLogout}/>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/register" element={<UserManagement onSignup={handleLogin}/>} />
            <Route path="/login" element={<Login onLogin={handleLogin}/>} />
            <Route path="/success" component={SuccessPage} />
            <Route path="/cancel" component={CancelPage} />
            <Route path="/script-request" element={<PrivateRoute />}>
              <Route path="" element={<ScriptRequest />} />
            </Route>
            <Route path="/edit-script" element={<PrivateRoute />}>
              <Route path=":scriptId" element={<ScriptEdit />} />
            </Route>
            <Route path="/dashboard" element={<PrivateRoute />}>
              <Route path="" element={<UserDashboard />} />
            </Route>
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;

function SuccessPage() {
  // Handle the successful checkout scenario
  return <div>Checkout successful!</div>;
}

function CancelPage() {
  // Handle the canceled checkout scenario
  return <div>Checkout canceled.</div>;
}