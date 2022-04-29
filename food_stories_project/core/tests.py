from django.test import TestCase
from core.models import Contact


class TestContactModel(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'full_name': 'Resul Qenberov',
            'email': 'resul@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'Sayt islemir!!!',
        }
        cls.contact = Contact.objects.create(**cls.data1)

    def test_created_data(self):
        contact = Contact.objects.first()
        self.assertEqual(contact.full_name, self.data1['full_name'])
    
    def test_str_method(self):
        self.assertEqual(str(self.contact), self.data1['full_name'])
    
    @classmethod
    def tearDownClass(cls):
        Contact.objects.first().delete()
        del cls.contact
        del cls.data1