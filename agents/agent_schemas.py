from pydantic import BaseModel, Field

class BusinessProfile(BaseModel):
    """
    A Pydantic model representing a business profile.

    Attributes:
        Business_name (str): The name of the business.
        Business_industry (str): The industry of the business.
        Business_services (list): A list of services offered by the business.
        Target_customers (str): The target customers of the business.
        Business_description (str): A brief description of the business.
        services (list): A list of services offered by the business.
    """

    business_name: str = Field(..., description="The name of the business.")
    business_industry: str = Field(..., description="The industry of the business.")
    business_services: list = Field(..., description="A list of services offered by the business.")
    target_customers: str = Field(..., description="The target customers of the business.")
    business_description: str = Field(..., description="A brief description of the business.")



