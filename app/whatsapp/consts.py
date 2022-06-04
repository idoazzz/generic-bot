from enum import Enum
from typing import List


class Templates(Enum):
    Order = 'custom'


AVAILABLE_TEMPLATES: List[str] = [e.value for e in Templates]

TEST_TARGET_PHONE_NUMBER: str = '972542214311'
FROM_PHONE_NUMBER_ID: str = '106092558789170'
ACCESS_TOKEN: str = 'EAAXgDNmWZCEsBAIfAZA95IUX0GAClKMhOU82NHB4q1gGDT5vfGRx4wTZBxOmRRqh6ezFLFrp1cTkCJ7ZCcpR1' \
                    'dx9XogBPRebd9bTLkEppW8FOOMY32805SJWSlrEmSZCV9zQtHJb4eZANKhgphrvPCEK0rWfagtd8DZC8MeWWD3' \
                    'tcOJrInU5GbcWKeZAC1x5ZBVMbxKfiFc1ISLpBRZAAbOR4gZAG8gVZAdeo1EZD'
