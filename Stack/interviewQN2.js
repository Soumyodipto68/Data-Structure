// Given a Postfix expression, convert it into a Prefix expression.

// Instead of converting Postfix → Infix → Prefix, we can directly convert Postfix → Prefix.
// This method is both efficient (fewer steps) and intuitive, since computers naturally evaluate expressions in Postfix form.

// Examples: 

// Input :  Postfix : AB+CD-*
// Output : Prefix :  *+AB-CD
// Explanation : Postfix to Infix : (A+B) * (C-D)
//               Infix to Prefix :  *+AB-CD

// Input :  Postfix : ABC/-AK/L-*
// Output : Prefix :  *-A/BC-/AKL
// Explanation : Postfix to Infix : ((A-(B/C))*((A/K)-L))
//               Infix to Prefix :  *-A/BC-/AKL 

function isOperator(x) {
    switch (x) {
        case '+':
        case '-':
        case '/':
        case '*':
            return true;
    }
    return false;
}
function postToPre(post_exp) {
    let s = [];

    let length = post_exp.length;

    for (let i = 0; i < length; i++) {

        if (isOperator(post_exp[i])) {
           
            let op1 = s.pop();
            let op2 = s.pop();
            let temp = post_exp[i] + op2 + op1;
            s.push(temp);
        } else {
            s.push(post_exp[i] + "");
        }
    }
    return s.pop();
}

let post_exp = "ABC/-AK/L-*";
console.log("Prefix:", postToPre(post_exp));