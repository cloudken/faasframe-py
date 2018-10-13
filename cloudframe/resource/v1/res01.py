
from six.moves import http_client
from cloudframe.common import job
import logging
import time

LOG = logging.getLogger(__name__)


def post(tenant, req):
    ack = {'status': 'OK'}
    job.rpc_cast(_create_server, server=req)
    return http_client.OK, ack


def put(tenant, res_id, req):
    ack = {'status': 'OK'}
    return http_client.OK, ack


def get(tenant, res_id=None):
    ack = {'status': 'OK'}
    return http_client.OK, ack


def delete(tenant, res_id):
    ack = {'status': 'OK'}
    return http_client.OK, ack


def _create_server(server):
    time.sleep(5)
    LOG.debug('create server success!')
    return
