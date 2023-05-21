import pickle

def predict_disease(symptoms):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict([symptoms])[0]