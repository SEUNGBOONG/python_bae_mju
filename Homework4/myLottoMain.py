import myLotto as mlt

lotto = mlt.buyautolotto()
mlt.printlotto(lotto)
mlt.setwinlotto()
print("당첨번호:", end=" ")
mlt.printnums(mlt.winnum)
print()
mlt.getwinner(lotto)
