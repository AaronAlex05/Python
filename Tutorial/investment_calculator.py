import os

def calculate_future_value(principal, monthly_contribution, annual_rate, years, compounding_per_year=12):
    """
    Calculates the future value of an investment with compound interest and monthly contributions.
    Formula: FV = P(1 + r/n)^(nt) + PMT * [((1 + r/n)^(nt) - 1) / (r/n)] * (1 + r/n)
    """
    r = annual_rate / 100
    n = compounding_per_year
    t = years
    pmt = monthly_contribution

    # Future value of the principal
    fv_principal = principal * (1 + r/n)**(n*t)

    # Future value of the monthly contributions (annuity due)
    if r == 0:
        fv_contributions = pmt * 12 * t
    else:
        # We assume monthly contributions, so we adjust the formula for monthly rate
        monthly_rate = r / 12
        total_months = t * 12
        fv_contributions = pmt * (( (1 + monthly_rate)**total_months - 1 ) / monthly_rate) * (1 + monthly_rate)

    return fv_principal + fv_contributions

def adjust_for_inflation(future_value, inflation_rate, years):
    """
    Calculates the 'Real Purchasing Power' of a future sum given an inflation rate.
    Formula: Real Value = FV / (1 + i)^t
    """
    i = inflation_rate / 100
    return future_value / ((1 + i)**years)

def print_table(principal, monthly_contribution, rate, years, inflation_rate):
    print(f"\n{'Year':<6} | {'Total Balance':<15} | {'Real Value (Inflation Adj)':<25}")
    print("-" * 50)
    
    for year in range(1, years + 1):
        fv = calculate_future_value(principal, monthly_contribution, rate, year)
        real_fv = adjust_for_inflation(fv, inflation_rate, year)
        print(f"{year:<6} | ${fv:,.2f}{' ' * (14 - len(f'${fv:,.2f}'))} | ${real_fv:,.2f}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 40)
    print("   SMART INVESTMENT CALCULATOR   ")
    print("=" * 40)

    try:
        principal = float(input("Initial Principal ($): "))
        monthly_contribution = float(input("Monthly Contribution ($): "))
        annual_rate = float(input("Expected Annual Return (%): "))
        years = int(input("Investment Duration (Years): "))
        inflation_rate = float(input("Expected Inflation Rate (%): "))

        future_value = calculate_future_value(principal, monthly_contribution, annual_rate, years)
        real_value = adjust_for_inflation(future_value, inflation_rate, years)
        total_contributions = principal + (monthly_contribution * 12 * years)
        total_interest = future_value - total_contributions

        print_table(principal, monthly_contribution, annual_rate, years, inflation_rate)

        print("\n" + "=" * 40)
        print("          INVESTMENT SUMMARY          ")
        print("=" * 40)
        print(f"Total Contributions:   ${total_contributions:,.2f}")
        print(f"Total Interest Earned: ${total_interest:,.2f}")
        print(f"Final Balance:         ${future_value:,.2f}")
        print(f"Purchasing Power:      ${real_value:,.2f} (Real Value)")
        print("=" * 40)
        print("\nNote: Inflation adjustment uses a constant annual rate.")

    except ValueError:
        print("\nError: Please enter valid numbers.")

if __name__ == "__main__":
    main()
