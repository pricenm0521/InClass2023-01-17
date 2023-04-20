# in-Class work 2023-01-17
from pickle import TRUE
from _testmultiphase import foo
from pkg_resources._vendor.jaraco.context import null
epsilon = 123
zeta = 456
iota = epsilon + zeta
print(iota)

beta = "123"
delta = "456"
gamma = beta + delta # 'add' a string and an integer, fixed to run program
print(gamma)

x = 42
y = 1.5
z = x + y # try to add float and int
print(z)

zeta = True
foo = zeta + 1 # does this make sense?
print(foo)

gamma = True
eta = gamma + 1.5
print(eta)

# Can I add a booloean to a string? no we cannot
# peer = True
# peerless = "Hello"
# print(peer + peerless)

#Store a float in variable epsilon
#Store a float in variable nu
#Divide epsilon by nu
#Store the result in sigma
#Print the value of sigma to 2 decimal places
epsilon = 12.25
nu = 3.75
sigma = epsilon / nu
print("{:.2f}".format(sigma)) # https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

#alternate solution
epsilon = 12.25
nu = 3.75
sigma = round(epsilon/nu, 2)
print(sigma)

x = 12312312312312312312312312312312312312312312312312
print(x)
x = x + 1
print(x)

# introduce the % operator, integer remainder operator aka mod or modulo
a = 100
b = 30
c = a%b
print(c) # c is the remainder of a divided by b

print("c =", c)
# mod operator is fundamental operator of data encryption 

a = 30
b = 100
c = a%b # integer remainder of 30/100


