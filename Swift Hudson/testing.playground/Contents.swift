import Cocoa

var num1 = 3
var num2 = 5
var nums = [Int]()
var rng = 100


for i in 1...rng  {
    if i.isMultiple(of: num1) && i.isMultiple(of: num2) {
        nums.append(i)
    }
}

print(nums)
