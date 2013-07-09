import unittest

from circus.discovery import AutoDiscovery

from zmq.eventloop import ioloop


class TestDiscover(unittest.TestCase):

    def test_discovery_callback(self):
        payload = "Beer. Now there's a temporary solution."
        loop = ioloop.IOLoop.instance()

        self.received_data = None

        def cb(data, emitter_addr, send_message):
            self.received_data = data
            loop.stop()

        AutoDiscovery('udp://237.219.251.97:12027', loop, payload, cb)
        loop.add_timeout(loop.time() + 1, loop.stop)

        loop.start()
        self.assertEquals(self.received_data['nodes'], payload)
