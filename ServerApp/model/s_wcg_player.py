from ServerApp import db

class s_wcg_player(db.Model):
    __tablename__ = 's_wcg_player'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    wxid = db.Column(db.String(255))
    name = db.Column(db.String(255))
    head = db.Column(db.String(255))
    bestScore = db.Column(db.Integer)
    bestCombo = db.Column(db.Integer)
    coin = db.Column(db.Integer)
    ball_1 = db.Column(db.Integer)
    ball_2 = db.Column(db.Integer)
    ball_3 = db.Column(db.Integer)
    ball_4 = db.Column(db.Integer)
    ball_5 = db.Column(db.Integer)
    ball_6 = db.Column(db.Integer)
    ball_7 = db.Column(db.Integer)
    ball_8 = db.Column(db.Integer)



    def __init__(self,wxid,name,head,bestScore,bestCombo,coin,ball_1,ball_2,ball_3,ball_4,ball_5,ball_6,ball_7,ball_8):
        self.wxid = wxid
        self.name = name
        self.head = head
        self.bestScore = bestScore
        self.bestCombo = bestCombo
        self.coin = coin
        self.ball_1 = ball_1
        self.ball_2 = ball_2
        self.ball_3 = ball_3
        self.ball_4 = ball_4
        self.ball_5 = ball_5
        self.ball_6 = ball_6
        self.ball_7 = ball_7
        self.ball_8 = ball_8

    def __repr__(self):
        return '<s_wcg_player %r>' % self.id