#!/usr/bin/env python3
"""
Unit tests for ThreadNote (Threads Clone) persona engine and curriculum parser.
"""

import unittest
from app import (
    PERSONA_PROFILES,
    CURRICULUM_PRELOADED_THREADS,
    parse_curriculum_sections,
    generate_curriculum_thread
)

class TestCurriculumThreads(unittest.TestCase):

    def test_persona_profiles_configured(self):
        expected = ["elementary_teacher", "pass_candidate", "extreme_t_math", "student_minsoo", "cat_teacher"]
        for p in expected:
            self.assertIn(p, PERSONA_PROFILES)
            self.assertTrue(len(PERSONA_PROFILES[p]["name"]) > 0)
            self.assertTrue(len(PERSONA_PROFILES[p]["avatar"]) > 0)

    def test_preloaded_threads_validity(self):
        self.assertTrue(len(CURRICULUM_PRELOADED_THREADS) >= 5)
        for t in CURRICULUM_PRELOADED_THREADS:
            self.assertIn("thread_id", t)
            self.assertIn("category", t)
            self.assertIn("posts", t)
            self.assertEqual(len(t["posts"]), 3)
            self.assertIn("source_insight", t)
            self.assertIn("academic_quote", t["source_insight"])
            self.assertIn("simulated_comments", t)
            self.assertTrue(len(t["simulated_comments"]) >= 1)

    def test_parse_curriculum_sections(self):
        sample_text = """
1. 평면도형 1. 평면도형과 그 구성 요소
+ 배경 지식 +
내포와 외연
(오) 바닥에 닿은 면만 밑면이다. -> (지) 마주 보는 면도 밑면이다.
Q. 삼각형의 속성 파악을 위한 구체적인 발문?
A. 삼각형들은 변이 몇 개인가요?
[유의점] '선분' 용어 사용 X -> 3-1 도입.
"""
        sections = parse_curriculum_sections(sample_text)
        self.assertTrue(len(sections) >= 1)
        sec = sections[0]
        self.assertTrue("평면도형" in sec["title"])
        self.assertTrue(len(sec["misconceptions"]) >= 1)
        self.assertTrue(len(sec["qna"]) >= 1)

    def test_generate_curriculum_thread(self):
        sec = {
            "title": "4. 원의 성질",
            "content": ["맨홀 뚜껑이 원인 이유는 지름보다 긴 변이 없기 때문이다."],
            "misconceptions": [],
            "qna": ["Q. 맨홀 뚜껑이 원인 이유는? A. 지름이 가장 길어서 빠지지 않음."]
        }
        res = generate_curriculum_thread(sec, "pass_candidate")
        self.assertEqual(len(res["posts"]), 3)
        self.assertEqual(res["persona"]["id"], "pass_candidate")
        self.assertIn("원", res["source_insight"]["title"])


if __name__ == "__main__":
    unittest.main()
