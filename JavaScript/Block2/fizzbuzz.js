var output = [];
var count = 1;
function fizzbuzz(){
    output.push(count);
    count++;
    console.log(output);
}
var stop = false;
while(stop==false){
fizzbuzz();
if (count ==10){
    stop= true;
}
}