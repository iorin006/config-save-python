import shutil
print('・デスクトップにconfigができていればコピー成功です。\n・エンターを押した瞬間消えるとエラーが出てます。')
name=input('PCのユーザーネームを入力してください::')
def c():
    print('コピーする方法を選んでください。\n1・configファイルだけをコピー\n2・マインクラフトのファイルごとコピー')
    i=int(input())
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
