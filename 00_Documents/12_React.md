# React



## 1. 설치 및 환경설정

```bash
# node js 설치
https://nodejs.org/ko/

# 설치 완료 후 cmd 창에서 설치 확인
node -v
npm -v

# React 설치하기 (글로벌 옵션으로)
npm install -g create-react-app

# 설치 확인
create-react-app -V
```



## 2. 프로젝트 생성

```
# 프로젝트 생성을 원하는 디렉토리에서
create-react-app .
```



## 3. 실행

```
npm run start
```



## 4. 빌드 및 배포

- 빌드시 파일구성 및 코드가 달라지는 이유는 실제 프로덕션 환경에서 사용되는 앱을 만들기 위해서 개발 편의를 위해 있던 파일들, 공백 등을 제거하기 떄문이다.
- 이 과정에서 용량 역시 감소한다. (확실하지 않지만 아마 브라우저에서 실행시 걸리는 시간 또한 단축될 것으로 예상됨)

```
# 빌드파일 생성
npm run build

# npm에서 사용할 수 있는 serve 웹서버 설치
npm install -g serve

# 생성한 빌드파일을 document root로 하여 serve에서 앱 실행
npm serve -s build
```



## 5. State

- React에서는 props 또는 state가 수정되면 해당되는 컴포넌트의 render() 함수가 다시 호출되고, render 함수에 포함된 하위 컴포넌트들의 render도 새로 호출된다. 즉 화면이 다시 그려진다.

```react
# App.js
class App extends Component{
    constructor(props){ // 컴포넌트 렌더링(render함수) 보다 먼저 실행되면서 그 컴포넌트를 초기화시켜주고 싶은 코드는 constructor 안에 작성한다.
        super(props); // 이 부분은 하위 컴포넌트에 값을 전달하고자할때 원칙적으로 선언해준다고 이해하면 된다.
        this.state= {
            subject:{title:'WEB', sub:'World Wide Web!'}
        }
    }
      render() {
    return (
    <div className="App">
      <Subject title="WEB" sub="world wide web!"></Subject>
      <TOC></TOC>
      <Content title="HTML" desc="HTML is HyperText Markup Language."></Content>
      </div>);
  }
}
```



## 5-2. render 함수 내에서 state를 변경하기

```react
  render() {
    console.log("App render===========");
    var _title, _desc = null;
    if(this.state.mode === 'welcome'){
      _title =  this.state.welcome.title;
      _desc =  this.state.welcome.desc; 
    } else if(this.state.mode === 'read'){
      _title =  this.state.contents[0].title;
      _desc =  this.state.contents[0].desc; 
    }
    
    return (
    <div className="App">
      {/* <Subject 
        title={this.state.subject.title}
        sub={this.state.subject.sub}>
      </Subject> */}
       <header>
      <h1><a href="/" onClick={function(e){
        e.preventDefault()
       this.state.mode = 'welcome' // 여기서는 상위 state를 참조할 수 없음. this는 undefined             
       // setState를 통해 this.state.mode의 값을 변경한다.
       this.setState({
         mode:'welcome'
       });
      // this가 undefined일때는 함수의 끝에 bind(this)를 넣어 component 자체를 this에 맵핑시킬 수 있다. 하지만 setState가 없다면 (추측)값이 변경되도 위의 if 분기가 먼저 실행되기 때문에 랜더링 내용이 바뀌지 않는 것 같다. 아마 setState가 코드에 포함되면 그 부분을 먼저 바라보는듯?
      }.bind(this)}>{this.state.subject.title}</a></h1>
      {this.state.subject.sub}
    </header>
      <TOC data={this.state.contents}></TOC>
      <Content title={_title} desc={_desc}></Content>
      </div>);
  }
```



## 6. Event

```react
# App.js
class App extends Component {
  constructor(props){ // 컴포넌트 렌더링(render함수) 보다 먼저 실행되면서 그 컴포넌트를 초기화시켜주고 싶은 코드는 constructor 안에 작성한다.
    super(props); // 이 부분은 하위 컴포넌트에 값을 전달하고자할때 원칙적으로 선언해준다고 이해하면 된다.
    this.state= {  
      mode : 'read',
      subject:{title:'WEB', sub:'World Wide Web!'},
      welcome:{title:'Welcome', desc:'Hello, React!!'},
      contents:[
        {id:1, title:'HTML', desc: 'HTML is HyperText ...'},
        {id:2, title:'CSS', desc: 'CSS is for design ...'},
        {id:3, title:'JavaScript', desc: 'JavaScript is for interactive ...'}
      ]
  }
  }
  render() {
    console.log("App render===========");
    var _title, _desc = null;
    // 이벤트 분기 처리
    if(this.state.mode === 'welcome'){
      _title =  this.state.welcome.title;
      _desc =  this.state.welcome.desc; 
    } else if(this.state.mode === 'read'){
      _title =  this.state.contents[0].title;
      _desc =  this.state.contents[0].desc; 
    }
    return (
    <div className="App">
      {/* <Subject 
        title={this.state.subject.title}
        sub={this.state.subject.sub}>
      </Subject> */}
       <header>
      <h1><a href="/" onClick={function(e){
        console.log(e);
        e.preventDefault(); // 이 코드가 속한 태그의 기본 기능을 비활성화함. (a태그이기 때문에 링크 정지)
        debugger; // 브라우저에서 코드 실행시 코드를 잠시 멈추고 디버깅을 지원함.
      }}>{this.state.subject.title}</a></h1>
      {this.state.subject.sub}
    </header>
      <TOC data={this.state.contents}></TOC>
      <Content title={_title} desc={_desc}></Content>
      </div>);
  }
}
```



## 7. function

```react
# App.js
<Subject 
        title={this.state.subject.title}
        sub={this.state.subject.sub}
        onChangePage={function(){
          alert('hi!');
        }.bind(this)}>
      </Subject>

# Subject.js
class Subject extends Component {
  render(){
    return(
      <header>
      <h1><a href="/" onClick={function(e){
        e.preventDefault();
        this.props.onChangePage();
      }.bind(this)}>{this.props.title}</a></h1>
      {this.props.sub}
    </header>
    )
  }
}

export default Subject;   
```

