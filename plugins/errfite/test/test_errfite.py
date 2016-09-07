import os
import logging
from errbot.backends.test import testbot

logging.disable(logging.CRITICAL)

class TestErrFite(object):
    extra_plugin_dir = '.'

    def test_ping(self, testbot):
        testbot.push_message('!ping')
        assert 'ping' in testbot.pop_message()

    def test_pong(self, testbot):
        testbot.push_message('!ping')
        assert 'ping' in testbot.pop_message()

    def test_get_pending_lists(self, testbot):
        testbot.push_message('!get_pending_lists')
        lists = testbot.pop_message()
        assert not lists
        assert lists == []
