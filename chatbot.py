import openai
from datetime import date
import os

# Set your OpenAI API key here (preferably via environment variable)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY environment variable.")

client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Create the client

def collect_user_input():
    print("Welcome! Let's generate your legal document.")

    doc_type = input("What type of document would you like to generate? (e.g., NDA, Contract, Will, Agreement): ").strip()

    if doc_type.lower() == "nda":
        disclosing_party = input("Name of the Disclosing Party: ")
        receiving_party = input("Name of the Receiving Party: ")
        term = input("Duration of the NDA (in years): ")
        return {
            'doc_type': doc_type,
            'disclosing_party': disclosing_party,
            'receiving_party': receiving_party,
            'term': term,
            'date': date.today().strftime("%B %d, %Y")
        }
    elif doc_type.lower() == "contract":
        party_a = input("Name of Party A: ")
        party_b = input("Name of Party B: ")
        contract_details = input("Provide a brief description of the contract's terms: ")
        return {
            'doc_type': doc_type,
            'party_a': party_a,
            'party_b': party_b,
            'contract_details': contract_details,
            'date': date.today().strftime("%B %d, %Y")
        }
    elif doc_type.lower() == "will":
        testator_name = input("Name of the testator (the person writing the will): ")
        beneficiaries = input("List of beneficiaries (separate with commas): ")
        assets = input("List of assets to be distributed (separate with commas): ")
        return {
            'doc_type': doc_type,
            'testator_name': testator_name,
            'beneficiaries': beneficiaries,
            'assets': assets,
            'date': date.today().strftime("%B %d, %Y")
        }
    elif doc_type.lower() == "agreement":
        parties_involved = input("Name of the parties involved in the agreement (separate with commas): ")
        agreement_terms = input("Provide the terms of the agreement: ")
        return {
            'doc_type': doc_type,
            'parties_involved': parties_involved,
            'agreement_terms': agreement_terms,
            'date': date.today().strftime("%B %d, %Y")
        }
    else:
        print("Sorry, I can only generate NDA, Contract, Will, and Agreement documents for now.")
        return None

def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use the free-tier model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        document = response.choices[0].message.content.strip()
        return document
    except Exception as e:
        print(f"Error while generating response from GPT-3.5: {e}")
        return ""

def generate_document(data):
    if data['doc_type'].lower() == "nda":
        prompt = f"Generate a Non-Disclosure Agreement (NDA) between {data['disclosing_party']} and {data['receiving_party']} for a term of {data['term']} years, starting from {data['date']}. The NDA should include confidentiality terms and obligations for both parties."
    elif data['doc_type'].lower() == "contract":
        prompt = f"Generate a legal contract between {data['party_a']} and {data['party_b']} based on the following terms: {data['contract_details']}. The contract should include the rights and obligations of each party, as well as the effective date of {data['date']}."
    elif data['doc_type'].lower() == "will":
        prompt = f"Generate a last will and testament for {data['testator_name']} with the following beneficiaries: {data['beneficiaries']} and the following assets: {data['assets']}. Include instructions on asset distribution and any necessary legal language for a valid will. The date of the will is {data['date']}."
    elif data['doc_type'].lower() == "agreement":
        prompt = f"Generate a legal agreement between {data['parties_involved']} based on the following terms: {data['agreement_terms']}. The agreement should cover rights, responsibilities, and any obligations of each party, with the effective date being {data['date']}."
    else:
        print("Invalid document type.")
        return None

    document = ask_gpt(prompt)
    print("\nGenerated Document Content:")
    print(document)
    if not document:
        print("No content generated.")
        return

    print("\nGenerated Legal Document:")
    print(document)

    save_to_file = input("\nWould you like to save the document to a file? (yes/no): ").strip().lower()
    if save_to_file == "yes":
        file_name = f"documents/{data['doc_type'].lower()}_document_{data['date']}.txt"
        os.makedirs("documents", exist_ok=True)
        with open(file_name, "w") as f:
            f.write(document)
        print(f"\nDocument saved as {file_name}.")

# Main execution
if __name__ == "__main__":
    user_data = collect_user_input()
    if user_data:
        generate_document(user_data)
