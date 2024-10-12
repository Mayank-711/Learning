import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { greet as Greet } from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    <Greet />
  </React.StrictMode>
);

// Call the greet function outside of the render method
 // This will log the UTC hours to the console

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

