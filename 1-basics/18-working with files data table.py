from datetime import datetime
# Define the file name where data will be saved
file_name = "docs/data.txt"

# Define the headers and data
header = ["First Name", "Last Name", "Age", "School", "Gender", "Occupation"]
data=[]

# Add a new row (replace this with any data you want to add)
new_row = ["Ali", "Miller", 29, "MIT", "Male", "Scientist"]
data.append(new_row)  # Append the new row to the existing data

new_rows = [
    ["Alisa", "Miller", 29, "MIT", "Male", "Scientist"],
    ["Christina", "Johnson", 31, "Stanford", "Male", "Engineer"],
    ["Monique", "Schiller", 29, "MIT", "Female", "IT nerd"],
    ["Antika", "Schiller", 29, "MIT", "Female", "IT nerd"],
]
# Add multiple rows to the data
data.extend(new_rows)  # Adds all new rows to the existing data
# Set fixed column widths
col_widths = [15, 15, 10, 10, 10, 10]

# Open the file in write mode to start fresh (overwrite if exists)
with open(file_name, "w") as file:
    # Write the header
    file.write("".join(f"{header[i]:<{col_widths[i]}}" for i in range(len(header))) + "\n")

    # Write each row of data
    for row in data:
        file.write("".join(f"{str(row[i]):<{col_widths[i]}}" for i in range(len(row))) + "\n")
print(f"Data has been written to {file_name}")


# Function to delete a row by line number (1-based index)
def delete_row_by_line_number(file_name, line_number=2):
    # Read the current data from the file
    with open(file_name, "r") as file:
        lines = file.readlines()

    # Adjust for zero-based index by subtracting 1
    index = line_number - 1
    if 0 <= index < len(lines):
        del lines[index]  # Delete the row by index
    else:
        print(f"Line number {line_number} is out of range.")
        return

    # Write the updated content back to the file
    with open(file_name, "w") as file:
        file.writelines(lines)

    print(f"Row {line_number} has been deleted.")

# Example: Delete the 4th row (line number 4)
delete_row_by_line_number(file_name, line_number=4)

# Function to display the content of data.txt
def display_file_content(file_name):
    with open(file_name, "r") as file:
        # Read and print all lines from the file
        content = file.read()
        print(content)
        
# Display the content of the file
display_file_content(file_name)

def check_for_exact_duplicates(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    
   
 # Remove the header and process the rows
    header = lines[0]
    data = lines[1:]

    seen = set()
    duplicates = []
    
    for line in data:
        if line in seen:
            duplicates.append(line.strip())  # Add duplicate row
        else:
            seen.add(line)

    if duplicates:
        print(f"Found {len(duplicates)} duplicate(s):")
        for dup in duplicates:
            print(dup)
    else:
        print("No exact duplicates found.") 

def track_changes(file_name, log_file="change_log.txt"):
    with open(file_name, "r") as file:
        content = file.read()

    with open(log_file, "a") as log:
        log.write(f"Changes made on {datetime.now()}:\n")
        log.write(content)
        log.write("\n" + "="*40 + "\n")

    print(f"Changes logged to {log_file}.")
