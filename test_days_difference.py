import pytest # importing pytest
from datecalc import duration # importing function from the backend file which needs to be tested
from datecalc import when # importing function from the backend file which needs to be tested
from datetime import datetime, timedelta # importing datetime module

def test_for_days_difference():
  d1 = datetime(2022,8,2)
  d2 = datetime(2021,7,6)
  assert duration(d1,d2) == 392

def test_for_date_since_start_date():
#checking if the returned date is correct when inputting the start date and duration
  d1 = datetime(2022,8,9)
  dur = int(5)
  assert when(d1,dur) == datetime(2022,8,14)
