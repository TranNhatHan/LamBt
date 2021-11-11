class Customer:

    def __init__(self,name:str,address):
        self.name = name
        self.address = address

class Order:

    def __init__(self,date,status:str):
        self.date = date
        self.status = status

    def calcSub_Total(self):
        pass

    def calcTax(self):
        pass

    def calcTotal(self):
        pass

    def calcTotalWeight(self):
        pass

class OrderDetail:

    def __init__(self,quantity:int,taxStatus:str):
        self.quantity = quantity
        self.taxStatus = taxStatus

    def calcSub_Total(self):
        pass

    def calcWeight(self):
        pass

    def calcTax(self):
        pass
class Item:

    def __init__(self,shippingWeight,description:str):
        self.shippingWeight = shippingWeight
        self.description = description

    def getPriceForQuanlity(self):
        pass

    def getTax(self):
        pass

    def inStock(self):
        pass

class Payment:

    def __init__(self,amount:float):
        self.amount=amount

class Cash(Payment):

    def __init__(self,amount:float,cashTendered:float):
        super.__init__(amount)
        self.cashTendered=cashTendered

class Check(Payment):

    def __init__(self,amount:float,name:str,bankID:str):
        super.__init__(amount)
        self.name=name
        self.bankID=bankID

    def athorized(self):
        pass

class Credit(Payment):

    def __init__(self,amount:float,number:str,type:str,expDate):
        super.__init__(amount)
        self.number=number
        self.type=type
        self.expDate=expDate

    def athorized(self):
        pass