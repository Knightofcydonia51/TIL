# DOM과 BOM



## BOM(Browser Object Model)

- 웹 브라우저 환경의 객체들의 집합을 표현한 모델을 BOM(Browser Object Model)이라고 한다.
- 브라우저 객체 모델이라고 번역할 수 있다. 좁게 보면 BOM에 해당하는 객체들의 집합을 말하기도 한다.
- window 객체가 이에 해당하며, BOM에 해당하는 객체들은 아래와 같다.

| 이름      | 설명                                  |
| --------- | ------------------------------------- |
| window    | 현재 브라우저 창 또는 탭의 모든 자원  |
| navigator | 브라우저 명과 버전정보를 나타냄       |
| document  | 현재 로드된 웹페이지                  |
| history   | 브라우저 히스토리에 기록된 웹페이지들 |
| screen    | 장치의 디스플레이 정보                |
| location  | 현재 페이지 url                       |

- 위 모두가 window의 하위 객체이므로 window.navigator와 같은 방식으로 접근이 가능하다.
- 또한, window가 브라우저에서 표현된 최상위의 객체이자 전역 객체이므로 자바스크립트 소스 내에서 선언한 모든 변수와 함수들은 window.function과 같이 접근이 가능하다.



## DOM(Document Object Model)

- DOM은 BOM의 하위 객체
- 문서(HTML, XML) 에 대한 모든 내용을 담고 있는 객체
- 텍스트 파일로 만들어진 문서를 브라우저가 이해할 수 있는 구조로 구성한 것
- HTML 요소 간의 부자 관계를 반영하여 모든 노드들을 **트리 구조**로 구성한 것
- 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 문서 구조, 스타일, 내용 등을 변경할 수 있게 도움
- 자바스크립트가 확장자가 다른 HTML, CSS 파일의 내용을 읽고 수정할 수 있는 이유가 바로 이것이다.



![](C:\Users\배태한\Desktop\work\02_mine\TIL\00_Documents\img\htmlExample.png)



![](C:\Users\배태한\Desktop\work\02_mine\TIL\00_Documents\img\htmlTree.png)

- document 노드가 최상위 노드가 되고, 밑으로 element 노드가 오며, 이어 text노드와 attribute 노드가 오는 계층적 구조를 이룬다.



### Document node(문서 노드)

- DOM Tree에서 최상위 루트 노드를 나타내며, document 객체를 가리킨다. HTML 문서 전체를 나타내는 노드라고 할 수 있다.



### Element node(요소 노드)

- 모든 HTML 요소(body, h2, div, li 등)이 요소 노드에 포함된다.
- 속성 노드를 가질 수 있는 유일한 노드이며 부모-자식 관계를 가지게 되기 때문에 계층적 구조를 이룬다.



### Attribute node(속성 노드)

- 요소 노드의 속성을 나타내는 노드이다.
- color, size와 같이 요소 노드의 속성을 표현할 수 있다.



### Text node(텍스트 노드)

- HTML 요소의 텍스트를 가리키는 객체이다.
- 문서의 정보를 표현한다. 
- 텍스트 요소는 요소 노드의 자식 노드이며 자식 노드를 가질 수 없는 노드라 리프 노드라고도 한다.
- 텍스트 노드에 접근하려면 먼저 부모 노드인 요소 노드에 접근해야 한다.



## JaveScript DOM  접근 및 수정 예시

```javascript
# div 생성
const exampleDiv = document.createElement('div')

# text 추가
exampleDiv.textContent = 'test!'

# html 문서에 추가
document.body.append(exampleDiv)
document.body.appendChild(exampleDiv)

# html 문서에서 제거
exampleDiv.remove();
document.body.removeChild(exampleDiv)
```



> https://www.codestates.com/blog/content/dom-javascript
>
> https://yung-developer.tistory.com/74