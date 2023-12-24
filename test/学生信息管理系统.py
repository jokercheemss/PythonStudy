class Book:
    def __init__(self,isbn,title,author,publisher):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
    def show(self):
        print("%16s %16s %16s %16s %16s" %(self.isbn,self.title,self.author,self.publisher))
