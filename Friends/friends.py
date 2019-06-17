from mrjob.job import MRJob

class MRFriendsByAge(MRJob):
    # Pass instace, ? and lines
    def mapper(self, _, line):
        # Separate raw data with split func
        (ID, name, age, friends) = line.split(',')
        # Return data with yield to leave the current state and be able to loop the mapper
            # Age - Key , NumberFriends - Value
        yield age, float(friends)

    # Reduce parsing ages and number of friends
    # Match & Group by Key (Age)
    def reducer(self, age, friends):
        total = 0
        numElement = 0
        for x in friends:
            total += x
            numElement += 1
        
        yield age, total / numElement

if __name__ == '__main__':
    MRFriendsByAge.run()
