"""Tests for Requestor functions and classes from erpsc.core."""

import time

from erpsc.core.requester import Requester

##################################################################################
##################################################################################
##################################################################################

def test_requester():
    """   """

    assert Requester()

def test_throttle():
    """   """

    req = Requester()
    req.time_last_req = time.time()

    req.throttle()

    assert True

def test_wait():
    """   """

    req = Requester()

    req.wait(0.01)

    assert True

def test_get_url():
    """   """

    req = Requester()

    web_page = req.get_url('http://www.google.com')

    assert web_page

def test_open():
    """   """

    req = Requester()

    req.open()

    assert req.is_active

def test_close():
    """   """

    req = Requester()

    req.open()
    req.close()

    assert not req.is_active