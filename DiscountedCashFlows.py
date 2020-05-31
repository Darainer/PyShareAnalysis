#def ShareData(sharePrice, dividend, dividend_history: list, payout_ratio):
    #tuple sharePrice

def apply_percentage_change(base: float, increase_rate: float) -> float:
    next = base * (100 + increase_rate) / 100
    return next


def Calculate_return_metrics(start_price, current_dividend, share_price_increase_percent=4,
                             dividend_increase_percent=5, years=20, finalPEvalue=10, payout_ratio=0.5):

    current_price = start_price

    eps_growth = 0.05  # 5% earnings growth
    eps = current_dividend / payout_ratio
    PE_ratio = start_price/eps
    yearly_dividend = []
    cumulative_payout = []
    discounted_flow = 0.0
    for i in range(0, years):
        current_dividend = apply_percentage_change(current_dividend, dividend_increase_percent)
        yearly_dividend.append(current_dividend)
        discounted_flow += current_dividend
        cumulative_payout.append(discounted_flow)
        current_price = apply_percentage_change(current_price, share_price_increase_percent)

    price_at_PE = yearly_dividend[-1] * 1 / payout_ratio * finalPEvalue  # assume 50% payout
    total_expected_return = (discounted_flow + current_price) / start_price
    total_expected_return_atPE10 = (discounted_flow + price_at_PE) / start_price
    Dividend_payback_in_years = start_price / discounted_flow
    PEG_ratio = PE_ratio/eps_growth

    # print("dividends per year", yearly_dividend)
    print("PEG_ratio", PEG_ratio)
    print("discounted cash flow recieved", discounted_flow)
    print("expected value", current_price)
    print("total expected return %", total_expected_return * 100)
    print("total return with stock at average PE", total_expected_return_atPE10 * 100)
    print('')


# shell

#shell.start_price
Calculate_return_metrics(34,4,3,3,20,12,0.5)
#no_shares = 200000 / original_price
#total_portfolio_value = (discounted_flow + current_price) * no_shares
#print("portfolio contribution ", total_portfolio_value)
