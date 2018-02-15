
# scope is different based on (scope)
# where you are inside or outside the function




# version 1
version = "Version 1"
message = "simple variable changed globaly no function"
print version
print message
x = "Texas"
print x
x = "Utah"
print x



version = "\n\nVersion 2"
message = "function tries to change global variable but fails"
print version
print message

x = "Texas"
def update_city():
    x = "New Mexico"

print x
update_city()
print x




version = "\n\nVersion 3"
message = "function tries to change global variable with same name but fails"
print version
print message

x = "Texas"
def update_city3(x):
    x = "New Mexico"

print x
update_city3(x)
print x


version = "\n\nVersion 4"
message = "function tries to change global variable that is a nested array with same name but fails"
reason = "objects are passed by reference but strings and numbers are passed by value"
print version
print message

x = [["Austin"],["Texas"]]
def update_city4(x):
    x[0]= "Santa Fe",
    x[1]="New Mexico"

print x
update_city4(x)
print x




version = "\n\nVersion 5"
message = "function get pass global object with different name"
reason = "global obejct wil change because objects are passed by reference"
print version
print message

x = [["Austin"],["Texas"]]
# this b variable does not relate to anything else
def update_city5(b):
    b[0]= "Santa Fe",
    b[1]="New Mexico"

print x
update_city5(x)
print x




version = "\n\nVersion 6"
message = "function tries to change global variable with same name but fails"
print version
print message

x = "Texas"
# again b doesn't matter its just a label for what is being passed
def update_city6(b):
    b = "New Mexico"

print x
update_city6(x)
print x





def toLeft(x,y):
    return [(x-1),(y-1)]


print toLeft(1,3)
