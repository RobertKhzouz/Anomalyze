import React, { useEffect, useState } from 'react'
import axios from "axios";
import './Dashboard.css';

export default function Dashboard() {

  const [latestTemperature, setLatestTemperature] = useState(70);

  useEffect(() => {
    const fetchLatestTemperature = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5050/api/fetch_latest");
        console.log(response)
        setLatestTemperature(response["data"][0]["temperature"]);
      } catch (err) {
        console.error("Error fetching latest temperature:", err);
      }
    };
    fetchLatestTemperature();
    const interval = setInterval(fetchLatestTemperature, 5000);
    return () => clearInterval(interval);
  }, []);

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
            <span>{latestTemperature}</span>
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
