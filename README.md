# sa-team5

<br><br>

# Structure

Inside the /doc directory all files regarding the project management and design can be found.

The /TrainScheduler Directory contains the main piece of the PoC, and the /AnalyticsReporting, /TrainMaintenance, and /TrainOperations contains stubs for the other spaces.

The /live_data_generation contains the python script used to create example data, this is then showcased by the Vue project in /ui.


<br><br>

# Running the PoC/Demo

To run the PoC on your own machine you need to have both Docker and Docker Compose installed.
Now to run the PoC run the following command in the root folder of the git repository. It might take quite some time to run the first time because it has to build/download all images.

```
cd infra && sudo docker compose up
```
To stop the containers you can press `ctrl` + `c`, and can be pressed again to force shutdown instead of shutting down gracefully.

During the running of the containers you can look navigate to [the following URL](http://localhost:3000), and you will see the frontend.
Now you can safely shut down one of the two scheduler containers and the frontend will continue functioning without any problems, showing high availability works.

<br><br>

# Blog creation

Jekyll is the static site generator that is used for this blog, and [to see a live version click here.](https://blog-sa-tudelft.writerit.com)

## How to create blog posts

In this blog post we have two types of documents, actual posts that are visible on the front page and appendices. Both are written in Markdown but use different types of headers, it is also possible to add citations to these posts, how to do all of this can be seen below.

### Creating blog post files
To create a blog post you can just write a plain markdown file, the only thing required is a special header like this:

```
---
layout: post
title:  "Title"
date:   2023-03-06 17:53:53 +0100 
categories: category
---
```
**Be aware that if you put the date in the future you are not able to see or access that post yet.**

### Creating appendix files

And for the appendices we also can create a markdown file, and again with a special header, but this one is slightly different:

```
---
layout: page
title: "Title"
permalink: /appendices/design/something
---
```
Here take not of the permalink, this normally should be your folder structure starting out from the blog folder + the appendix name, so for example for the non-functional requirements it would look like this: \
```
permalink: /appendices/design/non_functional_requirements/
```

You can then use this permalink in other markdown files to reference to this page, you would do that like this:

```
Also don't forget to [look at this interesting post too](/appendices/design/something)
```

<br><br>

## How to add references
First you can add your BibTeX references at doc/blog/_bibliography/references.bib

Now in your blog post to cite you can use this command `{% cite paper %}` where the paper is the key assigned in the BibTeX reference. Ensure that you close your brackets because Jekyll will be extremely unhelpful if you don't close it and point to the first use of the `{% %}` block and not the faulty block. If you want to use other kinds of citations, [have a look here.](https://gist.github.com/roachhd/ed8da4786ba79dfc4d91#citations)

Now to actually see your references add this line to the bottom of the markdown file, `{% bibliography --cited_in_order %}` this will generate your references in the order of citation, and only those you actually used.

To actually build the blog look below in the next section.

<br><br>

## How to build the blog

To view to blog on your local machine for quick feedback use the following commands:
```
cd doc/blog/ # This step is important, otherwise the website will not generate correctly
bundle exec jekyll serve
```

When you open a merge request then a pipeline will launch so you can view your changes in real-time, [have a look at that here.](https://test-blog-sa-tudelft.writerit.com/)

To get this to the live version create a merge request, the built task will be triggered to verify Jekyll can compile your version correctly. If your MR is accepted and the branch is merged into main, the CI/CD will kick off a deployment task to deploy the blog to [the Azure Static Webpage used to host this blog.](https://blog-sa-tudelft.writerit.com/)

<br><br>

## Authors and acknowledgment
