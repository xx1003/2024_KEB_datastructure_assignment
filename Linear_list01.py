def insert_friend(new_friend):
    global kakao_friends, size
    idx = 0
    for i in kakao_friends:
        if new_friend[1] >= i[1]:
            kakao_friends.append(None)
            last = size - 1
            while last >= idx:
                kakao_friends[last + 1] = kakao_friends[last]
                last -= 1
            kakao_friends[idx] = new_friend
            size += 1
            return
        idx += 1
    kakao_friends.append(new_friend)
    size += 1
    return


kakao_friends = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
size = 5

if __name__ == "__main__":
    while True:
        name = input("추가할 친구--> ")
        kakao_count = int(input("카톡 횟수--> "))
        insert_friend((name, kakao_count))
        print(kakao_friends)

