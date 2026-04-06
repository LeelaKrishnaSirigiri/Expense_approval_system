# 💳 Expense Approval System

A full-stack Expense Approval System where employees submit expenses and managers review, approve, or reject them with proper validation and workflow.

---

## 🚀 Project Overview

This project simulates a real-world expense management system used in organizations.

- Employees can submit expenses  
- Managers can approve or reject them  
- The system enforces rules and tracks status  

---

## ❗ Problem Statement

In many organizations:

- Expenses are managed using emails or spreadsheets  
- No proper tracking of expense status  
- No structured approval workflow  
- High chance of data errors  

👉 This project solves these problems by providing a centralized and structured system.

---

## ✨ Features

- 📝 Submit new expense  
- 📄 View all expenses  
- ✏️ Update expense (only if Pending)  
- 🗑️ Delete expense (only if Pending)  
- ✅ Approve expense  
- ❌ Reject expense  
- 🔄 Track expense status  

---

## 🔄 Workflow

1. Employee submits expense → **Status = Pending**  
2. Manager reviews the expense  
3. Manager takes action:  
   - Approve → **Approved**  
   - Reject → **Rejected**  
4. Once approved/rejected → ❌ Cannot be modified  

---

## 🛠️ Tech Stack

- 🚀 FastAPI → Backend API development  
- 📊 Pydantic → Data validation  
- 🗄️ SQLAlchemy → ORM  
- 🐘 PostgreSQL → Database  
- 🎨 Streamlit → Frontend UI  

---

## 🗄️ Database Design

### Users Table
- `id`
- `name`
- `email`
- `role`

### Expenses Table
- `id`
- `user_id` (Foreign Key)
- `amount`
- `category`
- `description`
- `status`

👉 Relationship:
- One User → Many Expenses  

---

## 🔌 API Endpoints

- `POST /expenses` → Create expense  
- `GET /expenses` → Get all expenses  
- `PUT /expenses/{id}` → Update expense  
- `DELETE /expenses/{id}` → Delete expense  
- `PATCH /expenses/{id}/status` → Approve/Reject  

---

## ⚙️ Business Logic

- Only **Pending** expenses can be updated  
- Only **Pending** expenses can be deleted  
- Approved/Rejected expenses cannot be modified  
- Amount must be greater than 0  
- User must exist before creating expense  

---

## ✅ Validation Rules

- Required fields cannot be empty  
- Amount must be positive  
- Proper data types must be provided  

---

## 🎨 Frontend (Streamlit)

- Simple and interactive UI  
- Expense submission form  
- Dashboard to view expenses  
- Options to update/delete/approve/reject  

---

## 📚 Learning Outcomes

- Built REST APIs using FastAPI  
- Designed relational database using PostgreSQL  
- Used SQLAlchemy ORM for database operations  
- Applied data validation using Pydantic  
- Implemented real-world business logic and workflow  
- Integrated frontend with backend  

---

## 🔮 Future Enhancements

- 🔐 Authentication system (Login/Signup)  
- 👥 Role-based access control  
- 📧 Email notifications  
- 🎨 Improved UI/UX  

---

## 🙌 Conclusion

This project helped me understand how real-world backend systems work, including API design, validation, database relationships, and workflow implementation.

---
