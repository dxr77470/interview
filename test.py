import os
import unittest
import sys
from Q1 import read_text, sort_data, write_output


CURRENT_DIR = os.path.dirname(__file__)


class TestReadText(unittest.TestCase):
   
    def setUp(self):
        self.correct_result = {
            2: [(1, '1 Steak'), (1, '34 Burger'), (1, '56 chicken wings')],
            10: [(2, '2 Nuggets')],
            15: [(2, '5 pizza')],
            343: [(3, '90Turkey')],
            sys.maxsize: [(0, 'Pork'), (0, 'kebab'), (0, 'apple'), (0, 'mySideWalk'), (0, 'Happyhours')]
        }

        # files
        self.sample_input = os.path.join(CURRENT_DIR, 'sample_input.txt')
        self.sample_bad_input = os.path.join(CURRENT_DIR, 'sample_bad_input.txt')

    def test_non_existing_file(self):
        self.assertIsNone(read_text('non_existing_file'))

    def test_correct_result(self):
        self.assertEqual(read_text(self.sample_input), self.correct_result)

    def test_bad_input_tolerance(self):
        self.assertEqual(read_text(self.sample_bad_input), self.correct_result)


class TestSortData(unittest.TestCase):
   

    def setUp(self):
        self.input = {
            2: [(1, '1 Steak'), (1, '34 Burger'), (1, '56 chicken wings')],
            10: [(2, '2 Nuggets')],
            15: [(2, '5 pizza')],
            343: [(3, '90Turkey')],
            sys.maxsize: [(0, 'Pork'), (0, 'kebab'), (0, 'apple'), (0, 'mySideWalk'), (0, 'Happyhours')]
        }

        self.correct_result = [
            '1Steak',
            '2 Nuggets',
            '5 pizza'
            '34 Burger',
            '56 Chicken Wings',
            '90Turkey',
            'Apple',
            'happyhours',
            'kebab',
            'mysidewalk',
            'pork',
        ]
    def test_wrong_input(self):
        self.assertIsNone(sort_data('wrong'))

    def test_empty_input(self):
        self.assertEqual(sort_data({}), [])

    def test_process_data(self):
        self.assertEqual(sort_data(self.input), self.correct_result)


class TestWriteValues(unittest.TestCase):
   
    def setUp(self):
        self.input = [
            '1Steak',
            '2 Nuggets',
            '5 pizza'
            '34 Burger',
            '56 Chicken Wings',
            '90Turkey',
            'Apple',
            'happyhours',
            'kebab',
            'mysidewalk',
            'pork',
        ]

        
        self.test_output = os.path.join(CURRENT_DIR, 'test_output.txt')
        self.sample_output = os.path.join(CURRENT_DIR, 'sample_output.txt')

    def test_no_data(self):
        self.assertFalse(write_output(None))

    def test_bad_values(self):
        self.assertFalse(write_output([{}, None, 123, '']))

    def test_correct_file_output(self):
     
        write_output(self.input, filename=self.test_output)

        
        saved_file_list = []
        with open(self.test_output, 'r') as saved_file:
            for line in saved_file:
                saved_file_list.append(line.rstrip())

       
        os.remove(self.test_output)

        correct_file_list = []
        with open(self.sample_output, 'r') as comp_file:
            for line in comp_file:
                correct_file_list.append(line.rstrip())

        self.assertEqual(saved_file_list, correct_file_list)


if __name__ == '__main__':
    unittest.main()