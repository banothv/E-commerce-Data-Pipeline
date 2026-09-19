E-Commerce Data Engineering & Analytics Pipeline
📌 Project Overview
This project is an end-to-end E-Commerce Data Engineering and Analytics Pipeline built to demonstrate data ingestion, ETL processing, PostgreSQL data storage, SQL transformations, analytics, and a Flask-based dashboard.
The project takes raw e-commerce data stored in CSV files, processes the data using Python, loads it into PostgreSQL, performs SQL-based transformations and analytics, and exposes the results through a Flask application.
🏗️ Current Architecture
                E-Commerce CSV Data
                        │
                        ▼
                ┌───────────────┐
                │  Python ETL   │
                │    Pandas     │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │  PostgreSQL   │
                │    Database   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ SQL Transform │
                │   & Analytics │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   Flask API   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   Dashboard   │
                │   HTML/CSS/JS │
                └───────────────┘
🛠️ Technologies Used
- Python
- Pandas
- PostgreSQL
- SQL
- psycopg2
- Flask
- HTML
- CSS
- JavaScript
- Docker
- Docker Compose
- VS Code
📂 Project Structure
ecommerce-data-pipeline/
│
├── dags/
│   └── ecommerce_pipeline.py
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   └── order_items.csv
│
├── scripts/
│   ├── extract.py
│   ├── validate.py
│   └── load.py
│
├── sql/
│   ├── create_tables.sql
│   ├── transform.sql
│   └── analytics.sql
│
├── tests/
│   └── test_pipeline.py
│
├── docker/
│
├── logs/
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
├── .env
├── .gitignore
└── README.md
Note: Some folders/files in the final structure are part of the planned pipeline and are not yet completed.

✅ Completed Work
1. Python Environment
Created a Python virtual environment for the project.
python -m venv venv
Activated the environment:
venv\Scripts\activate
Installed the required Python packages:
pip install pandas psycopg2-binary flask
2. Docker Environment
Docker Desktop was configured with WSL2 and is being used to run PostgreSQL.
Verified Docker installation with:
docker --version
Docker Compose is also available for the project.
3. PostgreSQL Database
PostgreSQL 16 is running inside a Docker container.
Database configuration:
Database: ecommerce_db
User: ecommerce_user
Port: 5432
Container: ecommerce-postgres
PostgreSQL is managed through Docker Compose.
4. Source E-Commerce Data
Created four CSV datasets:
Customers
customers.csv
Contains:
customer_id
first_name
last_name
email
country
Products
products.csv
Contains:
product_id
product_name
category
price
Orders
orders.csv
Contains:
order_id
customer_id
order_date
order_status
Order Items
order_items.csv
Contains:
order_item_id
order_id
product_id
quantity
unit_price
🗄️ 5. PostgreSQL Database Schema
Created the following tables:
dim_customer
dim_product
fact_orders
fact_order_items
The database follows a simple dimensional data model.
             dim_customer
                  │
                  │
                  ▼
             fact_orders
                  │
                  ▼
          fact_order_items
                  ▲
                  │
                  │
             dim_product
🔄 6. Python ETL
Created an initial Python ETL process using Pandas and psycopg2.
The ETL process:
CSV Files
    ↓
Pandas
    ↓
Python Processing
    ↓
PostgreSQL
The data from the four CSV files was successfully loaded into PostgreSQL.
📥 7. Data Loading
The following datasets were loaded into PostgreSQL:
customers.csv
      ↓
dim_customer

products.csv
      ↓
dim_product

orders.csv
      ↓
fact_orders

order_items.csv
      ↓
fact_order_items
The database tables were also verified using PostgreSQL queries.
🔀 8. SQL Transformations
SQL transformations were created to calculate order-level revenue.
Order revenue is calculated using:
quantity × unit_price
For example:
1 Laptop × ₹75,000
= ₹75,000
Cancelled orders are excluded from completed revenue calculations.
📊 9. SQL Analytics
Created analytical SQL views for:
analytics_summary
daily_revenue
top_products
revenue_by_country
customer_spending
These views provide business metrics such as:
- Total revenue
- Total orders
- Daily revenue
- Top-selling products
- Revenue by country
- Customer spending
Current sample data produces:
Completed Revenue: ₹101,900
🌐 10. Flask API
Created a Flask backend that connects the application to PostgreSQL.
Available API endpoints include:
/api/summary
/api/daily-revenue
/api/top-products
/api/revenue-by-country
The Flask application retrieves analytical data from PostgreSQL and provides it to the frontend.
📈 11. Dashboard
Created the initial dashboard using:
HTML
CSS
JavaScript
Flask
The dashboard is designed to display:
Revenue
Orders
Customers
Products
Daily Revenue
Top Products
Revenue by Country
The dashboard communicates with the Flask API to retrieve data from PostgreSQL.

## 📸 Screenshots

### Project Structure
![Project Structure](screenshots/01-project-structure.png)

### Docker Environment
![Docker](screenshots/02-docker.png)

### PostgreSQL Database
![PostgreSQL](screenshots/03-postgresql.png)

### Database Tables
![Database Tables](screenshots/04-database-tables.png)

### SQL Analytics
![SQL Analytics](screenshots/05-sql-analytics.png)

### E-Commerce Dashboard
![Dashboard](screenshots/06-dashboard.png)
