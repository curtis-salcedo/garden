import React, { useContext } from "react";
import axios from 'axios';

// Data Imports
import { logoutUser, login_url, signup_url } from "../../utilities/users-api"

// Component Imports
import NavBar from '../../components/NavBar/NavBar';

// Style Imports
import './AuthPage.css';
import {
  Button,
  Container,
  Card,
  CardHeader,
  CardBody,

} from 'reactstrap';


export default function AuthPage({ user }) {
  const login_url = 'http://localhost:8000/accounts/login';
  const logout_url = 'http://localhost:8000/accounts/logout';
  const signup_url = 'http://localhost:8000/accounts/signup';

  const handleLogout = (e) => {
    e.preventDefault();
    logoutUser(e);
  }

  const handleLogin = () => {
    window.location.href = 'http://localhost:8000/accounts/login';
  }

  return (
    <main className='auth-page-container'>
      { user ?
      <>
      <Container>
        <Card>
          <CardHeader>
            <h3 className='center'>Garden Name?</h3>
          </CardHeader>
          <CardBody className='center'>
            <div>
              Card Body
            </div>
          </CardBody>
        </Card>
      </Container>
      <div>User : {user.email}</div>
        <Button onClick={(e) => handleLogout(e)}>Logout</Button>
      </>
      :
      <>
      <Container className="auth-page-container">
        <Card className='login-card'>
        <div>
          <div className="NavBarContainer">
            <div className="NavBarLogo">
              <span className="NavBarOne">Garden</span> 
              <span className="NavBarTwo">Buddy</span>
            </div>
          </div>
        </div>
          <CardBody className='login-card-body'>
            Please login to your account
            <Button color='primary' size='lg' onClick={(e) => handleLogin(e)}>Login</Button>
          </CardBody>
        </Card>
        Don't have an account yet? <a href={signup_url}>Sign Up</a> here!
      </Container>
        </>
      }

    </main>
  );
}