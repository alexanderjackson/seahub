from django.test import override_settings

from seahub.invitations.utils import validate_accepter
from seahub.test_utils import BaseTestCase


class ValidateAccepterTest(BaseTestCase):
    def test_valid_email(self):
        assert validate_accepter('a@a-a-a.com') is True

    def test_invalid_email(self):
        assert validate_accepter('ffff') is False

    @override_settings(INVITATION_ACCEPTER_BLACKLIST=["a@a.com", "*@a-a-a.com", r".*@(foo|bar).com"])
    def test_email_in_blacklist(self):
        assert validate_accepter('a@a.com') is False
        assert validate_accepter('a@a-a-a.com') is False
        assert validate_accepter('a@foo.com') is False
        assert validate_accepter('a@bar.com') is False
        assert validate_accepter('a@foobar.com') is True
