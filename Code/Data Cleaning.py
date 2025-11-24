# Business
business['categories'] = business['categories'].fillna('Unknown')
business['address'] = business['address'].fillna('Unknown')
business['postal_code'] = business['postal_code'].fillna('Unknown')
business['attributes'] = business['attributes'].fillna('Unknown')
business['hours'] = business['hours'].fillna('Unknown')
business['city'] = business['city'].str.title()
business['state'] = business['state'].str.upper()

# Check for invalid star ratings
print(f"Check for invalid star ratings: {business[(business['stars'] > 5) | (business['stars'] < 0)]}")
print(f"check for null value: {business.isnull().sum()}")

business['main_cat'] = business['categories'].apply(lambda x: str(x).split(',')[0].strip() if x else 'Unknown')
business['main_cat'].value_counts().head(50)

def map_category(x):
    x = str(x).lower()

    # Food & Beverage
    food_keywords = ['restaurant','sandwiches', 'american (traditional)', 'american (new) ', 'italian', 'chinese','coffee & tea', 'fast food', 'breakfast & brunch','mexican', 'cafe', 'coffee', 'food', 'specialty food', 'pizza', 'bakeries', 'burgers', 'desserts', 'seafood', 'dessert', 'ice cream & frozen yogurt', 'chicken wings', 'bistro', 'brunch']
    if any(k in x for k in food_keywords):
        return 'Food & Beverage'

    # Health & Wellness
    wellness_keywords = ['beauty & spas', 'health & medical', 'nail salons ', 'hair', 'hair salons', 'barbers', 'beauty', 'hair removal', 'fitness & instruction', 'doctors','nail', 'fitness', 'wellness', 'clinic', 'chiropractic', 'optometrist', 'dentists']
    if any(k in x for k in wellness_keywords):
        return 'Health & Wellness'

    # Accommodation
    accommodation_keywords = ['hotels & travel ', 'hotels', 'inn', 'motel', 'hostel', 'apartments', 'lodge', 'bnb', 'bed and breakfast', 'apartment', 'vacation rental']
    if any(k in x for k in accommodation_keywords):
        return 'Accommodation'

    # Nightlife
    nightlife_keywords = ['bar', 'bars', 'nightlife', 'club', 'pub', 'lounge', 'karaoke', 'casino', 'brewery', 'wine']
    if any(k in x for k in nightlife_keywords):
        return 'Nightlife'

    # Retail
    retail_keywords = ['shopping', 'store', 'retail', 'market', 'boutique', 'supermarket', 'grocery', 'electronics', 'clothing', 'fashion', 'books', 'jewelry', 'furniture', 'pets', 'appliance']
    if any(k in x for k in retail_keywords):
        return 'Retail'

    # Professional Services
    service_keywords = ['law', 'event planning & services','accountant', 'financial services', 'consulting', 'real estate', 'professional services', 'travel', 'education', 'school', 'pet services', 'training']
    if any(k in x for k in service_keywords):
        return 'Professional Services'

    # Automotive
    automotive_keywords = ['automotive','car', 'auto repair', 'auto', 'mechanic', 'repair', 'tires']
    if any(k in x for k in automotive_keywords):
        return 'Automotive'

    # Active Life
    active_life_keywords = ['active life', 'sports', 'fitness', 'hiking', 'cycling', 'golf', 'yoga', 'gym', 'outdoor', 'climbing', 'swimming']
    if any(k in x for k in active_life_keywords):
        return 'Active Life'

    # Arts & Entertainment
    arts_entertainment_keywords = ['arts & entertainment', 'music', 'theater', 'gallery', 'cinema', 'comedy', 'performing arts', 'museum', 'festival', 'art']
    if any(k in x for k in arts_entertainment_keywords):
        return 'Arts & Entertainment'

    # Home Services
    home_services_keywords = ['home service', 'local services', 'plumber', 'home & garden', 'electrician', 'cleaning', 'pest control', 'landscaping', 'roofing', 'contractor', 'painting']
    if any(k in x for k in home_services_keywords):
        return 'Home Services'

    # Other
    return 'Other'

