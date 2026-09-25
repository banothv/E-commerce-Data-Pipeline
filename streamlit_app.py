import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="E-Commerce Data Engineering",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 E-Commerce Data Engineering Dashboard")
st.write("E-commerce data pipeline and analytics dashboard")

DATA_DIR = Path("data")


def load_csv(filename):
    file_path = DATA_DIR / filename

    if file_path.exists():
        return pd.read_csv(file_path)

    return pd.DataFrame()


customers = load_csv("customers.csv")
products = load_csv("products.csv")
orders = load_csv("orders.csv")
order_items = load_csv("order_items.csv")


st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Customers", len(customers))

with col2:
    st.metric("Products", len(products))

with col3:
    st.metric("Orders", len(orders))

with col4:
    st.metric("Order Items", len(order_items))


st.divider()

st.subheader("📊 Dataset Preview")

dataset = st.selectbox(
    "Select Dataset",
    ["Customers", "Products", "Orders", "Order Items"]
)

if dataset == "Customers":
    st.dataframe(customers, use_container_width=True)

elif dataset == "Products":
    st.dataframe(products, use_container_width=True)

elif dataset == "Orders":
    st.dataframe(orders, use_container_width=True)

elif dataset == "Order Items":
    st.dataframe(order_items, use_container_width=True)


st.divider()

st.subheader("🔄 Pipeline Overview")

st.write("""
**Extract → Validate → Transform → Load → Analyze**

- Python for ETL processing
- PostgreSQL for data storage
- SQL for transformation and analytics
- Apache Airflow for workflow orchestration
- Docker for containerization
- Streamlit for dashboard visualization
""")