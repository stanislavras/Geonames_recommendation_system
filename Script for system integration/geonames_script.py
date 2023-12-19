def clear_text(text):
    import re
    clear_text = re.sub(r'[^a-zA-Z]', ' ', text)
    clear_text = clear_text.split()
    clear_text = " ".join(clear_text)
    clear_text = clear_text.replace('https en wikipedia org wiki ','')
    clear_text = clear_text.replace('https ru wikipedia org wiki ','')
    return clear_text

class MyClass():
    def __init__(self, init_value):
        self.iv = init_value

    def geo(self, table):
        import pandas as pd
        result = pd.merge(self.iv, table, on="name")
        result = result.drop_duplicates()
        result = result.sort_values(by = ["score", "population"], ascending = False)
        result = result.drop(['corpus_id', 'population'], axis=1)
        result = result.to_dict(orient='records')
        return result

