// App.js
import './App.css';
import SearchBar from './SearchBar';
import categories from "./data/categories.json";
import ordering from "./data/ordering.json";
import period from "./data/period.json";
import tags from "./data/tags.json";

// Diğer JSON dosyalarını da burada içe aktarın

function App() {
  return (
    <div className="App">
      <h1>Category Search</h1>
      <SearchBar data={categories} />

      <h1>Tags Search</h1>
      <SearchBar data={tags} />

      <h1>Ordering Search</h1>
      <SearchBar data={ordering} />

      <h1>Period Search</h1>
      <SearchBar data={period} />

      {/* Diğer JSON dosyaları için SearchBar bileşenlerini burada ekleyin */}
    </div>
  );
}

export default App;
