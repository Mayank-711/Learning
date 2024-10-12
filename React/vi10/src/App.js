import './style.css';

function App() {
  return (
    <>
      <h1>Hello</h1>
    </>
  );
}

export default App;

function greet() {
  const now = new Date(); // Get the current date and time
  let hours = now.getHours();// Get the current hours in UTC
  if (hours < 12){
    return(
      <>
      <h1 class = "morning"> Good Morning
        </h1></>
    )
  } 
  else if (hours >12 && hours <18){
    return(
      <>
      <h1 class="afternoon">Good Evening
        </h1></>
    )
  }
  else {
    return(
      <>
      <h1 class="goodnight"> Good Night
        </h1></>
    )
  }// Logs the hours to the console
}

export { greet };
