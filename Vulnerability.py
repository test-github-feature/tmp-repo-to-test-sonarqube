import sqlite3


def insecure_eval():
    user_input = input("Enter a calculation: ")
    result = eval(user_input)
    print(f"The result of your calculation is: {result}")

insecure_eval()



def vulnerable_sql_query(user_input):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# Example of calling the function
results = vulnerable_sql_query("admin'; DROP TABLE users; --")
print(results)


def connect_to_db():
    username = "admin"
    password = "12345_secure"  # Not secure!
    # Connect to the database
    print("Connecting to the database...")
    # Simulated database connection logic here

connect_to_db()

def read_user_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

# Dangerous if the filename comes from an untrusted source
file_contents = read_user_file("/etc/passwd")
print(file_contents)
