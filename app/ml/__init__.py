from app.data.loader import load_from_file, load_object
from app.ml.metrics import get_accuracy, get_probablity
from sklearn.preprocessing import LabelEncoder

def _predict_class(config, lead):
    _true_status = config.get("true_status")
    _category_cols = config.get('category_cols')
    
    print("Loading data... ")
    _df = load_object(lead)
    print("Data Loaded... ")
    print(_df.head())
    print("Shape: ",_df.shape)
    print('Original df \n')
    print(_df)
    
    if(_category_cols):
        print("Encoding data")
        print(_category_cols)
        for _col,_classes in _category_cols.items():
            encoder = LabelEncoder()
            encoder.classes_ = _classes
            _df[_col] = encoder.transform(_df[_col])

    print('Transformed df \n')
    print(_df)
    _model = load_from_file(config.get("model_dump_file_path"))
    print('Predicting the score...')
    _cls , _probability = get_probablity(_model, _df.iloc[:,1:].values, _true_status) #iloc to skip first column which has id
    print(_cls, _probability)
    _score = round(_probability*100, 2)

    return _score, _cls
