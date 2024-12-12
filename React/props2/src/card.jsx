import { Avatar } from "./avatar";
import { Details } from "./details";

export function Card(props){
    return(
      <div>
          <div className="card">
            <div className="top">
                <p>{props.id}</p>
              <h2 className="name">{props.name}</h2>
             <Avatar img = {props.imageurl}/>
             </div>
            <Details number = {props.number} email={props.email}/>
          </div>
        </div>
       
    );
    }