nombrearch = input("Ingrese el nombre del archivo: ")
n = nombrearch.index('.')
sufijo = nombrearch[n:].lower()
mime = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

if sufijo in mime:
    print(f"El tipo MIME del archivo {nombrearch} es: {mime[sufijo]}")
else:
    print(f"El tipo MIME del archivo {nombrearch} es: application/octet-stream")