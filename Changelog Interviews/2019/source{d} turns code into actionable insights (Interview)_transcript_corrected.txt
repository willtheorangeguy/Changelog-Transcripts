**Adam Staravia:** You're at source{d} now... Give me the breakdown of what sourced{d} is. It's formed around open source... Everything right now is open source, right? There's nothing you have that's a paid product, at least yet.

**Francesc Cambó:** Everything we do is open source. We are working on an enterprise edition for one of the products, and basically the whole idea is that everything will keep on being open source, except for one thing that allows our product to work distributed.

To back up a little bit and give a little bit a context - what we do at source{d} is our tagline is "Machine learning for large-scale code analysis."

**Adam Staravia:** I like that tagline.

**Francesc Cambó:** We worked on that tagline quite a lot, so I'm happy you like it.

**Adam Staravia:** It's succinct, and it gets the message across. That's the whole point.

**Francesc Cambó:** The whole idea behind it is when you're writing code, normally people think about the fact that you write code, then you build it, and you ship something, and what you ship is what matters, right? Source code is just a way to get there. And what we realized is that actually it's a huge and very, very deep source of data. When you have a Git repository, you can actually see what's happened there since the beginning of time until now. You can actually analyze trends, you can see so much stuff in there.

So what we did is we created this engine product that basically what it does is it provides a SQL interface, so you can find things in the repository. You can do things like "Find commit messages with this text", or whatever, but you can actually go even deeper than that and go into actually "I want to see the content of the file, I want to parse it, I want to extract the function names, I want to extract the strings", or whatever. So there are a bunch of different projects that make this possible, and basically every single one of those projects is completely open source, and I've created a product which is called The Engine, which is putting all those together nicely to use; a little binary, you get started and everything just works. That is what we call the code as data - seeing source code as a source of data.

The other part is ML on code. ML on code is the part that I've been talking around, because it's super-exciting. The whole idea is learning stuff from source code. One of the things that you can learn, for instance, is say to predict a token in a program, if you're given the rest. I give you a Go program, and I've removed one viable name from somewhere, and you need to predict it. You train the neural network to do this, and eventually it will be able to do this quite correctly.

\[04:23\] Now, what we try to do is not to predict the missing pieces of a program, because in general programs do not have missing pieces, but what we can see is that if what we predict and what you wrote is very different, and even more than that, what you wrote we know that is unpredictable, what we can tell you is that probably there's a bug.

It's a slightly complicated way of doing it, but what this detects is copy/paste errors. When you copy a section of code and paste it somewhere else, and you modify a bunch of things, but probably when you're checking for the error that's not what you wanted, and you're checking for the previous error, or something like that... That happens all the time. I know it happens to me all the time. With this, you're actually able to detect it directly.

Building something that would use static analysis for that - it is possible, but it's really hard, because static analysis deals with syntaxes, and grammar, and stuff like that, but not really with the semantics of the program. I like this idea, when you're writing code, there are two things - there's what you say, and what you mean. When those two things differ, that's when you have a bug. When you're saying "Oh, actually that's not what I meant. Sorry" and you need to fix it, what we're trying to do is apply machine learning to see what you meant, and compare it to what you said, and see whether we can find bugs in there. That's super-interesting, super-powerful, and we are doing a lot in that, but that is more like the future.

Currently, the cool thing that we've just released yesterday was an analysis of the Kubernetes codebase.

**Adam Staravia:** Yeah. I was going to ask you about this - a pretty lengthy, data-filled blog post. Great job on that. Good timing, too.

**Francesc Cambó:** Yeah. I mean, the cool thing is that there's so much data in there. You have almost two million lines of code, and we've been working on that project since 2014, I think... So that's a lot of data in there. We were able to find things like "Oh, so how many exported functions are there, and how did that grow over time?" We saw that from version 1.0 to 1.4 the API grew by four times the size... which is bad. If we kept on doing that, it means that by now we would have -- so we went from 4,000 to 16,000; if we kept on going the same pace, we would have something like around 100,000 endpoints. That is not maintainable. It's too complex, and no contributor will be able to think about Kubernetes as a thing. You have to split it into pieces, right?

**Adam Staravia:** Right.

**Francesc Cambó:** So yeah, we were able to see all of these things, super-interesting, and the whole idea behind that article was give back to the community. When you tell to the community, "Hey, you're doing great. You're maturing, and you can tell, and the innovation is somewhere else, which means that the APIs are perfect - all of this data... I mean, it's not news-worthy, I'd say, right? Because it's nothing crazy new. But it's just confirmation through data that this feeling of "Kubernetes is doing well" is actually accurate.

