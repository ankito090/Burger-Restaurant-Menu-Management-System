from pyfiglet import Figlet  # type: ignore
from tabulate import tabulate  # type: ignore
from typing import Callable
import sys


class Validation:
    """
    A collection of static methods for validating various item attributes
    such as name, description, diet type, and unit price.

    Each method interacts with the user, ensuring inputs meet specific
    criteria.
    """

    @staticmethod
    def validate_name() -> str | None:
        """
        Validates the user's name input.

        Returns:
            str | None: The validated name or None if the user chooses not to retry.

        Raises:
            ValueError: if the user inputs an invalid item name, or retry selection
        """
        while True:
            # Prompt the user for an item name
            name = input("\nName: ").strip().title()
            if len(name) >= 3 and len(name) <= 50:  # Check length constraints.
                if "'S" in name:  # Handle specific capitalization case.
                    name = name.replace("'S", "'s")
                return name
            else:
                print(
                    """Invalid name! Please ensure the following:
1. Name should not be empty.
2. Name should be between 3 and 50 characters long."""
                )

                # Prompt the user for retry.
                while True:
                    try:
                        print("Do you want to retry?")
                        retry = int(input("Enter 1 for Yes or 2 for No: "))
                        if retry == 1:
                            break
                        elif retry == 2:
                            return None
                        else:
                            raise ValueError
                    except ValueError:
                        # Handle invalid input.
                        print("Invalid input! Please try again.")

    @staticmethod
    def validate_description() -> str | None:
        """
        Validates the user's description input.

        Returns:
            str | None: The validated description or None if the user chooses not to retry.

        Raises:
            ValueError: if the user inputs an invalid item description or retry option
        """
        while True:
            # Prompt the user for an item description
            description = input("\nDescription: ").strip().capitalize()
            if (
                len(description) >= 10 and len(description) <= 150
            ):  # Check length constraints.
                if "'S" in description:  # Handle specific capitalization case.
                    description = description.replace("'S", "'s")
                return description
            else:
                print(
                    """Invalid description! Please ensure the following:
1. Description should not be empty.
2. Description should be between 10 and 150 characters long."""
                )

                # Prompt the user for retry.
                while True:
                    try:
                        print("Do you want to retry?")
                        retry = int(input("Enter 1 for Yes or 2 for No: "))
                        if retry == 1:
                            break
                        elif retry == 2:
                            return None
                        else:
                            raise ValueError
                    except ValueError:
                        # Handle invalid input.
                        print("Invalid input! Please try again.")

    @staticmethod
    def validate_diet_type() -> str | None:
        """
        Validates the user's diet type input.

        Returns:
            str | None: The validated diet type or None if the user chooses not to retry.

        Raises:
            ValueError: if the user inputs an invalid diet type or retry option
        """
        while True:
            # Display options.
            print("\nDiet type: Enter 1 for Veg or 2 for Non-Veg")

            try:
                # Prompt the user for a diet type selection
                diet_type = int(
                    input("Select an option by entering the corresponding number: ")
                )
                if diet_type == 1:
                    return "Veg"
                elif diet_type == 2:
                    return "Non-Veg"
                else:
                    raise ValueError
            except ValueError:
                # Handle invalid input.
                print(
                    """Invalid diet type! Please ensure the following:
1. Enter 1 to apply Veg.
2. Enter 2 to apply Non-Veg."""
                )

                # Prompt the user for retry.
                while True:
                    try:
                        print("Do you want to retry?")
                        retry = int(input("Enter 1 for Yes or 2 for No: "))
                        if retry == 1:
                            break
                        elif retry == 2:
                            return None
                        else:
                            raise ValueError
                    except ValueError:
                        # Handle invalid input.
                        print("Invalid input! Please try again.")

    @staticmethod
    def validate_unit_price() -> float | None:
        """
        Validates the user's unit price input.

        Returns:
            float | None: The validated unit price or None if the user chooses not to retry.

        Raises:
            ValueError: if the user inputs an invalid unit price or retry option
        """
        while True:
            try:
                # Prompt the user for an unit price
                unit_price = float(input("\nUnit Price: "))
                if unit_price > 0:
                    return unit_price  # Return the validated unit price.
                else:
                    raise ValueError  # Raise error for non-positive value.
            except ValueError:
                print(
                    """Invalid unit price! Please ensure the following:
1. Unit price should not be empty.
2. Unit price should be a positive numerical value."""
                )

                # Prompt the user for retry.
                while True:
                    try:
                        print("Do you want to retry?")
                        retry = int(input("Enter 1 for Yes or 2 for No: "))
                        if retry == 1:
                            break
                        elif retry == 2:
                            return None
                        else:
                            raise ValueError
                    except ValueError:
                        # Handle invalid input.
                        print("Invalid input! Please try again.")


