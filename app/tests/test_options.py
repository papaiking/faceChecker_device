import unittest

from lib import Options


class TestCommandLineParameters(unittest.TestCase):

    def setUp(self):
        self.options = Options()

    def test_options_example_is_set(self):
        opts = self.options.parse(['-c', 'checking_interval'])
        self.assertEquals(opts.example, '2')


if __name__ == '__main__':
    unittest.main()