**Adam Staravia:** Right. You also were able to account for the different languages within Kubernetes, so it shows where there's declines or growths, or even for developers who are thinking about transitioning to a different language, just identifying where some of their future value for their career could be. There are a lot of indications around that. Or even, as you mentioned, contributors and healthy growth, and things like that - those are all indicators of "Well, 8,000 people are here at this conference now, versus 4,000 last year in Austin." What that shows is a significant sign of investment and betting on Kubernetes... So understanding that it is healthy, in fact, based on true data. It's amazing.

**Francesc Cambó:** \[08:21\] The cool thing is I will open source the way I did all of this analysis, but it is literally just a bunch of SQL and a bunch of Python. It is not that complicated. I mean, I'm not a good Pythons, let's not go there; I'm not perfect at writing Python, I had to learn a lot... But still, it's actually pretty straightforward. When you say, for instance, "I want to count all the languages that I have", basically what you're doing is "Okay, give me all the files, and I'm going to use this language function that classifies and tells you what language it is, and classify that. Easy." I think we are around at 72,000 commits on the Kubernetes codebase, so I'm going to do it every 1,000. Every 1,000 commits, find how many you have, and just create the plot, right?

**Adam Staravia:** Yeah.

**Francesc Cambó:** So it's actually very straightforward, but the information we got from that was super-interesting. I shared it with Kris Nova and Joe Bed, and they were very interested in checking it out. They found a little bug, because apparently I'm not very good at reading, so instead of "a million lines of code" on the PR that was sent to many analysts, instead I said "billions".

**Adam Staravia:** Oh, gosh... There's a difference there.

**Francesc Cambó:** \[laughs\] Yeah, so Joe Bed now is calling Mr. Billions, which is awful.

**Adam Staravia:** Nice. So the example you're sharing here, at least with the analysis, is an open source project, right?

**Francesc Cambó:** Yeah. All of this is open source, and not only open source, but also Apache v2.

**Adam Staravia:** What I mean is analyzing an open source codebase... So maybe give an example of, say, how this applies to enterprises; maybe somebody that's got their internal code -- I know most things are open source, but we're building our own products, and those products tend to be behind the scenes, and the things we touch tangentially, through dependencies, our contributions are in the open source world. So how does source{d} - it's Engine, right?

**Francesc Cambó:** source{d} Engine, yeah.

**Adam Staravia:** So how does that apply in a case where it's my own code? How do I run it on my own codebases?

**Francesc Cambó:** You can run it exactly the same way. The cool thing is that since the beginning we've developed all the tools we've built to be run on-prem.

**Adam Staravia:** Okay.

**Francesc Cambó:** I used to work at Google... If you go to a Google, and you tell them "Hey, we're going to be sending you source code over the network to some random server...", they're going to be like "There's no way you're doing that." So we knew that source code is a very, very delicate piece of data, so everything can run on-prem; everything runs on Docker. You can even have a Helm chart and just start everything up, very easy. And everything is open source.

**Adam Staravia:** Would you do this on a laptop, would you do this at the server level? Where's the interface?

**Francesc Cambó:** It depends on the amount of code you have. If you're doing it on a laptop... Yeah, it's going to take some time.

**Adam Staravia:** So this is highly process-intensive.

**Francesc Cambó:** Yeah. I mean, it's pretty large, because it's big data. The analysis that I did for the Kubernetes codebase - I was running on an instance in Google Cloud platform, with (I think it was) 96 cores. So you know, a pretty large instance... And yeah, the analysis of counting all the languages, for all the commits over time took around ten minutes. It's not that bad, actually... But if you're trying to do this for a very large thing, 96 cores is going to be maybe enough at the beginning. But eventually you'll want to have it distributed, and that's where basically we're saying, you know, once you need more than one node, then it's enterprise edition, and we should talk... Because the whole idea is that we want to give as much as possible to the open source community, and especially the engine can be a really powerful way to obtain data for all the research part of machine learning. There's a lot of people doing research, and they need datasets. The fact that they will be able to generate those datasets by running SQL queries that they already know very well - it's super-powerful. So we want to make sure that they've got access to that.

\[12:14\] But for larger companies that want to do analysis -- and the interesting thing is that those metrics that we came out with, you can tweak them... And we are going to come up with a catalogue of the kind of metrics that you should be figuring out and looking at. For instance, if you're saying "I'm going to be moving on cloud-native... Cloud Native Computing Foundation, I'm going to go cloud-native." Cool. What are the things that you should be looking at? Well, you should have a Docker file, you should have continuous integration, you should have continuous deployment. All of these things nowadays are in the source code, so we can analyze those things and give you a little bit of an idea of, if you're going towards being cloud-native, how far away are you from getting there, and also, what are the things that you should be changing, what piece of the source code should be worked on in order to get there.

