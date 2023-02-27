msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

operations = ['+', '-', '*', '/']
M = 0


def is_one_digit(v):
    v = float(v)
    if -10 < v < 10 and v.is_integer() is True:
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) is True and is_one_digit(v2) is True:
        msg = msg + msg_6
    if (v1 == '1' or v2 == '1') and v3 == "*":
        msg = msg + msg_7
    if (v1 == '0' or v2 == '0') and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    calc = input()
    calc_list = calc.split(' ')
    x = calc_list[0]
    if x == 'M':
        x = str(M)

    y = calc_list[2]
    if y == 'M':
        y = str(M)
    operator = calc_list[1]

    if x.isalpha() is False and y.isalpha() is False:
        if operator in operations:
            check(x, y, operator)

            if operator == "+":
                result = float(x) + float(y)
            elif operator == '-':
                result = float(x) - float(y)
            elif operator == '*':
                result = float(x) * float(y)
            elif operator == "/" and y != 0:
                try:
                    result = float(x) / float(y)
                except ZeroDivisionError:
                    print(msg_3)
                    continue

            print(result)
            print(msg_4)
            answer = input()

            if answer == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer_2 = input()
                        if answer_2 == 'y':
                            if msg_index < 12:
                                msg_index = msg_index + 1
                            else:
                                M = result
                                break
                        if answer_2 == 'n':
                            break
                else:
                    M = result

            if answer == 'n':
                M = 0
            print(msg_5)
            answer_1 = input()
            if answer_1 == 'y':
                continue
            elif answer_1 == 'n':
                break

        else:
            print(msg_2)
            continue
    else:
        print(msg_1)
        continue
