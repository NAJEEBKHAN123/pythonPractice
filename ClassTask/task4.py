filename = 'simple.txt'

class TextProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []
        
        
    
    def read_file(self):
        
        try:
            with open(self.filename, 'r') as file:
                self.lines = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"Error: file {self.filename} not found")
            self.lines = []
        
    def process(self):
        for line in self.lines:
            print(line)

class LineNumberPerTextProcessor(TextProcessor):
    
    def process(self):
        for idx, line in enumerate(self.lines, start=1):
            print(f"{idx} : {line}")
            
        
        
p = LineNumberPerTextProcessor(filename)
p.read_file()
p.process()

        
        
        
    
    

p = TextProcessor('simple.txt')
p.read_file()
p.process()
