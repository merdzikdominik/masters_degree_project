// import React from 'react'

// const App = () => {
//     return <div>
//         Hello world
//     </div>
// }

// export default App

import React, { Component } from "react"
import { render } from "react-dom"
import classes from './App.module.scss'

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className={classes['main']}>
        Hello world
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);