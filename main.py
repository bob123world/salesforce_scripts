from salesforce import sf, utils

def main():
    # List all Salesforce orgs
    print("Listing all Salesforce orgs:")
    print(utils.list_sf_orgs())

    # Get a specific Salesforce org by ID
    org_id = 3  # Example org ID
    print(f"\nGetting Salesforce org with ID {org_id}:")
    org = utils.get_sf_org(org_id=org_id, environment_name="DEVMICHQA")
    if org:
        print(org)
    else:
        print(f"No org found with ID {org_id}")

    sf_instance = sf.sf(org)
    # Check connection to the Salesforce org
    print("\nChecking connection to the Salesforce org:")
    if sf_instance.check_connection():
        print("Connection successful!")
    else:
        print("Connection failed.")



if __name__ == "__main__":
    main()