"""
    Retirement Simulator
    Taxes were neglected in calculations as they are personal and vary.
"""
import csv
import os
from configuration import configuration


class Trinity2:
    def __init__(self, data_source_path=configuration['DATA_SOURCE'], portfolio_size=1000):
        self.data_source_path = data_source_path
        self.RETIRE_YEARS = configuration['RETIRE_YEARS']
        self.DRAW_PERCENTAGE = configuration['DRAW_PERCENTAGE']
        self.START_YEAR = configuration['START_YEAR']
        self.END_YEAR = configuration['END_YEAR']
        self.portfolio_size = portfolio_size

    def load_data(self):
        """
        :return: Parsed data list
        """
        _data = []
        # Check the data file exists.
        if not os.path.isfile(self.data_source_path):
            raise FileNotFoundError('Could not find CSV file {}'.format(self.data_source_path))
        # Read the CSV file, create a new list consists of a dictionary for every year
        with open(self.data_source_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                _data.append({'year': row['Year'], 's&p500': row['S&P500'],
                             '3-month': row['3-month T.Bill'], '10-year': row[' 10-year T. Bond']})
        return _data

    def test_safe_withdrawal(self, _data, year_started):
        """
        This function tests if the portfolio exhausted itself before RETIRE_YEARS years have passed
        :param _data: The data set of S&P 500 performance
        :param year_started: Simulated year to retire
        :return: True if the portfolio survived, False otherwise
        """
        years_survived = 0
        draw_amount = self.portfolio_size * self.DRAW_PERCENTAGE

        # if not starting from 1928, need to check how many years to skip
        years_counter = year_started - self.START_YEAR
        if years_counter < 0:
            raise RuntimeError('Can\'t process demos before 1928')
        # As long as the portfolio has enough money and RETIRE_YEARS haven't passed
        while self.portfolio_size > draw_amount and years_survived < self.RETIRE_YEARS:
            try:
                # Calculate the new portfolio amount
                self.portfolio_size = (self.portfolio_size - draw_amount) * \
                                      float(_data[years_survived + years_counter]['s&p500'])

            except IndexError:
                raise RuntimeError('There was a problem in calculating {} years from the year {}'
                                   .format(self.RETIRE_YEARS, year_started))
            years_survived += 1
        if years_survived == self.RETIRE_YEARS:
            return True
        return False

    def calculate(self):
        data = self.load_data()
        success_counter = 0
        test_cases_counter = 0
        # Get each year that is less than (the last year in the data set + RETIRE_YEARS).
        for year in range(self.START_YEAR, self.END_YEAR + 1 - self.RETIRE_YEARS):
            test_cases_counter += 1
            if self.test_safe_withdrawal(data, year):
                success_counter += 1
        success_rate = success_counter / test_cases_counter
        print('The portfolio endured in {:.2f}% of the test cases for {}% withdrawal rate.'
              .format(success_rate * 100, self.DRAW_PERCENTAGE * 100))
