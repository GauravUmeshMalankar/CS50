# command line arguments
# means take input from command prompt/terminal

from sys  import argv

if (len(argv)) == 2:
    print(f"Hello,{argv[1]}")
else:
    print(f"Hello,world")
