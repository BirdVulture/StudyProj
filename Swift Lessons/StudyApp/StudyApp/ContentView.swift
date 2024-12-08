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



struct ContentView: View {
    @State private var users = ["Paul", "Taylor", "Adele"]
    @State private var selection: String? = nil
    
    

    var body: some View {
        
            VStack {
                Spacer()
                HStack {
                    Button("Add data") {
                        users.append("A")
                    }
                  
                }
                Spacer()
                List {
                    ForEach(users, id: \.self) { user in
                        NavigationLink {
                            Text(user)
                        }
                        label: {
                            HStack {
                                Text("User \(user)")
                                Spacer()
                                Text("Delete")
                                    .onTapGesture {
                                        print("OOk")
                                    }
                            }
                        }
                        
                    }
                }
                
                        
                }
                
            }
        
         
}

    

   
    
   









struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

