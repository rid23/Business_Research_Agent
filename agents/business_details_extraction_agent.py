from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from pprint import pprint
from .agent_schemas import BusinessProfile
from .sample_data import sample_website_content
from langchain_google_genai import ChatGoogleGenerativeAI



def extract_business_details(website_content: str) -> BusinessProfile:
    """
    Extracts business details from the provided website content using a structured LLM.

    Args:
        website_content (str): The content of the business website.

    Returns:
        BusinessProfile: The extracted business profile information.
    """



    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2)

    structured_llm = llm.with_structured_output(BusinessProfile)

    result = structured_llm.invoke(f"""
        Analyze the following business information and provide a structured output in the format of the BusinessProfile schema. If any information is missing, please leave it blank.
        Business Information:

        {website_content} 
        """)
    return result

if __name__ == "__main__":
    # Example usage
    website_content = sample_website_content
    business_profile = extract_business_details(website_content)
    business_profile_dict = business_profile.dict()  # Convert to dictionary
    pprint(business_profile_dict)  # Pretty print the dictionary
    #pprint(business_profile)