That is super-useful, because basically the whole idea is that it brings visibility to processes like going cloud-native, or adopting inner source, or adopting DevOps... Lots of people talk about "Oh, we're going to be doing DevOps." What does that mean, right?

**Adam Staravia:** Please answer that...

**Francesc Cambó:** Oh, yeah... I mean how many hours do we have...? \[laughs\] No, like -- doing DevOps can be many things, but the beginning is "Well, you're going to need to have clear observability, you're going to have metrics, you're going to have a lot of different things that then you're going to be fetching into some systems that will allow you to understand what your system is doing." But all the observability things - again, it's source code. When you think about infrastructure as code, where do you find that? Source code.

We keep on putting more and more stuff inside of Git repositories, and what we're trying to do is "Sure, that's great, but now let's analyze it." Let's use that data we've put in there to try to understand what's going on.

The cool thing about being SQL -- because I was, and I'm still thinking about offering a GraphQL thing, because Git repositories are trees, and once you parse code, you get a tree; so everything's trees, and GraphQL for trees is great... But the fact that it's SQL, it allows you to mix it with other datasets. You have Looker, or Power BI, or things like this where you can have many datasets and do a query across many different databases. Imagine doing something where you're saying -- say inner source; The whole goal under inner source is really make sure you break the silos in a company and that everybody collaborates with each other. Like the Google-style, Facebook-style, even though the inner source term was created at PayPal. In order to measure how well you're doing, the whole idea is that you need to first know who is in each team. Unfortunately, that is not in your Git dataset, so you're going to need to mix it with some other dataset - HR dataset, or whatever it is. So Looker, or Power BI, and I think that even Tableau - they will allow you to do these kinds of things...

**Adam Staravia:** You can look up the repo URL on GitHub, even if it's a private GitHub repo as well.

**Francesc Cambó:** Yeah, yeah. So the cool thing is that--

**Adam Staravia:** Because you have teams at the org level, so you could look up not so much by the repo, but by the repo URL.

**Francesc Cambó:** Yeah, yeah. So the thing is that all of that -- that is the GitHub API. We work with any Git repository, so all the concepts that we work with are Git, for now... That's why, for instance, the organization is a GitHub or GitLab. Point: you could expose it from a different dataset. Just download the whole thing, put it in a MySQL and that's it. You can do that, too.

**Adam Staravia:** Right.

**Francesc Cambó:** \[15:50\] And that's actually really powerful, because you can then mix it with (if you have) financial data, or things like this; you can try to see correlations... One that I like is the correlation of "Can we correlate the number of commits with the money we're making? When developers write a lot of code, is it good?" Maybe it's bad, and you should stop your developers from writing more code, who knows...?

**Adam Staravia:** Or is there no relationship at all, and it just doesn't matter...?

**Francesc Cambó:** Yeah, yeah.

**Adam Staravia:** Interesting.

**Francesc Cambó:** All of these things -- once you expose all of that data, our idea is data analysts and data scientists are going to be able to do really cool stuff with that.

**Adam Staravia:** It sounds though like source{d} Engine is -- let's maybe use an analogy; I'm a painter, I want to paint a painting, but it sounds like source{d} is just a brush. I've still gotta apply the right kind of colours and understand colour theory. It's a tool to get there, but it's not the recipe to get there. You have to write your own queries.

**Francesc Cambó:** Yeah, for the metaphor I would say that source{d} Engine wouldn't even be the brush or anything, it would actually be deeper than that - it would be the thing that makes the paint for you. You're going to be extracting all of this data, and then with the data you're going to be painting something. You're going to create your dashboards, you're going to be proving your point... Data and statistics - those are not new. We've been using statistics to prove our point for quite a while.

For data analysts - if you tell a data analyst "Oh yeah, you should use Git in order to find this, so let me explain to you how Git log (to start with) works, and how branches work, and how commits work, and what is a merge commit, and all these things...", the data analyst probably stopped listening to you like five minutes ago. So the idea of exposing all of these concepts in a way that data analysts understand is actually really powerful. Because a data analyst is also a data scientist and also a machine learning scientist.

**Adam Staravia:** So is the interface a config file of queries, is it a dashboard of queries? What's the interface to sit down and get something done?

