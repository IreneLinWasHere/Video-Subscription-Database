#sample cases
#case 0
# months_subscribed = [1, 2, 2]
# ad_free_months = [1, 0, 2]
# video_on_demand_purchases = [3, 0, 1]

#case 1
# months_subscribed = [13, 4, 8]
# ad_free_months = [2, 0, 3]
# video_on_demand_purchases = [1, 7 ,3]

#case 2
# months_subscribed = [3, 1, 9]
# ad_free_months = [2, 1, 3]
# video_on_demand_purchases = [3, 1, 0]

#case 3
# months_subscribed = [12]
# ad_free_months = [11]
# video_on_demand_purchases = [4]

#case 4
months_subscribed = [1, 12, 3, 5, 1]
ad_free_months = [0, 1, 0, 5, 1]
video_on_demand_purchases = [7, 1, 2, 3, 0]

#case 5
# months_subscribed = [13, 4, 10]
# ad_free_months = [1, 2, 10]
# video_on_demand_purchases = [3, 1, 3]

#case 6
# months_subscribed = [13, 10, 10]
# ad_free_months = [1, 10, 10]
# video_on_demand_purchases = [3, 3, 3]

def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    print("Welcome to the Ada+ Account Dashboard")
    print()

    account_total_list= []
    ad_free_total_list = []
    on_demand_total_list = []

    
#per account summary
    for i in range(len(months_subscribed)):
    #total from subscriptions
        bundles = (months_subscribed[i]//3) * 18.00
        singles = (months_subscribed[i]%3) * 7.00
        subs_total = bundles + singles
        
  #total from ad-free upgrades
        ad_free_total = ad_free_months[i] * 2.00
        ad_free_total_list.append(ad_free_total)  
        
  #total from on demand
        on_demand_total= video_on_demand_purchases[i] * 27.99
        on_demand_total_list.append(on_demand_total)
        
   #account total
        account_total = subs_total + ad_free_total + on_demand_total
        account_total_list.append(account_total)
        
        print(f"Account {i+1} made ${account_total:.2f} total")
        print(f">>> ${subs_total:.2f} from monthly subscription fees")
        print(f">>> ${ad_free_total:.2f} from Ad-free upgrades")
        print(f">>> ${on_demand_total:.2f} from Video on Demand purchases")
        print()
        
  #combined all accounts
    combined = sum(account_total_list)
    premium_combined = sum(ad_free_total_list) + sum(on_demand_total_list)
    print (f"Combined all accounts made ${combined:.2f} total")
    print(f"Premium content (Ad-free watching and Video on Demand) made ${premium_combined:.2f} total")
    print()

#highest earner
    most_earned = max(account_total_list)
    print(f"${most_earned:.2f} was the most earned by any single account")
    
#highest earner acct nums
    #make new list of indexes with amount equal to most_earned
    acct_nums = [i for i, amount in enumerate(account_total_list) if amount == most_earned]
    #add 1 to indices to get acct nums
    acct_nums = [x+1 for x in acct_nums]
    #formatting for print
    acct_nums = ["#" + str(x) for x in acct_nums]
    acct_nums= ', '.join(acct_nums)
    print(f"The accounts that earned the most were: {acct_nums}")

subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases)