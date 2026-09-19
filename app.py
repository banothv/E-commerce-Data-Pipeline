from flask import Flask, jsonify, render_template
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "ecommerce_db",
    "user": "ecommerce_user",
    "password": "ecommerce_password",
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/summary")
def summary():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    total_orders,
                    total_customers,
                    total_revenue,
                    average_order_value
                FROM analytics_summary;
            """)

            row = cursor.fetchone()

            return jsonify({
                "total_orders": row[0],
                "total_customers": row[1],
                "total_revenue": float(row[2]),
                "average_order_value": float(row[3])
            })

    finally:
        connection.close()


@app.route("/api/daily-revenue")
def daily_revenue():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    order_date,
                    orders,
                    revenue
                FROM daily_revenue
                ORDER BY order_date;
            """)

            rows = cursor.fetchall()

            return jsonify([
                {
                    "date": row[0].isoformat(),
                    "orders": row[1],
                    "revenue": float(row[2])
                }
                for row in rows
            ])

    finally:
        connection.close()


@app.route("/api/top-products")
def top_products():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    product_id,
                    product_name,
                    category,
                    units_sold,
                    revenue
                FROM top_products
                ORDER BY revenue DESC;
            """)

            rows = cursor.fetchall()

            return jsonify([
                {
                    "product_id": row[0],
                    "product_name": row[1],
                    "category": row[2],
                    "units_sold": row[3],
                    "revenue": float(row[4])
                }
                for row in rows
            ])

    finally:
        connection.close()


@app.route("/api/revenue-by-country")
def revenue_by_country():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    country,
                    total_orders,
                    revenue
                FROM revenue_by_country
                ORDER BY revenue DESC;
            """)

            rows = cursor.fetchall()

            return jsonify([
                {
                    "country": row[0],
                    "total_orders": row[1],
                    "revenue": float(row[2])
                }
                for row in rows
            ])

    finally:
        connection.close()


if __name__ == "__main__":
    app.run(debug=True)