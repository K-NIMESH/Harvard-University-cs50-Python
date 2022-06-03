num_list = ["0","1","2","3","4","5","6","7","8","9"]
letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]    


def main():
    plate_request = get_input()
    response = process_plate(plate_request) 
    print(response)

    
def get_input():
    user_input = input("Plate: ").lower()
    return user_input

    
def analyze_plate(string):
    if letter_after_num(string) != "reject string":
        if check_zero(string) != "0":
            if 2 <= len(string) <= 6:
                if string[0] in letter_list:
                    if string[1] in letter_list:
                        for char in string:
                            if char in num_list or char in letter_list:
                                ...
                            else:
                                return False
                    else:
                        return False
                else:
                    return False
            else: 
                return False
        else:
            return False
    else:
        return False

    
def check_zero(string):
    for i in string:
            if i in num_list:
                check_list = []
                check_list.insert(0,i)
                if check_list[0] != "0":
                    return check_list[0]
                else:
                    return check_list[0]

                
def letter_after_num(string):
    for i in string:
        if i in num_list:
            num = i
            split_string = string.split(num)
            if split_string[1] != '':
                r_string = split_string[1][0]     
                if r_string not in num_list:
                    return "reject string"
                

def process_plate(string):
    result = analyze_plate(string)
    if result != False:
        return "Valid"
    else:
        return "Invalid"    



main()  
