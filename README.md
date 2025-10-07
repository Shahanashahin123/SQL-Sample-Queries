# SQL Queries on a Sample Database

This mini project demonstrates how to use **SQL queries** to interact with and analyze data from a **sample database**.  
It covers the basics of data retrieval, filtering, aggregation, and table relationships — perfect for beginners learning SQL.

---

## 📘 Project Overview

This project contains:
- A sample SQL database (such as `employees`, `students`, or `sales`)
- A collection of SQL queries for:
  - Creating tables
  - Inserting sample data
  - Performing simple `SELECT`, `UPDATE`, and `DELETE` operations
  - Using `WHERE`, `GROUP BY`, `ORDER BY`, and `JOIN` clauses

---

## 🧠 Concepts Covered

- Basic SQL syntax
- Data insertion and updates
- Filtering with `WHERE`
- Sorting with `ORDER BY`
- Aggregation using `COUNT`, `AVG`, `SUM`, `MIN`, and `MAX`
- Combining data using `INNER JOIN` and `LEFT JOIN`

---

## ⚙️ How to Run

1. Open your SQL editor (MySQL Workbench, SQLite, or any online SQL compiler)
2. Copy and paste the queries from this project.
3. Run each query step by step to see how SQL works in real-time.

---

## 🧩 Example Queries

```sql
-- Create a sample table
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  grade VARCHAR(5)
);

-- Insert data
INSERT INTO students VALUES
(1, 'Alice', 20, 'A'),
(2, 'Bob', 22, 'B'),
(3, 'Charlie', 21, 'A');

-- Select all students
SELECT * FROM students;

-- Find students with grade A
SELECT name FROM students WHERE grade = 'A';
