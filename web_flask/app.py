# Import the required packages
#!/usr/bin/python3
"""Flask app for book recommendation system"""
from flask import Flask, render_template, request, jsonify
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from web_flask.get_book import get_book_by_id


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


# Load the books data into a Pandas dataframe
books = pd.read_csv('books_data.csv')

# Combine the genres for each book into a single string
genres_combined = books['genre'].apply(lambda x: ' '.join(eval(x)))

# Create a TfidfVectorizer object to transform the book genres into a Tf-idf representation
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(genres_combined)

# Calculate the cosine similarity matrix between the books
cosine_similarity_matrix = cosine_similarity(tfidf_matrix)

# Create a dataframe with the cosine similarity scores
similarity_df = pd.DataFrame(cosine_similarity_matrix, index=books['title'], columns=books['title'])


@app.route('/')
@app.route('/home')
def home():
    """Route renders the home page"""
    return render_template('home.html')


@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    book_input = request.form.get('book')
    if book_input and books is not None:
        # Filter the books DataFrame to get similar book titles based on the user's input
        similar_books = books[books['title'].str.contains(book_input, case=False)]['title'].tolist()
        return jsonify(similar_books)
    else:
        return jsonify([])  # Return an empty list if no suggestions are available


@app.route('/recommendations', methods=['POST'])
def recommendations():
    """
        Route that renders recommendations post request
    """
    # Retrieve the user input from the form
    book_input = request.form.get('book')

    if book_input:
        try:
            # Find the index of the book in the similarity dataframe
            book_index = similarity_df.index.get_loc(book_input)

            # Get the top 15 most similar books to the input book
            top_15 = similarity_df.iloc[book_index].sort_values(ascending=False)[1:16]
            # Retrieve the book details based on the top 15 similar book titles
            recommendations_df = books.loc[books['title'].isin(top_15.index)]
            # convert the DataFrame to a list of dictionaries 
            recommendations = recommendations_df.to_dict(orient='records')
                
            return render_template('recommendations.html', recommendations=recommendations, book_input=book_input)
        except KeyError:
            # Handle the case where the book input is not found in the similarity dataframe
            error_message = "Book not found. Please try again."
            return render_template('error.html', error_message=error_message)


@app.route('/recommendations/book/<int:book_id>')
def book_details(book_id):
    """
        Route gets a specific book based on the id of the book click on from recommendations
    """
    book = get_book_by_id(str(book_id))
    if book:
        return render_template('book_details.html', book=book)
    else:
        # Handle the case when the book is not found, e.g., display an error message
        return render_template('book_not_found.html')


@app.route('/recommendations/genre/<genre>', methods=['GET'])
def genre_recommendations(genre):
    """
        Route that gets the genre recommendation when a
        specific genre is clicked on
    """
    # Filter the books dataframe based on the selected genre
    genre_books = books[books['genre'].str.contains(genre, case=False)]


    # Sort the DataFrame by rating and select the top 15 books
    top_15_books = genre_books.sort_values('rating', ascending=False).head(15)

    return render_template('genre_recommendations.html', genre=genre, books=top_15_books)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
