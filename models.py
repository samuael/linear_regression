class LinearRegression:

  def __init__(self,cgs=True):
      # ADD YOUR CODES
      self.cgs = cgs
      self.theta = None
      
  def fit(self,x,y):
    # ADD YOUR CODES
    if self.cgs:
      Q, R = cgs(x)
      self.theta= backsubs(R, np.matmul( np.transpose(Q), y ))
    else:
      self.theta= normalEquation(x, y)

  def predict(self,x):
    #ADD YOUR CODES
    return np.matmul(x,self.theta)

    