# bookishread_project
A web app that allows users to input the title of a book they have read and gives recommendations based on genre
This is a flask app built with python
**Frontend:** HTML, CSS
**Backend:** python, flask, Jinja

# Getting Started
- Clone the repository in your local device.
- Install all the requirements using : ```pip install requirements.txt```
- Code could be run with
```
heroku local web`
# or
gunicorn web_flask.app:app
```
- Open with http://0.0.0.0:5000 in your browser to see the web app
## Algorithm used
- CONTENT BASED FILTERING: Content based recommender systems take into account the data provided by the user both directly or indirectly. For example, the book title inputed can the user can be used ot determine books the user may want to read based on the genre of the inputed book title. This type of recommender system relies on characteristics of object. New content can be quickly recommended to the user. These type of systems does not take into account behavior/ data about other users in the systems.

- COSINE SIMILARITY: Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

- Similarity Score : How does it decide which item is most similar to the item the user likes? Here come the similarity scores.

  - It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
 
## Glimpse of the web app
![Screenshot of the home page]![Screen Shot 2023-06-29 at 09 55 22](https://github.com/Nnenna-udefi/bookishread_project/assets/68693000/9e63923e-5c6f-4c0d-a0c2-41d0357f94aa)
)
![Screenshot of the popular books section](![Screen Shot 2023-06-29 at 09 55 31](https://github.com/Nnenna-udefi/bookishread_project/assets/68693000/cf9e7d3c-ab3f-4d46-8d92-ff5395235fbd)
)
![Screenshot of the recommendations page](![Screen Shot 2023-06-29 at 09 55 49](https://github.com/Nnenna-udefi/bookishread_project/assets/68693000/dfeada40-8277-4270-ac90-e3c1b0ab08b9)
)
![Screenshot of the book details page](![Screen Shot 2023-06-29 at 09 55 54](https://github.com/Nnenna-udefi/bookishread_project/assets/68693000/14b1b350-7c6a-41e8-ac4f-4e1398d36fea)
)
## Deployment
Deployed locally with heroku
Deployed gloally with render (https://render.com/)
- Render is the faster way to host your web apps and it does require verification of card details
- Deployment link : https://bookishreads.onrender.com/
