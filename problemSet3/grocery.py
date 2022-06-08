def main():
    g_list = []    
    shop()


def shop():
    while True:
        try:
            user_input = input().upper().strip()
            g_list.append(user_input)
        except (EOFError, KeyError):
            sorted_list = sorted(set(g_list))
            for i in sorted_list:
                print(g_list.count(i),i)
            quit()


main()
