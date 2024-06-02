from allFunction import heuristic
import copy
class Sudoku:
    bord=[]
    bord_info={}
    def __init__(self,bord):
        # initialize the bord for the opject
        self.bord=bord
        self.bord_info={}
        # loop through all the cells in the bord
        for i in range(0,9):
            for j in range(0,9):
                # if one of the cells have a value of none conclude the missing numbers in it
                if self.bord[i][j]==None:
                    mising_numbers=[1,2,3,4,5,6,7,8,9]
                    # for each celle in the same row and column
                    for m in range(0,9):
                        # if the celle don't have a value none then it have a number in it
                        # if that number is in missing_numbers, remove that number from the missing numbers
                        if self.bord[i][m]!=None and self.bord[i][m] in mising_numbers:
                            mising_numbers.remove(self.bord[i][m])

                        if self.bord[m][j]!=None and self.bord[m][j] in mising_numbers:
                                mising_numbers.remove(self.bord[m][j])

                    m=int(i/3)*3
                    n=int(j/3)*3
                    # the same thing in the previous block but for the cells in the same sub_grid
                    for x in range(m,m+3):
                        for y in range(n,n+3):
                            if self.bord[x][y]!=None and self.bord[x][y] in mising_numbers:
                                mising_numbers.remove(self.bord[x][y])
                    # after conclude the missing numbers for the celle with i,j index
                    # stor that in a dictionay, calle it bord_info 
                    self.bord_info[(i,j)]=mising_numbers
                # end of the block of code that conclude the missing numbers for the celle
        # end of iterations that loops through all the cells
    
    def mrv(self):
        rv_list=list(self.bord_info.values())
        indexs=list(self.bord_info.keys())
        if len(rv_list)==0:
            return None
        else:
            minmam=rv_list[0]
            for x in rv_list:
                if len(x)<len(minmam):
                    minmam=x
            if len(minmam)==0:
                return None
            else:
                return indexs[rv_list.index(minmam)]

    def generat_value_of_stat(self):
        valu_of_stat={}
        childs=[]
        celle=self.mrv()
        if celle==None:
            valu_of_stat={"childs":[], "H":1000}
            return valu_of_stat
        
        for mv in self.bord_info[celle]:
            newbord=copy.deepcopy(self.bord)
            i=celle[0]
            j=celle[1]
            newbord[i][j]=mv
            child=Sudoku(newbord)
            childs+=[[child,0]]
        valu_of_stat["childs"]=childs
        valu_of_stat["H"]=heuristic(self.bord_info)
        return valu_of_stat