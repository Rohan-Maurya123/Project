import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";

import Dashboard from "./pages/Dashboard";
import Courses from "./pages/Courses";
import Analytics from "./pages/Analytics";
import Recommendations from "./pages/Recommendations";
import CourseDetail from "./pages/CourseDetail";
import Enrolled from "./pages/Enrolled";

import Layout from "./components/Layout";

function App() {
  // Pre-set a default user so app works directly without login
  if (!localStorage.getItem("user")) {
    localStorage.setItem("user", JSON.stringify({
      _id: "1",
      name: "Rohan",
      email: "rohan@gmail.com",
      interests: ["Programming", "Data Science"]
    }));
  }

  return (
    <BrowserRouter>
      <Routes>
        {/* AUTH PAGES (NO SIDEBAR) - still accessible but not required */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* DASHBOARD PAGES (WITH SIDEBAR) */}
        <Route path="/" element={
          <Layout>
            <Dashboard />
          </Layout>
        } />
        {/* DASHBOARD PAGES (WITH SIDEBAR) */}
        <Route
          path="/dashboard"
          element={
            <Layout>
              <Dashboard />
            </Layout>
          }
        />

        <Route
          path="/courses"
          element={
            <Layout>
              <Courses />
            </Layout>
          }
        />

        <Route
          path="/analytics"
          element={
            <Layout>
              <Analytics />
            </Layout>
          }
        />

        <Route
          path="/recommendations"
          element={
            <Layout>
              <Recommendations />
            </Layout>
          }
        />

        <Route
          path="/course/:id"
          element={
            <Layout>
              <CourseDetail />
            </Layout>
          }
        />

        <Route
          path="/enrolled"
          element={
            <Layout>
              <Enrolled />
            </Layout>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
