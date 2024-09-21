import Cocoa


let myName = "Oleg"
let myAge = 44
let yourName = "Misha"
let yourAge = 13

if myName == "oleg" {
    "your name is \(myName)"
} else {
    "Oops, I gussed it wrong"
}

if myName == "Oleg" {
    "Now I guessed it correctly"
} else if myName == "Foo" {
    "Are you foo?"
} else {
    "Okay I give up"
}


if myName == "Oleg" && myAge == 44 {        // AND
    "Name is Oleg and Age is 44"
} else if myAge == 20 {
    "I only guessed the age right"
} else {
    "I don't know what i'm doing "
}

if myAge == 20 || myName == "Foo" {         // OR
    "Either age is 20,  name is Foo or both"
} else if myName == "Oleg" || myAge == 44 {
    "Its too late  to get in this clause"
}

if myName == "Oleg"
    && myAge == 44
    && yourName == "Foo"
|| yourAge == 13 {
    "My name is Oleg and I'm 44  and your name is Foo ... OR  .. you are 13"
}


if (myName == "Oleg"
    && myAge == 44)
    &&
    (yourName == "Misha"
     || yourAge == 14) {
    "My name is Oleg and I'm 44... AND .... your name is Misha or you are 13"
} else {
    "Hmm,  that didn't work so well"
}
