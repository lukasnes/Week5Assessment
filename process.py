log_file = open("um-server-01.txt") #Opens the text file to read.


def sales_reports(log_file): #This is a function. It takes a file in as a variable
    for line in log_file: #This loops through every line in our file
        line = line.rstrip() #This removes any white space at the end or start of our string
        day = line[0:3] #This line defines that the day is equal to everything from the start of the line until 3 characters in.
        if day == "Mon": #This statement is truthy when the day at the start of the line is Tuesday.
            print(line) #If that statement is truthy, this line prints the line.


sales_reports(log_file) #This calls our function with our .txt file as the variable
print('\n')
log_file = open("um-server-01.txt")

def num_melons(log_file):
    for line in log_file:
        line = line.rstrip().split(' ')
        if int(line[2]) > 10:
            print(' '.join(line))
num_melons(log_file)