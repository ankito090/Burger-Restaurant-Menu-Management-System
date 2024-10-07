import pytest
import project


def test_validation(monkeypatch, capsys):
    validation = project.Validation

    def test_item_name_validation():

        def test_valid_item_name():
            # Test for valid item name
            input = (
                "Chicken Sausage Burger"  # Simulate user providing a valid item name
            )
            monkeypatch.setattr("builtins.input", lambda _: input)  # Mock user input
            assert (
                validation.validate_name() == "Chicken Sausage Burger"
            )  # Check if item name is validated correctly and the method returned it

        def test_invalid_item_name_1():
            # Test for invalid name (too short)
            inputs = iter(
                ["Na", 2]
            )  # Simulate user providing a too short invalid name and choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_name()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid name! Please ensure the following:" in captured.out
            )  # Verify the invalid name message
            assert (
                "1. Name should not be empty." in captured.out
            )  # Verify the invalid name message
            assert (
                "2. Name should be between 3 and 50 characters long." in captured.out
            )  # Verify the invalid name message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result is None
            )  # Check if item name is failed to validate and the method returned None

        def test_invalid_item_name_2():
            # Test for invalid name (too long)
            inputs = iter(
                [
                    "Chicken Sausage Burger with Extra Cheese, Crispy Bacon, Fresh Lettuce, and Tangy Tomato Sauce",
                    2,
                ]
            )  # Simulate user providing a too long invalid name and choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_name()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid name! Please ensure the following:" in captured.out
            )  # Verify the invalid name message
            assert (
                "1. Name should not be empty." in captured.out
            )  # Verify the invalid name message
            assert (
                "2. Name should be between 3 and 50 characters long." in captured.out
            )  # Verify the invalid name message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result is None
            )  # Check if item name is failed to validate and the method returned None

        def test_retry_mechanism():
            # Test for retry mechanism
            inputs = iter(
                ["Na", 1, "Chicken Sausage Burger"]
            )  # Simulate user entering invalid name, retrying, and then valid name
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_name()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid name! Please ensure the following:" in captured.out
            )  # Verify the invalid name message
            assert (
                "1. Name should not be empty." in captured.out
            )  # Verify the invalid name message
            assert (
                "2. Name should be between 3 and 50 characters long." in captured.out
            )  # Verify the invalid name message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result == "Chicken Sausage Burger"
            )  # Check if item name is validated correctly and the method returned it

        def test_invalid_retry_selection_1():
            # Test for invalid retry selection with a valid data-type
            inputs = iter(
                ["Na", 3, 2]
            )  # Simulate user trying to select an invalid retry option (3), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_name()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid name! Please ensure the following:" in captured.out
            )  # Verify the invalid name message
            assert (
                "1. Name should not be empty." in captured.out
            )  # Verify the invalid name message
            assert (
                "2. Name should be between 3 and 50 characters long." in captured.out
            )  # Verify the invalid name message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                "Invalid input! Please try again." in captured.out
            )  # Verify the output for invalid retry selection
            assert (
                result is None
            )  # Check if item name is failed to validate and the method returned None

        def test_invalid_retry_selection_2():
            # Test for invalid retry selection with an invalid data-type
            inputs = iter(
                ["Na", "Na", 2]
            )  # Simulate user selecting an invalid retry option ("Na") with an invalid data-type (str), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_name()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid name! Please ensure the following:" in captured.out
            )  # Verify the invalid name message
            assert (
                "1. Name should not be empty." in captured.out
            )  # Verify the invalid name message
            assert (
                "2. Name should be between 3 and 50 characters long." in captured.out
            )  # Verify the invalid name message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                "Invalid input! Please try again." in captured.out
            )  # Verify the output for invalid retry selection
            assert (
                result is None
            )  # Check if item name is failed to validate and the method returned None

        # Run all the tests
        test_valid_item_name()
        test_invalid_item_name_1()
        test_invalid_item_name_2()
        test_retry_mechanism()
        test_invalid_retry_selection_1()
        test_invalid_retry_selection_2()

    def test_item_description_validation():

        def test_valid_item_description():
            # Test for valid item description
            input = "Juicy chicken sausage patty in a toasted bun with fresh lettuce, tomato, and a hint of mayo for a flavorful bite."  # Simulate user providing a valid item description
            monkeypatch.setattr("builtins.input", lambda _: input)  # Mock user input
            assert (
                validation.validate_description()
                == "Juicy chicken sausage patty in a toasted bun with fresh lettuce, tomato, and a hint of mayo for a flavorful bite."
            )  # Check if item description is validated correctly and the method returned it

        def test_invalid_item_description_1():
            # Test for invalid description (too short)
            inputs = iter(
                ["Na", 2]
            )  # Simulate user providing a too short invalid description and choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_description()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid description! Please ensure the following:" in captured.out
            )  # Verify the invalid description message
            assert (
                "1. Description should not be empty." in captured.out
            )  # Verify the invalid description message
            assert (
                "2. Description should be between 10 and 150 characters long."
                in captured.out
            )  # Verify the invalid description message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result is None
            )  # Check if item description is failed to validate and the method returned None

        def test_invalid_item_description_2():
            # Test for invalid description (too long)
            inputs = iter(
                [
                    "A delicious chicken sausage patty, grilled to perfection, served in a toasted bun with crisp lettuce, fresh tomatoes, creamy mayo, tangy mustard, and melted cheese, topped with pickles and onions for extra flavor.",
                    2,
                ]
            )  # Simulate user providing a too long invalid description and choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_description()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid description! Please ensure the following:" in captured.out
            )  # Verify the invalid description message
            assert (
                "1. Description should not be empty." in captured.out
            )  # Verify the invalid description message
            assert (
                "2. Description should be between 10 and 150 characters long."
                in captured.out
            )  # Verify the invalid description message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result is None
            )  # Check if item description is failed to validate and the method returned None

        def test_retry_mechanism():
            # Test for retry mechanism
            inputs = iter(
                [
                    "Na",
                    1,
                    "Juicy chicken sausage patty in a toasted bun with fresh lettuce, tomato, and a hint of mayo for a flavorful bite.",
                ]
            )  # Simulate user entering invalid description, retrying, and then valid diet type
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_description()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid description! Please ensure the following:" in captured.out
            )  # Verify the invalid description message
            assert (
                "1. Description should not be empty." in captured.out
            )  # Verify the invalid description message
            assert (
                "2. Description should be between 10 and 150 characters long."
                in captured.out
            )  # Verify the invalid description message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result
                == "Juicy chicken sausage patty in a toasted bun with fresh lettuce, tomato, and a hint of mayo for a flavorful bite."
            )  # Check if item description is validated correctly and the method returned it

        def test_invalid_retry_selection_1():
            # Test for invalid retry selection with a valid data-type
            inputs = iter(
                ["Na", 3, 2]
            )  # Simulate user trying to select an invalid retry option (3), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_description()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid description! Please ensure the following:" in captured.out
            )  # Verify the invalid description message
            assert (
                "1. Description should not be empty." in captured.out
            )  # Verify the invalid description message
            assert (
                "2. Description should be between 10 and 150 characters long."
                in captured.out
            )  # Verify the invalid description message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                "Invalid input! Please try again." in captured.out
            )  # Verify the output for invalid retry selection
            assert (
                result is None
            )  # Check if item description is failed to validate and the method returned None

        def test_invalid_retry_selection_2():
            # Test for invalid retry selection with an invalid data-type
            inputs = iter(
                ["Na", "Na", 2]
            )  # Simulate user selecting an invalid retry option ("Na") with an invalid data-type (str), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_description()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid description! Please ensure the following:" in captured.out
            )  # Verify the invalid description message
            assert (
                "1. Description should not be empty." in captured.out
            )  # Verify the invalid description message
            assert (
                "2. Description should be between 10 and 150 characters long."
                in captured.out
            )  # Verify the invalid description message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                "Invalid input! Please try again." in captured.out
            )  # Verify the output for invalid retry selection
            assert (
                result is None
            )  # Check if item description is failed to validate and the method returned None

        # Run all the tests
        test_valid_item_description()
        test_invalid_item_description_1()
        test_invalid_item_description_2()
        test_retry_mechanism()
        test_invalid_retry_selection_1()
        test_invalid_retry_selection_2()

    def test_diet_type_validation():

        def test_valid_diet_type_1():
            # Test for valid item diet type
            input = 1  # Simulate user selecting a valid item diet type
            monkeypatch.setattr("builtins.input", lambda _: input)  # Mock user input
            assert (
                validation.validate_diet_type() == "Veg"
            )  # Check if item diet type is validated correctly and the method returned "Veg"

        def test_valid_diet_type_2():
            # Test for valid item diet type
            input = 2  # Simulate user selecting a valid item diet type
            monkeypatch.setattr("builtins.input", lambda _: input)  # Mock user input
            assert (
                validation.validate_diet_type() == "Non-Veg"
            )  # Check if item diet type is validated correctly and the method returned "Non-Veg"

        def test_invalid_diet_type_1():
            # Test for invalid diet type with a valid data-type
            inputs = iter(
                [3, 2]
            )  # Simulate user providing an invalid input for diet type (3), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_diet_type()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid diet type! Please ensure the following:" in captured.out
            )  # Verify the invalid diet type message
            assert (
                "1. Enter 1 to apply Veg." in captured.out
            )  # Verify the invalid diet type message
            assert (
                "2. Enter 2 to apply Non-Veg." in captured.out
            )  # Verify the invalid diet type message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result is None
            )  # Check if item diet type is failed to validate and the method returned None

        def test_invalid_diet_type_2():
            # Test for invalid diet type with an invalid data-type
            inputs = iter(
                ["Non-Veg", 2]
            )  # Simulate user providing an invalid input for diet type ("Non-Veg") with an invalid data-type (str), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_diet_type()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid diet type! Please ensure the following:" in captured.out
            )  # Verify the invalid diet type message
            assert (
                "1. Enter 1 to apply Veg." in captured.out
            )  # Verify the invalid diet type message
            assert (
                "2. Enter 2 to apply Non-Veg." in captured.out
            )  # Verify the invalid diet type message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result is None
            )  # Check if item diet type is failed to validate and the method returned None

        def test_retry_mechanism():
            # Test for retry mechanism
            inputs = iter(
                [3, 1, 2]
            )  # Simulate user entering invalid diet type, retrying, and then valid diet type
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_diet_type()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid diet type! Please ensure the following:" in captured.out
            )  # Verify the invalid diet type message
            assert (
                "1. Enter 1 to apply Veg." in captured.out
            )  # Verify the invalid diet type message
            assert (
                "2. Enter 2 to apply Non-Veg." in captured.out
            )  # Verify the invalid diet type message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result == "Non-Veg"
            )  # Check if item diet type is validated correctly and the method returned it

        def test_invalid_retry_selection_1():
            # Test for invalid retry selection with a valid data-type
            inputs = iter(
                ["Non-Veg", 3, 2]
            )  # Simulate user trying to select an invalid retry option (3), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_diet_type()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid diet type! Please ensure the following:" in captured.out
            )  # Verify the invalid diet type message
            assert (
                "1. Enter 1 to apply Veg." in captured.out
            )  # Verify the invalid diet type message
            assert (
                "2. Enter 2 to apply Non-Veg." in captured.out
            )  # Verify the invalid diet type message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                "Invalid input! Please try again." in captured.out
            )  # Verify the output for invalid retry selection
            assert (
                result is None
            )  # Check if item diet type is failed to validate and the method returned None

        def test_invalid_retry_selection_2():
            # Test for invalid retry selection with an invalid data-type
            inputs = iter(
                ["Non-Veg", "Na", 2]
            )  # Simulate user selecting an invalid retry option ("Na") with an invalid data-type (str), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_diet_type()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid diet type! Please ensure the following:" in captured.out
            )  # Verify the invalid diet type message
            assert (
                "1. Enter 1 to apply Veg." in captured.out
            )  # Verify the invalid diet type message
            assert (
                "2. Enter 2 to apply Non-Veg." in captured.out
            )  # Verify the invalid diet type message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                "Invalid input! Please try again." in captured.out
            )  # Verify the output for invalid retry selection
            assert (
                result is None
            )  # Check if item diet type is failed to validate and the method returned None

        # Run all the tests
        test_valid_diet_type_1()
        test_valid_diet_type_2()
        test_invalid_diet_type_1()
        test_invalid_diet_type_2()
        test_retry_mechanism()
        test_invalid_retry_selection_1()
        test_invalid_retry_selection_2()

    def test_unit_price_validation():

        def test_valid_unit_price():
            # Test for valid item unit price
            input = 209.99  # Simulate user selecting a valid item unit price
            monkeypatch.setattr("builtins.input", lambda _: input)  # Mock user input
            assert (
                validation.validate_unit_price() == 209.99
            )  # Check if item unit price is validated correctly and the method returned it

        def test_invalid_unit_price_1():
            # Test for invalid unit price by providing an empty value
            inputs = iter(
                ["", 2]
            )  # Simulate user trying to provide an empty unit price, and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_unit_price()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid unit price! Please ensure the following:" in captured.out
            )  # Verify the invalid unit price message
            assert (
                "1. Unit price should not be empty." in captured.out
            )  # Verify the invalid unit price message
            assert (
                "2. Unit price should be a positive numerical value." in captured.out
            )  # Verify the invalid unit price message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result is None
            )  # Check if item unit price is failed to validate and the method returned None

        def test_invalid_unit_price_2():
            # Test for invalid unit price by providing a negative unit price
            inputs = iter(
                [-209.99, 2]
            )  # Simulate user trying to provide a negative unit price (-209.99), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_unit_price()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid unit price! Please ensure the following:" in captured.out
            )  # Verify the invalid unit price message
            assert (
                "1. Unit price should not be empty." in captured.out
            )  # Verify the invalid unit price message
            assert (
                "2. Unit price should be a positive numerical value." in captured.out
            )  # Verify the invalid unit price message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result is None
            )  # Check if item unit price is failed to validate and the method returned None

        def test_invalid_unit_price_3():
            # Test for invalid unit price with an invalid data-type
            inputs = iter(
                ["Two hundred nine point ninety nine", 2]
            )  # Simulate user providing an invalid unit price ("Two hundred nine point ninety nine") with an invalid data-type (str), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_unit_price()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid unit price! Please ensure the following:" in captured.out
            )  # Verify the invalid unit price message
            assert (
                "1. Unit price should not be empty." in captured.out
            )  # Verify the invalid unit price message
            assert (
                "2. Unit price should be a positive numerical value." in captured.out
            )  # Verify the invalid unit price message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result is None
            )  # Check if item unit price is failed to validate and the method returned None

        def test_retry_mechanism():
            # Test for retry mechanism
            inputs = iter(
                ["Two hundred nine point ninety nine", 1, 209.99]
            )  # Simulate user entering invalid unit price, retrying, and then valid unit price
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_unit_price()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid unit price! Please ensure the following:" in captured.out
            )  # Verify the invalid unit price message
            assert (
                "1. Unit price should not be empty." in captured.out
            )  # Verify the invalid unit price message
            assert (
                "2. Unit price should be a positive numerical value." in captured.out
            )  # Verify the invalid unit price message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                result == 209.99
            )  # Check if item unit price is validated correctly and the method returned it

        def test_invalid_retry_selection_1():
            # Test for invalid retry selection with a valid data-type
            inputs = iter(
                ["Two hundred nine point ninety nine", 3, 2]
            )  # Simulate user trying to select an invalid retry option (3), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_unit_price()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid unit price! Please ensure the following:" in captured.out
            )  # Verify the invalid unit price message
            assert (
                "1. Unit price should not be empty." in captured.out
            )  # Verify the invalid unit price message
            assert (
                "2. Unit price should be a positive numerical value." in captured.out
            )  # Verify the invalid unit price message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                "Invalid input! Please try again." in captured.out
            )  # Verify the output for invalid retry selection
            assert (
                result is None
            )  # Check if item unit price is failed to validate and the method returned None

        def test_invalid_retry_selection_2():
            # Test for invalid retry selection with an invalid data-type
            inputs = iter(
                ["Two hundred nine point ninety nine", "Na", 2]
            )  # Simulate user selecting an invalid retry option ("Na") with an invalid data-type (str), and then choosing not to retry
            monkeypatch.setattr(
                "builtins.input", lambda _: next(inputs)
            )  # Mock user input
            result = validation.validate_unit_price()  # Perform validation
            captured = capsys.readouterr()  # Capture the error message
            assert (
                "Invalid unit price! Please ensure the following:" in captured.out
            )  # Verify the invalid unit price message
            assert (
                "1. Unit price should not be empty." in captured.out
            )  # Verify the invalid unit price message
            assert (
                "2. Unit price should be a positive numerical value." in captured.out
            )  # Verify the invalid unit price message
            assert "Do you want to retry?" in captured.out  # Verify the retry message
            assert (
                "Invalid input! Please try again." in captured.out
            )  # Verify the output for invalid retry selection
            assert (
                result is None
            )  # Check if item unit price is failed to validate and the method returned None

        # Run all the tests
        test_valid_unit_price()
        test_invalid_unit_price_1()
        test_invalid_unit_price_2()
        test_invalid_unit_price_3()
        test_retry_mechanism()
        test_invalid_retry_selection_1()
        test_invalid_retry_selection_2()

    # Run all the tests
    test_item_name_validation()
    test_item_description_validation()
    test_diet_type_validation()
    test_unit_price_validation()


