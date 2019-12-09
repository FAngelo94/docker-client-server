import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  console.log("APP");

  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  const myInit =
  {
    method: 'GET',
    headers: myHeaders,
    cache: 'default'
  };

  fetch('http://localhost:49160/get', myInit)
    .then(response => response.json())
    .then(res => {
      console.log(res);
    });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          TEST PROVA
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

// cd client
// docker run --name client_5 -i -d -v ${PWD}:/srv/app client /bin/bash
// docker exec -w /srv/app client_1 npm install
// docker exec -w /srv/app client_1 npm start