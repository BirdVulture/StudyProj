import Cocoa

class Animal {
    var name = "Animal name"
    
    init(name: String = "Animal name") {
        self.name = name
    }
    
}

class Dog: Animal {
    let haveTail: Bool
    
    func speak() {
        print("gaf")
    }
    
    init(name: String, haveTail: Bool) {
        self.haveTail = haveTail
        super.init(name: name)
    }
    
}

class Cat: Animal {
    let haveTail: Bool
    
    func speak() {
        print("miu")
    }
    
    init(name: String, haveTail: Bool) {
        self.haveTail = haveTail
        super.init(name: name)
    }
    
}

let bosya = Cat(name: "Bosya", haveTail: true)

bosya.speak()

let basya = Dog(name: "Basik", haveTail: true)

basya.speak()



