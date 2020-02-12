# HanjaDB
한글 한자 DB

## 사용법
**parser.py는 다음 모듈에 의존성을 갖습니다:**
 - pyyaml
 - hanja
 
**pip install [library name] 명령어로 위의 두 모듈을 install 한 뒤 실행해주십시오**

input 디렉토리 하위에 resource 파일이 있는지 확인 후 parser.py를 실행하시면 output/result.json 파일이 생성됩니다.

[결과물을 csv/mysql/sqlite 등으로 변환을 원하시면 이곳을 방문해주세요](https://numidian.io/convert/json/to/sqlite)

*결과물이 생성되지 않는다면, 파일 읽기/쓰기 권한이 있는지 확인해주세요.*

## 구현 언어 및 환경
 - Language: Python 3.6.5
 - Editor: Python IDLE
 
## [라이센스는 이곳을 참조해주세요](/LICENSE)