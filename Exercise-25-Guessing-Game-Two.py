'''
Exercise 25: Guessing Game Two

In a previous exercise, we’ve written a program that “knows”
a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the
user, will have in your head a number between 0 and 100. The
program will guess a number, and you, the user, will say
whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how
many guesses it took to get your number.

'''
# Solution
def main():
    import random
    guess_log = [random.randint(0, 101)]
    log_dict = {'lower':[0], 'higher':[100]}
    while True:
        print(guess_log[-1])
        evaluate = input('Tell me my number is:\n1: too low\n2: too high\n3: Right\n')
        try:
            evaluate = int(evaluate)
            if evaluate == 1:
                log_dict['lower'].append(guess_log[-1])
                guess_log.append(int((min(log_dict['higher']) + max(log_dict['lower']))/ 2 ))
            elif evaluate == 2:
                log_dict['higher'].append(guess_log[-1])
                guess_log.append(int((min(log_dict['higher']) + max(log_dict['lower']))/ 2 ))
            else:
                print('Yeah!\n', guess_log)
                break
        except ValueError:
            print('Input error.')
    
        
if __name__ == "__main__":
    main()
    
# Test Part
# >>> %Run test.py
# 68
# Tell me my number is:
# 1: too low
# 2: too high
# 3: Right2
# 34
# Tell me my number is:
# 1: too low
# 2: too high
# 3: Right3
# Yeah!
#  [68, 34]
# >>> %Run test.py
# 40
# Tell me my number is:
# 1: too low
# 2: too high
# 3: Right
# 1
# 70
# Tell me my number is:
# 1: too low
# 2: too high
# 3: Right
# 1
# 85
# Tell me my number is:
# 1: too low
# 2: too high
# 3: Right
# 2
# 77
# Tell me my number is:
# 1: too low
# 2: too high
# 3: Right
# 1
# 81
# Tell me my number is:
# 1: too low
# 2: too high
# 3: Right
# 2
# 79
# Tell me my number is:
# 1: too low
# 2: too high
# 3: Right
# 2
# 78
# Tell me my number is:
# 1: too low
# 2: too high
# 3: Right
# 3
# Yeah!
#  [40, 70, 85, 77, 81, 79, 78]
