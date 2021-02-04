""" V1.0--cleaning coding"""
import sys
import os
sys.path.append(f"{os.getcwd()}/flask_app/")
from grandpy import req_grandpy


def test_request_google(monkeypatch):
    os.environ["GOOGLE_KEY"] = "1"
    dico_grandpy_google = {
        "formatted_address": "Statue of Liberty National Monument, New York, NY 10004, USA",
        'latitude': '48.85837009999999',
        'longitude': '2.2944813',
    }

    class MockRequestsGet_Google:
        def __init__(self, url, params=None):
            self.status_code = 200
            self.dict_test = {}
            self.GOOGLE_KEY = '1'

        def json(self):
            self.dict_test = {
                'results': [
                    {
                        "formatted_address": "Statue of Liberty National Monument, New York, NY 10004, USA",
                        'geometry': {
                            'location': {
                                'lat': '48.85837009999999',
                                'lng': '2.2944813',
                            }
                        }
                    }
                ]
            }
            return self.dict_test

    monkeypatch.setattr('requests.get', MockRequestsGet_Google)

    object_from_import_class = req_grandpy()
    dict_google = object_from_import_class.search_by_google()
    assert dict_google == dico_grandpy_google


def test_request_wiki(monkeypatch):
    os.environ["GOOGLE_KEY"] = "1"
    dico_grandpy_wiki = {'pageid' : '1359783', 'title' : 'Tour Eiffel','latitude' : '48.8583','longitude' : '2.2944813'}

    class MockRequestsGet_Wiki:
        def __init__(self, url, params=None):
            self.status_code = 200
            self.dict_test_wiki = {}
        def json(self):
            self.dict_test_wiki = {
                'query' : {
                    'geosearch' : [{
                            'pageid' : '1359783',
                            'title' : 'Tour Eiffel',
                            'latitude' : '48.8583',
                            'longitude' : '2.2944813'

                    }]
                }
            }
            return self.dict_test_wiki
    monkeypatch.setattr('requests.get', MockRequestsGet_Wiki)


    object_from_import_class = req_grandpy()
    object_from_import_class.dict_return = {'latitude' : '48.8583','longitude' : '2.2944813','pageid' : '1359783','title' : 'Tour Eiffel',}
    object_from_import_class.geosearch = {}
    dict_wiki = object_from_import_class.search_by_wiki()
    assert dict_wiki == dico_grandpy_wiki


def test_request_openweathermap(monkeypatch):
    os.environ["OWM_KEY"] = "1"
    dico_grandpy_owm = {"temp": 280.85,
        "feels_like": 278.04,
        "temp_min": 280.15,
        "temp_max": 281.48,
        "pressure": 996,
        "humidity": 76,
        }

    class MockRequestsGet_OpenWeather:
        def __init__(self, url, params=None):
            self.status_code = 200
            self.dict_test_owm = {}

        def json(self):
            self.dict_test_owm = {
                "weather": [
                            {
                                "id": 804,
                                "main": "Clouds",
                                "description": "couvert",
                                "icon": "04d"
                            }
                ],
                "main": {
                    "temp": 280.85,
                    "feels_like": 278.04,
                    "temp_min": 280.15,
                    "temp_max": 281.48,
                    "pressure": 996,
                    "humidity": 76
                }
            }
            return self.dict_test_owm

    monkeypatch.setattr('requests.get', MockRequestsGet_OpenWeather)

    object_from_import_class = req_grandpy()
    object_from_import_class.dict_return = {'latitude' : '48.8583','longitude' : '2.2944813','pageid' : '1359783','title' : 'Tour Eiffel',}
    dict_owm = object_from_import_class.search_by_openweathermap()
    assert dict_owm == dico_grandpy_owm
    






