import unittest

from model.minified_user import MinifiedUser


class MinifiedUserTest(unittest.TestCase):
    def test_update_name(self):
        mini_user = MinifiedUser(name='Miniuser',
                                 mail='miniuser@example.com',
                                 phonenumber='0123456789',
                                 uid='asdf1234')

        self.assertEqual(mini_user.name, 'Miniuser')
        mini_user.update(name='new name')
        self.assertEqual(mini_user.name, 'new name')

    def test_update_mail(self):
        mini_user = MinifiedUser(name='Miniuser',
                                 mail='miniuser@example.com',
                                 phonenumber='0123456789',
                                 uid='asdf1234')

        self.assertEqual(mini_user.mail, 'miniuser@example.com')
        mini_user.update(mail='newmail@example.com')
        self.assertEqual(mini_user.mail, 'newmail@example.com')

    def test_update_phonenumber(self):
        mini_user = MinifiedUser(name='Miniuser',
                                 mail='miniuser@example.com',
                                 phonenumber='0123456789',
                                 uid='asdf1234')

        self.assertEqual(mini_user.phonenumber, '0123456789')
        mini_user.update(phonenumber='0102030405')
        self.assertEqual(mini_user.phonenumber, '0102030405')

    def test_update_uid(self):
        mini_user = MinifiedUser(name='Miniuser',
                                 mail='miniuser@example.com',
                                 phonenumber='0123456789',
                                 uid='asdf1234')

        self.assertEqual(mini_user.uid, 'asdf1234')
        mini_user.update(uid='qwer5678')
        self.assertEqual(mini_user.uid, 'qwer5678')

    def test_equal(self):
        mini_user = MinifiedUser(name='Miniuser',
                                 mail='miniuser@example.com',
                                 phonenumber='0123456789',
                                 uid='asdf1234')

        mini_user2 = MinifiedUser(name='Miniuser',
                                  mail='miniuser@example.com',
                                  phonenumber='0123456789',
                                  uid='asdf1234')

        self.assertEqual(mini_user, mini_user2)

    def test_not_equal(self):
        mini_user = MinifiedUser(name='Miniuser',
                                 mail='miniuser@example.com',
                                 phonenumber='0123456789',
                                 uid='asdf1234')

        mini_user2 = MinifiedUser(name='Miniuser2',
                                  mail='miniuser2@example.com',
                                  phonenumber='9876543210',
                                  uid='4321asdf')

        self.assertNotEqual(mini_user, mini_user2)

    def test_string(self):
        mini_user = MinifiedUser(name='Miniuser',
                                 mail='miniuser@example.com',
                                 phonenumber='0123456789',
                                 uid='asdf1234')

        expected = 'User: Miniuser, miniuser@example.com, 0123456789'

        self.assertEqual(str(mini_user), expected)

    def test_to_dict(self):
        mini_user = MinifiedUser(name='Miniuser',
                                 mail='miniuser@example.com',
                                 phonenumber='0123456789',
                                 uid='asdf1234')

        expected = {
            'name': 'Miniuser',
            'mail': 'miniuser@example.com',
            'phonenumber': '0123456789',
            'uid': 'asdf1234'
        }

        self.assertDictEqual(mini_user.to_dict(), expected)
