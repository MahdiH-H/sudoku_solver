def show_dictionary(dictionary):
    keys=list(dictionary.keys())
    valus=list(dictionary.values())
    print("{")
    i=0
    for key in keys:
        print(f'{key} : {valus[i]}')
        i+=1
    print("}")

def inopen(open,node):
    for n in open:
        if n[0]==node: return True
    return False

def inclose(close,node):
    for n in close:
        if n[0]==node: return True
    return False

def heuristic(bord_info):
    max=0
    for x in bord_info.keys():
        if len(bord_info[x])>max:
            max=len(bord_info[x])
    h=0
    waight=0.1
    for i in range(1,max+1):
        for x in bord_info.keys():
            if len(bord_info[x])==0:
                return 1000
            if len(bord_info[x])==i:
                h+=waight
        waight+=0.1
    return h

def get_h(graph,node): return graph[node]["H"]

def get_min_h(opened):
    x=opened[0]
    for n in opened:
        if x[2]>n[2]:
            x=n
    return x
