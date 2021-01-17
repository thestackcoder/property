import React, { Component, useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Project from './Project';

class App extends Component {
    render(){
        return (
            <Router>
              <div>
                <nav>
                  <ul>
                    <li>
                      <Link to="/">Home</Link>
                    </li>
                    <li>
                      <Link to="/projects">Projects</Link>
                    </li>
                  </ul>
                </nav>
        
                {/* A <Switch> looks through its children <Route>s and
                    renders the first one that matches the current URL. */}
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/projects" component={Project} />
                </Switch>
              </div>
            </Router>
        );
    }

}

function Home() {
    return <h2>Home</h2>;
}

export default App;

