import React, { useState } from 'react'; 
import "./Banner.scss";

function Banner(props) {
    // const [connectDeviceModalShow, setConnectDeviceShow] = useState(false);
    // const [registerDeviceModalShow, setRegisterDeviceShow] = useState(false);

    return (
        <div className="page-header">
            <span className="header-title">{props.title}</span>
            <div className="link-container">
                {/* Space to add to banner - Home, Account, etc */}
                {/* <span className="my-devices-link">My Devices</span>
                <span className="connect-device-link" onClick={(e) => {setConnectDeviceShow(true)}}>Connect a Device</span>
                <span className="register-link" onClick={(e) => {setRegisterDeviceShow(true)}}>Register</span> */}
            </div>
        </div>
    )
}

export default Banner;