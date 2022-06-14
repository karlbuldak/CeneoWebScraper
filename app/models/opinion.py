from ..utils import get_item
from app.parameters import selectors
class Opinion:
    def __init__(self,opinion_id=None, author=None, recomendation=None, score=None, pros=None, cons=None, usefull=None, useless=None, publish_date=None, purchase_date=None):
        self.opinion_id = opinion_id
        self.author = author
        self.recomendation = recomendation
        self.score = score
        self.pros = pros
        self.cons = cons
        self.usefull = usefull
        self.useless = useless
        self.publish_date = publish_date
        self.publish_date = purchase_date

    def __str__(self):
        return(f'{self.product_id}, {self.product_name}, {self.opinions}, {self.opinions_count}, {self.pros_count}, {self.cons_count}, {self.average_score}')


    def __repr__(self):
        return(f'{self.product_id}, {self.product_name}, {self.opinions}, {self.opinions_count}, {self.pros_count}, {self.cons_count}, {self.average_score}')

    def to_dict(self):
        return {
            "author": self.author,
            "recomendation": self.recomendation,
            "score": self.score,
            "pros": self.pros,
            "cons": self.cons,
            "usefull": self.usefull,
            "publish_date": self.publish_date,
            "purchase_date": self.purchase_date
        }
    def extract_opinion(self, opinion):
        for key, value in selectors.items():
            setattr(self,key, get_item(opinion, *value))
        self.opinion_id = opinion["data-entry-id"]
        return self