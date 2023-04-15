# Unit 4 Project: Anonymous Forum Website

![DALLE](/assets/documentation/DALL·E.png)
<i> draw a low poly art of a person working on a computer on the edge of a building with sky scrapper in the night</i>

# Criteria A: Planning

## Problem definition

I am a student of a international IB high school in Japan. Like IB and many other educational systems a lot of it's content is private or only available with a subscription. The problem is that the subscription are extremely expensive and in my opinion are exploiting the students desperation to improve in their subjects. Also often, when a student finds a good resource their share them to their close friends, leaving the rest of the class out of the loop. Additionally some times teachers know where to find good resources but cannot share them because of the content being mostly pirated. As for it there is a strong need for a platform where students can share resources and help each other out. (See evidence of consultation in the appendix)##### TO DO

## Proposed solution

Considering the clients requirements there is a strong need for a platform where students can share resources and help each other out. Because of the varied nature of the students operating systems a website would be strongly advantageous. Moderns website are mostly made out of HTML which is the standard for browsers markup languages, CSS which allows more style personalization than HTML and finally Javascript which is responsible for the client side code of browsers. Now days the backend servers are usually drive by software like apache or nginx, but for this project I decided to go for a python framework called flask. Why? Because it has many advantages compared to nginx and apache, but mainly it is very modular and extensible (file uploads implemented in 5 lines of code), has very flexible routing and has a built in development server for easy debugging[^1]. To handle the data management of the platform, I propose using SQLite as the database system. SQLite is a lightweight, file-based database that is easy to use and does not require a separate server. It is ideal for small to medium-sized projects such as this one. Additionally, SQLite offers great performance with a small footprint, making it a good choice for web applications with moderate traffic. It also has good security features because of it locality [^2]. In addition to Flask and SQLite, I recommend using Bootstrap 5 as the front-end framework for the platform. Bootstrap is a popular CSS framework that provides a set of pre-designed UI components and styles that can be easily customized to match the look and feel of the platform. Bootstrap 5 offers a wide range of responsive design elements, such as navigation bars, buttons, forms, and cards, which can save a lot of development time and ensure a consistent user experience across different devices and screen sizes. It also has a rich set of utility classes that can help with common layout tasks, such as spacing and alignment. [^3]. To prevent my house from being raided by IB lawyers, one solution is to use the Tor. Tor is a free and open-source software that enables anonymous communication over the Internet. By using Tor, the platform can be hosted on a hidden service, which is only accessible through the Tor network and prevents you from sharing your server ip, preventing any tracing back to me[^4].

## Design statement

## Success criteria

1. The platform allows students to easily share educational resources, such as study materials, files, and helpful websites.
2. The platform is easy to navigate and user-friendly, with a clear layout and intuitive interface that is accessible to students with different levels of technical expertise.
3. The platform is secure and private, with robust measures in place to protect users' personal information and prevent unauthorized access to the platform's data.
4. The platform includes a post rating system, where users can rate and provide feedback on the quality of shared resources, allowing the community to identify the most helpful and relevant content. Also the platform offers proper sorting options, such as by subject, topic, popularity, and date, enabling users to quickly and easily find the information they need and stay up-to-date on the latest developments in their fields of study.

# Criteria B: Design

## System Diagram

![System Diagram](/assets/documentation/SystemDiagram.png)

**Fig.1** *System diagram of the Website*

## Data Storage

![Er](/assets/documentation/ER.png)

**Fig.2** *ER diagram of the Website

## Example of Data Entries

![Er](/assets/documentation/data_entry_user_table.png)

**Fig.3** *Example of data entry in the User table*

![Er](/assets/documentation/data_entry_post_table.png)

**Fig.4** *Example of data entry in the Post table*

## UML Diagram

![Er](/assets/documentation/UML.png)

**Fig.5** *UML Diagram of the website*




[^1]: https://stackshare.io/stackups/flask-vs-nginx
[^2]: https://www.infoworld.com/article/3331923/why-you-should-use-sqlite.html
[^3]: https://www.jadeglobal.com/blog/6-reasons-use-bootstrap-5-better-ui-development
[^4]: The Tor Project. (n.d.). Retrieved from https://www.torproject.org/ 