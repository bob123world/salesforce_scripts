import os

from salesforce import sf, utils
from utils.logger import console, logger
from sk import objects

def main():
    # List all Salesforce orgs
    logger.info("Listing all Salesforce orgs:")
    console.print(utils.list_sf_orgs())

    # Get a specific Salesforce org by ID
    org_id = 3  # Example org ID
    print(f"\nGetting Salesforce org with ID {org_id}:")
    org = utils.get_sf_org(org_id=org_id, environment_name="UAT")
    if org:
        print(org)
    else:
        print(f"No org found with ID {org_id}")

    sf_instance = sf.sf("Sociaal Kompas", org)

    for object in objects.sobjects:
        logger.info(f"Fetching records for object: {object}")
        records = sf_instance.fetch_all_records(object)
        if records:
            logger.info(f"Fetched {len(records)} records for object: {object}")
            # Save records to CSV
            csv_path = os.path.join("data", f"{sf_instance.name}", f"{sf_instance.environment}", f"{object}.csv")
            sf_instance.save_to_csv(records, csv_path)
            logger.info(f"Records saved to {csv_path}")
            console.print(f"[bold green]Records saved to {csv_path}[/bold green]")
        else:
            logger.warning(f"No records found for object: {object}")

if __name__ == "__main__":
    main()