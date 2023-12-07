import json
import parameters

MAX_POINT = 3
MIN_POINT = 1

etalon = {
    "respiration" : 16,
    "heart rate" : 60,
    "blushing level" : 2,
    "pupillary dilation" : 4
}

#***************************************************************************
#***************************************************************************


def get_choice():
    """
    Gets choice from user. This function bounds choice to 1-2.

    :return: choice
    :rtype: int

    """
    choice = ""
    while choice != "1" and choice != "2":
        choice = input(">>>")
    return choice


def print_question(question):
    """
    Prints question in user-friendly format.

    :param question: dictionary with question and answers
    :type param: dict

    """
    print(question["question"])
    counter: int = 1
    for answer in question["answers"]:
        print(f"\t{counter}: {answer['answer']}")
        counter += 1


def decide(decision):
    """
    Prints decision based on float value compared with etalon value.

    :param decision: accumulated value, formed by sum of all answers
    :type param: float

    """    
    try:
        if decision > MAX_POINT / 2:
            print("human")
        else:
            print("replicant")
    except TypeError as e:
        pass

def main():
    params_asker = parameters.Params()
    params_asker.set_etalon_params(etalon)

    with open("questions.json", "r") as f:
        questions = json.load(f)
    total_score = 0
    for question in questions:
        print_question(question)
        choice = get_choice()
        answ_points = question["answers"][int(choice) - 1]["value"]
        coeff = params_asker.evaluate_params()
        if coeff < 0:
            return
        else:
            answ_points *= coeff
            total_score += answ_points

    decision = total_score / len(questions) 
    decide(decision)

if __name__ == "__main__":
    main()