import psycopg2

def insert_data(connection_info, table, data):
    try:
        conn = psycopg2.connect(**connection_info)
        cursor = conn.cursor()
        insert_query = f"INSERT INTO {table} (data, created_at) VALUES (%s, %s)"
        cursor.executemany(insert_query, data)
        conn.commit()

        # Đóng cursor và connection
        cursor.close()
        conn.close()

        print("Data inserted successfully")

    except Exception as e:
        print(f"Error: {e}")

def query_data(connection_info, table):
    try:
        conn = psycopg2.connect(**connection_info)

        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table}")
        records = cursor.fetchall()
        for row in records:
            print(row)  # Xử lý mỗi hàng dữ liệu

        # Đóng cursor và kết nối
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

# Thông tin kết nối
connection_info = {
    'dbname': 'yourdb',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',  # Hoặc địa chỉ IP của Docker container nếu chạy từ ngoài Docker
    'port': 5432
}

# Dữ liệu cần chèn
data_to_insert = [
    ('Sample data 1', '2021-01-01 00:00:00'),
    ('Sample data 2', '2021-01-02 00:00:00')
]

# Tên bảng
table_name = 'example_table'

# Chèn dữ liệu
insert_data(connection_info, table_name, data_to_insert)
query_data(connection_info, table_name)
