from fpdf import FPDF

def generate_dashboard_pdf(output_path: str = "Admin_Dashboard_Plan.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)  # Changed to built-in font
    
    # Title
    pdf.set_font("Helvetica", style='B', size=16)
    pdf.cell(200, 10, txt="Admin Dashboard Plan", ln=True, align="C")
    pdf.ln(10)
    
    # Section: SQL Tables
    pdf.set_font("Helvetica", style='B', size=14)
    pdf.cell(200, 10, txt="SQL Table Structures", ln=True)
    pdf.ln(10)
    
    sql_tables = """\
1. Users Table
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    role ENUM('Admin', 'User', 'Subscriber', 'Teacher', 'Student', 'Employee'),
    password_hash VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

2. Roles and Permissions
CREATE TABLE Roles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    role_name VARCHAR(255) UNIQUE
);

CREATE TABLE Permissions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    role_id INT,
    permission VARCHAR(255),
    FOREIGN KEY (role_id) REFERENCES Roles(id)
);

3. Courses Table
CREATE TABLE Courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_id INT,
    title VARCHAR(255),
    description TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (teacher_id) REFERENCES Users(id)
);
"""
    
    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(0, 6, txt=sql_tables)  # Reduced line spacing for better formatting
    pdf.ln(10)
    
    # Section: Coding Implementation
    pdf.set_font("Helvetica", style='B', size=14)
    pdf.cell(200, 10, txt="Coding Implementation", ln=True)
    pdf.ln(10)
    
    coding_part = """\
Frontend:
- React.js with TailwindCSS for responsive UI.
- Role-based navigation.

Backend:
- FastAPI for REST API.
- SQLAlchemy for database operations.

Database:
- MySQL.

Authentication:
- JWT authentication.
- Role-based middleware.

Example Query:
SELECT * FROM Users WHERE role = 'Admin';
"""
    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(0, 6, txt=coding_part)  # Reduced line spacing
    
    pdf.output(output_path)
    return output_path

if __name__ == "__main__":
    path = generate_dashboard_pdf()
    print(f"PDF generated at: {path}")
