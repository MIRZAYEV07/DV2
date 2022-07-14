import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Assign credentials ann path of style sheet
creds = ServiceAccountCredentials.from_json_keyfile_name("creds/client_secrets.json", scope)
client = gspread.authorize(creds)
sheet = client.open("davomat").sheet1

def make_sheet(user_id,user_name,ketgan_vaqti,kelgan_vaqti,sana,vazifalari,joylashuvi):
    insertRow = [user_id,user_name,ketgan_vaqti,kelgan_vaqti,sana,vazifalari,joylashuvi]
    sheet.insert_row(insertRow, 2)
