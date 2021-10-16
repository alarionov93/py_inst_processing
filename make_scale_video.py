import sys
import numpy as np
import cv2 as cv

if __name__=='__main__':
	img = cv.imread(sys.argv[1],1)

	res = []
	miny = int(img.shape[0]/2)
	minx = int(img.shape[1]/2)
	for x, y in zip(np.linspace(int(img.shape[1]/2),img.shape[1],1200), np.linspace(int(img.shape[0]/2),img.shape[0],1200)):
		top = int((y-miny)/2)
		bottom=int(miny+top)
		left = int((x-minx)/2)
		right = int(minx+left)
		res.append(cv.resize(img, (int(x),int(y)), cv.INTER_AREA)[top:bottom,left:right])
		# print((x,y))
	# i = 0
	# print(res[329])
	# for r in res:
	# 	cv.imwrite('/Users/sanya/test%s.jpg' % i ,r)
	# 	i+=1

	fourcc = cv.VideoWriter_fourcc(*'mp4v')
	video=cv.VideoWriter('%s_vid_%s.mp4' % (sys.argv[1],fourcc),fourcc,35,(int(img.shape[1]/2), int(img.shape[0]/2)))
	for j in range(0,499):
		video.write(res[499-j])

	video.release()