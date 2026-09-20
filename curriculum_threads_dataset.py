"""
Comprehensive Curriculum & Exam Threads Dataset for ThreadNote
Covers:
1. 16 Diverse Personas
2. All Math Theories (Skemp, Dienes, Bruner, Piaget, Van Hiele, Freudenthal, Wertheimer, Ausubel, Brousseau, Lakatos, Polya)
3. All Math 2022 Curriculum & Content Areas (Geometry, Measurement, Numbers & Operations, Patterns, Data/Probability)
4. 2025~2026 Elementary Teacher Certification Exam Items (Korean, English, Social Studies, Science, Ethics, Practical Arts, Music, Art, PE, General)
"""

PERSONA_PROFILES = {
    "elementary_teacher": {
        "id": "elementary_teacher",
        "name": "초등 3년차 김교사",
        "handle": "elementary_kim",
        "role": "2학년 담임 • 수업 멘붕기 기록",
        "avatar": "👩‍🏫",
        "badge": "교실 현실 썰",
        "intro": "오늘도 2학년 교실에서 애들이랑 뒹굴다 멘탈 털린 초등교사의 생생한 수업 썰과 지도 꿀팁 🍎",
        "bg_gradient": "linear-gradient(135deg, #FF6B6B, #FF8E53)",
        "followers": "14.2K"
    },
    "pass_candidate": {
        "id": "pass_candidate",
        "name": "임용 수석합격생 박선배",
        "handle": "pass_onepoint",
        "role": "각론 200% 정복자",
        "avatar": "📚",
        "badge": "출제 함정 팩폭",
        "intro": "초등 임용고시 각론 단권화 마스터. 출제위원들이 눈에 불 켜고 파놓은 함정 포인트만 족집게처럼 풂 🧵",
        "bg_gradient": "linear-gradient(135deg, #4776E6, #8E54E9)",
        "followers": "32.1K"
    },
    "extreme_t_math": {
        "id": "extreme_t_math",
        "name": "극T 수학교육 분석관",
        "handle": "math_extreme_t",
        "role": "원리 & 논리 집착러",
        "avatar": "⚡",
        "badge": "3줄 팩트폭격",
        "intro": "감정 빼고 수학적 공준과 지도서 원리로만 말합니다. 반박 시 님 증명이 오개념임.",
        "bg_gradient": "linear-gradient(135deg, #00C0FF, #42E695)",
        "followers": "9.8K"
    },
    "student_minsoo": {
        "id": "student_minsoo",
        "name": "2학년 3반 김민수",
        "handle": "elem_minsoo",
        "role": "수학시간에 억울한 초딩",
        "avatar": "🎒",
        "badge": "초딩의 일기",
        "intro": "오늘 선생님이 종이 두 번 접으라고 하더니 직각이래요... 왜 각도기 안 쓰고 손으로 접음? 억울함",
        "bg_gradient": "linear-gradient(135deg, #F9D423, #FF4E50)",
        "followers": "6.4K"
    },
    "cat_teacher": {
        "id": "cat_teacher",
        "name": "냥집사 수학쌤",
        "handle": "cat_math_teacher",
        "role": "고양이 관찰형 교사",
        "avatar": "🐱",
        "badge": "냥생철학",
        "intro": "우리 집 치즈냥이 택배 상자 굴리는 거 보다가 깨달은 직육면체와 밑면의 위대한 법칙 🐾",
        "bg_gradient": "linear-gradient(135deg, #F2994A, #F2C94C)",
        "followers": "21.5K"
    },
    "super_veteran": {
        "id": "super_veteran",
        "name": "교단 30년차 최부장",
        "handle": "veteran_cho",
        "role": "관록의 장학지도 수석교사",
        "avatar": "👴",
        "badge": "부장님의 통찰",
        "intro": "교단에서 분필 잡은 지 30년. 후배 교사들의 지도안을 1초 만에 꿰뚫어 보는 관록의 교육학 썰",
        "bg_gradient": "linear-gradient(135deg, #2b5876, #4e4376)",
        "followers": "18.3K"
    },
    "pass_retry": {
        "id": "pass_retry",
        "name": "독서실 사활 건 N수생",
        "handle": "pass_or_die",
        "role": "눈물의 단권화 암기러",
        "avatar": "🔥",
        "badge": "피눈물 암기법",
        "intro": "새벽 2시 독서실에서 지도서 백구 단권화 찢을 뻔한 수험생의 눈물겨운 암기 치트키 방출 ✍️",
        "bg_gradient": "linear-gradient(135deg, #f857a6, #ff5858)",
        "followers": "15.7K"
    },
    "edutech_innovator": {
        "id": "edutech_innovator",
        "name": "에듀테크 AI 선도 정쌤",
        "handle": "edutech_jung",
        "role": "디지털 소양 연구회장",
        "avatar": "💻",
        "badge": "디지털 각론",
        "intro": "지오지브라, 알지오매스, 블록코딩으로 초등 수학·실과 각론을 3D로 해체하는 얼리어답터 교사",
        "bg_gradient": "linear-gradient(135deg, #13547a, #80d0c7)",
        "followers": "11.2K"
    },
    "liberal_arts_mom": {
        "id": "liberal_arts_mom",
        "name": "초4맘 교육 인플루언서",
        "handle": "mom_insight",
        "role": "학부모 시점 교육 칼럼니스트",
        "avatar": "🌸",
        "badge": "엄마의 시선",
        "intro": "초4 아이 수학 숙제 봐주다 지도서 각론 읽고 경악한 문과 엄마의 사이다 교육 썰 ☕",
        "bg_gradient": "linear-gradient(135deg, #a18cd1, #fbc2eb)",
        "followers": "26.4K"
    },
    "science_lab_specialist": {
        "id": "science_lab_specialist",
        "name": "과학실험 전담 송교사",
        "handle": "science_song",
        "role": "실험실 안전 & 탐구 마스터",
        "avatar": "🧪",
        "badge": "실험실 비화",
        "intro": "오늘도 비커 깨질 뻔한 위기를 넘긴 과학 전담 교사. 귀추적 추론과 순환학습 모형으로 과학 씹어먹기",
        "bg_gradient": "linear-gradient(135deg, #0ba360, #3cba92)",
        "followers": "13.9K"
    },
    "english_native_buddy": {
        "id": "english_native_buddy",
        "name": "원어민 협력교사 크리스",
        "handle": "teacher_chris",
        "role": "EFL 상호작용 코치",
        "avatar": "🗽",
        "badge": "원어민 팩폭",
        "intro": "Korean 초등 영어 수업 참관하며 Noticing 오류 피드백과 파열음 최소대립쌍 코칭하는 미국인 쌤 🇺🇸",
        "bg_gradient": "linear-gradient(135deg, #e1eec3, #f05053)",
        "followers": "16.8K"
    },
    "pe_sports_coach": {
        "id": "pe_sports_coach",
        "name": "체육부장 강코치",
        "handle": "pe_coach_kang",
        "role": "PAPS & 안전 전문 체육교사",
        "avatar": "🏃‍♂️",
        "badge": "체육관 호루라기",
        "intro": "수영장 과호흡 응급처치부터 라반의 움직임 4요소까지, 몸으로 증명하는 초등 체육 각론 썰 ⚽",
        "bg_gradient": "linear-gradient(135deg, #ff9966, #ff5e62)",
        "followers": "17.4K"
    },
    "art_music_maestro": {
        "id": "art_music_maestro",
        "name": "예체능 감성 전담 한쌤",
        "handle": "art_music_han",
        "role": "음악·미술 더블 전담",
        "avatar": "🎨",
        "badge": "예체능 아틀리에",
        "intro": "판화 찍을 때 숟가락으로 문지르고, 6/8박자 노래에 장구 장단 얹는 융합 예술 수업의 달인 🎶",
        "bg_gradient": "linear-gradient(135deg, #654ea3, #eaafc8)",
        "followers": "14.7K"
    },
    "morality_philosopher": {
        "id": "morality_philosopher",
        "name": "도덕과 철학자 윤교사",
        "handle": "moral_ethic_yoon",
        "role": "학급 평화 & 가치갈등 중재자",
        "avatar": "⚖️",
        "badge": "인성 나침반",
        "intro": "교실 싸움 중재할 때 아리스토텔레스와 칸트를 소환하는 찐 윤리학 덕후 초등교사 🏛️",
        "bg_gradient": "linear-gradient(135deg, #2c3e50, #3498db)",
        "followers": "12.0K"
    },
    "exam_evaluator": {
        "id": "exam_evaluator",
        "name": "전직 출제위원 장학사 Q",
        "handle": "evaluator_q",
        "role": "채점관 시점 비밀 해설관",
        "avatar": "🧐",
        "badge": "칼채점 주의보",
        "intro": "임용 1차 채점관 경험 다수. 수험생들이 어디서 키워드 빼먹고 0.5점 깎여 탈락하는지 적나라하게 공개",
        "bg_gradient": "linear-gradient(135deg, #000000, #434343)",
        "followers": "45.2K"
    },
    "practical_smartfarm": {
        "id": "practical_smartfarm",
        "name": "실과 스마트팜 지도교사",
        "handle": "smartfarm_teacher",
        "role": "생명기술 & 코딩 융합 연구원",
        "avatar": "🌱",
        "badge": "스마트 텃밭",
        "intro": "킬패트릭 프로젝트로 방울토마토 키우고 토양수분센서 엔트리로 제어하는 미래 농업 교육자 🍅",
        "bg_gradient": "linear-gradient(135deg, #56ab2f, #a8e063)",
        "followers": "10.5K"
    }
}

