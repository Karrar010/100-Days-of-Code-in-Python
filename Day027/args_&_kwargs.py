
#DEFAULT VALUES FOR OPTIONAL ARGUMENTS OF A FUNCTION

#sometimes when we call a func we dont always have to pass arguments, we can create a function with default values
def defualt_Arg_func (a = 1, b= 2, c = 4):
    print(a+b+c)
defualt_Arg_func() #when calling a func with default arguments then it return result without passing any value
defualt_Arg_func(c= 3)


# ARGS UNLIMITED POSITIONAL ARGUMENTS

#somtimes we need func to take infinite number of argument give a corresponding output SYNTAX: *args or *anything

def multiply(*args): #using this we can pass infinite arguments but these arguments are stored in args(which acts as a tuple) as elements
    prod = 1
    print(type(args)) #see type of args in tuple
    for n in args:
        prod *= n 
    return prod
print(multiply(1,2,3,4,5))


# KWARGS UNLIMITED KEYWORD ARGUMENTS
#SYNTAX: **kwargs
#we implement this into a function to give the function infinite keyword arguments access
#
def calculate(n,**kwargs):
    print(kwargs) #in kwargs(which is a dict) arguments keyword will be stored with arguments value  keyword: value
    print(n*kwargs['two'])
    return kwargs.get('three') #get func is used to fetch the corresponding keyword value, if such a value doesnot exist then it returns NONE

# print(calculate(1,2,3,4)) #if you write this line error will pop as no keyword is given for each of the arguments
print(calculate(9,one = 1, two = 2, three = '3'))

class Car:
    def __init__ (self,**kwargs):
        # self.name = kwargs['name']   #if lets say we dont pass the name of car then this line will result in error as not car name is given
        self.name = kwargs.get('name') #but his line gets a None value when no car name is given, thus no error pops
        self.seats = kwargs.get('seats')
        self.model = kwargs.get('model')
    def details(self):
        print(f'Name: {self.name}, No.of Seats = {self.seats}, Model Year = {self.model}')

car = Car(seats =2, model = 2019)
# car = Car(name= 'Lambo',seats =2, model = 2019)
car.details()