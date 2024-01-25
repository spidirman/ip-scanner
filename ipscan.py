import asyncio
import aiohttp
import time
import os

async def ip():
    os.system("clear || cls")
    arg1 = input("ip:")
    if arg1 == "":
        print("invalid ip")
        return
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://ip-api.com/json/{arg1}?fields=66846719") as r:
            js = await r.json()
    
    status = js["status"]
    if status == "fail":
        message = js["message"]
        print(message)
        return
    
    continent = js.get("continent", "None")
    country = js.get("country", "None")
    region = js.get("regionName", "None")
    city = js.get("city", "None")
    rue = js.get("district", "None")
    zipcode = js.get("zip", "None")
    lat = js.get("lat", "None")
    lon = js.get("lon", "None")
    timezone = js.get("timezone", "None")
    offset = js.get("offset", "None")
    iso = js.get("isp", "None")
    org = js.get("org", "None")
    reverse = js.get("reverse", "None")
    mobile = js.get("mobile", "None")
    proxy = js.get("proxy", "None")
    hosting = js.get("hosting", "None")

                        log = f"continent: {str(continent)}\ncountry: {str(country)}\nregion: {str(region)}\ncity: {str(city)}\ndistrict: {str(rue)}\nzipcode: {str(zipcode)}\nlatitude: {str(lat)}\nlongitude: {str(lon)}\ntimezone: {str(timezone)}\noffset: {str(offset)}\nisp: {str(iso)}\norganisation: {str(org)}\nreverse: {str(reverse)}\nmobile: {str(mobile)}\nproxy: {str(proxy)}\nhosting: {str(hosting)}";print(log);file = input ("do you want txt file to save data [y/n]:")
                        if file == "y" or file == "yes":
                            with open(str(arg1)+'.txt', 'w') as f:f.write(str(log));time.sleep(5)
while True:asyncio.run(ip())
