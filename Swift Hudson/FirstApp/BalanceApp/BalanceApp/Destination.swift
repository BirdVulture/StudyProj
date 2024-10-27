//
//  File.swift
//  BalanceApp
//
//  Created by Oleg Z on 26.10.2024.
//

import SwiftData
import SwiftUI

@Model
class Destination {
    var name: String
    var details: String
    var date: Date
    var priority: Int
    
    init(name: String = "", details: String = "", date: Date = .now, priority: Int = 2) {
        self.name = name
        self.details = details
        self.date = date
        self.priority = priority
    }
}
