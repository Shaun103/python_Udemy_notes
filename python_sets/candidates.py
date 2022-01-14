def main():
    print()

    required_skills = ['Python', 'Github', 'Linux']

    candidates = {
        'Anna': {'Java', 'Linux', 'Windows', 'Github', 'Python', 'Full Stack'},
        'Bob': {'Github', 'Linux', 'Python'},
        'Carol': {'Linux', 'Javascript', 'HTML', 'Python', 'Github'},
        'Daniel': {'Pascal', 'Java', 'C++', 'Github'},
        'Ekani': {'HTML', 'CSS', 'Github', 'Python', 'Linux'},
        'Fenna': {'Linux', 'Pascal', 'Java', 'C', 'Lisp', 'Modula-2', 'Perl', 'Github'},
    }


    interviewees = set()

    for candidate, skills in candidates.items():
        # if skills.issuperset(required_skills): # only looking for the skills you are looking for 
        if skills > set(required_skills): # if they have more than skills you are asking for 
            interviewees.add(candidate)

    print(interviewees)

#_________________________________________________







if __name__ == "__main__":
    main()