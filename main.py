import asyncio
from body_vts import VTubeStudioBody as CurrentBody 
# CHANGE 1: Import the new handler
from input_handler import InputHandler, speak_response
from integrater import parse_and_execute
from index import get_llama_response

async def main_loop():
    print("AI Assistant starting...")
    
    # CHANGE 2: Initialize the new Input Handler
    user_input = InputHandler()

    # Initialize Body
    body = CurrentBody()
    try:
        await body.connect()
    except Exception as e:
        print(f"Visual Body Connection Failed: {e}")

    while True:
        # CHANGE 3: Use the smart input function
        # We run it in a thread so it doesn't freeze the face animation
        query = await asyncio.to_thread(user_input.get_input)

        if query:
            # Get AI Logic Response
            llm_response = get_llama_response(query)
            
            # Execute Tools
            final_response = parse_and_execute(llm_response)
            
            # --- ANIMATION LOGIC ---
            response_lower = final_response.lower()
            if "sad" in response_lower or "sorry" in response_lower:
                await body.trigger_expression("dark_face")
            elif "love" in response_lower or "like" in response_lower:
                await body.trigger_expression("heart_eyes")
            elif "selfie" in response_lower:
                await body.trigger_expression("selfie_hand")
            elif "happy" in response_lower:
                await body.trigger_expression("star_eyes")
            
            # Speak
            await asyncio.to_thread(speak_response, final_response)
            
            await asyncio.sleep(1)

        await asyncio.sleep(0.1)

if __name__ == "__main__":
    try:
        asyncio.run(main_loop())
    except KeyboardInterrupt:
        print("Shutting down...")