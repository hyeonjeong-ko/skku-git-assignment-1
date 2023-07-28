markdown_file="2nd-assignment.md"

# 타이틀,cover 추가
echo -e "타이틀\n" > "$markdown_file"
echo -e "![Cover](jk.jpg)\n" >> "$markdown_file"

echo "가사입력"

# 가사 전반부 입력 받아서 마크다운 파일에 추가,커밋
line_number=1
while IFS= read -r line
do
  echo "$line" >> "$markdown_file"
  git add "$markdown_file"
  git commit -m "$line_number번째 솜사탕 노래 줄"
  ((line_number++))
done

echo "가사 입력 및 작업 수행 종료"
