# Claude Skills - 주님의교회 자동화 프로젝트

이 폴더는 주님의교회와 디딤교회의 주간 콘텐츠를 자동 생성하는 Claude Code 스킬 모음입니다.

## 프로젝트 구조

```
Claude skills/
├── CLAUDE.md              ← 이 파일
├── .claude/
│   └── settings.local.json
├── 매일묵상/              ← 주님의교회 매일묵상 콘텐츠
│   ├── CLAUDE.md
│   ├── .claude/skills/
│   │   ├── weekly-devotion/
│   │   └── insert-images/
│   ├── data/
│   ├── output/
│   └── capture-a4.js
└── 수요기도회/            ← 디딤교회 수요기도회 기도제목
    ├── CLAUDE.md
    ├── .claude/
    │   ├── skills/prayer-doc/
    │   └── commands/
    │       ├── 기도제목.md
    │       └── 기도제목-전체.md
    ├── data/
    ├── output/
    └── assets/
```

## 사용 방법

각 프로젝트는 독립적으로 실행됩니다.

### 매일묵상
- 폴더: `매일묵상/`
- 스킬: `/weekly-devotion`, `/insert-images`
- 자세한 내용은 `매일묵상/CLAUDE.md` 참조

### 수요기도회
- 폴더: `수요기도회/`
- 명령어: `/기도제목`, `/기도제목-전체`
- 자세한 내용은 `수요기도회/CLAUDE.md` 참조

## 실행 환경
- Node.js 18+
- Puppeteer (A4 캡쳐용)
- 각 프로젝트 폴더에서 독립적으로 npm 패키지 관리
