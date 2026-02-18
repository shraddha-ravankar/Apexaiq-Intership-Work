def write_file():
    """
    Writes data to a file using write mode
    """
    file = open("example.txt", "w")
    file.write("Python File Handling\n")
    file.write("This is write mode\n")
    file.close()


write_file()

# read data from file using read mode
def read_file():
    file = open("example.txt", "r")
    content=file.read()
    print(content)
    file.close()

read_file()

def append_file():
    """
    Appends data to a file using append mode
    """
    file = open("example.txt", "a")
    file.write("This line is added later\n")
    file.close()


append_file()


def read_all_lines():
    """
    Reads all lines from file using readlines()
    """
    file = open("example.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        print(line.strip())


read_all_lines()



def write_lines_example():
    """
    Writes multiple lines to a file using writelines()
    """
    lines = [
        "Python\n",
        "File Handling\n",
        "Using writelines method\n"
        "shraddha ravankar"
    ]

    file = open("example.txt", "a")
    file.writelines(lines)
    file.close()


write_lines_example()




def write_binary():
    """
    Writes binary data to a file using wb mode
    """
    data = b"Hello Python Binary"

    file = open("binary_file.bin", "wb")
    file.write(data)
    file.close()


write_binary()


# def copy_image():
#     """
#     Copies an image file using binary mode
#     """
#     source = open("input.jpg", "rb")
#     destination = open("output.jpg", "wb")

#     data = source.read()
#     destination.write(data)

#     source.close()
#     destination.close()


# copy_image()
