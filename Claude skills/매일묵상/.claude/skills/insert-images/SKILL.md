---
name: insert-images
description: 생성된 매일묵상 HTML 파일에 이미지를 삽입합니다. [이미지_URL] 플레이스홀더를 실제 이미지 경로로 교체합니다.
disable-model-invocation: true
argument-hint: [주차번호] [이미지소스]
allowed-tools: Read, Write, Bash
---

# 묵상 이미지 삽입

## 실행
```
/insert-images 7 ~/images/week-7/
/insert-images 7 https://example.com/images/
```

## 인수
- **$0**: 주차 번호 (1~52)
- **$1**: 이미지 소스 (로컬 폴더 경로 또는 URL 접두사)

## 작업 대상
- 대상 폴더: `../../output/week-{N}_YYYY-MM-DD/`
- 소스: `html-original/` 폴더의 HTML 파일들
- 결과: `html-with-images/` 폴더에 이미지 삽입된 HTML 저장

## 이미지 파일 규칙
- 파일명: `mon`, `tue`, `wed`, `thu`, `fri`
- 확장자: `.jpg`, `.jpeg`, `.png`, `.webp` 중 자동 인식
- 로컬 경로 예: `~/images/week-7/mon.jpg`
- URL 예: `https://example.com/images/mon.jpg`

## 작업 순서

### 1단계: 이미지 소스 확인
- 로컬 경로인 경우: 폴더 내 mon~fri 이미지 파일 존재 확인
- URL인 경우: URL 패턴 검증

### 2단계: 대상 HTML 파일 확인
```
output/week-{N}_YYYY-MM-DD/
└── html-original/     ← mon~fri × 3가지 형식 = 15개 HTML
    ├── mon-adult-wordpress.html
    ├── mon-adult-a4.html
    ├── mon-youth-a4.html
    └── ... (총 15개)
```
총 15개 파일에서 `[이미지_URL]` 플레이스홀더가 있는지 확인

### 3단계: 이미지 경로 교체
각 요일(mon~fri)에 해당하는 이미지를 매칭하여 교체:

**로컬 이미지인 경우:**
- 이미지를 `images/` 폴더로 복사
- HTML 파일을 `html-with-images/` 폴더에 저장
- 상대 경로 `../images/mon.png` 형식으로 삽입

**URL인 경우:**
- HTML 파일을 `html-with-images/` 폴더에 저장
- URL 직접 삽입

### 4단계: A4 HTML 자동 캡쳐
- `html-with-images/` 폴더의 A4 HTML 파일들을 PNG로 캡쳐
- 캡쳐 결과를 `captured/` 폴더에 저장
- capture-a4.js 스크립트 사용 (Puppeteer)

### 5단계: 결과 보고
```
✅ 이미지 삽입 및 캡쳐 완료 (week-7_2026-02-16)
├── html-with-images/: 15개 HTML 파일 생성
├── images/: 5개 이미지 복사됨
└── captured/: 10개 PNG 캡쳐됨 (성인/청소년 A4)
이미지 소스: ~/images/week-7/
```

## 교체 대상
HTML 파일 내 `[이미지_URL]`이 포함된 모든 `<img>` 태그의 `src` 속성을 교체한다.

## 주의사항
- 이미 이미지가 삽입된 파일(플레이스홀더가 없는 파일)은 건너뛴다
- 교체 전 원본 파일을 변경하므로, 필요 시 사전 백업을 권장한다
- 이미지 파일이 누락된 요일은 경고를 표시하고 해당 파일만 건너뛴다
