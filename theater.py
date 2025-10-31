def calculate_ticket_revenue(show_type, tickets_sold, time_slot):
    if show_type == "blockbuster":
        if time_slot == "morning":
            price = 12
        elif time_slot == "afternoon":
            price = 18
        else: 
            price = 25

    elif show_type == "standard":
        if time_slot == "morning":
            price = 8
        elif time_slot == "afternoon":
            price = 12
        else:
            price = 16

    else: 
        if time_slot == "morning":
            price = 5
        elif time_slot == "afternoon":
            price = 8
        else:
            price = 10

    return tickets_sold * price


def calculate_occupancy_rate(theater_years, baseline_seats, filled_seats):
    expected_capacity = 1000 + (theater_years * 100)
    seat_availability = expected_capacity - baseline_seats
    occupancy_percent = (filled_seats - baseline_seats) / seat_availability * 100
    return occupancy_percent


def determine_popularity_status(occupancy_percent):
    if occupancy_percent < 50:
        return "Low Demand"
    elif occupancy_percent < 60:
        return "Moderate Demand"
    elif occupancy_percent < 70:
        return "Good Demand"
    elif occupancy_percent < 85:
        return "High Demand"
    else:
        return "Sold Out Status"


def calculate_total_profit(revenue, tickets, status):
    if status == "Low Demand":
        multiplier = 0.5
    elif status == "Moderate Demand":
        multiplier = 1.0
    elif status == "Good Demand":
        multiplier = 1.2
    elif status == "High Demand":
        multiplier = 1.5
    else:
        multiplier = 1.8

    base_profit = revenue * 0.05 + tickets * 2
    final_profit = base_profit * multiplier
    return round(final_profit, 1)


def needs_promotion(screening_days, total_tickets, avg_occupancy):
    if screening_days >= 6 and avg_occupancy < 50:
        return True
    if total_tickets < 100 and avg_occupancy < 60:
        return True
    if screening_days >= 4 and avg_occupancy < 40:
        return True
    return False


def generate_theater_report(movie_title, show_type, tickets, time_slot, years, baseline, filled, days):
    revenue = calculate_ticket_revenue(show_type, tickets, time_slot)
    occupancy = calculate_occupancy_rate(years, baseline, filled)
    status = determine_popularity_status(occupancy)
    profit = calculate_total_profit(revenue, tickets, status)
    promo = needs_promotion(days, tickets, occupancy)

    print("\n========================================")
    print(f"Theater Report for: {movie_title}")
    print("----------------------------------------")
    print(f"Show Type: {show_type}")
    print(f"Tickets Sold: {tickets}")
    print(f"Time Slot: {time_slot}")
    print(f"Ticket Revenue: ${revenue}")
    print("Occupancy Analysis:")
    print(f"  Experience: {years} years, Baseline: {baseline}, Filled Seats: {filled}")
    print(f"  Occupancy: {round(occupancy,1)}%")
    print(f"  Popularity Status: {status}")
    print(f"Total Profit: ${profit}")
    print(f"Screening Days: {days}")
    print("Promotion Needed:", "Yes" if promo else "No")

generate_theater_report("Space Adventure", "blockbuster", 45, "evening", 3, 800, 1150, 3)
generate_theater_report("Comedy Night", "standard", 60, "afternoon", 5, 900, 1300, 5)
generate_theater_report("Old Classic", "classic", 30, "morning", 8, 850, 950, 7)