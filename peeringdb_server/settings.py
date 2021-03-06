import os
from django.conf import settings

PEERINGDB_VERSION = getattr(settings, "PACKAGE_VERSION", "")
RDAP_URL = getattr(settings, "PEERINGDB_RDAP_URL", "https://rdap.db.ripe.net/")
RDAP_LACNIC_APIKEY = getattr(settings, "PEERINGDB_RDAP_LACNIC_APIKEY", None)
RDAP_RECURSE_ROLES = getattr(
    settings, "PEERINGDB_RDAP_RECURSE_ROLES", ["administrative", "technical"]
)
TUTORIAL_MODE = getattr(settings, "TUTORIAL_MODE", False)
AUTO_APPROVE_AFFILIATION = getattr(settings, "AUTO_APPROVE_AFFILIATION", False)
AUTO_VERIFY_USERS = getattr(settings, "AUTO_VERIFY_USERS", False)
MAINTENANCE_MODE_LOCKFILE = getattr(
    settings, "MAINTENANCE_MODE_LOCKFILE", "maintenance.lock"
)
