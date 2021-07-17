import os
from datetime import datetime

import allure
import pytest


@pytest.mark.usefixtures("driver_get", "test_data")
class BaseTest:
    def getData(self, name):
        valid_data = self.data[name]
        return valid_data

    def take_screenshot(self, exception):
        today = datetime.today()
        date = today.strftime("%d_%m_%Y")
        timestamp = today.strftime("%d_%m_%Y_%H_%M_%S")
        file_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(file_directory) + "/testresults/" + date + "/Screenshots/"