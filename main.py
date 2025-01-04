
#from fileinput import filename
from tkinter import * # type: ignore
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.font import *  # type: ignore
from PIL import Image,ImageTk
import random
from tkinter import messagebox
import os
import tempfile
from time import strftime

class bill_app:
    def __init__(self,root):  #root->window nameppy
        self.root=root
        self.root.geometry('1500x800+0+0')
        self.root.title('Billing Software')
        ############variables#######

        self.cnsme=StringVar()
        self.cphon=StringVar()
        self.bill_no=IntVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.cemail=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.taxes=StringVar()
        self.totals=StringVar()

        ############product category list######################
        self.categoryy=['Select Option','Clothing','Lifestyle','Mobile']
        self.subclothing=['Pant','T-Shirt','Shirt','Jackets']
        self.pant=['Levis','Roadster','Off Duty']
        self.price_levis=4500
        self.price_roadster=2300
        self.price_offduty=2900
        self.tshirt=['U.S. Polo','Roadster','Jack&Jones']
        self.price_us=2100
        self.price_road=1200
        self.price_jack=1189
        self.shirt=['Peter England','Park Avenue','Louis Vuition']
        self.price_peter=1000
        self.price_park=990
        self.price_louis=2300
        self.jacket=['Roadster','Safaras']
        self.price_roads=3300
        self.price_safaras=2589


        self.sublife=['Bathsoap','FaceCream','Hair Oil','Shampoo','Facewash','Perfumes']
        self.bathsoap=['Lux','Dove','Johnson Baby']
        self.price_lux=100
        self.price_dove=180
        self.price_baby=150
        self.facecream=['Foxtale','Nivea','Lakme']
        self.price_fox=350
        self.price_nivea=170
        self.price_lakme=120
        self.hair=['Indulekha','Almond Oil','Rosemarry']
        self.price_indu=440
        self.price_almond=150
        self.price_rose=300
        self.shampoo=['Hair Essence','Indu-lekha','Dove s']
        self.haire=700
        self.price_in=800
        self.price_dovee=500
        self.facewash=['Fox-tale','Wow','Himalayan']
        self.price_foxtale=399
        self.price_wow=300
        self.price_him=200
        self.perfumes=['Watta Girl','Bella Vita','Blue Hommie']
        self.price_watta=300
        self.price_bella=499
        self.price_blue=1999

        self.submobile=['Iphone','Samsung','Xiaomi','One Plus']
        self.iphone=['iphone11','iphone12','iphone13','iphone14']
        self.price_i11=50000
        self.price_i12=69000
        self.price_i13=89000
        self.price_i14=120000

        self.samsung=['New Galaxy Z','Galaxy M14','Galaxy A35']
        self.price_s1=164999
        self.price_s2=10000
        self.price_s3=30999

        self.Xiaomi=['Redmi Note 13','Redmi Note 13Pro','Redmi 14 Civi']
        self.price_r1=16999
        self.price_r2=42999
        self.price_r3=27399

        self.oneplus=['One Plus 9 Pro','One PLus 9R','One Plus Nord CE']
        self.price_o1=64999
        self.price_o2=39999
        self.price_o3=22999



#first 4 images

        img=Image.open('C:/Users/KOMAL/Desktop/wd/mypython/project/imgg/s03.jpeg')
        img=img.resize((320,100)) # type: ignore
        self.photoimg=ImageTk.PhotoImage(img)

        l1=Label(self.root,image=self.photoimg)  # type: ignore
        l1.place(x=0,y=0,width=320,height=100)
        
        img1=Image.open('C:/Users/KOMAL/Desktop/wd/mypython/project/imgg/s01.jpeg')
        img1=img1.resize((320,100)) # type: ignore
        self.photoimg1=ImageTk.PhotoImage(img1)

        l2=Label(self.root,image=self.photoimg1)  # type: ignore
        l2.place(x=320,y=0,width=320,height=100)

        img2=Image.open('C:/Users/KOMAL/Desktop/wd/mypython/project/imgg/s04.jpeg')
        img2=img2.resize((325,100)) # type: ignore
        self.photoimg2=ImageTk.PhotoImage(img2)

        l3=Label(self.root,image=self.photoimg2)  # type: ignore
        l3.place(x=640,y=0,width=325,height=100)

        img4=Image.open('C:/Users/KOMAL/Desktop/wd/mypython/project/imgg/s05.jpeg')
        img4=img4.resize((375,100)) # type: ignore
        self.photoimg4=ImageTk.PhotoImage(img4)

        l4=Label(self.root,image=self.photoimg4)  # type: ignore
        l4.place(x=965,y=0,width=375,height=100)



