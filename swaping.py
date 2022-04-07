def swapFileData():
    
    file1=input('enter the file name')
    data_b=input('file1')
    data_a=input('file2')
      
    with open(file1,'r')as a:
        data_a=data_a.read()
    with open(file1,'r')as a:
        a.write(data_b)
    
    data_a=file1.read()
    data_b=file1.read()
   
    
    


    
swapFileData()

