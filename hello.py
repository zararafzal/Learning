# # # # print ("HELLO")

# # # # Write a program to prompt the user for hours and rate per hour using input to compute gross pay.Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.The function should return a value.Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).You should use input to read a string and float() to convert the string to a number.Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

# # # # def computepay(h, r):
# # # #    if h <= 40:
# # # #        p = h*r
# # # #        return p
# # # #    elif h > 40:
# # # #        p = 1.5 * r * (h - 40) + (40 * r)
# # # #        return p


# # # # h = float(input("Enter Hours:"))
# # # # r = float(input("Enter Rate:"))
# # # # p = computepay(h, r)
# # # # print("Pay", p)

# # # # while True:
# # # #    line = input(">:")
# # # #    if line[0] == "#":
# # # #        continue
# # # #    if line == "done":
# # # #        break
# # # #    print(line)
# # # # print("DONE")

# # # # 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# largest = None
# smallest = None

# while True:
#     num_input = input("Enter a number: ")
#     if num_input == 'done':
#         break
#     try:
#         num = int(num_input)
#         if smallest is None or num < smallest:
#             smallest = num
#         if largest is None or num > largest:
#             largest = num
#     except ValueError:
#         print("Invalid input")

# # # # if largest is None or smallest is None:
# # # #     print("No valid numbers entered.")
# # # # else:
# # # #     print("Maximum is", largest)
# # # #     print("Minimum is", smallest)

# # # COURSE 2

# # CODE TO SLICE AND SPLIT
# # text = "X-DSPAM-Confidence:    0.8475"
# # s = text.find(':')
# # s1 = text[s + 1:]
# # end = float(s1)
# # print(end)

# # Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file PYTHON.txt to produce the output below.
# # fname = input("Enter file name: ")
# # fh = open(fname)
# # for i in fh:
# #     i = i.rstrip()
# #     i = i.upper()
# #     print(i)

# # Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

# # X-DSPAM-Confidence:    0.8475

# # Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# # fname = input("Enter file name: ")
# # fh = open(fname)
# # count = 0
# # total = 0
# # for line in fh:
# #     if not line.startswith("X-DSPAM-Confidence:"):
# #         continue
# #     t = line.find("0")
# #     number = float(line[t:])
# #     count = count + 1
# #     total = total + number

# # average = total/count
# # print("Average spam confidence:", average)