def main():
    main_menu()


def main_menu() -> None:
    """
    Displays the main menu for the burger menu management program, allowing the user to
    view the menu, add an item, update an item, remove an item, or exit the program.

    Returns:
        None

    Raises:
        ValueError: If the user inputs an invalid category selection.
    """
    figlet: Figlet = Figlet(font="doom")

    # Print the program title with a decorative text.
    print(
        figlet.renderText("Ankito's  Burger"),
        """
                    ⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣿⣿⣿⣿⣿⣿⠿⠷⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣯⣀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
                    ⠀⠀⢠⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣁⣈⣽⣿⣷⡀⠀⠀
                    ⠀⠀⣿⣿⣶⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣧⠀⠀
                    ⠀⠀⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠧⠤⠾⠿⠿⠿⠿⠿⠷⠶⠾⠟⠀⠀
                    ⠀⠀⢶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠶⠀⠀
                    ⠀⣠⣤⣤⣤⣤⣤⣤⣄⣀⣀⣈⣉⣉⣉⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣤⣄⠀
                    ⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
                    ⠀⢀⣤⣭⠉⠉⠉⢉⣉⡉⠉⠉⠉⣉⣉⠉⠉⠉⢉⣉⠉⠉⠉⢉⣭⣄⠀⠀
                    ⠰⡟⠁⠈⢷⣤⣴⠟⠉⠻⣄⣠⡾⠋⠙⠳⣤⣴⠟⠉⠳⣦⣠⡾⠃⠙⢷⡄
                    ⠀⠀⢀⣀⣀⣉⡀⠀⠀⠀⠈⠉⠀⠀⠀⣀⣈⣁⣀⣀⣀⣀⣉⣀⣀⠀⠀⠀
                    ⠀⠀⠛⠛⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠛⠛⠛⠛⠛⠛⠃⠀
                    ⠀⠀⢸⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿

═════════════════════════════════════════════════════════════════════
║ 1. View Menu                                                      ║
║ 2. Add an Item                                                    ║
║ 3. Update an Item                                                 ║
║ 4. Remove an Item                                                 ║
║ 5. Exit                                                           ║
═════════════════════════════════════════════════════════════════════""",
    )

    while True:
        try:
            # Prompt the user for a menu selection.
            user_input: int = int(
                input("Select an option by entering the corresponding number : ")
            )

            # Process the user's selection.
            if user_input == 1:
                view_menu()
            elif user_input == 2:
                add_item()
            elif user_input == 3:
                update_item()
            elif user_input == 4:
                remove_item()
            elif user_input == 5:
                sys.exit()
            else:
                raise ValueError

        except ValueError:
            # Handle invalid input for category selection.
            print("Invalid input! Please try again.")


