def copyOneFileToOther(file1, file2):
    with open(file1, 'r') as firstfile, open(file2, 'w') as secondfile:
        for line in firstfile:
            secondfile.write(line)