**Francesc Cambó:** The interface - there are a couple ways of doing it. Source{d} Engine itself is a SQL interface. We do have a playground that allows you to have a list of all the tables, understands well what a tree is, and it shows it better than what you see with a traditional SQL client... But I think that the best way to do this is actually with Jupyter. Jupyter notebooks work incredibly well. That's what I've been using. You have your text describing what you're measuring, then you have your SQL query that you send, then you use the result, you use a little bit of Python, and then you generate your graph, and all of this stays in the same place. That's what I've been using, and it's a really great experience, to be honest. I like that better. But if you want to use the MySQL client from your command line, that works too. It's just MySQL. Anything that works with MySQL works with the Engine.

**Adam Staravia:** The example you've talked us through -- and if you want, I'd love to go into some of the data that you pulled back for Kubernetes, if you want to share some of that...

**Francesc Cambó:** Oh, yeah.

**Adam Staravia:** But I also want to mention that that's an example that you've done. What's an example of, say, someone who's a customer, an adopter of your open source, and they're using source{d} Engine in ways that you -- share some of the imagination of users.

**Francesc Cambó:** We've been working with especially large banks, and large banks are fascinating because they have an incredible amount of source code... And that incredible amount of source code goes from their cloud-native Kubernetes, Docker Compose, stuff like that, and COBOL. They go all the way back to having COBOL. When you tell them that they're going to be able to measure the technical debt, for them, it's like "Oh, yes! Let's do this!"

**Adam Staravia:** Because they're all about the debt, right? \[laughter\]

**Francesc Cambó:** Yeah, true.

**Adam Staravia:** Let's write what's black.

**Francesc Cambó:** \[20:02\] Yeah. \[laughs\] No, but once you tell them -- many banks do not really even know how much code they have. There's so much of it that when you tell them "Okay, so how much COBOL do you think you have?" and they're like "In-between 100,000 and maybe half a million..." I was like, "Well, if you're going to put some budget to go and rewrite that in something more modern, good luck, with that estimation..." So the idea is we're going to be able to bring all of these data to them, so they're going to be able to make informed decisions. Counting lines of code per language, which for us is literally a "group by" query, it's super-simple to do... For them, it was like "This is actually fascinating."

The other change that lots of banks want to do is going back to the inner sourcing. Large banks, they have much IT groups all around the organization, and they want them to work together well, and the first piece is to figure out who is doing what, what resembles to what, how much code duplication you have... We have a thing that analyzes code duplication not character by character, but rather extracting the abstract syntax tree, modifying a couple of things, so it's actually a very smart way of figuring out whether two pieces of code are very similar. They're so similar that if you saw them next to each other, you would say "You need to refactor them and just write one function." We're able to detect this automatically, and this helps a lot, because if you imagine you're like the CTO of a bank, and you have this codebase that dates from the '60s, and they tell you "Please put it on the cloud." That's hard. That is a harsh thing to ask anyone.

The idea of being able to tell them, "Well, actually all of this source code - let's see which parts are going to be the easiest ones, there's MTA, "modernizing traditional applications", which is not really cloud-native, but we can make it be cloud-native, we can make it run in Kubernetes... And then what is the COBOL that -- you know, that's going to be an interesting challenge to migrate. So having a view of all of this by just running a couple queries is really powerful. The other option is literally running -- I'm going to be very hopeful and say that you could run a really huge Bash script calling Git very often, and maybe you will get something similar... But it would take hours instead of seconds.

**Adam Staravia:** Yeah. I think the thing I'm trying to drive out here is that clearly you can pull back a lot of intelligence if you know what you're looking for. It seems like maybe some consulting is involved there, or at least the right kind of teams in place to know how to ask those questions of bigger data analysis for your data analyst, for example...

**Francesc Cambó:** What we're trying to do -- we're not that interested on the consulting side of things...

**Adam Staravia:** Well, not so much as a company, but it seems like the intermediary there is someone who knows how to use source{d} Engine.

**Francesc Cambó:** There's going to be service integrators, there's going to be people not only installing the things, but also...

**Adam Staravia:** Okay, so you're kind of building out an economy even, almost...

**Francesc Cambó:** Yeah, yeah.

**Adam Staravia:** With the final product you'll -- basically, you're going to have an enterprise version of it, and/or also enable others to make sense of data.

**Francesc Cambó:** Yeah. Nowadays, you have many consultants that are helping with these kinds of tasks. What we're building is a super-powerful tool for those consultants.

**Adam Staravia:** Right.

