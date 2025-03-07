import React from 'react';

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import Home from './components/home.jsx'
import Add from './components/add.jsx'
import Delete from './components/delete.jsx'
import View from './components/view.jsx'

function Header() {
    return(
        <div className="banner">
                <header id="top">
                    <img id="TopPic" alt="MoneyTrack" src="https://cdn-icons-png.flaticon.com/512/2150/2150264.png"></img>
                    <h1 id="head1">Expense Tracker</h1>
                </header>
                <nav id ="list">
                    <span><Link to="/">Home</Link></span>
                    <span><Link to="/add">Add</Link></span>
                    <span><Link to="/delete">Delete</Link></span>
                    <span><Link to="/view">View</Link></span>
                </nav>
        </div>
    );
}

export default Header;
