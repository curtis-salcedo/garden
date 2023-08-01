import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Routes, Route } from 'react-router-dom';

// Component Imports
import NavBar from '../../components/NavBar/NavBar';
import Footer from '../../components/Footer/Footer';

// Page Imports
import LandingPage from '../LandingPage/LandingPage';
import HomePage from '../HomePage/HomePage';
import ProfilePage from '../ProfilePage/ProfilePage';
import GardenPage from '../GardenPage/GardenPage';
import Dashboard from '../Dashboard/Dashboard';

// Utility Imports
import { getUser } from '../../utilities/getUser';

// Style Imports
import './App.css';

import { Button } from 'reactstrap';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    
  }, []);

  console.log(user)

  return (
    <div className="App">
      <NavBar />
      <h1>Main App</h1>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/garden" element={<GardenPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
