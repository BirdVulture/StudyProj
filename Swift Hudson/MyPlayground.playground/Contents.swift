import Cocoa

///VARIABLES AND CONSTANTS
var name = "Ted" // variable

name = "Keeley"

let character = "Daphne" // constant

var playerName = "Roy"
print(playerName)



let managerName = "Michael Scott"
let dogBreed = "Samoed"
let meaningOfLife = "How many roads must a man walk down?"

/// STRINGS

let quote = "Then he tapped a sign saying \"Believe\" and walked away." // backslash before quotes


let  multiLineString = """
"Then he tapped a sign
saying \"Believe\" and walked away.
"""

let nameLength = name.count // cont symbols in string
print(multiLineString.uppercased()) // string to uppercase
print(meaningOfLife.hasPrefix("How many"))
print(meaningOfLife.hasSuffix("down?"))

/// NOMBERS. INTEGER

let score = 10
let reallyBig = 100_000_000

let lowerScore = score - 2
let higherScore = score + 10
let doubleScore = score * 2
let squaredScore = score * score

var counter = 1
counter = counter + 5
counter += 1

let number = 6
print(number.isMultiple(of: 3)) // is multiple?

///NUMBERS. DECIMAL (DOUBLE)

let numberTwo = 0.1 + 0.2
print(numberTwo)

let a = 1
let b = 2.0

let c = Double(a) + b

var rating = 5.0
rating *= 2

/// BOOLEAN

let filename = "paris.jpg"
print(filename.hasSuffix(".jpg"))

let goodDogs = true

/// JOIN STRINGS TOGETHER

let firstPart = "Hello, "
let secondPart = "world!"
let greeting = firstPart + secondPart
let luggageCode = "1" + "2" + "3"

let firstName = "Taylor"
let age = 26

let message = "Hello, my name is \(firstName) and I'm \(age)"
print(message)

print("5 x 5 is \(5 * 5)")

/// ARRAYS

var beatles = ["John", "Paul", "George", "Ringo"] // Array of strings

var numbers = [4, 8, 15] //Array of integers

var temperatures = [25.3, 28.2, 26.4]

print(temperatures[0])

numbers.append(9)

var scores = Array<Int>()  // Array must hold integers
scores.append(100)

var albums = [String]()
albums.append("Folklore")
albums.append("red")
print(albums.count)

beatles.remove(at: 3)
var count = beatles.count

let bondMovies = ["Casino Royale", "Spectre", "No Yime to Die"]
print(bondMovies.contains("Frozen")) // Check array  for Frozen

let cities = ["London", "Tokyo", "Rome"]
print(cities.sorted())

print(cities.reversed())

/// DICTIONARIES

var employee = [
    "name" : "Taylor Swift",
    "job" : "Singer",
    "location" : "Nashville"
]

print(employee["name", default: "Unknown"])
print(employee["job", default: "Unknown"])
print(employee["home", default: "Unknown"])

let hasGraduated = [
    "Eric": false,
    "Maeve": false,
    "Otis": false
]

let olympics = [
    2012: "London",
    2016: "Rio",
    2021: "Tokyo"
]

print(olympics[2012, default: "Unknown"])

var heights = [String: Int]()
heights["Yao"] = 229
heights["shaquille"] = 216
heights["James"] = 206
print(heights)



///SETS

