#lists



def younger_person():
    ages = [72,42,32,50,56,14,78,30,51,89,12,38,67,10]

    solution = ages[0]
    for age in ages:
        # if the age is lower than the solution, the solution should be equal to age
        if age < solution:
            solution = age

    print(solution)


def statistics():
    data = [12,-1,123,345,412,4.55,123,23.4,123,4587,-129,94,956,14565,32, 0.001, 123]

#1 - how many elements
#2 - what is the sum
#3 - sum of the negative numbers
#4 - count how many are over 500

    count = 0
    total = 0
    negative = 0
    over_500 = 0

    for num in data:
        count = count + 1
        total = total + num
        # total += num
        #the above two lines are identical
        if num < 0:
           negative = negative + 1
           #negative += 1

        if(num > 500):
            over_500 += 1    
    

    print(f"solution #1 is: {count}")        
    print(f"solution #2 is: {total}")
    print(f"the solution to 1 is {len(data)}")
    print (f"the solution to 3 is {negative} ")
    print (f" the solution to 4 is {over_500}")

def print_some_nums():
    #print the multiples of 10 that exist between 10 and 100
    
    for num in range(1, 11):
        print(num * 10)

    for x in range(10, 110, 10):
        print(x)

    #the above are two ways of doing the same thing




print(len("hello world")) 
print("Aye Aye Aye! Arriba, Arriba!")
younger_person()
statistics()
print_some_nums()