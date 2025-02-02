import React from 'react'
import './Dashboard.css';


export default function Dashboard() {
  return (
    <body>
  <header>
    <div> 
    Home Dashboard
    </div>
    <div class="dropdown">
    <button class="profile-button">View Profile</button>
    <div class="dropdown-content">
      <a href="#">Profile Settings</a>
      <a href="#">Logout</a>
      <a href="#">Help</a>
    </div>
  </div>
  </header>
  
  <div class="dashboard-container">
    <div class="live-feed">
      <span>Live video feed placeholder</span>

    </div>
    <div class="control-panel">
      <div class="control-panel-item">
        <h3>Air Temperature</h3>
        <span>--- °C</span>
      </div>

      <div class="control-panel-item">
        <h3>Air Pressure</h3>
        <span>--- hPa</span>
      </div>
      <div class="control-panel-item">
        <h3>Humidity</h3>
        <span>--- %</span>
      </div>
    </div>
  </div>
</body>
  )
}
