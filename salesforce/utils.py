import json

def list_sf_orgs() -> str:
    """
    Lists all Salesforce orgs from the configuration file.

    Returns:
        List[str]: A list of Salesforce org names.
    """
    return_str = "id - org - environment\n"
    config = read_sf_orgs_config()
    for org in config.get('orgs', []):
        for environment in org.get('environments', []):
            if environment.get('name'):
                return_str += f"{org['id']} - {org['name']} - {environment['name']}\n"
    return return_str

def get_sf_org(org_id: int = None, org_name: str = None, environment_name: str = None) -> dict:
    """
    Retrieves a specific Salesforce org from the configuration.

    Args:
        org_id (int, optional): The ID of the org to retrieve.
        org_name (str, optional): The name of the org to retrieve.
        environment_name (str, optional): The name of the environment to retrieve.

    Returns:
        dict: The requested Salesforce org information, or an empty dict if not found.
    """
    config = read_sf_orgs_config()
    for org in config.get('orgs', []):
        if org_id == org.get('id') or org_name == org.get('name'):
            for environment in org.get('environments', []):
                if environment_name == environment.get('name'):
                    return environment
    return {}

def read_sf_orgs_config():
    """
    Reads the Salesforce orgs configuration file and returns the content as a dictionary.

    Returns:
        dict: Configuration data.
    """
    with open('salesforce_orgs.json', 'r') as file:
        config = json.load(file)
    return config