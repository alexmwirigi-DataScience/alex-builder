class MLModel:
    def __init__(self, name , version, status = "active"):
        self.name = name
        self.version = version
        self.status = status

    def describe(self):
        print(f"Model: {self.name}, Version: {self.version}")
    
    def show_status(self):
        print(f"Model: {self.name} | Version: {self.version} | Status: {self.status} ")

model1 = MLModel("FraudDetector", "1.0")
model2 = MLModel("ChurnPredictor", "2.1", "retired")
model3 = MLModel("CancerDetector", "0.1", "testing")

model1.describe()
model2.describe()

model1.show_status()
model2.show_status()
model3.show_status()