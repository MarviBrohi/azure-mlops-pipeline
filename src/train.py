import argparse
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--n_estimators', type=int, default=100)
    parser.add_argument('--test_size', type=float, default=0.2)
    args = parser.parse_args()
    
    print(f"Loading data from: {args.data_path}")
    
    data = pd.read_csv(args.data_path)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=42
    )
    
    model = RandomForestClassifier(n_estimators=args.n_estimators, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average='weighted')
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/model.pkl')
    print("Model saved to outputs/model.pkl")

if __name__ == '__main__':
    main()
