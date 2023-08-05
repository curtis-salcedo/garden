import React, { useEffect, useState } from 'react';

// Style Imports
import './ProfilePage.css';
// import * as Unicons from '@iconscout/react-unicons';
import {
  Form,
  FormGroup,
  Label,
  Input,
  InputGroup,
  FormText,
  Col,
  Button,
} from 'reactstrap';
import axios from 'axios';

export default function ProfilePage({ user }) {
  const [profile, setProfile] = useState({})

  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    bio: '',
    address: '',
    city: '',
    state: '',
    zip: '',
  });

  useEffect(() => {
    fetchProfileData()
  }, [])

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  }

  const fetchProfileData = () => {
    try {
      axios
        .get(`http://localhost:8000/api/profiles/${user.id}/`, { withCredentials: true })
        .then((res) => {
          setProfile(res.data)
        })
    } catch (err) {
      console.log('Error fetching profile data', err)
    }
  }

  const handleSubmit = (e) => {
    const addressData = {
      address: formData.address,
      city: formData.city,
      state: formData.state,
      zip: formData.zip,
    }

    const profileData = {
      first_name: formData.first_name,
      last_name: formData.last_name,
      bio: formData.bio,
    }

    
    e.preventDefault();
    // First post will create the profile to get the profile ID which will be used to save the second post of the address
    try {
      axios
      .put(`http://localhost:8000/api/profiles/${user.id}/`, profileData)
      .then((res) => {
          console.log('res, check res.data.id for being the right profile id', res)
        })
    } catch (err) {
      console.log('Error submitting profile data', err)
    }
  }

  return (
    <div className='profile-page-container'>
      <h1>Profile Page</h1>

      <FormGroup>
          <Label>Username: {user.username}</Label>
          <Label>Email: {user.email}</Label>
        <InputGroup>
          <Label for="first_name">First Name:</Label>
          <Input onChange={handleChange} type="text" name="first_name" id="first_name" placeholder={`${profile.first_name ? profile.first_name : 'First Name'}`} />
        </InputGroup>
        <InputGroup>
          <Label for="last_name">Last Name:</Label>
          <Input onChange={handleChange} type="text" name="last_name" id="last_name" placeholder={`${profile.last_name ? profile.last_name : 'Last Name'}`} />
        </InputGroup>
        <InputGroup>
          <Label for="bio">About:</Label>
          <Input onChange={handleChange} type="textarea" name="bio" id="bio" placeholder={`${profile.bio ? profile.bio : "More about you and your garden"}`} />
        </InputGroup>
        <InputGroup>
          <Label for="address">Address:</Label>
          <Input onChange={handleChange} type="text" name="address" id="address" placeholder="address" />
        </InputGroup>
        <InputGroup>
          <Label for="city">City:</Label>
          <Input onChange={handleChange} type="text" name="city" id="city" placeholder="City" />
        </InputGroup>
        <InputGroup>
          <Label for="state">State:</Label>
          <Input onChange={handleChange} type="text" name="state" id="state" placeholder="State" />
        </InputGroup>
        <InputGroup>
          <Label for="zip">Zip:</Label>
          <Input onChange={handleChange} type="text" name="zip" id="zip" placeholder="Zip" />
        </InputGroup>
        <Button onClick={handleSubmit}>Save</Button>
      </FormGroup>


      <div className='profile-container'>

        <div className='profile-image-container'>
          <img src='https://i.imgur.com/1qkYzX7.png' alt='profile' />
        </div>

        <div className='profile-info'>
          <h2>Username</h2>
          <h3>First Name</h3>
          <h3>Last Name</h3>
          <h3>Email</h3>
          <h3>Location</h3>
        </div>

      </div>

      <div className='profile-preferences'>
        <h2>Preferences</h2>


        <FormGroup>
          <InputGroup>
            <Label for="exampleSelect">Select</Label>
            <Input type="select" name="select" id="exampleSelect">
              <option>Option 1</option>
              <option>Option 2</option>
            </Input>
            <Label>
              <Input type="checkbox" />{' '}
              Checkbox
            </Label>
          </InputGroup>
        </FormGroup>


          <Form>
          <FormGroup row>
            <Label
              for="exampleEmail"
              sm={2}
            >
              Email
            </Label>
            <Col sm={10}>
              <Input
                id="exampleEmail"
                name="email"
                placeholder="with a placeholder"
                type="email"
              />
            </Col>
          </FormGroup>
          <FormGroup row>
            <Label
              for="examplePassword"
              sm={2}
            >
              Password
            </Label>
            <Col sm={10}>
              <Input
                id="examplePassword"
                name="password"
                placeholder="password placeholder"
                type="password"
              />
            </Col>
          </FormGroup>
          <FormGroup row>
            <Label
              for="exampleSelect"
              sm={2}
            >
              Select
            </Label>
            <Col sm={10}>
              <Input
                id="exampleSelect"
                name="select"
                type="select"
              >
                <option>
                  1
                </option>
                <option>
                  2
                </option>
                <option>
                  3
                </option>
                <option>
                  4
                </option>
                <option>
                  5
                </option>
              </Input>
            </Col>
          </FormGroup>
          <FormGroup row>
            <Label
              for="exampleSelectMulti"
              sm={2}
            >
              Select Multiple
            </Label>
            <Col sm={10}>
              <Input
                id="exampleSelectMulti"
                multiple
                name="selectMulti"
                type="select"
              >
                <option>
                  1
                </option>
                <option>
                  2
                </option>
                <option>
                  3
                </option>
                <option>
                  4
                </option>
                <option>
                  5
                </option>
              </Input>
            </Col>
          </FormGroup>
          <FormGroup row>
            <Label
              for="exampleText"
              sm={2}
            >
              Text Area
            </Label>
            <Col sm={10}>
              <Input
                id="exampleText"
                name="text"
                type="textarea"
              />
            </Col>
          </FormGroup>
          <FormGroup row>
            <Label
              for="exampleFile"
              sm={2}
            >
              File
            </Label>
            <Col sm={10}>
              <Input
                id="exampleFile"
                name="file"
                type="file"
              />
              <FormText>
                This is some placeholder block-level help text for the above input. It‘s a bit lighter and easily wraps to a new line.
              </FormText>
            </Col>
          </FormGroup>
          <FormGroup
            row
            tag="fieldset"
          >
            <legend className="col-form-label col-sm-2">
              Radio Buttons
            </legend>
            <Col sm={10}>
              <FormGroup check>
                <Input
                  name="radio2"
                  type="radio"
                />
                {' '}
                <Label check>
                  Option one is this and that—be sure to include why it‘s great
                </Label>
              </FormGroup>
              <FormGroup check>
                <Input
                  name="radio2"
                  type="radio"
                />
                {' '}
                <Label check>
                  Option two can be something else and selecting it will deselect option one
                </Label>
              </FormGroup>
              <FormGroup
                check
                disabled
              >
                <Input
                  disabled
                  name="radio2"
                  type="radio"
                />
                {' '}
                <Label check>
                  Option three is disabled
                </Label>
              </FormGroup>
            </Col>
          </FormGroup>
          <FormGroup row>
            <Label
              for="checkbox2"
              sm={2}
            >
              Checkbox
            </Label>
            <Col
              sm={{
                size: 10
              }}
            >
              <FormGroup check>
                <Input
                  id="checkbox2"
                  type="checkbox"
                />
                {' '}
                <Label check>
                  Check me out
                </Label>
              </FormGroup>
            </Col>
          </FormGroup>
          <FormGroup
            check
            row
          >
            <Col
              sm={{
                offset: 2,
                size: 10
              }}
            >
              <Button>
                Submit
              </Button>
            </Col>
          </FormGroup>
        </Form>


      </div>
    </div>
  );
}