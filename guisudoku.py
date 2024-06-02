import tkinter
from tkinter import ttk
from main import algorithmA
from Sudokuclass import Sudoku

def init_bord(celles):
    bord=[]
    for r in celles:
        ro=[]
        for c in r:
            text=c.get(1.4, "end-1c")
            if text=='':
                ro.append(None)
            else:
                ro.append(int(text))
        bord.append(ro)
    return bord

def solve(celles):
    bord=init_bord(celles)
    S=Sudoku(bord)
    valu=S.generat_value_of_stat()
    graph={S:valu}
    info=algorithmA(graph,S)
    goal=info["pathe"][-1].bord
    i=0
    for row in celles:
        j=0
        for cell in row:
            cell.delete("1.0","end")
            cell.insert(index='end',chars='    '+str(goal[i][j]))
            j+=1
        i+=1
    massag=f"The number of nodes in the closed list : {len(info['closed'])}\n"
    massag+=f"The number of nodes in the opened list : {len(info['opend'])}\n"
    massag+=f"The number of steps taken to solve : {len(info['pathe'])-1}"
    label=ttk.Label(window,text=massag,font=('Helvetica bold', 18))
    label.grid(row=10,column=0,columnspan=9)

window=tkinter.Tk()
window.title('Sudoku')
window.geometry('600x570')
entry=ttk.Entry(window)


window.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
window.columnconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)

celles=[]

for i in range(0,9):
    row=[]
    for j in range(0,9):
        
        celle=tkinter.Text(window,font=16,height=0)
        celle.grid(row=i,column=j,pady=0,sticky="nsew")
        row.append(celle)
    celles.append(row)

bord1=[
        [8,1,None,9,None,None,None,None,3],
        [None,3,4,None,None,None,None,6,None],
        [None,None,None,None,4,None,5,None,None],
        [None,5,None,8,None,4,None,None,None],
        [1,4,9,None,None,None,None,None,8],
        [None,8,None,2,None,7,None,None,None],
        [None,None,None,None,5,None,8,None,None],
        [None,2,5,None,None,None,None,7,None],
        [7,9,None,6,None,None,None,None,5]
    ]

bord2=[
        [None,None,9,None,None,None,6,5,1],
        [None,4,None,None,6,9,None,None,None],
        [None,None,None,None,None,8,None,7,None],
        [5,None,None,2,None,None,None,None,None],
        [None,None,None,None,8,None,None,9,None],
        [None,3,2,None,4,None,None,None,None],
        [None,None,None,6,None,None,None,None,None],
        [2,None,7,3,5,None,None,6,None],
        [None,None,None,None,None,None,3,None,None]
    ]

i=0
for r in bord2:
    j=0
    for c in r:
        if c==None:
            celles[i][j].insert(index='end',chars='\t   '+str())
        else:
            celles[i][j].insert(index='end',chars='\t   '+str(c))
        j+=1
    i+=1

button=ttk.Button(window,text="solve",width=1,command=lambda : solve(celles))
button.grid(row=9,column=4,columnspan=1,sticky="nsew")

window.mainloop()