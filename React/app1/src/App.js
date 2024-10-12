import './style.css'
const fname = 'Mayank';
const lname = 'Mishra';
const age = 20;

function App() {
  return (
    <>
      <h1 contentEditable= "true" spellCheck="false">Kilua Coder </h1>
      <ul>
        <li><img class="banner" src='https://m.media-amazon.com/images/M/MV5BYzYxOTlkYzctNGY2MC00MjNjLWIxOWMtY2QwYjcxZWIwMmEwXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg'></img></li>
        <li><img class ="banner" src='https://m.media-amazon.com/images/M/MV5BZTNjOWI0ZTAtOGY1OS00ZGU0LWEyOWYtMjhkYjdlYmVjMDk2XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg'></img></li>
        <li><img class ="banner" src ='https://m.media-amazon.com/images/M/MV5BMTNjNGU4NTUtYmVjMy00YjRiLTkxMWUtNzZkMDNiYjZhNmViXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg'></img></li>
      </ul>
    </>
  );
}

function Names() {
  return (
    <>
      <h1 class="heading">Hello {fname} {lname}</h1>
      <p>Your age is {age}</p>
    </>
  );
}

function v007() {
  const currentYear = new Date().getFullYear(); // Get the current year correctly

  return (
    <>
      <p>Created by {fname} {lname}</p>
      <p>Copyright {currentYear}</p> {/* Display the current year */}
    </>
  );
}

export default App;
export { Names, v007 };
