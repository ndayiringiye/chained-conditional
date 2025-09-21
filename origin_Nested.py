# Example Medical Procedure Authorization System
insurance_coverage = True
doctor_referral = True
waiting_period_days = 30

if insurance_coverage:
    if doctor_referral:
        if waiting_period_days >= 14:
            procedure_authorized = True
            print("Medical procedure authorized! All requirements met.")
        else:
            procedure_authorized = False
            print("Authorization denied: Waiting period not completed.")
    else:
        procedure_authorized = False
        print("Authorization denied: Doctor referral required.")
else:
    procedure_authorized = False
    print("Authorization denied: Insurance coverage required.")