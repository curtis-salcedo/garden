import React from 'react';

// Style Imports
import './Footer.css';
import {
  List,
  ListInlineItem,
  ListGroup,
  ListGroupItem,

} from 'reactstrap';

export default function Footer() {
  return (
    <div className='footer-container'>
      <div className='footer-upper'> 

        <div className='footer-list-left'>
          <h5>Footer List Left</h5>
          <ListGroup flush>
            <ListGroupItem
              disabled
              href="#"
              tag="a"
            >
              Cras justo odio
            </ListGroupItem>
            <ListGroupItem
              href="#"
              tag="a"
            >
              Dapibus ac facilisis in
            </ListGroupItem>
            <ListGroupItem
              href="#"
              tag="a"
            >
              Morbi leo risus
            </ListGroupItem>
          </ListGroup>
        </div>

        <div className='footer-list-center'>
          <h5>Footer List Left</h5>
          <ListGroup flush>
            <ListGroupItem
              disabled
              href="#"
              tag="a"
            >
              Cras justo odio
            </ListGroupItem>
            <ListGroupItem
              href="#"
              tag="a"
            >
              Dapibus ac facilisis in
            </ListGroupItem>
            <ListGroupItem
              href="#"
              tag="a"
            >
              Morbi leo risus
            </ListGroupItem>
          </ListGroup>
        </div>

        <div className='footer-list-right'>
          <h5>Footer List Left</h5>
          <ListGroup flush>
            <ListGroupItem
              disabled
              href="#"
              tag="a"
            >
              Cras justo odio
            </ListGroupItem>
            <ListGroupItem
              href="#"
              tag="a"
            >
              Dapibus ac facilisis in
            </ListGroupItem>
            <ListGroupItem
              href="#"
              tag="a"
            >
              Morbi leo risus
            </ListGroupItem>
          </ListGroup>
        </div>

      </div>
      <div className='footer-lower'>
        <h6>@ 2023 Copyright: GreenThumbGarden.com</h6>
      </div>
    </div>
  );
}