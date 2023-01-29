import shutil,os

original = r'C:\Users\1000300665\Desktop\FVT\PBM\Performance_Benchmark_Automaton__\practice\a.txt'
target = r'C:\Users\1000300665\Desktop\FVT\PBM\Performance_Benchmark_Automaton__\practice\lg\bb\mm\tt'

path = target
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist: 
   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory with is created!")

c = "bt.txt"
path =  "{0}\{1}".format(path,c)
shutil.copyfile(original, path)