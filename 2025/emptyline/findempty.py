with open( 
    "linefile.txt", 'r') as r, open( 
        'output.txt', 'w') as o: 
      
    for line in r: 
        #strip() function 
        if line.strip(): 
            o.write(line) 
  
f = open("output.txt", "r") 
print("New text file:\n",f.read())