from django.test import TestCase
from .models import Invitation

from django.contrib.auth.models import User


class InvitationTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        from_user = User.objects.create(username='jimmy')
        to_user = User.objects.create(username='joe')
        Invitation.objects.create(from_user=from_user,
                                  to_user=to_user,
                                  message='I will crush you!'
                                  )

    def test_to_user(self):
        invitation = Invitation.objects.get(id=1)
        expected_user = f'{invitation.from_user}'
        self.assertEquals(expected_user, 'jimmy')

    def test_from_user(self):
        invitation =Invitation.objects.get(id=1)
        expected_user = f'{invitation.to_user}'
        self.assertEquals(expected_user, 'joe')

    def test_message(self):
        invitation = Invitation.objects.get(id=1)
        expected_message = f'{invitation.message}'
        self.assertEquals(expected_message, 'I will crush you!')



