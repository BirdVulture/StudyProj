//
//  BalanceAppApp.swift
//  BalanceApp
//
//  Created by Oleg Z on 25.10.2024.
//

import SwiftUI
import SwiftData

@main
struct BalanceAppApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Destination.self)
    }
}

