DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  f_name VARCHAR(255),
  l_name VARCHAR(255)
);


CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255),
  assignee VARCHAR(255),
  duration INT,
  completed BOOLEAN DEFAULT FALSE,
  user_id INT REFERENCES users(id)
);

