#!/usr/bin/env python3
"""
콜드 메일 자동화 시스템
Google Sheets에서 고객 리스트를 읽어 개인화된 이메일을 발송합니다.
"""

import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

# 환경변수 로드
load_dotenv()

GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")
GMAIL_ID = os.getenv("GMAIL_ID")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
SENDER_NAME = os.getenv("SENDER_NAME", "발신자")

# Google Sheets API 스코프
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly",
]


def get_email_template(company_name: str, representative_name: str) -> str:
    """개인화된 이메일 HTML 템플릿 생성"""
    return f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
            line-height: 1.8;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .greeting {{
            margin-bottom: 20px;
        }}
        .content {{
            margin-bottom: 30px;
        }}
        .signature {{
            border-top: 1px solid #e0e0e0;
            padding-top: 20px;
            margin-top: 30px;
        }}
        .signature-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            padding: 20px;
            color: white;
        }}
        .signature-name {{
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .signature-title {{
            font-size: 14px;
            opacity: 0.9;
            margin-bottom: 15px;
        }}
        .signature-info {{
            font-size: 13px;
            opacity: 0.85;
        }}
        .signature-info p {{
            margin: 3px 0;
        }}
    </style>
</head>
<body>
    <div class="greeting">
        <p>안녕하세요, <strong>{company_name}</strong> {representative_name} 대표님.</p>
    </div>

    <div class="content">
        <p>바쁘신 와중에 메일 드려 죄송합니다.</p>

        <p>저희는 기업의 비즈니스 성장을 돕는 솔루션을 제공하고 있습니다.</p>

        <p>{company_name}의 사업 현황을 살펴보고, 귀사에 도움이 될 수 있는 부분이 있을 것 같아 연락드렸습니다.</p>

        <p>짧게 10분 정도 통화가 가능하시다면, 구체적인 협업 방안을 말씀드리고 싶습니다.</p>

        <p>편하신 시간에 회신 부탁드립니다.</p>

        <p>감사합니다.</p>
    </div>

    <div class="signature">
        <div class="signature-card">
            <div class="signature-name">{SENDER_NAME}</div>
            <div class="signature-title">Business Development</div>
            <div class="signature-info">
                <p>Email: {GMAIL_ID}</p>
            </div>
        </div>
    </div>
</body>
</html>
"""


def connect_to_sheet():
    """Google Sheets에 연결하고 워크시트 반환"""
    # 서비스 계정 credentials.json이 있는 경우
    credentials_path = os.path.join(os.path.dirname(__file__), "credentials.json")

    if os.path.exists(credentials_path):
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        client = gspread.authorize(creds)
    else:
        # OAuth 인증 (처음 실행 시 브라우저에서 인증)
        client = gspread.oauth(scopes=SCOPES)

    # URL에서 시트 열기
    sheet = client.open_by_url(GOOGLE_SHEET_URL)
    worksheet = sheet.sheet1

    return worksheet


def apply_header_style(worksheet):
    """헤더 행에 스타일 적용"""
    # 헤더 확인 및 설정
    headers = worksheet.row_values(1)
    expected_headers = ["이메일", "회사명", "대표자명", "발송시간"]

    if not headers or headers != expected_headers:
        worksheet.update("A1:D1", [expected_headers])

    # 헤더 스타일 적용 (배경색, 굵게)
    worksheet.format("A1:D1", {
        "backgroundColor": {"red": 0.2, "green": 0.4, "blue": 0.8},
        "textFormat": {"bold": True, "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
        "horizontalAlignment": "CENTER",
    })

    print("헤더 스타일이 적용되었습니다.")


def send_email(to_email: str, company_name: str, representative_name: str) -> bool:
    """이메일 발송"""
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"[{company_name}] 비즈니스 협업 제안"
        msg["From"] = formataddr((SENDER_NAME, GMAIL_ID))
        msg["To"] = to_email

        html_content = get_email_template(company_name, representative_name)
        msg.attach(MIMEText(html_content, "html", "utf-8"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_ID, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_ID, to_email, msg.as_string())

        return True
    except Exception as e:
        print(f"이메일 발송 실패 ({to_email}): {e}")
        return False


def main():
    """메인 실행 함수"""
    print("=" * 50)
    print("콜드 메일 자동화 시스템 시작")
    print("=" * 50)

    # 환경변수 검증
    if not all([GOOGLE_SHEET_URL, GMAIL_ID, GMAIL_APP_PASSWORD]):
        print("오류: .env 파일에 필수 환경변수를 설정해주세요.")
        print("  - GOOGLE_SHEET_URL")
        print("  - GMAIL_ID")
        print("  - GMAIL_APP_PASSWORD")
        return

    # Google Sheets 연결
    print("\nGoogle Sheets 연결 중...")
    try:
        worksheet = connect_to_sheet()
        print("연결 성공!")
    except Exception as e:
        print(f"Google Sheets 연결 실패: {e}")
        return

    # 헤더 스타일 적용
    apply_header_style(worksheet)

    # 데이터 읽기 (2행부터)
    all_records = worksheet.get_all_values()

    if len(all_records) <= 1:
        print("\n발송할 데이터가 없습니다.")
        return

    sent_count = 0
    skipped_count = 0
    failed_count = 0

    print(f"\n총 {len(all_records) - 1}개의 데이터를 처리합니다.\n")

    for row_idx, row in enumerate(all_records[1:], start=2):
        if len(row) < 3:
            print(f"[행 {row_idx}] 데이터 부족, 건너뜀")
            continue

        email = row[0].strip()
        company_name = row[1].strip()
        representative_name = row[2].strip()
        sent_time = row[3].strip() if len(row) > 3 else ""

        # 발송시간이 있으면 이미 발송된 것이므로 건너뜀
        if sent_time:
            print(f"[행 {row_idx}] {company_name} - 이미 발송됨 ({sent_time}), 건너뜀")
            skipped_count += 1
            continue

        if not email or not company_name or not representative_name:
            print(f"[행 {row_idx}] 필수 정보 누락, 건너뜀")
            continue

        print(f"[행 {row_idx}] {company_name} ({representative_name}) - {email} 발송 중...", end=" ")

        if send_email(email, company_name, representative_name):
            # 발송 성공 시 시간 기록
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            worksheet.update_cell(row_idx, 4, current_time)
            print(f"성공!")
            sent_count += 1
        else:
            print(f"실패")
            failed_count += 1

    # 결과 요약
    print("\n" + "=" * 50)
    print("처리 완료!")
    print(f"  - 발송 성공: {sent_count}건")
    print(f"  - 건너뜀 (이미 발송): {skipped_count}건")
    print(f"  - 발송 실패: {failed_count}건")
    print("=" * 50)


if __name__ == "__main__":
    main()
