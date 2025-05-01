# Legal Document Generator

An AI-powered chatbot that helps generate various legal documents using Google's Gemini AI model.

## Features

- Generate various types of legal documents
- User-friendly web interface with modern design
- Document preview and download functionality
- Document history tracking
- Support for multiple document types
- Custom document generation
- Additional parameters for precise document generation
- Responsive layout with tips and guidance

## Prerequisites

- Python 3.8 or higher
- Google API Key (free)
- Internet connection

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd legal-document-generator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Google API key:
```
GOOGLE_API_KEY=your-api-key-here
```

To get a free Google API key:
1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key and paste it in your `.env` file

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Using the application:
   - Select the type of document you want to generate from the sidebar
   - Provide detailed requirements in the main text area
   - Optionally, expand "Additional Parameters" to specify:
     - Jurisdiction
     - Duration of agreement
     - Parties involved
   - Click "Generate Document"
   - Review the generated document
   - Download the document if needed
   - View your document history in the sidebar

## Available Document Types

- Non-Disclosure Agreement (NDA)
  - For protecting confidential information
- Employment Contract
  - For employer-employee relationships
- Lease Agreement
  - For rental properties
- Service Agreement
  - For professional services
- Partnership Agreement
  - For business partnerships
- Custom Document
  - For unique legal requirements

## Tips for Better Results

1. Be specific about your requirements
2. Include important details like:
   - Duration of agreement
   - Specific clauses needed
   - Any special conditions
3. Mention the jurisdiction
4. Specify the parties involved
5. Include any specific legal terms

## Security

- Your Google API key is stored locally in the `.env` file
- Generated documents are stored in the session and cleared when you close the browser
- No data is stored permanently on any server

## Disclaimer

This tool is for informational purposes only and does not constitute legal advice. Always consult with a qualified attorney for legal matters. The generated documents should be reviewed by a legal professional before use.

## License

MIT License

## Support

For support or feature requests, please open an issue in the repository. 