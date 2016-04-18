import sys

from nose.tools import *

if sys.version_info[0] == 3:
    from unittest.mock import Mock
else:
    from mock import Mock

from odin.adapters.dummy import DummyAdapter

class TestDummyAdapter():

    @classmethod
    def setup_class(cls):

        cls.adapter = DummyAdapter()
        cls.path = '/dummy/path'
        cls.request = Mock()
        cls.request.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def test_adapter_get(self):
        response = self.adapter.get(self.path, self.request)
        assert_equal(response.data, 'DummyAdapter: GET on path {}'.format(self.path))
        assert_equal(response.status_code, 200)

    def test_adapter_put(self):
        response = self.adapter.put(self.path, self.request)
        assert_equal(response.data, 'DummyAdapter: PUT on path {}'.format(self.path))
        assert_equal(response.status_code, 200)

    def test_adapter_delete(self):
        response = self.adapter.delete(self.path, self.request)
        assert_equal(response.data, 'DummyAdapter: DELETE on path {}'.format(self.path))
        assert_equal(response.status_code, 200)

    def test_adapter_put_bad_content_type(self):
        bad_request = Mock()
        bad_request.headers = {'Content-Type': 'text/plain'}
        response = self.adapter.put(self.path, bad_request)
        assert_equal(response.data, 'Request content type (text/plain) not supported')
        assert_equal(response.status_code, 415)

    def test_adapter_put_bad_accept_type(self):
        bad_request = Mock()
        bad_request.headers = {'Accept': 'text/plain'}
        response = self.adapter.put(self.path, bad_request)
        assert_equal(response.data, 'Requested content types not supported')
        assert_equal(response.status_code, 406)

