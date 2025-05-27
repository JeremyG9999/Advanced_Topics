import pandas as pd  
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

class TitanicClassifier:
    @staticmethod
    def main():
        # Load dataset
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, "titanic.csv")
        data_set = pd.read_csv(csv_path)
        print(data_set.shape)
        print(data_set.head())

        # Extract features and label
        independent = data_set.iloc[:, [2, 9]].values  
        dependent = data_set.iloc[:, 1].values  

        # Split data
        x_train, x_test, y_train, y_test = train_test_split(independent, dependent, test_size=0.50, random_state=0)  

        # Normalize
        sc = StandardScaler()
        x_train = sc.fit_transform(x_train)
        x_test = sc.transform(x_test)

        # Train model
        classifier = RandomForestClassifier(random_state=0)
        classifier.fit(x_train, y_train)  

        # Predict and evaluate
        y_pred = classifier.predict(x_test)
        print(x_test)
        print(y_test)
        print(y_pred)  
        cm = confusion_matrix(y_test, y_pred)  
        print(cm)
        print(classification_report(y_test, y_pred))

        # Classify a custom person
        fare = float(input("Enter fare: "))
        pclass = int(input("Enter Pclass as 1, 2, or 3: "))  
        sample = [[fare, pclass]]
        sample = sc.transform(sample)  
        answer = classifier.predict(sample)
        print("Prediction:", answer)
