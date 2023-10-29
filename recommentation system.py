import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'User': ['User1', 'User2', 'User3', 'User4'],
    'Book1': [5, 4, 0, 0],
    'Book2': [0, 0, 4, 5],
    'Book3': [3, 0, 5, 0],
    'Book4': [0, 5, 0, 3],
}

df = pd.DataFrame(data)

cosine_sim = cosine_similarity(df.drop('User', axis=1))

def get_book_recommendations(book_title, cosine_sim=cosine_sim, df=df):
    book_index = df.columns.get_loc(book_title) - 1
    similar_scores = list(enumerate(cosine_sim[book_index]))
    similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)
    similar_books_indices = [i for i, score in similar_scores]

    recommended_books = []
    for index in similar_books_indices:
        if index != book_index:
            recommended_books.append(df.columns[index + 1])

    return recommended_books

user_input = input("Enter a user : ")

if user_input in df['User'].values:
    user_ratings = df[df['User'] == user_input].drop('User', axis=1)
    print("User", user_input, "has the following book recommendations:")
    for book_column in user_ratings.columns:
        if user_ratings[book_column].values[0] == 0:
            recommendations = get_book_recommendations(book_column)
            print(f"For {book_column}: {recommendations}")
else:
    print("User not found in the dataset.")
