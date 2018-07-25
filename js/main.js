import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
  {
    'title': "A Serverless Portforlio",
    'href' : "https://s3.amazonaws.com/portfolio.alandiaz.com/AWS-Serverless-Architecture.jpg",
    'desc' : "My portfolio showcases how I host and deploy serverless applications with AWS. I used source control with git and github. I secured and controlled access to my AWS account with IAM. I managed DNS for my website with Route 53. I stored objects in the cloud with S3 and distributed them with Cloud Front. I also used AWS CI/CD technologies like Code Build and Code Pipeline to help build my web application. I used Functions as a Service with AWS Lambda to deploy my portfolio. I also created a frontend application with React. HTML determines my page structures while the look and feel is determined by CSS. I added interactivity with JavaScript, specifically with the React library. I used cross browser compatibility with Babel and bundling and asset management using the Webpack tool. I also manage my portfolio’s packages with NPM. I test with Jest, as well as with Chai and Mocha. ",
    'image' : {
      'desc' : "example screenshot of a project inolving code",
      'src' : "images/example1.png",
      'comment' : ""
    }
  },
  {
    'title': "Work Example 2 - Coming Soon",
    'href' : "https://example.com",
    'desc' : "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    'image' : {
      'desc' : "example screenshot of a project inolving code",
      'src' : "images/example2.png",
      'comment' : ""
    }
  }
]

ReactDOM.render(<ExampleWork work={myWork} />, document.getElementById('example-work'));
