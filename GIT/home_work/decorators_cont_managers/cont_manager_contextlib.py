from contextlib import contextmanager

@contextmanager

def file_opener(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()


with file_opener("file.txt", "r") as f:
    print(f.read())
    
    
