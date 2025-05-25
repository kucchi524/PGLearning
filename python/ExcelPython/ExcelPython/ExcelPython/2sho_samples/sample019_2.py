class Players:
    score1 = 0
    score2 = 0

    def judge(self):
        if self.score1 > self.score2:
            print('プレイヤー1の勝ち')
        elif self.score1 < self.score2:
            print('プレイヤー2の勝ち')

p = Players()
p.score1 = int(input('プレイヤー1の得点:'))
p.score2 = int(input('プレイヤー2の得点:'))
p.judge()
