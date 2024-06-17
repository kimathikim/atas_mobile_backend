from app.models.company import Company
from app.models import storage
company = Company(
    CompanyName="Test Company",
    CompanyDescription="This is a test company",
    WebsiteURL="http://test.com",
    Location="Test Location"
)
company.save()
print(company)
print()
print(storage.get(Company, company.id))
