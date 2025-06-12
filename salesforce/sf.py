from typing import List, Dict, Any, Tuple

from simple_salesforce import Salesforce, SalesforceMalformedRequest

class sf:
    def __init__(self, instance: dict):
        auth = instance.get('authentication', {})
        variables = instance.get('variables', {})
        if auth == "session":
            self.sf = Salesforce(instance_url=instance.get("instance_url"),
                                session_id=variables.get("session_id"))
            
    def check_connection(self) -> bool:
        """Check if the Salesforce connection is valid."""
        try:
            self.sf.describe()
            return True
        except SalesforceMalformedRequest as e:
            print(f"Connection error: {e}")
            return False