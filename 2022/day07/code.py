class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirectories = []
        self.files = []
        self.size = None

    def print_out(self, depth):
        print(depth, self.name + " (dir)")
        for subdir in self.subdirectories:
            subdir.print_out(depth + 1)
        for file in self.files:
            file.print_out(file, depth + 1)

    def get_size(self):
        if self.size is None:
            self.size = 0
            for subdir in self.subdirectories:
                self.size += subdir.get_size()
            for file in self.files:
                self.size += file.size
        return self.size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def print_out(self, depth):
        print(depth, self.name, self.size)


def get_directory(root_dir, dir_name):
    for directory in root_dir.subdirectories:
        if directory.name == dir_name:
            return directory
    return None


def get_file(root_dir, file_name):
    for file in root_dir.files:
        if file.name == file_name:
            return file
    return None


root = Directory("/", None)
currentDirectory = root
with open('input.txt') as data:
    for line in data.readlines():
        lineData = line.split(" ")
        if lineData[0] == "$":
            if lineData[1] == "cd":  # can ignore ls
                targetDir = lineData[2].strip()
                if targetDir == "/":
                    currentDirectory = root
                elif targetDir == "..":
                    if currentDirectory.parent is not None:
                        currentDirectory = currentDirectory.parent
                else:
                    navigatedDirectory = get_directory(currentDirectory, targetDir)
                    if navigatedDirectory is not None:
                        currentDirectory = navigatedDirectory
        elif lineData[0] == "dir":  # add dir
            directoryName = lineData[1].strip()
            if get_directory(currentDirectory, directoryName) is None:
                newDirectory = Directory(directoryName, currentDirectory)
                currentDirectory.subdirectories.append(newDirectory)
        else:  # add file
            fileName = lineData[1].strip()
            fileSize = lineData[0]
            if get_file(currentDirectory, fileName) is None:
                newFile = File(fileName, fileSize)
                currentDirectory.files.append(newFile)

print("Part 1:")
maxSize = 100000


def recursive_count_size(dir, maxSize):
    totalSize = 0
    if dir.get_size() < maxSize:
        totalSize += dir.get_size()
    for subdir in dir.subdirectories:
        totalSize += recursive_count_size(subdir, maxSize)
    return totalSize


print(recursive_count_size(root, maxSize))

print("Part 2:")
totalSize = 70000000
minSizeToDelete = 30000000 - (totalSize - root.get_size())


def recursive_find_smallest(dir, minSizeToDelete, currentSmallest):
    if minSizeToDelete <= dir.get_size() < currentSmallest.get_size():
        currentSmallest = dir
    for subdir in dir.subdirectories:
        currentSmallest = recursive_find_smallest(subdir, minSizeToDelete, currentSmallest)
    return currentSmallest


print(recursive_find_smallest(root, minSizeToDelete, root).get_size())
