from Sudokuclass import Sudoku
from allFunction import inclose,inopen,heuristic,get_h,get_min_h


def algorithmA(graph,start):
    opened=[[None,start,get_h(graph,start)]]
    closed=[]
    while(opened!=[]):
        leftmost=get_min_h(opened)
        opened.remove(leftmost)
        if leftmost[1].bord_info=={}:
            closed.append(leftmost)
            closed=list(reversed(closed))
            path=[]
            curnt=leftmost[1]
            for x in closed:
                if x[1]==curnt:
                    path=[curnt]+path
                    curnt=x[0]
            # return path
            info={"closed":closed,"opend":opened,"pathe":path}
            return info
        else:
            oldg=leftmost[2]-heuristic(leftmost[1].bord_info)
            for child in graph[leftmost[1]]["childs"]:
                if (not inopen(opened,child[0])) and (not inclose(closed,child[0])):
                    h=heuristic(child[0].bord_info)
                    g=oldg+child[1]
                    f=g+h
                    opened.append([leftmost[1],child[0],f])
                    graph[child[0]]=child[0].generat_value_of_stat()

        closed.append(leftmost)   
    
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
        [None,2,None,8,None,None,None,None,5],
        [None,None,9,3,None,None,None,None,8],
        [None,3,None,None,None,None,None,4,None],
        [6,None,None,None,None,None,None,None,1],
        [2,9,None,1,8,5,None,None,None],
        [None,None,None,None,None,6,3,None,9],
        [1,None,None,2,None,3,6,None,None],
        [None,None,None,None,9,None,5,None,None],
        [None,4,None,None,None,None,8,7,3]
    ]

bord3=[
        [None,None,2,None,4,3,None,None,8],
        [None,3,None,8,None,None,None,9,None],
        [4,None,None,None,5,7,3,None,None],
        [None,6,5,None,None,None,None,3,7],
        [1,None,None,None,None,None,2,None,None],
        [None,2,4,None,None,None,None,1,9],
        [None,None,6,None,3,8,None,None,1],
        [None,None,None,6,None,None,None,8,None],
        [5,None,None,None,7,9,6,None,None]
    ]

bord4=[
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

bord5=[
        [None,None,None,None,9,None,None,5,None],
        [None,8,5,4,None,None,None,None,None],
        [4,None,6,None,None,None,1,None,8],
        [None,7,None,None,4,None,9,None,5],
        [None,None,None,1,7,None,3,8,None],
        [6,None,None,8,None,None,None,None,None],
        [1,None,None,9,None,3,None,None,None],
        [9,6,7,2,None,5,8,4,None],
        [None,3,8,7,None,4,2,1,9]
    ]

# if you wanna print the solution on consle

S=Sudoku(bord5)
valu=S.generat_value_of_stat()
graph={S:valu}
pathe=algorithmA(graph,S)
for x in pathe:
    for y in x.bord:
        print(y)
    print('\n')