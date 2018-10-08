import unittest
import suffixarrayA


class testImplementation(unittest.TestCase):

    def test_suffixArrray(self):

        string = "banana"
        got = suffixarrayA.suffixArray(string)
        self.assertEqual(got, [5, 3, 1, 0, 4, 2])

        string = "GATAGACA$"
        got = suffixarrayA.suffixArray(string)
        self.assertEqual(got, [8, 7, 5, 3, 1, 6, 4, 0, 2])


if __name__ == "__main__":
    unittest.main()
