import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import App from "./App";
import AuthPage from "./AuthPage";
import Dashboard from "./Dashboard";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
    <Router>
      <Routes>
        <Route path="/" element={<AuthPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/test-api" element={<App />} />
      </Routes>
    </Router>
  </StrictMode>
);
