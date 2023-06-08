import datetime
import PySimpleGUI as sg
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the path to your service account key file
key_file = "credentials.json"

# Define the scope (permissions) for accessing Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Create credentials using the key file and scope
credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file, scope)

# Authorize the credentials
client = gspread.authorize(credentials)

# Open the Google Sheet by its title
sheet = client.open("Convict Conditioning - Progress Tracker")

# Access the worksheets
worksheet = sheet.get_worksheet(0)  # Get the first worksheet (index 0)

# Example: Read cell values
values = worksheet.get_all_values()

# Add some color to the window
sg.theme('DarkTeal9')

def get_current_date():
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y")

def get_reps(reps):
    reps = reps.split(' ')
    return reps[0] if len(reps) == 1 else 'L' + reps[0] + ' R' + reps[1]

def get_weight(weight):
    return ' +17kg' if weight == True else ''

def clear_input():
    for key in values:
        if key not in ['WeightWarmup', 'WeightSet1', 'WeightSet2']:
            window[key]('')
    return None

def get_program(exercise):
    if exercise in ['Pullups', 'Squats', 'Bridges']:
        return 'A'
    else:
        return 'B'

def processData():
    row['program'] = get_program(values['Name'])
    row['exercise'] = values['Name']
    row['warmup'] = f"{values['StepWarmup']}{get_weight(values['WeightWarmup'])}: {get_reps(values['RepWarmup'])}"
    row['set1'] = f"{values['StepSet1']}{get_weight(values['WeightSet1'])}: {get_reps(values['RepSet1'])}"
    row['set2'] = f"{values['StepSet2']}{get_weight(values['WeightSet2'])}: {get_reps(values['RepSet2'])}"
    row['date'] = f"{values['Date'] if values['Date'] != '' else get_current_date()}"
    worksheet.append_row(list(row.values()))

# Options of the Program
program = ['A', 'B']
exercises = ['Pushups', 'Bridges', 'Pullups', 'Squats', 'Leg Raises', 'Handstand Pushups']
steps = ["Step {}".format(i) for i in range(1, 11)]

# Dictionary to store the values
row = {
    'program':'',
    'exercise':'',
    'warmup':'',
    'set1':'',
    'set2':'',
    'date':''
}

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Exercise:', size=(6, 1)), sg.Combo(exercises, key='Name')],
    [sg.Text('Warmup:', size=(6, 1)), sg.Combo(steps, key='StepWarmup'), sg.Text('Reps'), sg.InputText(key='RepWarmup', size=(10, 1)), sg.Checkbox('Weighted', key='WeightWarmup')],
    [sg.Text('Set 1:', size=(6, 1)), sg.Combo(steps, key='StepSet1'), sg.Text('Reps'), sg.InputText(key='RepSet1', size=(10, 1)), sg.Checkbox('Weighted', key='WeightSet1', default=True)],
    [sg.Text('Set 2:', size=(6, 1)), sg.Combo(steps, key='StepSet2'), sg.Text('Reps'), sg.InputText(key='RepSet2', size=(10, 1)), sg.Checkbox('Weighted', key='WeightSet2', default=True)],
    [sg.Text('Date:', size=(6, 1)), sg.InputText(key='Date', size=(10, 1))],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Convict Conditioning', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        processData()
        sg.popup('Data saved!')
        clear_input()

window.close()
