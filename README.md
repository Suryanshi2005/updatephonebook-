# updatephonebook-
# Phone Book Application (For Beginners)

This is a simple Phone Book application with a graphical interface that allows you to store, search, delete, and display contacts easily.

If you have never used Python before, don't worry! Follow these easy steps to run the Phone Book on your computer.

## What is This?

This is a small app where you can:

- Add new contacts (name and phone number).
- Search for existing contacts.
- Delete contacts.
- View all contacts.

The app uses a simple window (GUI) where you can click buttons and type in names and numbers.

## How to Set This Up

### Step 1: Install Python

Before running this app, you'll need to have Python installed on your computer. Python is a programming language, and this app is written in Python.

1. Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the version that matches your operating system (Windows, macOS, or Linux).
3. Make sure you check the box that says "Add Python to PATH" when installing (important for Windows users).

If you already have Python installed, you can skip this step.

### Step 2: Download the App Files

Next, you need to download the files for this Phone Book app.

1. Click the green "Code" button at the top of this page and select "Download ZIP."
2. Extract the downloaded ZIP file to a folder on your computer.

### Step 3: Install Required Libraries

Open a terminal or command prompt on your computer.

- On Windows: Press `Win + R`, type `cmd`, and hit Enter.
- On macOS: Open the Terminal application.
- On Linux: Open your Terminal.

Navigate to the folder where you extracted the ZIP file. For example, if the folder is on your Desktop:

cd Desktop/phone-book
Now install the required Python libraries by running this command:

bash
Copy code
pip install -r requirements.txt
This command will automatically install any necessary tools to run the app.

Step 4: Run the Phone Book App
After installing everything, you're ready to run the Phone Book app. Simply run this command in your terminal:

bash
Copy code
python phone_book.py
This will open the app's window where you can start adding, searching, and managing contacts.

How to Use the App
Add a Contact: Type a name and phone number in the text boxes and click the "Add Contact" button.
Search for a Contact: Type the name of the person you want to find and click "Search Contact."
Delete a Contact: Type the name of the person you want to delete and click "Delete Contact."
Display All Contacts: Click the "Display Contacts" button to see all the contacts you've saved.
Troubleshooting
"Python is not recognized" error: This means Python is not installed correctly. Try reinstalling Python and make sure to check "Add Python to PATH" during installation.
No contacts appearing: Make sure you're adding contacts before trying to search or display them.
What's Inside
phone_book.py: The Python file that runs the app.
requirements.txt: The file that lists the Python libraries required to run the app
Future Improvements
Adding the ability to edit contact details.
Improving the GUI to be more user-friendly.
Contributing
If you want to make improvements or add new features, feel free to fork the project and submit a pull request. I am happy to see contributions!


