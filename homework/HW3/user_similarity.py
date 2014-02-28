from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

import re
WORD_RE = re.compile(r"[\w']+")

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol
    def mapper_get_business_ids(self,_, record):
        #yield each user with <user_id, business id>
        if record['type'] == 'review':
            user_id = record['user_id']
            for business in WORD_RE.findall(record['business_id']):
                yield [user_id, business]

    def reducer_user_business(self, user_id, business_ids):
        yield ['NONE', [user_id,list(business_ids)]]

    def pair_users(self, _, user_business):
        for i in user_business:
            for j in user_business:
                if user_business.index(i) > user_business.index(j):
                    yield [[i[0],j[0]], [i[1],j[1]]]
            
    #         for j in user_business:
    #            if i> j:
    #               yield None, [[i[0],j[0]], [i[-1],j[-1]]]
       
    # def get_similarity(self, _, user_business_ids):
    #     union = ()
    #     inter = ()
    #     for i in user_business_ids
    #         union = set(i[1])
    #         inter = list(i[1][0] & i[1][1]]) 
    #         if (1.0*len(inter))/(1.0*len(union)) > 0.5:
    #             yield i[0], Jac
    #         union 
    ###
    # TODO: write the functions needed to
    # 1) find potential matches,
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##

    #def mapper

    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [
            self.mr(mapper=self.mapper_get_business_ids, reducer=self.reducer_user_business),
            self.mr(mapper=self.pair_users),
        ]

if __name__ == '__main__':
    UserSimilarity.run()



"""

Asymmetric binary similarity
More commonly used for calculating set similarity
|intersection| / |union|
"Jimmy likes pizza" | "Shreyas likes pizza"

d = 1 - J, where J = AXB/A+B


User similarity:
1 user i had Ni businesses reviewed.
[user_id, business_id]

Coeff de Jacquard: distance petite = J superieur a 0.5.
Jacquard: 

A = BizA, BizB, BizC, BizD
B = BizB, BizC, BizD

J(A,B) = (BizB, BizC, BizD) / (Biz A, BizB, BizC, BizD) = 0.75 > 0.5 OK.

1/ Users <-> {Biz Ai}
UsersId User ID {Biz List} {Biz List}




Mapper: 
Reducer: 
Output:
Reducer => <[user_id, user_id2], Jaccard coefficient>

"""
