from unittest import TestCase
from unittest.mock import patch
import io


def check_same():
    enter = str(input())
    out = []
    for i in enter:
        if enter.count(i) > 1 and i not in out:
            out.append(i)
    print(out)


class TestCheckSame(TestCase):
    @patch('builtins.input', lambda *args: '11112222')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_numbers(self, mock_stdout):
        check_same()
        self.assertEqual(mock_stdout.getvalue()[:-1], "['1', '2']")

    @patch('builtins.input', lambda *args: 'aaaddfgh')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_letters(self, mock_stdout):
        check_same()
        self.assertEqual(mock_stdout.getvalue()[:-1], "['a', 'd']")

    @patch('builtins.input', lambda *args: '11112aaaab')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_numbers_and_letters(self, mock_stdout):
        check_same()
        self.assertEqual(mock_stdout.getvalue()[:-1], "['1', 'a']")

    @patch('builtins.input', lambda *args: 'AaBBcc')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_up_and_low_letters(self, mock_stdout):
        check_same()
        self.assertEqual(mock_stdout.getvalue()[:-1], "['B', 'c']")

    @patch('builtins.input', lambda *args: '')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty(self, mock_stdout):
        check_same()
        self.assertEqual(mock_stdout.getvalue()[:-1], "[]")