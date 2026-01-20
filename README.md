# agent-1: Diagram Generation Agent

Investigation of a simple agent capable of generating Mermaid.js diagrams from various inputs.

## Features
- **Natural Language to Diagram**: Convert text descriptions into diagrams.
- **PDF to Diagram**: Analyze PDF content and visualize flows/structures.
- **Image to Diagram**: (Experimental) Convert images of diagrams or sketches into editable Mermaid code.


## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your Google Gemini API key:
   - Create a `.env` file in the root directory.
   - Add `GEMINI_API_KEY=your_api_key_here`.

## Usage

### Text to Diagram
```bash
python -m src.main "A user logs in, checks their balance, and logs out."
```

### PDF to Diagram
```bash
python -m src.main path/to/document.pdf --file
```

### Image to Diagram
```bash
python -m src.main path/to/diagram.png --file
```
