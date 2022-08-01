import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Model():
    def __init__(self,input=np.array([]),y=np.array([]),neurdim = []):
        #most important data
        self.inputdata = input
        self.y = y
        self.neurondimensions = neurdim

        #Variables to change in order to tweek things
        self.alpha = 0.1
        self.epsilon = 2
        self.gradcheckeps = 0.00001
        self.lamb = 0.2
        self.epochs = 4000

        try:
            self.examnum = self.inputdata.shape[1]
        except:
            self.examnum = 1
        
        self.neurondim = tuple((x,self.examnum) for x in self.neurondimensions)
        self.thetadim = tuple((self.neurondim[i+1][0],self.neurondim[i][0]+1) for i in range(len(self.neurondim)-1))

        #configuring parts
        self.theta = np.zeros((sum([x[0]*x[1] for x in self.thetadim]),1))
        self.thetamatrices = [np.zeros(i) for i in self.thetadim]
        self.D = np.zeros((sum([x[0]*x[1] for x in self.thetadim]),1))
        self.Dmatrices = [np.zeros(i) for i in self.thetadim]
        self.normalizedata()
        self.randomizetheta()
        self.hyp = np.zeros((neurdim[-1],self.examnum))

    def normalizedata(self):
        self.mu = np.mean(self.inputdata)
        self.s = np.std(self.inputdata)
        self.inputdata = (self.inputdata-self.mu)/self.s

    def unrolltheta(self):
        prevend = 0
        for i in range(len(self.thetamatrices)):
            curend = prevend + self.thetamatrices[i].size
            self.thetamatrices[i] = self.theta[prevend:curend].reshape(self.thetadim[i])
            prevend = int(curend)            

    def rolltheta(self):
        self.theta = (self.thetamatrices[0]).ravel().reshape(-1,1)
        for i in self.thetamatrices[1:]:
            th = i.ravel().reshape(-1,1)
            self.theta = np.concatenate((self.theta,th))

    def rolld(self):
        self.D = (self.Dmatrices[0]).ravel().reshape(-1,1)
        for i in self.Dmatrices[1:]:
            d = i.ravel().reshape(-1,1)
            self.D = np.concatenate((self.D,d))

    def unrolld(self):
        prevend = 0
        for i in range(len(self.Dmatrices)):
            curend = prevend + self.Dmatrices[i].size
            self.Dmatrices[i] = self.D[prevend:curend].reshape(self.thetadim[i])
            prevend = int(curend)

    def randomizetheta(self):
        self.theta = np.random.rand(self.theta.shape[0],self.theta.shape[1])*(2*self.epsilon)-self.epsilon

    def sigmoid(self,array):
        if len(array.shape) == 1:
            return 1/(1+np.exp(-array)).reshape(-1,1)
        else:
            return 1/(1+np.exp(-array))

    def cost(self):
        a = (-1/self.examnum)*np.sum(self.y*np.log(self.hyp)+(1-self.y)*np.log((1-self.hyp)))
        regparameter = (self.lamb/(2*self.examnum))*sum([np.sum(np.square(i[:,1:])) for i in self.thetamatrices])
        return a+regparameter
        
    def fp(self):
        self.unrolltheta()

        ones1 = np.ones((1,self.examnum))
        self.amatrices = [np.zeros((i[0]+1,i[1])) if i!= self.neurondim[-1] else np.zeros(i) for i in self.neurondim]
        self.amatrices[0] = np.concatenate((ones1,self.inputdata))

        for i in range(1,len(self.neurondim)-1):
            z = np.matmul(self.thetamatrices[i-1],self.amatrices[i-1])
            ones = np.ones((1,self.examnum))
            self.amatrices[i] = np.concatenate((ones,self.sigmoid(z)))
        
        zlast = np.matmul(self.thetamatrices[-1],self.amatrices[-2])
        self.amatrices[-1] = self.sigmoid(zlast)
        self.hyp = np.array(self.amatrices[-1])        

    def bp(self):
        newy = self.y.reshape(-1,1).T
        self.deltamatrices = [np.zeros((i[0]+1,i[1])) if i!= self.neurondim[-1] else np.zeros(i) for i in self.neurondim[1:]]

        
        self.deltamatrices[-1] = self.hyp-self.y

        for i in range(len(self.deltamatrices)-1,0,-1):
            if i == len(self.deltamatrices)-1:
                d1 = np.matmul(self.thetamatrices[i].T,self.deltamatrices[i])
            else:
                strippedd = self.deltamatrices[i][1:,:]
                d1 = np.matmul(self.thetamatrices[i].T,strippedd)
            d2 = np.multiply(self.amatrices[i],(1-self.amatrices[i]))
            self.deltamatrices[i-1] = np.multiply(d1,d2)

        for i in range(len(self.Dmatrices)):
            if i == len(self.Dmatrices)-1:
                dbias = (np.matmul(self.deltamatrices[i],self.amatrices[i].T)[:,0] / self.examnum).reshape(-1,1)
                dmain = (np.matmul(self.deltamatrices[i],self.amatrices[i].T)[:,1:] / self.examnum) + (self.lamb/self.examnum)*(self.thetamatrices[i][:,1:])
                self.Dmatrices[i] = np.concatenate((dbias,dmain),axis=1)
            else:
                dbias = (np.matmul(self.deltamatrices[i][1:,:],self.amatrices[i].T)[:,0] / self.examnum).reshape(-1,1)
                dmain = (np.matmul(self.deltamatrices[i][1:,:],self.amatrices[i].T)[:,1:] / self.examnum) + (self.lamb/self.examnum)*(self.thetamatrices[i][:,1:])
                self.Dmatrices[i] = np.concatenate((dbias,dmain),axis=1)

        self.rolld()
    
    def predict(self,example):
        self.unrolltheta()

        #normalize example
        mu = np.mean(example)
        s = np.std(example)
        example = (example-mu)/s

        #fp to get result
        ones1 = np.ones((1,example.shape[1]))
        aold = np.concatenate((ones1,example))

        for i in range(1,len(self.neurondim)-1):
            z = np.matmul(self.thetamatrices[i-1],aold)
            ones = np.ones((1,aold.shape[1]))
            anew = np.concatenate((ones,self.sigmoid(z)))
            aold = anew
        
        zlast = np.matmul(self.thetamatrices[-1],aold)
        result = self.sigmoid(zlast)
        return result

    def gradcheck(self):
        thetaval = np.array(self.theta)
        dvec = np.zeros((sum([x[0]*x[1] for x in self.thetadim]),1))
        for i in range(sum([x[0]*x[1] for x in self.thetadim])):
            self.theta[i] += self.gradcheckeps
            self.fp()
            plus = self.cost()

            self.theta[i] -= 2*self.gradcheckeps
            self.fp()
            minus = self.cost()
            self.theta[i] += self.gradcheckeps
            dvec[i,:] = (plus-minus)/(2*self.gradcheckeps)
        return dvec

    def gradientdescent(self):
        self.theta = self.theta - (self.alpha*self.D)

    def train(self):
        idk_amount = 0.0000008
        x = []
        y = []
        for i in range(2):
            self.fp()
            self.bp()
            x.append(i)
            self.gradientdescent()
            y.append(self.cost())
            print(y[-1])
        index = i
        while not((y[-1] < y[-2]) and (y[-1]+idk_amount>y[-2])):
            index += 1
            self.fp()
            self.bp()
            x.append(index)
            self.gradientdescent()
            y.append(self.cost())
            print(y[-1])

        plt.plot(x,y)
        plt.show()
    
    def SaveWeights(self):
        try:
            df = pd.DataFrame(self.theta,columns=["Thetas"])
            df.to_excel("Weights.xlsx",index=False)
        except:
            print("Weights couldn't be saved")

    def LoadWeights(self,name="Weights.xlsx"):
        try:
            df = pd.read_excel(name)
            self.theta = np.array(df['Thetas'])
        except:
            print("Couldn't load Weights")


    
if __name__ == "__main__":
    
    df = pd.read_excel("adatok.xlsx")
    x = np.array([df["x1"],df["x2"],df["x3"]])
    y = np.array([df["y1"],df["y2"],df["y3"],df["y4"],df["y5"],df["y6"],df["y7"],df["y8"],df["y9"],df["y10"],df["y11"],df["y12"],df["y13"],df["y14"],df["y15"],df["y16"],df["y17"],df["y18"],df["y19"],df["y20"],df["y21"],df["y22"],df["y23"],df["y24"]])
    dim = [3,128,128,128,24]
    model = Model(x,y,dim)
    model.train()
    model.SaveWeights()

