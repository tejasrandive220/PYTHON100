class emp:
    
    def __init__(self):
        print('Employee created....')
  
    def __del__(self):
        print('Destructor called....')

obj = emp()
del obj