burgers: list[dict[str, str | float]] = [
    {
        "item_name": "Classic Chicken Burger",
        "description": "Juicy chicken patty with cheese, lettuce, and tomato",
        "diet_type": "Non-Veg",
        "unit_price": 199.99,
    },
    {
        "item_name": "Chicken Feast",
        "description": "Double chicken patty with spicy sauce",
        "diet_type": "Non-Veg",
        "unit_price": 209.99,
    },
    {
        "item_name": "Spicy BBQ Burger",
        "description": "Fried chicken breast with BBQ sauce and pickles",
        "diet_type": "Non-Veg",
        "unit_price": 229.99,
    },
    {
        "item_name": "Crispy Chicken Burger",
        "description": "Breaded chicken patty with mayo and lettuce",
        "diet_type": "Non-Veg",
        "unit_price": 189.99,
    },
    {
        "item_name": "Veggie Burger",
        "description": "Grilled veggie patty with lettuce and tomato",
        "diet_type": "Veg",
        "unit_price": 149.99,
    },
    {
        "item_name": "Paneer Tikka Burger",
        "description": "Grilled paneer with mint chutney and veggies",
        "diet_type": "Veg",
        "unit_price": 169.99,
    },
    {
        "item_name": "Black Bean Burger",
        "description": "Spicy black bean patty with avocado",
        "diet_type": "Veg",
        "unit_price": 179.99,
    },
]
meals: list[dict[str, str | float]] = [
    {
        "item_name": "Chicken Combo Meal",
        "description": "Chicken breast with mashed potatoes and vegetables",
        "diet_type": "Non-Veg",
        "unit_price": 299.99,
    },
    {
        "item_name": "Grilled Chicken Meal",
        "description": "Grilled chicken breast with salad and fries",
        "diet_type": "Non-Veg",
        "unit_price": 289.99,
    },
    {
        "item_name": "Chicken Tenders Meal",
        "description": "Chicken tenders with mashed potatoes and gravy",
        "diet_type": "Non-Veg",
        "unit_price": 299.99,
    },
    {
        "item_name": "Veggie Combo Meal",
        "description": "Veggie patty with salad and fries",
        "diet_type": "Veg",
        "unit_price": 259.99,
    },
    {
        "item_name": "Paneer Tikka Meal",
        "description": "Spicy grilled paneer with salad and fries",
        "diet_type": "Veg",
        "unit_price": 269.99,
    },
]
snacks: list[dict[str, str | float]] = [
    {
        "item_name": "Fries",
        "description": "Crispy golden fries",
        "diet_type": "Veg",
        "unit_price": 89.99,
    },
    {
        "item_name": "Onion Rings",
        "description": "Crispy fried onion rings",
        "diet_type": "Veg",
        "unit_price": 119.99,
    },
    {
        "item_name": "Mozzarella Sticks",
        "description": "Breaded mozzarella sticks with marinara sauce",
        "diet_type": "Veg",
        "unit_price": 149.99,
    },
    {
        "item_name": "Stuffed Jalapenos",
        "description": "Jalapenos stuffed with cheese and deep-fried",
        "diet_type": "Veg",
        "unit_price": 189.99,
    },
    {
        "item_name": "Chicken Nuggets",
        "description": "Breaded chicken nuggets (6 pieces)",
        "diet_type": "Non-Veg",
        "unit_price": 149.99,
    },
    {
        "item_name": "Buffalo Wings",
        "description": "Spicy chicken wings with celery and ranch",
        "diet_type": "Non-Veg",
        "unit_price": 199.99,
    },
    {
        "item_name": "Chicken Tenders",
        "description": "Breaded chicken tenders with dipping sauce",
        "diet_type": "Non-Veg",
        "unit_price": 299.99,
    },
]
beverages: list[dict[str, str | float]] = [
    {
        "item_name": "Coca-Cola",
        "description": "Chilled Coca-Cola (500 ml)",
        "diet_type": "Veg",
        "unit_price": 59.99,
    },
    {
        "item_name": "Iced Lemonade",
        "description": "Freshly squeezed lemonade with ice",
        "diet_type": "Veg",
        "unit_price": 79.99,
    },
    {
        "item_name": "Chocolate Milkshake",
        "description": "Thick chocolate milkshake with whipped cream",
        "diet_type": "Veg",
        "unit_price": 99.99,
    },
    {
        "item_name": "Coffee",
        "description": "Freshly brewed coffee (medium)",
        "diet_type": "Veg",
        "unit_price": 59.99,
    },
    {
        "item_name": "Iced Tea",
        "description": "Refreshing iced tea with lemon",
        "diet_type": "Veg",
        "unit_price": 59.99,
    },
    {
        "item_name": "Sparkling Water",
        "description": "Carbonated water with a hint of lime",
        "diet_type": "Veg",
        "unit_price": 39.99,
    },
]
desserts: list[dict[str, str | float]] = [
    {
        "item_name": "Brownie Sundae",
        "description": "Warm brownie with vanilla ice cream and chocolate syrup",
        "diet_type": "Veg",
        "unit_price": 149.99,
    },
    {
        "item_name": "Apple Pie",
        "description": "Classic apple pie with cinnamon",
        "diet_type": "Veg",
        "unit_price": 199.99,
    },
    {
        "item_name": "Vanilla Ice Cream",
        "description": "Creamy vanilla ice cream in a cone",
        "diet_type": "Veg",
        "unit_price": 109.99,
    },
    {
        "item_name": "Chocolate Cake",
        "description": "Rich chocolate cake with fudge frosting",
        "diet_type": "Veg",
        "unit_price": 199.99,
    },
    {
        "item_name": "Cheesecake",
        "description": "Creamy cheesecake with a graham cracker crust",
        "diet_type": "Veg",
        "unit_price": 199.99,
    },
]


