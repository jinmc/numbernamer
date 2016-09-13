def name_of_digit(n):               # name one digit
    dict = {0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"}
    return dict[n]

def name_of_tens(n):                # name of tens
    dict = {1: "ten",
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"}
    return dict[n]


def name_of_teens(n):               # name of teens
    dict = {10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"}
    return dict[n]
def name_of_integerone(n):                  #handles from 1 to 99
    if 1 <= n <= 9:
        return name_of_digit(n)
    elif 10 <= n <= 99:
        if divmod(n, 10)[0] == 1:
            return name_of_teens(n)
        elif divmod(n, 10)[1] == 0:
            return name_of_tens(divmod(n, 10)[0])
        return name_of_tens(divmod(n, 10)[0]) + " " + name_of_digit(divmod(n,10)[1])

def name_of_integertwo(n):                      #handles from 1 to 999
    if 1 <= n <= 9:
        return name_of_digit(n)    
    elif 10 <= n <= 99:
        if divmod(n, 10)[0] == 1:
            return name_of_teens(n)
        elif divmod(n, 10)[1] == 0:
            return name_of_tens(divmod(n, 10)[0])
        return name_of_tens(divmod(n, 10)[0]) + " " + name_of_digit(divmod(n,10)[1])
    elif 100 <= n <= 999:
        if divmod(n, 100)[1] == 0:
            return name_of_digit(divmod(n, 100)[0]) + " hundred"
        return name_of_digit(divmod(n, 100)[0]) + " hundred " + name_of_integerone(divmod(n, 100)[1])

def name_of_integerthree(n):                #handles from 1 to 999999
    if 1 <= n <= 9:
        return name_of_digit(n)
    elif 10 <= n <= 99:
        if divmod(n, 10)[0] == 1:
            return name_of_teens(n)
        elif divmod(n, 10)[1] == 0:
            return name_of_tens(divmod(n, 10)[0])
        return name_of_tens(divmod(n, 10)[0]) + " " + name_of_digit(divmod(n,10)[1])
    elif 100 <= n <= 999:
        if divmod(n, 100)[1] == 0:
            return name_of_digit(divmod(n, 100)[0]) + " hundred"
        return name_of_digit(divmod(n, 100)[0]) + " hundred " + name_of_integerone(divmod(n, 100)[1])
    elif 1000 <= n <= 999999:
        if divmod(n, 1000)[1] == 0:
            return name_of_integertwo(divmod(n, 1000)[0]) + " thousand"
        return name_of_integertwo(divmod(n, 1000)[0]) + " thousand " + name_of_integertwo(divmod(n, 1000)[1])
                                 
def name_of_integer(n):                 #handles from 1 to 999999999
    if 0 <= n <= 9:
        return name_of_digit(n)
    elif 10 <= n <= 99:
        if divmod(n, 10)[0] == 1:
            return name_of_teens(n)
        elif divmod(n, 10)[1] == 0:
            return name_of_tens(divmod(n, 10)[0])
        return name_of_tens(divmod(n, 10)[0]) + " " + name_of_digit(divmod(n,10)[1])
    elif 100 <= n <= 999:
        if divmod(n, 100)[1] == 0:
            return name_of_digit(divmod(n, 100)[0]) + " hundred"
        return name_of_digit(divmod(n, 100)[0]) + " hundred " + name_of_integerone(divmod(n, 100)[1])
    elif 1000 <= n <= 999999:
        if divmod(n, 1000)[1] == 0:
            return name_of_integertwo(divmod(n, 1000)[0]) + " thousand"
        return name_of_integertwo(divmod(n, 1000)[0]) + " thousand " + name_of_integertwo(divmod(n, 1000)[1])
    elif 1000000 <= n <= 999999999:
        if divmod(n, 1000000)[1] == 0:
            return name_of_integertwo(divmod(n, 1000000)[0]) + " million"
        return name_of_integertwo(divmod(n, 1000000)[0]) + " million " + name_of_integerthree(divmod(n, 1000000)[1])
    

def name_of_fraction(tuple):            # make fraction words
    if tuple[0] == 1:
        return name_of_integer(tuple[0]) + " " + name_of_integer(tuple[1]) + "th"
    elif tuple[1] == 10:
        return name_of_integer(tuple[0]) + " " + name_of_integer(tuple[1]) + "ths"
    elif tuple[1] == 100:
        return name_of_integer(tuple[0]) + " hundredths"
    elif tuple[1] == 1000:
        return name_of_integer(tuple[0]) + " thousandths"

def name_of_decimal(n, tuple):      # make (3, (2, 10)) to three and two tenths
    if n == 0 and tuple[0] == 0:
        return "zero"
    elif n == 0 and tuple[0] != 0:
        return name_of_fraction(tuple)
    elif n != 0 and tuple[0] == 0:
        return name_of_integer(n)
    
    return name_of_integer(n) + " and " + name_of_fraction(tuple)

def name_in_dollars(dollars, cents):
    if dollars == 0 and cents == 0:
        return "zero dollars"
    elif dollars == 0 and cents != 0:
        if cents == 1:
            return "one cent"
        else:
            return name_of_integer(cents) + " cents"
    elif dollars != 0 and cents == 0:
        if dollars == 1:
            return "one dollar"
        else:
            return name_of_integer(dollars) + " dollars"
    elif dollars != 0 and cents != 0:
        if dollars == 1 and cents == 1:
            return "one dollar and one cent"
        elif dollars == 1 and cents != 1:
            return "one dollar and " + name_of_integer(cents) + " cents"
        elif dollars != 1 and cents == 1:
            return name_of_integer(dollars) + " dollars and one cent"
        elif dollars != 1 and cents != 1:
                return name_of_integer(dollars) + " dollars and " + name_of_integer(cents) + " cents"
    
def name_of_number(str):
    if str == "":
        return ""
    elif str[0] == "$":
        if "." in str:
            if str[1] == ".":
                if len(str[2:]) == 1:
                    return name_in_dollars(0, int(str[2:]) * 10)
                else:
                    return name_in_dollars(0, int(str[2:]))
            if len(str[1:].split(".")[1]) == 1:
                return name_in_dollars(int(str[1:].split(".")[0]), 10 * int(str[1:].split(".")[1]))
            else:
                return name_in_dollars(int(str[1:].split(".")[0]), int(str[1:].split(".")[1]))
        else:
            return name_in_dollars(int(str[1:]), 0)
    else:
        if "." in str:
            if str[0] == ".":
                return name_of_decimal(0, (int(str[1:]), 10 ** len(str[1:])))
                
            else:
                return name_of_decimal(int(str.split(".")[0]), (int(str.split(".")[1]), 10 ** len(str.split(".")[1])))
        else:
            return name_of_integer(int(str))

def main():
    modifiedinput = ""
    numberlike = ""
    sentence = "anything"
    while sentence != "":
        if sentence == "":
            break
        
        sentence = input("input sentence : ")
    
        for n in range(len(sentence)):
            if sentence[n] == "$":
                if sentence[n + 1].isdigit:
                    numberlike += "$"
                elif sentence[n + 1] == ".":
                    if sentence[n + 2].isdigit:
                        numberlike += "$."
                else:
                    modifiedinput += "$"
            elif sentence[n].isdigit():
                numberlike += sentence[n]
                if n == len(sentence) - 1:
                    modifiedinput += name_of_number(numberlike)

            elif sentence[n] == ".":
                if n == len(sentence) - 1:
                    if sentence[n - 1].isdigit:
                        modifiedinput += name_of_number(numberlike)
                    else:
                        modifiedinput += "."
                elif sentence[n + 1].isdigit:
                    numberlike += "."
                else:
                    modifiedinput += "."
                    
            else:
                numberlike = name_of_number(numberlike)
                modifiedinput += numberlike
                modifiedinput += sentence[n]
                numberlike = ""
        print(modifiedinput)
        numberlike = ""
        modifiedinput = ""
    print("Thank you!")

if __name__ == "__main__":
    main()
