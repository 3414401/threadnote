#!/usr/bin/env python3
"""
Unit test for updated ThreadNote Request Handler including PDF upload and infinite scroll feed.
"""

import io
import json
import unittest
from unittest.mock import MagicMock
from app import ThreadsCloneHandler

class MockServer:
    pass

class TestHandlerDirect(unittest.TestCase):
    def setUp(self):
        self.handler = ThreadsCloneHandler.__new__(ThreadsCloneHandler)
        self.handler.server = MockServer()
        self.handler.close_connection = False
        self.handler.request_version = "HTTP/1.1"
        self.handler._headers_buffer = []

    def test_get_feed_pagination(self):
        # Page 1
        self.handler.path = "/api/feed?page=1&limit=3&category=all"
        self.handler.wfile = io.BytesIO()
        self.handler.send_response = MagicMock()
        self.handler.send_header = MagicMock()
        self.handler.end_headers = MagicMock()

        self.handler.do_GET()

        resp_data = json.loads(self.handler.wfile.getvalue().decode("utf-8"))
        self.assertTrue(resp_data.get("has_more"))
        self.assertEqual(len(resp_data["threads"]), 3)

        # Page 2 (Infinite scroll generation)
        self.handler.path = "/api/feed?page=2&limit=3&category=all"
        self.handler.wfile = io.BytesIO()
        self.handler.do_GET()

        resp_page2 = json.loads(self.handler.wfile.getvalue().decode("utf-8"))
        self.assertEqual(len(resp_page2["threads"]), 3)
        self.assertEqual(resp_page2["page"], 2)

    def test_post_upload_simulation(self):
        payload = json.dumps({
            "filename": "test_curriculum.txt",
            "text": "1. 평면도형과 구성요소\n+ 핵심 각론 +\n(오) 예각이 하나만 있어도 예각삼각형이다 -> (지) 직각삼각형에도 예각이 있음.",
            "persona": "elementary_teacher"
        }).encode("utf-8")

        self.handler.path = "/api/upload"
        self.handler.headers = {"Content-Length": str(len(payload))}
        self.handler.rfile = io.BytesIO(payload)
        self.handler.wfile = io.BytesIO()
        self.handler.send_response = MagicMock()
        self.handler.send_header = MagicMock()
        self.handler.end_headers = MagicMock()

        self.handler.do_POST()

        resp_data = json.loads(self.handler.wfile.getvalue().decode("utf-8"))
        self.assertTrue(resp_data.get("success"))
        self.assertTrue(len(resp_data["new_threads"]) >= 1)
        self.assertIn("평면도형", resp_data["new_threads"][0]["source_insight"]["title"])

    def test_personas_api(self):
        self.handler.path = "/api/personas"
        self.handler.wfile = io.BytesIO()
        self.handler.send_response = MagicMock()
        self.handler.send_header = MagicMock()
        self.handler.end_headers = MagicMock()

        self.handler.do_GET()

        resp_data = json.loads(self.handler.wfile.getvalue().decode("utf-8"))
        self.assertEqual(len(resp_data), 16)
        self.assertIn("exam_evaluator", resp_data)
        self.assertIn("pe_sports_coach", resp_data)
        self.assertIn("art_music_maestro", resp_data)

    def test_end_headers_cache_control(self):
        handler = ThreadsCloneHandler.__new__(ThreadsCloneHandler)
        handler.request_version = "HTTP/1.1"
        handler._headers_buffer = []
        headers_sent = {}
        def mock_send_header(k, v):
            headers_sent[k] = v
        handler.send_header = mock_send_header
        handler.flush_headers = MagicMock()

        handler.end_headers()

        self.assertEqual(headers_sent.get("Cache-Control"), "no-cache, no-store, must-revalidate")
        self.assertEqual(headers_sent.get("Pragma"), "no-cache")
        self.assertEqual(headers_sent.get("Expires"), "0")


if __name__ == "__main__":
    unittest.main()
