import unittest

from rtpplayapi import RTPPlayAPI


class TestApi(unittest.TestCase):

    def test_auth(self):
        rtpp = RTPPlayAPI()
        self.assertEqual(rtpp.AUTH_TOKEN, "")
        self.assertEqual(rtpp.AUTH_TOKEN_LIFETIME, 0)
        # dummy request
        req = rtpp.get_live_tv_channels()
        self.assertNotEqual(rtpp.AUTH_TOKEN, "")
        self.assertGreater(rtpp.AUTH_TOKEN_LIFETIME, 0)
        self.assertNotIn("error", req)

    def test_get_collection(self):
        rtpp = RTPPlayAPI()
        req = rtpp.get_collection(178)
        self.assertEqual(req["name"], "64 Anos de RTP")
        self.assertEqual(req["collection_id"], "178")


if __name__ == '__main__':
    unittest.main()
