import cv2
import numpy as np
from db import *
#from PanZoomWindow import PanZoomWindow

def setText(img, text, location):
  font                   = cv2.FONT_HERSHEY_SIMPLEX
  bottomLeftCornerOfText = location
  fontScale              = 0.5
  fontColor              = (255,255,255)
  lineType               = 1

  cv2.putText(img,text, 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)

def drawPrimaryCord(cord_length, beginning, termination, twist):

  x_margin = 20
  y_margin = 20
  cord_length *= 10

  x1 = x_margin
  y1 = y_margin
  x2 = x1 + cord_length
  y2 = y1
  
  #beginning = "K"
  #termination = "K"
  #twist = "S"

  khipu = np.zeros((cord_length + x_margin*2, cord_length + x_margin*2, 3), np.uint8)

  cv2.line(khipu, (x1, y1), (x2, y2), (0, 255, 0), thickness=1)
  
  setText(khipu, beginning, (x1, y1))
  setText(khipu, termination, (x2, y2))
  setText(khipu, twist, (int(x1+cord_length/2),y1))
  
  #drawCords(khipu):
  #total_cord_cluster = getTotalClusteCord()
  clusters = getClusterCords("1000000")
  #total_cord_cluster = len(cluster)

  #for i in range(total_cord_cluster):
  for cluster in clusters:
    #start_position = 
    num_cords = cluster['NUM_CORDS']
    x1 += 20
    for j in range(num_cords):
      cord_length = 100
      x1 += 2
      x2 = x1
      y2 = y1 + cord_length

      cv2.line(khipu, (x1, y1), (x2, y2), (0, 255, 0), thickness=1)


  cv2.imshow('Khipu',khipu)
  cv2.waitKey(0)

def drawCords(img):
  cv2.line(khipu, (x1, y1), (x2, y2), (0, 255, 0), thickness=1)

def drawKhipu(id):

  #id = "1000189"

  data = getPrimaryCordData(id)

  print(data)

  pcord_id = int(data['PCORD_ID'])
  cord_length = int(data['PCORD_LENGTH'])
  beginning = data['BEGINNING']
  termination = data['TERMINATION']
  twist = data['TWIST']

  #drawPrimaryCord(cord_length, beginning, termination, twist)

  #drawCords()
  x_margin = 20
  y_margin = 20
  cord_length *= 10

  x1 = x_margin
  y1 = y_margin
  x2 = x1 + cord_length
  y2 = y1
  
  #beginning = "K"
  #termination = "K"
  #twist = "S"

  khipu = np.zeros((600, cord_length + x_margin*2, 3), np.uint8)

  cv2.line(khipu, (x1, y1), (x2, y2), (0, 255, 0), thickness=1)
  
  setText(khipu, beginning, (x1, y1))
  setText(khipu, termination, (x2, y2))
  setText(khipu, twist, (int(x1+cord_length/2),y1))
  
  #drawCords(khipu):
  #total_cord_cluster = getTotalClusteCord()
  clusters = getClusterCords(pcord_id)
  #total_cord_cluster = len(cluster)

  print("total cluster: ", len(clusters))

  #for i in range(total_cord_cluster):
  for cluster in clusters:
    #start_position = 
    num_cords = cluster['NUM_CORDS']

    start_position = cluster['START_POSITION']
    end_position = cluster['END_POSITION']

    x1 += start_position*10

    cords_space = ((end_position-start_position)/num_cords)*10

    cords = getCords(int(cluster['CLUSTER_ID']))

    for cord in cords:
      cord_length = cord['CORD_LENGTH']*10
      x1 += cords_space
      x2 = x1
      y2 = y1 + cord_length

      cv2.line(khipu, (x1, y1), (x2, y2), (0, 255, 0), thickness=1)

  cv2.imshow('Khipu',khipu)
  cv2.waitKey(0)  
  '''
  window = PanZoomWindow(khipu, "test window")
  key = -1
  while key != ord('q') and key != 27: # 27 = escape key
      #the OpenCV window won't display until you call cv2.waitKey()
      key = cv2.waitKey(5) #User can press 'q' or ESC to exit.
  cv2.destroyAllWindows()
  '''
if __name__ == "__main__":
    id = "1000192"
    drawKhipu(id)