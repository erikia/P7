import csv
from datetime import datetime
start_time = datetime.now()


class Greedy:
    """Greedy approach who calculate the ratio value/weight for each item and sort the item on basis of this ratio"""

    def clean_list(shares_list):
        """Clean the list by removing the price = or < 0"""
        cleaned_list = [x for x in shares_list if float(x[1]) > 0]
        return cleaned_list

    def return_shares_list(csv_file):
        """Read the CSV file and turn it into a list"""
        shares_list = []
        with open(csv_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                shares_list.append(row)
            shares_list.remove(shares_list[0])
        return shares_list

    def sorted_list_by_perfermance(shares_list):
        """Sort all the items in decreasing order of the ratio"""
        sorted_list = sorted(
            shares_list, key=lambda x: float(x[2]), reverse=True)
        return sorted_list

    def get_sorted_shares_list(csv_file):
        """Return the shares list cleaned and sorted"""
        dataset = Greedy.return_shares_list(csv_file)
        cleaned_list = Greedy.clean_list(dataset)
        sorted_list = Greedy.sorted_list_by_perfermance(cleaned_list)
        return sorted_list

    def calculate_profitable_investment(shares_list, wallet, share_wallet):
        """Return the list of the best calculated investment"""
        for share in shares_list:
            if wallet > 0 and wallet > float(share[1]):
                share_wallet.append(share)
                wallet -= float(share[1])
        return share_wallet

    def return_price(combinaison):
        """return the calculated price in the combination"""
        total_price = 0
        for share in combinaison:
            price = float(share[1])
            total_price += price
        return total_price

    def return_profit(combinaison):
        """return the calculated profit in the combination"""
        total_benefits = 0
        for share in combinaison:
            price = float(share[1])
            benefits_percent = float(share[2])
            benefit = price * benefits_percent / 100
            total_benefits += benefit
        return total_benefits

    def main(shares_list):
        """Print total cost, total return, shares list"""
        print(f"Number of shares purchased: {len(shares_list)}")
        print("Shares name / Total cost / Total return in %: ")
        print(shares_list)
        print(f"Total cost: {Greedy.return_price(shares_list)}")
        print(f"Total return: {Greedy.return_profit(shares_list)}")


if __name__ == "__main__":
    dataset1 = Greedy.get_sorted_shares_list("csv/dataset1_Python+P7.csv")
    dataset2 = Greedy.get_sorted_shares_list("csv/dataset2_Python+P7.csv")
    share_wallet1 = []
    share_wallet2 = []
    wallet = 500

    shares_list1 = Greedy.calculate_profitable_investment(
        dataset1, wallet, share_wallet1)
    shares_list2 = Greedy.calculate_profitable_investment(
        dataset2, wallet, share_wallet2)
    Greedy.main(shares_list1)
    Greedy.main(shares_list2)

    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
