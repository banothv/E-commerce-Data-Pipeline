# E-Commerce Data Engineering & Analytics Pipeline

An end-to-end E-Commerce Data Engineering project that demonstrates how raw CSV data can be extracted, loaded into PostgreSQL, transformed using SQL, analyzed, and exposed through a Flask API and web dashboard.

## 📌 Project Overview

This project simulates an e-commerce data platform using customer, product, order, and order item data.

The pipeline currently follows this flow:

```text
CSV Source Data
      ↓
Python ETL
      ↓
PostgreSQL
      ↓
SQL Transformations
      ↓
SQL Analytics
      ↓
Flask API
      ↓
Web Dashboard
```

The project is designed as a portfolio project to demonstrate practical Data Engineering skills including:

- Python
- Pandas
- PostgreSQL
- SQL
- Docker
- Flask
- REST APIs
- Data Transformation
- Data Analytics

---

# 🏗️ Project Architecture

```text
                E-Commerce CSV Files
                         │
                         ▼
                  Python ETL
                         │
                         ▼
                PostgreSQL Database
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        SQL Transformations     SQL Analytics
              │                     │
              └──────────┬──────────┘
                         ▼
                    Flask API
                         │
                         ▼
                  Web Dashboard
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | ETL and backend development |
| Pandas | CSV data processing |
| PostgreSQL | Relational database |
| SQL | Data transformation and analytics |
| Docker | PostgreSQL container |
| Flask | Backend API |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| Git/GitHub | Version control and project hosting |

---

# 📂 Project Structure

```text
ecommerce-data-pipeline/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   └── order_items.csv
│
├── scripts/
│   └── etl.py
│
├── sql/
│   ├── schema.sql
│   └── analytics.sql
│
├── static/
│   └── style.css
│
├── templates/
│   └── dashboard.html
│
├── app.py
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Project Development Steps

## 1. Project Setup

Created the initial project structure for the E-Commerce Data Engineering pipeline.

The project separates:

- Source data
- Python ETL scripts
- SQL scripts
- Flask application
- Frontend files
- Docker configuration

---

## 2. Python Virtual Environment

Created a Python virtual environment to isolate the project dependencies.

```powershell
python -m venv venv
```

Activated the virtual environment:

```powershell
venv\Scripts\activate
```

---

## 3. Installed Python Dependencies

Installed the main Python libraries required for the project.

```powershell
pip install pandas psycopg2-binary flask
```

Dependencies are stored in:

[requirements.txt](requirements.txt)

---

# 🐳 4. Docker Setup

Docker Desktop was configured with WSL2 on Windows.

Docker is used to run PostgreSQL in a containerized environment.

Verified Docker:

```powershell
docker --version
```

Verified Docker Compose:

```powershell
docker compose version
```

---

# 🗄️ 5. PostgreSQL Setup

PostgreSQL was configured using Docker Compose.

PostgreSQL configuration:

```text
Database: ecommerce_db
User: ecommerce_user
Port: 5432
```

Docker configuration:

[docker-compose.yml](docker-compose.yml)

Start PostgreSQL:

```powershell
docker compose up -d
```

Check the running container:

```powershell
docker ps
```

---

# 📊 6. Created Source E-Commerce Data

Created four CSV files representing different entities in an e-commerce system.

### Customers

[data/customers.csv](data/customers.csv)

Contains:

- Customer ID
- First Name
- Last Name
- Email
- Country

### Products

[data/products.csv](data/products.csv)

Contains:

- Product ID
- Product Name
- Category
- Price

### Orders

[data/orders.csv](data/orders.csv)

Contains:

- Order ID
- Customer ID
- Order Date
- Order Status

### Order Items

[data/order_items.csv](data/order_items.csv)

Contains:

- Order Item ID
- Order ID
- Product ID
- Quantity
- Unit Price

---

# 🗃️ 7. PostgreSQL Database Schema

Created a relational database schema to store the e-commerce data.

The database contains four main tables:

```text
dim_customer
dim_product
fact_orders
fact_order_items
```

The schema includes:

- Primary keys
- Foreign keys
- Data types
- Constraints
- Relationships between tables

Database schema:

[sql/schema.sql](sql/schema.sql)

---

# 🔄 8. Python ETL

Created a Python ETL script using Pandas and PostgreSQL.

The ETL process:

```text
CSV Files
   ↓
Pandas
   ↓
Data Processing
   ↓
PostgreSQL
```

The ETL script reads the CSV files and loads the data into PostgreSQL.

ETL code:

[scripts/etl.py](scripts/etl.py)

---

# 📥 9. Load Data into PostgreSQL

