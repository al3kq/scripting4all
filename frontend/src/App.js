import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import UserRegistration from './pages/UserRegistration';
import Login from './pages/Login';
import AdminUserManagement from './pages/AdminUserManagement';
import ScriptRequest from './pages/ScriptRequest';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <main>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/register" component={UserRegistration} />
            <Route path="/login" component={Login} />
            <Route path="/admin/users" component={AdminUserManagement} />
            <Route path="/script-request" component={ScriptRequest} />
          </Switch>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;