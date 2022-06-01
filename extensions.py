extensionsList = ["gif", "image/gif", "jpg", "image/jpeg", "bin", "application/octet-stream", "png", "image/png", "pdf", "application/pdf", "txt", "text/plain", "zip", "application/zip"]


def main():
    fileExtension = getFile()
    application = getApplication(fileExtension)
    print(application)


def getFile():
    while True:
        userFile = input("File name: ").lower().replace(" ", "").replace("jpeg", "jpg")
        if len(userFile) > 4 and "." in userFile:
            separator = userFile[-4]
            fileName_into_list = userFile.split(separator)
            extension = fileName_into_list[-1]
            if extension in extensionsList:
                return extension
        return extensionsList[4]


def getApplication(fileExtension):
    y = 0
    for i in extensionsList:
        if i == fileExtension:
            application = extensionsList[y + 1]
            return application
        y += 1        


main()

