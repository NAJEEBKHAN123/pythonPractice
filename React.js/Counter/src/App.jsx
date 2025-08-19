import React, { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
 
  const handleIncrement = () =>{
    setCount(count + 1)
  }

  const handleDecrement = () =>{
     setCount(count - 1)
  }


  
 
  return (
    <div>
      <button onClick={handleIncrement}>Increment</button>
      <h1>{count}</h1>
      <button onClick={handleDecrement} disabled={count === 0}>Decrement</button>
      <button onClick={ () => setCount(0)}>Reset</button>
    </div>
  )
}

export default App