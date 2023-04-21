#Iterator using Class
#creating your custom iterator


class TVChannels():
    def __init__(self):
        self.channels = ["ZeeTV", "StarTV", "Sony" ,"TenSports", "AajTak"]
        self.index = -1     #initialise to -1, no channel is watched

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        if(self.index == len(self.channels)):
            raise StopIteration         #raise StopIteration notification

        return self.channels[self.index]

channel = TVChannels()

itr = iter(channel)
print(next(itr))
print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
#print(next(itr))   # raises StopIteration