#!/usr/bin/env python3
import json
import re

DB_PATH = 'uploads/user_threads.json'
with open(DB_PATH, 'r', encoding='utf-8') as f:
    threads = json.load(f)

# 1. Specifically clean up Thread 102
t102 = threads[102]
if t102.get('thread_id') == 'user_1789743258790_952':
    t102['posts'][0]['text'] = (
        '"선생님, 분수의 나눗셈을 할 때 왜 뒤의 분수를 뒤집어서 곱해야(역수의 곱) 하나요?"\n\n'
        '초등 임용 1차 기출 0순위 제재입니다! 단순한 기계적 암기가 아니라 **\'포함제 vs 등분제 맥락\'**과 '
        '**\'수직선·면적 모델을 통한 역수 곱 알고리즘의 원리적 형식화\'** 과정을 완벽히 서술할 수 있어야 합니다.'
    )
    t102['posts'][1]['text'] = (
        '**분수 나눗셈의 2대 지도 맥락**\n\n'
        '1. **포함제(동수누감) 맥락**\n'
        '• 전체 양에서 나누는 양을 **\'몇 번 덜어낼 수 있는가\'**를 묻는 맥락입니다.\n'
        '• 예: 4 ÷ 1/3 ➔ 1 속에 1/3이 3번 들어가므로, 4 속에는 4 × 3 = 12번 들어감을 직관적으로 파악합니다.\n\n'
        '2. **등분제(단위 비율 구하기) 맥락**\n'
        '• 주어진 양이 부분에 해당할 때, **\'전체 1(단위량)에 해당하는 양\'**을 구하는 맥락입니다.\n\n'
        '**\'역수의 곱\' 알고리즘 형식화 2단계 원리 (이중 수직선 모델)**\n'
        '• 예: 4 ÷ 2/3 에서 전체 1에 해당하는 양을 구할 때\n'
        '- 1단계: 단위분수 1/3에 해당하는 양을 구하기 위해 **분자 2로 나눕니다** (4 ÷ 2 = 4 × 1/2).\n'
        '- 2단계: 전체 1에 해당하는 양을 구하기 위해 **분모 3을 곱합니다** (4 × 1/2 × 3 = 4 × 3/2).\n'
        '➔ 결론: 나누는 수의 분모와 분자를 바꾼 **\'역수를 곱하는 알고리즘(× 3/2)\'**으로 형식화됩니다!'
    )
    t102['posts'][2]['text'] = (
        '💡 **임용 1차 서술형 채점 방어 가이드**\n\n'
        '분수 나눗셈의 역수 곱 지도 방안을 쓸 때 단순 \'통분해서 계산한다\'만 쓰면 출제 의도에 따라 감점될 수 있습니다!\n\n'
        '등분제 맥락의 단위량 모델에서는 반드시 **"단위분수에 해당하는 양을 구하기 위해 분자로 나누고, 전체 1의 양을 구하기 위해 분모를 곱한다"**는 '
        '2단계 조작 원리와 학술적 연결 과정을 명확히 기술해야 만점을 받습니다!'
    )

# 2. Specifically clean up Thread 103
t103 = threads[103]
if t103.get('thread_id') == 'user_1789743258790_931':
    t103['posts'][1]['text'] = (
        '**도형 및 수 배열에서 대응 관계 지도 3단계**\n\n'
        '1. **구체적 조작 및 표로 나타내기**\n'
        '• 배열 순서(탁자 수)가 1, 2, 3, …으로 변함에 따라 대응하는 양(사람 수)이 4, 6, 8, …으로 변함을 표로 정리합니다.\n'
        '• 이때 한 양의 변화만 보는 것이 아니라 **\'두 양의 변화를 함께 고려\'**하도록 지도합니다.\n\n'
        '2. **대응 규칙의 언어화 및 일반화**\n'
        '• "탁자가 1개 늘어날 때마다 사람은 2명씩 늘어난다"는 한 양의 순차적 변화(재귀적 규칙)에 머물지 않고,\n'
        '• "사람 수는 탁자 수에 2를 곱한 후 2를 더한 것과 같다"는 **두 양 사이의 수직적 대응 관계(함수적 규칙)**를 언어로 표현하게 합니다.\n\n'
        '3. **기호를 사용한 식 세우기 (변수 개념 기초)**\n'
        '• 탁자 수를 □, 사람 수를 △라 할 때, △ = □ × 2 + 2 로 표현합니다.\n'
        '• 여기서 기호는 특정한 미지수가 아니라, **상황에 따라 변하는 여러 값을 나타내는 \'변수(Variable)\'의 기초**가 됩니다.'
    )

