//https://www.youtube.com/watch?v=CGdcHl8ExcM&list=PLUb9K99oQb2u1swlk6TTuV1vnMEG8ktfV&index=1&pp=iAQB


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
// Array Массив

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

// SET Множество - когда порядок не важен, все значения - уникальные

var set = Set<String>()

var listOfSports: Set = ["Babminton", "Bowling", "Tennis", "Hockey"]

// методы для работы множеством

listOfSports.count //подсчет количества элементов в множестве

listOfSports.isEmpty // проверка на наличие значений

listOfSports.insert("Fishing") //вставка нового элемента

listOfSports.remove("Bowling")

listOfSports

listOfSports.contains("Tennis") //проверка наличия значения в множестве

// работа с сетом через итерации (в цикле)

for i in listOfSports {
    print(i)
}

listOfSports.sorted() // сортировка множества

for i in listOfSports.sorted() {
    print(i)
}

// Преобразование массива в множество

let colors1 = ["red", "green", "blue", "red", "green", "blue"]

let colors2 = Set(colors1)

// базовые операции с множествами

let oddNumbers: Set = [1, 3, 5, 7, 9] // нечетные числа

let evenNumbers: Set = [0, 2 ,4, 6, 8] // четные числа

let primeNumbers: Set = [2, 3, 5, 7] // простые числа

// объединенние двух множеств в третье
oddNumbers.union(evenNumbers).sorted()

// создание множества из общих значений двух других множеств

oddNumbers.intersection(evenNumbers).sorted()
oddNumbers.intersection(primeNumbers).sorted()

//вычитание одного множества из другого

oddNumbers.subtracting(primeNumbers).sorted()

// создание множества из неповторяющихся значений двух других множеств

oddNumbers.symmetricDifference(primeNumbers).sorted()

//Dictionary - словарь Ключ - значение [key: value]

var diction = [Int: String]()

var heights = ["Ian": 1.75, "Maria": 1.76, "Igor": 1.82, "Olga": 1.56]

// работа со словарем по ключу

heights["Ian"]

var results1 = ["Mathematics": 100, "English": 85, "Geography": 75]

results1["English"]

results1.count //подсчет количества элементов
results1.isEmpty //проверка на наличие значений
results1["History"] = 80 // добавление элемента в словарь
results1["History"] = 90

results1["History"]

//обновление значений через методы

results1.updateValue(70, forKey: "History")
results1["History"]

//удаление пары ключ-значение из словаря

results1.removeValue(forKey: "History")
results1["History"]

// итерации со словарем через цикл

for (subject, point) in results1 {
    print("\(subject): \(point) ")
}

for subject in results1.keys {
    print("Subject: \(subject)")
}

for point in results1.values {
    print("point: \(point)")
}

// преобразование в массивы

var keys = Array(results1.keys)
var values = Array(results1.values)

// ФУНКЦИИ

// Объявление и вызов функций

func greetFunc() {
    print("Hello")
}

greetFunc()

// Принимать

func square(number: Int) {
    print(number * number)
}

square(number: 3)


// Возвращать значение в переменную

func square1 (number: Int) -> Int {
    return number * number
}

var result123 = square1(number: 5)

print(result123)

// Возвращать несколько значений в tuple

// Решение 1
func getUser() -> [String] {
    return ["Ivan", "Ivanov"]
}

let user1234 = getUser()

print(user1234[0])


// решение 2
func getUser1() -> [String: String] { // функция возвращает словарь
    return ["firstName": "Ivan", "secondName": "Ivanov"]
}

let user22 = getUser1()

print(user22["secondName"] ?? "not found")

// решение 3 - с помощью tuple

func getUser2() -> (first: String, second: String) {
    return (first: "Ivan", second: "Ivanov")
}

let user23 = getUser2()

print(user23.first)


// Имена параметров

func sayHello(to name: String) {
    print("Hello \(name)")
}

sayHello(to: "Ian")

// Пропуск имен параметров

func sayHello2(_ person: String) {
    print("Hello \(person)")
}

sayHello2("Ian")





















            
            

















