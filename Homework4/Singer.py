singer = ['bts', '볼빨간사춘기', 'bts', '블랙핑크', '뉴진스']
song = ['작은것들을 위한 시', '나만 봄', '소우주', 'Kill This Love', '슈퍼 샤이']

kpop = zip(singer, song)
kpChart = enumerate(kpop, start=1)

for index, (singer, song) in kpChart:
    print(f"{index}: singer={singer}, song={song}")
