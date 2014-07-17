from views import db

class Link(db.Model):
    __tablename__ = 'link'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    link = db.Column(db.String)

    def __init__(self, name=None, link=None):
        self.name = name
        self.link = link

    def __repr__(self):
        return u"Link(id='%s', name='%s', link='%s')" % (self.id, self.name, self.link)

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__repr__()