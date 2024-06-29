import gspread
from oauth2client.service_account import ServiceAccountCredentials

def fetch_result(sheet, input_box_names, values, output_box_name):
    for box, value in zip(input_box_names, values):
        sheet.update_acell(box, value)

    result = sheet.acell(output_box_name).value
    return result

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']


# Sample : credentials.json file structure
# How to generate : From Google cloud console API provider
# {
#   "type": "service_account",
#   "project_id": "",
#   "private_key_id": "",
#   "private_key": "",
#   "client_email": "",
#   "client_id": "",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "",
#   "universe_domain": "googleapis.com"
# }

creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\mehak\OneDrive\Desktop\kipps assignment\credentials.json', scope)
client = gspread.authorize(creds)

spreadsheet_name = input("Enter the name of your Google Spreadsheet: ")
spreadsheet = client.open(spreadsheet_name)
# sheet_name = "Sheet2"
sheet_name = input("Enter the sheet name: ")
sheet = spreadsheet.worksheet(sheet_name)

# spreadsheet = client.open("sample")
# sheet = spreadsheet.sheet1

N = int(input("Enter the number of input boxes: "))

input_box_names = []
for i in range(N):
    box = input(f"Enter the name of input box {i+1}: ")
    input_box_names.append(box)

values = []
for i in range(N):
    value = input(f"Enter the value for {input_box_names[i]}: ")
    values.append(value)

output_box_name = input("Enter the cell name of the output box: ")

result = fetch_result(sheet, input_box_names, values, output_box_name)
print("The result in", output_box_name, "is:", result)


# sheet.update_acell('A1', 5)
# sheet.update_acell('B1', 10)
# result = sheet.cell(1, 3).value
# print("The result in C1 is:", result)

