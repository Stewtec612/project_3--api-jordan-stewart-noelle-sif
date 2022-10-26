# this will be in a different place in your project 

import unittest
from unittest import TestCase
import horoscope_api  # modify according to your project structure 

class TestHoroscope(TestCase):

    def test_get_time(self):
        example_horoscope_response = {
            'date': '2022-02-02', 
            'horoscope': 'whatever'
            }
        time = horoscope_api.get_time_of_horoscope(example_horoscope_response)
        self.assertEqual(time, '2022-02-02')
        

if __name__ == '__main__':
    unittest.main()

