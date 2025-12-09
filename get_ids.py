# get_ids.py
import asyncio
import pyvts

async def main():
    # Define plugin info
    plugin_info = {
        "plugin_name": "MARIE Core",
        "developer": "Mansal",
        "authentication_token_path": "./token.txt"
    }
    
    myvts = pyvts.vts(plugin_info=plugin_info)
    print("Connecting to VTube Studio...")
    await myvts.connect()
    
    # Authenticate
    print("Check your VTube Studio screen and click 'Allow' if asked!")
    await myvts.request_authenticate_token()
    await myvts.request_authenticate()
    
    # Get List of Hotkeys
    print("\n--- YOUR HOTKEY IDs (COPY THESE) ---")
    response = await myvts.request(myvts.vts_request.requestHotKeyList())
    
    # Print them nicely
    if "data" in response and "availableHotkeys" in response["data"]:
        for hotkey in response["data"]["availableHotkeys"]:
            print(f"Name: {hotkey['name']}")
            print(f"ID:   {hotkey['hotkeyID']}")
            print("-" * 20)
    else:
        print("No hotkeys found! Did you set up Hotkeys in VTube Studio settings?")

    await myvts.close()

if __name__ == "__main__":
    asyncio.run(main())