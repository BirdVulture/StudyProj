import Cocoa

func max_lengt(a: Int, b: Int, c: Int) -> Int {
    var maxValue = a
    
    if b > maxValue {
        maxValue = b
    }
    if c > maxValue {
        maxValue = c
    }
        
    return maxValue
}

print(max_lengt(a: 100, b: 20, c: 55))

