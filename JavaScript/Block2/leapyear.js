var year = 2100;
function isleapyear(){
if(year%4==0){
    if(year%100==0){
        return false
    }
    else{
        return true;
    }
}
else{
    return false
}}

var ans = isleapyear(year);
console.log(ans);