**Francesc Cambó:** And then -- I mean, they're going to be able to run it internally, and keep it as a dashboard, so... It's observability, it's all about seeing where we are right now, and see where we want to go and how to get there.

**Adam Staravia:** There has to be a lot of tools around this front.

**Francesc Cambó:** Observability on source code - not really, no...

**Adam Staravia:** I mean, at this level, what you're doing - it kind of reminds me of... You probably know his name - Felipe, I believe... Worked at Google, and he would do these things...

**Francesc Cambó:** Oh, Felipe Hoffa.

**Adam Staravia:** Yeah, yeah. This seems almost like you were inspired by the work he's done.

**Francesc Cambó:** \[23:56\] I actually wrote a blog post that was like the one that Felipe worked on, but I'm pretty sure that mine got more views, so... Hey, Felipe... \[laughter\] No, but the idea was I was trying to analyze on all the source that we had on BigQuery, analyzing which is the most common package thing, or which is the most common package we import, and stuff like that... And it was everything... Like, it was cool to do, but also regular expressions everywhere. Our idea is that it's kind of similar to that, but imagine that--

**Adam Staravia:** Even a better interface...

**Francesc Cambó:** ...instead of doing "Find function names", it's going to be "fun.\*" and then something that starts with the letter, whatever... That's a pain to write. And also, what if now you don't have a Go function, but you have a Go method; actually, that will not work anymore, right? So what we're doing is instead allowing you to extract the tokens that you care about. We work with this concept that we call "universal abstract syntax trees", and the whole idea is that it's an abstract syntax tree, so the result of parsing a program, but it allows you to extract things by using annotations, and those annotations are universal, right? Say, a function -- a function is a function, no matter what programming language you have, right? An identifier, same thing; strings, same thing. So if you want to extract the function names, what you need to do is basically use the LAST function, you pass the content, you pass what language you want to use, and then you just pass something that -- it's a XPath thing that basically says the function names.

**Adam Staravia:** Right.

**Francesc Cambó:** Same thing will work for Go, for Python, for Java, for no matter what programming language you're trying to use. That is the kind of power that, you know -- yeah, you could use it with an incredibly... Like, I would love to see the regular expression that that's the same thing, if someone has the time to write it...

**Adam Staravia:** Just for fun, right?

**Francesc Cambó:** Yeah, yeah... Just for pain... \[laughs\] But that would take a super-long time, and even once you're done, if you ask the person that wrote it "Are you completely sure that this covers all the cases?", probably the answer is no. So we are making it a much more reliable and easy way to kind of extract the same information that you could in some other ways.

**Break:** \[26:17\]

**Adam Staravia:** Let's give a prescription then for those listeners out there thinking "I'd love to find some intelligence, I'd love to come in on a Monday morning with greater intelligence to my codebase..." Give some examples of how someone listening to this, whether they're in a larger team, smaller team, their own project, whatever... What's a good prescription for getting up and running?

**Francesc Cambó:** I would say the best place to start is you go to sourced.tech and check the Engine, download it... It's a little binary, and it only has one dependency, which is Docker, so probably you already have it on your computer.

**Adam Staravia:** I was curious why on the macOS installation process you got a use Homebrew. I know it's just a binary file, and you just put it in your Bin folder, but I was wondering why--

**Francesc Cambó:** Oh, we don't have Homebrew yet, but we will get there, yeah.

**Adam Staravia:** The process to install it seems so simple... It's like, "It's probably a simple Homebrew recipe as well..."

**Francesc Cambó:** Yeah... I need to work on that, but you know, it's been a busy week... \[laughs\]

**Adam Staravia:** Well, just going on any macOS, install, I'm always expecting a Homebrew process, or something specific to the way a language installs certain things.

**Francesc Cambó:** There's an issue somewhere to implement that, yeah...

**Adam Staravia:** I bet. Sorry for pulling that off...

**Francesc Cambó:** Oh, no worries. So once you have that binary, however you install it, the idea is that you can just run something like "source: SQL", and now you are inside a SQL client, and you are acquiring all the Git repositories that you've found from the directory where you were, right?

So now the cool thing is that you can start by doing things like, you know, count the commits that you have per month, or something like that. That is actually very interesting, because you can see how much the team has been working overtime, or you can count the number of lines, or things like this. These seem like pretty simple things, but even those are actually going to show weird things. For instance, for Kubernetes, I was like "Oh, I'm going to count the number of lines of code." It goes up, right? Sure. But it also goes down, eventually... And it's really weird, because it goes down by a lot of lines of code...

