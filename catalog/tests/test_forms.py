from django.test import TestCase

class MyTestCase(TestCase):
    def test_equal(self):
        print("^^^^****************************^^^^")
        self.assertEqual(1+3, 4)

    def test_assertTrue(self):
        print("Asertion is true")
        self.assertFalse(False)