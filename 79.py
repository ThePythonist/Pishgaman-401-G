def myhash(x):
    if len(str(x)) == 1:
        return x
    else:
        x = sum([int(i) for i in str(x)])
        return myhash(x)


entry = int(input("Enter any number to hash : "))
print(myhash(entry))
