/* eslint-disable no-unused-vars */
import React from "react";
import PostList from "./components/PostList";
import PostForm from "./components/PostForm";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>React-Redux Apptication</h1>
      <PostForm />
      <PostList />
    </div>
  );
}

export default App;
