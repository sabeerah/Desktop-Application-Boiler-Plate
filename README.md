
# README: Automation Script for CattleXpert Application

## Overview

This Python script automates interactions with the CattleXpert application. It performs several actions, including logging into the application, navigating through various menus, selecting items, and saving and reading data to/from an Excel file. It also interacts with different UI elements and verifies the presence of certain components.

## Prerequisites

Before running this script, you need to have the following installed:

1. **Python** (3.x): The script is written in Python, so you need to have Python installed on your system.

2. **pywinauto**: This library is used for automating Windows GUI applications.

3. **openpyxl**: This library is used for reading and writing Excel files.

## Installation

### 1. Install Python

Download and install Python from the [official website](https://www.python.org/downloads/).

### 2. Install Required Libraries

You can install the required libraries using pip. Open a terminal or command prompt and run the following commands:

```bash
pip install pywinauto
pip install openpyxl
```

## Running the Script

1. **Save the Script**: Save the provided Python code into a file named `cattlexpert_automation.py` or any name of your choice.

2. **Run the Script**: Execute the script from the terminal or command prompt using the following command:

   ```bash
   python cattlexpert_automation.py
   ```

## What the Script Does

1. **Launches the CattleXpert Application**:
   - Starts the application using the specified executable path.
   - Connects to the login window.

2. **Logs In**:
   - Fills in the username and password fields.
   - Clicks the OK button to log in.

3. **Navigates Through Menus**:
   - Selects various options from the menu bar, including File, Procurement, Commodity, and others.

4. **Interacts with UI Elements**:
   - **Commodity -> Contract**:
     - Selects and interacts with elements in the 'Commodity -> Contract' section.
     - Retrieves values from specific fields and performs an assertion to verify the values.
     - Writes contract and combo box values to an Excel file named `contract_values.xlsx`.
     - Reads the saved values from the Excel file and enters them into the application.

   - **Reports -> Commodity Scale Ticket Reports**:
     - Navigates to the Commodity Scale Ticket Reports section.
     - Interacts with the date picker and refresh buttons.

   - **Processing -> Cattle Board**:
     - Verifies the existence of specific UI elements in the Cattle Board section.
     - Locates and clicks the Refresh and Exit buttons.

5. **Exits and Closes the Application**:
   - Clicks on the Exit button and closes the application.

## Notes

- Ensure that the file paths and identifiers (e.g., auto_id, control_type) used in the script match those in your application. You may need to adjust these based on your specific setup.
- The script includes explicit waits and interactions. Adjust time delays (`time.sleep()`) if needed to ensure the application has enough time to respond to actions.

## Troubleshooting

- **Import Errors**: Make sure all required libraries are installed. Re-run the installation commands if necessary.
- **Element Not Found**: Verify that the identifiers used to locate UI elements are correct. Use tools like Inspect.exe or Swappy.exe to identify the correct values.
- **Application Path**: Ensure that the path to the `CattleXpert.exe` executable is correct.
