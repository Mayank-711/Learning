var names = ['Mayank','Amit','Abhisex','Ganesh'];
var posi = Math.floor(Math.random()*names.length);
function whowillpay(hewill){
    return names[hewill];
}
var whowillpay = whowillpay(posi);
console.log(whowillpay +" Will Pay The Bill")