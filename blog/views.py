from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain-g2055d4c5f_1920.jpg",
        "author": "Javier Blanco",
        "date": date(2022, 7, 21),
        "title": "Mountain Hiking",
        "excert":"There is nothing like the views you get when hiking in the mountains! And I was not even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit error nulla vero repellendus, possimus eveniet magni iure mollitia? Numquam obcaecati eum facilis ipsum, cum voluptatem dolore non nisi cupiditate dolores?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit error nulla vero repellendus, possimus eveniet magni iure mollitia? Numquam obcaecati eum facilis ipsum, cum voluptatem dolore non nisi cupiditate dolores?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit error nulla vero repellendus, possimus eveniet magni iure mollitia? Numquam obcaecati eum facilis ipsum, cum voluptatem dolore non nisi cupiditate dolores?
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "programming-g53c633f33_1920.png",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excert": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "forest-g81f64045e_1920.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excert": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def home_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    
    # Typically, we have learnt how to use a list comprehension like the following to return certain items that meet some condition. However, the follow line of code will always return a list, even if there is just one line, therefore a list of one item. We do not need a list of value but a value itself. 
    # post = [post for post in all_posts if post['slug'] == slug] 
    # That is where the built-in function next comes in, to return the next value that meet the condition
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-details.html', {
        'post': identified_post
    })