from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")


# 방법 1. 리스트에 비딩에 참여한 사람과 비딩 금액을 모두 넣은 후 마지막에 최대값을 찾아서 보여줌
def make_bidding_list(bidder, amount):
    bidders = {"bidder_name": bidder, "bid_amount": amount}
    bidding_list.append(bidders)


def find_max_bid(bid_list):
    winner = max(bid_list, key=lambda x: x['bid_amount'])
    print(f"The winner is {winner['bidder_name']} with a bid of ${winner['bid_amount']}")


bidding_list = []
end_of_bid = False
# 비딩을 계속 하시겠습니까? 에 대한 대답이 no가 나올 때까지 비딩을 계속 하면서 비딩 리스트에 계속 추가함
while not end_of_bid:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    make_bidding_list(name, bid)
    keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()
    if keep_bidding == 'no':
        end_of_bid = True

# bidders 중 누가 최고 비딩 금액을 가지고 있는지 알아냄
find_max_bid(bidding_list)

# 방법 2. dictionary 에 최종 낙찰자의 이름과 비딩금액을 넣어두고 매번 들어올떄마다 비딩금액과 비교해서 마지막에 남아있는 사람이 우승자

# def decide_winner(bidder, amount):
#     if "bidder_name" not in winner.keys():
#         winner['bidder_name'] = bidder
#         winner['bid_amount'] = amount
#     else:
#         if winner['bid_amount'] < amount:
#             winner['bidder_name'] = bidder
#             winner['bid_amount'] = amount
#
#
# winner = {}
# end_of_bid = False
# # 비딩을 계속 하시겠습니까에 대한 대답이 no가 나올때까지 비딩을 계속하면서 필요 시 winner dictionary를 업데이트 함
# while not end_of_bid:
#     name = input("What is your name?: ")
#     bid = int(input("What's your bid?: $"))
#     decide_winner(name, bid)
#     keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
#     clear()
#     if keep_bidding == 'no':
#         end_of_bid = True
#
# # 최종 낙찰자를 발표함
# print(f"The winner is {winner['bidder_name']} with a bid of ${winner['bid_amount']}")