# The Master Threads Dataset (40+ deeply curated Threads spanning all domains)
ALL_CURRICULUM_THREADS = [
    # -------------------------------------------------------------
    # 1. 수학 교육론 (Math Theory) - Skemp, Dienes, Bruner, Piaget, Van Hiele, Freudenthal, Brousseau, Lakatos, Polya
    # -------------------------------------------------------------
    {
        "thread_id": "th_theory_skemp",
        "category": "수학교육론",
        "grade": "수학 기본이론",
        "persona": PERSONA_PROFILES["extreme_t_math"],
        "created_at": "12분 전",
        "metrics": {"likes": 2840, "replies": 112, "reposts": 490, "views": 14200},
        "tags": ["#스켐프", "#도구적이해", "#관계적이해", "#수학이론", "#임용적중"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "공식만 달달 외워서 분수 나눗셈 역수 곱하는 사람들에게 팩폭 날립니다 🧵👇\n\n'왜 역수를 곱하는지 설명할 수 있나요?'\n'그냥 그렇게 하라고 배워서요.'\n\n이게 바로 스켐프(Skemp)가 말한 가장 위험한 상태인 [도구적 이해]입니다."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 도구적 이해: 이유는 모르면서 기계적 규칙(방법 O, 원리 X)만 암기해 빠르게 답을 냄. 문제 조금만 변형되면 뇌정지 옴.\n• 관계적 이해: 수학적 규칙이 왜 그렇게 만들어졌는지 이유와 원리(방법 O, 원리 O)를 알아 새로운 문제에 응용 가능!\n\n시험 당일 긴장해서 공식 까먹었을 때 스스로 유도해 낼 수 있는 힘은 오직 [관계적 이해]에서만 나옵니다."
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "💡 출제위원 채점 기준:\n학생이 '2/3 ÷ 4/5'를 풀 때 단위비율 결정이나 통분 과정을 그림으로 설명할 수 있는가가 핵심 채점 포인트!\n\n도구적 이해에 머무는 수업은 인지적 사기입니다. 내일 수업 지도안에 '관계적 이해 유도 발문' 한 줄 꼭 넣으세요 📌"
            }
        ],
        "source_insight": {
            "title": "02 수학 교수·학습 이론 - 스켐프(R. Skemp)",
            "curriculum_code": "수학교육론 기본이론 01",
            "academic_quote": "도구적 이해: 방법 O, 이유·원리 X (규칙이나 공식이 구성된 이유는 모르면서 기계적으로 암기). 관계적 이해: 방법 O, 이유·원리 O (수학적 규칙이 왜 그렇게 만들어졌는지 명확한 이유와 적용 방법).",
            "core_concept": "개념적 지식과 절차적 지식의 통합 및 수학적 연결성",
            "qna": "Q. 관계적 이해의 장점? A. 학습한 내용의 기억이 오래 지속되고 까먹어도 다시 유추하여 상기 가능함."
        },
        "simulated_comments": [
            { "author": "독서실사활러", "handle": "pass_or_die", "avatar": "🔥", "content": "진짜 도구적 이해로 외웠다가 기출 B형 1번 분수 나눗셈에서 털렸던 기억남 ㅠㅠ" },
            { "author": "수석교사최", "handle": "veteran_teacher", "avatar": "👓", "content": "정확한 지적입니다. 교사의 발문이 도구적 처방에 그치면 안 됩니다." }
        ]
    },
    {
        "thread_id": "th_theory_dienes",
        "category": "수학교육론",
        "grade": "수학 기본이론",
        "persona": PERSONA_PROFILES["edutech_innovator"],
        "created_at": "25분 전",
        "metrics": {"likes": 1950, "replies": 78, "reposts": 310, "views": 8900},
        "tags": ["#디에네스", "#지각적다양성", "#수학적다양성", "#교구활용", "#임용단골"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "평행사변형 가르칠 때 종이로만 보여주면 애들이 시험 망치는 이유 🧵👇\n\n디에네스(Dienes)의 개념 학습 원리 중 수험생들이 매년 헷갈리는 [지각적 다양성의 원리] vs [수학적 다양성의 원리] 완벽 정리!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "1. 지각적 다양성: 재질이나 감각을 다양하게! (종이, 나무 블록, 지오보드 고무줄, 벽지 패턴으로 평행사변형 제시)\n2. 수학적 다양성: 비결정적 속성을 변화시키고 결정적 속성만 고정! (변의 길이, 각의 크기, 놓인 방향을 마구 돌려보지만 '두 쌍의 대변이 평행하다'는 본질만 유지)\n\n애들은 항상 똑같은 방향의 반듯한 평행사변형만 보면 비결정적 속성(가로로 누운 모양)까지 본질로 착각합니다."
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "📌 6단계 암기 청크: [자-게-공-표-상-형]\n자유놀이 → 게임 → 공통점 탐색 → 표현 → 상징화 → 형식화!\n\n교구 만지작거리며 노는 단계가 '자유놀이', 규칙성 찾는 단계가 '게임'입니다. 이 6단계 순서 객관식 시절부터 서술형까지 출제 1순위!"
            }
        ],
        "source_insight": {
            "title": "02 수학 교수·학습 이론 - 디에네스(Z. Dienes)",
            "curriculum_code": "개념 학습 원리 및 6단계",
            "academic_quote": "지각적 다양성의 원리: 지각적으로 다르지만 구조적으로 동형인 구체물 활용. 수학적 다양성의 원리: 결정적 속성은 고정하고 비결정적 속성을 변화하여 제시.",
            "core_concept": "다양한 감각적 구체물 경험을 통한 수학적 구조의 추상화",
            "qna": "Q. 지각적 다양성과 수학적 다양성의 차이? A. 지각적 다양성은 구체물의 재질·형태 다양화, 수학적 다양성은 비결정적 속성의 다양화."
        },
        "simulated_comments": [
            { "author": "초등3년차김교사", "handle": "elementary_kim", "avatar": "👩‍🏫", "content": "맞아요 지오보드로 돌려가면서 보여주니까 애들이 '어? 이것도 평행사변형이네!' 하더라고요." }
        ]
    },
    {
        "thread_id": "th_theory_bruner_piaget",
        "category": "수학교육론",
        "grade": "수학 기본이론",
        "persona": PERSONA_PROFILES["pass_candidate"],
        "created_at": "38분 전",
        "metrics": {"likes": 3120, "replies": 145, "reposts": 620, "views": 15400},
        "tags": ["#브루너EIS", "#피아제", "#반영적추상화", "#가역적사고", "#임용합격"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "초등 1학년한테 원 가르칠 때 바로 '원: 한 점으로부터 같은 거리에 있는 점들의 집합' 쓰면 F학점인 이유 🧵👇\n\n브루너의 EIS 표상 이론과 피아제의 구체적 조작기를 모르면 초등 교사 자격증 반납해야 합니다."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 활동적 표상(E): 팔 벌려 친구들과 손잡고 둥글게 원 만들기 (신체/구체물 조작)\n• 영상적 표상(I): 동그라미 그림이나 훌라후프 사진 보여주기 (시각적 이미지)\n• 기호적 표상(S): '원'이라는 글자와 반지름 r, 원주율 π 기호 쓰기\n\n피아제 형님이 말했듯 초등학생은 '구체적 조작기'라 구체물 없이 기호(S)로 직행하면 인지 부조화와 좌절만 겪게 됩니다."
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🎯 2026 기출 연계 포인트:\n피아제의 [반영적 추상화]! 십 모형 1개를 일 모형 10개로 쪼개는 '행동 그 자체'를 머릿속으로 내면화해서 받아내림 논리를 구성하는 것.\n이게 바로 임용 답안지에 들어가야 할 무적의 키워드입니다 ✍️"
            }
        ],
        "source_insight": {
            "title": "02 브루너의 EIS 이론 & 피아제의 인지발달",
            "curriculum_code": "표상 이론 및 추상화 기제",
            "academic_quote": "브루너 EIS: 활동적(E, 신체/구체물) -> 영상적(I, 그림/도식) -> 기호적(S, 문자/기호). 피아제 반영적 추상화: 대상에 대한 조작 행동을 추상화하여 논리-수학적 스키마 형성.",
            "core_concept": "아동의 인지 발달 단계에 맞춘 다중 표상(Multiple Representations) 연계 지도",
            "qna": "Q. 수 모형 조작이 반영적 추상화로 이어지는 과정? A. 구체물을 쪼개는 행동을 내면화하여 수학적 알고리즘으로 구조화함."
        },
        "simulated_comments": [
            { "author": "김교생", "handle": "student_teacher_kim", "avatar": "👩‍🎓", "content": "E->I->S 순서 안 지키고 수식부터 썼다가 지도교수님한테 털렸던 기억이 주마등처럼..." }
        ]
    },
    {
        "thread_id": "th_theory_van_hiele",
        "category": "수학교육론",
        "grade": "수학 기본이론",
        "persona": PERSONA_PROFILES["exam_evaluator"],
        "created_at": "55분 전",
        "metrics": {"likes": 4210, "replies": 210, "reposts": 980, "views": 21000},
        "tags": ["#반힐레", "#기하사고수준", "#비형식적연역", "#채점관피셜", "#임용출제1위"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "임용 1차 기하 파트 채점관 들어갔을 때 수험생 40%가 여기서 점수 다 깎여 나갔습니다 🧵👇\n\n반 힐레(Van Hiele)의 기하 사고 발달 5수준:\n'직사각형은 평행사변형이다'를 이해하는 학생은 과연 몇 수준일까요?"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 1수준(시각적 인식): 창문 보고 '네모 모양이다' 직관적 인식 (성질 모름)\n• 2수준(분석적): 네 각이 직각이고 마주 보는 변이 같다는 성질은 알지만, 도형 간의 [포함 관계]는 모름! '직사각형은 평행사변형이 아니에요'라고 우김.\n• 3수준(비형식적 연역/관계적): 드디어 성질 사이의 위계와 포함 관계를 이해! '평행사변형 중에서 네 각이 직각이면 직사각형이구나!' 국소적 조직화 가능!\n\n따라서 포함 관계를 이해하는 것은 무조건 [3수준(관계적 수준)]입니다."
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🚨 칼감점 방지 경고:\n초등 3~4학년은 2수준(분석적)에 머물기 때문에, 2022 개정 교육과정 고려사항에 '여러 가지 사각형 사이의 관계는 다루지 않는다'고 명시해 놓은 겁니다!\n\n발달 수준을 뛰어넘는 교육은 폭력입니다. 수준 상승의 비약(수단->대상) 원리를 명심하세요."
            }
        ],
        "source_insight": {
            "title": "02 반 힐레(Van Hiele) - 기하 사고 수준 이론",
            "curriculum_code": "기하학적 사고 발달 수준 및 계열성",
            "academic_quote": "제1수준(시각적/통합적) -> 제2수준(분석적: 성질 파악, 포함관계 X) -> 제3수준(비형식적 연역/관계적: 성질 정렬, 위계적 분류 및 포함관계 이해).",
            "core_concept": "사고의 대상이 다음 수준에서는 사고의 수단으로 변환되는 수준 상승의 메커니즘",
            "qna": "Q. 초등 교육과정에서 사각형의 포함관계를 직접적으로 지도하지 않는 이유? A. 초등학생의 기하 사고 수준(분석적 수준)을 고려하여 성질 탐구에 집중하기 위함."
        },
        "simulated_comments": [
            { "author": "극T분석관", "handle": "math_extreme_t", "avatar": "⚡", "content": "팩트입니다. 2수준 학생한테 사다리꼴 포함관계 들이밀면 뇌 과부하 옵니다." }
        ]
    },
    {
        "thread_id": "th_theory_freudenthal_brousseau",
        "category": "수학교육론",
        "grade": "수학 기본이론",
        "persona": PERSONA_PROFILES["super_veteran"],
        "created_at": "1시간 전",
        "metrics": {"likes": 2650, "replies": 92, "reposts": 410, "views": 11800},
        "tags": ["#프로이덴탈", "#수학화", "#안내된재발명", "#브루소", "#메타인지이동"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "30년 동안 교생 실습 지도하면서 가장 안타까웠던 수업 장면 하나 🧵👇\n\n선생님이 삼각형 넓이 구하라고 칠판에 (밑변×높이÷2) 공식 떡하니 적어놓고 문제 20개 풀리는 수업...\n\n프로이덴탈 형님이 무덤에서 통곡할 일입니다."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "수학은 완성된 지식을 받아먹는 게 아니라, 현실의 문제를 수학적으로 조직하는 [수학화(Mathematization)] 과정이어야 합니다!\n• 수평적 수학화: 현실 문제 -> 수학적 기호 표현\n• 수직적 수학화: 수학적 표현 -> 더 추상화된 기호와 공식\n\n역사 속 수학자들이 피땀 흘려 발견했던 공식을 아이가 교실에서 스스로 다시 찾아내게 돕는 것, 그것이 바로 [안내된 재발명(Guided Reinvention)]입니다."
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "⚠️ 브루소(Brousseau)의 극단적 교수학적 현상 경계:\n교사가 답을 다 알려주는 '토파즈식 외면치레'나, 교구 만지기에만 정신 팔려 본질을 잊는 '메타인지 이동'을 경계하세요.\n아이들에게 스스로 생각할 [사고실험]의 자유를 주는 수업이 진짜 명수업입니다 👴"
            }
        ],
        "source_insight": {
            "title": "02 프로이덴탈의 수학화 & 브루소의 교수학적 변환론",
            "curriculum_code": "수학교육론 교수학적 현상",
            "academic_quote": "프로이덴탈: 안내된 재발명(사고실험을 통한 재발명 유도), 수평적/수직적 수학화. 브루소: 메타인지 이동(보조수단에 사고 집중), 형식적 고착, 토파즈식 외면치레(힌트 남발).",
            "core_concept": "학문 수학을 가르칠 수 있는 학교 수학으로 변환할 때 일어나는 인지적 왜곡의 극복",
            "qna": "Q. 토파즈 효과(Topaze effect)란? A. 학생이 어려워할 때 교사가 유도 질문이나 힌트로 답을 가르쳐주어 학습 기회를 박탈하는 현상."
        },
        "simulated_comments": [
            { "author": "초등3년차김교사", "handle": "elementary_kim", "avatar": "👩‍🏫", "content": "부장님 말씀 백번 맞습니다 ㅠㅠ 교구 쓰다 보면 애들이 블록 쌓기 놀이만 하고 있어서 메타인지 이동 바로 터짐 ㅋㅋㅋ" }
        ]
    },
    {
        "thread_id": "th_theory_lakatos_polya",
        "category": "수학교육론",
        "grade": "수학 기본이론",
        "persona": PERSONA_PROFILES["pass_retry"],
        "created_at": "1시간 20분 전",
        "metrics": {"likes": 3580, "replies": 128, "reposts": 710, "views": 17500},
        "tags": ["#라카토스", "#준경험주의", "#보조정리합체법", "#폴리아", "#What_if_not"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "오늘 모의고사에서 라카토스(Lakatos) 보조정리 합체법 틀리고 독서실 계단에서 오열함 ㅠㅠ 🧵👇\n\n'수학적 지식은 영원불변의 진리가 아니라, 반례를 통해 끊임없이 개선되는 지식이다!'\n이거 시험에 무조건 나옵니다. 3대 반례 대응법 30초 컷 정리!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "1. 보조정리 합체법: 반례가 튀어나온 원인이 된 부분 추측을 찾아서 증명에 쏙 집어넣고, 원래 추측에 조건으로 추가함! (가장 생산적인 방법)\n2. 예외 배제법: 반례를 쫓아내려고 '단, ~는 제외한다'고 원래 추측에 예외 조건을 달아버림.\n3. 괴물 배제법: 반례를 '저건 다각형도 아닌 괴물이다!'라며 용어 정의를 다시 내려 쫓아냄 ㅋㅋㅋ\n\n그리고 폴리아(Polya)의 문제 만들기 전략 [What-if-not]! '만약 밑면이 사각형이 아니라면 어떻게 될까?' 조건을 뒤집어 새 문제를 만드는 기법!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "📝 수험생 단권화 암기 공식:\n폴리아 4단계: [문제 이해 -> 계획 수립 -> 계획 실행 -> 반성]\n반성 단계에서는 답이 맞았는지 확인뿐 아니라 '다른 풀이 탐색'과 '조건을 바꾼 새로운 문제 만들기'까지 가야 만점입니다!\n올해는 꼭 1차 뚫자 🔥"
            }
        ],
        "source_insight": {
            "title": "03 라카토스의 준경험주의 & 폴리아의 문제해결 교육론",
            "curriculum_code": "수학적 추측의 개선 과정 및 반성",
            "academic_quote": "라카토스: 원래 추측 -> 부분 추측 분해 -> 반례 출현 -> 보조정리 합체법(반례 원인 규명 후 증명 합체 및 조건 추가). 폴리아 문제 만들기 전략: 수용 단계, 도전 단계(What-if-not).",
            "core_concept": "오류 가능주의에 입각한 수학적 지식의 역동적 성장과 메타인지적 반성",
            "qna": "Q. 보조정리 합체법의 의의? A. 반례를 단순히 배제하지 않고 증명 개선의 기회로 삼아 수학적 지식을 확장함."
        },
        "simulated_comments": [
            { "author": "임용수석박선배", "handle": "pass_onepoint", "avatar": "📚", "content": "작년 기출 B형 3번 나눗셈 배열 규칙도 결국 폴리아의 반성 단계 지필계산 불가 시 계산기 활용과 연결됩니다. 힘내세요!" }
        ]
    },

    # -------------------------------------------------------------
    # 2. 2025~2026학년도 기출문제 전 과목 적격 타래 (Exam Questions 1:1 Targeted)
    # -------------------------------------------------------------
    {
        "thread_id": "th_exam_korean_barrett",
        "category": "국어",
        "grade": "4학년",
        "persona": PERSONA_PROFILES["pass_candidate"],
        "created_at": "1시간 40분 전",
        "metrics": {"likes": 3890, "replies": 164, "reposts": 840, "views": 19800},
        "tags": ["#2026기출", "#국어과", "#바렛", "#사실과의견", "#비판적이해"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "2026학년도 초등 임용 국어 1번 문제 보셨나요? 🧵👇\n'사실 50%도 높은 비율이다'라는 문장을 읽고 학생이 '사실'이라는 단어가 들어갔으니 사실이라고 우길 때, 교사는 뭐라고 지도해야 할까요?"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "정답: 이 문장은 [의견]입니다!\n'50%'라는 통계 숫자가 들어갔고 '사실'이라는 표현이 쓰였더라도, 그 수치에 대해 '높은 비율이다'라고 개인의 주관적인 가치 판단과 평가를 내렸기 때문입니다.\n\n바렛(Barrett)의 읽기 기능 수준:\n• 사실적 이해: 글에 명시된 내용 파악\n• 추론적 이해: 문맥으로 단어 뜻 짐작, 이어질 내용 예측\n• 비판적 이해: 글의 내용이 객관적 사실인지 글쓴이의 주관적 의견인지 타당성 평가!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🎯 2022 개정 성취기준 설정 이유 꿀팁:\n글을 읽을 때 사실과 의견을 구분해야 하는 이유는 '글쓴이의 주장이나 관점을 무비판적으로 수용하지 않고, 정보의 타당성과 신뢰성을 주체적으로 판단하는 비판적 읽기 역량을 기르기 위함'입니다!\n키워드 외워두세요 📌"
            }
        ],
        "source_insight": {
            "title": "2026 초등 임용 교육과정 A 국어 1번 - 바렛의 읽기 수준과 사실/의견",
            "curriculum_code": "2022 개정 국어과 3~4학년군 읽기",
            "academic_quote": "바렛(Barrett)의 읽기 기능: 사실적 이해, 추론적 이해, 비판적 이해, 감상적 이해. 사실과 의견 구분의 목적: 정보의 신뢰성과 타당성을 비판적으로 판단하여 주체적 수용 태도 형성.",
            "core_concept": "비판적 문해력(Critical Literacy)과 담화 텍스트의 사실-의견 판별 기제",
            "qna": "Q. '50%도 높은 비율이다'가 의견인 이유? A. 수치에 대한 화자의 주관적 평가와 가치 판단이 포함되어 있기 때문."
        },
        "simulated_comments": [
            { "author": "초등3년차김교사", "handle": "elementary_kim", "avatar": "👩‍🏫", "content": "애들이 진짜 '사실'이란 단어만 보면 무조건 사실이라고 체크하더라고요 ㅋㅋㅋ 딱 기출 포인트!" }
        ]
    },
    {
        "thread_id": "th_exam_korean_genre_writing",
        "category": "국어",
        "grade": "6학년",
        "persona": PERSONA_PROFILES["exam_evaluator"],
        "created_at": "2시간 전",
        "metrics": {"likes": 3410, "replies": 130, "reposts": 670, "views": 16900},
        "tags": ["#2026기출", "#장르중심쓰기", "#내용지식", "#담화관습", "#쓰기교육"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "설명문 쓰기 수업할 때 '선생님 쓸 말이 없어요' 하는 학생한테 모범글 따라 쓰게 시키면 왜 빵점일까요? 🧵👇\n2026 임용 국어 2번 문제의 본질을 털어드립니다."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 학생 A의 문제: 쓸 말이 없는 건 쓰기 형식을 몰라서가 아니라, 대상에 대해 알고 있는 정보인 [내용 지식(주제 지식)]이 부족하기 때문임! 브레인스토밍만 돌리지 말고 관련 서적이나 자료를 조사·수집하는 활동을 제공해야 함.\n• 결과 중심 vs 장르 중심 쓰기의 관습적 규약 관점 차이:\n- 결과 중심: 담화의 관습적 규약을 '고정불변의 정적인 문법·형식 규칙'으로 봄.\n- 장르 중심: 규약을 '사회적 소통 맥락 속에서 담화 공동체 구성원의 상호작용에 따라 끊임없이 변화하는 역동적 관습'으로 봄!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "💡 채점관의 핵심 키워드:\n'사회적 상호작용', '담화 공동체', '소통 맥락', '역동적 변화'!\n이 4개 단어 안 들어간 답안지는 전부 칼감점했습니다. 장르 중심 쓰기는 쓰기가 개인의 머릿속 작업이 아니라 '사회적 행위'라는 패러다임 전환입니다 ✍️"
            }
        ],
        "source_insight": {
            "title": "2026 초등 임용 교육과정 A 국어 2번 - 장르 중심 쓰기와 쓰기 지식",
            "curriculum_code": "2022 개정 국어과 쓰기 영역",
            "academic_quote": "쓰기 지식: 내용 지식(무엇을 쓸 것인가), 담화 지식(어떻게 쓸 것인가). 장르 중심 쓰기: 장르는 소통 맥락 속에서 존재하고 변화하는 사회적 행위. 담화 관습에 대한 역동적 관점.",
            "core_concept": "사회구성주의 작문 이론 및 장르 지식을 통한 효과적 독자 소통 필자 양성",
            "qna": "Q. 장르 중심 쓰기에서 담화 관습의 특성? A. 고정된 형식이 아니라 소통 맥락과 담화 공동체의 반응에 따라 끊임없이 변화하는 역동적 규약."
        },
        "simulated_comments": [
            { "author": "독서실사활러", "handle": "pass_or_die", "avatar": "🔥", "content": "장학사님 해설 소름... '역동적 관습' 단어 안 써서 1점 깎였던 기억납니다 ㅠㅠ" }
        ]
    },
    {
        "thread_id": "th_exam_korean_phonology",
        "category": "국어",
        "grade": "1학년",
        "persona": PERSONA_PROFILES["pass_candidate"],
        "created_at": "2시간 15분 전",
        "metrics": {"likes": 2980, "replies": 95, "reposts": 520, "views": 13800},
        "tags": ["#2025기출", "#음운변동", "#자음군단순화", "#평파열음화", "#표준발음"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "초등 1학년이 '책을 읽고'를 발음할 때 [익꼬]일까요, [일꼬]일까요? 🧵👇\n2025 국어 1번 문제! 성인 70%가 틀리게 발음하고 있는 충격적 음운 변동의 진실."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "정답은 바로 [일꼬]입니다!\n'읽다'의 어간 받침 'ㄺ'은 원칙적으로 ㄱ 앞에서 [ㄹ]로 발음한다는 예외 규정이 있음(국어 맞춤법 제11항).\n\n• 음운 변동 2단계 순서:\n1단계: 자음군 단순화 (겹받침 'ㄺ'에서 하나 탈락 -> 'ㄹ' 남음)\n2단계: 된소리되기 (어간 받침 뒤에서 'ㄱ'이 'ㄲ'으로 변함) -> 최종 [일꼬]!\n\n반면 '읽는다'는 'ㄺ'이 ㄱ으로 자음군 단순화된 후 비음 'ㄴ'을 만나 비음화되어 최종 [잉는다]가 됨!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "📌 초등 지도 포인트:\n음절 끝소리에는 오직 7개 대표음(ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ, ㅇ)만 올 수 있음!\n아이들이 '밟는'을 [발른]으로 발음하면, 'ㅂ'으로 단순화된 후 'ㄴ' 앞에서 비음화되어 [밤는]이 된다는 단계적 원리를 놀이 카드로 익히게 하세요!"
            }
        ],
        "source_insight": {
            "title": "2025 초등 임용 교육과정 A 국어 1번 - 음운 변동 단계 및 표준 발음 지도",
            "curriculum_code": "1~2학년군 문법/발음 지도",
            "academic_quote": "받침의 자음이 2개인 경우 자음군 단순화에 의해 하나가 탈락. 어간 받침 'ㄺ'은 'ㄱ' 앞에서 [ㄹ]로 발음(읽고->[일꼬]). 비음화: 자음군 단순화 후 비음 앞에서 비음으로 동화.",
            "core_concept": "음절 구조 제약과 음운 규칙의 단계적 적용을 통한 표준 발음 형성",
            "qna": "Q. '읽고'의 올바른 발음과 적용된 음운 현상? A. [일꼬], 자음군 단순화와 된소리되기."
        },
        "simulated_comments": [
            { "author": "초4맘인플루언서", "handle": "mom_insight", "avatar": "🌸", "content": "헐 저 여태까지 [익꼬]라고 발음했는데 대박 충격... 애한테 다시 알려줘야겠어요!" }
        ]
    },
    {
        "thread_id": "th_exam_english_noticing_dictogloss",
        "category": "영어",
        "grade": "4~6학년",
        "persona": PERSONA_PROFILES["english_native_buddy"],
        "created_at": "2시간 40분 전",
        "metrics": {"likes": 2740, "replies": 105, "reposts": 480, "views": 12500},
        "tags": ["#2026기출", "#영어과", "#Noticing", "#Dictogloss", "#최소대립쌍"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "Teacher Chris here! 🇺🇸 한국 초등 영어 선생님들이 가장 감탄한 최고의 리스닝-문법 융합 기법 [Dictogloss]를 아시나요? 🧵👇\n2026 임용 영어 5번 문제 완벽 분석!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 딕토글로스(Dictogloss, Wajnryb): \n선생님이 짧은 글을 자연스러운 속도로 읽어주면 학생들은 절대 쓰지 않고 듣기만 함. 두 번째 들을 때 '핵심 키워드'만 메모한 뒤, 4명 모둠이 머리를 맞대어 원래 문장을 완벽한 문법과 의미로 복원(Reconstruct)하는 협동 학습!\n\n• 노티싱(Noticing, Schmidt):\n교사가 올바른 표현을 모델링해 줬을 때(Recast), 학생이 '어? 내가 말한 문장에 오류가 있었네?' 하고 의식적으로 주의를 기울여 스스로 발화를 수정(Repair)하는 인지적 과정!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "📌 2025 기출 [Minimal Pairs (최소대립쌍)] 조건 3가지:\n1. 분절음의 수가 같아야 한다.\n2. 오직 한 곳의 분절음만 달라야 한다.\n3. 그 차이로 인해 단어의 의미가 달라져야 한다! (예: play vs pray, pin vs fin)\n영어 임용 서술형 단골 키워드입니다!"
            }
        ],
        "source_insight": {
            "title": "2025~2026 초등 임용 영어과 - Dictogloss, Noticing, Minimal Pairs",
            "curriculum_code": "2022 개정 영어과 교수·학습 방법",
            "academic_quote": "Dictogloss: 듣기와 메모를 바탕으로 원문을 협동 재구성하는 의미-형태 통합 기법. Noticing: 학습자가 목표어 입력의 언어적 특징을 의식적으로 인지하고 발화를 수정하는 기제.",
            "core_concept": "형태 초점 교수법(Focus on Form)과 학습자 능동적 발화 수정(Self-repair)",
            "qna": "Q. 최소대립쌍이 성립하기 위한 필수 조건? A. 분절음 수가 같고, 단 한 위치의 분절음만 다르며, 이로 인해 의미가 구별되어야 함."
        },
        "simulated_comments": [
            { "author": "임용수석박선배", "handle": "pass_onepoint", "avatar": "📚", "content": "크리스 쌤 설명 완벽함! 딕토글로스 스펠링 dictogloss 철자 틀려서 깎인 수험생들 많았음 ㅋㅋㅋ" }
        ]
    },
    {
        "thread_id": "th_exam_social_banks_gis",
        "category": "사회",
        "grade": "4~6학년",
        "persona": PERSONA_PROFILES["morality_philosopher"],
        "created_at": "3시간 전",
        "metrics": {"likes": 3180, "replies": 114, "reposts": 580, "views": 15200},
        "tags": ["#2026기출", "#사회과", "#뱅크스가치탐구", "#ESG", "#지리도해력"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "기업이 돈만 벌면 장땡일까요, 아니면 환경(ESG)을 지켜야 할까요? 🧵👇\n2026 임용 사회과 7번에 출제된 뱅크스(Banks)의 가치 탐구 모형으로 교실 토론 종결짓기!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "뱅크스 가치 탐구 수업 단계:\n1. 문제 인식 ('기업은 친환경 원료를 써야 하는가?')\n2. 가치 관련 행동 진술 -> 행동에 가치 이름 붙이기\n3. [대립 가치 확인]: '이윤 추구(경제적 가치)' vs '환경 보전/사회적 책임(생태적 가치)'\n4. 가치의 원천 진술 -> 대안적 가치 결과 예측\n5. 가치 선택 및 대안 모색 -> 선택에 따른 행위!\n\n학생들에게 정답을 강요하지 않고, 각 가치의 결과를 예측한 뒤 스스로 합리적 의사결정을 내리게 하는 것이 핵심입니다."
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🗺️ 2026 사회 8번 지리 도해력(Graphicacy) 꿀팁:\n지도의 4요소는 [방위표, 축척, 등고선, 기호와 범례]!\n공간 정보를 시각 자료로 가공·변환하고, 지도에 저장된 정보를 [해석/판독]해 낼 수 있는 능력이 바로 도해력입니다. 암기 필수 📌"
            }
        ],
        "source_insight": {
            "title": "2026 초등 임용 사회과 7, 8번 - 뱅크스 가치 탐구 모형 & 지리 도해력",
            "curriculum_code": "사회과 고차 사고력 및 지리 탐구",
            "academic_quote": "뱅크스(J. Banks) 가치 탐구 모형: 가치 문제 인식 -> 대립 가치 확인 -> 결과 예측 -> 가치 선택. 도해력(Graphicacy): 공간 정보를 시각 자료로 변환하고 시각 자료를 해석하는 능력.",
            "core_concept": "합리적 가치 갈등 해결 역량 및 공간 인지적 지리 정보 문해력",
            "qna": "Q. 뱅크스 모형에서 기업의 역할 관련 대립 가치? A. 기업의 자유로운 이윤 추구 vs 기업의 사회적 책임(환경 보전)."
        },
        "simulated_comments": [
            { "author": "교단30년차최부장", "handle": "veteran_cho", "avatar": "👴", "content": "윤교사 아주 훌륭해요. 아이들에게 가치를 주입하지 않고 가치 갈등을 다루는 게 2022 개정의 핵심이지요." }
        ]
    },
    {
        "thread_id": "th_exam_science_abduction_rotation",
        "category": "과학",
        "grade": "6학년",
        "persona": PERSONA_PROFILES["science_lab_specialist"],
        "created_at": "3시간 20분 전",
        "metrics": {"likes": 3670, "replies": 158, "reposts": 740, "views": 18400},
        "tags": ["#2026기출", "#과학과", "#귀추적추론", "#지구자전", "#관찰의이론의존성"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "'선생님, 번개 치고 천둥소리가 나중에 들리는 건, 달리기 빠른 자동차가 자전거보다 먼저 도착하는 거랑 똑같은 거죠?' 🧵👇\n이 말을 들은 과학 쌤의 심장이 요동치는 이유... 이게 바로 2026 과학 6번 정답인 [귀추적 추론]입니다!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 귀납: 소리굽쇠, 북, 스피커를 쳐보고 '소리 나는 물체는 떨린다'는 공통 규칙 발견\n• 연역: '길이가 짧을수록 높은 소리가 난다'는 원리를 빨대 피리에 적용\n• 귀추(Abduction): 관찰한 미지의 현상(천둥 번개 시간차)을 자신이 이미 알고 있는 다른 친숙한 현상(자동차-자전거 속도차)의 유사성에 빗대어 그럴듯한 원인을 설명해 내는 창의적 추론!\n\n과학은 정답 맞히기 학문이 아니라, 가설을 세우고 설명해 내는 귀추적 사고의 여정입니다."
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🚨 2025 과학 8번 지구 자전 방위 함정:\n'지구본을 오른쪽으로 돌린다'고 지도하면 오답 처리!\n관측자가 남쪽을 바라보고 서 있을 때 태양이 동쪽에서 떠서 서쪽으로 지므로, 지구는 [서쪽에서 동쪽(시계 반대 방향)]으로 자전한다고 명확한 방위로 지도해야 합니다 🌍"
            }
        ],
        "source_insight": {
            "title": "2025~2026 초등 임용 과학과 - 과학적 추론 3요소 & 지구 자전 모형",
            "curriculum_code": "과학과 탐구 기능 및 천체 운동",
            "academic_quote": "귀추적 추론: 이미 알고 있는 다른 현상과의 유사성에 기초하여 관찰한 미지의 현상을 설명하는 추론. 천체 방위 지도 유의점: 오른쪽/왼쪽과 같은 상대적 방향어 대신 방위(서->동)를 사용.",
            "core_concept": "가설 연역적 탐구와 귀추적 모델링, 우주 천체 관측의 좌표계 설정",
            "qna": "Q. 지구 자전 지도 시 '오른쪽/왼쪽' 용어가 부적절한 이유? A. 관측자의 시선 방향에 따라 좌우가 달라지므로 객관적인 방위(서->동)로 지도해야 함."
        },
        "simulated_comments": [
            { "author": "초딩김민수", "handle": "elem_minsoo", "avatar": "🎒", "content": "선생님 저도 옛날에 번개가 달리기 1등이고 천둥이 2등인 줄 알았어요 ㅋㅋㅋ" }
        ]
    },
    {
        "thread_id": "th_exam_ethics_aristotle_kant",
        "category": "도덕",
        "grade": "4~5학년",
        "persona": PERSONA_PROFILES["morality_philosopher"],
        "created_at": "3시간 50분 전",
        "metrics": {"likes": 3290, "replies": 121, "reposts": 590, "views": 15800},
        "tags": ["#2026기출", "#도덕과", "#아리스토텔레스", "#니코마코스윤리학", "#아레테"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "4학년 애들이 '친구를 위해서 거짓말해 준 건 착한 일 아닌가요?' 물어볼 때... 🧵👇\n2026 도덕과 9번 기출! 아리스토텔레스의 《니코마코스 윤리학》으로 우정의 본질 파헤치기."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "아리스토텔레스가 분류한 우정의 3가지 차원:\n1. 유익에 근거한 우정 (서로 도움/이득이 될 때만 친구)\n2. 쾌락에 근거한 우정 (같이 게임하고 놀 때만 재밌는 친구)\n3. [선함에 근거한 우정]: 상대방이 잘되기를 바라는 품성적 덕에 기반한 진정한 우정!\n\n유익과 쾌락은 상황이 바뀌면 금방 깨지지만, '선함'에 근거한 우정은 평생 갑니다.\n또한 덕(Arete, 아레테)이란 인간을 포함한 모든 존재가 그 기능과 목적 면에서 [탁월성]을 발휘하는 상태를 말합니다."
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "⚖️ 도덕과 학습 지도의 2대 원리:\n• 심정화의 원리: 도덕적 가치 규범을 머리로만 아는 게 아니라 가슴으로 사랑하고 감동을 느끼게 함!\n• 통합성의 원리: 인지(알고), 정의(느끼고), 행동(실천)의 일체화!\n2026 기출 정답 키워드 꼭 챙겨가세요 🏛️"
            }
        ],
        "source_insight": {
            "title": "2026 초등 임용 도덕과 9번 - 아리스토텔레스 우정론 & 아레테(덕)",
            "curriculum_code": "도덕과 3~4학년군 관계 중심",
            "academic_quote": "니코마코스 윤리학: 유익, 쾌락, 선함에 근거한 우정 중 '선함'에 근거한 우정이 참된 품성 상태. 아레테(덕): 기능과 목적 면에서의 탁월성. 심정화의 원리와 통합성의 원리.",
            "core_concept": "품성 중심 덕 윤리학과 인지·정의·행동 통합 교수학습",
            "qna": "Q. 아레테(덕)의 개념적 정의? A. 모든 존재가 그 고유한 기능과 목적 면에서 탁월성을 지니는 것."
        },
        "simulated_comments": [
            { "author": "독서실사활러", "handle": "pass_or_die", "avatar": "🔥", "content": "아레테 빈칸에 '탁월성' 쓰고 1점 챙겼을 때의 그 짜릿함이란 ㅠㅠ" }
        ]
    },
    {
        "thread_id": "th_exam_practical_kilpatrick_coding",
        "category": "실과",
        "grade": "5~6학년",
        "persona": PERSONA_PROFILES["practical_smartfarm"],
        "created_at": "4시간 전",
        "metrics": {"likes": 2950, "replies": 88, "reposts": 440, "views": 13900},
        "tags": ["#2026기출", "#실과", "#킬패트릭", "#프로젝트학습", "#스마트팜코딩"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "초등 6학년 실과 스마트팜 코딩 수업에서 센서에 '5' 대신 '오'라고 입력하면 기계가 뻗는 이유 🧵👇\n2026 실과 10번 기출! 킬패트릭 프로젝트와 엔트리 디버깅의 정석."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 킬패트릭(Kilpatrick)의 프로젝트 학습 4단계:\n[목적 설정 -> 계획 -> 실행 -> 평가]\n채소 가꾸기 전 학생들의 경험과 흥미를 조사해 재배할 채소를 고르는 단계가 바로 '목적 설정'!\n\n• 스마트팜 엔트리 프로그래밍의 결정적 버그:\n토양수분함량에 0.5 같은 소수가 들어오면 '버림' 블록으로 정수화해야 하고, 문자 '오'가 들어오면 조건문으로 [입력값 유효성 검사 (1 이상 100 이하 숫자인지 판별)] 기능을 추가해야 시스템 오작동을 막을 수 있음!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🌱 농업·농촌의 다원적 가치 암기:\n농산물 생산뿐 아니라 [환경 보전, 수자원 함양, 전통문화 계승(세시풍속), 지역사회 유지]!\n2022 개정에서 새로 추가된 성취기준이니 임용 답안에 토씨 하나 안 틀리고 쓸 수 있어야 합니다 🍅"
            }
        ],
        "source_insight": {
            "title": "2026 초등 임용 실과 10번 - 킬패트릭 프로젝트 & 스마트팜 알고리즘",
            "curriculum_code": "실과 생명기술 및 소프트웨어",
            "academic_quote": "킬패트릭 프로젝트: 목적 설정, 계획, 실행, 평가. 농업의 다원적 가치: 환경/생태계 보전, 전통문화 계승. 프로그램 디버깅: 조건문을 활용한 입력값 유효성 검사.",
            "core_concept": "생명 기술 프로젝트 학습과 피지컬 컴퓨팅 제어 알고리즘의 유효성 검증",
            "qna": "Q. 문자 데이터 입력 시 오류 방지를 위한 기능? A. 조건문을 활용하여 입력값이 1 이상 100 이하의 숫자인지 판별하는 데이터 유효성 검사 기능."
        },
        "simulated_comments": [
            { "author": "에듀테크정쌤", "handle": "edutech_jung", "avatar": "💻", "content": "실과에서 파이썬이나 블록코딩 예외처리(Exception) 개념이 기출로 나오는 시대가 됐네요 대박!" }
        ]
    },
    {
        "thread_id": "th_exam_music_hanbae_meter",
        "category": "음악",
        "grade": "4~6학년",
        "persona": PERSONA_PROFILES["art_music_maestro"],
        "created_at": "4시간 20분 전",
        "metrics": {"likes": 2810, "replies": 94, "reposts": 490, "views": 13200},
        "tags": ["#2026기출", "#음악과", "#6_8박자", "#한배", "#종묘제례악"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "'선생님, 6/8박자는 왜 3/4박자랑 박자표가 다를까요? 둘 다 한 마디에 8분음표 6개 들어가잖아요!' 🧵👇\n2026 음악 8번 기출! 서양 음악의 기준박과 국악의 '한배' 개념 완벽 정리."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 3/4박자: 사분음표가 1박! 쿵-짝-짝 3박자 계통.\n• 6/8박자: 8분음표 3개를 묶은 [점4분음표]가 1박! 쿵-치-따 쿵-치-따 2박자 계통임!\n특히 빠르게 연주할 때는 점4분음표가 기준박이 되고, 아주 느리게 연주할 때는 8분음표가 기준박이 됨!\n\n• 국악의 [한배]: 곡의 빠르기를 뜻하는 우리말!\n'한배가 짧다' = 빠르다 / '한배가 길다' = 느리다!\n(예: 진양조는 한배가 길고, 자진모리는 한배가 짧음)"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🔔 종묘제례악 악기 편성 출제 포인트:\n선율을 연주할 수 있는 타악기는 [편종, 편경, 방향]!\n음악을 시작할 때 세 번 치는 것은 [축], 끝낼 때 긁는 것은 [어]!\n이거 헷갈려서 악기 이름 잘못 쓰면 1점 그냥 날아갑니다 🎶"
            }
        ],
        "source_insight": {
            "title": "2025~2026 초등 임용 음악과 - 박자 구조, 국악 한배, 종묘제례악",
            "curriculum_code": "음악과 표현 및 감상 영역",
            "academic_quote": "6/8박자: 악곡의 빠르기에 따라 기준박이 달라짐(느릴 땐 8분음표, 빠를 땐 점4분음표). 한배: 국악에서 악곡의 빠르기. 종묘제례악 선율 타악기: 편종, 편경.",
            "core_concept": "박과 박자의 내적 셈여림 구조 및 국악 장단의 한배에 따른 악곡 분류",
            "qna": "Q. '한배를 짧게 연주한다'의 뜻? A. 템포를 빠르게 연주하여 빠른 장단으로 변화시킨다는 뜻."
        },
        "simulated_comments": [
            { "author": "초등3년차김교사", "handle": "elementary_kim", "avatar": "👩‍🏫", "content": "한배가 짧은 게 왜 빠른 건지 애들한테 '숨 한 번 쉬는 간격(배)이 짧아지니까 헉헉대며 빨리 달리는 거'라고 가르쳐요 ㅋㅋㅋ" }
        ]
    },
    {
        "thread_id": "th_exam_art_printmaking_calligraphy",
        "category": "미술",
        "grade": "3~6학년",
        "persona": PERSONA_PROFILES["art_music_maestro"],
        "created_at": "4시간 40분 전",
        "metrics": {"likes": 2690, "replies": 76, "reposts": 380, "views": 11900},
        "tags": ["#2026기출", "#미술과", "#볼록판화", "#바렌", "#궁체"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "판화 수업 때 미술실에 '바렌(Baren)' 없다고 당황하지 마세요! 숟가락 하나면 해결됩니다 🧵👇\n2025~2026 미술과 판화 & 서예 기출 3분 요약!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 바렌(문지르개): 판과 맞닿은 종이 뒷면을 골고루 문질러 잉크가 균일하게 묻어나도록 돕는 도구 (숟가락으로 완벽 대체 가능!)\n• 볼록 판화 제작 차이:\n- 우드록 판화: 우드록 표면을 누르거나 새겨서 파냄\n- 종이 판화: 두꺼운 종이를 모양대로 오려서 밑판에 붙여서 만듦!\n• 다색 판화 찍는 법: 판 하나를 색깔별로 잘라 찍거나(판 분할), 한 색 찍고 파내고 다음 색 찍는 소멸법(소거법) 활용!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🖌️ 궁체 붓글씨 'ㅇ' 쓰는 2가지 원리:\n1. 한 번에 쓰기: 시계 반대 방향으로 원을 긋고 시작과 끝의 굵기를 고르게 마무리\n2. 두 번에 나누어 쓰기: 왼쪽 반원 먼저 긋고, 오른쪽 반원을 겹쳐 굵기를 맞춤!\n모음(ㅏ, ㅓ, ㅗ, ㅜ) 위치에 따라 자음의 형태가 달라진다는 궁체의 조형미를 잊지 마세요."
            }
        ],
        "source_insight": {
            "title": "2025~2026 초등 임용 미술과 - 판화 도구 & 궁체 서예 제작 원리",
            "curriculum_code": "미술과 표현 기법 및 전통 미술",
            "academic_quote": "바렌: 종이 뒷면을 문질러 잉크를 전사하는 도구. 판화의 특성: 간접 표현, 복수성. 궁체 특징: 결합하는 모음에 따라 자음자의 형태와 접필 위치가 달라짐.",
            "core_concept": "판화의 매체적 간접성 및 한글 서체의 조형적 결구 원리",
            "qna": "Q. 종이 판화와 우드록 판화의 판 제작상 차이점? A. 우드록은 판을 새겨서 만들고, 종이 판화는 오려 붙여서 요철을 만든다."
        },
        "simulated_comments": [
            { "author": "초4맘인플루언서", "handle": "mom_insight", "avatar": "🌸", "content": "초등학교 판화 시간에 숟가락으로 문지르던 추억 돋네요 ㅋㅋㅋ 바렌이라는 정식 이름이 있었군요!" }
        ]
    },
    {
        "thread_id": "th_exam_pe_aquatics_paps",
        "category": "체육",
        "grade": "3~4학년",
        "persona": PERSONA_PROFILES["pe_sports_coach"],
        "created_at": "5시간 전",
        "metrics": {"likes": 3340, "replies": 139, "reposts": 610, "views": 16400},
        "tags": ["#2026기출", "#체육과", "#수영안전", "#과호흡응급처치", "#PAPS", "#라반"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "체육 시간에 수영하다가 애가 갑자기 손발 저리고 숨을 헐떡이며 과호흡 왔을 때... 🧵👇\n당황해서 심폐소생술 하면 큰일 납니다! 2026 체육 9번 기출 응급처치법."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 과호흡(Hyperventilation) 응급처치:\n불안과 과도한 호흡으로 체내 이산화탄소 농도가 급감한 상태이므로, 안정을 취하게 하고 천천히 깊게 코로 숨을 들이마시고 입으로 내쉬도록 유도(호흡 조절)! (과거 비닐봉지 호흡법은 위험성으로 지양)\n\n• 수영 기능 지도 난점 처방:\n- 물속 호흡 곤란: '음-(물속에서 코로 내쉬기), 파-(물 밖에서 입으로 들이마시기)' 호흡 타이밍 분리 지도\n- 발차기해도 안 나감: 무릎을 굽히지 말고 허벅지부터 물을 누르듯 발등으로 차기!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🏃‍♂️ PAPS 심폐지구력 하위 등급 처방 & 체력 증진 원리:\n심폐지구력 부족 학생에겐 [줄넘기, 오래달리기] 추천!\n원리 2가지: [점진성의 원리] (운동 강도와 시간을 단계적으로 늘림), [과부하의 원리] (일상 수준 이상의 자극 부여)!\n라반의 움직임 4요소 [신체, 공간, 노력, 관계]도 함께 박제하세요 ⚽"
            }
        ],
        "source_insight": {
            "title": "2025~2026 초등 임용 체육과 - 수영 안전, PAPS 체력 처방, 라반의 움직임",
            "curriculum_code": "체육과 스포츠 및 운동 영역",
            "academic_quote": "과호흡 대처: 심리적 안정 유지 및 호흡 속도 조절. 체력 증진 원리: 과부하의 원리, 점진성의 원리. 라반 움직임 4요소: 신체(무엇을), 공간(어디로), 노력(어떻게), 관계(누구와).",
            "core_concept": "신체 활동 안전 관리 및 운동 생리학적 체력 발달 트레이닝 원리",
            "qna": "Q. 수영 발차기로 전진하지 못하는 학생 지도 방안? A. 무릎을 과도하게 굽히지 않고 고관절부터 발등 전체로 물을 누르듯 차도록 지도."
        },
        "simulated_comments": [
            { "author": "초등3년차김교사", "handle": "elementary_kim", "avatar": "👩‍🏫", "content": "생존수영 데리고 갈 때마다 과호흡이랑 체온 떨어지는 애들 때문에 긴장 백배인데 필수 상식입니다!" }
        ]
    },
    {
        "thread_id": "th_exam_general_autonomy",
        "category": "총론",
        "grade": "전학년",
        "persona": PERSONA_PROFILES["exam_evaluator"],
        "created_at": "5시간 30분 전",
        "metrics": {"likes": 3780, "replies": 142, "reposts": 730, "views": 18200},
        "tags": ["#2026기출", "#2022개정총론", "#학교교육과정자율설계", "#창체", "#임용만점"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "2022 개정 총론 시험지 펼치자마자 1초 만에 적었어야 하는 마법의 단어 🧵👇\n'학교 교육과정 ( ㉠ )과/와 운영'\n빈칸에 들어갈 말을 못 쓰면 올해 임용 1차는 포기해야 합니다."
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "정답은 바로 [자율적인 설계] (또는 개발/설계)입니다!\n2022 개정 교육과정 총론의 가장 거대한 패러다임 변화는 국가가 정해준 것을 그대로 실행하는 수동적 교사에서 벗어나, 학교와 교사가 지역과 학생의 특성에 맞춰 교육과정을 [자율적으로 설계]하는 주체로 격상되었다는 점입니다.\n\n• 창의적 체험활동의 설계 주체:\n교사가 일방적으로 짜는 것이 아니라, [교사와 학생이 공동으로 계획하거나, 학생이 자기주도적으로 계획]해야 함!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "💡 2025 총론 기출 복습:\n학교 자율시간 운영! 3~4학년 및 5~6학년에서 학기별 시수를 20% 범위 내에서 감축하여 지역 연계 선택 과목을 개설할 수 있음!\n총론 원문 키워드를 그대로 복사하듯 머릿속에 각인하세요 🧐"
            }
        ],
        "source_insight": {
            "title": "2025~2026 초등 임용 총론 및 창의적 체험활동",
            "curriculum_code": "2022 개정 교육과정 총론 핵심",
            "academic_quote": "학교 교육과정 자율적인 설계와 운영: 국가 교육과정을 바탕으로 학교와 지역의 교육 여건을 반영하여 자율적으로 설계·운영. 창체: 교사와 학생이 공동으로 계획하거나 학생이 자기주도적으로 계획.",
            "core_concept": "학교 자율성과 교사 교육과정 문해력(Curriculum Literacy)의 극대화",
            "qna": "Q. 창의적 체험활동의 세부 내용과 방식 설계 주체? A. 교사와 학생이 공동으로 계획하거나 학생이 자기주도적으로 계획."
        },
        "simulated_comments": [
            { "author": "교단30년차최부장", "handle": "veteran_cho", "avatar": "👴", "content": "장학사님 요약 아주 깔끔합니다. 교원 연수 때 배포해도 손색이 없겠어요." }
        ]
    }
]


