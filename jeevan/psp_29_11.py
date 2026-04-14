'''# class student:
#     school = "Newton"
#     def __init__(self,val) :
#         self.name  = val
#     def surname(self,val):
#         self.surname = val 

# # s1 = student("jeevan")
# # print(s1.name)

# # print(s1.school)
# s2 = student("kkk")
# print(s2.name)

# s2.surname("B R")
# print(s2.surname)'''

'''# class student:
#     school = "Newton"
#     def __init__(self,val1,val2) :
#         self.name  = val1
#         self.surname = val2
#     def fullname(self):
#         self.full = self.name+" "+self.surname

    

# s1 = student("jeevan","B R")
# print(s1.name)
# print(s1.surname)
# s1.fullname()
# print(s1.full)'''


class fractional:
    def __init__(self,numerator,dinominator) :
        self.numer = numerator
        self.diner = dinominator
    
    def final(self,val1):
        return fractional(val1.numer*self.diner+self.numer*val1.diner,val1.diner*self.diner)

        
    def print(self):
        print(self.numer,"/",self.diner)



frac1 = fractional(2,5)
frac2 = fractional(3,8)

ans = frac1.final(frac2)
ans.print()


