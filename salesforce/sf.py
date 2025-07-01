from typing import List, Dict, Any, Tuple

from simple_salesforce import Salesforce, SalesforceMalformedRequest

from utils.logger import console, logger

class sf:
    def __init__(self, instance: dict):
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