#billing heading

        ltitle=Label(self.root,text='BILLING SOFTWARE                  ',font=('times new roman',31,'bold'),bg='white',foreground='red')
        ltitle.place(x=0,y=100,width=1500,height=40)
############adding clock
        def myclock():
             watch=strftime('%H:%M:%S %p') # type: ignore
             l1.config(text=watch)
             l1.after(1000,myclock)  #1000=1s

        l1=Label(ltitle,font=('Times new roman',14,'bold'),background='white',foreground='red')
        l1.pack(side=LEFT)

        myclock()  
#frameF

        mainf=Frame(self.root,bd=4,relief=GROOVE,bg='white')
        mainf.place(x=0,y=141,width=1500,height=659)
#CREATING CUSTOMER FIELD

        customerf=LabelFrame(mainf,text='Customer',font=('times new roman',10,'bold'),bg='white',foreground='red')
        customerf.place(x=8,y=4,width=280,height=120)

        self.name=Label(customerf,text='Name',font=('times new roman',10,'bold'),bg='white')
        self.name.grid(row=0,column=0,sticky=W,padx=4,pady=3)

        self.entryn=ttk.Entry(customerf,textvariable=self.cnsme,font=('times new roman',10,'bold'),width=24)
        self.entryn.grid(row=0,column=1)

        self.mob=Label(customerf,text='Mobile No.',font=('times new roman',10,'bold'),bg='white')
        self.mob.grid(row=1,column=0,sticky=W,padx=4,pady=3)

        self.entrym=ttk.Entry(customerf,textvariable=self.cphon,font=('times new roman',10,'bold'),width=24)
        self.entrym.grid(row=1,column=1)

        
        self.e=Label(customerf,text='Email',font=('times new roman',10,'bold'),bg='white')
        self.e.grid(row=2,column=0,sticky=W,padx=4,pady=3)

        self.entrye=ttk.Entry(customerf,textvariable=self.cemail,font=('times new roman',10,'bold'),width=24)
        self.entrye.grid(row=2,column=1)

#CREATING product FIELD

        product=LabelFrame(mainf,text='Product',font=('times new roman',10,'bold'),bg='white',foreground='red')
        product.place(x=300,y=4,width=500,height=120)
#FOR CATEGORY
        self.cat=Label(product,text='Category',font=('times new roman',10,'bold'),bg='white')
        self.cat.grid(row=0,column=0,sticky=W,padx=4,pady=3)

        self.cc=ttk.Combobox(product,values=self.categoryy,font=('times new roman',10,'bold'),width=20,state='readonly')
        self.cc.current(0)
        self.cc.grid(row=0,column=1,sticky=W,padx=4,pady=3)
        self.cc.bind('<<ComboboxSelected>>',self.categories) # type: ignore

        #FOR SUB-CATEGORY
        self.sub=Label(product,text='Subcategory',font=('times new roman',10,'bold'),bg='white')
        self.sub.grid(row=1,column=0,sticky=W,padx=4,pady=3)

        self.cs=ttk.Combobox(product,values=[''],font=('times new roman',10,'bold'),width=20,state='readonly')
        self.cs.grid(row=1,column=1,sticky=W,padx=4,pady=3)
        self.cs.bind('<<ComboboxSelected>>',self.product_add) # type: ignore

         #FOR PRODUCT

        self.pro=Label(product,text='Product',font=('times new roman',10,'bold'),bg='white')
        self.pro.grid(row=2,column=0,sticky=W,padx=4,pady=3)

        self.cp=ttk.Combobox(product,textvariable=self.product,font=('times new roman',10,'bold'),width=20,state='readonly')
        self.cp.grid(row=2,column=1,sticky=W,padx=4,pady=3)
        self.cp.bind('<<ComboboxSelected>>',self.pricez) # type: ignore
         #FOR PRICE
        self.pr=Label(product,text='Price',font=('times new roman',10,'bold'),bg='white')
        self.pr.grid(row=0,column=2,sticky=W,padx=4,pady=3)

        self.cpr=ttk.Combobox(product,textvariable=self.prices,font=('times new roman',10,'bold'),width=20,state='readonly')
        self.cpr.grid(row=0,column=3,sticky=W,padx=4,pady=3)

          #FOR QTY
        self.q=Label(product,text='Quatity',font=('times new roman',10,'bold'),bg='white')
        self.q.grid(row=1,column=2,sticky=W,padx=4,pady=3)

        self.cq=ttk.Entry(product,textvariable=self.qty,font=('times new roman',10,'bold'),width=20,state='readonly')
        self.cq.grid(row=1,column=3,sticky=W,padx=4,pady=3)

