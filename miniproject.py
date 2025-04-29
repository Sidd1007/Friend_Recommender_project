from collections import deque

class FriendRecommender:
    count = 0

    def __init__(self):
        self.graph = {}      # user_id -> set of friend user_ids
        self.user_info = {}  # user_id -> user name
    
    def add_user(self, name):
        FriendRecommender.count += 1
        user_id = FriendRecommender.count
        self.user_info[user_id] = name

        self.graph[user_id] = set()

    def add_connection(self, user1, user2):
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

    def display_user(self):
        print()
        for user_id in self.user_info:
            print("Id:", user_id, " Name:", self.user_info[user_id])

        print()

    def display_graph(self):
        print()
        print("Connections:")
        for user in self.graph:
            print(self.user_info[user]+":", end=" ")
            connetions = self.graph[user]

            for connection in connetions:
                print(self.user_info[connection], end=", ")
            print()

        print()

    def get_suggestions(self, user_id, max_depth=2):
        queue = deque([(user_id, 0)])
        visited = set()
        visited.add(user_id)
        suggestions = []

        while queue:
            current_user, depth = queue.popleft()

            if depth == max_depth:
                continue

            for friend in self.graph[current_user]:
                if friend not in visited:
                    visited.add(friend)
                    if friend != user_id and friend not in self.graph[user_id]:
                        suggestions.append(friend)
                    queue.append((friend, depth + 1))


        return suggestions
    
    def display_suggestion(self, user_id):
        suggestions = self.get_suggestions(user_id)

        print(f"Suggestions for user({user_id})", self.user_info[user_id])
        for suggestion in suggestions:
            print("\tUser:", suggestion, " Name:", self.user_info[suggestion])


        
def meun(fr):
    flag = 1

    while flag:
        print("Enter your choice: ")
        print("1. Add user")
        print("2. Add connection")
        print("3. Get friend suggestion")
        print("4. Exit")
        ch = int(input("-> "))

        if ch == 1:
            name = input("Enter user name: ")
            fr.add_user(name)
            fr.display_user()
        elif ch == 2:
            fr.display_user()

            user1_id = int(input("Enter user-1 ID: "))
            user2_id = int(input("Enter user-2 ID: "))

            fr.add_connection(user1_id, user2_id)
            fr.display_graph()
        elif ch == 3:
            user_id = int(input("Get suggestion for user(ID): "))

            fr.display_suggestion(user_id)
            
        elif ch == 4:
            flag = 0
        else:
            print("Invalid choice!!")

def main():
    fr = FriendRecommender()
    
    meun(fr)


main()


# fr = FriendRecommender()

# fr.add_user("Faraz")    #1
# fr.add_user("Sidd")     #2
# fr.add_user("Zaid")     #3
# # print(fr.count)
# fr.add_user("Parth")    #4
# fr.add_user("Kushal")   #5

# fr.add_connection(1, 2)
# fr.add_connection(1, 5)
# fr.add_connection(2, 3)
# fr.add_connection(4, 5)

# fr.display_graph()

# suggestions = fr.display_suggestion(5)