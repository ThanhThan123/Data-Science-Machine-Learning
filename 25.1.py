# Khong co label nen khong can bo tesst
# Tính giữa 2 vector(hàng) dùng cosine similarity
import pandas as pd
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity # new

def format_title(title):
    return title.replace("|", " ").replace("-", " ")

data = pd.read_csv("movies.csv", encoding="latin-1", sep="\t", usecols=["title", "genres"])
# data["genres"] = data["genres"].apply(format_title)
data["genres"] = data["genres"].apply(lambda title:title.replace("|", " ").replace("-",""))

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data["genres"])
tfidf_matrix_dense = pd.DataFrame(tfidf_matrix.todense(), index=data["title"],
                            columns=vectorizer.get_feature_names_out())

cosine_sim =  cosine_similarity(tfidf_matrix)
cosine_sim_dense = pd.DataFrame(cosine_sim, index=data["title"], columns=data["title"])

input_movie = "Jumanji (1995)"
top_k = 20
relevant_row = cosine_sim_dense.loc[input_movie, :]
result = relevant_row.sort_values(ascending=False)[:top_k].to_frame(name="score").reset_index()