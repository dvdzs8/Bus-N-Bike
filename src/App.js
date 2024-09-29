
import './App.css';
import Header from './components/Header';
import Maps from './components/Maps';
import { useState} from 'react';
import FileUpload from './components/FileUpload';

function App() {

  const[isMapVisible, setIsMapVisible] = useState(false);

  const toggleMapVisibility = () => {
    setIsMapVisible(prevState => !prevState);
  };

  return (
    <div className="App">
      <Header />

      
      
      <header className="App-header">

      {isMapVisible && <Maps />}
        
      
       
          
      
        

      <p className = "Para"> Display optimal locations for new POGOH locations</p>
      <form>
        
        
      </form>
      <button className="MyButton" onClick={toggleMapVisibility}>
         Generate
      </button>

      <FileUpload />
    {isMapVisible &&
      <div>
          <img
          src="bikeUsageImage.png"
          
          style = {{width: '60%', height: 'auto', marginRight: '20px', marginTop: '40px' }} 
          />
          <img 
              src="busStopsImage.png"
              
              style={{ width: '60%', height: 'auto' , marginRight: '20px', marginTop: '20px'}} 
            />
        {isMapVisible}
      
      </div>
      
    }
      </header>
      

      
    </div>
  );
}

export default App;
