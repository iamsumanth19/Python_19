# aggregation example by car and driver classes
class Car:
    def __init__(self,cna,cn,cm,cp):
        self.cname=cna
        self.cnumber=cn
        self.cmodel=cm
        self.cprize=cp
        
    def car_details(self):
        print(f'car name is {self.cname}')
        print(f'car number is {self.cnumber}')
        print(f'car model is {self.cmodel}')
        print(f'car prize is {self.cprize}')
        
    def start(self):
        print('car started!!')
        
    def accelerate(self):
        print('car accelerated!!')
        
    def stop(self):
        print('car stoped!!')
        
class Driver:
    def __init__(self,dn,did,de):
        self.dname=dn
        self.D_id=did
        self.dexp=de
        cna=input('Enter car name:')
        cn=input('Enter car number:')
        cm=input('Enter car model:')
        cp=input('Enter car prize:')
        DCO=Car(cna,cn,cm,cp)
        self.dcar=DCO
        
    def driving(self):
        self.dcar.start()
        self.dcar.accelerate()
        self.dcar.stop()
        
    def driver_details(self):
        print(f'Driver name is {self.dname}')
        print(f'Driver driver_id is {self.D_id}')
        print(f'Driver dexperience is {self.dexp}')
        print('car details are:-')
        self.dcar.car_details()
        
        
sumanth=Driver('sumanth',123,5)
sumanth.driver_details()
sumanth.driving()