class Message:
    """Message Department, displays all the necessary information within a message.
    : ivar int id: Message ID.
    : ivar string body: Message body.
    : ivar string sender: Name of sender of the message.
    : ivar string status: Message Read Status - Optional.

    : param int message_id: Identifies the message being produced.
    : param string message_body: The body of the message produced.
   : param string message_sender: Name of the current sender of the message.
   : param string message_status: Status of reading the current message.
    """

    def __init__(self, message_id, message_body, message_sender, message_status="not read"):
        self.id = message_id
        self.body = message_body
        self.sender = message_sender
        self.status = message_status

    def __str__(self):
        """Prints the message.
        """
        print("Message from ",  self.sender, ":")
        print(self.body)

    def len(self):
        """Returns the body length of the message.
        : return: Length of message..
        : rtype: int
        """


    class PostOffice:
        """A Post Office class. Allows users to message each other.

        :ivar int message_id: Incremental id of the last message sent.
        :ivar dict boxes: Users' inboxes.

        :param list usernames: Users for which we should create PO Boxes.
        """

        def __init__(self, usernames):
            self.message_id = 0
            self.boxes = {user: [] for user in usernames}

        def send_message(self, sender, recipient, message_body, urgent=False):
            """Send a message to a recipient.

            :param str sender: The message sender's username.
            :param str recipient: The message recipient's username.
            :param str message_body: The body of the message.
            :param urgent: The urgency of the message.
            :type urgent: bool, optional
            :param status: Message Read Status.
            :return: The message ID, auto incremented number.
            :rtype: int
            :raises KeyError: if the recipient does not exist.
            """
            user_box = self.boxes[recipient]
            self.message_id = self.message_id + 1
            new_message= Message(self.message_id, message_body, sender)

            if urgent:
                user_box.insert(0, new_message)
            else:
                user_box.append(new_message)
            return self.message_id

        def read_inbox(self, username, N = 100000):  # 100000 If the user did not send a number
            """Send readable messages to the user.
            username sender: The username of the message requester.
            : param int N: The number of messages he wants to read, optional.
            : return: List of readable messages.
            : rtype: list
            """
            user_box = self.boxes[username]
            return_message = []
            count_message = 0
            if not N == 0:
                if N < len(self.boxes[username]):
                    for message in range(len(self.boxes[username])):
                        if self.boxes[username][message].status == 'not read':
                            self.boxes[username][message].status == 'read'
                            count_message = count_message + 1
                            return_message.append(self.boxes[username][message])
                        if count_message == N:
                            break

            for message in range(len(self.boxes[username])):
                if self.boxes[username][message].status == 'not read':
                    self.boxes[username][message].status == 'read'
                    return_message.append(self.boxes[username][message])
            return return_message

        def search_inbox(self, username, sentence):
            """Send readable messages to the user.
                        usernamesender: The username of the message requester.
                        : param string sentence: Sentence search sentence
                        : return: The list of messages that contain the search phrase.
                        : rtype: list
                         """
            return_message = []
            for message in self.boxes[username]:
                if sentence in message.body or sentence in message.sender:
                    return_message.append(message)

            return return_message

