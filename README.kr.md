## 실행방법

먼저 git clone한 뒤 루트 폴더에 들어감. 그리고 나서 할일:

1. docker 다운로드
2. docker desktop 실행
3. 관리자 권한으로 cmd파일 연 뒤 dockerStart.bat 파일 실행
- 이 bat 파일은 관련 모델을 설치하고 모델을 이용할 수 있는 환경을 만들어줌.
4. 방화벽 권한 허용 (서버 실행)
5. 서버 실행(Starting Webserver) 메시지가 나올 때까지 기다리기
6. python main.py 실행
7. 결과 확인 후 Ctrl+C하여 종료
