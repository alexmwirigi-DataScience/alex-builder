#Mini ml_pipeline - Alex Mirigi
#Nairobi, Kenya

def load_data():
    data = [10,20,30,40,50]
    print("Data loaded successfully")
    return data

def calculate_average(data):
    average = sum(data) / len(data)
    return average

def run_pipeline():
    data = load_data()
    average = calculate_average(data)
    print(f"Model result:The average is {average}")

run_pipeline()