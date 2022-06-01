def main():
    q = input("What's the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    if greatAnswer(q):
        print("Yes")
    else:
        print("No")

def greatAnswer(a):
    if a == "42":
        return True
    elif "forty-two" in a:
        return True
    elif "forty two" in a:
        return True

main()