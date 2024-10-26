 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Read the dataset csv file
df = pd.read_csv("imdb-movies-dataset.csv")

#Filter the data to include only movies with Nicolas Cage in the cast
#We use case=false so filtering is case-insensitive: "Nicolas Cage", "nicolas cage", and "NICOLAS CAGE" can be recognized
df_cage = df[df['Cast'].str.contains('Nicolas Cage', case=False, na=False)].copy()

#Introduction to the app
st.header("\U0001F3AC Welcome to the World of Nicolas Cage!")
st.write("Join us on a cinematic journey as we explore the fascinating filmography of Nicolas Cage—an actor known for his quirky choices and remarkable performances! From *blockbuster hits* to *cult classics*, there's much to discover!")

st.write("---")

#Find the top 5 movies that Nicolas Cage has done by rating
top_movies = df_cage.nlargest(5, 'Rating')[['Poster', 'Title', 'Rating', 'Year', 'Description', 'Genre', 'Cast', 'Director']]
st.header("🏆Top 5 Highest-Rated Movies Starring Nicolas Cage:")

#For each movie, display facts such as the cover poster, rating, genre...
rank = 1
for index, row in top_movies.iterrows():
    st.markdown(f"### **Number {rank}**: {row['Title']} ({int(row['Year'])})")
    st.image(row['Poster'], width=150)
    st.write(f"**Rating**: {row['Rating']}/10")
    st.write(f"**Genre**: {row['Genre']}")
    st.write(f"**Director**: {row['Director']}")
    st.write(f"**Cast**: {row['Cast']}")
    st.write(f"**About**: {row['Description']}")           
    st.write("---")
    rank = rank + 1

#Diving into the statistics
st.header("📈Nic By The Numbers: Let's Take a Look at The Stats")
st.write("In this section, we’ll dive into some data-driven insights, giving you a glimpse of how Nicolas Cage's movies fare across different categories.")

st.write("---")

#Looking at film ratings:
st.write('### ⭐Exploring Ratings:')
st.write("This chart illustrates the distribution of Nicolas Cage's films across different rating categories.")

#Need to find the rating counts for all Nicolas Cage movies:
bins = [2,3,4,5,6,7,8]
labels = ['2-3','3-4','4-5','5-6','6-7','7-8']

#We do right=False so that the right edge of bins is not included
#For example, a rating of 3 would fall into the 2-3 category
df_cage['Rating Category'] = pd.cut(df['Rating'], bins=bins, labels=labels, right=False)
rating_counts = df_cage['Rating Category'].value_counts().sort_index()

#Create the bar chart
plt.figure(figsize=(10,6)) #10 inches width, 6 inches height
plt.bar(rating_counts.index, rating_counts.values, color='pink')
plt.title('Number of Movies by Rating Category')
plt.xlabel("Rating Categories")
plt.ylabel('Number of Movies')

st.pyplot(plt)

#Explain insights about the bar chart
st.write("### Insights:")
st.write("A significant number of his films fall into the **5-6** and **6-7 range**, where 10 is the highest rating possible. This indicates a trend towards average reception. This suggests that while Cage has some memorable performances, many of his choices may not resonate well with critics.")
st.write("On the flip side, several films in the **7-8 range** show that Cage has won over many viewers. Do you think these ratings reflect the quality of the films?")

#Looking at film genres:
st.write("---")
st.write('### 🎭Investigating Genres:')
st.write("This chart reveals the diverse genres that Nicolas Cage has explored throughout his career, showcasing the breadth of his filmography.")

genre_counts = df_cage['Genre'].str.get_dummies(sep=', ').sum()

#Create the bar chart 
plt.figure(figsize=(10, 6))
plt.bar(genre_counts.index, genre_counts.values, color='lightblue')  
plt.title('Number of Movies by Genre')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45, ha='right')  #Since titles are too long, we rotate the x labels for better readability
st.pyplot(plt)

#Explain insights
st.write("### Insights:")
st.write("It's clear that Cage has made a significant mark in **action**, **drama,** and **thriller** genres, which allow his unique acting style to shine. However, there are notably many comedy and crime movies, suggesting that he may enjoy playing roles in diverse genres.")
st.write("Cage's films often blend genres, which illustrates his versatility as an actor and leads to unique storytelling experiences.")
st.write("As you look at this genre distribution, consider this: What's your favorite genre that Cage has worked in?")

st.write("---")

#Looking at films over time:
st.write('### 📆 Diving Into Time:')
st.write("This chart examines the wide array of movies Nicolas Cage has been in over time, revealing quite a lengthy career.")

#Count movies per year
movies_per_year = df_cage['Year'].value_counts().sort_index()  

#Create the chart
plt.figure(figsize=(10, 6))  
plt.bar(movies_per_year.index, movies_per_year.values, color='lightgreen')
plt.title('Number of Movies Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45) #Rotate the x labels so the years are more visibly aligned with the bars
st.pyplot(plt)

#Explain insights
st.write("### Insights:")
st.write("It’s clear from the graph that **2014** was a monumental year for Nicolas Cage, featuring the highest number of movie releases (8) in his career This reflects a phase where Cage was particularly active in the film industry.")
st.write("The chart also shows a noticeable dip in movie releases from around 1970 to 1990. This might indicate a sabbatical or a shift in the types of projects Cage was pursuing during that time.")

st.write("---")

#Conclusion
st.header("🎉Conlusion: The Legendary Filmography of Nicolas Cage")
st.write("As we wrap up our journey through the captivating world of Nicolas Cage, it’s clear that his filmography is as diverse and intriguing as the man himself. Whether you’re a longtime fan or a newcomer to his unique style, we hope this exploration has sparked curiosity about his films.")
st.write("Thank you for joining us on this cinematic adventure! 🎬✨")
