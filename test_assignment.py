# test_assignment.py
from playwright.sync_api import sync_playwright
from pages.locators import AutomationAnywherePage

def test_automation_assignment():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        aa_logic = AutomationAnywherePage(page)

        # Credentials [cite: 27]
        MY_USER = "keerthi2454@gmail.com" #
        MY_PASS = "your-password"

        # --- USE CASE 1 & 2 ---
        aa_logic.login(MY_USER, MY_PASS)
        aa_logic.use_case_1_message_box("TaskBot_2026")
        aa_logic.use_case_2_form_upload("Form_2026", "dummy_document.pdf")

        # --- USE CASE 3: API Flow ---
        # Identify endpoints via browser Network tab [cite: 30]
        api_url = "https://community.cloud.automationanywhere.digital/v1/learning-instances"
        headers = {"Authorization": "Bearer YOUR_CAPTURED_TOKEN"}
        
        response = page.request.post(
            api_url,
            data={"name": "LearningInstance_01", "description": "API Test"},
            headers=headers
        )
        
        # API Assertions [cite: 30]
        assert response.status in [200, 201], f"Status failed: {response.status}"
        print(f"API Response Body: {response.json()}")

        browser.close()