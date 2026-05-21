from sklearn.linear_model import LinearRegression


def train_model(x, y):
    model = LinearRegression()
    model.flt(x, y)
    return model
