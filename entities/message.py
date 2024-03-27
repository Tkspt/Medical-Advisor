class Message():
    def __init__(self, id, label, chatId, date, isGenerated = False):
        self.id = id
        self.label = label
        self.chatId = chatId
        self.date = date
        self.isGenerated = isGenerated
        