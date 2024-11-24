import unittest
from fireDrill import phonebook


class TestPhonebook(unittest.TestCase):

    def test_that_add_contacts_function_exist(self):
        phonebook.add_contacts("name", "email", "phone")

    def test_that_add_contacts_function_returns_expected_results(self):
        contacts = []
        contact = ["chigbo", "chigbo@gmail.com", "08165498422"]
        contacts.append(contact)
        self.assertEqual(len(contacts), 1)
        second_contact = ["Daniel", "daniel@gmail.com", "08165498456"]
        contacts.append(second_contact)
        self.assertEqual(len(contacts), 2)

    def test_that_remove_contact_function_exists(self):
        phonebook.remove_contact("name")

    def test_that_remove_contact_function_returns_expected_result(self):
        contacts = [{"name": "chigbo", "email": "chigbo@gmail.com", "phone": "08165498422"},
                    {"name": "daniel", "email": "daniel@gmail", "phone": "08165498456"}
                    ]
        expected_result = [{"name": "chigbo", "email": "chigbo@gmail.com", "phone": "08165498422"}]
        result = phonebook.remove_contact("name")
        self.assertEqual(result, expected_result)
