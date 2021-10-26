import sys
import os
import traceback as tb
import numpy as np
import cv2 as cv


if __name__=='__main__':
	img = cv.imread(sys.argv[1],1)

	FRAME_CNT = 1200
	FPS = 50
	i = 0
	path = 'img/test%s.jpg'
	miny = int(img.shape[0]/2)
	minx = int(img.shape[1]/2)
	for x, y in zip(np.linspace(int(img.shape[1]/2),img.shape[1],FRAME_CNT), np.linspace(int(img.shape[0]/2),img.shape[0],FRAME_CNT)):
		top = int((y-miny)/2)
		bottom=int(miny+top)
		left = int((x-minx)/2)
		right = int(minx+left)
		cv.imwrite(path % i , cv.resize(img, (int(x),int(y)), cv.INTER_AREA)[top:bottom,left:right])
		i+=1
	try:
		fourcc = cv.VideoWriter_fourcc(*'mp4v')
		video=cv.VideoWriter('%s_vid.mp4' % (sys.argv[1]),fourcc,fps,(int(img.shape[1]/2), int(img.shape[0]/2)))
		for j in range(0,FRAME_CNT-1):
			video.write(cv.imread(path % int(FRAME_CNT-1-j), 1))

		video.release()
	except FileNotFoundError:
		print('Problem with saved resized images, check path exists and they are saving correctly.')
	except OSError:
		print('Problem with opening some files (video or photos).')
	except Exception as e:
		tb.format_exception(None, e, e.__traceback__)
	finally:
		try:
			[os.remove('/Users/sanya/Work/py_inst_processing/img/test%s' % f_num) for f_num in range(0,FRAME_CNT-1)]
		except OSError:
			print('Can not remove temp jpg files.')
		except Exception as e:
			tb.format_exception(None, e, e.__traceback__)


