import './App.css';
import { useState } from "react"

var categories = require("./data/categories.json");

function App() {
  const [value, setValue] = useState('');

  const onChange = (event) => {
    setValue(event.target.value);
  }

  const onSearch = (searchTerm) => {
    setValue(searchTerm);
    console.log("search ", searchTerm);
  }
  
  return (
    <div className="App">
      <h1>Category</h1>
      <div className="search-container">
        <div className="search-inner">
          <input type="text" value={value} onChange={onChange}></input>

        </div>
        <div className='dropdown'>
          {categories.filter(item => {
            const searchTerm = value.toLowerCase();
            const cat = item.key.toLowerCase();

            return searchTerm && cat.includes(searchTerm) && searchTerm !== cat
          }).map((item) => (
          <div onClick={() => onSearch(item.key)}
          className='dropdown-row' 
          key={item.key}> 
          {item.key}</div>
          ))} 
        </div>
      </div>
    </div>
  );
}

export default App;
