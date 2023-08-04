import React, { useState } from 'react';
import axios from 'axios';

// Style Imports
import './AddGarden.css';
import { Button, Form, FormGroup, Label, Input, FormText } from 'reactstrap';


export default function AddGarden() {
  const [newGarden, setNewGarden] = useState([])

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(newGarden);
    try {
      axios
        .post('api/gardens/', newGarden)
        .then((res) => {
          console.log(res);
          console.log(res.data);
        })
    } catch (err) {
      console.log('Error at submitting new garden via AddGarden.jsx', err)
    }
  };

  const handleChange = (e) => {
    console.log(e.target);
    setNewGarden({
      ...newGarden,
      [e.target.name]: e.target.value
    });
  }

  return (
    <div>
      <h1>Add Garden</h1>
      <Form>
        <FormGroup>
          <Label for="name">Garden Name</Label>
          <Input type="text" name="name" id="name" placeholder="Garden Name" onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label for="description">Garden Description</Label>
          <Input type="textarea" name="description" id="description" placeholder="Garden Description" onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label for="size_x">Garden Size X</Label>
          <Input type="number" name="size_x" id="size_x" placeholder="Garden Size X" onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label for="size_y">Garden Size Y</Label>
          <Input type="number" name="size_y" id="size_y" placeholder="Garden Size Y" onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label for="direction">Garden Direction</Label>
          <Input type="select" name="direction" id="direction" onChange={handleChange}>
            <option>North</option>
            <option>South</option>
            <option>East</option>
            <option>West</option>
          </Input>
        </FormGroup>
        <Button type='submit' onClick={handleSubmit} >Submit</Button>
      </Form>
    </div>
  );
}