# 3. Specifically clean up Thread 108
t108 = threads[108]
if t108.get('thread_id') == 'user_1789743258790_126':
    t108['posts'][1]['text'] = (
        '**1. 원주와 지름의 비례 관계 및 원주율의 정의**\n'
        '- **정비례 관계**: 원의 지름이 2배, 3배 커지면 둘레인 **원주**도 정확히 2배, 3배 커집니다.\n'
        '- **원주율의 정의**: **\'지름에 대한 원주의 비율\'**(원주 ÷ 지름)로 정의되며, 원의 크기와 관계없이 **항상 일정한 값**(약 3.14)을 갖습니다.\n\n'
        '**2. 등적변형을 통한 원의 넓이 공식 유도**\n'
        '- 원을 8, 16, 32, 64등분... 한없이 잘게 잘라 서로 번갈아 엇갈려 붙이면 점차 **직사각형** 모양에 한없이 가까워집니다.\n'
        '- **직사각형의 가로**: **원주의 1/2** = (지름 × 원주율) × 1/2 = **반지름 × 원주율**\n'
        '- **직사각형의 세로**: 원의 **반지름**\n'
        '- **공식 도출**: **원의 넓이** = **직사각형의 넓이** = 가로 × 세로 = (반지름 × 원주율) × 반지름 = **반지름 × 반지름 × 원주율**'
    )
    t108['posts'][2]['text'] = (
        '💡 **임용 1차 서술형 칼채점 대비 포인트**\n\n'
        '1. 원주율의 정의 문항에서는 반드시 **[지름에 대한 원주의 비율]** 또는 **[원주 ÷ 지름]**을 정확한 용어로 서술하십시오. \'원주와 지름의 비\'처럼 기준량을 누락하면 감점됩니다.\n'
        '2. 원의 넓이 유도 서술 시 **[등적변형]**, **[직사각형의 가로 = 원주의 1/2 = 반지름 × 원주율]**, **[직사각형의 세로 = 반지름]**의 논리적 연결 고리를 완벽하게 인출하십시오!'
    )

def clean_latex(text):
    if not isinstance(text, str):
        return text
    # LaTeX replacements
    text = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', text)
    text = re.sub(r'\\text\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', text)
    text = text.replace(r'\times', '×')
    text = text.replace(r'\div', '÷')
    text = text.replace(r'\pm', '±')
    text = text.replace(r'\neq', '≠')
    text = text.replace(r'\leq', '≤')
    text = text.replace(r'\le', '≤')
    text = text.replace(r'\geq', '≥')
    text = text.replace(r'\ge', '≥')
    text = text.replace(r'\approx', '≈')
    text = text.replace(r'\cdot', '·')
    text = text.replace(r'\dots', '…')
    text = text.replace(r'\square', '□')
    text = text.replace(r'\triangle', '△')
    text = text.replace(r'\pi', 'π')
    text = text.replace(r'\(', '')
    text = text.replace(r'\)', '')
    text = re.sub(r'\$([^$]+)\$', r'\1', text)
    return text

cleaned_count = 0
for t in threads:
    modified = False
    for p in t.get('posts', []):
        old_text = p.get('text', '')
        new_text = clean_latex(old_text)
        if new_text != old_text:
            p['text'] = new_text
            modified = True
    if 'source_insight' in t:
        for k in ['academic_quote', 'core_concept', 'qna']:
            if k in t['source_insight']:
                old_val = t['source_insight'][k]
                new_val = clean_latex(old_val)
                if new_val != old_val:
                    t['source_insight'][k] = new_val
                    modified = True
    if modified:
        cleaned_count += 1

with open(DB_PATH, 'w', encoding='utf-8') as f:
    json.dump(threads, f, ensure_ascii=False, indent=2)

print(f'Successfully updated threads 102, 103, 108 and cleaned LaTeX across {cleaned_count} threads in live DB!')
