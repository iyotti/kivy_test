#http://www.k-techlabo.org/www_python/python_main.pdf
#%%
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.core.window import Window

class kivy03(App):
	def build(self):
		return root

class BtnClear(Button):
	def on_release(self):
		drawArea.canvas.clear()

class BtnQuit(Button):
	def on_release(self):
		sys.exit()

class DrawArea(Widget):
	def on_touch_down(self,t):
		self.canvas.add(Color(0.4,0.4,0,4,1)) #描画色
		self.lineObject = Line(points=(t.x,t.y),width=10)
		self.canvas.add(self.lineObject)
	
	def on_touch_move(self,t):
		self.lineObject.points += (t.x,t.y)

	def on_touch_up(self,t):
		pass

Window.size = (600,400)
Window.clearcolor = (1,1,1,1)

#最上位レイアウト作成
root = BoxLayout(orientation='vertical')
btnpanel = BoxLayout(orientation='horizontal')
btnClear = BtnClear(text='Clear') #Clearボタン生成
btnQuit  = BtnQuit(text='Quit')   #Quitボタン生成
btnpanel.add_widget(btnClear)     #Clearボタン取り付け
btnpanel.add_widget(btnQuit)      #Quitボタン取り付け
root.add_widget(btnpanel)		  #ボタンパネルをメインに取り付け

drawArea = DrawArea()
root.add_widget(drawArea)

ap = kivy03()
ap.run()