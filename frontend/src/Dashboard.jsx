import React, { useEffect, useState } from 'react'
import axios from "axios";
import './Dashboard.css';

export default function Dashboard() {

  const [latestTemperature, setLatestTemperature] = useState(70);
  const [latestPressure, setLatestPressure] = useState(70);

  useEffect(() => {
    const fetchLatestTemperature = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5050/api/fetch_latest");
        setLatestTemperature(response["data"][0]["temperature"]);
      } catch (err) {
        console.error("Error fetching latest temperature:", err);
      }
    };
    const fetchLatestPressure = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5050/api/fetch_latest");
        setLatestPressure(response["data"][0]["pressure"]);
      } catch (err) {
        console.error("Error fetching latest pressure:", err)
      }
    };
    fetchLatestTemperature();
    fetchLatestPressure();
    const interval = setInterval(fetchLatestTemperature, 500);
    const interval2 = setInterval(fetchLatestPressure, 500);
    return () => {
      clearInterval(interval);
      clearInterval(interval2);
    };
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
            <span>{latestPressure}</span>
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
