# Burger Menu Management System
main_menu.png
#### By Ankit AKash Kalita
#### Video Overview: https://youtu.be/z8ua2PS3Wrc?si=vrQoDaVGe9L_Voud  

## Contents

* [Project Overview](#project-overview)
* [Main Files](#main-files)
* [Function and Class Overview](#function-and-class-overview)
* [Libraries Used](#libraries-used)
* [Testing Approach](#testing-approach)
* [How to Use](#how-to-use)
* [Limitations](#limitations)

## Project Overview

* **Purpose**: This project is designed to manage the menu of a fictional burger shop. It allows the user to view, add, update, and remove items from different categories like burgers, snacks, beverages, etc.

* **Key Features**:
  - Display menu items categorized by type (e.g., burgers, meals, desserts).
  - Add new menu items with validation for name, description, diet type, and unit price.
  - Update existing menu items.
  - Remove items from the menu.
  - Navigate through a user-friendly text-based interface.


## Main Files

* **`project.py`**: Contains the main code for the Burger Menu Management System.
* **`test_project.py`**: Includes test cases for validating the functionality of the project’s core functions using pytest.
* **`requirements.txt`**: Lists external libraries required by the project.

## Function and Class Overview

* **`Validation`**: A class containing static methods for validating various fields like item name, description, diet type, and unit price. It ensures that user inputs meet the required constraints before proceeding with adding or updating items.
* **`main_menu()`**: This is the central navigation hub for the program. This function displays the main menu interface where the user can navigate between different options such as viewing the menu, adding new items, updating existing items, or removing items from the menu.
* **`view_menu()`**: This function allows the user to select and view items from specific menu categories (Burgers, Meals, Snacks, Beverages, and Desserts). The function presents the items in a tabular format, showing details like item name, description, diet type, and unit price.
* **`add_item()`**: This function is responsible for adding new items to the menu. It prompts the user to input key details for the item, such as its name, description, diet type, and unit price. The function performs validation on each input to ensure accuracy and data integrity. If an input fails validation (e.g., name too short, invalid price), the user is notified and can choose to either retry the input or cancel the process. Upon successful validation, the item is added to the selected category in the menu.
* **`update_item()`**: This function allows users to modify details of existing items in the menu. It first displays a list of menu categories (Burgers, Meals, Snacks, Beverages and Desserts) and allows the user to select one. Once a category is chosen, the user is prompted to enter the name of the item they wish to update. If the item is found in the selected category, the function prompts for updated value for the selected update category (name, description, diet type, or unit price). Updated input undergoes validation to ensure it meets the required criteria. In case of validation failure, the user can retry or cancel the update process. Upon successful validation, the new values replace the existing ones for the selected item.
* **`remove_item()`**: This function enables users to remove an existing item from the menu. It first displays a list of menu categories (Burgers, Meals, Snacks, Beverages amd Desserts) and allows the user to select one. Once a category is chosen, the user is prompted to enter the name of the item they wish to remove. If the item is found in the selected category, it is deleted, and the user is notified of the successful removal.

## Libraries Used

* **`pyfiglet`**: Used to generate ASCII art for branding in the main menu header.
* **`tabulate`**: Formats and prints tables to display the items in each menu category.
* **`pytest`**: Used to test the file **`test_project.py`**

## Testing Approach

* Functions are tested using pytest for basic functionality (excluding the main function).
* Monkeypatch and capsys features are used to test user input and printed outputs, ensuring that the validation works as expected.

## How to Use

### **Clone or Download the Repository**

To get started, first clone or download this repository to your local machine.

#### To clone the repository using Git, run the following command in your terminal or CLI:

```
git clone <repository-url>
```
**or**

#### [Download the Repository]()

###  **Set Up Your Environment** 

Ensure that Python is installed on your machine. You can download Python from [here](https://www.python.org/downloads/). During installation, make sure to add Python to your system's PATH.

### **IDE (Integrated Development Environment) and CLI (Command Line Interface) Options**

#### You can use any of the following IDEs or text editors to view, and run the code:

* VS Code
* PyCharm
* Sublime Text
* Atom

**or**

#### you can also run the code directly from the command line (CLI). Supported CLI options include:

* Command Prompt (Windows)
* Terminal (macOS/Linux)
* PowerShell (Windows)

### **Navigate to the Project Directory**

#### Open your terminal or CLI and navigate to the root directory of the cloned or downloaded project using this command:

```
cd path/to/project-directory
```
Replace `path/to/project-directory` with the actual path where the project is saved.

### Install Required Libraries

#### After navigating to the project directory, install the necessary libraries listed in the requirements.txt file by running this command:

```
pip install -r requirements.txt
```
This command will install all required dependencies.

### Run the Program

#### To run the program, use the following command:

```
python project.py
```
This will start the program in your terminal, allowing you to interact with the program

### Run the test file

#### To run the test file `test_project.py` using `pytest`, use the following command to run the tests:

```
pytest test_project.py
```
**or**
```
pytest -v test_project.py
```
This will execute all the test functions in test_project.py and display the results in your terminal.

## Limitations

*	**Temporary Data Storage**: All data modifications, including adding, updating, or removing items, are temporary. The project stores data in lists of dictionaries to replicate a database for demonstration purposes. Once the program is closed, any changes made during interaction will be lost. This is due to the scope of the project, which does not implement persistent storage (such as databases or file systems).
*	**Limited Scalability**: The current structure is designed for small-scale usage and may become inefficient with a larger dataset or more complex operations. It does not support advanced database queries or performance optimizations.
*	**No Input Validation for Special Characters**: The program allows certain characters in item names and descriptions but lacks advanced input validation to filter out special characters that may not be desirable in all cases.





