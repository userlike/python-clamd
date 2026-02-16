import clamd
from io import BytesIO

import pytest


class TestNetworkSocket(object):
    """
    Test suite expects ClamAV running at default host and port (localhost, 3310)
    """
    kwargs = {}

    @pytest.fixture(autouse=True)
    def setup(self):
        self.cd = clamd.ClamdNetworkSocket(**self.kwargs)

    def test_ping(self):
        result = self.cd.ping()
        assert result == "PONG"

    def test_version(self):
        version = self.cd.version()
        assert "ClamAV 1.5.1" in version

    def test_reload(self):
        assert self.cd.reload() == 'RELOADING'


    def test_instream_found(self):
        # Case: True positive
        expected = {'stream': ('FOUND', 'Eicar-Test-Signature')}
        assert self.cd.instream(BytesIO(clamd.EICAR)) == expected


    def test_instream_ok(self):
        # Case True negative
        assert self.cd.instream(BytesIO(b"foo")) == {'stream': ('OK', None)}


class TestUnixSocketTimeout(TestNetworkSocket):
    kwargs = {"timeout": 20}


def test_cannot_connect():
    with pytest.raises(clamd.ConnectionError):
        clamd.ClamdNetworkSocket(host="another_host").ping()
