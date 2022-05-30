from enum import Enum
from typing import List


class Templates(Enum):
    Order = 'custom'


AVAILABLE_TEMPLATES: List[str] = [e.value for e in Templates]

TEST_TARGET_PHONE_NUMBER: str = '972542214311'
FROM_PHONE_NUMBER_ID: str = '106092558789170'
ACCESS_TOKEN: str = 'EAAXgDNmWZCEsBAPc5LrHX7bFiZA7GnCEYqVAVzFoVWqONHUOiIN1UYlnPiP64YF3SSBWRzSltvqnnSapogKSGXZAUNX9U' \
                    'lnacnZBCDMWr2aiR9NZBh8Nuod8Su6fVN0AgCvboe8cL8drJKfMyFZCeVnYmZBLmZAXXfpZAz8tdgOSeUoFA35UJn1ZBR4' \
                    'epC1n7LpCzKmPjUyZAinibLajrxTrRsr'