def test_main_menu(monkeypatch, capsys):

    def test_view_menu_selection():
        # Test for selecting View Menu
        inputs = iter(
            [1, 6, 5]
        )  # Simulate user selecting View Menu, coming back to the main menu, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.main_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: View Menu" in captured.out
        )  # Verify the output for valid category selection

    def test_add_item_selection():
        # Test for selecting Add an Item
        inputs = iter(
            [2, 6, 5]
        )  # Simulate user selecting Add an Item, coming back to the main menu, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.main_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add an Item" in captured.out
        )  # Verify the output for valid category selection

    def test_update_item_selection():
        # Test for selecting Update an Item
        inputs = iter(
            [3, 6, 5]
        )  # Simulate user selecting Update an Item, coming back to the main menu, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.main_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update an Item" in captured.out
        )  # Verify the output for valid category selection

    def test_remove_item_selection():
        # Test for selecting Remove an Item
        inputs = iter(
            [4, 6, 5]
        )  # Simulate user selecting Remove an Item, coming back to the main menu, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.main_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Remove an Item" in captured.out
        )  # Verify the output for valid category selection

    def test_invalid_category_selection_1():
        # Test for invalid category selection with a valid data-type
        inputs = iter(
            [6, 5]
        )  # Simulate user selecting an invalid category (6), and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.main_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    def test_invalid_category_selection_2():
        # Test for invalid category selection with an invalid data-type
        inputs = iter(
            ["Six", 5]
        )  # Simulate user selecting a invalid category ("Six") with an invalid data-type (str), and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.main_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    # Run all the tests
    test_view_menu_selection()
    test_add_item_selection()
    test_update_item_selection()
    test_remove_item_selection()
    test_invalid_category_selection_1()
    test_invalid_category_selection_2()


