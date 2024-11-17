//
//  Item.swift
//  MyFirstApp
//
//  Created by Oleg Z on 15.11.2024.
//

import Foundation
import SwiftData

@Model
final class Item {
    var timestamp: Date
    
    init(timestamp: Date) {
        self.timestamp = timestamp
    }
}
