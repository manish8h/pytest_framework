import pytest
firefox_driver_path = "drivers/geckodriver"


# class TestSignup(BaseTest):
@pytest.mark.usefixtures('class_fixture')
@pytest.mark.usefixtures('test_data')

class TestFix():

    def test_signup_one(self):
        print("I am in valid data sign -  1")
        print("pytest -vs test_fix.py to print text")
        print("pytest --collect-only")
        print("pytest -vs test_fix.py::TestSignup::test_to_skip")
        #with specific name in test_mtd
        print("pytest -vs -k test_to_skip")
        print("pytest -vs test_fix.py -k test_to_skip")
        #with specific marker name
        print("pytest -vs -m regression")
        assert True


    @pytest.mark.skip
    def test_sigup_with_valid_data(self):
        print("I am in valid data sign -  1")
        assert True

    @pytest.mark.skip
    def test_sigup_with_invalid_data(self):
        print("I am in invalid data sign -  2")
        # print(self.driver)
        assert True

    @pytest.mark.xfail
    def test_sigup_with_invalid_data(self):
        print("this is xfail")
        print("it will run but not show if is pass or pass")
        # print(self.driver)
        assert True

    # @pytest.mark.skip
    def test_to_skip(self):
        print("this will skip...........")
        assert True
        # assert False

    @pytest.mark.regression
    def test_to_regression(self):
        print("this regression Tcs...........")
        assert True
        # assert False

    def test_to_Tcs(self):
        print("this Tcs...........")
        assert True
        # assert False


    def test_use_test_data(self, test_data):
        print(test_data[0])
        print(test_data)

    @pytest.mark.usefixtures('data_provider')
    def test_use_data_provider(self, data_provider):
        print(data_provider['user'])
        print(data_provider['pwd'])

