import React, {Component} from 'react'

class TOC extends Component{
  render(){
    var lists = [];
    var data=this.props.data;
    var i = 0;
    while(i < data.length){
      lists.push(
      <li key={data[i].id}>
        <a 
          href={"/content/"+data[i].id}
          onClick={function(e){
            this.props.onChangePage();
            e.preventDefault();
          }.bind(this)}>
          {data[i].title}
        </a>
      </li>); // key가 없어도 렌더링은 되지만 React 특성상 필요
      i=i+1;
    }
    return(
      <nav>
      <ul>
        {lists}
      </ul>
    </nav>
    );
  }
}

export default TOC;