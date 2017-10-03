import logging
from django.contrib.auth.models import User
from django.test import TestCase


class Test(TestCase):

    assert_http_status = [
    ]

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.user = User.objects.create_superuser('testrunner', 'test@test.com', 'testrunner')
        self.client.login(username='testrunner', password='testrunner')

    def tearDown(self):
        self.client.logout()
        self.user.delete()

    def test_url(self):
        for row in self.assert_http_status:
            url = row['url']
            status = row['status']
            response = self.client.get(url)

            if response.status_code == status:
                self.logger.info(f'{status} {url}')
            else:
                self.logger.error(f'{response.status_code} {url}')
                raise AssertionError(f'HTTP {response.status_code} for "{url}"')