business['main_cat'] = business['main_cat'].apply(map_category)
business['main_cat'].value_counts()

business.to_csv('business_cleaned_with_category.csv', index=False)

print("business CSV cleaned and main categories mapped successfully!")

# Photos
# Fill missing values for optional columns
photos['caption'] = photos['caption'].fillna('No caption')
photos['label'] = photos['label'].fillna('Unknown')

# Ensure IDs are strings
photos['photo_id'] = photos['photo_id'].astype(str)
photos['business_id'] = photos['business_id'].astype(str)

# Optional: capitalize caption
photos['caption'] = photos['caption'].str.title()

# Check for invalid IDs
invalid_photo_ids = photos[photos['photo_id'].str.strip() == '']
invalid_business_ids = photos[photos['business_id'].str.strip() == '']
print(f"Invalid photo IDs: {len(invalid_photo_ids)}")
print(f"Invalid business IDs: {len(invalid_business_ids)}")

# Check for null values
print(f"Null values per column:\n{photos.isnull().sum()}")

# Remove duplicates
photos = photos.drop_duplicates(subset=['photo_id'])

# Save cleaned CSV
photos.to_csv('photos_cleaned.csv', index=False)

print("Photo CSV cleaned and saved as 'photo_cleaned.csv'")

# Fill missing values
photos['caption'] = photos['caption'].fillna('No caption')
photos['label'] = photos['label'].fillna('Unknown')

# Ensure IDs are strings
photos['photo_id'] = photos['photo_id'].astype(str)
photos['business_id'] = photos['business_id'].astype(str)

# Optional: clean captions
photos['caption'] = photos['caption'].str.title()

# Map label to main category
def map_category(x):
    x = str(x).lower()

    # Food & Beverage
    food_keywords = ['restaurant','sandwiches','italian','chinese','coffee','pizza','bakeries','burgers','desserts','seafood','cafe','fast food','brunch','breakfast','ice cream']
    if any(k in x for k in food_keywords):
        return 'Food & Beverage'

    # Health & Wellness
    wellness_keywords = ['beauty','spa','hair','nail','fitness','clinic','wellness','medical','doctor','dentist']
    if any(k in x for k in wellness_keywords):
        return 'Health & Wellness'

    # Nightlife
    nightlife_keywords = ['bar','club','pub','lounge','karaoke','brewery','wine','nightlife']
    if any(k in x for k in nightlife_keywords):
        return 'Nightlife'

    # Retail
    retail_keywords = ['store','shopping','market','boutique','grocery','electronics','fashion','clothing','jewelry','appliance']
    if any(k in x for k in retail_keywords):
        return 'Retail'

    # Arts & Entertainment
    arts_keywords = ['art','music','theater','gallery','cinema','museum','festival','comedy','performance']
    if any(k in x for k in arts_keywords):
        return 'Arts & Entertainment'

    # Home Services
    home_keywords = ['plumber','electrician','cleaning','pest','landscaping','roof','painting','contractor']
    if any(k in x for k in home_keywords):
        return 'Home Services'

    # Automotive
    auto_keywords = ['car','auto','mechanic','repair','tires']
    if any(k in x for k in auto_keywords):
        return 'Automotive'

    # Active Life
    active_keywords = ['gym','fitness','hiking','cycling','yoga','swimming','sports','climbing','golf']
    if any(k in x for k in active_keywords):
        return 'Active Life'

    return 'Other'

# Apply category mapping to photos using 'label'
photos['main_cat'] = photos['label'].apply(map_category)

# Check counts
print(photos['main_cat'].value_counts())

# Remove duplicates
photos = photos.drop_duplicates(subset=['photo_id'])

# Save cleaned photo CSV
photos.to_csv('photos_cleaned_with_category.csv', index=False)

print("Photos CSV cleaned and main categories mapped successfully!")

# Review
# Keep only relevant columns
review = review[['review_id', 'user_id', 'business_id', 'stars', 'text', 'date']]

# Fill missing values
review['text'] = review['text'].fillna('No review text')
review['stars'] = review['stars'].fillna(0)  # if any missing ratings, set to 0
review['date'] = review['date'].fillna('Unknown')

