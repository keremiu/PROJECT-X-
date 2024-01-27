// SearchBar.js
import React, { useState } from 'react';

function SearchBar({ data }) {
  const [value, setValue] = useState('');

  const onChange = (event) => {
    setValue(event.target.value);
  };

  const onSearch = (searchTerm) => {
    setValue(searchTerm);
    console.log("search ", searchTerm);
  };

  return (
    <div className="search-container">
      <div className="search-inner">
        <input type="text" value={value} onChange={onChange}></input>
      </div>
      <div className='dropdown'>
        {data.filter(item => {
          const searchTerm = value.toLowerCase();
          const itemKey = item.key.toLowerCase();
          return searchTerm && itemKey.includes(searchTerm) && searchTerm !== itemKey;
        }).map((item) => (
          <div onClick={() => onSearch(item.key)}
            className='dropdown-row' 
            key={item.key}> 
            {item.key}
          </div>
        ))} 
      </div>
    </div>
  );
}

export default SearchBar;
