import unittest

import cps5790

class Test(unittest.TestCase):
        def test(self):
                self.assertEqual(cps5790(7), 42)


if __name__ == '__main__':
    unittest.main()
