import React from 'react'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Login from './login.jsx'
import Signup from './signup.jsx'
import Dashboard from './dashboard.jsx'

function App() {
    return(
        <Router>
            <Routes>
                <Route path="/login" element={<Login/>}/>
                <Route path="/signup" element={<Signup/>}/>
                <Route path="/dashboard" element={<Dashboard/>}/>
                
                <Route path="*" element={<Login/>}/>
            </Routes>
        </Router>
    );
};

export default App;
