import React from 'react';
import { Switch, Route } from 'react-router-dom'
import LinkList from './components/LinkList'
import CreateLink from './components/CreateLink'
import Login from './components/Login'
import Header from './components/Header'


function App() {
  return (
    <div className="App">
      <Header />    
      <Switch>
        <Route exact path="/" component={LinkList} />
        <Route exact path="/create" component={CreateLink} />
        <Route exact path="/auth" component={Login} />
      </Switch>
    </div>
  );
}

export default App;
