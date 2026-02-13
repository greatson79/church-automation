# 디딤수요기도회 기도제목 자동 생성 프로젝트

## 프로젝트 개요
디딤교회 수요기도회 기도제목을 A4 인쇄용 문서(HTML → PNG)로 자동 생성하는 프로젝트.

## 핵심 워크플로우
1. CSV 데이터에서 특정 월/주차의 기도제목 추출
2. 교회 로고가 포함된 A4 HTML 문서 생성
3. PNG로 캡처하여 인쇄용 파일 제공

## 주요 명령어
- `/기도제목` — 특정 월/주차 기도제목 문서 생성 (예: `/기도제목 3월 2주차`)
- `/기도제목-전체` — 특정 월 전체 주차 일괄 생성 (예: `/기도제목-전체 8월`)

## 파일 구조
```
수요기도회/
├── CLAUDE.md              ← 이 파일 (프로젝트 컨텍스트)
├── .claude/
│   ├── skills/
│   │   └── prayer-doc/    ← 기도제목 문서 생성 스킬
│   │       ├── SKILL.md
│   │       └── scripts/
│   └── commands/
│       ├── 기도제목.md     ← /기도제목 슬래시 커맨드
│       └── 기도제목-전체.md ← /기도제목-전체 슬래시 커맨드
├── assets/
│   └── logo.png           ← 디딤교회 로고
├── data/                  ← CSV 데이터 파일 보관
└── output/                ← 생성된 문서 (월/주차별 정리)
```

## 실행 환경 요구사항
- Python 3.10+
- Node.js 18+ (Puppeteer 실행용)
- 초기 설치: 프로젝트 루트에서 `npm install` (Puppeteer + Chromium 자동 설치)
- CSV 파일은 `data/` 폴더에 저장

## 데이터 소스
- 구글 시트: https://docs.google.com/spreadsheets/d/1vnI4uePp_JtStImDDanxqhs5cEp0wgzQSfEOX6wah-U/
- CSV로 내보내기 후 `data/` 폴더에 저장하여 사용
