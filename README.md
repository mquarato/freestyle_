## Stock Price and Performance Evaluation Application

This application is intended to do the following:

1) Retrieve stock market prices with google finance and return the prices onto the screen given a specific date range.  Once the user has visualized the data, the user can save the file to csv
2) Given a specific date range and the number of shares purchased, the application will return the gross profit (or loss) of the investment.

## Installation

Download the source code:

The source code is upload to github in the following repository:

```shell
git clone https://github.com/mquarato/freestyle_.git
cd Desktop/freestyle_
```
Requirements:

See requirements.txt file

## Usage

```shell
python3 freestyle_/app/freestyle.py
```
The user will be prompted to make one of two choices:

1) Stock Price
2) Stock Performance

For choice 1) the user will be able to retrieve closing price data for as many stocks as the user wishes, given a specific data range.  The range must be the same for all stock price returns.
For choice 2) the user will be able to retrieve the performance of a stock given a stock identifier and a purchase and sold date.  The dates must be open-stock market days.
