import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import { calculator as Calculator } from "./App";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    <Calculator />
  </React.StrictMode>
);
