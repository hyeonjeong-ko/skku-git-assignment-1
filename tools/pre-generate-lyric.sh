#!/bin/bash

FOLDER_GIT=.git
README_FILE=README.md

touch $README_FILE

git add $README_FILE && git commit -m "Making a new file called README.md"


echo "# Title : 솜사탕" >> $README_FILE
git add $README_FILE && git commit -m "타이틀을 커밋"

echo "![Cover img](mangboong.png)" >> $README_FILE
git add $README_FILE && git commit -m "커버 이미지를 커밋"

echo "### 나뭇가지에 실처럼" >> $README_FILE
git add $README_FILE && git commit -m "후반부 솜사탕 노래 첫줄"

echo "### 날아든 솜사탕" >> $README_FILE
git add $README_FILE && git commit -m "후반부 솜사탕 노래 두번째줄"

echo "### 하얀 눈처럼 희고도" >> $README_FILE
git add $README_FILE && git commit -m "후반부 솜사탕 노래 세번째줄"

echo "### 깨끗한 솜사탕" >> $README_FILE
git add $README_FILE && git commit -m "후반부 솜사탕 노래 네번째줄"

echo "### 엄마 손잡고 나들이 갈 때" >> $README_FILE
git add $README_FILE && git commit -m "후반부 솜사탕 노래 다섯번째줄"

echo "### 먹어본 솜사탕" >> $README_FILE
git add $README_FILE && git commit -m "후반부 솜사탕 노래 여섯번째줄"

echo "### 훅훅 불면은 구멍이 뚫리는" >> $README_FILE
git add $README_FILE && git commit -m "후반부 솜사탕 노래 일곱번째줄"

echo "### 커다란 솜사탕" >> $README_FILE
git add $README_FILE && git commit -m "후반부 솜사탕 노래 마지막 줄"






