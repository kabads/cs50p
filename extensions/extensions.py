
def getFileType():
    return input("File name: ").lower().strip()[-4:].replace(".", "")

def checkFileType(filetype):
    match filetype:
        case "jpg":
            print("image/jpeg")
        case "gif":
            print("image/gif")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")



def main():
    filetype = getFileType()
    checkFileType(filetype)

if __name__ == '__main__':
    main()
