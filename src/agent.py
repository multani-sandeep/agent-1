import os
from .diagram_gen import generate_mermaid
from .pdf_processor import extract_text_from_pdf
from .image_processor import process_image

def run_agent(input_data: str, is_file: bool = False) -> str:
    """
    Main agent entry point.
    Determines input type and orchestrates the generation process.
    """
    context = None
    input_type = "text"

    if is_file:
        if not os.path.exists(input_data):
            return f"Error: File '{input_data}' not found."
        
        _, ext = os.path.splitext(input_data)
        ext = ext.lower()
        
        if ext == '.pdf':
            input_type = "pdf"
            print(f"Processing PDF: {input_data}")
            context = extract_text_from_pdf(input_data)
        elif ext in ['.png', '.jpg', '.jpeg']:
            input_type = "image"
            print(f"Processing Image: {input_data}")
            context = process_image(input_data)
        else:
            return f"Error: Unsupported file type '{ext}'"
    else:
        context = input_data

    # Validation
    if input_type != "image":
        if not context or not isinstance(context, str) or not context.strip():
            return "Error: Could not extract context from input."
    elif context is None:
         return "Error: Could not load image."

    diagram_code = generate_mermaid(context, input_type)
    return diagram_code
