let greeting;
const date = new Date();
const currentTime = date.getHours();
const customStyle = {
    color: ""
  };
if (currentTime < 12) {
  greeting = "Good Morning";
  customStyle.color = "red";
} else if (currentTime < 18) {
  greeting = "Good Afternoon";
  customStyle.color = "green";
} else {
  greeting = "Good Night";
  customStyle.color = "blue";
}

export {greeting,customStyle};