# Problem 1 : Group Sold Products by the Date

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.groupby('sell_date').agg(
        num_sold = ('product','nunique'), 
        products = ('product', lambda x: ','.join(sorted(set(x)))
        )).reset_index()
    return activities.sort_values('sell_date')


# Problem 2 : Daily Leads and Partners

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(['date_id','make_name']).agg(
        unique_leads = ('lead_id','nunique'),
        unique_partners = ('partner_id','nunique')
    ).reset_index()


# Problem 3 : Actors and Directors who Cooperated At Least Three Times


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id','director_id']).count().reset_index()
    return df[df.timestamp>=3][['actor_id','director_id']]