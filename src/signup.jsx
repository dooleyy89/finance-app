import React, {useState} from "react"; {/* state to manage form inputs */}
import axios from "axios"; {/*HTTP client used to make requests from react to flask*/}
import { Link } from "react-router-dom"

function Signup() {
    return(
        <form>
            <label>Sign Up</label><br/>
            <input
                type="text"
                placeholder="Username"
            /><br/>
            <input
                type="password"
                placeholder="Password"
            /><br/>
            <input type="submit" value="Create Account"></input><hr/>
            <span>Already have an account? <Link to="/login">Log In</Link></span>
        </form>
    );
}

export default Signup;