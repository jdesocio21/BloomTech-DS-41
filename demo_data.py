import sqlite3


row_count = [(3,)]
xy_at_least_5 = [(2,)]
unique_y = [(2,)]


def connect_to_sqlite(db_name="demo_data.sqlite3"):
    # Connect to the db
    return sqlite3.connect(db_name)


def execute_query(conn, query):
    # Make a cursor (a middle man)
    cursor = conn.cursor()
    # Execute our query
    cursor.execute(query)
    # Pull results from the cursor
    results = cursor.fetchall()
    return results


row_count_query = """
SELECT COUNT (*)
FROM demo
"""


xy_at_least_5_query = """
SELECT COUNT(*)
FROM demo
WHERE x>=5 AND y>=5
"""


unique_y_query = """
SELECT COUNT(DISTINCT y)
FROM demo
"""


if __name__ == '__main__':
    conn = connect_to_sqlite("demo_data.sqlite3")
    results = execute_query(conn, row_count_query)
    print(results)
