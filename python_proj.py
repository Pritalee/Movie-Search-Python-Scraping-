from tkinter import *
# from movi import *
#from bs4 import BeautifulSoup
#from selenium import webdriver
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# import movi
# from ScrolledText import ScrolledText
import tkinter.scrolledtext as st
root = Tk()
import tkinter as tk
n1 = StringVar()


class Start:

    # ro = 0
    # e1 = 0
    def __init__(self, root):
        self.root = root
        self.f = Frame(root, height=2000, width=2000)
        self.f.propagate(0)
        self.f.pack()
        self.b1 = Button(self.f, text="Start", font=('Times', -15, 'bold'), height=4, width=10, command=self.one)
        self.b1.grid(row=5, column=3)
        # self.b2 = Button(self.f, text="pageone", font=('Times', -15, 'bold'), height=4, width=10, command=self.one)
        # self.b2.grid(row=10, column=3)

    def one(self):
        root2 = Toplevel(self.root)
        next = PageOne(root2)


class PageOne(object):
    name = ""
#    mystring = StringVar()
    l2 = []
    l4 = []

    def __init__(self, root):
        self.root = root
        self.f = Frame(root, height=10000, width=10000)
        self.f.propagate(0)
        self.f.pack()
        # self.l1 = Label(self.f, text="enter movie name:", height=4, width=20, font=('Times', -15,))
        # self.l1.grid(row=0, column=0)
        # self.e1 = Entry(self.f, font=('Times', -15, 'bold'), width=25)
        # print(type(self.e1))
        # self.e1.grid(row=0, column=2)
        self.b1=Button(self.f,text="Search Movies", font=('Times', -15, 'bold'), height=3, width=20,command=self.two)
        self.b1.grid(row=5, column=3)
        self.b2 =Button(self.f, text="Search Actors/Actress", font=('Times', -15, 'bold'), height=3, width=20, command=self.four)
        self.b2.grid(row=10, column=3)

        #self.b2 = Button(self.f, text="PRINT", font=('Times', -30, 'bold'), height=2, width=8, command=self.two)
        #self.b2.grid(row=2, column=3)

    def two(self):
        # e1 = self.e1
        # b = str(self.e1)
        root3 = Toplevel(self.root)
        next1 = PageThree(root3)
        # next1.receive(PageOne.name)

    def four(self):
        # e1 = self.e1
        # b = str(self.e1)
        root3 = Toplevel(self.root)
        next1 = PageFour(root3)
        # next1.receive(PageOne.name)


class PageThree:

    def __init__(self,root):
        self.root = root

        self.mystring = StringVar()
        self.f = Frame(root, height=10000, width=10000)
        self.f.propagate(0)
        self.f.pack()
        self.l1 = Label(self.f, text="enter movie name:", height=4, width=20, font=('Times', -15, 'bold'))
        self.l1.grid(row=0, column=0)

        #self.e1 = Entry(self.f, font=('Times', -15, 'bold'), width=25)

        Entry(self.f, textvariable=n1).grid(row=0, column=2)
        # .grid(row=0, column=2)

        #print(self.mystring.get())
       # PageOne.name = self.mystring
       # n1=self.mystring

        self.b2 = Button(self.f,text="Search", font=('Times', -15, 'bold'), height=2, width=8, command=self.three)
        self.b2.grid(row=2, column=3)

        #self.b3 = Button(self.f,text="search", font=('Times', -15, 'bold'), height=4, width=8, command=self.getval)
        #self.b3.grid(row=4, column=6)

    def three(self):
        # e1 = self.e1
        # b = str(self.e1)
        root4 = Toplevel(self.root)
        next = PageTwo(root4)
        # return e1

    def getval(self):
        print(n1.get())


