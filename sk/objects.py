sobjects = [
    "Account", 
    "Contact", 
    "User", 
    "AccountAccountRelation", 
    "AccountContactRelation", 
    "ContactContactRelation", 
    "PartyRoleRelation", 
    "ContactPointAddress",
    "ContactPointAddress",
    "PersonEmployment",
    "BenefitAssignment",
    "ProgramEnrollment",
    "Contact_Point_Financial__c",
    "Contact_Point_Identity__c",
    "Contact_Point_Nationality__c",
    "Account_Contact_Junction__c",
    "Register_Request__c",
    "Social_Indicator__c ",
]

record_types = [
    {
        "dev_name": "Person_Account",
        "name": "Person Account",
        "sobject": "Account",
    },
    {
        "dev_name": "Business_Account",
        "name": "Business Account",
        "sobject": "Account",
    },
    {
        "dev_name": "Household",
        "name": "Household",
        "sobject": "Account",
    },
    {
        "dev_name": "Organization",
        "name": "Organization",
        "sobject": "Account",
    },
    {
        "dev_name": "Service_Center",
        "name": "Service Center",
        "sobject": "Account",
    },
    {
        "dev_name": "Employee",
        "name": "Employee",
        "sobject": "Account",
    },
]