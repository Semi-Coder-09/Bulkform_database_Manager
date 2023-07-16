from tkinter import messagebox
import mysql.connector

def insert_words_from_file(file_path):
    # Connect to the database
    try:
        db = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Apr@2120',
            database='test'
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Open the file and read its contents
        with open(file_path, 'r') as file:
            duplicate_emails = 0
            duplicate_phones = 0

            for line in file:
                # Split the line into sentences using newlines as separators
                sentences = line.strip().split('\n')
                for sentence in sentences:
                    # Split the sentence into words using commas as separators
                    words = sentence.strip().split(',')

                    # Check if all the required data is present
                    if len(words) != 5:
                        messagebox.showinfo("Invalid Entry", f"Invalid entry: {sentence}")
                        continue

                    # Check if the first two words contain only letters
                    if not words[0].isalpha() or not words[1].isalpha():
                        messagebox.showinfo("Invalid Entry", f"Invalid entry: {sentence}")
                        continue

                    # Extract the words for further processing
                    first_name = words[0]
                    last_name = words[1]
                    email = words[2]
                    password = words[3]
                    phone_number = words[4]

                    # Check if the phone number is numeric
                    if not phone_number.isnumeric():
                        messagebox.showinfo("Invalid Entry", f"Invalid entry: {sentence}")
                        continue

                    # Prepare the SQL query to check if email or phone already exists
                    check_query = "SELECT email, phone FROM employee_data WHERE email = %s OR phone = %s"
                    check_values = (email, phone_number)
                    cursor.execute(check_query, check_values)

                    existing_data = cursor.fetchall()

                    # Check for duplicates
                    if existing_data:
                        for row in existing_data:
                            existing_email, existing_phone = row

                            if existing_email == email:
                                duplicate_emails += 1

                            if existing_phone == phone_number:
                                duplicate_phones += 1

                        continue  # Skip duplicate data

                    # Prepare the SQL query
                    query = "INSERT INTO employee_data (emp_ID, f_name, l_name, email, password, phone) VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (None, first_name, last_name, email + "@techmahindra.com", password, phone_number)

                    # Execute the query
                    cursor.execute(query, values)

        # Commit the changes to the database
        db.commit()

        if duplicate_emails > 0 or duplicate_phones > 0:
            messagebox.showinfo("Duplicate Data", f"{duplicate_emails} email(s) and {duplicate_phones} phone(s) already exist and were skipped.")

        messagebox.showinfo("Records Updated", f"{cursor.rowcount} record(s) updated")

    except mysql.connector.Error as error:
        # Handle database errors
        messagebox.showerror("Database Error", str(error))

    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()

        if db.is_connected():
            db.close()
