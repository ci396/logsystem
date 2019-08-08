from django.test import TestCase
from .models import Register

class Registertest(TestCase):
    def setUp(self):
        Register.objects.create(username = 'toms', first_name = 'Tom', middle_name = 'M.', last_name = 'Smith',
                               occupation = 'Student', phone_number = '9018970908', password = 't1',
                               mail_address = '47 W 13th St,New York', email = 'info@singularitysystem.com')

    def test_event_models(self):
        result = Register.objects.get(username = "toms")
        self.assertEqual(result.occupation, "Student")
        self.assertEqual(result.phone_number, '9018970908')
