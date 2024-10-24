import Cocoa

var data = [Int]()

data = [1, 2, 3]
func ranData(data: [Int]) -> Int {
    let ranNum = data
    let value =  ranNum.randomElement() ?? 0
    return value
}

let value = ranData(data: data)


