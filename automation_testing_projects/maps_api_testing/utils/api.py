from utils.http_methods import HttpMethods

"""Google Maps TESTING methods"""

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class GoogleMapsApi:

    @staticmethod
    def create_new_place():
        """method for creating a new location"""
        json_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": ["shoe park", "shop"],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"
        post_url = f"{base_url}{post_resource}{key}"
        print(post_url)
        result_post = HttpMethods.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_place(place_id):
        """method for getting new location"""
        get_resource = "/maps/api/place/get/json"
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_new_place(place_id):
        """method for changing new location"""
        put_resource = "/maps/api/place/update/json"
        put_url = f"{base_url}{put_resource}{key}"
        print(put_url)
        json_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        print(f"place id that is passed to the PUT: {place_id}")
        result_put = HttpMethods.put(url=put_url, body=json_update_new_location)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """method for deleting new location"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = f"{base_url}{delete_resource}{key}"
        print(delete_url)
        json_delete_new_location = {
            "place_id": place_id
        }
        result_delete = HttpMethods.put(delete_url, json_delete_new_location)
        print(result_delete.text)
        return result_delete
