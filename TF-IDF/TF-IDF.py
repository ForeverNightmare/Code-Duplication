from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.cluster import DBSCAN

import time
f = open("corpus2.txt")

lines = f.readlines()
corpus = []
file_list = []
for line in lines:
    t = line.replace("\n", '')
    file_name = line.split(' ')[0]
    file_list.append(file_name)
    file_name = file_name + ' '
    t = t.replace(file_name, '')
    corpus.append(t)
#print(file_list)
print(len(file_list))
#print(corpus)
length = len(corpus)
'''vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
word = vectorizer.get_feature_names()
print(word)
print(X.toarray())

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(X)
print(tfidf.toarray())'''

vectorizer = CountVectorizer()
transformer = TfidfTransformer()

tf_idf = transformer.fit_transform(vectorizer.fit_transform(corpus))

word = vectorizer.get_feature_names()

weight = tf_idf.toarray()
print(len(weight))
print(len(word))
'''for i in range(len(weight)):
    print(u"-------No.", i, u" file's tf-idf weight------")
    for j in range(len(word)):
        print(word[j], weight[i][j])'''

#k-means
'''start = time.time()
best_score = -10
best_k = 0
best_label = []
testlist = [82, 85, 87]
for i in testlist:
    print(i)
    #kmeans.fit(weight)
    # Center point
    #print(kmeans.cluster_centers_)
    #for index, label in enumerate(kmeans.labels_, 1):
     #   print("index: {}, label: {}".format(index, label))

    # the sum of each file's distance to the center point, the less the better
    # evaluate the n_cluster parameters
    #print("inertia: {}".format(kmeans.inertia_))
    kmeans_model = KMeans(n_clusters=i).fit(weight)
    #print(kmeans_model.labels_)
    score = silhouette_score(weight, kmeans_model.labels_, metric='euclidean')
    if score > best_score:
        best_score = score
        best_k = i
        best_label = kmeans_model.labels_
    print(score)

print(best_k)
#print(best_label)

output = open("class.txt", 'w', encoding='UTF-8')
output.write(str(best_k))
output.write("\n")
for i in range(len(file_list)):
    output.write(file_list[i] + " " + str(best_label[i]))
    output.write("\n")

end = time.time()
print(end-start)'''


start = time.time()
DBS_clf = DBSCAN(eps=1.1, min_samples=5)
DBS_clf.fit(weight)
print(DBS_clf.labels_)
end = time.time()
print(end-start)
output = open("class.txt", 'w', encoding='UTF-8')
for i in range(len(file_list)):
    output.write(file_list[i].replace("\n", "") + " " + str(DBS_clf.labels_[i]))
    output.write("\n")


score = silhouette_score(weight, DBS_clf.labels_, metric='euclidean')
print(score)
