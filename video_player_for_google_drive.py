from google.colab import drive
drive.mount('/content/drive')

from IPython.display import HTML

url = input("please enter your video url : \n")

HTML(f"""
<video width="1080" controls>
  <source src={url} type="video/mp4">
</video>
""")
