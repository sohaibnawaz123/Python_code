from tkinter import*

class Restaurant(Tk):
    def __init__(self):
        super().__init__()
        #BREAK_FAST VARIABLES
        self.customer = StringVar()
        self.table = StringVar()
        # self.prizeb = [50, 100, 75, 120, 150, 200,350, 50, 100, 30, 100]
        # self.prizel = [500,500,550,450,450,300,250,550,450,600,500,500,650,750]
        # self.prized = [300,350,300,400,450,450,500,350,50,250,450,500,600,650,1000,700,50,300,900]
        self.total =0
        self.chai_prize,self.coffee_prize,self.green_tea_prize ,self.apple_juice_prize,self.orange_juice_prize ,self.french_tose_prize\
        ,self.vanilla_latte_prize ,self.omelet_prize ,self.vegetable_omelet_prize,self.paratha_prize,self.pizza_paratha_prize = 50, 100, 75, 120, 150, 200,350, 50, 100, 30, 100

        self.chai , self.coffee ,self.green_tea,self.apple_juice ,self.orange_juice ,self.french_tose,\
        self.vanilla_latte ,self.omelet, self.vegetable_omelet, self.paratha,self.pizza_paratha = IntVar(),IntVar(),\
                                    IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()

        #LUNCH VARIABLE
        self.spghaetti,self.pasta_salad,self.italian_salad,self.muffins,self.bread_rolls,self.mash_potatos,\
        self.potato_chips,self.beef_steak_sandwitchs,self.chicken_steak_sandwitchs,self.beef_burek,\
        self.chese_spinach_burek,self.chicken_burek,self.charcoal_chicken,\
        self.bosnian_kebab = 500,500,550,450,450,300,250,550,450,600,500,500,650,750

        self.SPGHAETTI ,self.PASTA_SALAD ,self.ITALIAN_SALAD , self.MUFFINS ,self.BREAD_ROLLS ,self.MASH_POTATOS ,\
        self.POTATO_CHIPS,self.BEEF_STEAK_SANDWITCHS,self.CHICKEN_STEAK_SANDWITCHS,self.BEEF_BUREK ,\
        self.CHESE_SPINACH_BUREK,self.CHICKEN_BUREK,self.CHARCOAL_CHICKEN,self.BOSNIAN_KEBAB = IntVar(),\
        IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        self.l_total = 0

        # Dinner_Variables
        self.Hot_soup,self.Chicken_soup,self.Kuchumber_salad,self.Hawaii_salad,self.Thai_vegetable_salad,\
        self.kheer,self.Gulab_jamun,self.Fresh_juice,self.Mutton_biryani,self.Mutton_qeema,self.Gola_kabab,self.Green_boti,\
        self.Finger_fish,self.Vegetable_rice,self.Mix_nan,self.Beef_biryani,self.Brain_masala,\
        self.Labe_shireen,self.Soft_drinks=IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),\
            IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()

        self.Hot_Soup, self.Chicken_Soup, self.Kuchumber_Salad, self.Hawaii_Salad, self.Thai_Vegetable_Salad, \
        self.Kheer, self.Gulab_Jamun,self.Labe_Shireen,self.Soft_Drinks,self.Fresh_Juice,self.Mutton_Biryani, self.Mutton_Qeema\
            , self.Gola_Kabab, self.Green_Boti, \
        self.Finger_Fish, self.Vegetable_Rice, self.Mix_Nan,self.Beef_Biryani\
            ,self.Brain_Masala = 300,350,300,400,450,450,500,350,50,250,450,500,600,650,1000,700,50,300,900
        self.d_tolal = 0

    def SHOW(self):
        self.geometry("1500x900")
        self.minsize(750, 450)
        # self.scroll_bar = Scrollbar(self,orient= VERTICAL).pack(side = RIGHT)

        self.title("Restaurant Menu")
        self.configure(background="lightgrey")
        # try:
        #     self.wm_iconbitmap("logo.ico")
        #     self.photo = PhotoImage(file="logoPNG.png")
        #     Label(image=self.photo).pack(pady= 30)
        # except EXCEPTION:
        #     print("image not found")

        self.f1= Frame(self,bg ="lightblue",borderwidth = 5)
        self.restaurant_name=Label(self.f1,bg ="black",fg="white" ,text="WELCOME TO THE NEON LIGHT RESTAURANT",
                                   font="Agency 20 bold underline",pady =5).pack(side= TOP ,anchor =N ,fill =X,)
        self.f1.pack(pady =15)
        self.f2 =Frame(self,bg ="lightblue",borderwidth = 6)
        Label(self.f2,text="Enter Customer Name!",font="Agency 16 bold",fg = "Black",bg ="white")\
            .pack(anchor =N,side= "left")
        self.cus_name =Entry(self.f2,text = "Agency 20 bold",width =30,textvariable = self.customer)\
            .pack(anchor =N,side= "left",pady=5,padx =5)
        self.f2.pack(anchor =N,pady=15)

        self.f5 = Frame(self, bg="lightblue", borderwidth=6)
        Label(self.f5, text="Enter Table #:", font="Agency 16 bold", fg="Black", bg="white")\
            .pack(anchor=N, side="left")
        self.tab = Entry(self.f5, text="Agency 20 bold",width= 16, textvariable=self.table)\
            .pack(anchor=N, side="left",pady=5, padx=5)
        Button(self.f5, text="ENTER!", font="Agency 10 bold ",command=self.Enter)\
            .pack(anchor=N, side="left", padx=5)
        self.f5.pack(anchor=N, pady=15)

        self.f4 = Frame(self, bg="black")
        Label(self.f4, bg="black").pack(padx=20)
        self.f4.pack(side=LEFT, anchor=E, fill=Y)
        self.f4 = Frame(self, bg="black")
        Label(self.f4, bg="black").pack(padx=20)
        self.f4.pack(side=RIGHT, anchor=W, fill=Y)
        Button(self, text="EXIT!", font="Agency 15 bold", bg="black", fg="white", padx=10, command=self.destroy,
               width=10) \
            .pack(pady=5, padx=5, anchor=S, side=BOTTOM)

    def Enter(self):

        self.l = Label(self, font="Agency 30 bold underline", fg="black", bg="lightgrey") \
            .pack(anchor=N, pady=10)

        self.l = Label(self, text="What Do You Want !", font="Agency 30 bold underline", fg="black", bg="white") \
            .pack(anchor=N, pady=10)
        self.f3=Frame(self, bg ="lightblue",borderwidth = 2)
        self.b=Button(self.f3,text ="Break Fast",font="Agency 15 bold",bg ="white",fg ="black",command = self.Break_fast)\
            .pack(anchor =N,side= LEFT,padx=10)
        Button(self.f3, text="  Lunch  ", font="Agency 15 bold", bg="white", fg="black",padx =10,command = self.Lunch)\
            .pack(anchor=N,side= LEFT,padx=10)
        Button(self.f3, text="  Dinner ", font="Agency 15 bold", bg="white", fg="black",padx =5,command = self.Dinner)\
            .pack(anchor=N,side= LEFT, padx=10)
        self.f3.pack(anchor =N,pady=15)

    def Break_fast(self):
        self.BREAK_FAST = Toplevel(self)
        self.BREAK_FAST.geometry("1500x900")
        self.BREAK_FAST.minsize(750, 450)
        self.BREAK_FAST.title("BREAK FAST MENU")
        self.BREAK_FAST.configure(background="lightgrey")

        Button(self.BREAK_FAST, text="EXIT!", font="Agency 15 bold", bg="black", fg="white", padx=10,
               command=self.BREAK_FAST.destroy).pack(pady=5,padx=5,anchor=S, side=BOTTOM)

        self.BREAK_FAST.f6 = Frame(self.BREAK_FAST, bg="white")
        Label(self.BREAK_FAST.f6, text=" ITEMS ", font="Serif 30 bold underline", bg="black", fg="yellow")\
            .pack(side=TOP, anchor=NW, pady=5, padx=30)
        Label(self.BREAK_FAST.f6, text="1) CHAI ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        Label(self.BREAK_FAST.f6, text="2) COFFEE ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        Label(self.BREAK_FAST.f6, text="3) GREEN TEA ", font="Serif 15  underline", fg="black")\
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.BREAK_FAST.f6, text="4) APPLE JUICE ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.BREAK_FAST.f6, text="5) ORANGE JUICE ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.BREAK_FAST.f6, text="6) FRENCH TOSE ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.BREAK_FAST.f6, text="7) VANILLA LATTE ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.BREAK_FAST.f6, text="8) OMELET ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        Label(self.BREAK_FAST.f6, text="9) VEGETABLE OMELET ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.BREAK_FAST.f6, text="10) PARATHA ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        Label(self.BREAK_FAST.f6, text="11) PIZZA PARATHA ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        self.BREAK_FAST.f6.pack(side=LEFT, anchor=N, fill=Y)

        self.BREAK_FAST.f7 = Frame(self.BREAK_FAST, bg="white")
        Label(self.BREAK_FAST.f7, text=" PRIZE ", font="Serif 30 bold underline",bg="black", fg="yellow").pack(
            side=TOP, anchor=NW, pady=5, padx=30)
        Label(self.BREAK_FAST.f7, text=" Rs : 50 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 100 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW, pady=6,padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 75 ", font="Serif 15  underline",  fg="black")\
            .pack(side=TOP,anchor=NW,pady=6, padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 120 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 150 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW, pady=6,padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 200 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 350 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 50 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 100 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6, padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 30 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP, anchor=NW,pady=6, padx=5)
        Label(self.BREAK_FAST.f7, text=" Rs : 100 ", font="Serif 15 underline", fg="black")\
            .pack(side=TOP,anchor=NW,pady=6,padx=5)
        self.BREAK_FAST.f7.pack(side=LEFT, anchor=N, padx=30, fill=Y)

        self.BREAK_FAST.f8 = Frame(self.BREAK_FAST, bg="white")
        self.BREAK_FAST.l = Label(self.BREAK_FAST.f8, text=" QUANTITY ", font="Serif 30 bold underline", bg="black",
                                  fg="yellow").pack(side=TOP, anchor=NW, pady=5, padx=30)
        self.Chai = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.chai,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.Coffee = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.coffee,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.Green_Tea = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.green_tea,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.Apple_Juice = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.apple_juice,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.Orange_Juice = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.orange_juice,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.French_Tose = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.french_tose,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.Vanilla_Latte = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.vanilla_latte,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.Omelet = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.omelet,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.Vegetable_Omelet = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.vegetable_omelet,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.Paratha = Entry(self.BREAK_FAST.f8, width=10,textvariable=self.paratha,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.Pizza_Paratha = Entry(self.BREAK_FAST.f8, width=10,textvariable= self.pizza_paratha,bg= "lightblue")\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.BREAK_FAST.f8.pack(side=LEFT, anchor=N, padx=2, fill=Y)

        self.BREAK_FAST.f9 =Frame(self.BREAK_FAST,bg = "black")
        Label(self.BREAK_FAST.f9, text="TOTAL BILL:", fg="black",
              font="Serif 11 bold").pack(padx=10, pady=10,anchor=N, side=LEFT)
        self.Total = Entry(self.BREAK_FAST.f9, width=10, font="Serif 20 bold", bg="lightblue")
        self.Total.pack(anchor=N, side=TOP, padx=5, pady=5)
        Label(self.BREAK_FAST, text="Thank's For Ordering\n  Your Order Will \nRecived Soon", fg="black",
              font="Serif 15 bold").pack(padx=25, pady=10, side=TOP, fill=X)
        self.t = Text(self.BREAK_FAST,font="serif 10 ", bg="white", height=35, width=80)
        self.t.pack(pady=20, padx=5, side=TOP, anchor=N)
        self.BREAK_FAST.order = Button(self.BREAK_FAST.f9, text="ORDER", font="Serif 15 bold ", bg="yellow", fg="black"
                                       ,command =self.Break_Fast_Store).pack(pady = 5, anchor=S,side=BOTTOM)
        self.BREAK_FAST.f9.pack(padx = 5,pady = 5,anchor=SE,side=BOTTOM,fill=X)

    def Break_Fast_Store(self):
        try:
            self.total = (self.chai.get() * self.chai_prize) + (self.coffee.get() * self.coffee_prize) + \
                         (self.green_tea_prize * self.green_tea.get()) + (self.apple_juice.get() * self.apple_juice_prize) + \
                         (self.orange_juice_prize * self.orange_juice.get()) + (
                                     self.french_tose.get() * self.french_tose_prize) + \
                         (self.vanilla_latte_prize * self.vanilla_latte.get()) + (self.omelet_prize * self.omelet.get()) + \
                         (self.vegetable_omelet_prize * self.vegetable_omelet.get()) + (
                                     self.paratha_prize * self.paratha.get()) + \
                         (self.pizza_paratha_prize * self.pizza_paratha.get())
        except Exception:

            self.e = "\t\t\tError Found\n\tEnter The Number By Removing Zero\n\n"
            self.t.insert(INSERT,self.e)
            self.t.delete("0.1","end")

        self.Total.delete(0, 'end')
        self.Total.insert(0, self.total)

        with open("Break_Fast.txt", "a") as self.f:
            self.f.write("\t\tBREAK FAST MENU\n")
            self.f.write(f"Customer Name: {self.customer.get() }\nTable #:{self.table.get()}\n")
            self.f.write("=============================================\n")
            self.f.write("     ITEMS                PRIZE \t  AMOUNT\n")
            self.f.write("=============================================\n")
            self.f.write(f"= 01) CHAI               Rs : {self.chai_prize} \t    {self.chai.get()}\n")
            self.f.write(f"= 02) COFFEE             Rs : {self.coffee_prize}\t    {self.coffee.get()}\n")
            self.f.write(f"= 03) GREEN TEA          Rs : {self.green_tea_prize} \t    {self.green_tea.get()}\n")
            self.f.write(f"= 04) APPLE JUICE        Rs : {self.apple_juice_prize}\t    {self.apple_juice.get()}\n")
            self.f.write(f"= 05) ORANGE JUICE       Rs : {self.orange_juice_prize}\t    {self.orange_juice.get()}\n")
            self.f.write(f"= 06) FRENCH TOSE        Rs : {self.french_tose_prize}\t    {self.french_tose.get()}\n")
            self.f.write(f"= 07) VANILLA LATTE      Rs : {self.vanilla_latte_prize}\t    {self.vanilla_latte.get()}\n")
            self.f.write(f"= 08) OMELET             Rs : {self.omelet_prize} \t    {self.omelet.get()}\n")
            self.f.write(f"= 09) VEGETABLE OMELET   Rs : {self.vegetable_omelet_prize}\t    {self.vegetable_omelet.get()}\n")
            self.f.write(f"= 10) PARATHA            Rs : {self.paratha_prize} \t    {self.paratha.get()}\n")
            self.f.write(f"= 11) PIZZA PARATHA      Rs : {self.pizza_paratha_prize}\t    {self.pizza_paratha.get()}\n")
            self.f.write("=============================================\n")
            self.f.write(f"  \tTOTAL BILL : \t\t\t\t{self.total}\n")
            self.f.write("=============================================\n")
            
            self.message =f"\tCustomer Name: {self.customer.get()}\n\tTable #: {self.table.get()}\n"\
                          f"\t=============================================\n" \
                          f"\tITEMS\t\t\tPRIZE \t \tAMOUNT\n" \
                          f"\t=============================================\n" \
                          f"\t01) CHAI               \t\t\tRs : {self.chai_prize}\t\t   {self.chai.get()}\n" \
                          f"\t02) COFFEE             \t\t\tRs : {self.coffee_prize}\t\t   {self.coffee.get()}\n" \
                          f"\t03) GREEN TEA          \t\t\tRs : {self.green_tea_prize}\t\t   {self.green_tea.get()}\n" \
                          f"\t04) APPLE JUICE        \t\t\tRs : {self.apple_juice_prize}\t\t   {self.apple_juice.get()}\n" \
                          f"\t05) ORANGE JUICE       \t\t\tRs : {self.orange_juice_prize}\t\t   {self.orange_juice.get()}\n" \
                          f"\t06) FRENCH TOSE        \t\t\tRs : {self.french_tose_prize}\t\t   {self.french_tose.get()}\n" \
                          f"\t07) VANILLA LATTE      \t\t\tRs : {self.vanilla_latte_prize}\t\t   {self.vanilla_latte.get()}\n" \
                          f"\t08) OMELET             \t\t\tRs : {self.omelet_prize}\t\t   {self.omelet.get()}\n" \
                          f"\t09) VEGETABLE OMELET \t\tRs : {self.vegetable_omelet_prize}\t\t\t   {self.vegetable_omelet.get()}\n" \
                          f"\t10) PARATHA            \t\t\tRs : {self.paratha_prize}\t\t   {self.paratha.get()}\n" \
                          f"\t11) PIZZA PARATHA      \t\t\tRs : {self.pizza_paratha_prize}\t\t   {self.pizza_paratha.get()}\n" \
                          f"\t=============================================\n" \
                          f"\t\tTOTAL BILL : \t\t\t{self.total}\n" \
                          f"\t=============================================\n"

            self.t.insert(INSERT, self.message)


    def Lunch(self):

        self.LANCH = Toplevel(self)
        self.LANCH.geometry("1500x900")
        self.LANCH.minsize(750, 450)
        self.LANCH.title(" LUNCH  MENU")
        self.LANCH.configure(background="lightgrey")
        Button(self.LANCH, text="EXIT!", font="Agency 15 bold", bg="black", fg="white", padx=10,command=self.LANCH.destroy)\
            .pack(pady=5,padx=5,anchor=S, side=BOTTOM)

        self.LANCH.f10 = Frame(self.LANCH, bg="white")
        Label(self.LANCH.f10, text=" ITEMS ", font="Serif 30 bold underline", bg="black", fg="yellow") \
            .pack(side=TOP, anchor=NW, pady=5, padx=30)
        Label(self.LANCH.f10, text="1) SPGHAETTI ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="2) PASTA SALAD ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="3) ITALIAN SALAD ", font="Serif 15  underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="4) MUFFINS ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="5) BREAD ROLLS ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="6) MASH POTATOS ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="7) POTATO CHIPS ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="8) BEEF STEAK SANDWITCHS ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="9) CHICKEN STEAK SANDWITCHS ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="10) BEEF BUREK ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="11) CHESE SPINACH BUREK ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="12) CHICKEN BUREK ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="13) CHARCOAL CHICKEN ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f10, text="14) BOSNIAN KEBAB ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        self.LANCH.f10.pack(side=LEFT, anchor=N, fill=Y)

        self.LANCH.f11 = Frame(self.LANCH, bg="white")
        Label(self.LANCH.f11, text=" PRIZE ", font="Serif 30 bold underline", bg="black", fg="yellow").pack(
            side=TOP, anchor=NW, pady=5, padx=30)
        Label(self.LANCH.f11, text=" Rs : 500 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 500 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 550 ", font="Serif 15  underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 450 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 450 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 300 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 250 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 550 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 450 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 600 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 500 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 500 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 650 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        Label(self.LANCH.f11, text=" Rs : 750 ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
        self.LANCH.f11.pack(side=LEFT, anchor=N, padx=10, fill=Y)
        self.LANCH.f11.pack(side=LEFT, anchor=N, padx=10, fill=Y)

        self.LANCH.f11 = Frame(self.LANCH, bg="white")
        Label(self.LANCH.f11, text=" QUANTITY ", font="Serif 30 bold underline", bg="black",
              fg="yellow").pack(side=TOP, anchor=NW, pady=5, padx=30)
        self.SP = Entry(self.LANCH.f11, width=10,bg="lightblue",textvariable =self.SPGHAETTI) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.P_S = Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable =self.PASTA_SALAD) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.I_S = Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable =self.ITALIAN_SALAD ) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.M = Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable =self.MUFFINS ) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.B_R = Entry(self.LANCH.f11, width=10,bg="lightblue",textvariable =self.BREAD_ROLLS ) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.M_P = Entry(self.LANCH.f11, width=10,bg="lightblue",textvariable =self.MASH_POTATOS ) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.P_C= Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable =self.POTATO_CHIPS) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.BSS = Entry(self.LANCH.f11, width=10,bg="lightblue",textvariable =self.BEEF_STEAK_SANDWITCHS ) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.CHI = Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable =self.CHICKEN_STEAK_SANDWITCHS) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.BE = Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable =self.BEEF_BUREK )\
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.CHE = Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable =self.CHESE_SPINACH_BUREK ) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.CH = Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable =self.CHICKEN_BUREK) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.C= Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable=self.CHARCOAL_CHICKEN) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.B = Entry(self.LANCH.f11, width=10, bg="lightblue",textvariable = self.BOSNIAN_KEBAB) \
            .pack(side=TOP, anchor=N, pady=11, padx=5)
        self.LANCH.f11.pack(side=LEFT, anchor=N, padx=10, fill=Y)
        self.LANCH.f11.pack(side=LEFT, padx=1, fill=Y)

        self.LANCH.f12 = Frame(self.LANCH, bg="black")
        Label(self.LANCH.f12, text="TOTAL BILL:", fg="black",
              font="Serif 11 bold").pack(padx=10, pady=10, anchor=N, side=LEFT)
        self.Total = Entry(self.LANCH.f12, width=10, font="Serif 20 bold", bg="lightblue")
        self.Total.pack(anchor=N, side=TOP, padx=5, pady=5)
        Label(self.LANCH, text="Thank's For Ordering\n  Your Order Will \nRecived Soon", fg="black",
              font="Serif 15 bold").pack(padx=25, pady=10, side=TOP, fill=X)
        self.t = Text(self.LANCH,font="serif 10 ", bg="white", height=35, width=80)
        self.t.pack(pady=20, padx=30, side=TOP, anchor=N)
        self.LANCH.order = Button(self.LANCH.f12, text="ORDER", font="Serif 15 bold ", bg="yellow", fg="black"
                                       , command=self.Lunch_Store).pack(pady=5, anchor=S, side=BOTTOM)
        self.LANCH.f12.pack(padx=5, pady=5, anchor=SE, side=BOTTOM, fill=X)

    def Lunch_Store(self):
        try:
            self.l_total = (self.SPGHAETTI.get() * self.spghaetti) + (self.PASTA_SALAD.get() * self.pasta_salad) + \
                           (self.italian_salad * self.ITALIAN_SALAD.get()) + (self.MUFFINS.get() * self.muffins) + \
                           (self.bread_rolls * self.BREAD_ROLLS.get()) + \
                           (self.MASH_POTATOS.get() * self.mash_potatos) + \
                           (self.potato_chips * self.POTATO_CHIPS.get()) + (
                                       self.beef_steak_sandwitchs * self.BEEF_STEAK_SANDWITCHS.get()) + \
                           (self.chicken_steak_sandwitchs * self.CHICKEN_STEAK_SANDWITCHS.get()) + (
                                   self.beef_burek * self.BEEF_BUREK.get()) + \
                           (self.chese_spinach_burek * self.CHESE_SPINACH_BUREK.get()) + \
                           (self.chicken_burek * self.CHICKEN_BUREK.get()) + (
                                       self.charcoal_chicken * self.CHARCOAL_CHICKEN.get()) + \
                           (self.bosnian_kebab * self.BOSNIAN_KEBAB.get())
        except Exception:
            self.e = "\t\t\tError Found\n\tEnter The Number By Removing Zero\n\n"
            self.t.insert(INSERT, self.e)

        self.Total.delete(0, 'end')
        self.Total.insert(0, self.l_total)

        with open ("Lunch_Store.txt","a") as self.l:
            self.l.write("\t\tLUNCH MENU\n")
            self.l.write(f"Customer Name: {self.customer.get() }\nTable #:{self.table.get()}\n")
            self.l.write("=====================================================\n")
            self.l.write("  ITEMS\t\t\t\t\t\t\t  PRIZE\t\t AMOUNT\n")
            self.l.write("=====================================================\n")
            self.l.write(f"= 01) SPGHAETTI               \tRs : {self.spghaetti} \t    {self.SPGHAETTI.get()}\n")
            self.l.write(f"= 02) PASTA_SALAD             \tRs : {self.pasta_salad}\t    {self.PASTA_SALAD.get()}\n")
            self.l.write(f"= 03) ITALIAN_SALAD           \tRs : {self.italian_salad} \t    {self.ITALIAN_SALAD.get()}\n")
            self.l.write(f"= 04) MUFFINS                 \tRs : {self.muffins}\t    {self.MUFFINS.get()}\n")
            self.l.write(f"= 05) BREAD_ROLLS             \tRs : {self.bread_rolls}\t    {self.BREAD_ROLLS.get()}\n")
            self.l.write(f"= 06) MASH_POTATOS            \tRs : {self.mash_potatos}\t    {self.MASH_POTATOS.get()}\n")
            self.l.write(f"= 07) POTATO_CHIPS            \tRs : {self.potato_chips}\t    {self.POTATO_CHIPS.get()}\n")
            self.l.write(f"= 08) BEEF_STEAK_SANDWITCHS   \tRs : {self.beef_steak_sandwitchs} \t    {self.BEEF_STEAK_SANDWITCHS.get()}\n")
            self.l.write(f"= 09) CHICKEN_STEAK_SANDWITCHS\tRs : {self.chicken_steak_sandwitchs}\t    {self.CHICKEN_STEAK_SANDWITCHS.get()}\n")
            self.l.write(f"= 10) BEEF_BUREK              \tRs : {self.beef_burek} \t    {self.BEEF_BUREK.get()}\n")
            self.l.write(f"= 11) CHESE_SPINACH_BUREK     \tRs : {self.chese_spinach_burek}\t    {self.CHESE_SPINACH_BUREK.get()}\n")
            self.l.write(f"= 12) CHICKEN_BUREK           \tRs : {self.chicken_burek}\t    {self.CHICKEN_BUREK.get()}\n")
            self.l.write(f"= 13) CHARCOAL_CHICKEN        \tRs : {self.charcoal_chicken}\t    {self.CHARCOAL_CHICKEN.get()}\n")
            self.l.write(f"= 14) BOSNIAN_KEBAB           \tRs : {self.bosnian_kebab}\t    {self.BOSNIAN_KEBAB.get()}\n")
            self.l.write("=====================================================\n")
            self.l.write(f"  \tTOTAL BILL : \t\t\t\t{self.l_total}\n")
            self.l.write("=====================================================\n")

            self.message=f"Customer Name: {self.customer.get() }\n" \
                         f"Table #:{self.table.get()}\n" \
                         f"=============================================================\n" \
                         f"     ITEMS\t\t\t\t\tPRIZE \t\t  AMOUNT\n" \
                         f"=============================================================\n" \
                         f"01) SPGHAETTI               \t\t\t\t\tRs : {self.spghaetti}\t\t\t{self.SPGHAETTI.get()}\n" \
                         f"02) PASTA_SALAD             \t\t\t\t\tRs : {self.pasta_salad}\t\t\t{self.PASTA_SALAD.get()}\n" \
                         f"03) ITALIAN_SALAD           \t\t\t\t\tRs : {self.italian_salad}\t\t\t{self.ITALIAN_SALAD.get()}\n" \
                         f"04) MUFFINS                 \t\t\t\t\tRs : {self.muffins}\t\t\t{self.MUFFINS.get()}\n" \
                         f"05) BREAD_ROLLS             \t\t\t\t\tRs : {self.bread_rolls}\t\t\t{self.BREAD_ROLLS.get()}\n " \
                         f"06) MASH_POTATOS            \t\t\t\t\tRs : {self.mash_potatos}\t\t\t{self.MASH_POTATOS.get()}\n" \
                         f"07) POTATO_CHIPS            \t\t\t\t\tRs : {self.potato_chips}\t\t\t{self.POTATO_CHIPS.get()}\n" \
                         f"08) BEEF_STEAK_SANDWITCHS   \t\t\t\t\tRs : {self.beef_steak_sandwitchs}\t\t\t{self.BEEF_STEAK_SANDWITCHS.get()}\n" \
                         f"09) CHICKEN_STEAK_SANDWITCHS\t\t\t\t\tRs : {self.chicken_steak_sandwitchs}\t\t\t{self.CHICKEN_STEAK_SANDWITCHS.get()}\n" \
                         f"10) BEEF_BUREK              \t\t\t\t\tRs : {self.beef_burek}\t\t\t{self.BEEF_BUREK.get()}\n" \
                         f"11) CHESE_SPINACH_BUREK     \t\t\t\t\tRs : {self.chese_spinach_burek}\t\t\t{self.CHESE_SPINACH_BUREK.get()}\n" \
                         f"12) CHICKEN_BUREK           \t\t\t\t\tRs : {self.chicken_burek}\t\t\t{self.CHICKEN_BUREK.get()}\n" \
                         f"13) CHARCOAL_CHICKEN        \t\t\t\t\tRs : {self.charcoal_chicken}\t\t\t{self.CHARCOAL_CHICKEN.get()}\n" \
                         f"14) BOSNIAN_KEBAB           \t\t\t\t\tRs : {self.bosnian_kebab}\t\t\t{self.BOSNIAN_KEBAB.get()}\n" \
                         f"===============================================================\n" \
                         f"  \tTOTAL BILL : \t\t\t\t{self.l_total}\n" \
                         f"===============================================================\n"
            self.t.delete("1.0", "end")
            self.t.insert(INSERT,self.message)

    def Dinner(self):
      self.DINNER = Toplevel(self)
      self.DINNER.geometry("1500x900")
      self.DINNER.minsize(750, 450)
      self.DINNER.title("DINNER MENU")
      self.configure(background="lightgrey")
      Button(self.DINNER, text="EXIT!", font="Agency 15 bold", bg="black", fg="white", padx=10,command=self.DINNER.destroy)\
          .pack(pady=5,padx=5,anchor=S, side=BOTTOM)

      self.DINNER.f15=Frame(self.DINNER,bg ="white")
      Label(self.DINNER.f15, text=" ITEMS ", font="Serif 20 bold underline", bg="black", fg="yellow") \
          .pack(side=TOP, anchor=NW, pady=5, padx=30)
      Label(self.DINNER.f15,text= " STARTER ", font="Serif 15 underline", fg="black") \
            .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 1) Hot Soup ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 2) Chicken Soup ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 3) Kuchumber Salad ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 4) Hawaii_Salad ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 5) Thai Vegetable Salad ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)

      Label(self.DINNER.f15, text=" Main Course ", font="Serif 15 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 1) Brain Masala ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 2) Mutton Biryani ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 3) Mutton Qeema ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 4) Beef Biryani ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 5) Gola Kabab ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 6) Green Boti ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 7) Italian Fish/Finger Fish  ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 8) Vegetable Rice ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 9) Mix Nan ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)

      Label(self.DINNER.f15, text=" Drinks/Deserts ", font="Serif 15 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 1) Kheer ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 2) Gulab Jaman ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 3) Labe Shireen ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 4) Fresh Juices ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      Label(self.DINNER.f15, text=" 5) Soft Drinks ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=5)
      self.DINNER.f15.pack(side=LEFT, anchor=N, fill=Y,padx = 10)

      self.DINNER.f16 = Frame(self.DINNER, bg="white")
      Label(self.DINNER.f16, text="PRIZE ", font="Serif 20 bold underline", bg="black", fg="yellow") \
          .pack(side=TOP, anchor=N, pady=5, padx=30)
      Label(self.DINNER.f16,text = "---------------------------------", font="Serif 15 ", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 300 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 350 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 250", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 350 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 400 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text ="---------------------------------" ,font="Serif 15", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 900 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 450 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 500 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 300 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 600 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 650 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 1000 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 700 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 50 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text="---------------------------------", font="Serif 15", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 450 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 500 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 350 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 250 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      Label(self.DINNER.f16, text=" Rs : 50 ", font="Serif 10 underline", fg="black") \
          .pack(side=TOP, anchor=NW, pady=6, padx=15)
      self.DINNER.f16.pack(side=LEFT, anchor=N, fill=Y, padx=10)

      self.DINNER.f17 = Frame(self.DINNER, bg="white")
      Label(self.DINNER.f17, text=" QUANTITY ", font="Serif 20 bold underline", bg="black", fg="yellow") \
          .pack(side=TOP, anchor=NW, pady=5, padx=30)
      Label(self.DINNER.f17, text="---------------------------------", font="Serif 15", fg="black") \
          .pack(side=TOP, anchor=NW, pady=7, padx=5)
      self.h_s = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Hot_soup) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.c_s = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Chicken_soup) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.k_S = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Kuchumber_salad) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.h_s = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Hawaii_salad) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.t_h_S = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Thai_vegetable_salad) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      Label(self.DINNER.f17, text="---------------------------------", font="Serif 15", fg="black") \
          .pack(side=TOP, anchor=NW, pady=7, padx=5)
      self.b_m = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Brain_masala) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.M_b = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Mutton_biryani) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.M_q = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Mutton_qeema) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.B_b = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Beef_biryani) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.G_k = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Gola_kabab) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.G_b = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Green_boti) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.F_f = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Finger_fish) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.V_R = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Vegetable_rice) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      self.M_n = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Mix_nan) \
          .pack(side=TOP, anchor=N, pady=7, padx=5)
      Label(self.DINNER.f17, text="---------------------------------", font="Serif 15", fg="black") \
          .pack(side=TOP, anchor=NW, pady=15, padx=5)
      self.K = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.kheer) \
          .pack(side=TOP, anchor=N, pady=6, padx=5)
      self.G_B = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Gulab_jamun) \
          .pack(side=TOP, anchor=N, pady=6, padx=5)
      self.L_s = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Labe_shireen) \
          .pack(side=TOP, anchor=N, pady=6, padx=5)
      self.F_j = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Fresh_juice) \
          .pack(side=TOP, anchor=N, pady=6, padx=5)
      self.S_d = Entry(self.DINNER.f17, width=10, bg="lightblue", textvariable=self.Soft_drinks) \
          .pack(side=TOP, anchor=N, pady=6, padx=5)
      self.DINNER.f17.pack(side=LEFT, anchor=N, padx=10, fill=Y)

      self.DINNER.f18 = Frame(self.DINNER, bg="black")
      Label(self.DINNER.f18, text="TOTAL BILL:", fg="black",
            font="Serif 11 bold").pack(padx=10, pady=10, anchor=N, side=LEFT)
      self.Total = Entry(self.DINNER.f18, width=10, font="Serif 20 bold", bg="lightblue")
      self.Total.pack(anchor=N, side=TOP, padx=5, pady=5)
      Label(self.DINNER, text="Thank's For Ordering\n  Your Order Will \nRecived Soon", fg="black",
            font="Serif 15 bold").pack(padx=25, pady=10, side=TOP, fill=X)
      self.t = Text(self.DINNER,font="serif 10 ", bg="white", height=30, width=80)
      self.t.pack(pady=20, padx=5, side=TOP, anchor=N)
      self.DINNER.order = Button(self.DINNER.f18, text="ORDER", font="Serif 15 bold ", bg="yellow", fg="black"
                                     , command=self.Dinner_Store).pack(pady=5, anchor=S, side=BOTTOM)
      self.DINNER.f18.pack(padx=5, pady=5, anchor=SE, side=BOTTOM, fill=X)

    def Dinner_Store(self):
        try:
            self.d_tolal = (self.Hot_soup.get() * self.Hot_Soup) + (self.Chicken_soup.get() * self.Chicken_Soup) + \
                         (self.Kuchumber_salad.get() * self.Kuchumber_Salad) + (self.Hawaii_salad.get() * self.Hawaii_Salad) + \
                         (self.Thai_Vegetable_Salad * self.Thai_vegetable_salad.get()) + (self.Brain_masala.get() * self.Brain_Masala) + \
                         (self.Mutton_Biryani * self.Mutton_biryani.get()) + (self.Mutton_Qeema * self.Mutton_qeema.get()) + \
                         (self.Beef_Biryani * self.Beef_biryani.get()) + (self.Gola_Kabab * self.Gola_kabab.get()) + \
                         (self.Green_Boti * self.Green_boti.get())+(self.Finger_Fish * self.Finger_fish.get()) +\
                         (self.Vegetable_Rice * self.Vegetable_rice.get()) + \
                         (self.Mix_Nan * self.Mix_nan.get())+(self.Kheer * self.kheer.get()) + (self.Gulab_Jamun * self.Gulab_jamun.get()) + \
                         (self.Labe_Shireen * self.Labe_shireen.get())+ (self.Fresh_Juice * self.Fresh_juice.get()) + \
                         (self.Soft_Drinks * self.Soft_drinks.get())
        except Exception:
            self.e = "\t\t\tError Found\n\tEnter The Number By Removing Zero\n\n"
            self.t.insert(INSERT, self.e)

        self.Total.delete(0, 'end')
        self.Total.insert(INSERT,self.d_tolal)

        with open("Dinner_Store.txt", "a") as self.d:
            self.d.write("\t\tDinner MENU\n")
            self.d.write(f"\tCustomer Name: {self.customer.get()}\n" )
            self.d.write(f"\tTable #:{self.table.get()}\n" )
            self.d.write(f"\t=====================================================\n" )
            self.d.write(f"\t     ITEMS            \t\t  PRIZE \t     AMOUNT\n" )
            self.d.write(f"\t=====================================================\n" )
            self.d.write(f"\t01) Hot Soup             \tRs : {self.Hot_Soup}\t\t\t{self.Hot_soup.get()}\n" )
            self.d.write(f"\t02) Chicken Soup         \tRs : {self.Chicken_Soup}\t\t\t{self.Chicken_soup.get()}\n" )
            self.d.write(f"\t03) Kuchumber Salad      \tRs : {self.Kuchumber_Salad}\t\t\t{self.Kuchumber_salad.get()}\n" )
            self.d.write(f"\t04) Hawaii Salad         \tRs : {self.Hawaii_Salad}\t\t\t{self.Hot_soup.get()}\n" )
            self.d.write(f"\t05) Thai Vegetable Salad \tRs : {self.Thai_Vegetable_Salad}\t\t\t{self.Thai_vegetable_salad.get()}\n " )
            self.d.write(f"\t06) Brain Masala         \tRs : {self.Brain_Masala}\t\t\t{self.Brain_masala.get()}\n" )
            self.d.write(f"\t07) Mutton Biryani       \tRs : {self.Mutton_Biryani}\t\t\t{self.Mutton_biryani.get()}\n" )
            self.d.write(f"\t08) Mutton Qeema         \tRs : {self.Mutton_Qeema}\t\t\t{self.Mutton_qeema.get()}\n" )
            self.d.write(f"\t09) Beef Biryani         \tRs : {self.Beef_Biryani}\t\t\t{self.Beef_biryani.get()}\n" )
            self.d.write(f"\t10) Gola Kabab           \tRs : {self.Gola_Kabab}\t\t\t{self.Gola_kabab.get()}\n" )
            self.d.write(f"\t11) Green Boti           \tRs : {self.Green_Boti}\t\t\t{self.Green_boti.get()}\n" )
            self.d.write(f"\t12) Finger/ Italian Fish \tRs : {self.Finger_Fish}\t\t\t{self.Finger_fish.get()}\n" )
            self.d.write(f"\t13) Vegetable Rice       \tRs : {self.Vegetable_Rice}\t\t\t{self.Vegetable_rice.get()}\n" )
            self.d.write(f"\t14) Mix Nan              \tRs : {self.Mix_Nan}\t\t\t\t{self.Mix_nan.get()}\n" )
            self.d.write(f"\t15) Kheer                \tRs : {self.Kheer}\t\t\t{self.kheer.get()}\n" )
            self.d.write(f"\t16) Gulab Jamun          \tRs : {self.Gulab_Jamun}\t\t\t{self.Gulab_jamun.get()}\n" )
            self.d.write(f"\t17) Labe Shireen         \tRs : {self.Labe_Shireen}\t\t\t{self.Labe_shireen.get()}\n" )
            self.d.write(f"\t18) Fresh Juice          \tRs : {self.Fresh_Juice}\t\t\t{self.Fresh_juice.get()}\n" )
            self.d.write(f"\t19) Soft Drinks          \tRs : {self.Soft_Drinks}\t\t\t\t{self.Soft_drinks.get()}\n" )
            self.d.write(f"\t=====================================================\n" )
            self.d.write(f"\t  \tTOTAL BILL : \t\t\t\t{self.d_tolal}\n" )
            self.d.write(f"\t=====================================================\n")


            self.message = f"\tCustomer Name: {self.customer.get()}\n" \
                           f"\tTable #:{self.table.get()}\n" \
                           f"\t=====================================================\n" \
                           f"\t     ITEMS\t\t\tPRIZE\t\t\tAMOUNT\n" \
                           f"\t=====================================================\n" \
                           f"\t01) Hot Soup             \t\t\tRs : {self.Hot_Soup}\t\t\t{self.Hot_soup.get()}\n" \
                           f"\t02) Chicken Soup         \t\t\tRs : {self.Chicken_Soup}\t\t\t{self.Chicken_soup.get()}\n" \
                           f"\t03) Kuchumber Salad      \t\t\tRs : {self.Kuchumber_Salad}\t\t\t{self.Kuchumber_salad.get()}\n" \
                           f"\t04) Hawaii Salad         \t\t\tRs : {self.Hawaii_Salad}\t\t\t{self.Hot_soup.get()}\n" \
                           f"\t05) Thai Vegetable Salad \t\t\tRs : {self.Thai_Vegetable_Salad}\t\t\t{self.Thai_vegetable_salad.get()}\n " \
                           f"\t06) Brain Masala         \t\t\tRs : {self.Brain_Masala}\t\t\t{self.Brain_masala.get()}\n" \
                           f"\t07) Mutton Biryani       \t\t\tRs : {self.Mutton_Biryani}\t\t\t{self.Mutton_biryani.get()}\n" \
                           f"\t08) Mutton Qeema         \t\t\tRs : {self.Mutton_Qeema}\t\t\t{self.Mutton_qeema.get()}\n" \
                           f"\t09) Beef Biryani         \t\t\tRs : {self.Beef_Biryani}\t\t\t{self.Beef_biryani.get()}\n" \
                           f"\t10) Gola Kabab           \t\t\tRs : {self.Gola_Kabab}\t\t\t{self.Gola_kabab.get()}\n" \
                           f"\t11) Green Boti           \t\t\tRs : {self.Green_Boti}\t\t\t{self.Green_boti.get()}\n" \
                           f"\t12) Finger/ Italian Fish \t\t\tRs : {self.Finger_Fish}\t\t\t{self.Finger_fish.get()}\n" \
                           f"\t13) Vegetable Rice       \t\t\tRs : {self.Vegetable_Rice}\t\t\t{self.Vegetable_rice.get()}\n" \
                           f"\t14) Mix Nan              \t\t\tRs : {self.Mix_Nan}\t\t\t{self.Mix_nan.get()}\n" \
                           f"\t15) Kheer                \t\t\tRs : {self.Kheer}\t\t\t{self.kheer.get()}\n" \
                           f"\t16) Gulab Jamun          \t\t\tRs : {self.Gulab_Jamun}\t\t\t{self.Gulab_jamun.get()}\n"\
                           f"\t17) Labe Shireen         \t\t\tRs : {self.Labe_Shireen}\t\t\t{self.Labe_shireen.get()}\n" \
                           f"\t18) Fresh Juice          \t\t\tRs : {self.Fresh_Juice}\t\t\t{self.Fresh_juice.get()}\n" \
                           f"\t19) Soft Drinks          \t\t\tRs : {self.Soft_Drinks}\t\t\t{self.Soft_drinks.get()}\n" \
                           f"\t=====================================================\n" \
                           f"\t  \tTOTAL BILL : \t\t\t\t{self.d_tolal}\n" \
                           f"\t=====================================================\n"
            self.t.delete("1.0","end")
            self.t.insert(INSERT, self.message)


if __name__ == '__main__':

    menu = Restaurant()
    menu.SHOW()
    menu.mainloop()