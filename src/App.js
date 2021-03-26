import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect
} from "react-router-dom";
import logo from './assets/app-icon.png';
import './assets/main.css';
import './assets/bootstrap/css/bootstrap.min.css';
// pages
import Home from './Home';
/*
function App() {
  return (
    <Router>
      <div className="App">
        <div>
            <center>
                <img src={logo} alt="Classy Logo" height="64" width="64"></img>
            </center>
        </div>
        <Switch>
          <Route exact path="/">
            <Redirect to="/home"/>
          </Route>
          <Route path="/home">
            <Home/>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}
*/
class App extends React.Component {
  render() {
      return (
      <Router>
        <div className="App">
          <div>
              <center>
                  <img src={logo} alt="Classy Logo" height="64" width="64"></img>
              </center>
          </div>
          <Switch>
            <Route exact path="/">
              <Redirect to="/home"/>
            </Route>
            <Route path="/home">
              <Home name={this.props.name}/>
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}
export default App;
