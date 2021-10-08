def reverse(x):
    # print(x)
    strlist = []
    numlist = []
    n = [0,1,2,3,4,5,6,7,8,9]

    for i in x:
       #print(i)

        if i in n :
           numlist.append(i)

        else:
            strlist.append(i)
    numlist.reverse()
    print(numlist + strlist)
    #return numlist + strlist



if __name__ == '__main__':
    s = [1,2,3,4,5,'NULL']
    reverse(s)