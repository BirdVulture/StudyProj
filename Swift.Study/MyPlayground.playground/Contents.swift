
// КОНСТАНТЫ И ПЕРЕМЕННЫЕ

let greetings = "Hello" // Константа

var direction = "Left" // Переменная

direction = "Right" // Переназначение переменной

// ТИПЫ ДАННЫХ

var number: Int = 1

var numDouble: Double = 1.5
var numFloat: Float = 1.5
var greeting1: String = "Hello "
var greeting2: String = "World"

var greetingsum = greeting1 + greeting2 // Конкатенация строк

var greeting3 = "Hello, \(greeting2)" // Интерполяция строк

print(greeting3)

var areYouHappy: Bool = true

//БАЗОВЫЕ ОПЕРАТОРЫ

//Унарные: префиксные -a, !b постфиксные с!
//Бинарные: инфиксные a + b
//Тернарные: a ? b : c

//Оператор присваивания
var a = 12

var b = 5

//b = a

// Арифметические операторы +, -, *, /, % (остаток от деления)

var c = a + b
c = a - b
c = a * b
c = a / b

c = a % b

//Составные операторы присваивания +=, -=

c += 2 // c = c + 2

// Счетчик

var counter = 0

counter += 1

// Операторы сравнения ==, !=, >, <, <=, >=

c > a

//Тернарный условный оператор
//выражение ? действие 1 : (иначе) действие 2

//с помощью if
if a == b {
    print("a = b")
} else {
    print("a != b ")
}
// с помощью тернарного оператора
a == b ? print("a = b") : print("a != b ")

// Оператор замкнутого/закрытого (a...b) диапазона и полузамкнутого/полузакрытого диапазона (a..<b)


// Логические операторы !a (не равно) && (И) || (ИЛИ)

let isTheWeatherGood = true

areYouHappy = true

if areYouHappy && isTheWeatherGood {
    print("Go outside")
} else {
    print("Stay home")
}

// УСЛОВИЯ

let firstCard = 10
let secondCard = 10

if firstCard + secondCard == 21 {
    print("You are win")
} else if (firstCard + secondCard) > 18 && (firstCard + secondCard) < 21 {
    print("Good cards")
} else {
    print("Regular cards")
}

let age1 = 18
let age2 = 21

if age1 > 18 && age2 > 18 {
    print("Both are other 18" )
}

let weather = "sunny"

switch weather {
case "rain": print("Bring an umbrella")
case "snow": print("Wrap it warm")
case "sunny": print("Wear glasses")
    fallthrough //Провалиться дальше
default: print("enjoy")
}

switch age1 {
case 0...10: print("You are too young")
case 13..<20: print("You are teenager")
case 20...60: print("You are grown man")
case 80...: print("You are old man")
default: print("How old are you?")
}

//ЦИКЛЫ



















