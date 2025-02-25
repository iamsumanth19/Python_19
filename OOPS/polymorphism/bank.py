class BankV1:
    bank_name='SBI'
    bank_ifsc='SBIN000955'
    bank_roi=6
    bank_branch='HYD'
    
    def __init__(self,cn,ca,can,cb):
        self.customer_name=cn
        self.customer_age=ca
        self.customer_acc_num=can
        self.customer_balance=cb
    
    def customerDetails(self):
        print(f'Name of the customer: {self.customer_name}')
        print(f'Age of the customer: {self.customer_age}')
        print(f'Account number of the customer: {self.customer_name}')
        print(f'Balance of the customer account: {self.customer_balance}')
    @classmethod
    def bankDetails(cls):
        print(f'Name of the bank is {cls.bank_name}')
        print(f'IFSC code of the bank is {cls.bank_ifsc}')
        print(f'roi of the bank is {cls.bank_roi}')
        print(f'Branch of the bank is {cls.bank_branch}')

    @staticmethod
    def getIntValues():
        val=int(input('Enter the value:'))
        return val
    
    def withdraw(self):
        amt=self.getIntValues()
        if self.customer_balance>=amt:
            self.customer_balance-=amt
            print('Deposite successful!!')
            print(f'Current balance is {self.customer_balance}')
        else:
            print('Insufficient Balance!!!')
            print(f'Current balance is {self.customer_balance}')
    @classmethod
    def changeRoi(cls):
        new_roi=cls.getIntValues()
        cls.bank_roi=new_roi

class BankV2(BankV1):
    bank_branch='BLR'
    bank_mobile=9876543456

    def __init__(self,cn,ca,can,cb,cp,cm):
        self.customer_name=cn
        self.customer_age=ca
        self.customer_acc_num=can
        self.customer_balance=cb
        self.customer_pin=cp
        self.customer_mobile=cm
    
    def deposite(self):
        amt=self.getIntValues()
        self.customer_balance+=amt
        print('Deposite successful!!')

    def customerDetails(self):
        print(f'Name of the customer: {self.customer_name}')
        print(f'Age of the customer: {self.customer_age}')
        print(f'Account number of the customer: {self.customer_name}')
        print(f'Balance of the customer account: {self.customer_balance}')
        print(f'pin of the customer: {self.customer_pin}')
        print(f'mobile number of customer: {self.customer_mobile}')

    @classmethod
    def bankDetails(cls):
        print(f'Name of the bank is {cls.bank_name}')
        print(f'IFSC code of the bank is {cls.bank_ifsc}')
        print(f'roi of the bank is {cls.bank_roi}')
        print(f'Branch of the bank is {cls.bank_branch}')
        print(f'mobile number of the bank is {cls.bank_mobile}')

    def withdraw(self):
        amt=self.getIntValues()
        if self.customer_balance>=amt:
            pin=int(input('Enter the pin:'))
            if pin==self.customer_pin:
                self.customer_balance-=amt
                print('withdraw successful!!')
                print(f'Current balance is {self.customer_balance}')
            else:
                print('Incorrect Pin!!')
        else:
            print('Insufficient Balance!!!')
            print(f'Current balance is {self.customer_balance}')

sumanth=BankV2('sumanth',21,45678,20000,1916,9876543456)
sumanth.withdraw()
sumanth.deposite()
sumanth.customerDetails()
sumanth.bankDetails()
sumanth.changeRoi()