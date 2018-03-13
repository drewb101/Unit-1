#Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20

#Write a loop that prints each of the numbers on a new line, like this:

#12
#10
#...etc


#Then, write a loop that prints each number and its square on a new line, like this:

#The square of 12 is 144
#The square of 10 is 100
#...etc
nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for a in nums:
    print(a)

for b in nums:
    print("The square of", b, "is", b ** 2)
