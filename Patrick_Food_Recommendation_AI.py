rules = {
    "Diabetes": ["Tired", "Blurry Vision", "Tingling", "Thristy", "Weightloss", "Slow Recovery"],
    "Hypertension": ["Blurry Vision", "Nosebleed", "Ear Buzzing", "Shortness of Breath", "Headaches"],
    "Maag": ["Stomach Ache", "Nauseous", "Heartburn", "Lost Appetite", "Shortness of Breath", "Bloating"],
    "Flu": ["Fever", "Stuffy Nose", "Headaches", "Muscle Pain", "Runny Nose", "Sneeze"],
    "Diare": ["Stomach Ache", "Feses Cair", "Nauseous", "Tired", "Lost Appetite", "Thristy"],
    "Radang Tenggorokan": ["Sore Throat", "Cough", "Fever", "Hoarseness", "Tired"]
}

def diagnose(symptoms):
    possible_disease = []
    maximum = 0
    for disease,symptoms_knowledge in rules.items():
        similarity = set(symptoms).intersection(symptoms_knowledge)
        leng = len(similarity)
        if(leng>=maximum and leng!=0):
            maximum = len(similarity)
            possible_disease.append(disease)
    return possible_disease

print("Please input a minimum of 3 symptoms (Ex. Tired, Blurry Vision, Tingling):", end = " ")
tempSymptoms = input()
symptoms = tempSymptoms.split(", ")

print("Preferences (Ex. Breakfast, Snack):", end = " ")
tempPreferences = input()
preferences = tempPreferences.split(", ")

possible_disease = diagnose(symptoms)
print(possible_disease)

if not possible_disease:
    print("Can't Recognize Your Disease")

penyakit={
    "Diabetes": ["low-sugar", "low-fat"],
    "Hypertension": ["high-potassium", "low-fat", "low-sodium"],
    "Maag": ["high-fiber", "low-fat", "low-acid"],
    "Flu": ["high-vitamin C", "high-vitamin D", "high protein"],
    "Diare": ["probiotics", "bland foods"],
    "Radang Tenggorokan": ["soft-texture", "warm-foods"]
}

foods = {
    "Oatmeal": ["low-sugar", "low-fat", "low-calorie"],
    "Corn Salad": ["low-sugar", "low-fat", "low-calorie"],
    "Long Beans Stir Fried": ["low-fat", "low-calorie"],
    "Salmon Steak": ["low-fat", "low-calorie"],
    "Stir Fry Broccoli": ["low-fat", "low-calorie"],
    "Cooked Spinach": ["high-potassium", "low-sodium", "low-fat", "soft-texture"],
    "Avocado": ["high-potassium", "low-sugar"],
    "Crispy Potato Skins": ["high-fiber", "high-potassium"],
    "Asparagus": ["high-fiber", "low-acid"],
    "Oranges": ["high-vitamin C", "high-vitamin D"],
    "Sardines": ["high-vitamin D", "high-protein"],
    "Miso Soup": ["probiotics", "warm-foods", "soft-texture"],
    "Bread": ["bland foods", "high-protein"],
    "Porridge": ["bland foods", "warm-foods"]
}

foodsCategory = {
    "Oatmeal": ["Breakfast", "Snack"],
    "Corn Salad": ["Western", "Breakfast", "Vegetable"],
    "Long Beans Stir Fried": ["Vegetable", "Chinese"],
    "Salmon Steak": ["Western"],
    "Stir Fry Broccoli": ["Vegetable", "Chinese"],
    "Cooked Spinach": ["Vegetable"],
    "Avocado": ["Fruit"],
    "Crispy Potato Skins": ["Western", "Snack"],
    "Asparagus": ["Chinese", "Vegetable"],
    "Oranges": ["Fruit"],
    "Sardines": ["Seafood"],
    "Miso Soup": ["Soup", "Japanese"],
    "Bread": ["Western"],
    "Porridge": ["Breakfast"]
}

def plan(disease):
    suitFoods = []
    maximum = 0
    for i in disease:
        for food,nutritions in foods.items():
            similarity = set(penyakit[i]).intersection(nutritions)
            leng = len(similarity)
            if(leng>=maximum and leng!=0):
                maximum = len(similarity)
                suitFoods.append(food)
        return suitFoods

suitable_foods = plan(possible_disease)

def choose(preferences):
    chooseFoods = []    
    maximum = 0
    for food,category in foodsCategory.items():
        similarity = set(preferences).intersection(category)
        leng = len(similarity)
        if(leng>=maximum and leng!=0):
            maximum = len(similarity)
            chooseFoods.append(food)
    return chooseFoods

choose_foods = choose(preferences)
suggestion_foods = []

for i in suitable_foods:
    for j in choose_foods:
        if (i != j):
            suggestion_foods.append(i)

print(f'Based on your preferences: {choose_foods}')
print(f'Suggestions: {suggestion_foods}')