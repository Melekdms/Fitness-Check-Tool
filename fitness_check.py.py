#Fitness-Check-Tool

print("Willkommen zum Fitness-Check-Tool!")

# Nutzer-Eingaben
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
gewicht = float(input("Wie schwer bist du (kg)? "))
groesse_cm = float(input("Wie groß bist du (cm)? "))
groesse = groesse_cm / 100  # cm → m
stunden = int(input("Wie viele Trainingsstunden pro Woche? "))
ziel = input("Dein Ziel (Muskelaufbau/Fitness/Ausdauer): ").lower()

# BMI berechnen
bmi = gewicht / (groesse ** 2)

# Funktion für Fitness-Level
def fitness_level(alter, stunden, bmi, ziel):
	if alter < 14:
		return "Noch zu jung für intensives Training"
	elif stunden >= 10 and 18.5 <= bmi <= 25:
		return "Experte"
	elif stunden >= 7:
		return "Profi"
	elif stunden >= 4:
		return "Fortgeschritten"
	else:
		return "Anfänger"

# Empfehlung basierend auf Ziel
def empfehlung(ziel):
	if ziel == "muskelaufbau":
		return ["3x Krafttraining", "2x Cardio"]
	elif ziel == "ausdauer":
		return ["4x Cardio", "1x Krafttraining"]
	else:
		return ["3x Kraft, 2x Ausdauer"]

# Ergebnis ausgeben
level = fitness_level(alter, stunden, bmi, ziel)
plan = empfehlung(ziel)

print("\n--- Ergebnis ---")
print(f"{name} → {level}")
print(f"BMI: {bmi:.1f}")
print("Empfehlung für Trainingsplan:")
for uebung in plan:
	print("-", uebung)