def test_view_menu(monkeypatch, capsys):

    def test_valid_category_selection():
        # Test for valid category selection
        inputs = iter(
            [1, 2]
        )  # Simulate user selecting to view burgers, and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.view_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Burgers" in captured.out
        )  # Verify the output for valid category selection

    def test_invalid_category_selection_1():
        # Test for invalid category selection with a valid data-type
        inputs = iter(
            [8, 7]
        )  # Simulate user selecting an invalid category (8), and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.view_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    def test_invalid_category_selection_2():
        # Test for invalid category selection with an invalid data-type
        inputs = iter(
            ["Eight", 7]
        )  # Simulate user selecting a invalid category ("Eight") with an invalid data-type (str), and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.view_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    def test_valid_post_view_selection():
        # Test for valid post-view category selection
        inputs = iter(
            [2, 1, 7]
        )  # Simulate user selecting to go back after viewing the meals category, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.view_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Meals" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Category Selected: View Menu" in captured.out
        )  # Verify going back to the view menu category

    def test_invalid_post_view_selection_1():
        # Test for invalid post-view selection with a valid data-type
        inputs = iter(
            [2, 3, 2]
        )  # Simulate user trying to select an invalid post-view option (3) after viewing the meals category, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.view_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Meals" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid post-view selection

    def test_invalid_post_view_selection_2():
        # Test for invalid post-view selection with an invalid data-type
        inputs = iter(
            [3, "three", 2]
        )  # Simulate user trying to select an invalid post-view option ("three") with an invalid data-type (str) after viewing the snacks category, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.view_menu()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Snacks" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid post-view selection

    # Run all the tests
    test_valid_category_selection()
    test_invalid_category_selection_1()
    test_invalid_category_selection_2()
    test_valid_post_view_selection()
    test_invalid_post_view_selection_1()
    test_invalid_post_view_selection_2()


