export function Avatar(props){
    return (
             <img
              alt = "Profile Image"
              src={props.img}
                className="circle-img"
              />
        
    )
}