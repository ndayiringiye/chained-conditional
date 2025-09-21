# Example Gym Membership Discount System 
age = 22
student_status = True
monthly_visits = 15

if age <= 25 and student_status and monthly_visits >= 12:
    discount_approved = True
    print("Student discount approved! 30% off membership.")
else:
    discount_approved = False
    # Provide specific feedback about why discount was denied
    if age > 25:
        print("Discount denied: Age limit exceeded for student discount.")
    elif not student_status:
        print("Discount denied: Student status required.")
    else:
        print("Discount denied: Need to visit more frequently.")