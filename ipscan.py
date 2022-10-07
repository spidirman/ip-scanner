import asyncio
import aiohttp
import time
import os


os.system("color a")
async def ip():
   os.system("cls")
   arg1 = input ("ip:")
   if arg1 == "":print("invalid ip")
   else:
       async with aiohttp.ClientSession() as session:
                async with session.get(f"http://ip-api.com/json/{arg1}?fields=66846719") as r:
                    js = await r.json();myip = ('');status = (js["status"])
                    if "fail" == status:message = (js["message"]);print(message)
                    else:
                        continent = (js["continent"]);country = (js["country"]);region = (js["regionName"]);city = (js["city"]);rue = (js["district"]);zipcode = (js["zip"]);lat = (js["lat"]);lon = (js["lon"]);timezone = (js["timezone"]);offset = (js["offset"]);iso = (js["isp"]);org = (js["org"]);reverse = (js["reverse"]);mobile = (js["mobile"]); proxy = (js["proxy"]); hosting = (js["hosting"])
                       #################
                        if continent == "":continent = "None"
                        else:continent = (js["continent"])
                            #
                        if country == "":country == "None"
                        else:country = (js["country"])
                            #
                        if region == "":region = "None"
                        else:region = (js["regionName"])
                            #
                        if city == "":city = "None"
                        else:city = (js["city"])
                            #
                        if rue == "":rue = "None"
                        else:rue = (js["district"])
                            #
                        if zipcode == "":zipcode = "None"
                        else :zipcode = (js["zip"])
                            #
                        if lat == "":lat = "None"
                        else:lat = (js["lat"])
                            #
                        if lon == "":lon = "None"
                        else:lon = (js["lon"])
                            #
                        if timezone == "":timezone = "None"
                        else:timezone = (js["timezone"])
                            #
                        if offset == "":offset = "None"
                        else:offset = (js["offset"])
                            #
                        if iso == "":iso = "None"
                        else:iso = (js["isp"])
			#
                        if org == "":org = "None"
                        else:org = (js["org"])
			#
                        if reverse == "":reverse = "None"
                        else:reverse = (js["reverse"])
			#
                        if mobile == "":mobile = "None"
                        else:mobile = (js["mobile"])
			#
                        if proxy == "":proxy = "None"
                        else:proxy = (js["proxy"])
			#
                        if hosting == "":hosting = "None"
                        else:hosting = (js["hosting"])

                        log = f"continent: {str(continent)}\ncountry: {str(country)}\nregion: {str(region)}\ncity: {str(city)}\ndistrict: {str(rue)}\nzipcode: {str(zipcode)}\nlatitude: {str(lat)}\nlongitude: {str(lon)}\ntimezone: {str(timezone)}\noffset: {str(offset)}\nisp: {str(iso)}\norganisation: {str(org)}\nreverse: {str(reverse)}\nmobile: {str(mobile)}\nproxy: {str(proxy)}\nhosting: {str(hosting)}";print(log);file = input ("do you want txt file to save data [y/n]:")
                        if file == "y" or file == "yes":
                            with open(str(arg1)+'.txt', 'w') as f:f.write(str(log));time.sleep(5)
while True:asyncio.run(ip())
