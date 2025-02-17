import sqlite3

DB_NAME = 'students.db'

class StudentModel:

    @staticmethod
    def init_db():
        """Khởi tạo database."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birthdate TEXT,
                gender TEXT,
                department TEXT,
                gpa REAL,
                image TEXT
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def get_students():
        """Lấy danh sách sinh viên."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students ORDER BY name")
        students = cursor.fetchall()
        conn.close()
        return students

    @staticmethod
    def search_students(keyword):
        """Tìm sinh viên theo tên."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + keyword + '%',))
        students = cursor.fetchall()
        conn.close()
        return students

    @staticmethod
    def get_student_by_id(student_id):
        """Lấy thông tin sinh viên theo ID."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
        student = cursor.fetchone()
        conn.close()
        return student

    @staticmethod
    def add_student(name, birthdate, gender, department, gpa, image=None):
        """Thêm sinh viên vào database."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (name, birthdate, gender, department, gpa, image)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, birthdate, gender, department, gpa, image))
        conn.commit()
        conn.close()

    @staticmethod
    def update_student(student_id, name, birthdate, gender, department, gpa, image=None):
        """Cập nhật thông tin sinh viên."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        if image:
            cursor.execute("""
                UPDATE students
                SET name=?, birthdate=?, gender=?, department=?, gpa=?, image=?
                WHERE id=?
            """, (name, birthdate, gender, department, gpa, image, student_id))
        else:
            cursor.execute("""
                UPDATE students
                SET name=?, birthdate=?, gender=?, department=?, gpa=?
                WHERE id=?
            """, (name, birthdate, gender, department, gpa, student_id))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_student(student_id):
        """Xóa sinh viên khỏi database."""
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        conn.close()
