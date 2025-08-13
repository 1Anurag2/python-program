import os

# Get current working directory
print(os.getcwd())  

# Change directory
# os.chdir('name')

# List files in current directory
# print(os.listdir("chapter"))

# Make a new directory
# os.mkdir("data")

# Remove a directory
# os.rmdir("new_folder")

# for i in range(1, 10):
#     os.mkdir(f"data/folder_{i}")
#     i += 1

#Rename the file
for i in range(5, 10):
    os.rmdir(f"data/tutorial_{i}")
    i += 1

# List all folders in the "data" directory
folders = os.listdir("data")

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))




