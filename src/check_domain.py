import os

import requests


class CheckDomain:
    def __init__(self):
        self.domain_url = os.getenv('GET_DOMAIN_URL')

    def check_domain(self, domain_name: str) -> dict:
        domains = requests.get(
            self.domain_url.replace('<domain_name', domain_name)
        )

        return domains
