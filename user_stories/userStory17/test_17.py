import pytest
import pandas as pd
import pandas as pd
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import user_stories
from user_stories import no_marriages_to_descendants


import pytest
import pandas as pd
import pandas as pd
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date


def test_no_marriages_to_descendants():
    families_details=[{'id': 'F1',
  'Husband ID': 'I2',
  'Husband Name': ' Steven /Brindley/',
  'Wife ID': 'I6',
  'Wife Name': ' Amy /Brooks/',
  'children': ['I1', 'I4'],
  'married': ' 9 JUN 1992',
  'divorced': ' 10 JUL 2015'},
  {'id': 'F3',
  'Husband ID': 'I4',
  'Husband Name': ' Tim /Brindley/',
  'Wife ID': 'I10',
  'Wife Name': ' Selina /Rosemary/',
  'children': ['I6'],
  'married': ' 3 APR 1967'}, {'id': 'F4',
  'Husband ID': 'I5',
  'Husband Name': ' Erin /Brooks/',
  'Wife ID': 'I6',
  'Wife Name': ' Josie /Campbell/',
  'children': ['I3'],
  'married': ' 7 APR 1967'}]
    df2=pd.DataFrame(families_details)
    
    strout= "ERROR:USERSTORY17 Parents should not marry any of their descendants"
     
    assert strout == no_marriages_to_descendants(df2)
    print('---')
    
    
    