def view_menu() -> None:
    """
    Allows the user to display the items of the selected menu categories.

    Returns:
        None

    Raises:
        ValueError: If the user inputs an invalid category selection or post-view selection.
    """
    while True:
        # Display the menu category options to the user.
        print(
            """
Category Selected: View Menu 
--------------------------------
| 1. Burgers                   |              
| 2. Meals                     |  
| 3. Snacks                    |  
| 4. Beverages                 |
| 5. Desserts                  |
| 6. Go back to the main menu  |
| 7. Exit                      |
--------------------------------"""
        )

        # Define the headers for the table of items to be displayed.
        columns: list[str] = [
            "item_name",
            "description",
            "diet_type",
            "unit_price (in ₹)",
        ]

        # Define the menu categories and their associated items.
        menu_categories: dict[int, tuple[str, list[dict[str, str | float]]]] = {
            1: ("Burgers", burgers),
            2: ("Meals", meals),
            3: ("Snacks", snacks),
            4: ("Beverages", beverages),
            5: ("Desserts", desserts),
        }

        # Initialize a list to hold the rows of item data for display.
        rows: list[tuple[str | float, ...]] = []

        try:
            # Prompt the user for a category selection.
            category_selection: int = int(
                input("Select a category by entering the corresponding number: ")
            )

            # Check if the selected category is valid.
            if category_selection in menu_categories:
                category_name, category_items = menu_categories[category_selection]
                print(f"\nCategory Selected: {category_name}")

                # Collect item data from the selected category.
                for value in category_items:
                    rows.append(
                        (
                            value["item_name"],
                            value["description"],
                            value["diet_type"],
                            value["unit_price"],
                        )
                    )

                # Display the items in the selected category.
                if rows:
                    print(tabulate(rows, headers=columns, tablefmt="fancy_grid"))
                else:
                    print("No items are available in this category.")

                # Post view options: Go back or exit.
                while True:
                    try:
                        post_view_selection: int = int(
                            input("Enter 1 to go back or 2 to exit the program: ")
                        )
                        if post_view_selection == 1:
                            break
                        elif post_view_selection == 2:
                            sys.exit()
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid input! Please try again.")

            # Option to go back to the main menu.
            elif category_selection == 6:
                main_menu()

            # Option to exit the program.
            elif category_selection == 7:
                sys.exit()

            # Handle invalid selections.
            else:
                raise ValueError

        except ValueError:
            # Handle invalid input for category selection.
            print("Invalid input! Please try again.")


def add_item() -> None:
    """
    Allows the user to add an item to a selected category from the menu.

    Returns:
        None

    Raises:
        ValueError: If the user inputs an invalid category or post-add selection.
    """
    while True:
        # Display menu categories for adding an item.
        print(
            """
Category Selected: Add an Item 
--------------------------------
| 1. Add a Burger              |              
| 2. Add a Meal                |  
| 3. Add a Snack               |  
| 4. Add a Beverage            |
| 5. Add a Dessert             |
| 6. Go back to the main menu  |
| 7. Exit                      |
--------------------------------"""
        )

        # Dictionary mapping category numbers to their corresponding name and list.
        add_categories: dict[int, tuple[str, list[dict[str, str | float]]]] = {
            1: ("Add a Burger", burgers),
            2: ("Add a Meal", meals),
            3: ("Add a Snack", snacks),
            4: ("Add a Beverage", beverages),
            5: ("Add a Dessert", desserts),
        }

        try:
            # Prompt the user for a category selection.
            category_selection: int = int(
                input("Select an option by entering the corresponding number: ")
            )

            # If a valid category is selected.
            if category_selection in add_categories:
                category_name, category_type = add_categories[category_selection]
                print(f"\nCategory Selected: {category_name}")

                while True:
                    # Validate item name.
                    name: str | None = Validation.validate_name()
                    if name is None:
                        print("Failed to add an item")
                        break

                    # Validate description.
                    description: str | None = Validation.validate_description()
                    if description is None:
                        print("Failed to add an item")
                        break

                    # Validate diet type (veg/non-veg).
                    diet_type: str | None = Validation.validate_diet_type()
                    if diet_type is None:
                        print("Failed to add an item")
                        break

                    # Validate unit price.
                    unit_price: float | None = Validation.validate_unit_price()
                    if unit_price is None:
                        print("Failed to add an item")
                        break

                    # Check if the item already exists, if not, add the new item.
                    if not any(item["item_name"] == name for item in category_type):
                        category_type.append(
                            {
                                "item_name": name,
                                "description": description,
                                "diet_type": diet_type,
                                "unit_price": unit_price,
                            }
                        )
                        print(f"\n{name} is successfully added!")
                    else:
                        print(f"\n{name} already exists!")

                    # Post add options: Go back or exit.
                    while True:
                        try:
                            post_add_selection: int = int(
                                input("Enter 1 to go back or 2 to exit the program: ")
                            )
                            if post_add_selection == 1:
                                break
                            elif post_add_selection == 2:
                                sys.exit()
                            else:
                                raise ValueError
                        except ValueError:
                            print("Invalid input! Please try again.")
                    break

            # Option to go back to the main menu.
            elif category_selection == 6:
                main_menu()

            # Option to exit the program.
            elif category_selection == 7:
                sys.exit()

            # Handle invalid selections.
            else:
                raise ValueError

        except ValueError:
            # Handle invalid input for category selection.
            print("Invalid input! Please try again.")


