from O15_prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]
# trial_patients = ["Denise", "Eddie", "Frank", "Georgia"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    else:
        print(f"{patient} is not taking Warfarin."
              f"Please remove {patient} from trial list.")

    # Below is alternate code which makes use of exception thrown by .remove()
    # try:
    #     prescription.remove(warfarin)
    #     prescription.add(edoxaban)
    # except KeyError:
    #     print(f"{patient} is not taking Warfarin."
    #           f"Please remove {patient} from trial list.")

    print(patient, prescription)
