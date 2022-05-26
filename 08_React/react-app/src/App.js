
import "./App.css";
import { Component } from "react";
import TOC from "./components/TOC"
import Content from "./components/Content"
import Subject from "./components/Subject"

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
    // console.log("App render===========");
    var _title, _desc = null;
    if(this.state.mode === 'welcome'){
      _title =  this.state.welcome.title;
      _desc =  this.state.welcome.desc; 
    } else if(this.state.mode === 'read'){
      _title =  this.state.contents[0].title;
      _desc =  this.state.contents[0].desc; 
    }
    console.log('render', this)
    return (
    <div className="App">
      <Subject 
        title={this.state.subject.title}
        sub={this.state.subject.sub}
        onChangePage={function(){
          alert('hi!');
        }.bind(this)}>
      </Subject>
       {/* <header>
      
      <h1><a href="/" onClick={function(e){
        // console.log("THIS==========", this)
        console.log('event in', this)
        e.preventDefault()
        return;
       this.setState({
         mode:'welcome' // setState 함수로 현재 컴포넌트의 state값을 변경
       });
      }}>{this.state.subject.title}</a></h1>
      {this.state.subject.sub}
    </header> */}
      <TOC 
      onChangePage={function(){
          alert('bye!');
          this.setState({
            mode:'welcome'
          });
      }.bind(this)}
      data={this.state.contents}></TOC>
      <Content title={_title} desc={_desc}></Content>
      </div>);
  }
}

export default App;
 