import asyncio
import sys
from bot.main import bot

async def set_webhook(domain):
    # domen oxiridagi / belgisini olib tashlaymiz
    if domain.endswith('/'):
        domain = domain[:-1]
        
    webhook_url = f"{domain}/webhook/{bot.token}"
    print(f"Webhook sozlanmoqda: {webhook_url}")
    
    info = await bot.get_webhook_info()
    print(f"Eski webhook: {info.url}")
    
    await bot.set_webhook(webhook_url, drop_pending_updates=True)
    
    info = await bot.get_webhook_info()
    print(f"Yangi webhook muvaffaqiyatli o'rnatildi: {info.url}")
    
    await bot.session.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Iltimos, domenni kiriting!")
        print("Misol: python set_webhook.py https://username.pythonanywhere.com")
        sys.exit(1)
    
    url = sys.argv[1]
    if not url.startswith("http"):
        url = "https://" + url
        
    asyncio.run(set_webhook(url))
