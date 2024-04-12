import pytest
from datetime import datetime

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    timestamp = datetime.now().strftime('%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser')
        screenshot_file = f'D:/report/scr{timestamp}.png'
        driver.save_screenshot(screenshot_file)
        extra.append(pytest_html.extras.image(screenshot_file))
        report.extra = extra