#########################photos##################################################
        photo=Frame(mainf,bd=7,bg='white')
        photo.place(x=9,y=126,width=790,height=270)


        imgf=Image.open('C:/Users/KOMAL/Desktop/wd/mypython/project/imgg/s1.jpeg')
        imgf=imgf.resize((395,270)) # type: ignore
        self.photoimgf=ImageTk.PhotoImage(imgf)

        l1=Label(photo,image=self.photoimgf) # type: ignore
        l1.place(x=0,y=0,width=395,height=270)
        
        imgff=Image.open('C:/Users/KOMAL/Desktop/wd/mypython/project/imgg/s4.webp')
        imgff=imgff.resize((390,270)) # type: ignore
        self.photoimgff=ImageTk.PhotoImage(imgff)

        l2=Label(photo,image=self.photoimgff) # type: ignore
        l2.place(x=400,y=0,width=390,height=270)
        


#####################################SEARCH##################

        sf=Frame(mainf,bd=2,bg='white')
        sf.place(x=815,y=4,width=431,height=30)

        self.bill=Label(sf,text='Bill Number',font=('times new roman',10,'bold'),bg='red',fg='white')
        self.bill.grid(row=0,column=0,sticky=W,padx=7)

        self.bi=ttk.Entry(sf,textvariable=self.search_bill,font=('times new roman',10,'bold'),width=20)
        self.bi.grid(row=0,column=1,sticky=W,padx=5)

        self.bs=Button(sf,text='Search',command=self.find_bill,width=10,font=('times new roman',10,'bold'),bg='orangered',fg='white',cursor='hand2')
        self.bs.grid(row=0,column=2,padx=5)


 #BILL AREA
        right=LabelFrame(mainf,text='Billing Section',font=('times new roman',10,'bold'),bg='white',foreground='red')
        right.place(x=815,y=35,width=431,height=370)

        scroll_y=Scrollbar(right,orient=VERTICAL)
        self.textarea=Text(right,yscrollcommand=scroll_y.set,bg='white',fg='blue',font=('times new roman',10,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=TRUE)
  
  # #####################BILL COUNTER###############
        bottom=LabelFrame(mainf,text='Bill Counter',font=('times new roman',10,'bold'),bg='white',foreground='red')
        bottom.place(x=0,y=405,width=1260,height=95)

        
        self.subtotal=Label(bottom,text='Sub Total',font=('times new roman',10,'bold'),bg='white')
        self.subtotal.grid(row=0,column=0,sticky=W,padx=4,pady=2)

        self.entry=ttk.Entry(bottom,textvariable=self.sub_total,font=('times new roman',10,'bold'),width=20)
        self.entry.grid(row=0,column=1,sticky=W,padx=4,pady=2)

        self.tax=Label(bottom,text='GST',font=('times new roman',10,'bold'),bg='white')
        self.tax.grid(row=1,column=0,sticky=W,padx=4,pady=2)

        self.entry1=ttk.Entry(bottom,textvariable=self.taxes,font=('times new roman',10,'bold'),width=20)
        self.entry1.grid(row=1,column=1,sticky=W,padx=4,pady=2)

        self.total=Label(bottom,text='Total',font=('times new roman',10,'bold'),bg='white')
        self.total.grid(row=2,column=0,sticky=W,padx=4,pady=2)

        self.entry2=ttk.Entry(bottom,textvariable=self.totals,font=('times new roman',10,'bold'),width=20)
        self.entry2.grid(row=2,column=1,sticky=W,padx=4,pady=3)
        


########################BUTTON######################################
        bf=Frame(bottom,bd=2,bg='white')
        bf.place(x=300,y=0)

        self.b1=Button(bf,text='Add To Cart',command=self.additem,height=2,width=18,font=('times new roman',10,'bold'),bg='orangered',fg='white',cursor='hand2')
        self.b1.grid(row=0,column=0,padx=5)

        self.b2=Button(bf,text='Generate Bill',command=self.gen_bill,height=2,width=18,font=('times new roman',10,'bold'),bg='orangered',fg='white',cursor='hand2')
        self.b2.grid(row=0,column=1,padx=5)

        self.b3=Button(bf,text='Save Bill',command=self.save_bill,height=2,width=18,font=('times new roman',10,'bold'),bg='orangered',fg='white',cursor='hand2')
        self.b3.grid(row=0,column=2,padx=5)

        self.b4=Button(bf,text='Print',command=self.iprint,height=2,width=18,font=('times new roman',10,'bold'),bg='orangered',fg='white',cursor='hand2')
        self.b4.grid(row=0,column=3,padx=5)

        self.b5=Button(bf,text='Clear',command=self.clear,height=2,width=18,font=('times new roman',10,'bold'),bg='orangered',fg='white',cursor='hand2')
        self.b5.grid(row=0,column=4,padx=5)
        
        self.b6=Button(bf,text='Exit',command=self.root.destroy,height=2,width=18,font=('times new roman',10,'bold'),bg='orangered',fg='white',cursor='hand2')
        self.b6.grid(row=0,column=5,padx=5)
        self.welcome()


        self.l=[]

    





        
######################FUNCTION DECLARATION#################

#############welcome page on billing section##############
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,'\tWelcome To The Mini Mall ')
        self.textarea.insert(END,f'\n Bill Number:{self.bill_no.get()} ')
        self.textarea.insert(END,f'\n Customer Name:{self.cnsme.get()} ')
        self.textarea.insert(END,f'\n Phone Number:{self.cphon.get()} ')
        self.textarea.insert(END,f'\n Customer Email:{self.cemail.get()} ')

        self.textarea.insert(END,'\n =========================================================\n')
        self.textarea.insert(END,f'\nProducts\t\t\tQunatity\t\t\tPrice')
        self.textarea.insert(END,'\n==========================================================\n')

        #############add button############
    def additem(self):
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=='':
            messagebox.showerror('Error','Please select the product name')
        else:
            self.textarea.insert(END,f'\n    {self.product.get()}\t\t{self.qty.get()}\t\t{self.prices.get()}\t')   
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l)))) 
            self.taxes.set(str('Rs.%.2f'%((((sum(self.l))*0.5)/100))))
            self.totals.set(str('Rs.%.2f'%((sum(self.l))+((sum(self.l))*3/100))))
            #self.totals.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*23)/100)))))

    

