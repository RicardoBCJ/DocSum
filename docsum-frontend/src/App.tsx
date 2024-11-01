import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Upload from "./components/Upload";
import Documents from "./components/Documents";

function App() {
  return (
    <Router>
      <div className="container mx-auto">
        <nav className="flex justify-between items-center py-4">
          <h1 className="text-3xl font-bold">DocDigest</h1>
          <div>
            <Link to="/" className="mr-4 text-blue-600 hover:underline">
              Upload
            </Link>
            <Link to="/documents" className="text-blue-600 hover:underline">
              Documents
            </Link>
          </div>
        </nav>
        <Routes>
          <Route path="/" element={<Upload />} />
          <Route path="/documents" element={<Documents />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
