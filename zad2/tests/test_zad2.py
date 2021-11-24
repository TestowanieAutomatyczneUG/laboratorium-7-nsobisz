
from main import Password

import unittest


class PasswordTest(unittest.TestCase):

    def setUp(self):
        self.temp = Password()

    def test_correct_password(self):
        self.assertEqual(True, self.temp.validPassword("zaq1@WSX"))

    def test_correct_password_2(self):
        self.assertEqual(True, self.temp.validPassword("AWAWwe#@se123"))


    def test_wrong_password_one_letter(self):
        self.assertEqual(False,  self.temp.validPassword("w"))

    def test_wrong_password_one_number_str(self):
        self.assertEqual(False,  self.temp.validPassword("7"))

    def test_wrong_password_one_special_ch(self):
        self.assertEqual(False,  self.temp.validPassword("%"))
    def test_wrong_password_more_special_ch(self):
        self.assertEqual(False,  self.temp.validPassword("%#$#%#$%#"))
    def test_wrong_password_more_special_ch_numbers(self):
        self.assertEqual(False,  self.temp.validPassword("%#$#123%#$%#"))
    def test_wrong_password_more_number_str(self):
        self.assertEqual(False,  self.temp.validPassword("123123123123"))
    def test_wrong_password_more_small_letters(self):
        self.assertEqual(False, self.temp.validPassword("adadwdadwdawd"))
    def test_wrong_password_more_big_letters(self):
        self.assertEqual(False,  self.temp.validPassword("AFWAFWFAW"))
    def test_wrong_password_more_big_letters_numbers(self):
        self.assertEqual(False,  self.temp.validPassword("AFWA23232FWFAW"))
    def test_wrong_password_more_big_letters_spe_ch(self):
        self.assertEqual(False,  self.temp.validPassword("AFWAF#$%#%WFAW"))
    def test_wrong_password_more_small_letters_numbers(self):
        self.assertEqual(False, self.temp.validPassword("adadwda12313dwdawd"))
    def test_wrong_password_more_small_letters_big(self):
        self.assertEqual(False,  self.temp.validPassword("adadwdDHTDTwdawd"))
    def test_wrong_password_more_small_letters_spe_ch(self):
        self.assertEqual(False,  self.temp.validPassword("ada#$%#%awd"))

    def test_exception_number(self):
        self.assertRaises(TypeError, self.temp.validPassword, 7)
    def test_exception_float(self):
        self.assertRaises(TypeError, self.temp.validPassword, 7.3)
    def test_exception_list(self):
        self.assertRaises(TypeError, self.temp.validPassword, [7])
    def test_exception_dict(self):
        self.assertRaises(TypeError, self.temp.validPassword, {"a":7})

    def tearDown(self):
        self.temp = None