#####to generate bill######
    def gen_bill(self):
        if self.product.get()=='':
            messagebox.showerror('Error','Please select the proct name')
        else:
            text=self.textarea.get(9.0,(9.0+float(len(self.l))))  #9.0 is the 9th line from printing is to be start
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,'\n=======================================================')
            self.textarea.insert(END,f'\n Sub Amount:\t\t\t{self.sub_total.get()}')
            self.textarea.insert(END,f'\n Tax Amount:\t\t\t{self.taxes.get()}')
            self.textarea.insert(END,f'\n Total Amount:\t\t\t{self.totals.get()}')
            self.textarea.insert(END,'\n=======================================================')
 
 #####to save bill######
    def save_bill(self):
        op=messagebox.askyesno('Save Bill','Do you want to save will?')
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('C:/Users/KOMAL/Desktop/wd/mypython/project/bills/'+str(self.bill_no.get())+'.txt','w')
            f1.write(self.bill_data)
            messagebox.showinfo('Saved',f'Bill No: {self.bill_no.get()} is saved successfully')
            f1.close()
   #####to print bill######  
    def iprint(self):
        q=self.textarea.get(1.0,END)
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'print')

#############to clear$#############
    def clear(self):
        self.textarea.delete(1.0,END)
        self.cnsme.set('')
        self.cphon.set('')
        self.bill_no.set(0)
        x=random.randint(1000,9999)
        self.bill_no.set(x)
        self.cemail.set('')
        self.search_bill.set('')
        self.product.set('')
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set('')
        self.taxes.set('')
        self.totals.set('')
        self.welcome()
   
