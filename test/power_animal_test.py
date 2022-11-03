import unittest
import requests
from unittest import TestCase
import animal_api
from pprint import pprint


class TestAnimal(TestCase):
    def test_get_time(self):
        example_animal_response = {
            'date': '2022-11-01', 
            }
        time = animal_api.get_time_of_animal(example_animal_response)
        self.assertEqual(time, '2022-02-02')


if __name__ == '__main__':
    unittest.main()

