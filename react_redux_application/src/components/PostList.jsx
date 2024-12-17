/* eslint-disable no-unused-vars */
import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchPosts } from "../store/postsSlice";
import { List, Divider, Spin, Alert } from "antd";

const PostList = () => {
  const dispatch = useDispatch();
  const { posts, status, error } = useSelector((state) => state.posts);

  useEffect(() => {
    if (status === "idle") {
      dispatch(fetchPosts());
    }
  }, [status, dispatch]);

  if (status === "loading") {
    return (
      <div style={{ textAlign: "center", marginTop: "20px" }}>
        <Spin size="large" />
      </div>
    );
  }

  if (status === "failed") {
    return <Alert message={`Error: ${error}`} type="error" showIcon />;
  }

  return (
    <div>
      <h2>Posts</h2>
      {status === "succeeded" && (
        <div>
          <Divider orientation="left">Posts List</Divider>
          <List
            bordered
            dataSource={posts}
            renderItem={(post) => (
              <List.Item key={post.id}>
                <strong>{post.title}</strong>: {post.body}
              </List.Item>
            )}
          />
        </div>
      )}
    </div>
  );
};

export default PostList;