def update_item() -> None:
    """
    Allows the user to update an existing item from a selected category.

    Returns:
        None

    Raises:
        ValueError: If the user inputs an invalid selection for category, retry, update type, or post-update selection.
    """
    while True:
        # Display menu categories for updating an item.
        print(
            """
Category Selected: Update an Item 
--------------------------------
| 1. Update a Burger           |              
| 2. Update a Meal             |  
| 3. Update a Snack            |  
| 4. Update a Beverage         |
| 5. Update a Dessert          |
| 6. Go back to the main menu  |
| 7. Exit                      |
--------------------------------"""
        )

        # Dictionary mapping category numbers to their corresponding name and list.
        update_categories: dict[int, tuple[str, list[dict[str, str | float]]]] = {
            1: ("Update a Burger", burgers),
            2: ("Update a Meal", meals),
            3: ("Update a Snack", snacks),
            4: ("Update a Beverage", beverages),
            5: ("Update a Dessert", desserts),
        }

        # Dictionary mapping update type numbers to their corresponding validation functions, item keys, and status messages.
        update_options: dict[int, tuple[Callable, str, str]] = {
            1: (
                lambda: Validation.validate_name(),
                "item_name",
                "Item name is successfully updated!",
            ),
            2: (
                lambda: Validation.validate_description(),
                "description",
                "Item description is successfully updated!",
            ),
            3: (
                lambda: Validation.validate_diet_type(),
                "diet_type",
                "Item diet type is successfully updated!",
            ),
            4: (
                lambda: Validation.validate_unit_price(),
                "unit_price",
                "Item unit price is successfully updated!",
            ),
        }
        status: str = "break"
        try:
            # Prompt the user for a category selection.
            category_selection: int = int(
                input("Select an option by entering the corresponding number: ")
            )

            # If a valid category is selected.
            if category_selection in update_categories:
                category_name, category_type = update_categories[category_selection]
                print(f"\nCategory Selected: {category_name}")

                while True:
                    # Get the item name to update from the user.
                    item_to_update: str = (
                        input(f"Enter {category_name.replace('Update a ', '')} Name: ")
                        .strip()
                        .title()
                        .replace("'S", "'s")
                    )

                    # Search for the item in the selected category.
                    item: dict[str, str | float] | None = next(
                        (
                            item
                            for item in category_type
                            if item["item_name"] == item_to_update
                        ),
                        None,
                    )

                    # If the item is found, proceed with updating.
                    if item:
                        while True:
                            print(f"\nItem Selected: {item_to_update}")
                            # Display update options for the selected item.
                            print(
                                "1. Update Name",
                                "2. Update Description",
                                "3. Update Diet Type",
                                "4. Update Unit Price",
                                "5. Go Back",
                                sep="\n",
                            )

                            try:
                                # Get the update type selection from the user.
                                update_type_selection: int = int(
                                    input(
                                        "Select an option by entering the corresponding number:  "
                                    )
                                )

                                # If a valid update option is selected.
                                if update_type_selection in update_options:
                                    validation_method, item_key, update_status = (
                                        update_options[update_type_selection]
                                    )

                                    # Validate the new data for the selected update type.
                                    new_data: str | float | None = validation_method()
                                    if new_data is None:
                                        print("Failed to update an item")
                                        break

                                    # Update the item with the new data.
                                    item[item_key] = new_data
                                    print(f"\n{update_status}")

                                    # Post update options: Go back or exit.
                                    while True:
                                        try:
                                            post_update_selection: int = int(
                                                input(
                                                    "Enter 1 to go back to the update item menu or 2 to exit the program: "
                                                )
                                            )
                                            if post_update_selection == 1:
                                                break
                                            elif post_update_selection == 2:
                                                sys.exit()
                                            else:
                                                raise ValueError
                                        except ValueError:
                                            print("Invalid input! Please try again.")
                                    break

                                # Option to go back from the update item menu.
                                elif update_type_selection == 5:
                                    break

                                # Handle invalid update type selections.
                                else:
                                    raise ValueError

                            except ValueError:
                                # Handle invalid input for update type.
                                print("Invalid input! Please try again.")

                        break

                    # If the item is not found, ask the user if they want to retry.
                    else:
                        print("Item not found! Do you want to try again?")
                        while True:
                            try:
                                retry_choice: int = int(
                                    input("Enter 1 for Yes or 2 for No: ")
                                )
                                if retry_choice == 1:
                                    status = "continue"
                                    break
                                elif retry_choice == 2:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Invalid input! Please try again.")

                        # If the user chooses to retry, continue the loop.
                        if status == "continue":
                            continue
                        else:
                            break

            # Option to go back to the main menu.
            elif category_selection == 6:
                main_menu()

            # Option to exit the program.
            elif category_selection == 7:
                sys.exit()

            # Handle invalid selections for category.
            else:
                raise ValueError

        except ValueError:
            # Handle invalid input for category selection.
            print("Invalid input! Please try again.")


