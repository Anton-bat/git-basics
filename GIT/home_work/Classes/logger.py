

class Logger:

    def __init__(self, log_level) -> None:
        self.log_level = log_level
    
    def __call__(self, message):
        print(f'{self.log_level}: {message}')
    
logger = Logger("Info")
logger("Something happened")