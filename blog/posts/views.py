from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [ 
         
         {"id":1,
          "title":"First Post",
          "author":"John Doe",
          "body":"This is the first post"}
         ,
          
           { "id":2,
            "title":"Second Post",
            "author":"Jane Doe",
            "body":"This is the second post"}
           ,
            
           { "id":3,
            "title":"Third Post",
            "author":"John Doe",
            "body":"This is the third post"},
        ]

def home(request):
    html = ""
    for post in posts:
        html += f"<h2>{post['title']}</h2>"
        html += f"<p>{post['author']}</p>"
        html += f"<p>{post['body']}</p>"
        html += "<hr>"
        
    return HttpResponse(html)
