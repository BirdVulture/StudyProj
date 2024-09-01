import Foundation

let myName = "Oleg"
let yourName = "Foo"

var names = [
    myName,
    yourName
]

names.append("Misha")
names.append("Mama")

let foo = "Foo"
var foo2 = foo
foo2 = "Foo2"
foo
foo2

let moreNames = [ //structure
    "Foo",
    "Bar"
]

var copy = moreNames
copy.append("Baz")
moreNames
copy

let oldArray = NSMutableArray(   //class NSMutableArray
    array: [
        "Foo",
        "Bar"
    ]
)

oldArray.add("Baz")

var newArray = oldArray
newArray.add("Qux")
oldArray
newArray

let someNames = NSMutableArray(   //class NSMutableArray
    array: [
        "Foo",
        "Bar"
    ]
)
func changeTheArray(_ array: NSArray) {
    let copy = array as! NSMutableArray
    copy.add("Buz")
}
changeTheArray(someNames)
someNames
 

