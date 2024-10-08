# 2048 Game Bot

Normal Game: Run game.py using Python (command: python3 game.py) <br>
AI Mode: Run main.py using Python (command: python3 main.py)

### Algorithm

Four heuristics are used:

- Big: The higher the sum of the numbers on the board, the higher the score assigned to that board.
- Emptiness: The more empty tiles on the board, the higher the score assigned to that board.
- Monotonicity: The board scores higher if the tiles with large numbers are in the corners and arranged in descending order relative to those numbers.
- Smoothness: The smaller the difference between the numbers on adjacent tiles, the higher the score assigned to that board.
<br>

---

<br>

# 2048 게임을 수행 하는 봇

일반 게임 : 파이썬으로 game.py 실행 (python3 game.py) <br>
ai 모드 : 파이썬으로 main.py 실행 (python3 main.py)

### 알고리즘
4 가지 휴리스틱 사용
- big : 보드 위의 숫자 합이 클 수록 해당 보드의 스코어를 높게 평가
- emptyness : 보드에 빈 칸이 많을 수록 해당 보드의 스코어를 높게 평가
- monotonicity : 큰 숫자를 나타내는 타일은 구석에, 해당 숫자를 기준으로 내림차순으로 정리되어 있을 수록 높은 스코어
- smoothness : 주변 타일과의 숫자 차이가 작을 수록 높은 스코어의 보드
