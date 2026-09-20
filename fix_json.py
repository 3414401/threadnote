#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('uploads/user_threads.json', 'r', encoding='utf-8') as f:
    s = f.read()

res = []
i = 0
n = len(s)
while i < n:
    if s[i] == '\\':
        if i + 1 < n:
            next_ch = s[i+1]
            if next_ch in '"\\/bfnrt':
                res.append('\\' + next_ch)
                i += 2
                continue
            elif next_ch == 'u' and i + 5 < n and all(c in '0123456789abcdefABCDEF' for c in s[i+2:i+6]):
                res.append(s[i:i+6])
                i += 6
                continue
            else:
                # Invalid escape, drop the backslash!
                i += 1
                continue
        else:
            i += 1
            continue
    else:
        res.append(s[i])
        i += 1

fixed = ''.join(res)
with open('uploads/user_threads.json', 'w', encoding='utf-8') as f:
    f.write(fixed)

import json
with open('uploads/user_threads.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('SUCCESS! Valid JSON with threads count:', len(data))
