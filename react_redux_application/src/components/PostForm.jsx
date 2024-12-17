/* eslint-disable no-unused-vars */
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addPost } from "../store/postsSlice";
import { Button, Form, Input } from "antd";

const PostForm = () => {
  const dispatch = useDispatch();
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");

  const onFinish = (values) => {
    const { title, body } = values;
    if (title && body) {
      dispatch(addPost({ title, body }));
      setTitle("");
      setBody("");
    }
  };

  return (
    <Form
      name="postForm"
      onFinish={onFinish}
      style={{ marginBottom: "20px", maxWidth: 600 }}
      initialValues={{
        remember: true,
      }}
    >
      <h2>Add New Post</h2>

      <Form.Item
        label="Title"
        name="title"
        rules={[
          {
            required: true,
            message: "Please input the title!",
          },
        ]}
      >
        <Input placeholder="Enter post title" />
      </Form.Item>

      <Form.Item
        label="Body"
        name="body"
        rules={[
          {
            required: true,
            message: "Please input the body of the post!",
          },
        ]}
      >
        <Input.TextArea placeholder="Enter post body" rows={4} />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit">
          Add Post
        </Button>
      </Form.Item>
    </Form>
  );
};

export default PostForm;
