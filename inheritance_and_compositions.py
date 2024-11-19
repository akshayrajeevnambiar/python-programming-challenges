# Challenge: Create a class strucure to represent stocks and bonds
# Requirements:
# -- Both the stocks and bonds have a price
# -- Stocks have a company name and a ticker
# -- Bonds have a description, duration, and yeild
# -- You should not be able to instantiate the base class
# -- Subclasses are required to override the get_description()
# -- get_description returns formats for stocks and bonds
# For stocks: "Ticker: Company -- $Price"
# For Bonds: "Description: description'yr' : $price : yeildamt%"

from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        super().__init__()
        self.price = price

    @classmethod
    @abstractmethod
    def get_description(self):
        pass

class Stock(Asset):
    def __init__(self, companyName, price, ticker):
        super().__init__(price)
        self.companyName = companyName
        self.ticker = ticker

    def get_description(self):
        return f"{self.ticker}: {self.companyName} -- ${self.price}"

class Bond(Asset):
    def __init__(self, price, description, duration, yeild):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yeild = yeild

    def get_description(self):
        return f"{self.description}: {self.duration}'yr' : ${self.price} : {self.yeild}%"

# ----------------- TEST CODE ------------------
try:
    ast = Asset(100.0)
except:
    print("Cant instatiate Asset")

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("amzn", 137.0, "Amazon Inc")

us30yr = Bond(95.31, "30 Year US Treasury", 30, 4.38)
us10yr = Bond(96.70, "10 Year US Treasury", 10, 4.28)
us5yr = Bond(98.65, "5 Year US Treasury", 5, 4.43)
us2yr = Bond(99.57, "2 Year US Treasury", 2, 4.98)

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())

print(us30yr.get_description())
print(us10yr.get_description())
print(us5yr.get_description())
print(us2yr.get_description())

