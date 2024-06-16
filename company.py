from app.models.company import Company
company = Company(
    CompanyName="Test Company",
    CompanyDescription="This is a test company",
    WebsiteURL="http://test.com",
    Location="Test Location"
)
company.save()
print(company)
