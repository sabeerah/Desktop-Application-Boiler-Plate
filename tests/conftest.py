import pytest
import os 
import pyautogui
import csv
from pywinauto.application import Application
from pywinauto.controls.win32_controls import EditWrapper
from datetime import datetime, timezone
import allure

@pytest.fixture(scope="module")
def app():
    # Start the application
    app = Application(backend='uia').start("D:/CattleXpert/CattleXpert.exe")
    yield app
    # Ensure the application is closed after all tests
    app.kill()  

@pytest.fixture()
def take_screenshot():
    def _take_screenshot(file_name):

        # Define the screenshot directory relative to the project's root
        screenshot_dir = os.path.join(os.path.dirname(__file__), '..', 'screenshots')

        # Create the directory if it doesn't exist
        os.makedirs(screenshot_dir, exist_ok=True)

        # Get the current timestamp with UTC timezone
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

        # Add the timestamp to the file name
        file_name_with_timestamp = f"{file_name}_{timestamp}.png"

        # Define the full path for the screenshot
        screenshot_path = os.path.join(screenshot_dir, file_name_with_timestamp)

        # Take the screenshot and save it to the specified path
        pyautogui.screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        # Attach screenshot to Allure report
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=file_name_with_timestamp, attachment_type=allure.attachment_type.PNG)
        
        return screenshot_path
        
    return _take_screenshot

@pytest.fixture()
def login(app, take_screenshot):
    with open('credentials.csv', mode='r') as file:
        reader = csv.DictReader(file)
        credentials = next(reader)
        username = credentials['username']
        password = credentials['password']

    login_window = app.window(title="CattleXpert Login")

    username_field = EditWrapper(login_window.child_window(auto_id="4", control_type="Edit").wrapper_object())
    username_field.set_edit_text("")
    username_field.type_keys(username)

    password_field = login_window.child_window(auto_id="3", control_type="Edit").wrapper_object()
    password_field.type_keys(password)

    ok_button = login_window.child_window(title="OK", auto_id="2", control_type="Button").wrapper_object()
    ok_button.click()

    main_screen = app.window(title_re=".*CattleXpert - J.W. Freund Farms, Inc.*")
    
    if main_screen.exists(timeout=10):
        allure.step("Login successful.")
        take_screenshot("login_success")
        return app
    else:
        allure.step("Login failed. Taking screenshot.")
        take_screenshot("login_failure")
        app.kill()
        return None

@pytest.fixture
def main_screen(login):
    if login:
        return login.window(title_re=".*CattleXpert - J.W. Freund Farms, Inc.*")
    else:
        # If login fails, trigger the error screen handling
        error_screen = login.window(title="Program Error Intercepted", auto_id = "0")

        if error_screen.exists():

            take_screenshot("error_screen")
            allure.step("Error screen detected and screenshot taken.")
            print("Error screen detected and screenshot taken")
            login.kill()
            return error_screen
        
        else:
            pytest.fail("Login failed, and error screen could not be accessed.")


@pytest.fixture
def navigate_file(main_screen):
    main_screen.menu_select('File')
    yield main_screen

@pytest.fixture
def navigate_procurement(main_screen):
    main_screen.menu_select('Procurement')
    yield main_screen

@pytest.fixture
def navigate_commodity(main_screen):
    main_screen.menu_select('Commodity')  # Fixed the typo
    yield main_screen

@pytest.fixture
def navigate_receiving(main_screen):
    main_screen.menu_select('Receiving')
    yield main_screen

@pytest.fixture
def navigate_processing(main_screen):
    main_screen.menu_select('Processing')
    yield main_screen

@pytest.fixture
def navigate_ration(main_screen):
    main_screen.menu_select('Ration')
    yield main_screen

@pytest.fixture
def navigate_health(main_screen):
    main_screen.menu_select('Health')
    yield main_screen

@pytest.fixture
def navigate_invoice(main_screen):
    main_screen.menu_select('Invoice')
    yield main_screen

@pytest.fixture
def navigate_sales(main_screen):
    main_screen.menu_select('Sales')
    yield main_screen

@pytest.fixture
def navigate_risk_analysis(main_screen):
    main_screen.menu_select('Risk Analysis')
    yield main_screen

@pytest.fixture
def navigate_daily_jobs(main_screen):
    main_screen.menu_select('Daily Jobs')
    yield main_screen

@pytest.fixture
def navigate_view(main_screen):
    main_screen.menu_select('View')
    yield main_screen

@pytest.fixture
def navigate_window(main_screen):
    main_screen.menu_select('Window')
    yield main_screen

@pytest.fixture
def navigate_help(main_screen):
    main_screen.menu_select('Help')
    yield main_screen

@pytest.fixture
def navigate_reports(main_screen):
    main_screen.menu_select('Reports')
    yield main_screen

@pytest.fixture
def navigate_maintenance(main_screen):
    main_screen.menu_select('Maintenance')
    yield main_screen

@pytest.fixture
def exit_application(main_screen):
    exit_button = main_screen.child_window(auto_id="1", title="Exit").wrapper_object()
    exit_button.click()
    yield

@pytest.fixture
def navigate_to_reports_commodity_scale(main_screen):
    main_screen.menu_select('Reports -> Commodity')
    return main_screen

@pytest.fixture
def navigate_to_processing_cattleboard(main_screen):
    main_screen.menu_select('Processing -> Cattle Board')
    return main_screen

@pytest.fixture
def navigate_to_contract(main_screen):
    main_screen.menu_select('Commodity -> Contract')
    return main_screen

@pytest.fixture
def navigate_to_ration_actual_feed(main_screen):
    main_screen.menu_select('Ration -> Actual Feed Edit')
    return main_screen

@pytest.fixture
def navigate_to_pen_consumption_graph(main_screen):
    main_screen.menu_select("Ration -> Pen Consumption Graph")
    pen_consumption_graph = main_screen.window(title_re=".*Pen Consumption Graph.*")
    pen_consumption_graph.wait('exists', timeout=100)
    return pen_consumption_graph

@pytest.fixture
def navigate_to_feed_status(main_screen):
    main_screen.menu_select("Ration -> Feed Status")
    return main_screen


# @pytest.fixture
# def ration_page(main_screen):
#     return RationPage(main_screen)

# @pytest.fixture
# def navigate_to_manual_feed_entry(ration_page):
#     ration_page.navigate_to_manual_feed_entry()
#     yield ration_page

# @pytest.fixture
# def enter_ration_details(navigate_to_manual_feed_entry):
#     navigate_to_manual_feed_entry.enter_ration_details("CTC{SPACE}50gr", "Feed{SPACE}Rain")
#     yield navigate_to_manual_feed_entry

# @pytest.fixture
# def select_pen_and_retrieve(enter_ration_details):
#     enter_ration_details.select_pen_and_retrieve()
#     yield enter_ration_details

# @pytest.fixture
# def close_manual_feed_entry(select_pen_and_retrieve):
#     select_pen_and_retrieve.close_manual_feed_entry()
#     yield select_pen_and_retrieve