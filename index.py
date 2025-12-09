import ollama

def get_llama_response(prompt, system_prompt="You are a helpful, lively PC assistant like Siri. Respond concisely, suggest actions (e.g., 'open Spotify'), and add fun VTuber cues like [smile] or [wave]. Keep responses under 100 words."):
    """
    Get response from Llama 3 via Ollama.
    """
    try:
        response = ollama.chat(
            model='llama3',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt}
            ],
            options={
                'temperature': 0.7,
                'num_predict': 150
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        print(f"Error from Ollama: {e}")
        return "Sorry, I couldn't process your request."

# Test it
if __name__ == "__main__":
    print(get_llama_response("What's the time? Open Notepad."))
