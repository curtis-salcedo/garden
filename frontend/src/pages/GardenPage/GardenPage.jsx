import React, { useState } from 'react';

// Style Imports
import './GardenPage.css';
// import * as Unicons from '@iconscout/react-unicons';
import { Button } from 'reactstrap';

export default function GardenPage() {

  return (
    <div className='garden-page-container'>
      <h1>Garden Page</h1>
      <div className='garden-summary'>
        <div>Garden Summary</div>
      </div>
      <Button
        onClick={() => console.log('New Garden')}
      >New Garden</Button>
    </div>
  );
}