# 디딤수요기도회 기도제목 - 설치 가이드 (Mac + Cursor IDE)

## 1. 폴더 배치

zip 압축 해제 후 `수요기도회-claude-code/` 폴더를 아래 경로에 이동하고
폴더명을 `수요기도회`로 변경합니다:

```
~/Desktop/ai works/claude skills/수요기도회/
```

## 2. 초기 설치 (최초 1회만)

터미널을 열고 프로젝트 폴더로 이동 후 `npm install` 실행:

```bash
cd ~/Desktop/ai\ works/claude\ skills/수요기도회
npm install
```

이것만 하면 끝입니다. Puppeteer가 Chromium 브라우저를 자동으로 다운로드합니다.
(brew 설치 불필요, 시스템 설정 변경 없음)

### 확인사항
- **Node.js**: `node --version` (없으면 https://nodejs.org 에서 설치)
- **Python 3**: `python3 --version` (Mac에 기본 포함)

## 3. Cursor IDE에서 사용하기

### 방법 1: Cursor 터미널에서 Claude Code 실행
1. Cursor에서 `수요기도회` 폴더를 열기 (File → Open Folder)
2. 터미널 열기 (Ctrl+`)
3. Claude Code 실행:
   ```bash
   claude
   ```
4. 슬래시 커맨드 사용:
   ```
   /기도제목 3월 2주차
   /기도제목-전체 8월
   ```

### 방법 2: 자연어로 요청
```
8월 둘째 주 기도제목 만들어줘
```
→ Claude가 prayer-doc 스킬을 자동 인식

### 방법 3: Python 스크립트 직접 실행 (Claude 없이)
```bash
python3 .claude/skills/prayer-doc/scripts/run_pipeline.py \
  data/26년_수요기도회_-_26년_수요기도회.csv 3 2 \
  --base-dir .
```

## 4. CSV 데이터 업데이트

새 데이터가 필요하면:
1. 구글 시트 → 파일 → 다운로드 → 쉼표로 구분된 값(.csv)
2. 다운로드된 CSV를 `data/` 폴더에 복사

## 5. 출력 파일 위치

```
수요기도회/output/
├── 3월/
│   └── 2주차/
│       ├── 기도제목_3월_2주차.html
│       └── 기도제목_3월_2주차.png
├── 8월/
│   ├── 1주차/
│   ├── 2주차/
│   └── ...
└── ...
```

## 6. 문제 해결

| 문제 | 해결 |
|------|------|
| "Puppeteer not installed" | 프로젝트 폴더에서 `npm install` 실행 |
| "node: command not found" | https://nodejs.org 에서 Node.js 설치 |
| 한글 깨짐 | Mac에는 한글 폰트가 기본 포함이라 보통 발생 안함 |
| Claude가 스킬 인식 못함 | `수요기도회/` 폴더에서 `claude` 실행했는지 확인 |
| PNG 생성 안됨 | `node -e "require('puppeteer')"` 로 설치 확인 |
