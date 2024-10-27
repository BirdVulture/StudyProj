//
//  ContentView.swift
//  BalanceApp
//
//  Created by Oleg Z on 25.10.2024.
//

import SwiftData
import SwiftUI

struct ContentView: View {
    @Environment(\.modelContext) var modelContext
    @Query var destinations: [Destination]
    
    var body: some View {
        NavigationStack {
            List {
                ForEach(destinations) { destination in
                    VStack(alignment: .leading) {
                        Text(destination.name)
                            .font(.headline)
                    
                        Text(destination.date.formatted(date: .long, time: .shortened ))
                }
                    .navigationTitle("BalancseApp")
                    .toolbar{
                        Button("Add Samples", action: addSamples)
                    }
                }
            }
        }
    }
    
    func addSamples() {
        let rome = Destination(name: "Rome")
        let florence = Destination(name: "Florece")
        let naples = Destination(name: "Naples")
        
        modelContext.insert(rome)
        modelContext.insert(florence)
        modelContext.insert(naples)
    }
    
}






#Preview {
    ContentView()
}
