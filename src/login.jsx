import React, {useState} from "react"; {/* state to manage form inputs */}
import axios from "axios";
import { Link } from "react-router-dom"

function Login() {
    return(
        <form>
            <label>Sign In</label><br/>
            <input
                type="text"
                placeholder="Username"
            /><br/>
            <input
                type="password"
                placeholder="Password"
            /><br/>
            <input type="submit" value="Log In"></input><hr/>
            <span>Don't have an account? <Link to="/signup">Sign up</Link></span>
        </form>
    );
}

export default Login;