ADDITIONAL_CURRICULUM_THREADS = [
    # -------------------------------------------------------------
    # 3. 수학 교육론 심화: Wertheimer, Ausubel, Gagne, Constructivism, Teaching Models
    # -------------------------------------------------------------
    {
        "thread_id": "th_theory_wertheimer_ausubel",
        "category": "수학교육론",
        "grade": "수학 기본이론",
        "persona": PERSONA_PROFILES["extreme_t_math"],
        "created_at": "6시간 전",
        "metrics": {"likes": 3120, "replies": 114, "reposts": 540, "views": 14900},
        "tags": ["#베르트하이머", "#생산적사고", "#아하경험", "#오슈벨", "#선행조직자"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "평행사변형 넓이 공식을 외우지 않고 3초 만에 떠올리는 뇌의 비밀 🧵👇\n베르트하이머의 [생산적 사고] vs 기계적 암기의 천양지차!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 베르트하이머(Wertheimer)의 생산적 사고: \n평행사변형을 멍하니 보다가 왼쪽 튀어나온 직각삼각형을 잘라 오른쪽에 붙여 직사각형으로 [전체-부분의 구조적 재조직화]를 이루어내는 순간, 뇌에서 전율이 돋는 '아하 경험(Aha-experience)'이 터짐!\n\n• 오슈벨(Ausubel)의 유의미 수용학습:\n새로운 개념을 배울 때 머릿속에 미리 깔아두는 디딤돌 [선행조직자(Advance Organizer)]!\n- 설명 조직자: 상위 개념을 미리 알려줘 점진적 분화 유도 (예: 사각형 전체의 성질 먼저 소개)\n- 비교 조직자: 비슷한 동위 개념과 비교하여 통합적 조정 유도 (예: 마름모와 직사각형 차이점 대조)!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "💡 수험생 암기 키워드:\n[점진적 분화] = 상위 -> 하위! [통합적 조정] = 하위 -> 상위 또는 계통적 연결!\n베르트하이머의 '구조적 재조직화'와 오슈벨의 '선행조직자'는 2차 면접과 1차 교육론 만능 치트키입니다 📌"
            }
        ],
        "source_insight": {
            "title": "수학교육론 - 베르트하이머의 생산적 사고 & 오슈벨의 선행조직자",
            "curriculum_code": "인지주의 수학교육 이론",
            "academic_quote": "베르트하이머 생산적 사고: 전체-부분의 구조적 기능 파악을 통한 문제 재조직화(아하 경험). 오슈벨 선행조직자: 설명 조직자(점진적 분화), 비교 조직자(통합적 조정).",
            "core_concept": "유의미 학습(Meaningful learning)을 촉진하는 인지 구조의 재편 및 선행 개념 정착",
            "qna": "Q. 생산적 사고와 기계적 암기의 차이? A. 생산적 사고는 문제의 내적 구조를 통찰하여 유의미하게 해결하는 반면, 기계적 암기는 맹목적 공식 대입에 불과함."
        },
        "simulated_comments": [
            { "author": "임용수석박선배", "handle": "pass_onepoint", "avatar": "📚", "content": "비교조직자-설명조직자 구분하는 거 기출에 정말 자주 나오죠!" }
        ]
    },
    {
        "thread_id": "th_theory_math_models",
        "category": "수학교육론",
        "grade": "수학 수업모형",
        "persona": PERSONA_PROFILES["super_veteran"],
        "created_at": "6시간 30분 전",
        "metrics": {"likes": 3450, "replies": 128, "reposts": 620, "views": 16800},
        "tags": ["#수학수업모형", "#개념형성모형", "#원리탐구모형", "#귀납추론모형", "#지도안만점"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "수학 지도안 짤 때 모형 잘못 고르면 1차 시험 칼감점입니다 🧵👇\n초등수학 4대 수업 모형 3분 만에 마스터하기!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "1. [개념 형성 모형]: 범례 제시 -> 공통 성질 추상화 -> 개념 정의 (도형 단원에 제격!)\n2. [속성 모형]: 개념 정의 먼저 때리고 -> 결정적 속성+비결정적 속성 분석 (수학적 정의 명확화)\n3. [원리 탐구 모형]: 인지적 갈등 유발 -> 원리 조작 활동 -> [형식화(절차적 지식)]! (세로셈, 분수 곱셈/나눗셈 등 연산과 측정 공식에 무조건 적용)\n4. [귀납 추론 모형]: 사례 수집·관찰 -> 공통 규칙 추측 -> [반례 찾기(추측 검증)] -> 일반화 및 정당화!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "👴 30년차 부장쌤의 꿀팁:\n원리 탐구 모형의 핵심은 아이들이 수 모형이나 종이접기로 직접 원리를 조작한 뒤 스스로 '격식(알고리즘 세로셈)'으로 [형식화]하게 만드는 것입니다. 교사가 먼저 공식 써주면 감점!"
            }
        ],
        "source_insight": {
            "title": "04 수학 수업 모형 - 개념형성, 속성, 원리탐구, 귀납추론",
            "curriculum_code": "수학과 교수·학습 모형 체계",
            "academic_quote": "원리 탐구 모형: 문제상황 -> 원리 필요성 인식 -> 조작활동(개념적 지식) -> 수학적 원리의 형식화(절차적 지식) -> 익히기. 귀납 추론 모형: 사례수집 -> 추측하기 -> 추측 검증(반례 찾기) -> 일반화.",
            "core_concept": "개념적 이해에서 절차적 유창성으로의 형식화 및 반례 검증을 통한 수학적 일반화",
            "qna": "Q. 귀납 추론 모형에서 '추측의 검증' 단계의 활동? A. 새로운 다른 사례를 대입하거나 반례를 찾아 추측이 참인지 거짓인지 확인한다."
        },
        "simulated_comments": [
            { "author": "초등3년차김교사", "handle": "elementary_kim", "avatar": "👩‍🏫", "content": "원리 탐구 모형에서 '형식화' 단어 빼먹어서 모의고사 점수 날렸던 기억이 납니다 ㅠㅠ" }
        ]
    },
    {
        "thread_id": "th_theory_values_thinking",
        "category": "수학교육론",
        "grade": "수학 기본이론",
        "persona": PERSONA_PROFILES["pass_retry"],
        "created_at": "7시간 전",
        "metrics": {"likes": 2890, "replies": 98, "reposts": 470, "views": 13900},
        "tags": ["#수학의가치", "#유추적사고", "#가역적사고", "#수학적지식특성", "#단권화"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "'수학 공부해서 어디다 써먹어요?' 묻는 학생에게 교사가 던져야 할 4대 수학의 가치 🧵👇\n그리고 기출 단골인 [유추적 사고]와 [가역적 사고]!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 수학의 4대 가치: 실용적 가치(시장 장보기), 도야적 가치(논리적 사고력 신장), 문화적 가치(인류 문화 전달), 심미적 가치(증명의 아름다움과 희열)!\n\n• 수학적 사고의 정수:\n1. [유추적 사고(유비 추론)]: '이전에 다각형 넓이 구했던 거랑 비슷한 입체도형 부피 구하기는 없을까?' 두 대상의 유사한 구조에 착안하여 새 해결책을 유추하는 사고!\n2. [가역적 사고]: 일어난 변화를 거꾸로 되돌려 원래 상태로 복원하는 사고 (덧셈 <-> 뺄셈, 검산, 거꾸로 풀기 전략)!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "📝 수학적 지식의 3대 특성 짝짓기:\n• 추상화(이질적 요소 버리고 동질적 속성만 추출) -> 형식화(규칙과 편리한 기호 생성) -> 이상화(완벽한 직선, 원 가정)!\n이 기본 청크를 머릿속에 박고 시험장 들어가야 합니다 🔥"
            }
        ],
        "source_insight": {
            "title": "01 수학의 가치, 수학적 사고, 수학적 지식의 특성",
            "curriculum_code": "수학 교육의 필요성 및 지식론",
            "academic_quote": "유추적 사고: 두 대상 간의 수학적 구조의 유사성에 기초하여 문제해결 방식을 전이. 가역적 사고: 변화를 역으로 돌릴 수 있는 능력(역연산, 보존 개념). 지식의 특성: 추상화, 형식화, 이상화, 계통성.",
            "core_concept": "개연적 추론(귀납, 유추)과 논리적 사고, 수학 지식의 추상화-형식화 메커니즘",
            "qna": "Q. 유추적 추론의 유의점? A. 잠정적 추측이므로 반드시 연역적 사고에 의해 참임이 검증되어야 한다."
        },
        "simulated_comments": [
            { "author": "초딩김민수", "handle": "elem_minsoo", "avatar": "🎒", "content": "선생님 저 심미적 가치는 잘 모르겠고 실용적 가치(게임 머니 계산)는 100점입니다 ㅋㅋㅋ" }
        ]
    },

    # -------------------------------------------------------------
    # 4. 2022 개정 수학과 교육과정 성취기준 적용 시 고려사항 & 핵심 각론 제약
    # -------------------------------------------------------------
    {
        "thread_id": "th_curr_hangul_korean_ban",
        "category": "수학 각론",
        "grade": "1~2학년군",
        "persona": PERSONA_PROFILES["elementary_teacher"],
        "created_at": "7시간 30분 전",
        "metrics": {"likes": 3950, "replies": 182, "reposts": 880, "views": 20400},
        "tags": ["#초1수학", "#한글쓰기지양", "#성취기준고려사항", "#2022개정", "#초등교사공감"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "초등 1학년 수학 시험에서 숫자를 한글로 쓰라고 시험 문제 내면 장학지도 걸리는 이유 🧵👇\n2022 개정 수학과 성취기준 적용 시 고려사항 제1조!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "고려사항 원문:\n'저학년 학생들의 한글 학습 정도를 고려하여 수를 [여덟], [마흔아홉], [칠십육], [첫째] 등과 같이 한글로 쓰게 하는 것은 지양한다!'\n\n1학년 애들이 수학을 못하는 게 아니라 '여덟'의 겹받침 'ㄼ'을 못 써서 틀리고 울고불고 난리가 나기 때문입니다 ㅠㅠ\n수학 시간은 국어 맞춤법 시험 시간이 아닙니다!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "📌 초등 저학년 수학 지도의 황금률:\n1. 짝수와 홀수는 20 이하에서 '둘씩 묶어 보는 구체물 조작'으로 직관적 지도! (0이 짝수인지는 절대 다루지 않음)\n2. '더한다, 합한다, 뺀다, 덜어낸다' 등 일상용어로 먼저 친숙하게 접근하기!\n수학의 문턱을 낮추는 교육과정의 따뜻한 배려입니다 🍎"
            }
        ],
        "source_insight": {
            "title": "2022 개정 수학과 1~2학년군 수와 연산 - 성취기준 적용 시 고려사항",
            "curriculum_code": "[2수01-01~11] 성취기준 고려사항",
            "academic_quote": "저학년 학생들의 한글 학습 정도를 고려하여 수를 '여덟', '마흔아홉' 등과 같이 한글로 쓰게 하는 것은 지양한다. 짝수와 홀수는 20 이하의 범위에서 둘씩 묶어 보는 활동을 통해 직관적으로 이해하게 한다.",
            "core_concept": "발달적 기초 문해력과 수 개념 발달의 인지적 분리 배려",
            "qna": "Q. 초등 1~2학년에서 0이 짝수임을 지도하지 않는 이유? A. 둘씩 묶어보는 직관적 구체물 활동 수준에서 다루므로 0의 짝수성은 지도하지 않는다."
        },
        "simulated_comments": [
            { "author": "초4맘인플루언서", "handle": "mom_insight", "avatar": "🌸", "content": "어머나 세상에... 저 1학년 때 받아쓰기처럼 숫자 한글로 쓰게 스파르타 시켰는데 반성합니다 ㅠㅠ" }
        ]
    },
    {
        "thread_id": "th_curr_net_cone_pyramid_ban",
        "category": "수학 각론",
        "grade": "5~6학년군",
        "persona": PERSONA_PROFILES["exam_evaluator"],
        "created_at": "8시간 전",
        "metrics": {"likes": 4450, "replies": 224, "reposts": 1050, "views": 23800},
        "tags": ["#성취기준고려사항", "#원뿔전개도금지", "#각뿔전개도금지", "#칼채점", "#임용적중"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "임용 1차 시험지에 '원뿔의 전개도를 그리시오'라고 수업 계획 짜는 순간 0점 처리됩니다 🧵👇\n교육과정 고려사항을 안 읽은 수험생의 비극!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "2022 개정 수학과 성취기준 적용 시 고려사항 팩트:\n'각기둥의 전개도는 간단한 형태만 다루고, [각뿔과 원뿔의 전개도는 다루지 않는다]!'\n\n원뿔의 옆면 전개도를 펼치면 부채꼴이 나오는데, 초등학생은 부채꼴의 중심각 공식이나 호의 길이를 구하는 법을 배우지 않기 때문입니다!\n각뿔 역시 옆면 삼각형들이 모이는 꼭짓점 각도 계산이 초등 수준을 넘어서므로 전개도 지도에서 제외됩니다."
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🚨 기출에 나온 또 다른 절대 금지 조항:\n• 원그래프 그릴 때는 반드시 [눈금이 표시된 원]을 제공해야 함! (부채꼴 중심각을 직접 각도기로 재서 그리게 하면 오답!)\n• 1km와 1cm, 1t과 1g 등 지나친 단위 환산 평가 금지!\n지도 범위의 한계선(Boundary)을 아는 교사가 진짜 전문가입니다 🧐"
            }
        ],
        "source_insight": {
            "title": "2022 개정 수학과 도형과 측정 - 전개도 및 원그래프 지도 제한",
            "curriculum_code": "[6수03-06], [6수04-02] 성취기준 고려사항",
            "academic_quote": "각기둥의 전개도는 간단한 형태만 다루고, 각뿔과 원뿔의 전개도는 다루지 않는다. 원그래프를 그릴 때는 눈금이 표시된 원을 사용하게 한다.",
            "core_concept": "선행 학습 유발 방지 및 인지 발달에 맞춘 초등 수학의 외연 축소",
            "qna": "Q. 원그래프에서 눈금이 표시된 원을 제공해야 하는 이유? A. 초등 교육과정에서 부채꼴의 중심각과 호의 길이를 구하는 공식을 다루지 않기 때문."
        },
        "simulated_comments": [
            { "author": "독서실사활러", "handle": "pass_or_die", "avatar": "🔥", "content": "와... 원뿔 전개도 안 다루는 이유가 부채꼴 중심각 안 배워서라는 거 이번에 무릎 탁 치고 갑니다!" }
        ]
    },
    {
        "thread_id": "th_curr_calculator_subtraction_prime",
        "category": "수학 각론",
        "grade": "3~6학년군",
        "persona": PERSONA_PROFILES["pass_candidate"],
        "created_at": "8시간 30분 전",
        "metrics": {"likes": 3670, "replies": 135, "reposts": 680, "views": 17900},
        "tags": ["#계산기사용기준", "#소인수분해금지", "#동치관계막대모델", "#2026기출수학"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "2026학년도 기출 수학 B형 3번! '계산 결과의 규칙을 찾을 때 수가 커서 지필 계산이 어려울 때 교사는 어떻게 지도해야 할까?' 🧵👇"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "정답: '성취기준 고려사항에 근거하여 [계산기를 사용하게 한다]!'\n\n2022 개정 고려사항:\n'계산 기능을 숙달하는 것이 목적이 아닌 경우(규칙 찾기, 복잡한 문제해결, 검산의 목적 이해 등)에는 계산기를 사용하게 할 수 있다!'\n\n또 하나 기출 폭격:\n최대공약수와 최소공배수 구할 때 소인수들의 거듭제곱 곱으로 소인수분해해서 구하는 방법은 초등 평가에서 [다루지 않는다]! 오직 두 수의 공약수 나열이나 나눗셈식으로만 구해야 함!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "📐 2026 기출 막대 밀기 동치 관계 원리 (n을 이용한 수식):\n막대 a(40-18)를 오른쪽으로 n만큼 밀면 막대의 길이는 [(40+n) - (18+n)] = 40 - 18!\n'빼지는 수와 빼는 수에 같은 수를 더하거나 빼도 그 차는 항상 일정하다'는 뺄셈의 불변성 원리를 막대 이동 모델로 시각화한 문제였습니다 ✍️"
            }
        ],
        "source_insight": {
            "title": "2026 초등 임용 교육과정 B 수학 3번 - 계산기 사용 기준 & 동치 관계 수식화",
            "curriculum_code": "변화와 관계 및 수와 연산 고려사항",
            "academic_quote": "계산식의 배열에서 규칙을 찾는 활동을 할 때 필요에 따라 계산기를 사용하게 할 수 있다. 최대공약수/최소공배수 평가에서 소인수의 곱으로 나타내어 구하는 방법은 다루지 않는다.",
            "core_concept": "공학 도구(계산기)의 교육적 활용 및 뺄셈 연산의 불변성에 근거한 대수적 일반화",
            "qna": "Q. 막대를 n만큼 오른쪽으로 밀었을 때 길이를 나타내는 식? A. (40 + n) - (18 + n) = 40 - 18."
        },
        "simulated_comments": [
            { "author": "극T분석관", "handle": "math_extreme_t", "avatar": "⚡", "content": "단순 계산 노가다 시키지 말고 규칙 탐구에 집중하라는 게 교육과정의 엄밀한 철학이죠." }
        ]
    },

    # -------------------------------------------------------------
    # 5. 수학 각론 핵심 마스터 (도형, 측정, 수와 연산, 자료와 가능성 전 영역)
    # -------------------------------------------------------------
    {
        "thread_id": "th_math_circles_plates_geoboard",
        "category": "수학 각론",
        "grade": "3~4학년군",
        "persona": PERSONA_PROFILES["edutech_innovator"],
        "created_at": "9시간 전",
        "metrics": {"likes": 3280, "replies": 109, "reposts": 560, "views": 14900},
        "tags": ["#2026기출수학", "#원형도형판", "#원의정의", "#정다각형종류", "#중심각"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "2026 기출 수학 B형 2번! 못이 12개 박힌 원형 도형판에서 만들 수 있는 정다각형은 왜 딱 4종류뿐일까요? 🧵👇"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "수학적 원리 해체:\n원의 한 바퀴 중심각은 360도이고, 못이 12개면 못 사이의 한 각은 360÷12 = 30도입니다.\n정다각형을 만들려면 꼭짓점들이 원을 등분해야 하므로, 변의 개수가 12의 약수(3 이상)여야 합니다!\n\n따라서 12의 약수 중 3 이상의 수인 [3, 4, 6, 12]에 해당하는:\n• 정삼각형 (못 4칸씩 연결, 중심각 120도)\n• 정사각형 (못 3칸씩 연결, 중심각 90도)\n• 정육각형 (못 2칸씩 연결, 중심각 60도)\n• 정십이각형 (못 1칸씩 연결, 중심각 30도)!\n딱 이 4가지만 만들 수 있는 것입니다!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "⭕ 2학년과 3학년의 원 정의 차이:\n2학년: '그림과 같은 모양의 도형' (외연적/예시적 정의)\n3학년: '동그란 누름 못을 중심으로 띠종이를 한 바퀴 돌려 그린 도형' (내포적 정의를 구체적 조작으로 경험)!\n학년별 위계성을 꿰뚫고 있어야 기출 1점을 건집니다."
            }
        ],
        "source_insight": {
            "title": "2026 초등 임용 교육과정 B 수학 2번 - 원의 정의 & 원형 도형판 정다각형",
            "curriculum_code": "도형과 측정 영역 '원' 및 '정다각형'",
            "academic_quote": "원의 정의: 2학년 외연적 방법(모양 제시), 3학년 내포적 정의 조작 경험. 원형 도형판(못 12개)에서 만들 수 있는 정다각형: 정삼각형, 정사각형, 정육각형, 정십이각형 (12의 약수 조건).",
            "core_concept": "원주 등분과 정다각형 꼭짓점 분할의 정수론적/기하학적 관계",
            "qna": "Q. 못 12개 원형도형판에서 4종류 정다각형만 만들어지는 이유? A. 못의 개수 12의 약수 중 3 이상인 수가 3, 4, 6, 12뿐이어서 원주를 균등 분할할 수 있기 때문."
        },
        "simulated_comments": [
            { "author": "초등3년차김교사", "handle": "elementary_kim", "avatar": "👩‍🏫", "content": "도형판 못 개수랑 중심각 약수 관계를 서술하라는 문제 보고 감탄했습니다." }
        ]
    },
    {
        "thread_id": "th_math_fractions_benchmark",
        "category": "수학 각론",
        "grade": "3~6학년군",
        "persona": PERSONA_PROFILES["extreme_t_math"],
        "created_at": "9시간 30분 전",
        "metrics": {"likes": 3540, "replies": 131, "reposts": 610, "views": 16200},
        "tags": ["#2026기출수학", "#분수크기비교", "#벤치마크", "#기준점1_2", "#수감각"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "11/13 이랑 20/19 크기 비교할 때 분모 13×19 곱해서 통분하고 계신 분? 🧵👇\n2026 기출 수학 B형 1번! 통분 없이 1초 컷으로 분수 크기 비교하는 [벤치마크 기준점] 전략!"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• [1을 기준점으로 하기]:\n11/13은 진분수니까 1보다 작고, 20/19는 가분수니까 1보다 큼! 따라서 20/19가 무조건 큼! 통분할 이유가 1도 없음.\n\n• [1/2을 기준점으로 하기]:\n7/11과 8/15 중 어느 게 작을까?\n분모 15의 절반은 7.5이므로 8/15은 1/2보다 큼!\n분모 11의 절반은 5.5이므로 7/11도 1/2보다 큼!\n그렇다면 1/2보다 작은 분수(예: 5/12, 1/3, 2/5)를 하나 골라 넣으면 [1/2 기준점]으로 즉시 최소 분수를 가려낼 수 있음!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "💡 2022 개정 성취기준 핵심:\n'분모가 다른 분수의 크기 비교는 수 감각을 이용하여 추론하고 토론하는 활동을 강조한다!'\n기계적 통분 계산 기능에 매몰되지 않고 수 감각(Number sense)을 기르는 것이 현대 수학 교육의 핵심입니다."
            }
        ],
        "source_insight": {
            "title": "2026 초등 임용 교육과정 B 수학 1번 - 소수 및 분수의 크기 비교와 수 감각",
            "curriculum_code": "[4수01-14], [6수01-07] 성취기준 및 수 감각",
            "academic_quote": "분수의 크기 비교 시 통분 대신 벤치마크(기준점 1, 1/2 등)를 활용하여 수 감각을 기르게 지도. 소수 크기 비교 발문 의도: 자릿값 원리에 근거한 크기 비교 지도.",
            "core_concept": "벤치마크 어림 전략(Benchmark Fraction Estimation)과 자릿값 개념 체계",
            "qna": "Q. 1/2을 기준으로 분수 크기를 비교하는 과정? A. 분자의 값이 분모의 절반보다 큰지 작은지를 판별하여 크기 관계를 비교함."
        },
        "simulated_comments": [
            { "author": "독서실사활러", "handle": "pass_or_die", "avatar": "🔥", "content": "1/2 벤치마크 분수 쓰는 거 진짜 꿀팁이네요... 통분하다 계산 실수하던 시절 안녕 ㅋㅋㅋ" }
        ]
    },
    {
        "thread_id": "th_math_fraction_division_remainders",
        "category": "수학 각론",
        "grade": "5~6학년군",
        "persona": PERSONA_PROFILES["pass_candidate"],
        "created_at": "10시간 전",
        "metrics": {"likes": 3710, "replies": 149, "reposts": 720, "views": 18900},
        "tags": ["#2025기출수학", "#분수나눗셈", "#몫으로서의분수", "#동수누감", "#자연수나눗셈"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "2025 기출 수학 B형 1번! 9÷4를 분수로 나타낼 때 [자연수 나눗셈 알고리즘]과 [몫으로서의 분수]의 차이를 서술하시오 🧵👇"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "1. ㉠ 자연수 나눗셈 식: 9 ÷ 4 = 2 ... 1 (몫이 2이고 나머지가 1)\n2. ㉡ 몫으로서의 분수 식: 9 ÷ 4 = 9/4 (또는 2와 1/4)\n\n• 분수의 5가지 의미 중 [전체-부분] vs [몫]:\n- 전체-부분: 빵 1개를 5등분한 것 중의 1조각 (1/5)\n- 몫의 의미: 빵 1개를 5명이 똑같이 나누어 먹을 때 한 사람이 받는 양 (1÷5 = 1/5)!\n\n그리고 (분수)÷(분수) 도입 시 몫이 자연수가 되는 예(예: 4/5 ÷ 2/5)를 먼저 다루는 이유는, 피제수에서 제수를 몇 번 덜어낼 수 있는지 세어보는 [동수누감(포함제)] 원리로 자연수 나눗셈과 연결하기 위함입니다!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "📌 계산 과정 서술 답안:\n'4/5에서 2/5를 2번 빼면 0이 되므로 4/5 ÷ 2/5 = 2입니다.'\n이 포함제 모델링 서술 한 줄이 기출 2점을 가릅니다. 암기해 두세요 ✍️"
            }
        ],
        "source_insight": {
            "title": "2025 초등 임용 교육과정 B 수학 1번 - 분수 나눗셈의 지도 계열과 몫의 의미",
            "curriculum_code": "5~6학년군 수와 연산 '분수의 나눗셈'",
            "academic_quote": "자연수 나눗셈 알고리즘: 몫과 나머지. 몫으로서의 분수: 나눗셈의 결과를 단일 분수로 표현(a÷b = a/b). 동수누감: 피제수에서 제수를 0이 될 때까지 빼어 횟수를 구함.",
            "core_concept": "나눗셈 몫의 분수 확장 및 포함제 관점의 조작적 접근",
            "qna": "Q. 1/5을 예로 들어 '전체에 대한 부분'을 설명하면? A. 전체 1을 똑같이 5로 나눈 것 중의 1부분."
        },
        "simulated_comments": [
            { "author": "교단30년차최부장", "handle": "veteran_cho", "avatar": "👴", "content": "분수의 의미 5가지(전체-부분, 몫, 측정, 비, 연산자)는 초등 수학 교사의 필수 뼈대입니다." }
        ]
    },
    {
        "thread_id": "th_math_proportions_and_properties",
        "category": "수학 각론",
        "grade": "5~6학년군",
        "persona": PERSONA_PROFILES["extreme_t_math"],
        "created_at": "10시간 30분 전",
        "metrics": {"likes": 3050, "replies": 96, "reposts": 510, "views": 14100},
        "tags": ["#2025기출수학", "#비례식과비례배분", "#전항과후항", "#비례식성질", "#외항의곱"],
        "posts": [
            {
                "index": 1,
                "role": "hook",
                "text": "2025 기출 수학 B형 2번! 비례식 문제에서 '전항'과 '후항'을 넣어서 비의 성질을 서술하라고 했을 때 만점 받은 답안 🧵👇"
            },
            {
                "index": 2,
                "role": "story_twist",
                "text": "• 비의 기본 성질: \n'비의 [전항]과 [후항]에 0이 아닌 같은 수를 곱하거나 나누어도 비율은 같다!' (0을 곱하면 0:0이 되어 비율 정의 불가)\n\n• 비례식의 성질 vs 비의 성질:\n- 비의 성질: 한 비(a:b) 내에서 전항과 후항의 관계 (a:b = am:bm)\n- 비례식의 성질: 두 비가 같을 때(a:b = c:d), [외항의 곱은 내항의 곱과 같다(ad = bc)]!\n\n비례배분 실생활 문제:\n어제와 오늘 걸음 수 합이 5400보이고 오늘이 어제의 1.7배라면, 어제(10) : 오늘(17)로 비를 정수비로 전환한 뒤 5400 × 17/27 = 3400보!"
            },
            {
                "index": 3,
                "role": "insight_action",
                "text": "🎯 1단위 전략(Unitizing):\n전체 27단위가 5400보이므로, 1단위는 5400÷27 = 200보! 오늘 걸음은 17단위이므로 200×17 = 3400보.\n초등 지도서에서는 공식(비례배분) 외에도 이 '1단위 전략'을 반드시 가르치도록 되어 있습니다 📌"
            }
        ],
        "source_insight": {
            "title": "2025 초등 임용 교육과정 B 수학 2번 - 비의 성질과 비례배분 활용",
            "curriculum_code": "5~6학년군 수와 연산 '비례식과 비례배분'",
            "academic_quote": "비의 성질: 비의 전항과 후항에 0이 아닌 같은 수를 곱하거나 나누어도 비율은 같다. 비례식의 성질: 외항의 곱과 내항의 곱은 같다. 한 단위 전략: 전체 단위수로 1단위의 크기를 구하여 배분.",
            "core_concept": "승법적 관계의 동치성과 단위화(Unitizing)를 통한 비례 추론",
            "qna": "Q. 비의 전항과 후항에 0을 곱하면 안 되는 이유? A. 0을 곱하면 0:0이 되어 기준량이 0이 되므로 비율을 정의할 수 없다."
        },
        "simulated_comments": [
            { "author": "초4맘인플루언서", "handle": "mom_insight", "avatar": "🌸", "content": "1.7배를 10:17로 바꾸는 게 비례배분의 핵심이었군요! 애들 설명해 주기 딱 좋습니다." }
        ]
    }
]


