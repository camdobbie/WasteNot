import pandas as pd


cats = ["Baking", "Bread and bakery", "Breakfast foods", "Canned foods", "Condiments", "Dairy and eggs", "Drinks", "Frozen", "Fruits and vegetables", "Herbs and spices", "Meats and seafood", "Other", "Pasta, rice and beans", "Snacks"]


"""
def makeDict(category):
    #load Categories_Ingredients/Canned_foods.csv as a pandas dataframe
    df = pd.read_csv(f'Categories_Ingredients/{category}.csv')

    #create a dictionary with raw_ingredients as the keys and simplified_ingredients as the values
    d = dict(zip(df.raw_ingredients, df.simplified_ingredients))

    # create a df of the keys and values
    df2 = pd.DataFrame(list(d.items()), columns=['raw_ingredients', 'simplified_ingredients'])
    #print the size of the df

    #save the df as a csv file
    df2.to_csv(f'Dictionaries/{category}.csv', index=False)

for cat in cats:
    makeDict(cat)
"""

df = pd.read_csv('ingredients_150_recipes.csv')
df['raw_ingredients'] = df['raw_ingredients'].str.strip()

for cat in cats:

    cat2 = cat.replace(" ", "_")
    cat2 = cat2.replace(",", "")

    #for all rows with category in the section column, add column called 'simplified_ingredits' with the value of the simplified ingredient according to the dictionary described in Dictionaries/category.csv
    df.loc[df['section'] == cat, 'simplified_ingredients'] = df['raw_ingredients'].map(pd.read_csv(f'Dictionaries/{cat2}.csv').set_index('raw_ingredients')['simplified_ingredients'])
    
#print any rows of df that have a NaN value in the simplified_ingredients column
undefinedDataframe = df[df['simplified_ingredients'].isnull()]
print(undefinedDataframe)

#for each row in undefinedDataframe, ask the user to input the simplified ingredient and update the df
for index, row in undefinedDataframe.iterrows():
    print(f"Please enter the simplified ingredient for {row['raw_ingredients']}: ")
    undefinedDataframe.at[index, 'simplified_ingredients'] = input()

print(undefinedDataframe)