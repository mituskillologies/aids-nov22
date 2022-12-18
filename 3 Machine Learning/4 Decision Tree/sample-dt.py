from sklearn.tree import DecisionTreeClassifier 
clf = DecisionTreeClassifier()
#[height, hair-length, voice-pitch]
X = [[180,15,7],[167,42,2],[136,35,3],[174,15,8],[141,28,4]]

# Response variable
y = ['man', 'woman', 'woman', 'man', 'woman']
# Train the model
clf = clf.fit(X, y)
# Prediction
prediction = clf.predict([[165,30,9]])
print(prediction[0])  
