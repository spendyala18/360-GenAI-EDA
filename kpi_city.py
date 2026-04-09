import sqlite3

def city_kpi(city: str):
    conn = sqlite3.connect('data/db/analytics.db')
    cursor = conn.cursor()
    
    # Parameterized SQL query to prevent SQL Injection
    query = "SELECT COUNT(*), AVG(monthly_spend) FROM customers_raw WHERE city = ?"
    cursor.execute(query, (city,))
    result = cursor.fetchone()
    conn.close()

    if result and result[0] > 0:
        print(f"City: {city: <15} | Total Customers: {result[0]} | Avg Spend: {result[1]:.2f}")
        return result
    else:
        print(f"City: {city: <15} | Result: No data found.")
        return None

if __name__ == "__main__":
    city_kpi("Mumbai")
    city_kpi("Mumbai' OR 1=1 --")