import webbrowser, time, requests, sys, os

tokenbot = "7768613787:AAGXHqCRNK9Ze2FuVAXn-qCW2Obh1Pt7mFU"
channel = "@unsely" 
 

url = f"https://api.telegram.org/bot{tokenbot}/getChatMember?chat_id={channel}&user_id={teleid}"
response = requests.get(url).json()

print("\r", end="", flush=True)

if not (response.get("ok") and response.get("result", {}).get("status") in ["member", "administrator", "creator"]):
    print(" ㅤ⚚  𝐍ɪɢɢᴇʀ 𝐉ᴏɪɴ 𝐓ʜᴇ 𝐂ʜᴀɴɴᴇʟ 𝐓ᴏ 𝐔𝚂ᴇ 𝐓ʜᴇ 𝐓ᴏᴏʟ")
    sys.exit()
    
