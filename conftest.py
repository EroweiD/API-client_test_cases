import json
import os

import pytest
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"




@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSetting up resources...")
    yield
    print("\nTearing down resources...")

@pytest.fixture()
def user_create_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"json data", "users_data.json")
    with open(json_file_path) as json_file: # if you open file with with option it will close after using the file
        data = json.load(json_file)
    return data
