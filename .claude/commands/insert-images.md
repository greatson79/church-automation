---
description: 매일묵상 HTML에 이미지 삽입 + A4 HTML을 PNG로 자동 캡쳐까지 한번에 실행합니다.
allowed-tools: Read, Write, Bash
---

"Claude skills/insert-images/SKILL.md" 파일을 읽고 그 안의 지시사항에 따라 이미지를 삽입하세요.

인수: $ARGUMENTS
(첫 번째 인수: 주차 번호, 두 번째 인수: 이미지 소스 경로 또는 URL)

대상 HTML 파일 위치: "Claude skills/weekly-devotion/output/week-{주차번호}/"
파일명 패턴: {요일}-adult-wordpress.html, {요일}-adult-a4.html, {요일}-youth-a4.html
(요일: mon, tue, wed, thu, fri)

## 이미지 삽입 완료 후 자동 실행

이미지 삽입이 끝나면, 아래 명령을 실행하여 A4 HTML을 PNG로 캡쳐하세요:

```
node "Claude skills/capture-a4.js" {주차번호}
```

캡쳐 결과는 `Claude skills/output/week{주차번호}_image/captured/`에 저장됩니다.

최종 결과를 아래 형식으로 보고하세요:
```
✅ 이미지 삽입 + PNG 캡쳐 완료 (week-{N})
├── 이미지 삽입: {n}/15 파일 교체됨
├── PNG 캡쳐: {n}/10 파일 생성됨
└── 저장 위치: Claude skills/output/week{N}_image/captured/
```
