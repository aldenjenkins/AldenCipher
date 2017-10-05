import unittest
from AldenCipher import AldensEncryptions

class TestCeasarCipher(unittest.TestCase):

    """
    ENCRYPTION
    """
    def test_rotation(self):
        test_encryption_object = AldensEncryptions("abcf","a")
        test_encryption_object.encrypt_caesar()
        self.assertEqual(test_encryption_object.get_message(),"bcdg")

    def test_modulus(self):
        test_encryption_object = AldensEncryptions("xyz", "a")
        test_encryption_object.encrypt_caesar()
        self.assertEqual(test_encryption_object.get_message(), "yza")

    def test_uppercase(self):
        test_encryption_object = AldensEncryptions("XYZ", "a")
        test_encryption_object.encrypt_caesar()
        self.assertEqual(test_encryption_object.get_message(), "YZA")

    """
    DECRYPTION
    """

    def test_decryption(self):
        test_plain_text = "XYZ"
        test_decryption_object = AldensEncryptions(test_plain_text, "a")
        test_decryption_object.encrypt_caesar()
        test_decryption_object.decrypt_caesar()
        self.assertEqual(test_decryption_object.get_message(),test_plain_text)

if __name__ == "__main__":
    unittest.main()