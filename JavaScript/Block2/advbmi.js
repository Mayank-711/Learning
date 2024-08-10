function bmi(height,weight){
    var bmi = weight/(height*height);
    return bmi;
}

var ans = bmi(1.8,90);
if(ans<18.5){
    console.log("Maut ke kagar pe");
}
if(ans<24.5 && ans> 18.5){
    console.log("Khaate pite ghar ka");
}
else{
    console.log("Bhais");
}