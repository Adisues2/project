
with open('nameslist.txt', 'r') as f:
    # for i in range(4):
    #    f.write("this is line: %i\n"%i)
    files = f.readlines()
    print(files)