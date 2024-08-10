var bottle = 10
while(true){
    console.log(+bottle +" bottles of beer on the wall, "+bottle+ " bottles of beer.")
    --bottle
    console.log("Take one down and pass it around,"+bottle+" bottles of beer on the wall.")
    if(bottle==1)break;
}