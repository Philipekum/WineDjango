import pickle
import pandas as pd


def load_prediction_model():
    prediction_model = pickle.load(open('WineAnalyzer/prediction_model.pkl', 'rb'))

    return prediction_model


def combine_to_df_and_predict(response):
    columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
               'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
               'pH', 'sulphates', 'alcohol']
    df = pd.DataFrame(
        [[response['fixed_acidity'], response['volatile_acidity'], response['citric_acid'], response['residual_sugar'],
          response['chlorides'], response['free_sulfur_dioxide'], response['total_sulfur_dioxide'], response['density'],
          response['ph'], response['sulphates'], response['alcohol']]], columns=columns)

    prediction_model = load_prediction_model()

    return prediction_model.predict(df)
