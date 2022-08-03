
'''
+-------------------+
| AutoFileTransferer|
+-------------------+
by Bishal jaiswal Copyright (c) 2022
'''

import os

global Files
global Folders


def displayFolders():
    global Folders
    content = os.listdir()
    content.remove("main.py")
    content.remove("Transfer")
    Folders = [folder for folder in content if not os.path.isfile(folder)]
    if len(Folders) > 0:
        print("\n[i] The folders are:")
        for count1, folder in enumerate(Folders):
            print(f"   [{count1}]", folder, "")


def displayFiles():
    global Files
    content = os.listdir()
    content.remove("main.py")
    content.remove("Transfer")
    Files = [file for file in content if os.path.isfile(file)]
    if len(Files) > 0:
        print("\n[i] The files are:")
        for count, file in enumerate(Files):
            print(f"   [{count}]", file, "")


def copy_content(distPath):
    global Files
    global Folders
    folders = []
    files = []

    action = int(
        input("\n[1] Transfer Folders\n[2] Transfer Files\n Choos your action> "))
    if action == 1:
        displayFolders()
        if len(Folders) > 0:
            count = int(input("How many Folders you want to transfer> "))
            for i in range(count):
                chooseFolders = int(input("Choos the folders> "))
                folders.append(Folders[chooseFolders])
                os.replace(folders[i], f"{distPath}/{folders[i]}")
        else:
            print("[!] No Folders Found !")

    if action == 2:
        displayFiles()
        if len(Files) > 0:
            cnt = int(input("How many Files you want to transfer> "))
            for j in range(cnt):
                chooseFiles = int(input("Choose the files> "))
                files.append(Files[chooseFiles])
                os.replace(files[j], f"{distPath}/{files[j]}")
        else:
            print("[!] No Files Found")


if __name__ == "__main__":
    while True:
        choose = int(input(
            "\n[1] Display content\n[2] Copy content\n[3] To EXIT\nChoos the options> "))
        if choose == 1:
            displayFolders()
            displayFiles()
        elif choose == 2:
            copy_content(r"C:\\path where you want to copy content")
        elif choose == 3:
            print("\n[i] Thank you......:)")
            break
        else:
            print("\n[!] Error....")
