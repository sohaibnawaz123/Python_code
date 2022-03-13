from tkinter import*

class Resturant:
    prizes =[50, 100, 75, 120, 150, 200 ,350 , 50 , 100 , 30 , 100 ,500 ,500 , 550 , 450 , 450 , 300 , 250 , 550 ,450 , 600 , 500 , 500 , 650 ,
         750 , 300 , 350 , 300 , 400 , 450 , 450 , 500 , 350 , 50 , 250 , 450 , 500 , 600 , 650 , 1000 , 700 , 50 , 300 ,900 ]
    item_name = [ "Chai" , "Coffee" ,"Green Tea","Apple Juice" ,"Orange Juice" ,"French Tose","Vanilla Latte" , "Omelet", "Vegetable Omelet", "Paratha","Pizza Paratha"]
    
    def __init__(self,root):
        self.root = root
        self.sum = 0
        self.chai , self.coffee ,self.green_tea,self.apple_juice ,self.orange_juice ,self.french_tose,\
        self.vanilla_latte ,self.omelet, self.vegetable_omelet, self.paratha,self.pizza_paratha = IntVar(),IntVar(),\
                                    IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        
        self.vara = [self.chai , self.coffee ,self.green_tea,self.apple_juice ,self.orange_juice ,
                    self.french_tose,self.vanilla_latte ,self.omelet, self.vegetable_omelet, self.paratha,self.pizza_paratha]
        self.F5 =Frame(self.root,relief=SUNKEN,borderwidth=10,background="black")
        self.t =Text(self.F5,width = 72,height = 10)
        self.t.pack()
        self.F5.pack()
        self.f =Frame(self.root,relief=SUNKEN,borderwidth=10,background="black")
        self.F1 = Frame(self.f)
        self.F2 = Frame(self.f)
        self.F3 = Frame(self.f)
        for i in range(0,len(self.item_name)):
            Label(self.F1 , text =f"{i+1}) {self.item_name[i]}",font="serif 15 bold",relief= FLAT,width = 20,bg="lightblue" ,justify= LEFT,anchor=W).pack(padx=5,pady =1 )
            Label(self.F2 , text =f" Rs : {self.prizes[i]}",font="serif 15 bold",relief= FLAT,width = 15,bg="lightblue",justify= LEFT,anchor=W).pack(pady =1)
            Entry(self.F3,font="serif 16 ",relief= RIDGE,width = 10,textvariable=self.vara[i]).pack(pady =2,padx =5)
        self.F1.pack(side = LEFT) 
        self.F2.pack(side = LEFT)  
        self.F3.pack(side = LEFT) 
        self.f.pack()
        self.F4 =Frame(self.root)
        Button(self.F4,text = "CLICK",relief=RAISED,command= self.CAL).pack(side=LEFT)
        Button(self.F4,text = "RESET",relief=RAISED,command= self.Reset).pack(side=LEFT)
        self.F4.pack()  
        self.root.mainloop()
    def CAL(self):
        for i in range(0,len(self.item_name)):
            try:
                
                self.vara[i] = self.vara[i].get()                    
                if(self.vara[i]!= 0):
                    self.sum =self.sum + (self.vara[i]*self.prizes[i]) 
                    self.t.insert(END,f"=> {self.item_name[i]}\t\t\t:\t{self.prizes[i]}\t:\t{self.vara[i]}\n")
            except EXCEPTION:
                pass        
        self.t.insert(INSERT,"===================================================\n")  
        self.t.insert(INSERT,f" TOTAL = {self.sum}\n")
        self.t.insert(INSERT,"===================================================\n") 
    def Reset(self):
        self.t.delete("1.0","end")                          
                            
        
if __name__ == '__main__':
    root = Tk()
    obj = Resturant(root)   