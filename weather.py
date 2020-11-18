import tkinter as tk
import requests

root=tk.Tk()

def get_weather(city):
    weather_key="961b3df32dc4903aeaecb7cff3b82303"
    url="https://api.openweathermap.org/data/2.5/weather"
    par={'APPID':weather_key,'q':city,'units':'Imperial'}
    response=requests.get(url,params=par)
    weather=response.json()
    lable['text']=details(weather)

def details(weather):
    name=weather['name']
    country=weather['sys']['country']
    min_temp=5/9*(weather['main']['temp_min']-32)
    max_temp=5/9*(weather['main']['temp_max']-32)
    main_str='City= %s\n Country= %s\n Minimum Temprature= %s\n Maximum Temprature= %s' %(name,country,"{:.2f}".format(min_temp),"{:.2f}".format(max_temp))
    return main_str

canvas=tk.Canvas(root,height=500,width=500,bg="green")
canvas.pack()

frame1=tk.Frame(root,bg="red")
frame1.place(relheight=0.2,relwidth=0.8,relx=0.1,rely=0.1)

entry=tk.Entry(frame1,font=50,bd=20,fg="black")
entry.place(relheight=0.8,relwidth=0.6,relx=0.05,rely=0.1)

button=tk.Button(frame1,text="Get Weather",bd=17,bg="blue",fg="yellow",font=30,command=lambda:get_weather(entry.get()))
button.place(relheight=0.8,relwidth=0.3,relx=0.67,rely=0.1)

frame2=tk.Frame(root,bg="blue")
frame2.place(relheight=0.6,relwidth=0.8,relx=0.1,rely=0.3)

lable=tk.Label(frame2,font=50)
lable.place(relheight=0.4,relwidth=0.6,relx=0.05,rely=0.1)

tk.mainloop()