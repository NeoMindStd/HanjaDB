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
 
## 라이센스
본 소프트웨어는 [MIT 오픈소스 라이센스](/LICENSE)가 적용됩니다

[입력으로 사용한 데이터](/input/resource)는 hanjadic을 원본으로 하는 [데이터 배포본](http://www.happycgi.com/13322)을 사용합니다. 

hanjadic 소프트웨어는 GPL 또는 그 파생 라이센스를 적용하는 것으로 추정되나, 사전 자체에 대한 저작권은 [한자 사전에 대한 저작권 판례](http://www.copyright.or.kr/information-materials/law-precedent/view.do?brdctsno=10014&list.do?pageIndex=26&brdctsstatecode=&brdclasscode=&servicecode=06&nationcode=&searchText=&searchTarget=ALL)에 따라 적용되지 않는것으로 간주, 해당 프로젝트에는 MIT 라이센스를 사용했습니다.

HanjaDB 프로젝트의 소유자 및 기여자는 이 프로젝트의 입력물이나 결과물을 이용한 라이센스에 대해 법적 조언을 구하지 않았으며, 어떠한 책임도 지지 않음을 명시합니다.