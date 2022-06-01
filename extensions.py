f = ["gif", "image/gif", "jpg", "image/jpeg", "bin", "application/octet-stream", "png", "image/png", "pdf", "application/pdf", "txt", "text/plain", "zip", "application/zip"]


def main():
    fileName = getFileName()
    print(fileApp(fileName))


def getFileName():
    while True:
        x = input("File name: ").lower().replace(" ", "").replace("jpeg", "jpg")
        if len(x) > 4 and "." in x:
            z = x[-4]
            b = x.split(z)
            c = b[-1]
            if c in x:
                return c
        else:
            return f[4]


def fileApp(fileName):
    y = -1
    for i in f:
        y += 1
        if i == fileName:
            return f[y + 1]


main()

