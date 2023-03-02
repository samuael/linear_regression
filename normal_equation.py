def normalEquation(X,y):
  # ADD YOUR CODES
  return np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X),X)),np.transpose(X)),y)
  # return np.linalg.inv(np.matmul(np.transpose(X), X))
  # return np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)



  def mse(y, y_pred):
    # ADD YOUR CODES
    sum=0
    for  i in range(len(y)):
      sum+= (y[i]-y_pred[i])**2
    return sum/len(y)

   
   def split_data(X,Y, train_size):
  pole = int(len(X)*train_size)
  return X[: pole], X[pole: ], Y[:pole], Y[pole: ]