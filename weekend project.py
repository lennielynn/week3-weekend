class ROICalculator:
    
    
    def __init__(self, income, expences, cashFlow, roi, totalInvest):
        self.income = income
        self.expences = expences
        self.cashFlow = cashFlow
        self.roi = roi
        self.totalInvest = totalInvest
        
        
    def Income(self):
        self.income = float(input('Please enter Total Rental Income (The amout made before expences)\n(example input: 2000) '))
        
        
    def Expence(self):
        self.expences = float(input('Plase enter Total Property Expence(The cost of owning/maintaining the property)\n(example input: 1610) '))
        
        
    def CashFlow(self):
        self.cashFlow = self.income - self.expences
        print(f"Based on the given info your estimated Cash Flow is {self.cashFlow}")
   
        
    def TotalInv(self):
        dp = float(input('Please enter your Down Payment amount '))
        self.totalInvest += dp
        close = float(input('Please enter Total Closing Cost '))
        self.totalInvest += close
        repair = float(input('Please enter Total Repair Cost '))
        self.totalInvest += repair
        misc = float(input('Please enter any other investment cost '))
        self.totalInvest += misc
        print(f'Your estemated total investment is {self.totalInvest}')
        
    def EstematedROI(self):
        acf = self.cashFlow * 12
        self.roi = acf/self.totalInvest * 100
        print(f'Based on the given info your estemated ROI is {self.roi}%.\nIf this seems incorrect, please review your info and try again. ')
        
        
    def View(self):
        print(f'Total Rental Income: {self.income}')
        print(f'Total Property Expence: {self.expences}')
        print(f'Total Cash Flow: {self.cashFlow}')
        print(f'Total Investment Value: {self.totalInvest}. \nThis value includes: \n - Down Payment \n - Total Closing Cost \n - Extra Expense')
        print(f'Your Estemated ROI is {self.roi}% ')
        
        
def Driver():
    while True:
        print('To calculate your R.O.I., first, we need some info...')
        estamate.Income()
        estamate.Expence()
        estamate.CashFlow()
        estamate.TotalInv()
        estamate.EstematedROI()
        response = input('Would you like to [q]uit, [r]eview your info, or [s]tart over? ').lower
        if response == 'q':
            break
        elif response == 's':
            continue
        elif response == 'r':
            estamate.View()
            response_2 = input('Would you like to [q]uit, or [s]tart over? [c]hange my info? ').lower
            if response_2 == 'q':
                break
            elif response_2 == 's':
                continue
            elif response_2 == 'c':
                response_3 = input('What info would you like to edit?\n[i]ncome, [e]xpences, [t]otal investment ').lower
                if response_3 == 'i':
                    estamate.Income()
                    estamate.CashFlow()
                    response = input('Would you like to [q]uit, [r]eview your info, or [s]tart over? ').lower    
                elif response_3 == 'e':
                    estamate.Expence()
                    estamate.CashFlow()
                    response = input('Would you like to [q]uit, [r]eview your info, or [s]tart over? ').lower
                elif response_3 == 't':
                    estamate.TotalInv
                    response = input('Would you like to [q]uit, [r]eview your info, or [s]tart over? ').lower
        

estamate = ROICalculator(0, 0, 0, 0, 0)

Driver()
        