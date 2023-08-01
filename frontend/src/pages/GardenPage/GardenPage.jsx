import React, { useState } from 'react';

// Component Imports
import AddGarden from '../../components/Garden/AddGarden/AddGarden';

// Style Imports
import './GardenPage.css';
// import * as Unicons from '@iconscout/react-unicons';
import { Button } from 'reactstrap';

export default function GardenPage() {
  const [showAddGarden, setShowAddGarden] = useState(false);

  // Show the AddGarden component function
  const showAddGardenComponent = () => {
    setShowAddGarden(!showAddGarden);
  }

  return (
    <div className='garden-page-container'>
      <h1>Garden Page</h1>
      <div className='garden-summary'>
        <div>Garden Summary</div>
      </div>
      <Button
        onClick={() => showAddGardenComponent()}
      >New Garden</Button>
      { showAddGarden ? <AddGarden /> : null}
    </div>
  );
}