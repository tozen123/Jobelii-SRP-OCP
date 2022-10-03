'''
Single Responsibility Principle
Open-Closed Principle
'''

class Jobelii: # Main Class    
    def set_item(self, item, price, qty, taxRate):
        self.item = item
        self.price = price
        self.qty = qty
        self.taxRate = taxRate
        
class JobeliiCalculator:
    def calc_tax_rate (self, item):
        return item.price * item.taxRate

    def calc_order (self, item):
        return item.price * item.qty

class JobeliiPrintItem():
    def display (self, item):
        print (f'\nItem: {item.item}\nPrice: {item.price}\nTax Rate: {item.taxRate}\n')
        
class JobeliiPrintOrder(JobeliiCalculator):
    def display (self, item):
        print (f'\nItem: {item.item}\nPrice: {item.price}\nQty: {item.qty}\nTotal: {self.calc_order(item)}\n')
        
class JobeliiPrintTaxRate(JobeliiCalculator):
    def display (self, item):
        print (f'\nTax Rate: {self.calc_tax_rate(item)}\n')
    
order = Jobelii()
order.set_item('Borgir', 35.50, 3, 0.12)

printItem = JobeliiPrintItem().display(order)
printOrder = JobeliiPrintOrder().display(order)
printTax = JobeliiPrintTaxRate().display(order)