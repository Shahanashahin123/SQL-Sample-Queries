import sqlite3

# Step 1: Connect to (or create) a database
connection = sqlite3.connect("student_database.db")
cursor = connection.cursor()

# Step 2: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    marks INTEGER
)
""")

print("✅ Table created successfully!")

# Step 3: Insert sample student records
students = [
    ("John", 20, "CSE", 85),
    ("Anna", 22, "ECE", 90),
    ("Bob", 21, "CSE", 78),
    ("Mia", 19, "EEE", 88),
    ("Arun", 23, "ME", 92)
]

cursor.executemany("INSERT INTO students (name, age, department, marks) VALUES (?, ?, ?, ?)", students)
connection.commit()
print("🎓 Sample data inserted successfully!")

# Step 4: Query 1 — Display all students
print("\n📋 All Students:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

# Query 2 — Students with marks above 80
print("\n🏅 Students with marks above 80:")
for row in cursor.execute("SELECT name, marks FROM students WHERE marks > 80"):
    print(row)

# Query 3 — Average marks of all students
cursor.execute("SELECT AVG(marks) FROM students")
avg_marks = cursor.fetchone()[0]
print(f"\n📊 Average Marks of Students: {avg_marks:.2f}")

# Query 4 — Count of students in each department
print("\n🏫 Count of Students per Department:")
for row in cursor.execute("SELECT department, COUNT(*) FROM students GROUP BY department"):
    print(row)

# Query 5 — Highest marks
cursor.execute("SELECT name, MAX(marks) FROM students")
top_student = cursor.fetchone()
print(f"\n👑 Top Student: {top_student[0]} with {top_student[1]} marks")
