import sender_stand_request
import data


def positive_assert():
    track_number = sender_stand_request.post_create_order(data.order_body, data.headers)
    order_response = sender_stand_request.get_order_by_track_number(track_number)
    assert order_response.status_code == 200


# Тест 1. Успешное создание заказа
def test_id_1_create_order_success_response():
    positive_assert()
