import os
logo_path = os.path.join(os.path.dirname(__file__), 'Side Files', 'Logo.txt')
yt_path = os.path.join(os.path.dirname(__file__), 'Side Files', 'Youtube.lnk')
yttv_path = os.path.join(os.path.dirname(__file__), 'Side Files', 'Youtube TV.lnk')
logo = open(logo_path, 'r')
content = logo.read()
print(content)
ans = input("---------------- Which one (1-2)> ")

if ans == '1':
    os.startfile(yt_path)
if ans == '2':
    cans = input("This will close Chrome. (Ignore the restore popup) Continue? [y/n]: ")
    if cans == 'y':
        os.system('taskkill /F /IM chrome.exe')
        os.startfile(yttv_path)
    elif cans == 'n':
        print("Aborted")