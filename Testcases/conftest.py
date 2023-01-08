from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.service import Service

import pytest

@pytest.fixture()
def setup():

    driver = webdriver.Chrome("D:\python projects\driver\chromedriver.exe")

    return driver

# from py.xml import html
#
#
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.p("this is report")])
#     postfix.extend([html.p("this is result")])
#
#
# import pytest
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("http://www.example.com/"))
#         extra.append(pytest_html.extras.text('Add some simple Text'))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
#         report.extra = extra