# 🛒 E-Commerce Data Engineering & Analytics Pipeline

An end-to-end E-Commerce Data Engineering project that demonstrates how raw e-commerce data can be processed, stored, transformed, analyzed, and exposed through a Flask API and web dashboard.

The project starts with CSV files and builds a complete data flow using Python, PostgreSQL, SQL, Docker, Flask, HTML, and CSS.

---

# 📌 Project Overview

The main objective of this project is to build a practical E-Commerce data pipeline.

The pipeline processes:

- Customer data
- Product data
- Order data
- Order item data

The processed data is stored in PostgreSQL and transformed using SQL to generate business analytics.

A Flask backend exposes the analytics through API endpoints, and a web dashboard displays the results.

---

# 🏗️ Project Architecture

```text
                    E-Commerce CSV Files
                            │
                            ▼
                       Python ETL
                            │
                            ▼
                     PostgreSQL
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
          SQL Transformations    SQL Analytics
                 │                     │
                 └──────────┬──────────┘
                            ▼
                       Flask API
                            │
                            ▼
                     Web Dashboard
```

### Data Flow

```text
CSV
 ↓
Extract
 ↓
Process
 ↓
Load
 ↓
PostgreSQL
 ↓
Transform
 ↓
Analytics
 ↓
Flask API
 ↓
Dashboard
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | ETL and backend development |
| Pandas | CSV processing |
| PostgreSQL | Data storage |
| SQL | Transformation and analytics |
| Docker | PostgreSQL containerization |
| Flask | REST API and backend |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| Git | Version control |
| GitHub | Project repository |

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
├── screenshots/
│
├── app.py
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Project Development Process

## 1️⃣ Project Setup

The project was started by creating a structured folder architecture for the E-Commerce Data Engineering pipeline.

The project separates:

- Source data
- ETL scripts
- SQL scripts
- Flask backend
- Frontend files
- Docker configuration
- Documentation screenshots

### Project Structure

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/860a29ed-69f3-40be-9032-6fedcfce7f69" />


---

# 2️⃣ Python Virtual Environment

A Python virtual environment was created to isolate project dependencies.

### Create virtual environment

```powershell
python -m venv venv
```

### Activate environment

```powershell
venv\Scripts\activate
```

This ensures that project dependencies do not interfere with the system Python installation.

### Screenshot

![Python Virtual Environment](screenshots/02-python-environment.png)

---

# 3️⃣ Install Python Dependencies

The project uses Python libraries for data processing, PostgreSQL connectivity, and the Flask backend.

Installed packages:

```powershell
pip install pandas psycopg2-binary flask
```

Main libraries:

- `pandas`
- `psycopg2-binary`
- `flask`

### Requirements

[View requirements.txt](requirements.txt)

---

# 4️⃣ Docker and WSL2 Setup

Docker Desktop was configured on Windows with WSL2 support.

Docker is used to run PostgreSQL in a container instead of installing PostgreSQL directly on Windows.

### Verify Docker

```powershell
docker --version
```

### Verify Docker Compose

```powershell
docker compose version
```

### Screenshot

![Docker Setup](screenshots/03-docker.png)

---

# 5️⃣ PostgreSQL Setup Using Docker

PostgreSQL was configured using Docker Compose.

Database configuration:

```text
Database: ecommerce_db
User: ecommerce_user
Port: 5432
```

### Start PostgreSQL

```powershell
docker compose up -d
```

### Check container

```powershell
docker ps
```

### Docker Configuration

[View docker-compose.yml](docker-compose.yml)

### Screenshot

![PostgreSQL Docker](screenshots/04-postgresql.png)

---

# 6️⃣ Create E-Commerce Source Data

Four CSV files were created as the source data for the pipeline.

## Customers

The customer dataset contains:

- Customer ID
- First name
- Last name
- Email
- Country

[View customers.csv](data/customers.csv)

---

## Products

The product dataset contains:

- Product ID
- Product name
- Category
- Price

[View products.csv](data/products.csv)

---

## Orders

The order dataset contains:

- Order ID
- Customer ID
- Order date
- Order status

[View orders.csv](data/orders.csv)

---

## Order Items

The order item dataset contains:

- Order item ID
- Order ID
- Product ID
- Quantity
- Unit price

[View order_items.csv](data/order_items.csv)

### Source Data Screenshot

![Source Data](screenshots/06-source-data.png)

---

# 7️⃣ PostgreSQL Database Schema

A relational database schema was created to store the e-commerce data.

The database contains four main tables:

```text
dim_customer
dim_product
fact_orders
fact_order_items
```

### Table Relationships

```text
dim_customer
      │
      │ customer_id
      ▼
fact_orders
      │
      │ order_id
      ▼
fact_order_items
      │
      │ product_id
      ▼
dim_product
```

The schema uses:

- Primary keys
- Foreign keys
- NOT NULL constraints
- UNIQUE constraints
- Relationships between fact and dimension tables

### SQL Code

[View Database Schema](sql/schema.sql)

### Screenshot

![Database Tables](screenshots/05-database-tables.png)

---

# 8️⃣ Python ETL

A Python ETL script was created using Pandas and PostgreSQL connectivity.

The ETL process reads the CSV files and loads the data into PostgreSQL.

### ETL Flow

```text
customers.csv
products.csv
orders.csv
order_items.csv
       │
       ▼
     Pandas
       │
       ▼
 Data Processing
       │
       ▼
   PostgreSQL
