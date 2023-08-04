import React, { useState } from 'react';

// Style Imports
import './LandingPage.css';
import * as Unicons from '@iconscout/react-unicons';
import {
  Row,
  Button,
  Card,
  CardTitle,
  CardText,
} from 'reactstrap';

export default function LandingPage() {
  return (
    <div className='landing-page-container'>
      <h1>Landing Page</h1>
      <div className='welcome-container'>
        <div>
          <img className='welcome-image' src="https://i.imgur.com/KRRgRiK.jpg" alt='welcomeimage' />
        </div>
        <h2 className="welcome-message">Welcome to Garden!</h2>
        <p>Welcome Text / Mission Statement
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
          facilisi. Donec euismod, nisl sed aliquam ultricies, nunc
          sapien ultricies diam, eu tincidunt nisl augue vitae enim. Nulla
          facilisi. Donec euismod, nisl sed aliquam ultricies, nunc</p>
      </div>

      <div className='about-container'>
        <h2 className='about-header'>About</h2>
        <p className='about-text'>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
          facilisi. Donec euismod, nisl sed aliquam ultricies, nunc
          sapien ultricies diam, eu tincidunt nisl augue vitae enim. Nulla
          facilisi. Donec euismod, nisl sed aliquam ultricies, nunc
          sapien ultricies diam, eu tincidunt nisl augue vitae enim.
          Nulla facilisi. Donec euismod, nisl sed aliquam ultricies, nunc</p>
        <Button>Get Started</Button>
      </div>

      <div className='how-container'>
        <h2>How it Works</h2>
        <div className='how-card-container'>
          <Card className='how-card'>
            <CardTitle>
              <h3>Step 1</h3>
            </CardTitle>
            <CardText>
              Sign up for an account
              <Unicons.UilUser size="100" color="#61DAFB" />
            </CardText>
          </Card>
            <Unicons.UilArrowRight size="100" color="#61DAFB" />
          <Card className='how-card'>
            <CardTitle>
              <h3>Step 2</h3>
            </CardTitle>
            <CardText>
              Build your garden
              <Unicons.UilFlower size="100" color="#61DAFB" />
            </CardText>
          </Card>
            <Unicons.UilArrowRight size="100" color="#61DAFB" />
          <Card className='how-card'>
            <CardTitle>
              <h3>Step 3</h3>
            </CardTitle>
            <CardText>
              Yield Results
              <Unicons.UilCheckCircle size="100" color="#61DAFB" />
            </CardText>
          </Card>
        </div>
      </div>


    </div>
  );
}