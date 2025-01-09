from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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
           
           { "id":4,
            "title":"Fourth Post",
            "author":"Jane Doe",
            "body":"This is the fourth post"},
            
           
        ]

def home(request):
    html = ""
    for post in posts:
        html += f'''
            <div>
            <a href="/post/{post['id']}">
                <h1>{post['id']} - {post['title']}</h1></a>
                <p>{post['body']}</p>
            </div>'''
    return HttpResponse(html)      
        

def post_detail(request, id):
    html = ""
    for post in posts:
        if post['id'] == id:
            html += f"<h2>{post['title']}</h2>"
            html += f"<p>{post['author']}</p>"
            html += f"<p>{post['body']}</p>"
            return HttpResponse(html)
        
        else:
            return HttpResponseNotFound("Post not found 😿")
        
       
    
    