import configuration
import requests


def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


def get_order_by_track_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_NUMBER + str(track))
