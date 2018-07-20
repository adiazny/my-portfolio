import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
  {
    'title': "A Serverless Portforlio",
    'href' : "https://example.com",
    'desc' : "A Serverless Portfolio using AWS technology",
    'image' : {
      'desc' : "example screenshot of a project inolving code",
      'src' : "images/example1.png",
      'comment' : ""
    }
  },
  {
    'title': "Work Example 2 - Coming Soon",
    'href' : "https://example.com",
    'desc' : "A Serverless Portfolio using AWS technology",
    'image' : {
      'desc' : "example screenshot of a project inolving code",
      'src' : "images/example2.png",
      'comment' : ""
    }
  }
]

ReactDOM.render(<ExampleWork work={myWork} />, document.getElementById('example-work'));
