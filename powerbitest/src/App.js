import logo from './logo.svg';
import './App.css';
import PowerBIReport from './components/powerBIReport';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Power Bi Test Service.
        </p>
        <PowerBIReport />
      </header>
    </div>
  );
}

export default App;