class PageFour:

    def __init__(self,root):
        self.root = root

        self.mystring = StringVar()
        self.f = Frame(root, height=10000, width=10000)
        self.f.propagate(0)
        self.f.pack()
        self.l1 = Label(self.f, text="enter actor name:", height=4, width=20, font=('Times', -15, 'bold'))
        self.l1.grid(row=0, column=0)

        #self.e1 = Entry(self.f, font=('Times', -15, 'bold'), width=25)

        Entry(self.f, textvariable=n1).grid(row=0, column=2)
        # .grid(row=0, column=2)

        #print(self.mystring.get())
       # PageOne.name = self.mystring
       # n1=self.mystring

        self.b2 = Button(self.f,text="Search", font=('Times', -15, 'bold'), height=2, width=8, command=self.three)
        self.b2.grid(row=2, column=3)

        #self.b3 = Button(self.f,text="search", font=('Times', -15, 'bold'), height=4, width=8, command=self.getval)
        #self.b3.grid(row=4, column=6)

    def three(self):
        # e1 = self.e1
        # b = str(self.e1)
        root4 = Toplevel(self.root)
        next = PageFive(root4)
        # return e1

    def getval(self):
        print(n1.get())


class action(PageOne):
    l2 = []
    t4 = []
    name = ''
    
    def __init__(self):
        self.l2 = []
        self.t4 = []
    
    def receive(self,b):
        action.name = b
    
    def work(self):
        driver=webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

        # str1 = input("enter movie name")

        # u1 = PageOne()
        # print(u1)
        # func(u1)
        str1 = n1.get()
        print(str1)
        str1 = str1.replace(' ', '_')
        url = "https://en.wikipedia.org/wiki/" + str1
        # print(url)

        driver.get(url)
        # print(driver.page_source)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        # t1 = soup.find('div', {'id': 'bodyContent'})
        # t2 = t1.find('div', {'id': 'mw-content-text'})
        t3 = soup.find('div', class_='mw-parser-output')
        self.t4 = t3.find_all('p')
        # assert isinstance(t1, object)
        for i in range(len(self.t4)):
            self.l2.append(self.t4[i].text)
            # print(t4[i].text)
        # print(self.l2)



class action1:
    l2=[]
    intro=[]
    def __init__(self):
        self.l2=[]
    def work(self):

        driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        str2 = n1.get()#input('enter the name')
        str2=str2.replace(" ", "_")
        str1 = 'https://en.wikipedia.org/wiki/' + str2

        driver.get(str1)
        ht = driver.page_source
        # print(ht)
        soup = BeautifulSoup(ht, 'lxml')

        # print(req.content)
        # table_classes = {"class": ["sortable", "plainrowheaders"]}
        wikitables = soup.find("div", class_='mw-parser-output')
        self.intro = wikitables.find_all('p')
        # print(wikitables)
        # self.l2.append(intro.text)
        for i in range(len(self.intro)):
            self.l2.append(self.intro[i].text)

class PageTwo:
    name = ''

    def receive(self, b):
       PageTwo.name = b

    def __init__(self, root):
        # self.root = root
        self.f1 = Frame(root, height=1000, width=1000)
        self.f1.propagate(0)
        self.f1.pack()
        # p1 = PageOne(root)
        # e = p1.two()
        # #print(e)
        act = action()
        act.receive(n1)
        act.work()
        l2 = act.l2
        #for i in range(len(act.t4)):
            #print(act.t4[i].text+"\n")

        self.t = st.ScrolledText(self.f1, width=100, height=100, font=('Verdana', -15, 'bold'), wrap='word')
        for i in range(len(l2)):
            self.t.insert(END, l2[i])
        self.t.pack()

'''
class starting:
    def __init__(self):
        root = Tk()
        fo = Start(root)
        root.mainloop()


startin = starting()
'''


class PageFive:
    name = ''

    def receive(self, b):
       PageFive.name = b

    def __init__(self, root):
        # self.root = root
        self.f1 = Frame(root, height=1000, width=1000)
        self.f1.propagate(0)
        self.f1.pack()
        # p1 = PageOne(root)
        # e = p1.two()
        # #print(e)
        act = action1()
        #act.receive(n1)
        act.work()
        l2 = act.l2
        # for i in range(len(act.t4)):
            # print(act.t4[i].text+"\n")

        self.t = st.ScrolledText(self.f1, width=100, height=100, font=('Verdana', -15, 'bold'), wrap='word')
        self.t.insert(END, l2)
        self.t.pack()


fo = Start(root)

root.mainloop()