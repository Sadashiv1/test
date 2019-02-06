'''The observed PIN'''
'''Each digit could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could be the 2, 4, 6 or 8.'''





def get_pins(observed):
    if len(observed)==1:
        return possiblenumbers(observed)
    else:
        arr=[]
        arr1 = get_pins(observed[0:-1])
        for n in range(len(arr1)):
            poss = possiblenumbers(observed[-1])
            for m in range (len(poss)):
                arr.append("".join([arr1[n],poss[m]]))
        return arr

def possiblenumbers(num):
    if num== '0': return ['0', '8'] 
    elif num == '1': return ['1', '2', '4']
    elif num == '2': return ['1', '2', '3', '5']
    elif num == "3": return ['3', '2', '6']
    elif num == '4': return ["1", "5", "4","7"]
    elif num == "5": return ["5", "2", "4", "6","8"]
    elif num == "6": return ["3","6","9","5"]
    elif num == "7": return ["7", "8", "4"]
    elif num == "8": return ["5","7","8","9","0"]
    else: return ['6','8','9']
    
