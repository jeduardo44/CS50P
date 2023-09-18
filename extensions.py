extension=str(input("File name: "))

def split_extension(extension):
    extension_ls=extension.split(".")
    return extension_ls[-1].strip().lower()

result=split_extension(extension)

if result=="gif":
    print("image/gif")
elif result=="jpg" or result=="jpeg":
    print("image/jpeg")
elif result=="png":
    print("image/png")
elif result=="pdf":
    print("application/pdf")
elif result=="txt":
    print("text/plain")
elif result=="zip":
    print("application/zip")
else:
    print("application/octet-stream")