# Merge all threads
ALL_CURRICULUM_THREADS.extend(ADDITIONAL_CURRICULUM_THREADS)

# =============================================================
# 6. Additional Master Threads for Full Persona & Exam Coverage
# =============================================================
ADDITIONAL_PERSONA_THREADS = [
    {   'category': '도형',
        "persona": PERSONA_PROFILES["student_minsoo"],
    'created_at': '11시간 전',
    'grade': '1~2학년군',
    'metrics': {'likes': 4120, 'replies': 210, 'reposts': 620, 'views': 21000},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': '오늘 수학시간에 각도기 꺼냈다가 선생님한테 압수당함... 종이 두 번 접으래요 억울함 🧵👇'},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '선생님이 동그란 색종이를 아무렇게나 한 번 접고, 접힌 선이 딱 맞닿게 또 한 번 접더니 생기는 뾰족한 귀퉁이를 보면서 '
                             "'이게 바로 직각이란다!' 하셨음.\\n\\n'선생님 90도 각도기 쓰면 1초 컷인데 왜 귀찮게 종이를 두 번 접어요?' "
                             '물어봤다가 교무실 갈 뻔 ㅠㅠ\\n근데 짝꿍 지우개 모서리 대보니까 종이접은 모서리랑 똑같이 딱 맞아서 소름 돋았음!'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': "🎒 민수의 일기 결론:\\n초등학교 2학년은 아직 각도기를 안 배우기 때문에 '종이를 반듯하게 두 번 접었을 때 생기는 "
                             "각'으로 직각을 조작적으로 배운다고 함... 어른들의 사정이란 참 복잡하다."}],
    'simulated_comments': [   {   'author': '초등3년차김교사',
                                  'avatar': '👩\u200d🏫',
                                  'content': '민수야 선생님이 각도기 뺏은 게 아니라 교육과정 지키느라 그런 거야 ㅋㅋㅋ ㅠㅠ',
                                  'handle': 'elementary_kim'},
                              {   'author': '극T수학교육분석관',
                                  'avatar': '⚡',
                                  'content': '종이를 접어 180도를 이등분(90도)하는 유클리드 원론 제1권 정의 10의 구현입니다.',
                                  'handle': 'math_extreme_t'}],
    'source_insight': {   'academic_quote': '직각은 종이를 반듯하게 두 번 접었을 때 생기는 각으로 조작적으로 정의하며, 각도기를 사용하지 '
                                            '않고 주변의 직각 모양 물건을 찾아 대어보는 직관적·조작적 활동을 강조한다.',
                          'core_concept': '형식적 각도 측정 이전의 구체물 조작을 통한 직각의 개념적 정의',
                          'curriculum_code': '[2수02-04] 각과 직각의 개념 형성',
                          'qna': 'Q. 2학년에서 직각을 지도할 때 각도기 대신 종이접기를 사용하는 이유? A. 각도기 눈금 읽기 기능 이전에 '
                                 '반듯하게 두 번 접는 대칭적 조작 활동으로 직각의 본질적 모양을 직관적으로 이해시키기 위함.',
                          'title': '2022 개정 수학 1~2학년군 - 직각의 조작적 정의 지도'},
    'tags': ['#초딩일기', '#직각', '#종이접기', '#각도기압수', '#초2수학'],
    'thread_id': 'th_minsoo_right_angle_paper'},
    {   'category': '통합교과',
        "persona": PERSONA_PROFILES["student_minsoo"],
    'created_at': '11시간 30분 전',
    'grade': '1~2학년군',
    'metrics': {'likes': 3890, 'replies': 185, 'reposts': 540, 'views': 18200},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': "오늘 통합교과 시간에 당근 편식 안 걸리려고 '오감 탐구' 핑계 댄 썰 🧵👇\\n(2025 기출 통합교과 B형 9번 "
                             '급식탐험대)'},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '선생님이 급식판 보면서 눈으로 보고(시각), 코로 냄새 맡고(후각), 손으로 만져보고(촉각), 씹는 소리 듣고(청각), '
                             "맛을 보며(미각) 오감으로 관찰하라고 하셨음!\\n\\n'선생님! 당근을 촉각으로 만져보니 너무 딱딱하고, 시각으로 보니 "
                             "색이 너무 붉어서 제 인지 구조에 갈등이 옵니다. 오늘은 관찰만 하고 안 먹겠습니다!'\\n선생님: '민수야, 미각 "
                             "탐색까지 완료해야 단원 도달이란다. 아~ 해봐.'"},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': "🥦 교실 속 통합교과 꿀지식:\\n2학년 '나' 단원의 '급식탐험대' 주제는 음식을 단순 섭취하는 게 아니라 5가지 "
                             '감각기관을 모두 동원하여 사물의 특성을 탐색하는 슬기로운 생활의 핵심 탐구 활동입니다!'}],
    'simulated_comments': [   {   'author': '초4맘인플루언서',
                                  'avatar': '🌸',
                                  'content': '민수 논리왕이네 ㅋㅋㅋ 우리 집 아들도 맨날 당근 촉각 핑계 대는데 똑같네요!',
                                  'handle': 'mom_insight'}],
    'source_insight': {   'academic_quote': '오감(시각, 청각, 후각, 미각, 촉각)을 활용하여 음식 재료의 특징을 종합적으로 탐색하고 바른 '
                                            '식습관을 기른다.',
                          'core_concept': '감각적 경험 중심의 기초 탐구 기능 발달 및 건강한 기본 생활 습관 형성',
                          'curriculum_code': "2학년 1학기 '나' 단원 급식탐험대",
                          'qna': 'Q. 급식탐험대 활동에서 오감 관찰의 교육적 의도? A. 구체적 감각 경험을 통해 음식의 다양한 속성을 관찰하고 '
                                 '음식에 대한 친밀감을 높임.',
                          'title': '2025 초등 임용 교육과정 B 통합교과 9번 - 오감을 이용한 사물 탐색'},
    'tags': ['#2025기출', '#통합교과', '#급식탐험대', '#오감관찰', '#당근탈출'],
    'thread_id': 'th_minsoo_lunch_sensory'},
    {   'category': '측정',
        "persona": PERSONA_PROFILES["cat_teacher"],
    'created_at': '12시간 전',
    'grade': '5~6학년군',
    'metrics': {'likes': 5120, 'replies': 245, 'reposts': 1280, 'views': 27400},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': '치즈냥이가 지 몸집보다 작은 택배 박스에 기어들어가는 걸 보며 깨달은 직육면체 부피의 법칙 🧵🐾👇'},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '택배 상자가 가로 30cm, 세로 20cm, 높이 10cm인데 치즈냥이가 액체처럼 흘러들어감.\\n\\n• [직육면체 '
                             '부피]:\\n한 변 1cm인 쌓기나무(1cm³)가 밑바닥에 30×20 = 600개 깔리고, 그게 10층 높이로 쌓이니까 '
                             "600 × 10 = 6000cm³!\\n공식 '가로 × 세로 × 높이'는 단순히 외우는 게 아니라 단위부피가 밑면에 몇 개 "
                             '깔려서 몇 층 쌓였는지를 세는 층별 누적 원리임!\\n\\n• [직육면체 겉넓이]:\\n냥이가 긁어대는 겉표면 6개 면의 '
                             '넓이 합! 합동인 세 쌍의 면이 마주보므로 (앞면+옆면+밑면)×2로 깔끔하게 계산 끝!'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': "🐾 냥집사 쌤의 지도 팁:\\n아이들에게 1cm³ 쌓기나무로 직접 상자 채우기를 시킨 뒤, '밑면의 넓이 × 높이'로 "
                             '일반화하게 해야 부피 공식이 뇌에 착 붙습니다. 공식 먼저 암기시키면 직육면체 겉넓이랑 부피 공식 섞여서 오답 파티 '
                             '열림!'}],
    'simulated_comments': [   {   'author': '임용수석합격생박선배',
                                  'avatar': '📚',
                                  'content': '단위부피 개수 세기 -> 가로x세로x높이 형식화 과정 서술이 기출 만점 키워드죠!',
                                  'handle': 'pass_onepoint'}],
    'source_insight': {   'academic_quote': '직육면체의 부피는 단위부피(1cm³)의 개수를 세는 조작 활동을 통해 밑면의 넓이와 높이의 '
                                            '곱으로 형식화한다. 겉넓이는 전개도 또는 합동인 세 쌍의 면의 넓이를 합하여 구한다.',
                          'core_concept': '단위 부피의 3차원 배열 구조화(Array Structuring) 및 공식 유도',
                          'curriculum_code': "5~6학년군 도형과 측정 '직육면체의 부피와 겉넓이'",
                          'qna': "Q. 직육면체 부피를 '가로×세로×높이'로 유도하는 과정? A. 밑면에 놓이는 단위부피의 개수(가로×세로)에 "
                                 '높이만큼 층을 곱함.',
                          'title': '2025 초등 임용 교육과정 B 수학 3번 - 직육면체의 부피와 겉넓이 지도'},
    'tags': ['#고양이', '#직육면체부피', '#겉넓이', '#단위부피', '#냥스타그램'],
    'thread_id': 'th_cat_volume_surface_box'},
    {   'category': '측정',
        "persona": PERSONA_PROFILES["cat_teacher"],
    'created_at': '12시간 30분 전',
    'grade': '3~4학년군',
    'metrics': {'likes': 4670, 'replies': 198, 'reposts': 920, 'views': 23100},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': "'고양이는 액체다!' 짤 보면서 피아제의 들이 보존 개념 3요소 마스터하기 🧵🐾👇"},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': "넓고 납작한 그릇에 있던 물을 좁고 긴 원통형 꽃병에 부었을 때 초등 2학년 아이는 '물이 더 많아졌어요!'라고 외칩니다 "
                             '(높이라는 한 가지 차원에만 집중하는 중심화 현상!).\\n\\n하지만 구체적 조작기에 도달하면 [보존 개념]이 '
                             "획득됨:\\n1. [가역성(Reversibility)]: '긴 꽃병 물을 다시 넓은 그릇에 부으면 처음 높이랑 "
                             "똑같아져요!' (거꾸로 되돌리기)\\n2. [동일성(Identity)]: '아무것도 더 넣거나 빼지 않았으니 물의 양은 "
                             "같아요!'\\n3. [상보성(Compensation)]: '높이는 높아졌지만 폭이 그만큼 좁아졌잖아요!'"},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': '🥛 들이 지도 4단계 계열:\\n직관적 비교 -> 직접 비교(맞대어 붓기) -> 간접 비교(임의 단위 종이컵으로 몇 잔인지 '
                             '세기) -> 표준 단위(1L, 1mL)!\\n이 4단계를 건너뛰고 L와 mL 덧셈부터 가르치면 수포자 양성 코스입니다 '
                             '🐈'}],
    'simulated_comments': [   {   'author': '교단30년차최부장',
                                  'avatar': '👴',
                                  'content': '임의 단위의 불편함(종이컵 크기가 다름)을 경험시켜야 표준 단위 L, mL가 필연적으로 '
                                             '도입되죠. 명쾌합니다.',
                                  'handle': 'veteran_cho'}],
    'source_insight': {   'academic_quote': '보존 개념 획득의 3대 논리: 가역성, 동일성, 상보성. 측정 지도 계열: 직관적 비교 -> '
                                            '직접 비교 -> 간접 비교(임의 단위) -> 표준 단위 도입.',
                          'core_concept': '지각적 왜곡 극복을 위한 인지적 보존성 획득과 측정 지도 위계',
                          'curriculum_code': "3~4학년군 측정 영역 '들이와 무게'",
                          'qna': 'Q. 보존 개념을 형성하지 못한 학생의 특징? A. 대상의 모양 변화에 따라 양이 변했다고 지각하는 '
                                 '중심화(Centration) 경향을 보임.',
                          'title': '초등수학 측정 영역 - 들이의 비교 및 피아제 보존 개념'},
    'tags': ['#고양이액체설', '#피아제', '#보존개념', '#들이측정', '#가역성'],
    'thread_id': 'th_cat_liquid_conservation'},
    {   'category': '사회·도덕',
        "persona": PERSONA_PROFILES["liberal_arts_mom"],
    'created_at': '13시간 전',
    'grade': '3~4학년군',
    'metrics': {'likes': 4230, 'replies': 218, 'reposts': 870, 'views': 21900},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': '초4 아이 사회 교과서 펼쳤다가 GIS랑 디지털 영상 지도 나오는 거 보고 기절할 뻔한 문과 엄마 🧵☕👇\\n2026 기출 '
                             '사회 8번 분석!'},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '저희 때는 종이 사회과 부도 펼쳐놓고 범례랑 등고선 외웠는데, 요즘 초4는 스마트폰으로 [디지털 영상 지도(위성사진)]를 '
                             '확대·축소하고 거리뷰로 골목길까지 봅니다!\\n\\n• 종이 지도 vs 디지털 영상 지도:\\n- 종이 지도: 정적인 '
                             '2D, 축척 변경 불가, 정보 갱신 지연\\n- 디지털 영상 지도: 항공·위성 사진으로 실시간 현실 모습 확인, 자유로운 '
                             "축척 줌인/줌아웃, 다양한 레이어(편의시설, 버스노선 등) 중첩 가능!\\n\\n학교에서 '우리 지역 명소 소개하기' 할 "
                             '때 지도 플랫폼에서 [주제도 레이어] 얹는 법을 배운대요.'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': '💡 2026 기출 키워드 박제:\\n지리정보시스템(GIS)과 디지털 영상 지도를 활용할 때 주의점은, 기술 조작 자체에 '
                             "매몰되지 않고 '공간적 분포와 인문·자연 환경의 관계'를 공간적 사고력으로 해석하도록 발문해야 한다는 점입니다 ☕"}],
    'simulated_comments': [   {   'author': '에듀테크AI선도정쌤',
                                  'avatar': '💻',
                                  'content': '어머님 정확하십니다! 요즘은 Vworld나 카카오맵으로 등고선 레이어 겹쳐보는 수업 합니다 '
                                             'ㅎㅎ',
                                  'handle': 'edutech_jung'}],
    'source_insight': {   'academic_quote': '디지털 영상 지도: 항공 사진이나 위성 영상을 활용하여 만든 지도. 장점: 최신 지리 정보 '
                                            '반영, 확대·축소 용이, 입체적 지형 및 실제 모습 직관적 파악.',
                          'core_concept': '디지털 공간 정보 리터러시 및 실생활 지리 공간 추론 능력 신장',
                          'curriculum_code': "3~4학년군 사회 '지도로 만나는 우리 지역'",
                          'qna': 'Q. 디지털 영상 지도가 종이 지도에 비해 갖는 교육적 장점? A. 확대·축소가 자유롭고 실제 사진을 통해 우리 '
                                 '지역의 구체적 모습을 직관적으로 탐색할 수 있다.',
                          'title': '2026 초등 임용 교육과정 A 사회 8번 - 디지털 영상 지도 및 공간정보(GIS) 활용'},
    'tags': ['#2026기출', '#초4사회', '#디지털영상지도', '#GIS', '#문과엄마'],
    'thread_id': 'th_mom_gis_digital_map'},
    {   'category': '사회·도덕',
        "persona": PERSONA_PROFILES["liberal_arts_mom"],
    'created_at': '13시간 30분 전',
    'grade': '3~4학년군',
    'metrics': {'likes': 3760, 'replies': 142, 'reposts': 610, 'views': 17800},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': "아이 사회 시험문제에 '아파트 쓰레기 수거장 갈등을 해결하는 민주적 절차'가 나왔는데 어른들이 먼저 배워야 함 🧵👇"},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '2025 사회 7번 기출에서 다룬 [지역 문제 해결의 4단계]:\\n1. 문제 확인 (쓰레기 악취 및 소음 갈등 '
                             '파악)\\n2. 원인 분석 및 해결 방안 탐색 (수거 시간 변경, 차폐막 설치 등)\\n3. 해결 방안 결정 (주민 '
                             '공청회, 주민 투표를 통한 민주적 의사결정)\\n4. 실천 및 평가!\\n\\n지방자치단체(시청·구청)와 '
                             '지방의회(시의회·구의회)의 역할 구분:\\n• 지방의회: 조례 제정, 예산안 심의·확정 (의결 기관)\\n• 지방자치단체: '
                             '조례 집행, 행정 서비스 제공 (집행 기관)!'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': "⚖️ 엄마의 통찰:\\n'다수결의 원리'만 앞세우면 소수의 의견이 무시되므로, 사전에 충분한 [대화와 타협]을 거쳐야 "
                             '한다는 점이 지도서 총론의 핵심입니다. 교과서가 인성 교육의 정답지네요.'}],
    'simulated_comments': [   {   'author': '도덕과철학자윤교사',
                                  'avatar': '⚖️',
                                  'content': '하버마스의 담론 윤리와 민주적 시민의식이 초등 사회과에 녹아있는 명문입니다.',
                                  'handle': 'moral_ethic_yoon'}],
    'source_insight': {   'academic_quote': '주민 참여 방법: 공청회, 주민 투표, 서명 운동, 주민 발의. 지방의회(의결)와 '
                                            '지방자치단체(집행)의 견제와 균형을 통한 민주적 문제 해결.',
                          'core_concept': '풀뿌리 민주주의와 협력적 의사결정 프로세스',
                          'curriculum_code': "3~4학년군 사회 '지역 문제의 해결'",
                          'qna': 'Q. 주민 공청회의 교육적 역할? A. 주민들의 다양한 의견을 수렴하고 갈등을 조정하는 공론장 형성.',
                          'title': '2025 초등 임용 교육과정 A 사회 7번 - 지역 문제의 민주적 해결과 주민 참여'},
    'tags': ['#2025기출', '#초4사회', '#지역문제해결', '#주민투표', '#공공기관'],
    'thread_id': 'th_mom_local_problem_solving'},
    {   'category': '과학·실과',
        "persona": PERSONA_PROFILES["science_lab_specialist"],
    'created_at': '14시간 전',
    'grade': '3~4학년군',
    'metrics': {'likes': 4820, 'replies': 194, 'reposts': 890, 'views': 22600},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': "과학실에서 비커 소리 실험하다가 애들 90%가 '큰 소리'랑 '높은 소리'를 똑같은 걸로 착각하는 멘붕의 순간 🧵🧪👇"},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': "2026 기출 과학 6번 '소리의 성질' 단원 오개념 저격!\\n\\n1. [소리의 세기 (Loudness)]:\\n- "
                             "원인: 물체의 [진동 폭(진폭)]!\\n- 북을 세게 치면 북채가 크게 튀어오르며 진폭이 커져 '큰 소리', 살살 치면 "
                             "'작은 소리'가 남!\\n\\n2. [소리의 높낮이 (Pitch)]:\\n- 원인: 물체의 [진동 "
                             "빠르기(진동수)]!\\n- 비커에 물을 조금 넣고 치면 유리잔이 빠르게 떨어 '높은 소리', 물을 많이 넣으면 무거워서 "
                             "천천히 떨어 '낮은 소리'가 남! (단, 입으로 바람을 불 때는 반대! 공기 기둥의 길이가 짧을수록 높은 소리!)"},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': "📢 기출 서술형 함정 포인트:\\n'진동수'나 '진폭'이라는 중등 용어를 초등 3학년에게 직접 정의하지 않고, '진동의 "
                             "폭'과 '진동의 빠르기'라는 일상 관찰 언어로 지도해야 한다는 지도서 유의사항을 빼먹으면 감점입니다 🧪"}],
    'simulated_comments': [   {   'author': '예체능감성전담한쌤',
                                  'avatar': '🎨',
                                  'content': '음악과에서도 셈여림(세기)이랑 음고(높낮이) 헷갈리는 애들 엄청 많은데 과학이랑 딱 '
                                             '융합되네요!',
                                  'handle': 'art_music_han'}],
    'source_insight': {   'academic_quote': '소리의 세기는 진동하는 폭(진폭)에 따라 큰 소리와 작은 소리로 구별하고, 소리의 높낮이는 '
                                            '진동하는 빠르기(진동수)에 따라 높은 소리와 낮은 소리로 구별하여 지도한다.',
                          'core_concept': '파동의 기본 물리량(진폭과 진동수)에 대한 감각적 구인 식별',
                          'curriculum_code': "3~4학년군 과학 '소리의 성질'",
                          'qna': 'Q. 실로폰을 세게 칠 때와 살살 칠 때 변하는 소리의 속성은? A. 소리의 높낮이는 일정하고 소리의 세기만 '
                                 '변한다.',
                          'title': '2026 초등 임용 교육과정 B 과학 6번 - 소리의 발생과 성질 (세기 vs 높낮이)'},
    'tags': ['#2026기출', '#초3과학', '#소리의성질', '#소리세기vs높낮이', '#실험실안전'],
    'thread_id': 'th_science_sound_pitch_amplitude'},
    {   'category': '국어·영어',
        "persona": PERSONA_PROFILES["english_native_buddy"],
    'created_at': '14시간 30분 전',
    'grade': '3~6학년군',
    'metrics': {'likes': 3980, 'replies': 156, 'reposts': 640, 'views': 18400},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': 'Korean 초등 영어 수업 참관할 때 선생님들이 제일 많이 실수하는 PPP 모형의 치명적 함정 🧵🗽👇'},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '2025 기출 영어 A형 4번 분석:\\nPPP는 [Presentation -> Practice -> Production] '
                             '3단계로 진행됨.\\n\\n• 함정 1: Presentation에서 문법 규칙을 한국어로 길게 설명함 -> No! 교사 '
                             '발화량(TTT: Teacher Talking Time)은 최소화하고 상황 맥락(Context)과 대화문 모델링을 시각 '
                             '자료로 제시해야 함!\\n• 함정 2: Practice에서 Mechanical Drill만 반복함 -> 반드시 정보 '
                             '차이(Information Gap)가 있는 [유의미한 연습(Meaningful Practice)]으로 넘어가야 함!\\n• '
                             'Production: 배운 표현을 자기 자신의 실제 상황(Real-life personalization)에 적용하여 '
                             '자유롭게 발화!'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': "🗣️ Chris's Secret Tip:\\n학생들이 말할 때 자꾸 흐름을 끊고 문법을 고쳐주는(Immediate "
                             'Correction) 대신, 발화가 끝난 뒤 자연스럽게 올바른 문장으로 다시 들려주는 [Recast]를 활용하세요! 학생의 '
                             '정의적 여과막(Affective Filter)을 낮추는 최고의 비결입니다 🇺🇸'}],
    'simulated_comments': [   {   'author': '초등3년차김교사',
                                  'avatar': '👩\u200d🏫',
                                  'content': '크리스 쌤... 저 수업 실습 때 TTT 80% 찍고 지도 교수님한테 털렸던 기억이 생생합니다 '
                                             'ㅠㅠ',
                                  'handle': 'elementary_kim'}],
    'source_insight': {   'academic_quote': 'PPP 모형: 제시(Presentation) - 연습(Practice) - '
                                            '생성(Production). 기계적 연습에서 유의미한 의사소통 연습으로 이행. 오류 수정 시 '
                                            '정의적 여과막을 고려한 간접 수정(Recast).',
                          'core_concept': '정확성(Accuracy)에서 유창성(Fluency)으로의 체계적 언어 숙달 전이',
                          'curriculum_code': '초등 영어 교수·학습 방법론 PPP 모형',
                          'qna': 'Q. Meaningful Practice와 Mechanical Practice의 차이점? A. 유의미한 연습은 '
                                 '학생이 문장의 의미를 이해하고 실제 의미 전달(Information Gap)을 수행해야 정답을 도출할 수 있음.',
                          'title': '2025 초등 임용 교육과정 A 영어 4번 - PPP 수업 모형 및 상호작용 피드백'},
    'tags': ['#2025기출', '#초등영어', '#PPP모형', '#TTT줄이기', '#원어민코칭'],
    'thread_id': 'th_chris_ppp_model_ttt'},
    {   'category': '체육',
        "persona": PERSONA_PROFILES["pe_sports_coach"],
    'created_at': '15시간 전',
    'grade': '5~6학년군',
    'metrics': {'likes': 3610, 'replies': 128, 'reposts': 580, 'views': 16900},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': '체육 시간에 아이돌 댄스만 추게 하면 교육과정 진도 빵꾸 나는 이유 🧵⚽👇\\n2025 체육 B형 11번 표현 영역 '
                             '분석!'},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '초등 6학년 표현 영역의 본질은 안무 따라 하기가 아니라 [자신의 생각과 감정을 신체 움직임으로 형상화하는 창작 '
                             '표현]입니다!\\n\\n• 라반(Laban)의 움직임 4대 요소 실전 적용:\\n1. [신체(Body)]: 신체의 어떤 '
                             '부위를 움직이는가? (손끝, 발, 온몸)\\n2. [공간(Space)]: 어디로 움직이는가? (높낮이-높은/중간/낮은 '
                             '레벨, 직선/곡선 경로)\\n3. [노력(Effort)]: 어떻게 움직이는가? (무게-무겁게/가볍게, 시간-빠르게/느리게, '
                             '흐름-자유롭게/제한되게)\\n4. [관계(Relationship)]: 누구와 무엇과 움직이는가? (개인, 짝, 소그룹, '
                             '소품과의 조화)!'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': "🏃\u200d♂️ 강코치의 원포인트 레슨:\\n아이들에게 '가을바람에 떨어지는 낙엽'을 표현하라고 할 때, '가벼운 무게 "
                             "+ 느린 시간 + 곡선 경로(노력과 공간의 결합)'를 발문으로 이끌어내야 지도안 만점이 나옵니다!"}],
    'simulated_comments': [   {   'author': '독서실사활건N수생',
                                  'avatar': '🔥',
                                  'content': '라반 신공노관(신체, 공간, 노력, 관계) 두문자로 외웠는데 실전 적용 보니까 머리에 쏙 '
                                             '들어옵니다!',
                                  'handle': 'pass_or_die'}],
    'source_insight': {   'academic_quote': '라반의 움직임 분석(LMA): 신체(Body), 공간(Space), 노력(Effort), '
                                            '관계(Relationship). 학생 스스로 움직임 요소를 탐색하여 주제에 적합한 신체 표현을 '
                                            '구성하도록 지도.',
                          'core_concept': '신체화된 감정 표현(Embodied Expression)과 움직임의 질적 분석 틀',
                          'curriculum_code': "5~6학년군 체육 '표현' 영역",
                          'qna': "Q. 낙엽의 흩날림을 라반의 노력 요소 중 '시간'과 '무게'로 설명하면? A. 느린(Sustained) 시간감과 "
                                 '가벼운(Light) 무게감으로 표현.',
                          'title': '2025 초등 임용 교육과정 B 체육 11번 - 표현 영역 창작 무용과 라반의 움직임 분석'},
    'tags': ['#2025기출', '#초6체육', '#표현영역', '#창작무용', '#라반움직임'],
    'thread_id': 'th_pe_expressive_movement_laban'},
    {   'category': '과학·실과',
        "persona": PERSONA_PROFILES["practical_smartfarm"],
    'created_at': '15시간 30분 전',
    'grade': '5~6학년군',
    'metrics': {'likes': 3490, 'replies': 115, 'reposts': 520, 'views': 15800},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': "초등 6학년 실과 시험 단골! 식품구성자전거에서 왜 '유지·당류'는 바퀴에서 퇴출당했을까요? 🧵🌱👇"},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '2025 실과 A형 11번 식생활 단원 해체!\\n\\n• [식품구성자전거 뒷바퀴 5개 식품군과 면적 비중]:\\n1. '
                             '곡류 (밥, 빵, 떡 - 탄수화물 에너지원, 가장 넓은 면적!)\\n2. 고기·생선·달걀·콩류 (단백질 공급원, 근육 '
                             '생성)\\n3. 채소류 (비타민, 무기질, 식이섬유)\\n4. 과일류 (비타민, 당류)\\n5. 우유·유제품류 (칼슘 '
                             '공급원)\\n* 유지·당류는 조리 시 이미 충분히 섭취되므로 자전거 바퀴 면적에서 제외됨!\\n\\n• 앞바퀴 물방울: '
                             '[충분한 수분 섭취]!\\n• 자전거 전체 프레임: [규칙적인 신체 운동(활동성)]을 상징!'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': '🍅 스마트팜 쌤의 영양 융합 팁:\\n아이들과 학교 텃밭에서 방울토마토(과일/채소류)와 상추(채소류)를 기르며, 이 '
                             '작물들이 우리 몸의 생리 기능을 조절하는 비타민과 무기질을 어떻게 제공하는지 연결할 때 최고의 수업이 됩니다.'}],
    'simulated_comments': [   {   'author': '초딩김민수',
                                  'avatar': '🎒',
                                  'content': '선생님 그럼 라면(유지+나트륨)은 자전거 체인에 기름칠할 때만 먹는 건가요? ㅋㅋㅋ',
                                  'handle': 'elem_minsoo'}],
    'source_insight': {   'academic_quote': '식품구성자전거: 5가지 식품군(곡류, 고기·생선·달걀·콩류, 채소류, 과일류, 우유·유제품류)의 '
                                            '균형 잡힌 섭취, 앞바퀴의 수분 섭취, 자전거 타는 모습을 통한 운동의 중요성 강조.',
                          'core_concept': '생애주기 영양 균형 및 실천적 자립 식생활 역량 함양',
                          'curriculum_code': "5~6학년군 실과 '가정생활 - 균형 잡힌 식생활'",
                          'qna': 'Q. 식품구성자전거에서 뒷바퀴 면적의 의미? A. 하루 식사에서 각 식품군이 차지해야 하는 상대적 섭취 비율과 '
                                 '중요도.',
                          'title': '2025 초등 임용 교육과정 A 실과 11번 - 균형 잡힌 식생활과 식품구성자전거'},
    'tags': ['#2025기출', '#실과', '#식품구성자전거', '#6대영양소', '#스마트팜'],
    'thread_id': 'th_smartfarm_food_bicycle_nutrition'},
    {   'category': '국어·영어',
        "persona": PERSONA_PROFILES["elementary_teacher"],
    'created_at': '16시간 전',
    'grade': '1~2학년군',
    'metrics': {'likes': 4750, 'replies': 234, 'reposts': 1100, 'views': 25800},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': "1학년 받아쓰기 시험에서 '선생님 국물이 왜 [궁물]로 발음되는데 쓸 때는 [국물]로 써요?' 질문 받고 식은땀 흘린 썰 "
                             '🧵🍎👇'},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': "2025 국어 A형 1번 '소리와 표기가 다른 단어 바르게 읽기' 지도법!\\n\\n1. [연음 법칙]: 받침 뒤에 "
                             '모음으로 시작하는 형식 형태소가 오면 받침이 뒷말 첫소리로 그대로 옮겨감 (예: 옷이 -> [오시], 꽃을 -> '
                             "[꼬츨])\\n2. [비음화(자음동화)]: 받침 'ㄱ, ㄷ, ㅂ' 뒤에 비음 'ㄴ, ㅁ'이 오면 발음을 편하게 하려고 각각 "
                             '비음인 [ㅇ, ㄴ, ㅁ]으로 바뀜!\\n- 국물 -> [궁물]\\n- 밥물 -> [밤물]\\n- 닫는 -> '
                             "[단는]!\\n\\n한글 맞춤법 제1항: '표준어는 소리대로 적되, [어법에 맞도록] 함을 원칙으로 한다!'\\n뜻을 쉽게 "
                             '구별하기 위해 각 형태소의 본모양(원형)을 밝혀 적는다는 걸 8살 눈높이에 맞게 설명하느라 진땀 뺐습니다 ㅠㅠ'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': '📝 초등 저학년 한글 지도 핵심:\\n발음과 표기가 일치하는 단어(단순 낱말)를 먼저 지도한 후, 연음 현상 -> 자음동화 '
                             '순으로 단계적 노출을 해야 아이들의 철자 혼란을 막을 수 있습니다 🍎'}],
    'simulated_comments': [   {   'author': '초4맘인플루언서',
                                  'avatar': '🌸',
                                  'content': '김교사님 설명 들으니 저도 이제 아이한테 표의주의 원리로 차근차근 설명해 줄 수 있겠어요!',
                                  'handle': 'mom_insight'}],
    'source_insight': {   'academic_quote': '소리와 표기가 다른 낱말의 지도: 연음 법칙, 비음화 등 음운 변동을 직관적으로 탐구하고, 한글 '
                                            '맞춤법의 표음주의와 표의주의(원형 밝혀 적기) 원리를 이해하도록 지도.',
                          'core_concept': '음소-문자 대응의 음운론적 규칙성 및 형태음소론적 표기 원리',
                          'curriculum_code': "1~2학년군 국어 '문법 - 소리와 표기'",
                          'qna': "Q. '국물'을 '궁물'로 쓰지 않고 원형을 밝혀 적는 이유? A. 낱말의 원래 형태와 뜻을 쉽게 파악하여 독서와 "
                                 '의사소통의 효율성을 높이기 위함.',
                          'title': '2025 초등 임용 교육과정 A 국어 1번 - 소리와 표기가 다른 단어 지도 및 어법 원리'},
    'tags': ['#2025기출', '#초1국어', '#소리와표기', '#비음화', '#연음법칙', '#초등교사공감'],
    'thread_id': 'th_elem_kim_phonology_reading'},
    {   'category': '사회·도덕',
        "persona": PERSONA_PROFILES["pass_candidate"],
    'created_at': '16시간 30분 전',
    'grade': '5~6학년군',
    'metrics': {'likes': 4410, 'replies': 172, 'reposts': 880, 'views': 21500},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': '2025 기출 사회 8번! 우리나라 4대 극점과 영해 설정 기준선 1초 컷 암기 치트키 🧵📚👇'},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '• [우리나라 4대 극점]:\\n- 동단: 경상북도 울릉군 독도 (동경 131도 52분)\\n- 서단: 평안북도 용천군 '
                             '마안도 (동경 124도 11분)\\n- 남단: 제주특별자치도 서귀포시 마라도 (북위 33도 06분)\\n- 북단: 함경북도 '
                             '온성군 유원진 (북위 43도 00분)!\\n\\n• [영해 설정 기준선의 2대 원칙]:\\n1. [통상 기선]: 해안선이 '
                             '단조로운 동해안, 울릉도, 독도, 제주도는 썰물 때의 해안선(최저 조위선)으로부터 12해리!\\n2. [직선 기선]: 섬이 '
                             '많고 복잡한 서해안과 남해안은 가장 바깥쪽에 위치한 섬들을 직선으로 연결한 선으로부터 12해리!'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': '📌 출제위원 함정 트랩:\\n대한해협은 일본과 거리가 너무 가까워서 12해리를 적용하지 못하고 [직선기선으로부터 3해리]만 '
                             '적용한다는 특수 예외 조항! 기출에 단골로 나오니 형광펜 칠하세요 ✍️'}],
    'simulated_comments': [   {   'author': '전직출제위원장학사Q',
                                  'avatar': '🧐',
                                  'content': '대한해협 3해리까지 짚어내다니... 박선배 합격생 답안 수준이 수석 맞네요.',
                                  'handle': 'evaluator_q'}],
    'source_insight': {   'academic_quote': '영해: 영토에 인접한 해양 영역으로 기선으로부터 12해리까지. 통상기선(동해안, 제주도, '
                                            '울릉도, 독도)과 직선기선(서해안, 남해안)의 적용. 대한해협은 3해리 적용.',
                          'core_concept': '주권의 지리적 공간적 범위와 해양법 협약에 따른 경계 획정',
                          'curriculum_code': "5~6학년군 사회 '국토와 자연환경'",
                          'qna': 'Q. 서해안과 남해안에서 직선기선을 적용하는 이유? A. 해안선이 복잡하고 섬이 많아 최저조위선을 기준으로 하면 '
                                 '영해 경계가 불규칙해지기 때문.',
                          'title': '2025 초등 임용 교육과정 A 사회 8번 - 국토의 영역(영토, 영해, 영공)과 위치 특성'},
    'tags': ['#2025기출', '#초5사회', '#국토와자연환경', '#4대극점', '#영토영해영공'],
    'thread_id': 'th_pass_korean_territory_limits'},
    {   'category': '총론',
        "persona": PERSONA_PROFILES["super_veteran"],
    'created_at': '17시간 전',
    'grade': '전학년',
    'metrics': {'likes': 4010, 'replies': 159, 'reposts': 740, 'views': 19600},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': "2022 개정 총론을 관통하는 단 하나의 철학: '깊이 있는 학습(Deep Learning)'의 실체를 모르면 2차 면접 "
                             '탈락입니다 🧵👴👇'},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': "후배 교사들이 '깊이 있는 학습'이 뭐냐고 물어보면 저는 3가지를 말합니다:\\n1. 단편적 사실 암기를 털어내고, 학문의 "
                             '[핵심 아이디어(Big Ideas)]를 중심으로 내용을 엄선할 것!\\n2. 교과 고유의 사고와 탐구 방식을 경험하는 '
                             '[학생 주도형 탐구 활동]을 설계할 것!\\n3. 학습한 내용을 삶의 맥락에 적용하고 [자신의 배움 과정을 스스로 '
                             '성찰]하게 할 것!\\n\\n그리고 모든 학습의 토대가 되는 [기초 소양 3대장]:\\n• 언어 소양 (문해력)\\n• '
                             '수리 소양 (수리적 사고력)\\n• 디지털 소양 (디지털 기술과 윤리)!'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': "👴 부장 교사의 직언:\\n'교과서를 다 가르치려 하지 마라. 핵심 아이디어 하나를 깊게 파고들어 아이들이 자기 삶과 연결 "
                             "짓게 만드는 교사가 진짜 1급 정교사다.'"}],
    'simulated_comments': [   {   'author': '초등3년차김교사',
                                  'avatar': '👩\u200d🏫',
                                  'content': '부장님 말씀 가슴에 새깁니다... 진도 빼기에 급급했던 제 수업 반성하게 됩니다.',
                                  'handle': 'elementary_kim'}],
    'source_insight': {   'academic_quote': '깊이 있는 학습: 교과 내 깊이 있는 학습을 위해 교과 고유의 탐구 과정을 강조하고, 학습 '
                                            '내용을 실제 삶과 연계하며, 학습에 대한 성찰을 유도. 기초 소양: 언어 소양, 수리 소양, '
                                            '디지털 소양.',
                          'core_concept': '역량 함양을 위한 지식 구조화 및 전이 가능한 개념적 이해 추구',
                          'curriculum_code': '2022 개정 교육과정 총론 주요 개정 방향',
                          'qna': 'Q. 2022 개정 총론에서 제시한 3대 기초 소양? A. 언어 소양, 수리 소양, 디지털 소양.',
                          'title': '2025 초등 임용 교육과정 B 총론 6번 - 2022 개정 총론 깊이 있는 학습 및 기초 소양'},
    'tags': ['#2025기출', '#2022개정총론', '#깊이있는학습', '#기초소양3대요소', '#장학지도'],
    'thread_id': 'th_veteran_deep_learning_competency'},
    {   'category': '음악',
        "persona": PERSONA_PROFILES["art_music_maestro"],
    'created_at': '17시간 30분 전',
    'grade': '3~4학년군',
    'metrics': {'likes': 3840, 'replies': 147, 'reposts': 670, 'views': 17200},
    'posts': [   {   'index': 1,
                     'role': 'hook',
                     'text': '국악 민요 부를 때 전라도 노래랑 강원도 노래 느낌이 왜 완전히 다를까요? 🧵🎶👇\\n2025 음악 A형 6번 '
                             "'토리(Tori)' 3분 완전 정복!"},
                 {   'index': 2,
                     'role': 'story_twist',
                     'text': '각 지방 민요의 고유한 음악적 방언(특징)을 [토리]라고 합니다:\\n\\n1. [남도 민요 - 육자배기토리 '
                             "(전라도)]:\\n- 구성음: 미, 라, 시\\n- 시김새: '미'는 굵게 떨고(떠는 목), '도'에서 '시'로 꺾어 "
                             '내림(꺾는 목)! 한과 흥이 진하게 묻어남 (진도아리랑, 강강술래)\\n\\n2. [동부 민요 - 메나리토리 '
                             "(강원도·경상도·함경도)]:\\n- 구성음: 미, 솔, 라, 도, 레 (하행할 때 '라-솔-미' 진행이 특징!)\\n- "
                             "정선아리랑, 늴리리야, 쾌지나칭칭나네\\n\\n3. [서도 민요 - 수심가토리 (황해도·평안도)]:\\n- '레, 라' "
                             '중심음에 콧소리를 섞어 잘게 떨어줌(콧소리와 애수 어린 느낌)!'},
                 {   'index': 3,
                     'role': 'insight_action',
                     'text': '🪘 장구 반주와 형식 꿀팁:\\n민요는 혼자 부르는 독창보다 한 사람이 앞소리를 메기면 여럿이 뒷소리를 받는 [메기고 받는 '
                             "형식]이 제맛입니다. '말붙임새'를 살려 장구 장단에 노랫말을 얹어보세요 🎶"}],
    'simulated_comments': [   {   'author': '초딩김민수',
                                  'avatar': '🎒',
                                  'content': '선생님 강강술래 부를 때 왜 자꾸 목을 떠나 했더니 그게 떠는 목이었군요 ㅋㅋㅋ',
                                  'handle': 'elem_minsoo'}],
    'source_insight': {   'academic_quote': '토리의 종류: 남도(육자배기토리: 떠는 목 미, 꺾는 목 도-시), 동부(메나리토리: 라-솔-미 '
                                            '하행), 서도(수심가토리: 잘게 떠는 소리). 가창 형식: 메기고 받는 형식, 말붙임새 지도.',
                          'core_concept': '전통 음악 어법의 시김새 체계화 및 구전 심상 표현력 함양',
                          'curriculum_code': "3~4학년군 음악 '표현 - 국악의 멋'",
                          'qna': "Q. 육자배기토리의 대표적인 시김새 특징? A. '미'에서 굵게 떨고, '도'에서 '시'로 꺾어 내리는 특징이 "
                                 '있다.',
                          'title': '2025 초등 임용 교육과정 A 음악 6번 - 우리나라 민요의 지역별 토리 및 가창 지도'},
    'tags': ['#2025기출', '#초4음악', '#국악토리', '#육자배기토리', '#메나리토리', '#수심가토리'],
    'thread_id': 'th_han_music_tori_system'},
]

