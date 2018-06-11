# t-SNE http://www.scikit-yb.org/en/latest/api/text/tsne.html

from yellowbrick.text import TSNEVisualizer
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import HashingVectorizer
import codecs

class Corpus(object):
    def __init__(self, sentences):
        self.documents = codecs.open(sentences, encoding="utf-8").readlines()
        self.document_list = []
        for d in self.documents:
            self.document_list.append([d])

def load_corpus():
    c = Corpus("all_posts01.txt")
    return c
    

corpus = load_corpus()

#tfidf  = TfidfVectorizer(stop_words='english')
from sklearn.cluster import KMeans
vectorizer = TfidfVectorizer(max_df=0.5, max_features=10000,
                                 min_df=2,
                                 use_idf=True)
#transformer =  TfidfTransformer()
#tfidf = make_pipeline(hasher,transformer)
docs   = vectorizer.fit_transform(corpus.documents)

print(docs)

true_k = 500
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(docs)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

tsne = TSNEVisualizer(labels=["documents"])
tsne.fit(docs)
tsne.poof()