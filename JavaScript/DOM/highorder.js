const add = 'add';
const sub = 'sub';
const mul = 'mul';
const div = 'div';
const mod = 'mod';

function highorder(num1, num2, operator) {
    if (operator === add) {
        return num1 + num2;
    } else if (operator === sub) {
        return num1 - num2;
    } else if (operator === mul) {
        return num1 * num2;
    } else if (operator === div) {
        return num1 / num2;
    } else if (operator === mod) {
        return num1 % num2;
    } else {
        return "Give a real operator";
    }
}

console.log(highorder(2, 4, add)); // 6
console.log(highorder(5, 6, sub)); // -1
console.log(highorder(7, 8, mul)); // 56
console.log(highorder(8, 4, div)); // 2
console.log(highorder(7, 4, mod)); // 3
