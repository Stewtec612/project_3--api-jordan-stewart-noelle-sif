import unittest
import requests
from unittest import TestCase
import horoscope_api
from pprint import pprint


class TestHoroscope(TestCase):
    def test_get_time(self):
        example_horoscope_response = {
            'date': '2022-11-01', 
            'horoscope': 'whatever'
            }
        time = horoscope_api.get_time_of_horoscope(example_horoscope_response)
        self.assertEqual(time, '2022-02-02')


if __name__ == '__main__':
    unittest.main()

