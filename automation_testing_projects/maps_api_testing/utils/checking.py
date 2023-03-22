"""Testing requests responses"""
import json

from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        """Method for checking status code"""
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Success! Status code is: {response.status_code}")
        else:
            print(f"FAIL! Status code is: {response.status_code}")

    @staticmethod
    def check_json_response(response: Response, expected_value):
        """method for checking keys"""
        token = json.loads(response.text)
        # print(token)
        # print(list(token))
        assert list(token) == expected_value
        print("All fields are present")

    @staticmethod
    def check_json_values(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"The value of the field name <{field_name}> is correct")

