import React from 'react';

function Footer() {
    return(
        <div className="btm">
            <hr></hr>
            <footer>
                <p>&copy; {new Date().getFullYear()} David Dooley For Fun</p>
            </footer>
        </div>
    )
}

export default Footer;