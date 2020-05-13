from util import Queue

from random import randint


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        for user in range(num_users):
            for num_friends in range(randint(0, (avg_friendships * 2) - 1)):
                random_friend = randint(1, num_users)
                if random_friend != user + 1 and random_friend not in self.friendships[user + 1]:
                    self.add_friendship(user + 1, random_friend)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        visited = {}

        for user in self.users:

            q = Queue()

            q.enqueue([user_id])

            temp_visited = set()

            while q.size() > 0:
                path = q.dequeue()
                vertex = path[-1]

                if vertex not in temp_visited:
                    temp_visited.add(vertex)

                    if vertex == user:
                        break

                    for neighbor in self.friendships[vertex]:
                        path_copy = path.copy()
                        path_copy.append(neighbor)
                        q.enqueue(path_copy)

            visited[user] = path

        for user, path in visited.copy().items():
            if user not in path:
                visited.pop(user)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    sg2 = SocialGraph()
    sg2.populate_graph(1000, 5)
    print(sg2.friendships)
    connections2 = sg2.get_all_social_paths(1)
    print(connections2)
    print(len(connections2.keys()))
    print("Possible Stretch accidental completion???")
