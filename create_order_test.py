import sender_stand_request #импортировала файл с функциями которые выполняют запросы
import data #импортировала файл с данными для запросов


def positive_assert(): #объявила функцию без параметра положительных проверок
    response = sender_stand_request.post_create_order(data.order_body) #записала в переменную response результат вызвала функцию post_create_order из файла sender_stand_request, чтобы создать заказ, с параметром data.order_bod
    track_number = response.json()["track"] #записала в переменную track_number значение из поля ответа c ключем track
    order_response = sender_stand_request.get_order_by_track_number(track_number) #записала в переменную order_response результат вызвала функцию get_order_by_track_number из файла sender_stand_request, чтобы получить заказ по номеру track_number
    assert order_response.status_code == 200 #проверка что статус код в ответе соответсвтует ожидаемому коду-200


# Тест 1. Успешное создание заказа
def test_id_1_create_order_success_response(): #объявила функцию без параметра которая является тестом
    positive_assert() #вызвала внутри теста проверки, которые написаны выше
