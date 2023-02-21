
philosophers = {
    "Hegel": "Hegel's philosophy centers around the concept of dialectical idealism, which is the idea that history progresses through a series of conflicts and their resolutions. Hegel believed that history had a direction and a purpose, and that the ultimate goal was the realization of human freedom and rationality.",
    "Kant": "Kant's philosophy is best known for his ethical theory based on the categorical imperative, which states that actions should be based on principles that could be made universal without contradiction. Kant also developed a theory of knowledge that emphasized the role of the mind in shaping experience, and he believed that reason could provide insights into the nature of reality that were not accessible through empirical observation.",
    "Kierkegaard": "Kierkegaard's philosophy is often associated with existentialism, which emphasizes the individual's search for meaning in an indifferent universe. Kierkegaard believed that the highest form of existence was the 'leap of faith,' which involved a commitment to an irrational belief in God. Kierkegaard also criticized the idea of objective truth, arguing that human knowledge was always subjective and that the only meaningful truth was that which was personally experienced.",
    "Nietzsche": "Nietzsche's philosophy is characterized by his rejection of traditional morality and the idea of objective truth. Instead, Nietzsche argued that human beings should embrace their individual will to power and create their own values. Nietzsche believed that this would lead to the emergence of a new kind of human being, the Übermensch or 'Superman,' who would be free from the constraints of traditional morality.",
    "Foucault": "Foucault's philosophy is focused on power and knowledge, and how they shape human experience. Foucault argued that power was not just held by governments or institutions, but was present in all social relations. He also developed the concept of the 'disciplinary society,' in which institutions like prisons, schools, and hospitals serve to regulate and control individuals in modern society."
}


valid_responses = ["yes", "y", "no", "n"]


while True:
    
    philosopher = input("Enter the name of a philosopher: ")
    
   
    if philosopher in philosophers:
        print(philosophers[philosopher])
    else:
        print("Philosopher not found.")
        continue
    
    
    while True:
        response = input("Do you want to learn about another philosopher? (y/n) ")
        if response.lower() in valid_responses:
            break
        else:
            print("Invalid response.")
    
   
    if response.lower() == "no" or response.lower() == "n":
        break