**Adam Staravia:** Somebody's having some fun, deleting some stuff...

**Francesc Cambó:** Yeah, and I was like "What is going on with this?" So no matter what dataset it is, you're going to be finding a lot of cool stuff, because those are organic datasets. We keep on committing all the time, and we're going to make mistakes. You're going to see from time to time the number of files goes up by like thousands, and then goes down again, and then you look at that, and it's like "Huh, someone vendored the dependencies that they were not supposed to..."

**Adam Staravia:** \[laughs\] Whoops...

**Francesc Cambó:** Yeah... Like, "Whoops..." But all of these things - you're able to see more information, and the thing is that as soon as you start playing with this, at least in my experience, the more answers you get, the more questions you get. Like, "Okay, so I saw these, but what happened with this thing?" Or you can also find things like -- it's a really cool game, and I'm going to be open sourcing it soon... Have you ever heard about the Degrees of Bacon?

**Adam Staravia:** Yes, Kevin Bacon. Yes.

**Francesc Cambó:** Kevin Bacon, yeah.

**Adam Staravia:** Six Degrees of Kevin Bacon.

**Francesc Cambó:** Six Degrees of Kevin Bacon. So you can do the six degrees of Kevin Bacon, but on Git; trying to figure out... So from me to, say -- I don't know, someone famous in the Go community; Rob Pike, right? How many degrees are there? For me, I edited a file that was edited by someone else, that edited another file, that was edited by someone else, that was edited by Rob Pike, something like that. You can actually extract that information from Git. So you can extract really useful insights for your business, but also you can build pretty cool games.

\[32:10\] So that's the thing... Have fun with it. It's data, so if you've ever done any kind of data analysis -- I mean, it's called data exploration for a reason. You do not necessarily know what you're going to be finding, but that's the whole game; you're going to be able to extract some things, and then if you're actually interested on some specific metrics, check out the Kubernetes blog posts that we wrote, where you're going to have all the different queries that we run, and you can run the same thing for you, and see for instance the trends on what prominent languages are you using, how are they growing? Are you using more Go than before, or maybe you're using more Java, or Python? All of these things are going to appear very clearly on your graphs.

**Adam Staravia:** What do you say to maybe some for-profit (say) SaaS competitors, to say "This rough idea", which is basically data-driven intelligence in a development team? So "Look at our codebase, our repository, learn some insights." What do you know about other competitors and how do you see source{d} moving forward, coming from open core, eventually you're going to have your own products and different ways you can sustain financially...? I mean, you are a company, so eventually -- you've got open source, but that's only going to last so long, until you actually have to create some products to generate revenue... Where will you be at in this space?

**Francesc Cambó:** It is hard to answer, because we are somewhere in between many different fields. There are some companies that do software metrics, but the thing is that the software metrics they provide are the software metrics they provide; that's it.

**Adam Staravia:** Not the tool...

**Francesc Cambó:** Yeah.

**Adam Staravia:** You have no visibility into...

**Francesc Cambó:** Yeah, you can choose several metrics, and some of them might be fascinating; you can do lines of code, number of commits, stuff like that... But also you can do things like diplomatic complexity. Diplomatic complexity is a really cool concept, but probably doesn't apply to you. What you want is things like "Actually, what I care about is how many comments do I have per function? Are all my functions correctly commented, or not?" Those things - probably what you want to do is express exactly what you want. That's why I think that what we're building is something that many of the companies that compete with us - they could be powered by us, really.

**Adam Staravia:** That's I was thinking. It's almost as if you're building their future tools. If they've done what they've done, and they've got maybe (say) 2–3 years into their business, but they don't have the tooling, they may actually retro-fit their business to essentially become a service provider on top of source{d} Engine, for example.

**Francesc Cambó:** If they're interested in something like that, then talk to us. That is the thing, what we're building is --

**Adam Staravia:** So source{d} essentially is a standard. Source{d} Engine, at least, could become an open source standard for data intelligence in codebases.

**Francesc Cambó:** Absolutely. Yeah, the idea is we want to extract data from source code. The most common way of storing source code is Git, the most common way of analyzing data is SQL. We just put them together. That is our first product, but we actually built it to extract information that then we can use to train models and do machine learning. We believe that many people are interested in doing that kind of things, and we want them to do it, because at the end of the day, if we end up being successful, our code review tool which is called Lookout, it will provide an opportunity to write analyzers, to basically classify a piece of code as "Does this contain some specific thing or not?" Does this contain a bug, does it not? Does it contain lint errors? ...something like that. Those can be done with completely traditional tooling, like linters and stuff like that, but also we believe that many of them will need machine learning. We cannot build all of those things. We're building the platform, so other people can build on top of us.

