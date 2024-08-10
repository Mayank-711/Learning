function fibonacci(n) {
    if (n <= 0) return []; // Handle edge cases
    if (n === 1) return [0];
    if (n === 2) return [0, 1];

    var output = [0, 1];
    for (var i = 2; i < n; i++) {
        var secondlast = output[i - 2];
        var last = output[i - 1];
        output.push(secondlast + last);
    }
    return output;
}

var ans = fibonacci(10);
console.log(ans);
