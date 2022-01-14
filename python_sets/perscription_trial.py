from prescription_data import *

def main():
    print()

    trial_patients = ['Denise', 'Eddie', 'Frank', 'Georgia', 'Kenny']

    # remove Warfarin and add Edoxaban
    for patient in trial_patients:
        prescription = patients[patient]
        if warfarin in prescription:
        # print(patient, prescription)
            prescription.remove(warfarin)
            prescription.add(edoxaban)
        else:
            print(f"Patient: {patient} is not taking Wafarin."
                f"Please remove {patient} from trial")
        print(patient, prescription)

if __name__ == "__main__":
    main()