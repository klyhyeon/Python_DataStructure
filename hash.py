
book = dict()
book["1q84"] = 504
book["habit"] = 417

print(book["1q84"])

phone_book = {}
phone_book["me"] = 1049159399
phone_book["mom"] = 1058939399

vote = {}
vote["tom"] = True

def check_vote(name):
    if vote.get(name):
        print("돌려 보내세요!")
    else:
        vote[name] = True
        print("투표하게 하세요.")

check_vote("me")
check_vote("me")
