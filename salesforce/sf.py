import csv
import os
from typing import List, Dict, Any, Tuple

from simple_salesforce import Salesforce, SalesforceMalformedRequest

from utils.logger import console, logger

class sf:
    def __init__(self, name: str, instance: dict):
        self.name = name
        self.environment = instance.get('name')
        auth = instance.get('authentication', {})
        variables = instance.get('variables', {})
        if auth == "session":
            instance_url = instance.get("instance_url")
            session_id = variables.get("session_id")
            logger.info(f"Using session authentication for Salesforce, instance_url: {instance_url}, session_id: {session_id}")
            self.sf = Salesforce(instance_url=instance_url,
                                session_id=session_id)
        else:
            logger.critical("Unsupported authentication method for Salesforce. Only 'session' is currently supported.")
            console.print("[bold red]Unsupported authentication method for Salesforce. Only 'session' is currently supported.[/bold red]")
            exit(1)
        
        if self.check_connection():
            logger.info("Salesforce connection established successfully.")
            console.print(f"[bold green]Salesforce connection established successfully with {instance_url}.[/bold green]")
        else:
            logger.critical("Failed to connect to Salesforce.")
            console.print("[bold red]Failed to connect to Salesforce.[/bold red]")
            exit(1)
            
    def check_connection(self) -> bool:
        """Check if the Salesforce connection is valid."""
        try:
            self.sf.describe()
            return True
        except SalesforceMalformedRequest as e:
            logger.error(f"Connection error: {e}")
            return False
        
    def fetch_all_records(self, object_name):
        try:
            # Step 1: Get all field names — skip compound fields
            describe = self.sf.__getattr__(object_name).describe()
            field_names = [
                field['name'] for field in describe['fields']
                if field['type'] not in ('address', 'location') and not field['compoundFieldName']
            ]

            if not field_names:
                logger.info(f"No valid fields to query for {object_name}")
                return []

            # Step 2: Build query string
            field_list_str = ", ".join(field_names)
            query = f"SELECT {field_list_str} FROM {object_name}"

            # Step 3: Query using Bulk API
            logger.info(f"Using Bulk API for: {object_name}")
            job = self.sf.bulk.__getattr__(object_name).query(query)
            records = list(job)

            return records

        except Exception as e:
            logger.error(f"Error fetching {object_name} using Bulk API: {e}")
            return []
    
    def save_to_csv(self, records, path):
        if not records:
            logger.info(f"No records to save at {path}")
            return

        fieldnames = records[0].keys()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)