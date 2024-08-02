try:
    with(open("C:\\Users\\anura\\OneDrive\\Desktop\\python\A.txt","r"))as f1:
        with(open("C:\\Users\\anura\\OneDrive\\Desktop\\python\\B.txt","w"))as f2:
            for line in f1:
                f2.write(line)
except:
    print("Error")

f2.close()
print("file closed...")