
from six.moves import http_client

from cloudframe.resource.v1 import res01
from cloudframe.tests.base import FaasTestCase


class TestRes01Servers(FaasTestCase):

    def setUp(self):
        super(TestRes01Servers, self).setUp()

    def test_post(self):
        req = {
            'name': 'abc'
        }
        tenant = 'user'
        ack = {'status': 'OK'}
        rv = res01.post(tenant, req)
        self.assertEqual(http_client.OK, rv[0])
        self.assertEqual(ack, rv[1])

    def test_get(self):
        tenant = 'user'
        ack = {'status': 'OK'}
        rv = res01.get(tenant)
        self.assertEqual(http_client.OK, rv[0])
        self.assertEqual(ack, rv[1])

    def test_put(self):
        req = {
            'name': 'abc'
        }
        res_id = '1234'
        tenant = 'user'
        ack = {'status': 'OK'}
        rv = res01.put(tenant, res_id, req)
        self.assertEqual(http_client.OK, rv[0])
        self.assertEqual(ack, rv[1])

    def test_delete(self):
        res_id = '1234'
        tenant = 'user'
        ack = {'status': 'OK'}
        rv = res01.delete(tenant, res_id)
        self.assertEqual(http_client.OK, rv[0])
        self.assertEqual(ack, rv[1])
