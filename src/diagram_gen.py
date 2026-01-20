import os
from google import genai
from google.genai import types

def generate_mermaid(context, input_type: str = "text") -> str:
    """
    Sends the context to Gemini to generate a Mermaid diagram.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY not found in environment variables."

    client = genai.Client(api_key=api_key)
    
    # using gemini-1.5-flash for speed and multimodal capabilities
    model = "gemini-1.5-flash"

    base_prompt = """
    You are an expert at creating Mermaid.js diagrams.
    Your task is to generate valid Mermaid.js code based on the provided input.
    
    Rules:
    1. Return ONLY the Mermaid code block. Do not include markdown naming like ```mermaid or ```.
    2. Start directly with 'graph TD' (or appropriate type).
    3. Ensure the syntax is correct and will render properly.
    4. Make the diagram comprehensive but readable.
    """

    try:
        content = []
        if input_type == "image":
            # context is expected to be a PIL Image or similar supported object
            content.append(base_prompt + "\nAnalyze this image and convert it into a corresponding Mermaid diagram.")
            content.append(context)
        else:
            # context is text string
            content.append(f"{base_prompt}\n\nInput Context:\n{context}\n\nGenerate the mermaid code:")
        
        response = client.models.generate_content(
            model=model,
            contents=content
        )
            
        return response.text.strip().replace("```mermaid", "").replace("```", "").strip()
        
    except Exception as e:
        return f"Error generation diagram: {str(e)}"
