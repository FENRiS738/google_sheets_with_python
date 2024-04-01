from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from app.connection import connect
from app.schema import User

# To extract data from Google Sheets
def get_data():
    creds, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME = connect()
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        
        values = result.get("values", [])

        if not values:
            return "No data found."

        return values
    except HttpError as err:
        return err

# To append data in Google Sheets
def insert_data(user):
    creds, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME = connect()
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        
        body = {
            'values' : [[user.first_name, user.last_name, user.age]]
        }

        result = (
            sheet.values()
            .append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, valueInputOption = 'USER_ENTERED', body=body)
            .execute()
        )
        return({
            'message': 'Record inserted successfully',
            'user': user
        })
    except HttpError as err:
        return err