**Adam Staravia:** \[36:00\] So what you're talking about is a product called Lookout; it's in beta right now... You can request a demo obviously if you wanted to...

**Francesc Cambó:** source{d} Engine is in beta; I think that source{d} Lookout is in alpha, probably...

**Adam Staravia:** It says here on your site beta.

**Francesc Cambó:** Really?

**Adam Staravia:** Yeah.

**Francesc Cambó:** That's probably a mistake...

**Adam Staravia:** "Sign up for the beta", I see it right here...

**Francesc Cambó:** I'll talk to my team, I'm pretty sure that is an alpha normally... Sign up for the beta for the source{d} Engine, beta, yes. I'm pretty sure Lookout is still alpha, but anyway, again, it's completely open source, you can check it out, run it on your project etc. We do not think that running the engine as a SaaS (software as a service) makes much sense, because people do not want to send their code to random servers... But the assisted code review - we want to make that a SaaS, so eventually you will be able to just add as a GitHub application that just reviews your code. We've done that for all of our projects, and it works really well. It's able to warn you about "Hey, this piece of code is suspiciously similar to that piece of code in that dependency. Did you copy/paste it?" or "Maybe you should be calling that function..." There's a lot of perfect hands-on what you should be doing, and we want to have more and more of that. Those probably will have eventually a SaaS version that you can just click a button, install it in your repositories, in your own GitHub or GitLab, and that's it.

For many people - the people that really care about deep analysis of large codebases - they tend to also not want to share their source code. So for that it doesn't make that much sense to have a SaaS for the engine.

**Adam Staravia:** It makes sense. So if folks sign up for the beta, what can they expect? -- sorry, alpha. That's what I was trying to do - tee up the fact that it's sort of an early release; maybe you're even looking for feedback.

**Francesc Cambó:** Yeah. So that's the whole point - we are trying to get people to use the product, file issues, let us know what they think... File issues for things that do not work, but also for things that they would like to do. This is a pretty young project; we released it two months ago, something like that, so it's pretty early on... The idea is that we're going to be working with really large companies to try to make it as good as possible, but at the same time we also want to have the input from the community, because they have different needs.

We don't want to end up having something that targets only large companies, but is pretty useless for developers. We want to build something that everyone can get something from. Large companies, they're going to have some specific analyses and some specific things - that's what our enterprise edition will have... But also, our free edition will always be free. We want people to make sure that that becomes as good as possible, and also, if you feel like it, contribute. It's written in Go, it's a really cool project; we use a lot of open source, we use Pilose, which is for making indexes on SQL, we use Items, which is a Google thing that YouTube created between their Python code and MySQL... We grabbed all the SQL parsing, and stuff like that from there.

We use regular expressions from -- I forgot the name of the library... Yeah, I totally forgot the name of the library, but it's also open source... So we are open source, we use everything in open source, and for now we're analyzing also open source. So you know, open source everywhere.

**Adam Staravia:** I was just thinking about that now - any future plans for... Any sort of list you've got running right now for future blog posts of different analyses on different source codes? Or have you got any requests? Would you like requests?

**Francesc Cambó:** Yeah, absolutely.

**Adam Staravia:** What would you call it, "Request for analyzes"?

**Francesc Cambó:** \[40:05\] Request for analyses... Yeah, that's a good name. We did this analysis in Kubernetes, and as soon as we did it, there were some people saying "Oh, what about if you do it for the competitors of Kubernetes?" Cloud Foundry, stuff like that. People want to see how mature they are, and stuff like that. I think that the next analysis that I want to do - I want to do it in a different language. Kubernetes was mostly Go. I want to do it for TensorFlow, because it's also a huge community, and it's a different language - mostly Python, lots of C too, I think... So trying to figure that out, and probably in that analysis, when I'm going to open source that Six Degrees Off, and it's obvious they're going to be six degrees of "What's his name? I forgot..." One of the creators of Kubernetes... Jeff Dean, that's it. One of the big creators of everything machine learning related at Google, it's him behind it... So yeah, if you're a contributor to Kubernetes, how many degrees away are you from Jeff Dean? I think it could be an interesting thing to do.

**Adam Staravia:** Yeah.

**Francesc Cambó:** Also, if you have ideas on how to analyse this data from different \[unintelligible 00:41:16.12\] also I'm super-interested in that. So if you have follow-up questions, or projects that you would like to see analysed, let us know. We're going to be working on those, trying to get one per month at least, because we've seen a lot of perfect --

