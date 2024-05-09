import asyncio
import aiohttp
import os

async def get_ip_info(session, ip_address):
    url = f"http://ip-api.com/json/{ip_address}?fields=66846719"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None
    except aiohttp.ClientError:
        return None

async def main():
    os.system("clear || cls")
    while True:
        ip_address = input("Enter IP address (or press Enter to exit): ")
        if not ip_address:
            print("Exiting...")
            break

        async with aiohttp.ClientSession() as session:
            ip_info = await get_ip_info(session, ip_address)
        
        if ip_info is None:
            print("Failed to retrieve information for the given IP address.")
            continue

        status = ip_info.get("status")
        if status == "fail":
            print("Failed to retrieve information. Please check the provided IP address.")
            continue

        # Extract relevant information
        ip_data = {
            "Continent": ip_info.get("continent", "None"),
            "Country": ip_info.get("country", "None"),
            "Region": ip_info.get("regionName", "None"),
            "City": ip_info.get("city", "None"),
            "District": ip_info.get("district", "None"),
            "Zip Code": ip_info.get("zip", "None"),
            "Latitude": ip_info.get("lat", "None"),
            "Longitude": ip_info.get("lon", "None"),
            "Timezone": ip_info.get("timezone", "None"),
            "Offset": ip_info.get("offset", "None"),
            "ISP": ip_info.get("isp", "None"),
            "Organization": ip_info.get("org", "None"),
            "Reverse DNS": ip_info.get("reverse", "None"),
            "Mobile": ip_info.get("mobile", "None"),
            "Proxy": ip_info.get("proxy", "None"),
            "Hosting": ip_info.get("hosting", "None")
        }

        # Display information to the user
        print("IP Information:")
        for key, value in ip_data.items():
            print(f"{key}: {value}")

        # Ask if the user wants to save the data to a file
        save_to_file = input("Do you want to save this data to a text file? (y/n): ")
        if save_to_file.lower() in ("yes", "y"):
            filename = f"{ip_address}_info.txt"
            with open(filename, 'w') as file:
                for key, value in ip_data.items():
                    file.write(f"{key}: {value}\n")
            print(f"Data saved to {filename}")

if __name__ == "__main__":
    asyncio.run(main())
