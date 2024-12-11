//
//  ContentView.swift
//  StudyApp
//
//  Created by Oleg Z on 15.11.2024.
//

//
//  ContentView.swift
//  MyFirstProject
//
//  Created by Oleg Z on 09.11.2024.
//

import SwiftUI

struct Task: Identifiable {
    var id: ObjectIdentifier
    
    }

struct ContentView: View {
    @State private var data = [1, 2, 3, 4]
    @State private var selected = 0

    var body: some View {
        VStack {
            Spacer()
            HStack {
                Spacer()
                Button("Add data") {
                    addData()
                }
                Spacer()
                
            }
            Spacer()
            List {
                  ForEach(data, id: \.self) { element in
                      HStack {
                          Text("Data \(element)")
                          Spacer()
                          Image(systemName: "delete.left")
                              .onTapGesture {
                                  print("element \(element)" )
                                  print(data)
                                  
                                  let indexValue = data.firstIndex(of: element) ?? 0
                                  print(indexValue)
                                  deleteData(index: indexValue)
                                  print(data)
                                  
                              }
                                  
                                  
                        
                      }
                  }
                }
            
        }
    }
    
    func addData() {
        data.append(data.count + 1)
    }
    
    func deleteData(index: Int) {
        data.remove(at: index)
    }
}

    

   
    
   








#Preview {
    ContentView()
}

