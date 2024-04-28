class Practice:
    def append_list(self):
        #self.lst = lst
        self.lst = list(range(1,20))
        print(self.lst)
    
    def chk_dvsbl(self):
        for i in self.lst:
            if ((i%5==0) and (i%3==0)):
                print(i,'Nos is divisble by 5 and 3')
            elif i%3==0:
                print(i,'no is divisble by 3')
            elif i%5==0:
                print(i,'no is divisible 5')            

prac = Practice()
prac.append_list()
prac.chk_dvsbl()
        
