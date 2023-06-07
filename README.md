# ConvictConditioningProgressTracker
This program allows you to track your progress in the Convict Conditioning fitness program and store the data in a Google Sheet.

![image](https://github.com/YuryOAraujo/ConvictConditioningProgressTracker/assets/127779626/a51c60e6-2cb6-41a8-aa7b-cae3d933f52a)

## Prerequisites

- Python 3.x
- PySimpleGUI
- gspread
- oauth2client

## Installation

1. Clone the repository or download the files.

2. Install the required dependencies:

   ```shell
   pip install PySimpleGUI gspread oauth2client
Obtain the necessary credentials:

- Create a project in the Google Developers Console.
- Enable the Google Sheets API for your project.
- Create a service account and download the service account key JSON file.
- Rename the JSON file to credentials.json and place it in the same directory as the program.

## Usage
Run the program:

```shell
python progress_tracker.py
```

Fill out the required fields in the GUI:

Select the program (A or B) and exercise.
Enter the warmup, set 1, and set 2 details, including reps and weighted checkbox.
Optionally, enter the date or leave it blank to use the current date.

#### Click the "Submit" button to save the data to the Google Sheet.

To clear the input fields, click the "Clear" button.

Google Sheet Setup
The program assumes you have a Google Sheet named "Convict Conditioning - Progress Tracker" in your Google Drive.

The first worksheet (index 0) of the Google Sheet will be used to store the data.
