#http://www.k-techlabo.org/www_python/python_main.pdf
#%%
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout


#ラベルの拡張
class MyLabel(Label):
	#タッチ開始（マウスボタンの押下）の場合
	def on_touch_down(self,touch):
		print(self.events())
		print('touch down:', touch.spos)
	#タッチの移動（ドラッグの場合）の処理
	def on_touch_move(self,touch):
		print('touch move:',touch.spos)
	#タッチ終了
	def on_touch_up(self,touch):
		print('touch up:',touch.spos)

class kivy01(App):
	def build(self):
		self.lb1 = MyLabel(text='This is a test of Kivy.')
		return self.lb1

Window.size = (400,100)
ap = kivy01()
ap.run()