import webbrowser, requests, sys, os

tokenbot = "7391593372:AAFhLbgDhxgNmMZwlLIzB1VuxNnxykV83XQ"
channel = -1002162858751 
 

dvmb = f"https://api.telegram.org/bot{tokenbot}/getChatMember?chat_id={channel}&user_id={teleid}"
response = requests.get(dvmb).json()

if not (response.get("ok") and response.get("result", {}).get("status") in ["member", "administrator", "creator"]):
    anim(f""" ㅤ{black}ㅤ\033[101m[ 🚨 ]    𝐉𝚘𝚒𝚗 𝐀𝚕𝚕 𝐂𝚑𝚊𝚗𝚗𝚎𝚕𝚜 𝐓𝚑𝚎𝚗 𝐎𝚗𝚕𝚢 𝐘𝚘𝚞 𝐂𝚊𝚗 𝐏𝚛𝚘𝚌𝚎𝚎𝚍.{reset}""")
    webbrowser.open("https://t.me/addlist/-zdOU4i16nNjZjll")
except Exception as e :
    print(f"{e})
    sys.exit()
