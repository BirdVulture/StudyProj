import Foundation

let myAge = 22
let yourAge = 20

if myAge > yourAge {
    "I'm older than you"
}else if myAge < yourAge {
    "I'm younger  than you"
}else {
    "Oh hey, we are same age"
}

let myMotherAge = myAge + 30

/// three different types of operators
///
/// 1. unary prefix
let foo = !true /// ! true ! means NOT
/// 2. binary postfix
let name = Optional("Oleg")
type(of: name)
let unaryPostFix = name!
type(of: unaryPostFix)


/// 3. binary infix - between two values  myAge +(binary infix) 30

let result = 1 + 2


let names = "foo" + " " + "Bar"

let age = 30
//let message: String
//if age >= 18 {
//    message = "You are an adult"
//} else {
//    message = "You are not an adult"
//}



///let message = CONDITION
///    ? VALUE IF CONDITION IS MET
///    : VALUE IF CONDITION IS NOT MET

let message = age >= 18
    ? "You are an adult"
    : "You are not yet an adult"

