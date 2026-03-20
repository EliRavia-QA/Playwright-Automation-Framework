import pytest
import allure
import os
from playwright.sync_api import Page, APIRequestContext, Playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage



class App:
    def __init__(self, page: Page, api_request: APIRequestContext):
        self.page = page
        self.api_request = api_request
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.console_logs = []



@pytest.fixture(scope="function")
def app(page: Page, playwright: Playwright):
    api_context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    app_instance = App(page, api_context)

    page.on("console", lambda msg: app_instance.console_logs.append(f"[{msg.type}] {msg.text}"))

    yield app_instance
    api_context.dispose()




@pytest.fixture
def setup_ui(app):

    with allure.step("ניווט לאתר SauceDemo"):
        app.page.goto("https://www.saucedemo.com/")
    return app


@pytest.fixture
def api_only(app):

    return app



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:

        app_instance = None
        for arg in item.funcargs.values():
            if isinstance(arg, App):
                app_instance = arg
                break

        if app_instance:
            page = app_instance.page
            allure.attach(
                page.screenshot(full_page=True),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            if app_instance.console_logs:
                logs_text = "\n".join(app_instance.console_logs)
                allure.attach(
                    logs_text,
                    name="browser_console_logs",
                    attachment_type=allure.attachment_type.TEXT
                )



def pytest_sessionfinish(session, exitstatus):
    results_dir = os.path.join(session.config.rootdir, 'tests', '=allure-results')
    if os.path.exists(results_dir):
        env_file = os.path.join(results_dir, 'environment.properties')
        with open(env_file, 'w') as f:
            f.write(f"Platform={os.name}\n")
            f.write(f"Project=SauceDemo_Automation\n")
            f.write(f"URL=https://www.saucedemo.com/\n")
            f.write(f"Tester=Eli_Ravia\n")
            f.write(f"Python_Version={os.sys.version.split()[0]}\n")
