try:
    with open("C:\\Users\\anura\\Documents\\python.txt","r") as f2:
        with open("C:\\Users\\anura\\Documents\\write.txt","w") as f3:
            for i in f2:
                f3.write(i)
except:
    print("file not found...")

else:
    f2.close()
    print("File closed...")

