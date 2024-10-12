import { greeting,customStyle } from "./heading";
import { add,sub,mul,div } from "./calcuator";
function App(){
  return(
    <>
    <h1 style={customStyle}>{greeting}</h1>
    </>
  )
}
export default App;

function calculator(){
  return (
    <>
    <h1>Calculator</h1>
    <li>{add(2,5)}</li>
    <li>{sub(5,2)}</li>
    <li>{mul(2,5)}</li>
    <li>{div(6,3)}</li>
    </>
  )
}
export {calculator}