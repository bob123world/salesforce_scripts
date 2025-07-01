from salesforce import sf, utils
from utils.logger import console, logger

def main():
    # List all Salesforce orgs
    logger.info("Listing all Salesforce orgs:")
    console.print(utils.list_sf_orgs())

    # Get a specific Salesforce org by ID
    org_id = 3  # Example org ID
    print(f"\nGetting Salesforce org with ID {org_id}:")
    org = utils.get_sf_org(org_id=org_id, environment_name="QA")
    if org:
        print(org)
    else:
        print(f"No org found with ID {org_id}")

    sf_instance = sf.sf(org)

if __name__ == "__main__":
    main()