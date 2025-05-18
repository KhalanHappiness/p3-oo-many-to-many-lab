class Author:
    all = []
    def __init__(self, name = ""):
        self.name = name
        Author.all.append(self)
        pass
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        return sum(contract.royalties for contract in Contract.all if contract.author == self)

        


    pass


class Book:
    all = []
    def __init__(self, title =""):
        self.title = title
        Book.all.append(self)
        pass

    def contracts(self):
        return [contracts for contracts in Contract.all if contracts.book ==  self]
    
    def authors(self):
        return [contracts.author for contracts in Contract.all if contracts.book ==  self]
    

    pass


class Contract:
    all = []

    def __init__(self, author, book, date, royalties  ):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of author")
        self.author = author

        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of book")
        self.book = book

        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        self.date = date

        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        self.royalties = royalties

        Contract.all.append(self)




        
        self.date = date
        
        
        

        pass
    @classmethod
    def contracts_by_date(cls, date):
        return [contracts for contracts in cls.all if contracts.date == date]
    pass