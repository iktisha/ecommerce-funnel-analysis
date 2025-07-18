def calculate_funnel_counts(df):
    views = df[df['event_type'] == 'view']['user_id'].nunique()
    carts = df[df['event_type'] == 'cart']['user_id'].nunique()
    purchases = df[df['event_type'] == 'purchase']['user_id'].nunique()
    return {'views': views, 'carts': carts, 'purchases': purchases}

def print_funnel_counts(counts):
    print(f"Users who viewed products: {counts['views']}")
    print(f"Users who added products to cart: {counts['carts']}")
    print(f"Users who purchased products: {counts['purchases']}")

def calculate_conversion_rates(counts):
    views = counts.get('views', 0)
    carts = counts.get('carts', 0)
    purchases = counts.get('purchases', 0)

    view_to_cart = (carts / views * 100) if views else 0
    cart_to_purchase = (purchases / carts * 100) if carts else 0
    overall_conversion = (purchases / views * 100) if views else 0

    return {
        'view_to_cart_pct': view_to_cart,
        'cart_to_purchase_pct': cart_to_purchase,
        'overall_conversion_pct': overall_conversion
    }

def print_conversion_rates(rates):
    print(f"Conversion from View to Cart: {rates['view_to_cart_pct']:.2f}%")
    print(f"Conversion from Cart to Purchase: {rates['cart_to_purchase_pct']:.2f}%")
    print(f"Overall Conversion Rate: {rates['overall_conversion_pct']:.2f}%")

def hourly_funnel_counts(df):
    hourly_data = df.groupby(['hour', 'event_type'])['user_id'].nunique().unstack(fill_value=0)
    return hourly_data
