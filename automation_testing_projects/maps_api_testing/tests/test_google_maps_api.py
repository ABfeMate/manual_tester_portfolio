import json

from utils.api import GoogleMapsApi
from utils.checking import Checking


class TestCreatePlace:
    """Create, read, update and delete new location"""

    def test_create_new_place(self):
        print("\nMethod POST:\n")
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_json_response(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_status_code(result_post, 200)
        Checking.check_json_values(result_post, 'status', 'OK')

        print("\nMethod GET POST:\n")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        # token = json.loads(result_get.text)
        # print(list(token))
        Checking.check_json_response(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                                  'website', 'language'])
        Checking.check_json_values(result_get, 'address', '29, side layout, cohen 09')

        print("\nMethod PUT:\n")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_response(result_put, ['msg'])
        Checking.check_json_values(result_put, 'msg', 'Address successfully updated')

        print("\nMethod GET PUT:\n")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_values(result_get, 'address', '100 Lenina street, RU')

        print("\nMethod DELETE:\n")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_response(result_delete, ['status'])
        Checking.check_json_values(result_delete, 'status', 'OK')

        print("\nMethod GET DELETE:\n")
        result_get = GoogleMapsApi.get_new_place(place_id)  # should return error
        Checking.check_status_code(result_get, 404)
        Checking.check_json_response(result_get, ['msg'])
        Checking.check_json_values(result_get, 'msg', 'Get operation failed, looks like place_id  doesn\'t exists')

        print("\nTests of creation, reading, updating and deletion of new location PASSED.")
