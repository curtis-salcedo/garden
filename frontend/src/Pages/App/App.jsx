import React from 'react';
import axios from 'axios';
import { Routes, Route } from 'react-router-dom';

// Component Imports
import NavBar from '../../Components/NavBar/NavBar';
import Footer from '../../Components/Footer/Footer';

// Page Imports
import LandingPage from '../LandingPage/LandingPage';
import HomePage from '../HomePage/HomePage';
import ProfilePage from '../ProfilePage/ProfilePage';
import GardenPage from '../GardenPage/GardenPage';

// Style Imports
import './App.css';

import { Button } from 'reactstrap';

function App() {
  return (
    <div className="App">
      <NavBar />
      <h1>Main App</h1>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/garden" element={<GardenPage />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
