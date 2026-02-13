# 콜드 메일 자동화 시스템 구현 계획

## 목표
Google Spreadsheets에 정리된 고객 리스트(이메일, 회사명, 대표자명)를 읽어와 개인화된 이메일을 자동으로 발송합니다. 중복 발송을 방지하고, macOS에서 원클릭으로 실행 가능한 환경을 구축합니다.

## User Review Required
> [!IMPORTANT]
> **보안 주의**: 앱 비밀번호나 API 키는 절대 코드에 포함시키지 않고 `.env` 파일로 관리합니다. Google 계정의 "앱 비밀번호" 생성이 필요합니다.

## Proposed Changes

### Configuration
#### [NEW] .env
민감한 정보를 관리하기 위한 설정 파일입니다.
- `GOOGLE_SHEET_URL`: 구글 스프레드 시트 주소
- `GMAIL_ID`: 발송자 GMAIL 계정
- `GMAIL_APP_PASSWORD`: GMAIL 앱 비밀번호
- `SENDER_NAME`: 이메일에 표시될 발신자 이름 (이메일 주소 숨김)

### Core Logic
#### [NEW] main.py
전체 로직을 담당하는 Python 스크립트입니다.
1. **Google Sheets 연결**: `gspread` 라이브러리 사용.
2. **헤더 스타일링**: 시트 최상단(1행)에 배경색, 굵게 등 스타일 적용.
3. **데이터 처리**:
   - 컬럼 순서: 이메일 | 회사명 | 대표자명 | 발송시간
   - 2행부터 순회하며 '발송시간' 컬럼이 비어있는지 확인.
4. **이메일 발송**:
   - `smtplib` 활용.
   - **발신자명 표시**: `email.utils.formataddr` 사용하여 `이름 <email>` 포맷 적용 (수신자에게는 이름만 강조됨).
   - **템플릿**: 회사명, 대표자명을 삽입한 HTML 본문 + 명함 스타일 서명.
5. **결과 기록**: 발송 성공 시 현재 시간을 '발송시간' 컬럼에 기록.

#### [NEW] email_template.html (또는 코드 내 포함)
신뢰감을 주는 비즈니스 톤의 템플릿과 CSS로 디자인된 이메일 서명.

### Automation
#### [NEW] run_mailer.command
macOS에서 더블 클릭으로 실행할 수 있는 쉘 스크립트입니다.
- 터미널을 열지 않고 백그라운드나 별도 창에서 `python main.py`를 실행하도록 설정합니다.
- 실행 권한(`chmod +x`)이 부여됩니다.

## Verification Plan

### Automated Logic Checks
- 시트에 이미 '발송시간'이 있는 행은 건너뛰는지 로그로 확인.
- 헤더 스타일이 적용되었는지 시각적 확인.

### Manual Verification
1. `.env`에 테스트 계정 정보 입력.
2. `run_mailer.command` 더블 클릭 실행.
3. 테스트 수신함에서:
   - 발신자명이 설정한 이름으로만 뜨는지 확인.
   - 회사명/대표자명이 올바르게 치환되었는지 확인.
   - 서명이 제대로 렌더링되는지 확인.
4. 구글 시트에서 발송 시간이 갱신되었는지 확인.
