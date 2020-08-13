import React from 'react';
import { AppRouter } from "./AppRouting";
import { BrowserRouter as Router } from "react-router-dom";
import setEnvironments from './environments';

function App() {
  //TODO import from seperate interface file
  let objUI = {
    "registered_devices": []
  };
  objUI["config"] = setEnvironments();


  return (
    <Router>
      <AppRouter objUI={objUI}/>
    </Router>
  );
}

export default App;
