import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
df = pd.read_csv('netflix_titles.csv')
print(df.head())
print(df.shape)
print(df.info())
print(df.describe(include='all'))
#cleaning up data
df['date_added'] =pd.to_datetime(df['date_added'],errors='coerce')
df['year_added'] = df['date_added'].dt.year
print(df[['date_added', 'year_added']].head())
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('unknown')
#visualisation
content_by_year = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(10,5))
content_by_year.plot()
plt.title("Netflix Content Growth Over Years")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles Added")
plt.tight_layout()
plt.show()
#Insight: netflix Content Additions increased rapidly after 2015, indicating a strategic and aggressive push into original content and global expansion.

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type')
plt.title("Movies vs TV Shows on Netflix")
plt.tight_layout()
plt.show()

#Split multiple countries into searate row
country_series = (df.loc[df['country'] != 'Unknown' ,'country']. astype(str) .str.split(', ').explode())
# Get top 10 countries
top_countries = country_series.value_counts().head(10)
#plot
plt.figure(figsize=(10,5))
top_countries.plot(kind='bar')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()
#Insight: The United States leads in content production for Netflix, followed by India and the United Kingdom, reflecting Netflix's focus on these major markets.
#Final Insights:
#1. Netflix content additions increased rapidly after 2015,indicating aggressive global expansion.
#2. The apparent decline after 2018 is likely due to incomplete data for recent years rather than an actual slowdown.
#3. Movies dominate Netflix's catalog though TV shows are growing steadily.
#4. The United States lead in content production followed by India and United Kingdom, highlighting Netflix's global focus.

