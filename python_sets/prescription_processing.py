from prescription_data import patients


def main():
    print()

    trial_patients = {'Denise', 'Eddie', 'Frank', 'Georgia', 'Kenny'}

    while trial_patients:
        patient = trial_patients.pop()
        print(patient, end=" : ")
        prescription = patients[patient]
        print(prescription)


if __name__ == "__main__":
    main()