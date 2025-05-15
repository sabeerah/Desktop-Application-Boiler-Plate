import pytest

def test_login(login):
    if login is not None:
        main_screen = login.window(title_re=".*CattleXpert - J.W. Freund Farms, Inc.*")
        assert main_screen.exists(), "Login failed or main screen did not appear"
    else:
        pytest.fail("Login fixture returned None, login process likely failed.")

# def test_navigate_to_file(navigate_file):
#     # You can perform additional actions or assertions here
#     assert navigate_file, "Failed to navigate to File menu"

# def test_navigate_to_procurement(navigate_procurement):
#     # You can perform additional actions or assertions here
#     assert navigate_procurement, "Failed to navigate to Procurement menu"

# def test_navigate_to_commodity(navigate_commodity):
#     # You can perform additional actions or assertions here
#     assert navigate_commodity, "Failed to navigate to Commidity menu"

# def test_navigate_to_processing(navigate_processing):
#     # You can perform additional actions or assertions here
#     assert navigate_processing, "Failed to navigate to Processing menu"

# def test_navigate_to_ration(navigate_ration):
#     # You can perform additional actions or assertions here
#     assert navigate_ration, "Failed to navigate to Processing menu"

# def test_navigate_to_health(navigate_health):
#     # You can perform additional actions or assertions here
#     assert navigate_health, "Failed to navigate to Processing menu"

# def test_navigate_to_invoice(navigate_invoice):
#     # You can perform additional actions or assertions here
#     assert navigate_invoice, "Failed to navigate to Processing menu"

# def test_navigate_to_sales(navigate_sales):
#     # You can perform additional actions or assertions here
#     assert navigate_sales, "Failed to navigate to Processing menu"

# def test_navigate_to_risk_analysis(navigate_risk_analysis):
#     # You can perform additional actions or assertions here
#     assert navigate_risk_analysis, "Failed to navigate to Processing menu"

# def test_navigate_to_daily_jobs(navigate_daily_jobs):
#     # You can perform additional actions or assertions here
#     assert navigate_daily_jobs, "Failed to navigate to Processing menu"

# def test_navigate_to_view(navigate_view):
#     # You can perform additional actions or assertions here
#     assert navigate_view, "Failed to navigate to Processing menu"

# def test_navigate_to_window(navigate_window):
#     # You can perform additional actions or assertions here
#     assert navigate_window, "Failed to navigate to Processing menu"

# def test_navigate_to_help(navigate_help):
#     # You can perform additional actions or assertions here
#     assert navigate_help, "Failed to navigate to Processing menu"

# def test_navigate_to_reports(navigate_reports):
#     # You can perform additional actions or assertions here
#     assert navigate_reports, "Failed to navigate to Processing menu"

# def test_navigate_to_maintenance(navigate_maintenance):
#     # You can perform additional actions or assertions here
#     assert navigate_maintenance, "Failed to navigate to Processing menu"

# def test_exit_application(exit_application):
#     # This will run the exit application fixture
#     pass

if __name__ == "__main__":
    pytest.main(["-v", __file__])


# def test_contract_operations(navigate_to_contract):
#     contract_page = ContractPage(navigate_to_contract)
#     contract_value = contract_page.select_contract()
#     print("Selected Contract Value:", contract_value)

#     # Simulate entering the contract number in another field
#     contract_page.enter_contract_number(contract_value)


# def test_pen_consumption_graph(navigate_to_pen_consumption_graph):
#     ration_page = RationPage(navigate_to_pen_consumption_graph)
#     ration_page.pen_consumption_graph()

# def test_feed_status(navigate_to_feed_status):
#     ration_page = RationPage(navigate_to_feed_status)
#     ration_page.feed_status()