def test_add_item(monkeypatch, capsys):

    def test_valid_item_addition():
        # Test for valid item addition
        inputs = iter(
            [
                1,
                "Ankito's Special Burger",
                "A unique burger with a special blend of flavors exclusive to our restaurant",
                2,
                229.99,
                2,
            ]
        )  # Simulate user choosing to add a burger and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add a Burger" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Ankito's Special Burger is successfully added!" in captured.out
        )  # Verify the success message

    def test_invalid_category_selection_1():
        # Test for invalid category selection with a valid data-type
        inputs = iter(
            [8, 7]
        )  # Simulate user selecting an invalid category (8) and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    def test_invalid_category_selection_2():
        # Test for invalid category selection with an invalid data-type
        inputs = iter(
            ["Eight", 7]
        )  # Simulate user selecting a invalid category ("Eight") with an invalid data-type (str), and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    def test_existing_item_addition():
        # Test for existing item addition
        inputs = iter(
            [
                5,
                "Apple Pie",
                "Classic apple pie with cinnamon",
                1,
                199.99,
                2,
            ]
        )  # Simulate user choosing to add an already existing dessert and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add a Dessert" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Apple Pie already exists!" in captured.out
        )  # Verify that the item already exists

    def test_item_addition_fail_1():
        # Test for failing to add an item due to invalid name
        inputs = iter(
            [3, "Na", 2, 7]
        )  # Simulate user trying to add a snack by entering an invalid item name and choosing not to try again
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add a Snack" in captured.out
        )  # Verify the output for valid category selection
        assert "Failed to add an item" in captured.out  # Verify the failure message

    def test_item_addition_fail_2():
        # Test for failing to add an item due to invalid item description
        inputs = iter(
            [3, "Chicken Popcorn", "Na", 2, 7]
        )  # Simulate user trying to add a snack by entering an invalid item description and choosing not to try again
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add a Snack" in captured.out
        )  # Verify the output for valid category selection
        assert "Failed to add an item" in captured.out  # Verify the failure message

    def test_item_addition_fail_3():
        # Test for failing to add an item due to invalid diet type
        inputs = iter(
            [3, "Chicken Popcorn", "Crunchy bite-sized chicken popcorn", 3, 2, 7]
        )  # Simulate user trying to add a snack by entering an invalid item diet type and choosing not to try again
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add a Snack" in captured.out
        )  # Verify the output for valid category selection
        assert "Failed to add an item" in captured.out  # Verify the failure message

    def test_item_addition_fail_4():
        # Test for failing to add an item due to invalid unit price
        inputs = iter(
            [
                3,
                "Chicken Popcorn",
                "Crunchy bite-sized chicken popcorn",
                2,
                -149.99,
                2,
                7,
            ]
        )  # Simulate user trying to add a snack by entering an invalid item unit price and choosing not to try again
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add a Snack" in captured.out
        )  # Verify the output for valid category selection
        assert "Failed to add an item" in captured.out  # Verify the failure message

    def test_valid_post_add_selection():
        # Test for valid post-add selection
        inputs = iter(
            [
                2,
                "Grilled Chicken Caesar Salad",
                "A healthy salad with grilled chicken, romaine lettuce, parmesan cheese, and Caesar dressing",
                2,
                279.99,
                1,
                7,
            ]
        )  # Simulate user selecting to go back after adding a meal, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Grilled Chicken Caesar Salad is successfully added!" in captured.out
        )  # Verify the success message
        assert (
            "Category Selected: Add an Item" in captured.out
        )  # Verify going back to the add an item category

    def test_invalid_post_add_selection_1():
        # Test for invalid post-add selection with a valid data-type
        inputs = iter(
            [
                4,
                "Sprite",
                "Chilled Sprite (500 ml)",
                1,
                59.99,
                3,
                2,
            ]
        )  # Simulate user trying to select an invalid post-add option (3) after adding a beverage, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add a Beverage" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Sprite is successfully added!" in captured.out
        )  # Verify the success message
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid post-add selection

    def test_invalid_post_add_selection_2():
        # Test for invalid post-add selection with an invalid data-type
        inputs = iter(
            [
                4,
                "7 Up",
                "Chilled 7 Up (500 ml)",
                1,
                59.99,
                "three",
                2,
            ]
        )  # Simulate user trying to select an invalid post-add option ("three") with an invalid data-type (str) after adding a beverage, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.add_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Add a Beverage" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid post-add selection

    # Run all the tests:
    test_valid_item_addition()
    test_invalid_category_selection_1()
    test_invalid_category_selection_2()
    test_existing_item_addition()
    test_item_addition_fail_1()
    test_item_addition_fail_2()
    test_item_addition_fail_3()
    test_item_addition_fail_4()
    test_valid_post_add_selection()
    test_invalid_post_add_selection_1()
    test_invalid_post_add_selection_2()


