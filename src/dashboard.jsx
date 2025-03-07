import React from 'react'

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom"
import Home from './components/home.jsx'
import Add from './components/add.jsx'
import Delete from './components/delete.jsx'
import View from './components/view.jsx'

import Header from './Header.jsx'
import Footer from './Footer.jsx'

function Dashboard() {
    return(
            <div id="main">
                <Header/>
                <div className='main-body'>
                    <Routes>
                        <Route path="/" element={<Home/>} />
                        <Route path="/add" element={<Add/>} />
                        <Route path="/delete" element={<Delete/>} />
                        <Route path="/view" element={<View/>} />
                    </Routes>
                </div>
                <Footer/>
            </div>
    );
};

export default Dashboard;