def remove_item() -> None:
    """
    Allows the user to remove an existing item from a selected category.

    Returns:
        None

    Raises:
        ValueError: If the user inputs an invalid category, retry, or post-remove selection.
    """
    while True:
        # Display menu categories for removing an item.
        print(
            """
Category Selected: Remove an Item 
--------------------------------
| 1. Remove a Burger           |              
| 2. Remove a Meal             |  
| 3. Remove a Snack            |  
| 4. Remove a Beverage         |
| 5. Remove a Dessert          |
| 6. Go back to the main menu  |
| 7. Exit                      |
--------------------------------"""
        )

        # Dictionary mapping category numbers to their corresponding name and list.
        remove_categories: dict[int, tuple[str, list[dict[str, str | float]]]] = {
            1: ("Remove a Burger", burgers),
            2: ("Remove a Meal", meals),
            3: ("Remove a Snack", snacks),
            4: ("Remove a Beverage", beverages),
            5: ("Remove a Dessert", desserts),
        }
        status: str = "break"
        try:
            # Prompt the user for a category selection.
            category_selection: int = int(
                input("Select an option by entering the corresponding number: ")
            )

            # If a valid category is selected.
            if category_selection in remove_categories:
                category_name, category_type = remove_categories[category_selection]
                print(f"\nCategory Selected: {category_name}")

                while True:
                    # Get the item name to remove from the user.
                    item_to_remove: str = (
                        input(f"Enter {category_name.replace('Remove a ', '')} Name: ")
                        .strip()
                        .title()
                    )

                    # Search for the item in the selected category.
                    item: dict[str, str | float] | None = next(
                        (
                            item
                            for item in category_type
                            if item["item_name"] == item_to_remove
                        ),
                        None,
                    )

                    # If the item is found, remove it.
                    if item:
                        category_type.remove(item)
                        print(f"\n{item_to_remove} is successfully removed!")

                        # Post remove options: Go back or exit.
                        while True:
                            try:
                                post_remove_selection: int = int(
                                    input(
                                        "Enter 1 to go back to the remove item menu or 2 to exit the program: "
                                    )
                                )
                                if post_remove_selection == 1:
                                    break
                                elif post_remove_selection == 2:
                                    sys.exit()
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Invalid input! Please try again.")
                        break

                    # If the item is not found, ask the user if they want to retry.
                    else:
                        print("Item not found! Do you want to try again?")
                        while True:
                            try:
                                retry_choice: int = int(
                                    input("Enter 1 for Yes or 2 for No: ")
                                )
                                if retry_choice == 1:
                                    status = "continue"
                                    break
                                elif retry_choice == 2:
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Invalid input! Please try again.")

                        # If the user chooses to retry, continue the loop.
                        if status == "continue":
                            continue
                        else:
                            break

            # Option to go back to the main menu.
            elif category_selection == 6:
                main_menu()

            # Option to exit the program.
            elif category_selection == 7:
                sys.exit()

            # Handle invalid selections for category.
            else:
                raise ValueError

        except ValueError:
            # Handle invalid input for category selection.
            print("Invalid input! Please try again.")


if __name__ == "__main__":
    main()