def test_update_item(monkeypatch, capsys):

    def test_valid_item_update_1():
        # Test for valid item update by updating an item's name
        inputs = iter(
            [2, "Chicken Tenders Meal", 1, "Chicken Tenders Combo Meal", 2]
        )  # Simulate user choosing to update the name of a meal, and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item Selected: Chicken Tenders Meal" in captured.out
        )  # Verify the output for valid item selection
        assert (
            "Item name is successfully updated!" in captured.out
        )  # Verify the success message

    def test_valid_item_update_2():
        # Test for valid item update by updating an item's description
        inputs = iter(
            [
                2,
                "Chicken Tenders Combo Meal",
                2,
                "Crispy chicken tenders served with creamy mashed potatoes and rich gravy",
                2,
            ]
        )  # Simulate user choosing to update the description of a meal, and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item Selected: Chicken Tenders Combo Meal" in captured.out
        )  # Verify the output for valid item selection
        assert (
            "Item description is successfully updated!" in captured.out
        )  # Verify the success message

    def test_valid_item_update_3():
        # Test for valid item update by updating an item's diet type
        inputs_1 = iter(
            [2, "Chicken Tenders Combo Meal", 3, 1, 2]
        )  # Simulate user choosing to update the diet type of a meal to veg, and choosing to exit
        monkeypatch.setattr(
            "builtins.input", lambda _: next(inputs_1)
        )  # Mock user input
        inputs_2 = iter(
            [2, "Chicken Tenders Combo Meal", 3, 2, 2]
        )  # Simulate user again choosing to update the diet type of a meal back to Non-Veg, and choosing to exit
        monkeypatch.setattr(
            "builtins.input", lambda _: next(inputs_2)
        )  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item Selected: Chicken Tenders Combo Meal" in captured.out
        )  # Verify the output for valid item selection
        assert (
            "Item diet type is successfully updated!" in captured.out
        )  # Verify the success message

    def test_valid_item_update_4():
        # Test for valid item update by updating an item's name
        inputs = iter(
            [2, "Chicken Tenders Combo Meal", 4, 309.99, 2]
        )  # Simulate user choosing to update the unit price of a meal, and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item Selected: Chicken Tenders Combo Meal" in captured.out
        )  # Verify the output for valid item selection
        assert (
            "Item unit price is successfully updated!" in captured.out
        )  # Verify the success message

    def test_valid_item_update_5():
        # Test for valid item update by updating an item's name
        inputs = iter(
            [2, "Chicken Tenders Combo Meal", 5, 7]
        )  # Simulate user choosing to update the unit price of a meal, deciding to go back and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item Selected: Chicken Tenders Combo Meal" in captured.out
        )  # Verify the output for valid item selection
        assert (
            "Category Selected: Update an Item" in captured.out
        )  # Verify going back to the "Update an Item" menu

    def test_invalid_category_selection_1():
        # Test for invalid category selection with a valid data-type
        inputs = iter(
            [8, 7]
        )  # Simulate user selecting an invalid category (8) and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    def test_invalid_category_selection_2():
        # Test for invalid category selection with an invalid data-type
        inputs = iter(
            ["Eight", 7]
        )  # Simulate user selecting a invalid category ("Eight") with an invalid data-type (str), and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    def test_invalid_item_name_1():
        # Test for entering invalid item name and then correcting it
        inputs = iter(
            [3, "Potato Fries", 2, 7]
        )  # Simulate user trying to update a snack by providing invalid item name, refusing to try again, and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output

        assert (
            "Category Selected: Update a Snack" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item not found! Do you want to try again?" in captured.out
        )  # Verify the item not found message

    def test_invalid_item_name_2():
        # Test for entering invalid item name and then correcting it and then correcting it
        inputs = iter(
            [3, "Potato Fries", 1, "Fries", 2, "Crispy golden fries (Regular)", 2]
        )  # Simulate user trying to update a snack by providing invalid item name, correcting it to update the description, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Snack" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item not found! Do you want to try again?" in captured.out
        )  # Verify the item not found message
        assert (
            "Item Selected: Fries" in captured.out
        )  # Verify the output for valid item selection
        assert (
            "Item description is successfully updated!" in captured.out
        )  # Verify the success message

    def test_invalid_update_category_selection():
        # Test for invalid update category selection
        inputs = iter(
            [4, "Coca-Cola", 6, 4, 49.99, 2]
        )  # Simulate user trying to update a beverage, selecting an invalid update category, correcting it to update the unit price, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Beverage" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item Selected: Coca-Cola" in captured.out
        )  # Verify the output for valid item selection
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid update category selection
        assert (
            "Item unit price is successfully updated!" in captured.out
        )  # Verify the success message

    def test_item_update_fail():
        # Test for failing to update a item
        inputs = iter(
            [5, "Brownie Sundae", 2, "Non", 2, 7]
        )  # Simulate user trying to update a dessert by entering an invalid item description and choosing not to try again
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Dessert" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item Selected: Brownie Sundae" in captured.out
        )  # Verify the output for valid item selection
        assert "Failed to update an item" in captured.out  # Verify the failure message

    def test_valid_post_update_selection():
        # Test for valid post-update selection
        inputs = iter(
            [1, "Classic Chicken Burger", 4, 209.99, 1, 7]
        )  # Simulate user selecting to go back after updating a burger, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Burger" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item Selected: Classic Chicken Burger" in captured.out
        )  # Verify the output for valid item selection
        assert (
            "Item unit price is successfully updated!" in captured.out
        )  # Verify the success message
        assert (
            "Category Selected: Update an Item" in captured.out
        )  # Verify going back to the "Update an Item" menu

    def test_invalid_post_update_selection_1():
        # Test for invalid post-update selection with a valid data-type
        inputs = iter(
            [
                2,
                "Chicken Combo Meal",
                2,
                "Double chicken breast with mashed potatoes and vegetables",
                3,
                2,
            ]
        )  # Simulate user trying to select an invalid post-update option (3) after updating a meal, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item Selected: Chicken Combo Meal" in captured.out
        )  # Verify the output for valid item selection
        assert (
            "Item description is successfully updated!" in captured.out
        )  # Verify the success message
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid post-update selection

    def test_invalid_post_update_selection_2():
        # Test for invalid post-update selection with an invalid data-type
        inputs = iter(
            [
                2,
                "Chicken Combo Meal",
                2,
                "Double chicken breast with mashed potatoes, vegetables and a Coca-Cola",
                "three",
                2,
            ]
        )  # Simulate user trying to select an invalid post-update option ("three") with an invalid data-type (str) after updating a meal, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.update_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Update a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid post-update selection

    # Run all the tests
    test_valid_item_update_1()
    test_valid_item_update_2()
    test_valid_item_update_3()
    test_valid_item_update_4()
    test_valid_item_update_5()
    test_invalid_category_selection_1()
    test_invalid_category_selection_2()
    test_invalid_item_name_1()
    test_invalid_item_name_2()
    test_invalid_update_category_selection()
    test_item_update_fail()
    test_valid_post_update_selection()
    test_invalid_post_update_selection_1()
    test_invalid_post_update_selection_2()


