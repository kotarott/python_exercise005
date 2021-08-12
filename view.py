import eel
import desktop
import main

app_name="web"
end_point="index.html"
size=(700,600)

# @ eel.expose

    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)