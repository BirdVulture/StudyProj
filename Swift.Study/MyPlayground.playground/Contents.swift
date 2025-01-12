
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

//ЦИКЛЫ for in / while / repeat while

let count = 1...3

for number in count {
    print("Number is \(number)")
    
}

for index in 0...3 {
    print("\(index) умножить на 3 равно \(index * 3)")
}

var number1 = 1

while number1 <= 3 {
    print(number1)
    number1 += 1
}

print("Start!")

//СОСТАВНОЙ ТИП ДАННЫХ tuple используется для временного хранения данных

var person = (name: "Igor", age: 40, isMarried: true, weight: 70.5)

var tuple1 = (a, b)

var tuple2 = (10, "Hello")

var tuple3: (Int, String)

var tuple4 = (name: "Igor", age: 40, isMarried: true, weight: 70.5)

tuple4.0
tuple4.1

tuple4.name
tuple4.age

var (name, age, isMarried, weight) = tuple4 //разборка tuple4 на элементы

name
age
isMarried
tuple4


// ОПЦИОНАЛЬНЫЕ ТИПЫ ДАННЫХ

var age11: Int? = 12

age11 = nil

// 1 force unwrapping ---!
if age11 == nil {
    print("age is nil")
} else {
    age11! + 1
    
}


//2 Optional binding
let str1  = "5"

let num1 = Int(str1)

if var safeAge = age11 {
    safeAge += 1
}

let yearOfBirth = "1980"

if let safeYearOfBirth = Int(yearOfBirth) {
    safeYearOfBirth
}

// 3 Опциональное связование ??

var example: String? = "Hello"

print(example ?? "example = nil")

// 4 Неявно извлеченные опционалы

// int, Int?, Int!

var num2: Int! = nil

num2 = 10

num2 = num2 + 1



// КОЛЛЕКЦИИ: массивы, множества, словари
// Массивы

var arr1 = Array<String>()

var arr2 = [String]()

let apple = "apple"
let lemon = "lemon"
let orange = "orange"
let strawberry = "strawberry"

let fruits = [apple, lemon, orange, strawberry]

var shoppingList = ["eggs", "milk", "bread", "flour", "sweets"]

// Доступ к массиву - через методы или через индексы
// методы
shoppingList.count // счет количества элементов в массиве

shoppingList.isEmpty // проверка на наличие значений

shoppingList.append("butter") // добавление в конец списка

shoppingList.insert("sugar", at: 0) // вставка нового элемента на место старого по индексу

// доступ через индексы
shoppingList[0]

shoppingList[1] = "salt" // переназначение элемента массива

// Перебор элементов массива через цикл

for i in shoppingList {
    print(i)
}

//индексы и значения массива через цикл

for (index, value) in shoppingList.enumerated() {
    print("Index \(index): \(value) ")
}

// сложение массивов

shoppingList += ["pepper"]

var numb1 = [1, 2, 3, 4, 5]
var numb2 = [6, 7, 8, 9]

var numb3 = numb1 + numb2


// Множества

































            
            

















