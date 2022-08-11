import pytest # importing pytest
from datecalc import duration # importing function from the backend file which needs to be tested
from datecalc import when # importing function from the backend file which needs to be tested
from datetime import datetime, timedelta # importing datetime module

def test_for_days_difference():
#checking if the returned value is correct when inputting the start date and end date

  # Arrange
  end_date = datetime(2022,8,2)
  start_date = datetime(2021,7,6)
  expected_result = 392

  # Act
  final_act = abs((end_date - start_date).days)

  # Assert
  assert final_act == expected_result


def test_for_date_since_start_date():
#checking if the returned date is correct when inputting the start date and duration

  # Arrange
  start_date = datetime(2022,8,9)
  days_between = int(5)
  expected_result = datetime(2022,8,14)

  # Act
  final_act = start_date + timedelta(days=days_between)

  #Assert
  assert final_act == expected_result


