import configuration
import requests

def post_create_order(body, headers):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=headers)


def get_order_by_track_number(track_number):
    print(track_number)
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_NUMBER + track_number)