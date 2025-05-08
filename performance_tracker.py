#1. E-Commerce Cart System** 
def calculate_total_price(cart_items):
    if not cart_items:
        print("Cart is empty.")
        return
    total_price = sum(cart_items.values())
    if len(cart_items) > 5:
        total_price *= 0.9  
    print(f"Total Price: {int(total_price)}")
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
calculate_total_price(cart_items)

#2. Restaurant Menu Management
def add_menu_item(menu, item):
    if item not in menu:
        menu.append(item)

def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"Cannot remove: '{item}' not found in the menu.")

def check_menu_item(menu, item):
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
add_menu_item(initial_menu, add_item)
remove_menu_item(initial_menu, remove_item)
check_menu_item(initial_menu, check_item)
print("Updated menu:", initial_menu)

#3. Classroom Performance Tracker
def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)

def track_performance(students):
    averages = {name: calculate_average(scores) for name, scores in students.items()}
    top_performer = max(averages, key=averages.get)
    
    print("Average Marks:", averages)
    print("Top Performer:", top_performer)
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
track_performance(students)

#4. Movie Ticket Booking System
def book_seat(seat_number, booked_seats, total_seats):
    if seat_number < 1 or seat_number > total_seats:
        print(f"Seat {seat_number} is invalid.")
    elif seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    else:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} booked successfully.")

def cancel_seat(seat_number, booked_seats):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} cancelled successfully.")
    else:
        print(f"Seat {seat_number} is not currently booked.")

def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
total_seats = 10
booked_seats = [2, 5, 7]
book_seat_number = 3
cancel_seat_number = 5
book_seat(book_seat_number, booked_seats, total_seats)
cancel_seat(cancel_seat_number, booked_seats)
available = get_available_seats(total_seats, booked_seats)
print("Available seats:", available)

#5. Hospital Patient Management
def search_patients_by_disease(patients, disease):
    matching_patients = [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]
    return matching_patients
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"
result = search_patients_by_disease(patients, search_disease)
print(f"Patients with {search_disease}: {result}")

#6. Customer Feedback Analysis
def calculate_positive_feedback(ratings):
    if not ratings:
        print("No ratings available.")
        return
    positive_count = sum(1 for rating in ratings if rating >= 4)
    percentage = (positive_count / len(ratings)) * 100
    print(f"Positive Feedback: {round(percentage, 2)}%")
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
calculate_positive_feedback(ratings)

#7. Taxi Fare Calculation
ef calculate_fare(distance):
    base_fare = 50
    per_km_rate = 10
    return base_fare + (distance * per_km_rate)
trips = [5, 10, 3]  
total_fare = 0
for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare
print(f"Total Fare: ${total_fare}")




