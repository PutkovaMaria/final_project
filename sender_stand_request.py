import configuration #импортировала конфигурационный файл с вынесеными ссылками
import requests #импортировала библиотеку реквест для тестирования api


def post_create_order(body): #объявила функцию с параметром
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body) #вызвала функцию post из библиотеки реквест с параметрами:
    #ссылка на ручку api (склееная из адреса сервера и адреса ручки)
    # и поданным парамеметом body в json. Результат выполнения: объект ответа от api


def get_order_by_track_number(track): #объявила функцию с параметром
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_NUMBER + str(track))
#вызвала функцию get из библиотеки реквест с параметрами:
# ссылка на ручку api (склееная из адреса сервера и адреса ручки) и поданным парамеметом body в json.
# Результат выполнения: объект ответа от api