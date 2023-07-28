import React, { useState } from 'react';

// Style Imports
import './NavBar.css';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  NavbarText,
  InputGroup,
  InputGroupText,
  Input,
} from 'reactstrap';

export default function NavBar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  return (
    <div>
      <Navbar color='info' container expand='sm'>
        <NavbarBrand href="/">Garden</NavbarBrand>
        <NavbarToggler onClick={toggle} />
        <Collapse isOpen={isOpen} navbar>
          <Nav className="me-auto" navbar>

            <NavItem>
              <NavLink href="/">Landing</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/home">Home</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/profile">Profile</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/garden">Garden</NavLink>
            </NavItem>

            <InputGroup>
              <Input placeholder='Search for a plant!'/>
              < InputGroupText>
                Search
              </InputGroupText>
            </InputGroup>
            
          </Nav>
          <NavbarText>Simple Text</NavbarText>
        </Collapse>
      </Navbar>
    </div>
  );
}