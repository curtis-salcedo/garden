import React, { useState } from 'react';

// Style Imports
import './HomePage.css';
import * as Unicons from '@iconscout/react-unicons';
import {
  Row,
  Button,
  Card,
  CardTitle,
  CardText,
} from 'reactstrap';

export default function HomePage() {
  return (
    <div className='home-page-container'>

      <h1>Home Page</h1>

      <div className='home-page-weather-container'>

        <div className='weather-past-forecast'>
          <Card className='weather-card'>
            <CardTitle tag="h5">Past Weather 1</CardTitle>
            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
          </Card>
          <Card className='weather-card'>
            <CardTitle tag="h5">Past Weather 2</CardTitle>
            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
          </Card>
          <Card className='weather-card'>
            <CardTitle tag="h5">Past Weather 3</CardTitle>
            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
          </Card>
        </div>

        <div className='weather-current-forecast'>
          <Card className='weather-card'>
            <CardTitle tag="h5">Current Weather 1</CardTitle>
            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
          </Card>
        </div>

        <div className='weather-future-forecast'>
          <Card className='weather-card'>
            <CardTitle tag="h5">Future Weather 1</CardTitle>
            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
          </Card>
          <Card className='weather-card'>
            <CardTitle tag="h5">Future Weather 2</CardTitle>
            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
          </Card>
          <Card className='weather-card'>
            <CardTitle tag="h5">Future Weather 3</CardTitle>
            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
          </Card>
        </div>

        <div className='weather-suggestion-container'>
          <h2>Suggestions coming soon!</h2>
        </div>

      </div>

      <div className='home-page-garden'>
        <h2>Link to Garden Container</h2>
        <Button>View Garden</Button>
        <h2>Else this will show</h2>
        <Button>Create Your Garden</Button>
      </div>

      <div className='home-page-plant-container'>
        <h2>Link Plant Card Container Components</h2>
      </div>

    </div>
  );
}