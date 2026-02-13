# 매일묵상 프로젝트

이 폴더는 디딤교회 매일묵상 콘텐츠 생성 시스템입니다.

## 사용 가능한 스킬

### /weekly-devotion
매주 토요일에 다음 주 월~금 매일묵상 콘텐츠를 생성합니다.
- 성인 묵상 (워드프레스 + 카톡 A4)
- 청소년 QT (카톡 A4)
- 총 15개 파일 출력

### /insert-images
매일묵상 HTML에 이미지 삽입 + A4 HTML을 PNG로 자동 캡쳐합니다.

## 폴더 구조

```
매일묵상/
├── .claude/skills/
│   ├── weekly-devotion/
│   └── insert-images/
├── data/              # 묵상 데이터 저장소
├── output/            # 생성된 콘텐츠 출력
└── capture-a4.js      # A4 캡쳐 스크립트
```
