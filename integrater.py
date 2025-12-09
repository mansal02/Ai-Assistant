import subprocess
import pyautogui
import re
from index import get_llama_response

def parse_and_execute(response):
    """
    Parse Llama 3 response for commands and execute.
    Returns updated response.
    """
    original_response = response
    response_lower = response.lower()

    # Command mapping
    app_map = {
        'spotify': 'spotify',
        'notepad': 'notepad',
        'calculator': 'calc',
        'chrome': 'chrome'
    }

    # Open app command
    match = re.search(r'open\s+(\w+)', response_lower)
    if match:
        app_name = match.group(1)
        app_name_lower = app_name.lower()
        cmd = app_map.get(app_name_lower)
        if cmd:
            try:
                subprocess.run([cmd], shell=True)
                response += f" Opened {app_name}! "
            except Exception as e:
                response += f" Couldn't open {app_name}: {e} "
        else:
            response += f" App '{app_name}' not recognized. "

    # Volume control
    elif 'volume up' in response_lower:
        pyautogui.press('volumeup')
        response += " Volume increased! "

    elif 'volume down' in response_lower:
        pyautogui.press('volumedown')
        response += " Volume decreased! "

    # Play music
    elif 'play music' in response_lower or 'play spotify' in response_lower:
        try:
            subprocess.run(['start', 'spotify:'], shell=True)
            response += " Playing music! "
        except Exception as e:
            response += f" Couldn't play music: {e} "

    # Extend: Add more commands here

    return response

# Test
if __name__ == "__main__":
    query = "Open Spotify and turn up the volume."
    response = get_llama_response(query)
    final_response = parse_and_execute(response)
    print(final_response)
