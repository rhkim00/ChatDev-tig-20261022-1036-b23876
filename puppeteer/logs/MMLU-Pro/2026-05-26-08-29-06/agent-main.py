def calculate_partner_share():
    # Initial investments
    alcott_initial = 4000
    buxton_initial = 5000

    # Additional investments on May 1
    alcott_may = 2000
    buxton_may = 1750

    # Withdrawal on September 1
    alcott_withdrawal = 500

    # Additional investments on November 1
    alcott_november = 2000
    buxton_november = 2000

    # Total investments
    alcott_total = alcott_initial + alcott_may - alcott_withdrawal + alcott_november
    buxton_total = buxton_initial + buxton_may + buxton_november

    # Net profit
    net_profit = 8736

    # Calculate partner shares
    alcott_share = (alcott_total / (alcott_total + buxton_total)) * net_profit
    buxton_share = net_profit - alcott_share

    print("Alcott's total investment: $", alcott_total)
    print("Buxton's total investment: $", buxton_total)
    print("Net profit: $", net_profit)
    print("Alcott's share: $", round(alcott_share, 3))
    print("Buxton's share: $", round(buxton_share, 3))
    print("{'Alcott's share':", round(alcott_share, 3), ", 'Buxton's share':", round(buxton_share, 3), "}")

    return alcott_share, buxton_share

alcott_share, buxton_share = calculate_partner_share()