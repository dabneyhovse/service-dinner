# Dinner Service

This is a service module that links into dabney backbone. It scrapes the dining.caltech.edu page to find out what's for dinner and more, and host the results in one readable place.

## Scraping Details
Some of the menus available on the website are setup through canva, while others are pdfs. Annoyingly, canva pages cannot be displayed in iframes if you dont have access to the project. Thus the dinner service uses a headless browser (pupeteer) to take a screenshot of the pages so it can show them. Pdfs, of course can be downloaded and parsed in a normal fashion.

Of course html is also easily parsable, but none of the canva menus are of great interest for parsing as they are largely static.

At the time of writing this the menu for dinner (which is the main point) is a pdf which contains a single table.