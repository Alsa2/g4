# Unit 4 Project: Anonymous Forum Website

![DALLE](/assets/documentation/DALL·E.png)
<i>  low poly art of a person working on a computer on the edge of a building with sky scrapper in the night</i> by [DALL·E 2](https://openai.com/product/dall-e-2)

Link:
2dwfg6zxrbkyu3f27z76n6widmc4sp3zpt7olzzozqzwchgqnt5j7nad.onion

# Criteria A: Planning

## Problem definition

I am a student of a international IB high school in Japan. Like IB and many other educational systems a lot of it's content is private or only available with a subscription. The problem is that the subscription are extremely expensive and in my opinion are exploiting the students desperation to improve in their subjects. Also often, when a student finds a good resource their share them to their close friends, leaving the rest of the class out of the loop. Additionally some times teachers know where to find good resources but cannot share them because of the content being mostly pirated. Other platforms (DO I GIVE NAMES) are prohibiting pirated content so there is no place for students to share resources. Additionally when you occasionally find some pirated content that escaped the nets it is probably malware or a virus, making trust worthy and reliable content even harder to find and moderate.


## Proposed solution

Considering the clients requirements there is a strong need for a platform where students can share resources and help each other out. Because of the varied nature of the students operating systems a website would be strongly advantageous. Moderns website are mostly made out of HTML which is the standard for browsers markup languages, CSS which allows more style personalization than HTML and finally Javascript which is responsible for the client side code of browsers. Now days the backend servers are usually drive by software like apache or nginx, but for this project I decided to go for a python framework called flask. Why? Because it has many advantages compared to nginx and apache, but mainly it is very modular and extensible (file uploads implemented in 5 lines of code), has very flexible routing and has a built in development server for easy debugging[^1]. To handle the data management of the platform, I propose using SQLite as the database system. SQLite is a lightweight, file-based database that is easy to use and does not require a separate server. It is ideal for small to medium-sized projects such as this one. Additionally, SQLite offers great performance with a small footprint, making it a good choice for web applications with moderate traffic. It also has good security features because of it locality [^2]. In addition to Flask and SQLite, I recommend using Bootstrap 5 as the front-end framework for the platform. Bootstrap is a popular CSS framework that provides a set of pre-designed UI components and styles that can be easily customized to match the look and feel of the platform. Bootstrap 5 offers a wide range of responsive design elements, such as navigation bars, buttons, forms, and cards, which can save a lot of development time and ensure a consistent user experience across different devices and screen sizes. It also has a rich set of utility classes that can help with common layout tasks, such as spacing and alignment. [^3]. To prevent my house from being raided by IB lawyers, one solution is to use the Tor. Tor is a free and open-source software that enables anonymous communication over the Internet. By using Tor, the platform can be hosted on a hidden service, which is only accessible through the Tor network and prevents you from sharing your server ip, preventing any tracing back to me[^4].

## Design statement

## Success criteria

1. The platform allows students to easily post educational resources, such as study materials, files, and helpful websites.
2. The platform is secure and private, with robust measures in place to protect users' personal information and prevent unauthorized access to the platform's data.
3. The platform includes a post rating system, where users can rate and provide feedback on the quality of shared resources, allowing the community to identify the most helpful and relevant content. 
4. Also the platform offers proper sorting options, such as by subject, topic, popularity, and date, enabling users to quickly and easily find the information they need and stay up-to-date on the latest developments in their fields of study.
5. The platform has a system for moderating content and user behavior to ensure that the platform remains a safe and supportive space for learning and collaboration, and that inappropriate or harmful content is quickly removed.
6. The platform is easy to use and navigate, with a clean and intuitive interface that makes it easy for users to find the information they need and perform common tasks, such as posting and searching for resources. ##DO I KEEP IT?

# Criteria B: Design

## System Diagram

![System Diagram](/assets/documentation/SystemDiagram.png)

**Fig.1** *System diagram of the Website*

## Data Storage

![Er](/assets/documentation/ER.png)

**Fig.2** *ER diagram of the Website

## Example of Data Entries

![Data_entry_user](/assets/documentation/data_entry_user_table.png)

**Fig.3** *Example of data entry in the User table*

![Data_entry_post](/assets/documentation/data_entry_post_table.png)

**Fig.4** *Example of data entry in the Post table*

## UML Diagram

![UML](/assets/documentation/UML.png)

**Fig.5** *UML Diagram of the website*

## Wireframe

![WireFrame](/assets/documentation/Wireframe.png)

**Fig.6** *UML Diagram of the website*

## Records of Tasks

| Task No | Planned Action                       | Planned Outcome                                              | Time estimate | Target completion date | Criterion |
| ------- | ------------------------------------ | ------------------------------------------------------------ | ------------- | ---------------------- | --------- |
|         | Planning: First Meeting with client  | Start collecting the context of the problem and research on current solutions | 5min          |                        | A         |
|         | Planning: Second Meeting with client | Defining problem, proposed solution, tools needed,  and the clients requirements |               |                        |           |
|         |                                      |                                                              |               |                        |           |
|         |                                      |                                                              |               |                        |           |
|         |                                      |                                                              |               |                        |           |

## Flowcharts

### Token Management

![Flowchart_1](/assets/documentation/flowchart_1.png)

**Fig.7** *Here is a flowchart describing the process logging in and creating the token for the user. Without and encrypted token system "not nice people" could just access your website, create and account, login, and change the user_id until they get admin permission. Not good*

### Search Sorting System

![Flowchart_2](/assets/documentation/flowchart_2.png)

**Fig.8** *Here is a flowchart describing the process of searching and sorting the posts. The user can search by title, tag author, or content. Also it can be sorted by popularity (all times, in the last month, last day...), by the newest and randomly.*

### Javascript part of the sorting dropdown

![Flowchart_3](/assets/documentation/flowchart_3.png)
**Fig.9** *Here is a flowchart describing the process of the javascript part of the sorting dropdown. I added a on_release at every dropdown so there is no need to add a submit button and the page will reload by itself, making the whole filtering and researching process for the user a lot easier. It also permits to get the previous arguments of the user, so he doesn't need to retype the search every time he changes the sorting.*




## Test Plan

| Type | Description | Process | Anticipated Outcome |
| ---- | ----------- | ------- | ------------------- |
|      |             |         |                     |
|      |             |         |                     |
|      |             |         |                     |

# Criteria C: Development

## Existing Tools
ADD TABLE

## List of Techniques

## Development

### Modals [Success criteria:6]

Sometimes in your program you need to display some additional information, and because there is a strong link between the current page and the information you want to display you don't want to redirect the user to another page. In this case, you can use a modal. A modal is a small window that pops up on top of the current page. It can contain any information you want, and it can be closed by the user, and doesn't involve any redirection / page refresh.

Here is an example of how we could use it in our project:

We are in the login page, and we want to add the option for the user to register. We could add a button that redirects the user to the register page, but this would be a bad user experience. Instead, we can use a modal to display the register form. This way, the user doesn't have to leave the login page, and the user experience is much better.

Here is the register button:
```html
<button type="button" class="btn btn-primary w-100" data-bs-toggle="modal" data-bs-target="#myModal">Register</button>
```
On page load, the modal is hidden, but when the user clicks on the button, the modal will appear. The modal is defined in the following way:
```html
<!-- Modal -->
<div class="modal" id="myModal">
    <div class="modal-dialog">
    <div class="modal-content">
    
        <!-- Modal Header -->
        <div class="modal-header">
        <h4 class="modal-title">Register</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
    
        <!-- Modal body -->
        <div class="modal-body">
        <form method="POST" action="/register">
            <!-- Just A form content for the registration> -->
        </form>
        </div>
    
        <!-- Modal footer -->
        <div class="modal-footer">
        <button type="button" class="btn btn-danger w-100" data-bs-dismiss="modal">Close</button>
        </div>
    
    </div>
</div>
```
![Modal](assets/documentation/website_screenshots/register_modal.png)
As you can see it's very customizable, we can add headers, footers, and even a form.

### Cards [Success criteria:6]
Bootstrap's cards are a versatile (logins, elements, items...) and customizable (images, headers, footers...) tool that can be used to create visually appealing content containers that are consistent across multiple devices, screen sizes, and browsers. 

Here is an example of how we could use it in our project:
```html
<div class="card" style="...">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```
![Card](assets/documentation/website_screenshots/login_card.png)
You can see here it, certified highly customizable.

### Bootstrap 5 [Success criteria:6]
Bootstrap 5 offers a mobile-first approach, improved customization, performance, and accessibility, with a large community for support and resources. Instead of having to use custom styles for every single element available, now I just import the library in three lines of code, mentioning the type of the object in the class and that it, no more custom styles. 

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
```
The middle one could be removed, it's just for the icons. Also you normally include this in the header.

Example of how to use it on a button:
```html
<button type="button" class="btn btn-primary">Primary</button>
```
I just need to add the class "btn" and the type of the button, in this case "btn-primary" and I get a nice and working button.

### Jinja2 [Success criteria:5]
Jinja 2 provides template inheritance (more on this later), conditional statements, looping constructs, and filters in html templates. Lets take example with the posts page, as described in one of my success criteria we need moderation, but not every one needs moderation, so we need to check if the user is an admin or not. We could do this with a simple if statement:
```html
{% if user.role == "admin" %}
    <a href="/delete/{{post.id}}">Delete</a>
{% endif %}
```
![Admin_controls](assets/documentation/website_screenshots/admin_controls.png)
*This will only display the delete button if the user is an admin.*

Another example is loops, when we load the post page we need to show many posts not only one post, so we need to loop through all the posts. We can do this with a for loop:
```html
<table class="table">
            <thead>
                <tr>
                    <!-- Table Colomn Names -->
                </tr>
            </thead>
            <tbody>
                {% for post in posts %}
                <tr>
                    <th scope="row">{{ post.id }}</th>
                    <td>{{ post.title }}</td>
                    <td>{{ post.tags }}</td>
                    <td>{{ post.content }}</td>
                    <td>{{ post.datetime }}</td>
                    <td
                    <button type="button" class="btn" style="background-color: #003566;color: white;" onclick="window.location.href='/post/{{post.id}}'">View</button>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
            </table>
```
![Post_Looping](assets/documentation/website_screenshots/post_looping.png)
*This will loop through all the posts and display them.*

There is also a lot of filters, to make the the datetime looking better in our posts for example we can use the date filter:
```html
{{post.date|date}}
```

### JWT Tokens & Cookies [Success criteria:2]
Ok, lets pause the graphical part, how do we add security to our website? One way are cookies with a purpose of identification. How? Here is a simple example
```python
session['token'] = user_id
```

![Bad](assets/documentation/website_screenshots/bad_token_website.png)

But this is <i>BAD coding practice</i>. Why? I could just open my browser, open the integrated inspector and manyally changing it to a admin user_id. Cookies are stored on your browser they need to be protected. 

```python
jwt.encode({'user_id': user_id}, token_encryption_key, algorithm='HS256')
```
Using the jose library for this.
One way is to encrypt the cookie with a key stored in the server, but this is also <i>BAD coding practice</i>. Why? Some times people commit mistakes, download a suspicious file, open the wrong link, and now the hacker can just use your encrypted cookie over and over without having to log in.

To limit the damage we can make sure that a token will expire after a certain amount of time. Now instead of adding only the user_id to the token we add the user_id and the expiration date. This way the hacker can't use the token forever, it will expire after a certain amount of time. 

```python
unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
ttl = token_duration * 60 + unix_timestamp
token  = jwt.encode({'username': username, 'datetime': ttl}, token_encryption_key, algorithm='HS256')
```

![Good](assets/documentation/website_screenshots/good_token_website.png)

To make sure to avoid problems with timezones we use the unix timestamp (best explanation ever[^5]). Which is the number of seconds since 1970-01-01 00:00:00 UTC.

To check if the token is valid we can use the following code:
```python
try:
    token = request.cookies.get('token')
    decoded_token = jwt.decode(token, token_encryption_key, algorithms=['HS256'])
    if decoded_token['datetime'] < (datetime.now() - datetime(1970, 1, 1)).total_seconds():
        # Token expired redirect to login
    else:
        # Token valid
except:
    # Token invalid (probably hacker) redirect to login
```

And finally removing the token after the user logs out:
```python
session.pop('token', None)
```

### Headers and Navbar [Success criteria:6]
The header is the first thing you see when you open a website, it's the first impression. It's important to make it look good, and very usable. Also the header is the same for all the pages, helping the user to locate himself. Also giving the user a complete new page at every new page is not a good idea, it's better to keep the user on the same page and just change the content. This is called Single Page Application (SPA), and I tried to implement if, but now only the index is a bit SPA but there is still some other pages.

Here is the header:
```html
<header class="py-3 mb-4 border-bottom shadow custom-white-bg">
    <div class="container-fluid align-items-center d-flex">
        <div class="flex-shrink-1">
            <a href="/" class="d-flex align-items-center col-lg-4 mb-2 mb-lg-0 link-dark text-decoration-none">
                <i class="bi bi-graph-down-arrow fs-2 text-dark" style="margin-right: 10px;"></i><p class="fs-4 text-center mb-0" style="margin-right: 10px;">[blog_name]</p>
            </a>
        </div>
        <div class="flex-grow-1 d-flex align-items-center">
            <form class="w-100 me-3" method="get" action="/search">
                <input type="search" id="search" name="search" class="form-control" value="{{ search }}" placeholder="Search...">
            </form>
            <div class="flex-shrink-0 dropdown">
                <a href="#" class="d-block link-dark text-decoration-none dropdown-toggle" id="dropdownUser2" data-bs-toggle="dropdown" aria-expanded="false">
                    <img src="...profileimage..." alt="user" width="32" height="32" class="rounded-circle">
                </a>
                <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="dropdownUser2" style="">
                    <li><a class="dropdown-item" href="#settingslink">Settings</a></li>
                    <li><a class="dropdown-item" href="#profilelink">Profile</a></li>
                    <li>
                        <hr class="dropdown-divider">
                    </li>
                    <li><a class="dropdown-item" href="/logout">Sign out</a></li>
                </ul>
            </div>
        </div>
    </div>
</header>
```
![Header](assets/documentation/website_screenshots/header.png)
*You can see here a trusty worthy header with a search bar, profile image, drop down with the option to go to the settings, profile and logout. Also the icon from bootstrap and the blog name linked to the index page.*

The navbar is the same as the header but without the search bar and the profile image. Also instead of being on the top of the page it's on the left side of the page. Also I added some links to move around the website. Here is the navbar:
```html
<aside class="col-sm-3 flex-grow-sm-1 flex-shrink-1 flex-grow-0 sticky-top pb-sm-0 pb-3">
                <div class="border custom-white-bg rounded-3 p-1 h-100 sticky-top">
                    <ul class="nav nav-pills flex-sm-column flex-row mb-auto justify-content-between text-truncate">
                        <li class="nav-item">
                            <a href="/" class="nav-link px-2 text-truncate">
                                <i class="bi bi-house fs-5"></i>
                                <span class="d-none d-sm-inline">First Link</span>
                            </a>
                        </li>
                        <li>
                            <a href="/..." class="nav-link px-2 text-truncate">
                                <i class="bi bi-search fs-5"></i>
                                <span class="d-none d-sm-inline">Second Link</span>
                            </a>
                        </li>
                        <li>
                            <a href="/..." class="nav-link px-2 text-truncate"><i class="bi bi-bricks fs-5"></i>
                                <span class="d-none d-sm-inline">Third Link</span> </a>
                        </li>
                        <li>
                            <a href="/..." class="nav-link px-2 text-truncate"><i class="bi bi-people fs-5"></i>
                                <span class="d-none d-sm-inline">Customers</span> </a>
                        </li>
                    </ul>
                </div>
            </aside>
```
![Navbar](assets/documentation/website_screenshots/navbar.png)

### Base Template(Pattern Recognition/Generalization/Abstraction)
As presented before, my website has, headers, navbar, bootstrap defined in the head, and having to constantly copy and paste the same code over and over again is not a good idea, especially when you change elements of it you need to change it in every page.

To avoid this kind of problems, jinja2 comes to the rescue. Jinja2 has a template engine for python, it allows you to define a template and then use it in other pages. For example i created the base.html file to act as a base:
```html
<!DOCTYPE html>
<!-- This is starting the html file, useful for the browser to know what to do with the file -->
<html lang="en">
<!-- This is the language of the page, it's useful for the browser to know how to read the page -->
<head>
  <title>Welcome {{ username }}</title>
  <!-- This is the title of the page, it's the name you see in the bar with all the websites open -->
  <meta charset="utf-8">
    <!-- This is the encoding of the page, it's useful for the browser to know how to read the page -->
  <meta name="viewport" content="width=device-width, initial-scale=1">
<!-- This is the viewport of the page, for multi device support -->

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
  <!-- Importing the bootstrap scripts -->
  
  <script src="{{ url_for('static', filename='js/script.js') }}"></script>
  <!-- Importing my custom made scripts -->
  <style>
    .custom-primary-bg {
      background-color: #FFD166;
    }

    .custom-secondary-bg {
      background-color: #003566;
    }
  </style>
  <!-- Custom made colors so when I change them I only need to change them here -->

</head>
<body>
<!-- ALERT Flash Box -->
    <header>
        <!-- Table Header -->
    </header>
            <aside>
                <!-- Table Colomn Names -->
            </aside>
            {% block content %}
            {% endblock %}
        </div>
    </div>
</body>
```
*As you can see here here is my base code, when you see a comment without code above it, it means that I removed the code and replaced it with a comment.*


Then I created a file called index.html and I used the base.html file as a base:
```html
{% extends "base.html" %}

{% block content %}
<!-- Add the page code here -->
{% endblock %}
```



[^1]: https://stackshare.io/stackups/flask-vs-nginx
[^2]: https://www.infoworld.com/article/3331923/why-you-should-use-sqlite.html
[^3]: https://www.jadeglobal.com/blog/6-reasons-use-bootstrap-5-better-ui-development
[^4]: The Tor Project. (n.d.). Retrieved from https://www.torproject.org/ 
[^5]: The legend Tom Scott https://youtu.be/-5wpm-gesOY