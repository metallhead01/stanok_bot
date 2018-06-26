import unittest
import bot


class TestOpenToken(unittest.TestCase):
    def test_token_open_file(self):
        self.assertRaises(FileNotFoundError, bot.get_token, 'bot.token')

    def test_token_empty(self):
        self.assertIsNotNone(bot.get_token)


class UpdateStateFunc(unittest.TestCase):
    def test_check_len_list(self):
        pass

if __name__ == "__main__":
    unittest.main()
