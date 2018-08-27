from tkinter import *
from tkinter import ttk


# Formula
# Investible amount / Unit price of share = Number of shares (input)
# No. of Shares X Unit Price of Share = Investible Amount (calculate)
# No. of Shares X Commission Per Share (default 0.1$) + Fixed Commission Amount (default 3$) = Total Commission Amount(calculate)
# Investible Amount + Total Commission Amount = Total Invested Plus Fee Cost (final output)


class GUI(object):

    def __init__ (self, window):
        self.window = window
        self.window.wm_title("Trade fee Calculator") 
        self.balanceLabel = ttk.Label( window, text = "Balance")
        self.investiableLabel = ttk.Label(window, text="Amount to Invest $")
        self.unitSharePriceLabel = ttk.Label(window, text="Unit price of share")
        self.shareNumberLabel = ttk.Label(window, text="Number of shares")
        self.shareCommissionLabel = ttk.Label(window, text="Commission Per Share $")
        self.fixedCommissionLabel = ttk.Label(window, text="Fixed Commission Amount $")
        self.totalCommissionLabel = ttk.Label(window, text="Total Commission Amount $")
        self.totalInvestedCostLabel = ttk.Label(window, text= "Total Invested Plus Fee Cost $")
        self.balanceAfterLabel = ttk.Label(window, text="Balance after")

        self.balanceEntry = ttk.Entry()
        self.investiableEntry = ttk.Entry()
        self.unitSharePriceEntry = ttk.Entry()
        self.shareNumberEntry = ttk.Entry()
        self.shareCommissionEntry = ttk.Entry()
        self.shareCommissionEntry.insert(0,'0.1')
        self.fixedCommissionEntry = ttk.Entry()
        self.fixedCommissionEntry.insert(0,'3')
        self.totalCommissionEntry = ttk.Entry()
        self.totalInvestedCostEntry = ttk.Entry()
        self.balanceAfterEntry = ttk.Entry()

        self.buttoncalNumShares = ttk.Button(window, text="Calculate Number of shares", 
        command=lambda:self.calNumShares(self.investiableEntry.get(),self.unitSharePriceEntry.get()))

        self.buttoncalInvestAmt = ttk.Button(window, text="Calculate Investiable amount",
        command=lambda:self.calInvestAmt(self.shareNumberEntry.get(),self.unitSharePriceEntry.get()))

        self.buttoncalCommissionAmt = ttk.Button(window, text="Calculate Total Commission amount", 
        command=lambda:self.calCommissionAmt(self.shareNumberEntry.get(),self.shareCommissionEntry.get(),self.fixedCommissionEntry.get()))
        
        self.buttoncalTotalinvestCost = ttk.Button(window, text="Calculate Total Invested Plus Fee Cost", 
        command=lambda:self.calTotalinvestCost(self.investiableEntry.get(),self.totalCommissionEntry.get()))

        self.buttoncalTotalinvestCostOneStep = ttk.Button(window, text="Calculate Total Invested Plus Fee Cost 1 step", 
        command=lambda:self.calTotalinvestCostOneStep(self.investiableEntry.get(),self.unitSharePriceEntry.get()))

        self.buttondelete=ttk.Button(window,text='Clear',width=10, command=lambda:self.clear())
        
        self.balanceLabel.pack()
        self.balanceEntry.pack()

        self.investiableLabel.pack()
        self.investiableEntry.pack()
        
        self.unitSharePriceLabel.pack()
        self.unitSharePriceEntry.pack()
        

        self.shareNumberLabel.pack()
        self.shareNumberEntry.pack()

        self.shareCommissionLabel.pack()
        self.shareCommissionEntry.pack()

        self.fixedCommissionLabel.pack()
        self.fixedCommissionEntry.pack()

        self.totalCommissionLabel.pack()
        self.totalCommissionEntry.pack()

        self.totalInvestedCostLabel.pack()
        self.totalInvestedCostEntry.pack()

        self.balanceAfterLabel.pack()
        self.balanceAfterEntry.pack()

        # self.buttoncalNumShares.pack()
        # self.buttoncalInvestAmt.pack()
        # self.buttoncalCommissionAmt.pack()
        # self.buttoncalTotalinvestCost.pack()
        self.buttoncalTotalinvestCostOneStep.pack()
        self.buttondelete.pack()

    def calNumShares(self, investamount,shareUnitPrice):
        result=float(investamount)/float(shareUnitPrice)
        self.shareNumberEntry.delete(0,END)
        self.shareNumberEntry.insert(0,result)
        print(result)
    
    def calInvestAmt(self, shareNumber, shareUnitPrice):
        result=float(shareNumber)*float(shareUnitPrice)
        self.investiableEntry.delete(0,END)
        self.investiableEntry.insert(0,result)
        print(result)
    
    def calCommissionAmt(self, shareNumber, shareCommission, fixedCommissionAmt):
        result=float(shareNumber)*float(shareCommission)+float(fixedCommissionAmt)
        self.totalCommissionEntry.delete(0,END)
        self.totalCommissionEntry.insert(0,result)
        print(result)
    
    def calTotalinvestCost(self, investAmt, totalCommissionAmt):
        result=float(investAmt)+float(totalCommissionAmt)
        self.totalInvestedCostEntry.delete(0,END)
        self.totalInvestedCostEntry.insert(0,result)
        print(result)

    def calTotalinvestCostOneStep(self,investamount,shareUnitPrice):
        shareNum=float(investamount)/float(shareUnitPrice)
        self.shareNumberEntry.delete(0,END)
        self.shareNumberEntry.insert(0,shareNum)    
        commissionAmt=shareNum*float(self.shareCommissionEntry.get())+float(self.fixedCommissionEntry.get())            
        result=commissionAmt+float(investamount)
        balance = float(self.balanceEntry.get()) - result
        self.totalCommissionEntry.delete(0,END)
        self.totalCommissionEntry.insert(0,commissionAmt)
        self.totalInvestedCostEntry.delete(0,END)
        self.totalInvestedCostEntry.insert(0,result)
        self.balanceAfterEntry.delete(0,END)
        self.balanceAfterEntry.insert(0,balance)
        print(result)

    def clear(self):
        self.shareNumberEntry.delete(0,END)
        self.unitSharePriceEntry.delete(0,END)
        self.investiableEntry.delete(0,END)
        self.totalInvestedCostEntry.delete(0,END)
        self.totalCommissionEntry.delete(0,END)
        self.balanceEntry.delete(0,END)
        self.balanceAfterEntry.delete(0,END)

def main ():
    rootwindow=Tk()   
    windowUI=GUI(rootwindow)
    rootwindow.mainloop()

if __name__ == '__main__': main()


