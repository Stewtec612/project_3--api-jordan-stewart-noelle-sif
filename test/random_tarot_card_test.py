import unittest
import requests
from unittest import TestCase
import tarot_api
from pprint import pprint


class TestTarot(TestCase):
    def test_get_time(self):
        example_tarot_response = {
            'date': '2022-11-01', 
            }
        time = tarot_api.get_time_of_horoscope(example_tarot_response)
        self.assertEqual(time, '2022-02-02')


if __name__ == '__main__':
    unittest.main()

