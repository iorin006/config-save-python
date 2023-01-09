import shutil
print(' ██████  ██████  ███    ██ ███████ ██  ██████      ███████  █████  ██    ██ ███████ ')
print('██      ██    ██ ████   ██ ██      ██ ██           ██      ██   ██ ██    ██ ██    ')  
print('██      ██    ██ ██ ██  ██ █████   ██ ██   ███     ███████ ███████ ██    ██ █████   ')
print('██      ██    ██ ██  ██ ██ ██      ██ ██    ██          ██ ██   ██  ██  ██  ██    ')  
print(' ██████  ██████  ██   ████ ██      ██  ██████      ███████ ██   ██   ████   ███████ ') 
print("")
print('・デスクトップにconfigができていればコピー成功です。\n・エンターを押した瞬間消えるとエラーが出てます。\n・ファイルの上書きはできません')
print('')
print('PCのユーザーネームを入力してください')
name=input(">")
print(f"user name:{name}")
print('')
def c():
    print('コピーする方法を選んでください。\n1・configファイルだけをコピー\n2・マインクラフトのファイルごとコピー')
    print('')
    i=int(input(">"))
    if i==1:
        print('コピー中です。操作しないでください。')
        shutil.copytree(f'C:\\Users\\{name}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\RoamingState',f'C:\\Users\\{name}\\Desktop\\config')
        input('終了')
        return
    if i==2:
        print('コピー中です。操作しないでください。')
        shutil.copytree(f'C:\\Users\\{name}\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe',f'C:\\Users\\{name}\\Desktop\\config')
        input('終了')
        return
    else:
        print('>>>1~2の数字を入れてください<<<')
        return c()
c()