def test_remove_item(monkeypatch, capsys):
    def test_valid_item_removal():
        # Test for valid item removal
        inputs = iter(
            [1, "Classic Chicken Burger", 2]
        )  # Simulate user choosing to remove a burger, and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.remove_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Remove a Burger" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Classic Chicken Burger is successfully removed!" in captured.out
        )  # Verify the success message

    def test_invalid_category_selection_1():
        # Test for invalid category selection with a valid data-type
        inputs = iter(
            [8, 7]
        )  # Simulate user selecting an invalid category (8) and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.remove_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    def test_invalid_category_selection_2():
        # Test for invalid category selection with an invalid data-type
        inputs = iter(
            ["Eight", 7]
        )  # Simulate user selecting a invalid category ("Eight") with an invalid data-type (str), and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.remove_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid category selection

    def test_invalid_item_name_1():
        # Test for entering invalid item name and then correcting it
        inputs = iter(
            [2, "Chicken Combo Meals", 2, 7]
        )  # Simulate user trying to remove a meal by providing invalid item name, refusing to try again, and choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.remove_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output

        assert (
            "Category Selected: Remove a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item not found! Do you want to try again?" in captured.out
        )  # Verify the item not found message

    def test_invalid_item_name_2():
        # Test for entering invalid item name and then correcting it
        inputs = iter(
            [2, "Chicken Combo Meals", 1, "Chicken Combo Meal", 2]
        )  # Simulate user trying to remove a meal by providing invalid item name, correcting it, remove the meal, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.remove_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Remove a Meal" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Item not found! Do you want to try again?" in captured.out
        )  # Verify the item not found message
        assert (
            "Chicken Combo Meal is successfully removed!" in captured.out
        )  # Verify the success message

    def test_valid_post_remove_selection():
        # Test for valid post-remove selection
        inputs = iter(
            [3, "Onion Rings", 1, 7]
        )  # Simulate user selecting to go back after removing a snack, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.remove_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Remove a Snack" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Onion Rings is successfully removed!" in captured.out
        )  # Verify the success message
        assert (
            "Category Selected: Remove an Item" in captured.out
        )  # Verify going back to the "Remove an Item" menu

    def test_invalid_post_remove_selection_1():
        # Test for invalid post-remove selection with a valid data-type
        inputs = iter(
            [4, "Sparkling Water", 3, 2]
        )  # Simulate user trying to select an invalid post-remove option (3) after removing a beverage, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.remove_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Remove a Beverage" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Sparkling Water is successfully removed!" in captured.out
        )  # Verify the success message
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid post-remove selection

    def test_invalid_post_remove_selection_2():
        # Test for invalid post-remove selection with an invalid data-type
        inputs = iter(
            [4, "Iced tea", "three", 2]
        )  # Simulate user trying to select an invalid post-remove option ("three") with an invalid data-type (str) after removing a beverage, and then choosing to exit
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))  # Mock user input
        with pytest.raises(SystemExit):
            project.remove_item()  # Run the function and check for SystemExit
        captured = capsys.readouterr()  # Capture the output
        assert (
            "Category Selected: Remove a Beverage" in captured.out
        )  # Verify the output for valid category selection
        assert (
            "Invalid input! Please try again." in captured.out
        )  # Verify the output for invalid post-remove selection

    # Run all the tests
    test_valid_item_removal()
    test_invalid_category_selection_1()
    test_invalid_category_selection_2()
    test_invalid_item_name_1()
    test_invalid_item_name_2()
    test_valid_post_remove_selection()
    test_invalid_post_remove_selection_1()
    test_invalid_post_remove_selection_2()
