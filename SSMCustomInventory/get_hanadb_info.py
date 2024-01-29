from hdbcli import dbapi

# SAP HANA connection details
HOST = 'your_hana_host'
PORT = 30015  # default port, replace if different
USER = 'your_username'
PASSWORD = 'your_password'

def get_hana_db_info():
    # Function to retrieve information from the SAP HANA database.
   
    try:
        # Connect to the SAP HANA database
        connection = dbapi.connect(HOST, PORT, USER, PASSWORD)

        # Check if the connection is successful
        if connection.isconnected():
            print("Connected to SAP HANA database successfully.")

            # Create a cursor
            cursor = connection.cursor()

            # Query to get database information
            # For example, getting system information
            query = "SELECT * FROM M_SYSTEM_OVERVIEW"

            # Execute the query
            cursor.execute(query)

            # Fetch the results
            results = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            return results
        else:
            print("Failed to connect to SAP HANA database.")
            return None
    except dbapi.Error as e:
        print(f"Database error occurred: {e}")
        return None

if __name__ == "__main__":
    db_info = get_hana_db_info()
    if db_info:
        for row in db_info:
            print(row)
    else:
        print("No data retrieved from SAP HANA database.")