The processed data was loaded into PostgreSQL tables.

The loaded tables are:

```text
dim_customer
dim_product
fact_orders
fact_order_items
```

Data was verified directly inside PostgreSQL.

---

# 🔧 10. SQL Transformations

Created SQL transformations to calculate order totals.

For order revenue:

```sql
quantity * unit_price
```

The order totals are calculated from the order item data.

SQL transformation and analytics:

[sql/analytics.sql](sql/analytics.sql)

---

# 📈 11. SQL Analytics

Created analytical views to support business reporting.

The project includes analytics for:

### Analytics Summary

Provides high-level metrics such as:

- Total customers
- Total orders
- Total products
- Total revenue

### Daily Revenue

Calculates revenue by order date.

### Top Products

Identifies products based on revenue.

### Revenue by Country

Analyzes revenue based on customer country.

### Customer Spending

Analyzes customer-level spending.

SQL analytics:

[sql/analytics.sql](sql/analytics.sql)

---

# 📊 12. Business Analytics Verification

The completed orders were used for revenue analysis.

The project calculates revenue from:

```text
Quantity × Unit Price
```

Cancelled orders are excluded from completed-order revenue calculations.

The current sample data produces completed-order revenue of:

```text
₹101,900
```

---

# 🌐 13. Flask Backend

Created a Flask application to expose the PostgreSQL analytics through API endpoints.

Backend:

[app.py](app.py)

Current API endpoints include:

```text
/api/summary
/api/daily-revenue
/api/top-products
/api/revenue-by-country
```

The Flask application connects to PostgreSQL and returns analytics data.

---

# 🖥️ 14. Web Dashboard

Created a web dashboard using:

- HTML
- CSS
- Flask

Dashboard template:

[templates/dashboard.html](templates/dashboard.html)

Dashboard styling:

[static/style.css](static/style.css)

The dashboard is designed to display e-commerce analytics retrieved from the Flask API.

---

# 🔗 API Endpoints

## Summary

```text
GET /api/summary
```

Returns high-level business metrics.

## Daily Revenue

```text
GET /api/daily-revenue
```

Returns revenue by date.

## Top Products

```text
GET /api/top-products
```

Returns top-performing products.

## Revenue by Country

```text
GET /api/revenue-by-country
```

Returns revenue grouped by customer country.

---

# ▶️ How to Run the Project

## Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project:

```bash
cd ecommerce-data-pipeline
```

---

## Step 2: Create Virtual Environment

```powershell
python -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## Step 4: Start PostgreSQL

```powershell
docker compose up -d
```

Verify:

```powershell
docker ps
```

---

## Step 5: Start Flask Application

```powershell
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

# 📌 Current Project Status

## Completed

- [x] Project structure
- [x] Python environment
- [x] Python dependencies
- [x] Docker Desktop + WSL2
- [x] PostgreSQL Docker container
- [x] E-commerce CSV datasets
- [x] PostgreSQL database schema
- [x] Python ETL
- [x] Data loading
- [x] SQL transformations
- [x] SQL analytics
- [x] Flask backend
- [x] Flask API endpoints
- [x] Dashboard files

## In Progress / Future Work

- [ ] Separate `extract.py`
- [ ] Separate `validate.py`
- [ ] Separate `load.py`
- [ ] Apache Airflow DAG
- [ ] Airflow pipeline orchestration
- [ ] Data quality checks
- [ ] Automated tests
- [ ] Full application Dockerization
- [ ] Final dashboard improvements
- [ ] GitHub documentation and screenshots

---

# 🔮 Future Improvements

The next phase of the project will focus on building a production-style data pipeline.

Planned improvements:

```text
Extract
   ↓
Validate
   ↓
Load
   ↓
Transform
   ↓
Data Quality Checks
   ↓
Analytics
   ↓
Flask API
   ↓
Dashboard
```

Future technologies/components:

- Apache Airflow
- Automated data quality checks
- Pytest
- Separate ETL modules
- Dockerized Flask application
- Improved dashboard visualizations

---

# 🎯 Project Goal

The goal of this project is to demonstrate an end-to-end Data Engineering workflow starting from raw e-commerce data and progressing through:

```text
Data Ingestion
      ↓
Data Processing
      ↓
Data Storage
      ↓
Data Transformation
      ↓
Data Analytics
      ↓
API Layer
      ↓
Dashboard
```

This project demonstrates practical experience with Python, SQL, PostgreSQL, Docker, Flask, ETL, and analytics.

---

# 👨‍💻 Author

**Venkatesh**

Data Engineer

📍 Hyderabad, India