###############for searching$######################
    def find_bill(self):
        found='no'
        for i in os.listdir('C:/Users/KOMAL/Desktop/wd/mypython/project/bills/'):
            if i.split('.')[0]==self.search_bill.get():     
            #to take only bill no except .txt extnsio##
                f1=open(f'C:/Users/KOMAL/Desktop/wd/mypython/project/bills/{i}')
                self.textarea.delete(1.0,END)
                for d in f1:
                  self.textarea.insert(END,d)
                f1.close()
                found='yes'
        if found=='no':
                messagebox.showerror('Error','Bill no. is invalid!!')
     


##########adding dependecies between cat and subcat combobox################
    def categories(self,event=''):
        if self.cc.get()=='Clothing':
             self.cs.config(values=self.subclothing)
             self.cs.current(0)
        
        if self.cc.get()=='Lifestyle':
             self.cs.config(values=self.sublife)
             self.cs.current(0)

        if self.cc.get()=='Mobile':
             self.cs.config(values=self.submobile)
             self.cs.current(0)  

                

            


##########adding dependecies between product and subcat combobox  ################
    def product_add(self,event=''):
        #for clothing
        if self.cs.get()=='Pant':
            self.cp.config(values=self.pant)
            self.cp.current(0)

        if self.cs.get()=='T-Shirt':
            self.cp.config(values=self.tshirt)
            self.cp.current(0)

        if self.cs.get()=='Shirt':
            self.cp.config(values=self.shirt)
            self.cp.current(0) 

        if self.cs.get()=='Jackets':
            self.cp.config(values=self.jacket)
            self.cp.current(0)           
  # for lifestyle ################ 
        if self.cs.get()=='Bathsoap':
            self.cp.config(values=self.bathsoap)
            self.cp.current(0)

        if self.cs.get()=='FaceCream':
            self.cp.config(values=self.facecream)
            self.cp.current(0)

        if self.cs.get()=='Hair Oil':
            self.cp.config(values=self.hair)
            self.cp.current(0) 

        if self.cs.get()=='Shampoo':
            self.cp.config(values=self.shampoo)
            self.cp.current(0)     

        if self.cs.get()=='Facewash':
            self.cp.config(values=self.facewash)
            self.cp.current(0) 
        
        if self.cs.get()=='Perfumes':
            self.cp.config(values=self.perfumes)
            self.cp.current(0) 
#########for mobiles####
        if self.cs.get()=='Iphone':
            self.cp.config(values=self.iphone)
            self.cp.current(0) 

        if self.cs.get()=='Samsung':
            self.cp.config(values=self.samsung)
            self.cp.current(0)     

        if self.cs.get()=='Xiaomi':
            self.cp.config(values=self.Xiaomi)
            self.cp.current(0) 
        
        if self.cs.get()=='One Plus':
            self.cp.config(values=self.oneplus)
            self.cp.current(0)



