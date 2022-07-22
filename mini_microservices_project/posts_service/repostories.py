blogs = [
    {
        'id': 1,
        'title': 'My Post'
    },
    {
        'id': 2,
        'title': 'My Post'
    },
    {
        'id': 3,
        'title': 'My Post'
    }
]

def create_blog(title):
    blog_data = {
        'id': len(blogs) + 1,
        'title': title
    }
    blogs.append(blog_data)
    return blog_data

def get_blogs():
    return blogs