**Adam Staravia:** It's probably good for growth, adoption.

**Francesc Cambó:** Yeah, it's perfect for growth, perfect for adoption, and also perfect for us, because it's perfect to see whether every analysis that we want to do, whether it's doable or not. There were some things like... You know, silly example - \[unintelligible 00:41:47.25\] was not supported, so now we're going to be supporting it, too.

**Adam Staravia:** Right. You've become a user, too.

**Francesc Cambó:** Yeah, I am a user...

**Adam Staravia:** It's also a QA. You're Having your product, essentially, by doing this... A good exercise.

**Francesc Cambó:** Yeah... You know, developer relations, customer zero, all of those things; I still keep on doing those things...

**Adam Staravia:** It makes sense.

**Francesc Cambó:** Very, very useful. So if people have ideas, let me know.

**Adam Staravia:** One thing I love too, just to mention your website - I love when Community is in the main nav of open source-based companies...

**Francesc Cambó:** Oh, yeah.

**Adam Staravia:** ...because far too often it's like, "Where is the community? Who is the community? How is it represented and how can I talk to the contributors." Too many clicks are hard to find out "Who's involved in the team? How can I talk to somebody? What's my on-ramp? I've got questions, maybe it's a one-on-one I prefer..." and right here you have Community, and the second one down is Talk to Us... Very open and inviting.

**Francesc Cambó:** Yeah, we deeply care about community. There's some really active -- we have a very active Slack community, we have a bunch of different channels... Machine learning is one of them, super-active; people are there, talking about what they want us to build, and stuff like that. We also have language analysis; if you're a language analysis geek, we are doing a lot of really cool stuff. The number of conversations that I've had about Rust weird things, or even Lisp, or how to parse COBOL, and stuff like that... It is really cool. I'm a language nerd, I love different languages, and I'm having lots of fun because of that.

\[43:16\] If any of you aren't necessarily interested in what we're building with, which is this analysis engine, and you're interested just in some of the details, I think there's a lot that you can learn from that. The concept of universal abstract syntax tree is being used by other engineers who do things like security analysis of source code, things like this... So check it out, join us and let us know what you think, and if you're working on something, it's always good; we have our mailing list, bi-weekly mailing list, that was supposed to come out today, but there was no way I had the time to write it, or Victor, head of community... In that mailing list, at the end of the mailing list we always have a highlight on someone from the community that has done something cool.

**Adam Staravia:** Interesting.

**Francesc Cambó:** We really, really care about community. Join us, it's a good community.

**Adam Staravia:** And I'm sure that's probably the way you hire, too.

**Francesc Cambó:** Yeah, we've been hiring through that...

**Adam Staravia:** Or at least it's one way.

**Francesc Cambó:** By the way, we are hiring, so that's a good point... \[laughs\] Yeah, so we are trying to figure out -- we have engineers that have been hired through this. We have also people hired through they wrote about us, about like "Oh, I've discovered this", wrote a blog post, and now they're going to be joining us soon...

**Adam Staravia:** Interesting.

**Francesc Cambó:** So we're definitely hiring so many different people - machine learning experts, language analysis experts, people in product management, people in developer relations...

**Adam Staravia:** And the team is distributed, I assume...?

**Francesc Cambó:** The team is very distributed. The CEO is remote, just to give you an idea. The CEO is in Lisbon. We have people in Seattle, San Francisco, Madrid, London... Then some are in France, some are in Poland, some are in Russia, some are in Ukraine, some are in many places.

**Adam Staravia:** Nice. So the good thing is there's all these jobs you have opened... Worldwide.

**Francesc Cambó:** All of these jobs... Most of them, except -- there's a couple of them that are actually specifically for San Francisco, but all of them are completely distributed, so you can work from wherever you feel like.

**Adam Staravia:** Gotcha. Well, Frances, it's been a pleasure to meet with you, and...

**Francesc Cambó:** Thank you.

**Adam Staravia:** I've known you for years, but just never really had a chance to sit down and have a conversation with you; it's the first time, it's kind of a bummer, actually, but good at the same time.

**Francesc Cambó:** Let's just make it not the last time.

**Adam Staravia:** That's right, let's make it not the last time.

**Francesc Cambó:** Basically, you know, we're looking for feedback, we're looking for participation, so just go check out sourced.tech and then find the community and join us.

**Adam Staravia:** Cool.

**Francesc Cambó:** Thank you.

**Adam Staravia:** Alright man, thank you so much for your time. I appreciate it.