ALL_CURRICULUM_THREADS.extend(ADDITIONAL_PERSONA_THREADS)

print(f'Final master threads pool updated: {len(ALL_CURRICULUM_THREADS)} total threads!')

# =========================================================
# 2022 개정 교육과정 기출 스타일 수학 각론 스레드
# 파트 A: 도형 영역 챕터 1~5 (18개)
# 파트 B: 도형 영역 챕터 6~10 (17개)
# 파트 C: 측정/수와연산/통계 영역 챕터 11~18 (24개)
# 파트 D: 수학교육론 (15개)
# 총 74개 신규 스레드 추가
# =========================================================
import sys as _sys
import os as _os

def _load_part(filename):
    path = _os.path.join(_os.path.dirname(__file__), 'scratch', filename)
    ns = {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            exec(f.read(), ns)
        for v in ns.values():
            if isinstance(v, list) and v and isinstance(v[0], dict) and 'thread_id' in v[0]:
                return v
    except Exception as e:
        print(f'[Warning] {filename} 로드 실패: {e}', file=_sys.stderr)
    return []

_part_a = _load_part('math_threads_part_A.py')
_part_b = _load_part('math_threads_part_B.py')
_part_c = _load_part('math_threads_part_C.py')
_part_d = _load_part('math_threads_part_D.py')

MATH_CURRICULUM_THREADS = _part_a + _part_b + _part_c + _part_d
ALL_CURRICULUM_THREADS.extend(MATH_CURRICULUM_THREADS)

print(f'Final master threads pool updated: {len(ALL_CURRICULUM_THREADS)} total threads! (수학 각론 {len(MATH_CURRICULUM_THREADS)}개 포함)')
