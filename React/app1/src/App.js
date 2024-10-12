const fname = 'Mayank';
const lname = 'Mishra';
const age = 20;

function App() {
  return (
    <>
      <h1>Kilua Coder</h1>
      <ul>
        <li>Hunter X Hunter</li>
        <li>Naruto</li>
        <li>One Piece</li>
      </ul>
    </>
  );
}

function Names() {
  return (
    <>
      <h1>Hello {fname} {lname}</h1>
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