# Ensure IDs are strings
review['review_id'] = review['review_id'].astype(str)
review['user_id'] = review['user_id'].astype(str)
review['business_id'] = review['business_id'].astype(str)

# Remove duplicates based on review_id
review = review.drop_duplicates(subset=['review_id'])

# Clean review text: strip whitespace
review['text'] = review['text'].str.strip()

# Optional: convert date to datetime, errors='coerce' will convert invalid dates to NaT
review['date'] = pd.to_datetime(review['date'], errors='coerce')

# Check for invalid star ratings
invalid_stars = review[(review['stars'] > 5) | (review['stars'] < 0)]
print(f"Invalid star ratings:\n{invalid_stars}")

# Check for null values
print(f"\nNull values per column:\n{review.isnull().sum()}")

# Save cleaned review CSV
review.to_csv('review_cleaned.csv', index=False)

print("Review dataset cleaned and saved as 'review_cleaned.csv'")

# Checkin
checkin['date_list'] = checkin['date'].apply(lambda x: x.split(','))
checkin_explode = checkin.explode('date_list')
checkin_explode['checkin_time'] = pd.to_datetime(checkin_explode['date_list'].str.strip(), errors='coerce')

checkin_explode['year'] = checkin_explode['checkin_time'].dt.year
checkin_explode['month'] = checkin_explode['checkin_time'].dt.month
checkin_explode['day_of_week'] = checkin_explode['checkin_time'].dt.dayofweek
checkin_explode['hour'] = checkin_explode['checkin_time'].dt.hour

# Final cleaned checkin data
checkin = checkin_explode.dropna(subset=['checkin_time']).drop(columns=['date', 'date_list'])
checkin.info()

checkin.to_csv('checkin_cleaned.csv', index=False)

print("checkin dataset cleaned and saved as 'checkin_cleaned.csv'")

# User
# Drop irrelevant or redundant columns if any
user_clean = user.drop(columns=['friends'], errors='ignore')

# Handle missing values
user_clean = user_clean.fillna({
    'name': 'Unknown',
    'elite': 'None'
})

# Convert date columns
user_clean['yelping_since'] = pd.to_datetime(user_clean['yelping_since'], errors='coerce')

# Check for duplicates
user_clean = user_clean.drop_duplicates(subset='user_id')

# Feature: Calculate account age in years
from datetime import datetime
current_year = datetime.now().year
user_clean['account_age'] = current_year - user_clean['yelping_since'].dt.year

# Confirm cleaning
user_clean.info()

user_clean.to_csv('user_cleaned.csv', index=False)

print("checkin dataset cleaned and saved as 'user_cleaned.csv'")

# Tip
# Remove empty text entries
tip = tip[tip['text'].str.strip().notna()]

# Convert date column
tip['date'] = pd.to_datetime(tip['date'], errors='coerce')

# Handle null user/business IDs (if any)
tip = tip.dropna(subset=['user_id', 'business_id'])

# Remove duplicates
tip = tip.drop_duplicates(subset=['user_id','business_id','text'])

tip.to_csv('tip_cleaned.csv', index=False)

print("checkin dataset cleaned and saved as 'tip_cleaned.csv'")

# Export Cleaning Files in Once
SAMPLE_SIZE = 80_000
output_path = "yelp_cleaned_datasets_sampled.xlsx"


def sample_df(df, n=SAMPLE_SIZE):
    if len(df) > n:
        return df.sample(n=n, random_state=42)
    else:
        return df 

business_sample = sample_df(business)
review_sample = sample_df(review)
checkin_sample = sample_df(checkin)
user_sample = sample_df(user_clean)
tip_sample = sample_df(tip)

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    business_sample.to_excel(writer, index=False, sheet_name='Business')
    review_sample.to_excel(writer, index=False, sheet_name='Review')
    checkin_sample.to_excel(writer, index=False, sheet_name='Checkin')
    user_sample.to_excel(writer, index=False, sheet_name='User')
    tip_sample.to_excel(writer, index=False, sheet_name='Tip')

print("✅ Export completed: sampled datasets saved to 'yelp_cleaned_datasets_sampled.xlsx'")

