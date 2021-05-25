urls = "/home/mrasr/Desktop/story.txt"

files_load = open(urls)

files= files_load.readlines()

strd = ""


for i in files:
    correct = ""
    num = 0
    indexx = []
    while (num != -1):
        num += 1
        num = i.find("_",num)
        if num != -1:
            indexx.append(num)

        else:
            pass

    print(indexx)
    if (len(indexx)==1):
        correct = i[0:indexx[0]]+input()+i[(indexx[0]+1): ]
    else:
        correct = i[0:indexx[0]]+input()+i[(indexx[0]+1):indexx[1]]+input()+i[(indexx[1]+1):]
    print(correct)
                
                

    strd = strd + correct

print(strd)

    


    
                
            



    


