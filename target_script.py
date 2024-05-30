import sys
import xlwings as xw
import json

# Read input from standard input
input_data = sys.argv[1]


# Deserialize JSON string to dictionary
input_dict = json.loads(input_data)
# Open the Excel file
wb = xw.Book(r"C:\Users\angad\OneDrive\Desktop\Walsh\original2.xlsm")

# Select the sheet by name
sheet = wb.sheets['Walsh ECA Input (Gate)']

# Fill a cell with a value, for example, filling cell A1 with 'Hello, xlwings!'
sheet.range('Q9').value = input_dict['beams']
sheet.range('Q19').value = input_dict['columns']
sheet.range('Q28').value = input_dict['floors']
sheet.range('Q37').value = input_dict['foundations']
sheet.range('Q50').value = input_dict['walls']

# Save the changes
wb.save()

# Close the workbook
wb.close()


