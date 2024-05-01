class FileOpener:

    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileOpener("file.txt", "r") as f:
    f.read()
    
    
