import sys
import re
import math

# 총 단어 수와 게임 수 변수 초기화
word_count = 0
bullshit_count = 0
unique_words = set()

try:
    while True:
        # 한 줄씩 입력을 받아 알파벳 문자만 남기고 대문자로 변환
        line = re.sub(r'[^a-zA-Z]', ' ', input()).upper()
        # 단어를 분리하여 처리
        for word in line.split():
            if word == "BULLSHIT":
                # "BULLSHIT"을 만나면 게임 종료 처리
                bullshit_count += 1
                word_count += len(unique_words)
                unique_words.clear()
            else:
                # 중복되지 않는 단어를 집합에 추가
                unique_words.add(word)
except EOFError:
    # 입력이 끝나면 종료
    pass

# 분모가 0인 경우 처리 (게임이 없을 경우)
if bullshit_count == 0:
    print("0 / 1")
else:
    # 최대공약수를 구해서 약분
    gcd_result = math.gcd(word_count, bullshit_count)
    print(f"{word_count // gcd_result} / {bullshit_count // gcd_result}")

