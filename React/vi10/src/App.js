import { greeting,customStyle } from "./heading";

function App(){
  return(
    <>
    <h1 style={customStyle}>{greeting}</h1>
    </>
  )
}
export default App;