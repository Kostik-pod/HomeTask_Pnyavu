with open('Class list.txt') as file:
    clas11 = []
    clas10 = []
    porog = []
    neporog = []
    allstr = file.readlines()
    num = range(0,len(allstr))
    for i in num:
        NCM = []
        pupil_name, clas, Mark = map(str,allstr[i].split(','))
        Mark = Mark.replace('n','')
        Mark = Mark.replace('\n','')
        Mark=[int(i) for i in Mark]
        NCM.append(pupil_name)
        if clas=='10':
            clas10.append(NCM)
        else:
            clas11.append(NCM)        
        NCM.append(sum(Mark)/len(Mark))
        if NCM[1]<2.5:
            neporog.append(NCM)
        else:
            porog.append(NCM)
with open('Sortlist.txt', 'w') as file:
    file.write('Порог перешли:\n')
    for i in range(len(porog)):
        if porog[i] in clas10:
            file.write(porog[i][0] + ',10,' + str(porog[i][1]) + '\n')
    for i in range(len(porog)):        
        if porog[i] in clas11:
            file.write(porog[i][0] + ',11,' + str(porog[i][1]) + '\n')
    file.write('\n')
    file.write('Порог не перешли:\n')
    for i in range(len(neporog)):
        if neporog[i] in clas10:
            file.write(neporog[i][0] + ',10,' + str(neporog[i][1]) + '\n')
    for i in range(len(neporog)):       
        if neporog[i] in clas11:
            file.write(neporog[i][0] + ',11, ' + str(neporog[i][1]) + '\n')
