import jieba
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox
import wordcloud
import numpy as np
from PIL import Image
from collections import Counter
import tkinter.filedialog


def toImage():
    if entry1.get()=='':
        tk.messagebox.showerror('错误','您未选择图片')
        return
    if entry2.get()=='':
        tk.messagebox.showerror('错误','您未选择文本文件')
        return
    myWordCloud = toWordCloud(entry2.get(), entry1.get())
    plt.imshow(myWordCloud)
    myWordCloud.to_file('my.png')
    tk.messagebox.showinfo('请查看','请查看图片效果')
    plt.show()
    tk.messagebox.showinfo('完成','您的图片保存成功')




def selectImage():
    path = tk.filedialog.askopenfilename(filetype=[('png文件', '.png'), ['jpg文件', '.jpg']])
    entry1.delete(0, tk.END)
    entry1.insert(0, path)


def selectTxt():
    path = tk.filedialog.askopenfilename(filetype=[('文本文件', '.txt')])
    entry2.delete(0, tk.END)
    entry2.insert(0, path)


def toWordCloud(txtPath, imgPath):
    mywordCloud =  wordcloud.WordCloud(background_color='white', font_path='simsun.ttc', mask=np.array(Image.open(imgPath)))
    myfenci = jieba.lcut(open(txtPath, encoding='utf-8').read())
    counter =  Counter(myfenci)
    mywordCloud.generate_from_frequencies(counter
        )
    return mywordCloud


root = tk.Tk()
root.geometry('300x300')
mybutton1 = tk.Button(root, text='浏览', bg='white', command=selectImage)
mybutton2 = tk.Button(root, text='浏览', bg='white', command=selectTxt)
label1 = tk.Label(root,text='请选择图片')
entry1 = tk.Entry(root, bg='white')
label2 = tk.Label(root,text='请选择文本文件')
entry2 = tk.Entry(root, bg='white')
mybutton3 = tk.Button(root, text='确定', bg='white', command=toImage)
label1.grid(row=0,column=1,padx=50)
entry1.grid(row=1, column=1, padx=50)
mybutton1.grid(row=1, column=2)
label2.grid(row=2,column=1,padx=50)
entry2.grid(row=3, column=1, padx=50)
mybutton2.grid(row=3, column=2)
mybutton3.grid(row=4, column=1, padx=100)
root.mainloop()
