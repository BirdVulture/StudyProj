import Cocoa

var ex = { (num: Int) -> Int in
    num * 2
    }

print(ex(2))


func exemple(nums: Int) -> Int{
    var dat = nums * 2
    return dat
}

var data2: (Int) -> Int = exemple

var numb = data2(12)



