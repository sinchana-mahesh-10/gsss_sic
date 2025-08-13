'''
accept the average score of the student and print the result as follows
0 to 59    fail
60 to 84   second class
85 to 95   first class
96 to 100  excellent
also check for invalid score
'''

average_score =int (input("Enter your average score to print the result: "))
if average_score < 0 or average_score > 100:
    print('Invalid Score')
elif average_score >= 0 and average_score <=59:
    print('')