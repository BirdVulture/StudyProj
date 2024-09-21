import Foundation

func newFunction () {
    "Hello world"
}

newFunction()


func plusTwo(value: Int) {
    let newValue = value + 2
}


plusTwo(value: 30)

func newPlusTwo(value: Int) -> Int { /// -> return integer
    return value + 2 /// return - we can but we don't need type
}

newPlusTwo(value: 30)

func customAdd (
    value1: Int,
    value2: Int
) -> Int {
    value1 + value2
}

let customAdded = customAdd(
    value1: 10,
    value2: 20
)

func customMinus(
    lhs: Int,
    rhs: Int
) -> Int {
    lhs - rhs
}

let customSubstracted = customMinus(
    lhs: 20,
    rhs: 10
)

func customMinusTwo(
   _ lhs: Int,
   _ rhs: Int
) -> Int {
    lhs - rhs
}

let customSubstractedTwo = customMinusTwo(
    20,
    10
)

customAdd(
    value1: 20,
    value2: 30
)

@discardableResult /// ???
func myCustomAdd(
    _ lhs: Int,
    _ rhs: Int
) -> Int {
    lhs + rhs
}

myCustomAdd(
    20,
    30
)

func doSomethingComplicated( /// complicated functions
    with value: Int
) -> Int {
    func mainlogic(value: Int) -> Int { ///describe internal function
        value + 2
    }
    return mainlogic(value: value + 3) /// call internal function with argument = value + 3
}
doSomethingComplicated(with: 30)

/// default values

func getFullName(
    firstName: String = "Foo",
    lastName: String = "Bar"
) -> String {
    "\(firstName) \(lastName)"
}

getFullName()
getFullName(firstName: "Baz")
getFullName(lastName: "Foo")

getFullName(firstName: "Baz", lastName: "Quix")