```

### Python ETL Code

[View ETL Code](scripts/etl.py)

### Main technologies

```text
Python
Pandas
psycopg2
PostgreSQL
```

### Screenshot

![Python ETL](screenshots/07-etl.png)

---

# 9️⃣ Load Data into PostgreSQL

The ETL script loads the CSV data into PostgreSQL.

The target tables are:

```text
dim_customer
dim_product
fact_orders
fact_order_items
```

The loaded data was verified using PostgreSQL.

### Screenshot

![Loaded PostgreSQL Data](screenshots/08-loaded-data.png)

---

# 🔟 SQL Transformations

After loading the raw data, SQL transformations were created.

Order revenue is calculated using:

```text
quantity × unit_price
```

For example:

```text
1 Laptop × ₹75,000
+
1 Keyboard × ₹2,500
=
₹77,500
```

The `fact_orders.total_amount` field is updated based on the order items.

### SQL Code

[View SQL Analytics and Transformations](sql/analytics.sql)

---

# 1️⃣1️⃣ SQL Analytics

SQL views were created to generate business analytics.

The project currently includes:

### Analytics Summary

Provides high-level metrics such as:

- Total customers
- Total orders
- Total products
- Total revenue

### Daily Revenue

Calculates revenue by order date.

### Top Products

Analyzes product revenue.

### Revenue by Country

Analyzes revenue based on customer country.

### Customer Spending

Analyzes customer-level spending.

### SQL Code

[View Analytics SQL](sql/analytics.sql)

### Screenshot

![SQL Analytics](screenshots/09-sql-analytics.png)

---

# 1️⃣2️⃣ Business Analytics Verification

The analytics were verified using the PostgreSQL database.

Completed orders are included in the revenue calculation.

Cancelled orders are excluded from completed-order revenue.

The current sample dataset produces:

```text
Completed Order Revenue
₹101,900
```

### Revenue Calculation

```text
Order 1001 = ₹77,500
Order 1002 = ₹7,000
Order 1004 = ₹2,400
Order 1005 = ₹15,000

Total = ₹101,900
```

---

# 1️⃣3️⃣ Flask Backend

A Flask application was created to connect the PostgreSQL analytics layer with the web frontend.

### Flask Application

[View app.py](app.py)

The Flask backend provides API endpoints for the dashboard.

---

# 🔗 API Endpoints

## Summary

```http
GET /api/summary
```

Returns high-level e-commerce metrics.

---

## Daily Revenue

```http
GET /api/daily-revenue
```

Returns revenue grouped by date.

---

## Top Products

```http
GET /api/top-products
```

Returns product revenue information.

---

## Revenue by Country

```http
GET /api/revenue-by-country
```

Returns revenue grouped by customer country.

---

# 1️⃣4️⃣ Web Dashboard

A web dashboard was created using Flask, HTML, and CSS.

The dashboard communicates with the Flask API and displays the analytics.

### Dashboard Template

[View dashboard.html](templates/dashboard.html)

### Dashboard CSS

[View style.css](static/style.css)

### Dashboard Screenshot

![E-Commerce Dashboard](screenshots/11-dashboard.png)

---

# ▶️ How to Run the Project

## Step 1: Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

```bash
cd ecommerce-data-pipeline
```

---

## Step 2: Create Virtual Environment

```powershell
python -m venv venv
```

---

## Step 3: Activate Virtual Environment

```powershell
venv\Scripts\activate
```

---

## Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## Step 5: Start PostgreSQL

```powershell
docker compose up -d
```

Verify:

```powershell
docker ps
```

---

## Step 6: Run Flask Application

```powershell
python app.py
```

Open the application:

```text
http://127.0.0.1:5000
```

---

# 📊 Current Project Status

## ✅ Completed

- [x] Project structure
- [x] Python virtual environment
- [x] Python dependencies
- [x] Docker Desktop + WSL2
- [x] PostgreSQL Docker container
- [x] E-commerce source CSV files
- [x] PostgreSQL database schema
- [x] Python ETL
- [x] Data loading
- [x] SQL transformations
- [x] SQL analytics
- [x] Analytics verification
- [x] Flask backend
- [x] Flask API endpoints
- [x] Dashboard files

## 🔄 Future Development

- [ ] Separate `extract.py`
- [ ] Separate `validate.py`
- [ ] Separate `load.py`
- [ ] Apache Airflow DAG
- [ ] Airflow orchestration
- [ ] Data quality checks
- [ ] Automated tests
- [ ] Full application Dockerization
- [ ] Additional dashboard improvements

---

# 🔮 Future Architecture

The planned final pipeline is:

```text
             CSV / API
                 │
                 ▼
              Extract
                 │
                 ▼
             Validate
                 │
                 ▼
               Load
                 │
                 ▼
            PostgreSQL
                 │
                 ▼
             Transform
                 │
                 ▼
          Data Quality Check
                 │
                 ▼
             Analytics
                 │
                 ▼
             Flask API
                 │
                 ▼
             Dashboard
```

Apache Airflow will eventually be used to orchestrate these pipeline steps.

---

# 🎯 Project Goal

The goal of this project is to demonstrate an end-to-end Data Engineering workflow:

```text
Raw Data
   ↓
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
API
   ↓
Dashboard
```

This project demonstrates practical experience with:

- Python
- Pandas
- SQL
- PostgreSQL
- Docker
- ETL
- Flask
- REST APIs
- Data Analytics
- GitHub

---

# 👨‍💻 Author

**Venkatesh**

**Data Engineer**

📍 Hyderabad, India
