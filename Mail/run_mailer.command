#!/bin/bash
# 콜드 메일 자동화 실행 스크립트
# 이 파일을 더블클릭하면 메일 발송이 시작됩니다.

# 스크립트가 위치한 디렉토리로 이동
cd "$(dirname "$0")"

echo "======================================"
echo "  콜드 메일 자동화 시스템"
echo "======================================"
echo ""

# Python 가상환경이 있으면 활성화
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "가상환경 활성화됨"
fi

# 의존성 확인 및 설치
if ! python3 -c "import gspread" 2>/dev/null; then
    echo "필요한 패키지를 설치합니다..."
    pip3 install -r requirements.txt
fi

# 메인 스크립트 실행
python3 main.py

echo ""
echo "아무 키나 누르면 종료됩니다..."
read -n 1
