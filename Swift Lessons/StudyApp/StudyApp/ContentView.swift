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
import SwiftData



struct ContentView: View {
    @State private var showHello = true
    @State private var showDetail = false
    
    
    var body: some View {
        VStack(spacing: 100) {
            Toggle(isOn: $showHello) {
                Text("Show Hello")
            } .padding()
            if showHello {
                Text("Hello")
            }
            
            Button(action: {
                self.showDetail.toggle()
            }, label: {
                Image(systemName: "minus")
            })
            if showDetail {
                Text("somthing")
            }
            
            
            
            Text("Hello world")
                .foregroundColor(.white)
                .frame(width: 200, height: 200)
                .padding(.all, 50)
                .lineLimit(nil)
                .truncationMode(.middle)
                .font(.largeTitle)
                .multilineTextAlignment(.center)
                .background(Color.gray)
                .padding(.all, 50)
                .background(Color.indigo)
            Image(systemName: "minus.circle")
                .padding(30)
        }
        
    }
}

















struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
                                
