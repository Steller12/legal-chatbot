import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from datetime import datetime

# Set page configuration (must be first Streamlit command)
st.set_page_config(
    page_title="Legal Document Generator",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "generated_documents" not in st.session_state:
    st.session_state.generated_documents = []

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .document-preview {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("⚖️ Legal Document Generator")
st.markdown("""
This AI-powered chatbot helps you generate various legal documents. 
Simply describe what kind of legal document you need, and the AI will help you create it.
""")

# Document type selection with enhanced options
document_types = {
    "Non-Disclosure Agreement (NDA)": {
        "description": "Create a confidentiality agreement to protect sensitive information",
        "template": "NDA"
    },
    "Employment Contract": {
        "description": "Generate an employment agreement between employer and employee",
        "template": "Employment"
    },
    "Lease Agreement": {
        "description": "Create a rental agreement for residential or commercial property",
        "template": "Lease"
    },
    "Service Agreement": {
        "description": "Generate a contract for professional services",
        "template": "Service"
    },
    "Partnership Agreement": {
        "description": "Create an agreement between business partners",
        "template": "Partnership"
    },
    "Custom Document": {
        "description": "Generate a custom legal document based on your specific requirements",
        "template": "Custom"
    }
}

# Sidebar for document type selection
with st.sidebar:
    st.header("Document Type")
    selected_doc_type = st.selectbox(
        "Select Document Type",
        list(document_types.keys()),
        index=0
    )
    st.markdown(f"**Description:** {document_types[selected_doc_type]['description']}")

    st.header("Document History")
    if st.session_state.generated_documents:
        for doc in st.session_state.generated_documents:
            st.markdown(f"**{doc['type']}** - {doc['timestamp']}")
            if st.button(f"View {doc['type']}", key=f"view_{doc['timestamp']}"):
                st.text_area("Document Content", doc['content'], height=200)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # User input for document details
    user_input = st.text_area(
        "Describe your document requirements in detail:",
        placeholder="Example: I need an NDA for my software development company. The agreement should include confidentiality clauses, term duration of 2 years, and provisions for intellectual property protection.",
        height=150
    )

    # Additional document parameters
    with st.expander("Additional Parameters"):
        jurisdiction = st.text_input("Jurisdiction (e.g., California, USA)", "United States")
        duration = st.text_input("Duration of Agreement", "2 years")
        parties = st.text_input("Parties Involved", "Company and Employee")

    # Generate button
    if st.button("Generate Document", key="generate"):
        if not user_input:
            st.warning("Please provide details about the document you need.")
        else:
            with st.spinner("Generating your legal document..."):
                try:
                    # Create a prompt for Gemini
                    prompt = f"""You are a legal document generator. Create a professional {selected_doc_type} based on the following requirements.
                    Make sure the document is legally sound and includes all necessary sections and clauses.
                    Format the document with proper headings, sections, and legal terminology.
                    
                    Requirements:
                    - Jurisdiction: {jurisdiction}
                    - Duration: {duration}
                    - Parties: {parties}
                    - Additional Details: {user_input}
                    
                    Please generate a complete legal document with all necessary sections and clauses."""

                    # Initialize the model
                    model = genai.GenerativeModel('gemini-1.5-pro')
                    
                    # Generate the document
                    response = model.generate_content(prompt)
                    generated_document = response.text

                    # Store the generated document
                    st.session_state.generated_documents.append({
                        "type": selected_doc_type,
                        "content": generated_document,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })

                    # Display the generated document
                    st.subheader("Generated Document")
                    st.markdown('<div class="document-preview">', unsafe_allow_html=True)
                    st.text_area("Document Preview", generated_document, height=400)
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Add download button
                    st.download_button(
                        label="Download Document",
                        data=generated_document,
                        file_name=f"{selected_doc_type.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )

                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

with col2:
    st.header("Tips for Better Results")
    st.markdown("""
    1. Be specific about your requirements
    2. Include important details like:
       - Duration of agreement
       - Specific clauses needed
       - Any special conditions
    3. Mention the jurisdiction
    4. Specify the parties involved
    5. Include any specific legal terms
    """)

# Footer with disclaimer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><em>This tool is for informational purposes only and does not constitute legal advice. 
    Always consult with a qualified attorney for legal matters.</em></p>
</div>
""", unsafe_allow_html=True) 