##########adding dependecies between product and price combobox  ################
    def pricez(self,event=''):
        ######pants#
        if self.cp.get()=='Levis':
            self.cpr.config(values=self.price_levis) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)

        if self.cp.get()=='Roadster':
            self.cpr.config(values=self.price_roadster) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Off Dutty':
            self.cpr.config(values=self.price_offduty) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)
############for tshirts######
        if self.cp.get()=='U.S. Polo':
            self.cpr.config(values=self.price_us) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Roadster':
            self.cpr.config(values=self.price_road) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Jack&Jones':
            self.cpr.config(values=self.price_jack) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)
############for shirts######
        if self.cp.get()=='Peter England':
            self.cpr.config(values=self.price_peter) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Park Avenue':
            self.cpr.config(values=self.price_park) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Louis Vuition':
            self.cpr.config(values=self.price_louis) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)

############for shirts######
        if self.cp.get()=='Roadster':
            self.cpr.config(values=self.price_roads) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Safaras':
            self.cpr.config(values=self.price_safaras) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)


############Bathsoap######
        if self.cp.get()=='Lux':
            self.cpr.config(values=self.price_lux) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Dove':
            self.cpr.config(values=self.price_dove) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Johnson Baby':
            self.cpr.config(values=self.price_baby) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)            

############for Fcaecream######
        if self.cp.get()=='Foxtale':
            self.cpr.config(values=self.price_fox) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Nivea':
            self.cpr.config(values=self.price_nivea) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Lakme':
            self.cpr.config(values=self.price_lakme) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 

############for hair oil######
        if self.cp.get()=='Indulekha':
            self.cpr.config(values=self.price_indu) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Almond Oil':
            self.cpr.config(values=self.price_almond) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Rosemarry':
            self.cpr.config(values=self.price_rose) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)

############for hair shampoo######
        if self.cp.get()=='Indu-lekha':
            self.cpr.config(values=self.price_in) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Hair Essence':
            self.cpr.config(values=self.haire) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Dove s':
            self.cpr.config(values=self.price_dovee) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)
############for facewasho######
        if self.cp.get()=='Fox-tale':
            self.cpr.config(values=self.price_foxtale) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Wow':
            self.cpr.config(values=self.price_wow) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Himalayan':
            self.cpr.config(values=self.price_him) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)

############for perfume######
        if self.cp.get()=='Watta Girl':
            self.cpr.config(values=self.price_watta) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Bella Vita':
            self.cpr.config(values=self.price_bella) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Blue Hommie':
            self.cpr.config(values=self.price_blue) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)
############for mobiles iphone 11######
        if self.cp.get()=='iphone11':
            self.cpr.config(values=self.price_i11) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='iphone12':
            self.cpr.config(values=self.price_i12) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='iphone13':
            self.cpr.config(values=self.price_i13) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)
        if self.cp.get()=='iphone14':
            self.cpr.config(values=self.price_i14) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)

            self.qty.set(1)
############for mobiles samsung######
        if self.cp.get()=='New Galaxy Z':
            self.cpr.config(values=self.price_s1) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Galaxy M14':
            self.cpr.config(values=self.price_s2) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Galaxy A35':
            self.cpr.config(values=self.price_s3) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)
############for mobiles xiomi######
        if self.cp.get()=='Redmi Note 13':
            self.cpr.config(values=self.price_r1) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='Redmi Note 13Pro':
            self.cpr.config(values=self.price_r2) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='Redmi 14 Civi':
            self.cpr.config(values=self.price_r3) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)

############for mobiles one plus######
        if self.cp.get()=='One Plus 9 Pro':
            self.cpr.config(values=self.price_o1) # type: ignore
            self.cpr.current(0)
            self.qty.set(1) 
        if self.cp.get()=='One Plus 9R':
            self.cpr.config(values=self.price_o2) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)   

        if self.cp.get()=='One Plus Nord CE':
            self.cpr.config(values=self.price_o3) # type: ignore
            self.cpr.current(0)
            self.qty.set(1)

        
if __name__ == '__main__':
    root=Tk()
    obj=bill_app(root)
    root.mainloop()
        