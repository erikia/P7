import csv
from datetime import datetime
start_time = datetime.now()

class BruteForce():
    def clean_list(actions_list):
        cleaned_list = [x for x in actions_list if float(x[1]) > 0]
        return cleaned_list

    def turn_csv_into_actions_list(csv_file):
        actions_list = []
        with open(csv_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                actions_list.append(row)
            actions_list.remove(actions_list[0])
        return actions_list

    def get_sorted_actions_list(csv_file):
        dataset = BruteForce.turn_csv_into_actions_list(csv_file)
        cleaned_list = BruteForce.clean_list(dataset)
        return cleaned_list

    def get_best_invest(actions_list, wallet, action_wallet):
        for action in actions_list:
            if wallet > 0 and wallet > float(action[1]):
                action_wallet.append(action)
                wallet -= float(action[1])
        return action_wallet

    def return_price(combinaison):
        total_price = 0
        for action in combinaison:
            price = float(action[1])
            total_price += price
        return total_price

    def return_benefice(combinaison):
        total_benefits = 0
        for action in combinaison:
            price = float(action[1])
            benefits_percent = float(action[2])
            benefit = price * benefits_percent / 100
            total_benefits += benefit
        return total_benefits

    def main(actions_list):
        print(f"Nombres d'actions achetées: {len(actions_list)}")
        print("Liste Nom / Prix / Bénéfice en %: ")
        print(actions_list)
        print(f"Prix: {BruteForce.return_price(actions_list)}")
        print(f"Bénéfice: {BruteForce.return_benefice(actions_list)}")


if __name__ == "__main__":
    dataset1 = BruteForce.get_sorted_actions_list("csv/dataset1_Python+P7.csv")
    dataset2 = BruteForce.get_sorted_actions_list("csv/dataset2_Python+P7.csv")
    action_wallet1 = []
    action_wallet2 = []
    wallet = 500

    actions_list1 = BruteForce.get_best_invest(dataset1, wallet, action_wallet1)
    actions_list2 = BruteForce.get_best_invest(dataset2, wallet, action_wallet2)
    BruteForce.main(actions_list1)
    BruteForce.main(actions_list2)

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

