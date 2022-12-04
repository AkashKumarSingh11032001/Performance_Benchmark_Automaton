dictionary = {'geek': 1, 'abc': True, 4: 'geeky'}
  

geeky_file = open('FioScriptExtractor\\geekyfile.txt', 'wt')
for i in dictionary:
    x = str(i)+"="+str(dictionary[i])+"\n"
    geeky_file.write(x)
    
geeky_file.close()
