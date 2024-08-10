function bmi(height,weight){
    var bmi = weight/(height*height);
    return bmi;
}

var ans = bmi(1.8,68);
console.log(ans);