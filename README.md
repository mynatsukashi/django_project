<h1> Django Project: step-by-step guide</h1>
<p align= "justify"> Welcome to Shelf Nerds - site where users can review book, comment on already posted ones, and just have fun! I will direct you through the whole site and explain what I have done. </p> 
<br>
<p align="justify">When you run the server, it opens the main page with menu bar (Home, Create, LogOut), posts and its comments. Posts are sorted in descending order (newest post goes to the top).</p>

<p align="justify">I created three main models: Author, Book, Review. Review is the main post on the page, where you can see author, book title and description. For comments section I used "Comment" model. Additionally, to implement multiple genres, I created separate Genre model.</p>

<p align="justify">From the main page you can redirect to: 
<ul>
<li>Details page by clicking at any book's title</li>
<li>Create page to create a new post</li>
<li>Home page</li>
</ul>
</p>
<p align="justify">Now let's take a look at posts itself. On the top of it you see who wrote this post, when, what time. Besides, book title and author are presented with rating (showed in stars). Book genres separated by comma, description, aka review of the user. Then starts comments section: how many comments where written, who wrote those comments.</p>

<p align="justify">To find post that you need I created a search bar (followed by instructions from the project requirements). Unfortunately, I couldn't create filters for my site due to time limitation.</p>

<p align="justify">When you press on Log Out button, it redirects you to Log In page. In case if you haven't created account yet, it allows you to create your own. There are no stricts limitations of password and username, I specifically deleted those requirements to make it more comfortable to sign up quickly. </p>

<p align="justify">I have never written ReadMe.md file before, it might be incorrect, but I will answer all the questions on the demo session! :) </p>

