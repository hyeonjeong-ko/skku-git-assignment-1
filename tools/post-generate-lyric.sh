#!/bin/bash

FOLDER_GIT = .git
README_FILE = 2nd-assignment.md

git checkout sc-second-branch

echo "나뭇가지에 실처럼" >> $README_FILE
git add $README_FILE && git commit -m "강성철이 솜사탕 후반부 첫줄커밋"

echo "날아든 솜사탕" >> $README_FILE
git add $README_FILE && git commit -m "강성철이 솜사탕 후반부 두번째줄"

echo "하얀 눈처럼 희고도" >> $README_FILE
git add $README_FILE && git commit -m "강성철이 솜사탕 후반부 세번째줄"

echo "깨끗한 솜사탕" >> $README_FILE
git add $README_FILE && git commit -m "강성철이 솜사탕 후반부 네번째줄"

echo "엄마 손잡고 나들이 갈 때" >> $README_FILE
git add $README_FILE && git commit -m "강성철이 솜사탕 후반부 다섯번째줄"

echo "먹어본 솜사탕" >> $README_FILE
git add $README_FILE && git commit -m "강성철이 솜사탕 후반부 여섯번째줄"

echo "훅훅 불면은 구멍이 뚫리는" >> $README_FILE
git add $README_FILE && git commit -m "강성철이 솜사탕 후반부 일곱번째줄"

echo "커다란 솜사탕" >> $README_FILE
git add $README_FILE && git commit -m "강성철이 솜사탕 후반부 마지막줄"

