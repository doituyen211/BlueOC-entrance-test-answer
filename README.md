# BlueOC-entrance-test-answer

This repository contains solutions to three tasks, including Python scripts and a React-Redux application. Each task is explained with clear instructions, test cases, and example outputs.

## Table of Content

1. [Task 1: String Length Frequency](#task-1-string-length-frequency)
2. [Task 2: Sum of Top Two Integers](#task-2-sum-of-top-two-integers)
3. [Task 3: React-Redux Application](#task-3-react-redux-application)
4. [Setup and Running Instructions](#setup-and-running-instructions)

## Task 1: String Length Frequency

### **Objective**

Write a function that identifies the most frequent string lengths in an array of strings.

### **Solution**

The function takes an array of strings as input, calculates the frequency of string lengths, and returns the strings with the most frequent length.

### **Code Implementation**

`string_length_frequency.py`

### **Code Implementation**

`string_length_frequency.py`

```python
def find_string_length_frequency(strings):
    length_count = {}
    for s in strings:
        length = len(s)
        length_count[length] = length_count.get(length, 0) + 1

    max_frequency = max(length_count.values())
    result = [s for s in strings if len(s) in [key for key, value in length_count.items() if value == max_frequency]]

    return result

# Example usage:
input_strings = ['a', 'ab', 'abc', 'cd', 'def', 'gh']
output = find_string_length_frequency(input_strings)
print(output)  # Output: ['ab', 'cd', 'gh']

```

### **Test Cases**

| Input                             | Output            |
| --------------------------------- | ----------------- |
| `['a', 'ab', 'abc', 'cd', 'def']` | `['ab', 'cd']`    |
| `['a', 'b', 'c']`                 | `['a', 'b', 'c']` |
| `['abcd', 'efg', 'hi']`           | `['efg', 'hi']`   |

---

## **Task 2: Sum of Top Two Integers**

### **Objective**

Write a function that finds the sum of the two largest integers in an array.

### **Solution**

The function sorts the input array and returns the sum of the two largest integers.

### **Code Implementation**

`sum_of_top_two_integers.py`

```python
def sum_of_top_two_integers(numbers):
    if len(numbers) < 2:
        raise ValueError("Array must contain at least two integers")
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[0] + sorted_numbers[1]

# Example usage:
input_numbers = [1, 4, 2, 3, 5]
output = sum_of_top_two_integers(input_numbers)
print(output)  # Output: 9

```

### **Test Cases**

| Input              | Output |
| ------------------ | ------ |
| `[1, 4, 2, 3, 5]`  | `9`    |
| `[10, 20, 30, 40]` | `70`   |
| `[0, 1, -1, -2]`   | `1`    |

---

## **Task 3: React-Redux Application**

### **Objective**

Create a React-Redux app that fetches and displays posts from an API and includes a form to add new posts.

### **API Endpoint**

`https://jsonplaceholder.typicode.com/posts`

---

### **Features**

- Fetches and displays posts from the API using **Redux** for state management.
- Includes a **PostForm** component to add new posts.
- Uses **React-Redux** and **Redux Toolkit**.

---

### **Project Structure**

```
react_redux_application/
│── src/
│   ├── components/
│   │   ├── PostList.jsx
│   │   └── PostForm.jsx
│   ├── store/
│   │   ├── store.js
│   │   └── postsSlice.js
│   ├── App.jsx
│   └── main.jsx
└── package.json

```

---

### **Code Highlights**

### **PostList Component**

Fetches and displays posts from the Redux store.

```jsx
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
```

---

### **PostForm Component**

Allows users to add a new post.

```jsx
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
```

---

### **Setup and Running Instructions**

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd react_redux_application

   ```

2. Install dependencies:

   ```bash
   npm install

   ```

3. Run the React application:

   ```bash
   npm run dev

   ```

4. Open your browser at `http://localhost:5173`.
