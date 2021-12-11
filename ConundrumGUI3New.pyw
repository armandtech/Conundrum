from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Conundrum")

only = StringVar()


def clear():
    global ff
    ff = 0
    entry.focus()
    entry.delete(0, END)
    for i in xx:
        i.delete(0, END)

def key(event):
    global ff
    if ff == 13:
        search.focus()
        
    try:
        ents = xx[ff]
        ff+=1
        ents.focus()

    except IndexError:
        pass

ff = 0 #entry counter

def calc(*args):
    res.delete(0, END)
    fex = 0
    longst = ['a',]
    lets = [] #letters will be read from here
    
    apwords = []
    for singlelet in str(only.get()):
        lets.append(singlelet) #appends each letter that is typed in as a list objest

    try:
        def letr(arg):
            x = 0
            for ii in lets:
                if ii in arg and ii != ' ':
                    ct = arg.count(ii)
                    lt = lets.count(ii)
                    if ct >= lt:
                        x+=1
                    elif ct < lt:
                        ttt = ct/lt
                        ttt += 0.0001
                        x+=ttt
                                
            if x >= len(arg):
                apwords.append(arg)
                
                if len(arg) > len(longst[0]): #longest word
                    longst.remove(longst[0])
                    longst.append(arg)
                x = 0
                return
            else:
                x = 0
                return

    except ValueError:
        pass
    
    list1 = []
    di = []

    tet = list(open('newdict.txt')) #opens as tet
    for theline in tet:
        list1.append(theline) #appends the 'list' of dict words to list1
        
    negnums = eval(list1[0]) #fuck knows why, cant remember, but after eval it is placed into yet another list called di
    di.append(negnums)
    
    di[0] = [wo.rstrip() for wo in di[0]]
    for i in di[0]:
        letr(i)

    for item in apwords:
        res.insert(END, item)
        fex += 1

    nofou.configure(text=fex)
    longword.configure(text=longst[0])
    fex = 0
    global ff
    ff = 0


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

mainframe2 = ttk.Frame(root, padding="3 3 12 12")
mainframe2.grid(column=0, row=3, sticky=(N, W, E, S))
mainframe2.columnconfigure(0, weight=1)
mainframe2.rowconfigure(0, weight=1)

canvas = Canvas(mainframe2, width =22, height=8)
canvas.grid(column=0, row=0, sticky=W)

canvas2 = Canvas(mainframe2, width =22, height=15)
canvas2.grid(column=1, row=0, sticky=W)

nofou = ttk.Label(canvas2, text="0")
nofou.grid(column=0, row=1, sticky=(W, E))
longword = ttk.Label(canvas2, text="----")
longword.grid(column=0, row=4, sticky=(W, E))
ttk.Label(canvas2, text="Longest Word:").grid(column=0, row=3, sticky=(W, E))
ttk.Label(canvas2, text="Words Found:").grid(column=0, row=0, sticky=(W, E))


res = Listbox(canvas, height=6, width=20)
scroll = Scrollbar(canvas, command=res.yview)
res.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
res.pack()

entry = ttk.Entry(mainframe, width=22, textvariable=only)
entry.grid(column=0, row=1, sticky=W)

search = ttk.Button(mainframe, text="Search", command=calc)
search.grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="Clear", command=clear).grid(column=4, row=1, sticky=W)

xx = [entry,]

entry.focus()

root.bind("<Key>", key)
root.bind('<Return>', calc)
root.mainloop()
