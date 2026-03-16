import csv,numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB
d=list(csv.reader(open("naive_bayes_words.csv"))); h,r=d[0],np.array(d[1:])
e={}; a=np.zeros(r.shape,int)
for i,x in enumerate(h):
    le=LabelEncoder(); a[:,i]=le.fit_transform(r[:,i]); e[x]=le
m=CategoricalNB().fit(a[:,:-1],a[:,-1])
print("\nEnter input values:")
v=[input("Outlook (Sunny/Overcast/Rain): "),
   input("Temperature (Hot/Mild/Cool): "),
   input("Humidity (High/Normal): "),
   input("Wind (Weak/Strong): ")]
u=np.array([[e[x].transform([y])[0] for x,y in zip(h[:-1],v)]])
p=m.predict(u); pr=m.predict_proba(u)
print("\nEntered input values:")
for x,y in zip(h[:-1],v): print(f"{x}: {y}")
print("\nPrediction:",e["PlayTennis"].inverse_transform(p)[0])
print("Class Probabilities:",pr)
