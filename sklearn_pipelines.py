# Pipeline imports
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import make_column_transformer

# Preprocessing imports
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

# Modelling
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier

# Build pipeline for different types of features
pipeline_text = make_pipeline(CountVectorizer(ngram_range=(1,1), max_features=1000), TfidfTransformer())
pipeline_numerical = make_pipeline(SimpleImputer(strategy='median'), MinMaxScaler())

# Uses a column transformer to assign correct pipeline to each column
preprocess = make_column_transformer(
    (pipeline_text, 'colname_1'),
    (pipeline_text, 'colname_2'),
    (pipeline_numerical, col_names_list)
)

# Assemble preprocessing pipeline with model.
model = Pipeline([('prep', preprocess), 
                  ('clf', GradientBoostingClassifier())])

# Some parameters for grid search
parameters = {'clf__n_estimators': (200, 800),
              'clf__max_depth': (2, 3, 5)}

# Grid Search with informed params
gs_clf = GridSearchCV(model, parameters, n_jobs=-1)
gs_clf = gs_clf.fit(X_train, y_train)
