
from gevent import monkey
import testtools

from cloudframe.common import job


class FaasTestCase(testtools.TestCase):
    monkey.patch_all()
    job.start_worker(10)

    def setUp(self):
        super(FaasTestCase, self).setUp()
