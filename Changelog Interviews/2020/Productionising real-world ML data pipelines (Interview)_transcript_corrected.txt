**Jerold Santo:** Yaoundé, we're here to talk about Pedro, which is a Python library dealing with data pipelines. First, thanks so much for joining us on the show.

**Yaoundé Dada:** Thank you so much for having me.

**Jerold Santo:** And we should give a thanks to Wayland Walker, who requested this episode just recently, actually. Sometimes our requests take months and maybe even years for us to put the show together. This one was relatively recently. I should mention to our listeners that we do take requests at Changelog.com/request. If you have a topic, or a guest, or anything you'd like to hear on the show, just head over there and let it be known. We're happy to make shows that you all want to listen to.

We have Yaoundé here, who is the product manager at Quantum Black, and is on this Pedro project. Tell us about Quantum Black and what you all are up to.

**Yaoundé Dada:** Sure. Quantum Black is an advanced analytics company that was acquired by McKinsey a few years ago. We're in the consulting gig, and what we basically think of ourselves of is we're the Black Ops teams that go out to different companies around the world, and across many different industries, and what we do is effectively deliver functional machine learning code in production. So our success model looks at not only do we solve very difficult use cases, that have very challenging design problems, but we also have clients that are able to maintain their own codebases when we go. So that's what we do.

**Jerold Santo:** And Pedro is your first open source product, I read that's the case... Tell me about the experience, why is it open source, and all that stuff.

**Yaoundé Dada:** It's actually very interesting that you've asked that... Pedro, yes, is the first open source product that we've ever had coming out of McKinsey and Quantum Black. It was quite an experience open sourcing it, because it's very difficult to get corporate open source rolling, especially in a place where it hasn't happened before. We open sourced Pedro purely for client need. So what would happen effectively was that our data science teams would go out and use Pedro on their engagements wherever they were going for their consulting work... And they would obviously work with the client's data scientists and data engineers, and find that everyone really enjoys using Pedro.

\[03:56\] They'd suddenly have questions around "What do we do to keep on using the tool after we leave?" And the answer to us became "Let's actually open source this tool, so that our clients have access to it", and we'll be able to access upgrades, we'll be able to access an open source community so that they can help further engage with them as they use the tool. So that became the primary reason for us open sourcing.

We're very excited about open source in Quantum Black. We've just recently open sourced another tool called Causal. Causal is a causality data science library which helps somewhat tackle that problem between causality and correlation when you're busy assessing different datasets. We think of it as kind of like a way to really give back to the community, and really make a stake in some of the thought leadership pieces that we maintain at Quantum Black. We have a very exciting data science R&D function that is quite active with trying to solve issues around explainability, around fairness, around live model performance tracking... And really being able to share snippets of that knowledge I think is very exciting for us.

**Jerold Santo:** That is very exciting. I should mention that Wayland, when he requested the show, he did say that Pedro is changing the landscape of data pipelines in Python. I'm curious if you agree with that, and then secondly -- I mean, it seems like to me if it wasn't open source, that could not be the case; maybe it could be anyway... But I wanted your thoughts on the open sourcing of Pedro and how that has helped it to perhaps change this landscape, as he says.

**Yaoundé Dada:** I am so excited that Wayland finds that Pedro is changing the landscape for data science... Maybe I should actually describe what Pedro does.

**Jerold Santo:** Please do.

**Yaoundé Dada:** We think of Pedro as your way to apply software engineering best practice to your data science and data engineering code. It follows this whole principal that if we get everyone operating at a higher standard for software engineering best practice, we make code that is reproducible, it's deployable, it's versioned, and it makes it easier to put that code into production when it's time to go live on models.

It kind of fits into this whole problem space where for the longest time data scientists have not necessarily -- no, they've used code to solve the problem, as opposed to seeing code as the end goal, which is what is required for that code to be functional in the machine learning practice, and to have value for business. So Pedro essentially says "You have your standard way of working. We're just going to make some slight modifications to it, so that you have more robust code. In the end you get this production-ready code."

So I'm really excited that he says that we're changing the base of how data science should be done, because we believe in getting to the heart of users and really just having empathy for your workflow, and being able to enforce software engineering best practice is easy using Pedro.

Other exciting things that are happening because teams are using Pedro, from what we've seen from the open source community, is that people are following the trend of creating usable analytics code as well... Because there's a certain workflow consistency that happens when you have well-structured code, and they're now able to build their own reusable analytics libraries on top of Pedro, which has been quite exciting to see.

**Jerold Santo:** I was digging through Pedro docs as I was trying to figure out exactly what is this thing that I'm looking at, which is a fun endeavour for many open source projects... It's like, "Okay, I see what's written on the label... What exactly is going on here?" First, the documentation is perfect, which is indicative of the Python community; I'm not sure about the data science community, but you all are killing it there... And the Hello World is a very nice example of knowing exactly what Pedro starts you off with.

As I was reading it, it was more akin to me as a software developer as like a conventional framework; a thing that establishes norms, gives you buckets, very much kind of convention over configuration concept of "Here's where this goes, here's where you put your pipelines, put your data here etc. etc", and if we all follow these norms, life is better, life is smoother, it's more production-ready. Is that kind of the idea?

**Yaoundé Dada:** \[08:05\] That's actually completely the idea that it's based on. You'll note that -- I don't know if you're familiar with a tool called Cookie Cutter.

**Jerold Santo:** No.

**Yaoundé Dada:** Cookie Cutter follows this whole methodology - it's another open source project - that if we work in a standard way, so if we have the same setup in terms of directories and where we place certain files, it guarantees workflow consistency that makes it easier for you to work with yourself in the future if you have to look back at your code, and also easier for other people to work with you... Because in a sense, your code becomes self-documenting, because you were things are stored.

There's a derivative of Cookie Cutter called Cookie Cutter Data Science, and Pedro is actually built on top of Cookie Cutter Data Science, but takes into account how teams also need to construct data and ML pipelines, as well as also thinking about things like "How do we do data abstraction when trying to load data?", because there are many different ways of loading data using different Python libraries. And also things like "How do we do versioning of these datasets of models themselves so that we can actually reproduce runs?" Because the complexity of reproducing code - if you're building a software application and reproducing a previous version of the code, it might just be having a look at the logs to see what happened when a failure happened, and then having a look at the code that created that, and any other inputs that you have. In machine learning, that becomes a bit more complex because of the different variables that you would have had, that would have made that machine learning pipeline run, for instance... And Pedro kind of tries to -- I did say it's basically software engineering best practice, so it does try to implement those good sense principles in the data science world.

**Jerold Santo:** That's awesome, and definitely something that is needed in the data science world... As has been reported to me. I'm not living there, so I'm just going based on what you're saying and what people on Practical AI have also said - our other show - about machine learning.

Now, I'm coming from the other direction; I have a software background, and less of a machine learning background... And I'm not going to speak for our audience, but I'm sure there's plenty of them out there who are in a similar place as me. So when I look at Pedro, I see the conventions, I see the best practices in place, and I'm like "Yes, this makes total sense." But then I get to the other bits that I'm less familiar with, and I start to wonder "What are these things and how do they fit together for me to implement something in production and make it useful?" So when we start talking about data pipelines, nodes etc. can you explain some of the jargon perhaps and some of the things involved in starting a Pedro project, and maybe taking one into a production application?

**Yaoundé Dada:** Okay, so getting started with Pedro means after you've PIP-installed the library, simply running a CLI command for Pedro New will have you creating your project template. It's actually where you find the Hello World example is actually based, so you can get started in less than 30 seconds with your first Pedro project.

You can execute another command after you've created your project template, Pedro Run. You would have made your first Pedro pipeline run. So when I break down the components that are needed to actually understand Pedro, there are five. You'll understand that we have the project template, which is basically our series of files and folders that are generated by the Cookie Cutter Data Science template. It's kind of like best practice for "Where do I store bits and parts of my code?"

Although there are quite a few directories that will focus on even where you put your Jupyter Notebooks, to where you store your results, the two most important folders in that directory are where you put your configuration, which basically looks at - if you wanted in simply-explained terms - how do we remove hardcoded variables from our machine learning code? And there are two types you typically find - file paths and parameters. So how do we remove that from our machine learning code, so that it's more reproducible? So you'll put your configuration in a specific place.

\[12:02\] We also talk about our data catalogue, which is one of the library components of Pedro... Which is basically a series of extendable data connectors. If you extend our abstract dataset class, you can actually customize and create your own datasets for things that we don't typically support. But we support most file formats, so .csv all the way to Hadoop files, and \[unintelligible 00:12:22.29\] tables as well.

Then we talk about the Source folder being the next most important directory for you. In the Source folder you'll actually find the concept of nodes and the pipeline. Your nodes are just pure Python or PySpark functions that accept an input, and have an output. You use these nodes to actually construct a pipeline, because it's basically a series of nodes which have their inputs and outputs mapped to each other. So the pipeline can actually essentially work out where your dependencies are when you're building the pipeline, and that is the basis essentially of a Pedro pipeline.

Those are the primary concepts. There are obviously additional features built on top of all of these features, including the data catalogue allowing you to version your machine learning models, and your datasets. And there are all sorts of ways that you can extend Pedro however you feel.

**Jerold Santo:** Okay, I think I'm getting it. So you have your data catalogue, which is your input data, whether it be CSV, or JSON, or SQLite, right?

**Yaoundé Dada:** The data catalogue manages both loading and the saving of your data, so if you specify where the output should be saved, then Pedro will handle that, too.

**Jerold Santo:** Oh, okay. So it's on both ends. In the middle then you have your pipeline, which is stitching together these nodes, is that correct? The nodes are pure functions, so maybe it trains the model, maybe it does something else, predicts something... And then you have your pipeline, which is basically saying "Call function A, then B, then C, then D...", or whatever. Is there more to a pipeline than just like "Here's the order of operations?"

**Yaoundé Dada:** No, that's basically it. There are all sorts of things that you can do with the pipelines, there are additional features that you can do with it, but you've basically nailed down why Pedro is so easy to learn.

**Jerold Santo:** Okay.

**Yaoundé Dada:** It's basically specifying "Which function do I need? What is its input? What is its output?" and then "Let me put them all in this pipeline format." The pipeline syntax is very easy.

**Jerold Santo:** Very cool. So then the last bit was the output then. You said this goes back to the data catalogue, but what is the results of these pipelines producing? Is it on a case-by-case basis, based on what you're trying to gather from your model, or is it always the same kind of thing that comes out on the other end? What do our results look like?

**Yaoundé Dada:** It depends on what you're using Pedro for. An output could be a machine learning model, so even just a pickle file; what you would then use to test future predictions with... Or it could be maybe a table that you need to be loaded into some sort of database.

**Jerold Santo:** Okay.

**Yaoundé Dada:** So it depends on what you actually need the output to be, because that's what you would set up your pipeline to do.

**Jerold Santo:** I think I'm getting it now. So if we go back to the Hello World - because it's a simple one for us all to wrap our heads around - it's the Iris dataset, which is a well-known dataset of different pictures of flowers, these three different types of iris plants... And the goal is to classify. So you give it an image, and it says what kind of iris it is, or maybe you just give it some measurements of the petals... Talk us through the Hello World, we can use that as a reference point for conversation.

**Yaoundé Dada:** Cool. So the way that this pipeline is set up, it has four notes. One which will actually take in an Iris dataset, so the actual values, and it will split the data into training test samples, and also do some sort of data preprocessing as well to clean it up, so it's in a format that can be used.

\[16:05\] Then the next three nodes will train a model, then create the prediction model for you. And then how this pipeline ends - it ends slightly differently. This is why it always links back to what problem were you trying to solve, because it allows you to report accuracy... So you eventually in the last node can feed in a value, and then report accuracy on which -- based on which values, which iris flower are we looking at.

**Jerold Santo:** I see. So like you said, it's all based on what you're trying to accomplish. In this case, that's what it's trying to output, so... There you have it; the accuracy is important.

**Yaoundé Dada:** Yes. And that's why it will actually just tell you what the accuracy is at the end of the pipeline. So if you did a - like I mentioned, Pedro New, and then Pedro Run, once you've changed into the project directory, that's created for you; then it'll actually just tell you what the accuracy of this model is.

**Break:** \[17:05\]

**Jerold Santo:** So your first open source project at Quantum Black, and so far a success, perhaps changing the landscape of data pipelines - I like that line. And with any open source project, there's always big wins and there's often big fails, struggles along the way... You mentioned the reasoning behind it was your clients needed some sort of sustainability plan for these tools that you were working on for them or for their models to continue on after a contract was over... What have been some of the struggles or the things you had to consider as you took Pedro open source? Any insights you can share with the community?

**Yaoundé Dada:** One of the most surprising ones was actually our name. We were known by something else internally, and when we were like "Well, we want to go open source. We're going to go public" and everyone was on board, we kind of heard from legal that "Hey, we actually need to check out your name to check that it's not infringing on anyone's trademarks."

I think this is a bit unusual for open source projects where it's just like a personal project. You would never think that "I need to check my name for trademark infringement", and it needs to be kind of unique... Pedro is a bit of an abstract name for what the tool does, but we stuck by it and it works. But I've actually come to discover that a lot of corporate open source projects, including some friends at Uber, have spoken about doing the same thing... So I was like "Well, at least it's not unique to us that we have to undertake this."

\[20:05\] Another challenge that we had was really thinking about how do we support our users when they're using Pedro? Because our initial request for a public slug or a public Gitter was initially paused, and they told us we need to do some risk assessment on those platforms to work out for instance how do we enforce a code of conduct for users behaviour on the platforms as well, so that we have free and fair communications on them.

So we knew that beyond GitHub issues and Stack Overflow, both of those channels that we do watch, we needed to do something else. You actually see that we spent a lot of time on our documentation, so I'm really glad that you're enjoying our documentation... Because we knew that when we have users coming to Pedro, they want to get started very quickly, and if they run into issues, they need to be able to go to the docs and be able to troubleshoot their way through, at the very least. If they're not gonna talk to us on GitHub issues, which is sometimes a big thing for people to post questions there, or even Stack Overflow... But you'll be excited to know that we will be getting a public communication channel soon. So that's in the works for us to eventually release to users.

And then the third thing was that we didn't expect the community to pick up this quickly. That was something that we were not prepared for on the team. Pedro is maintained by nine people. So it's me as product manager, we've got Ivan Dance as the Pedro technical lead, and then an amazing group of software engineers, machine learning engineers, visual designers, and a front-end engineer who maintains the data pipeline visualization tool called Pedro-viz... And we were not ready for how many GitHub issues were created, pull requests were created, because people wanted to contribute code back to Pedro and make it better with us... And how many questions we'd get on Stack Overflow.

So that was a bit overwhelming, and I think we're still finding different strategies to manage it. One that we do on the team, because we're inevitably the ones that know the most about Pedro and how to fix different issues, is that we have a rotating role on the team called the Wizard; basically, we have a Wizard, and then the rest of the group are the warriors.

If you're the Wizard for the week, your job is to basically field all user queries, both in our internal channels, and our external channels as well, to try and make sure that users get quick and speedy responses to their questions, or to any issues or feature requests that they've raised.

So that was one of the strategies that have made things a bit better... But we are looking at ways to even scale support for our open source users in the future. So we're looking into new roles that McKinsey and Quantum Black have never hired before - because we've never open sourced anything - but developer advocates, or dev REL... I think it's sometimes called developer relations - to come onto the team and help us really scale out what that model will look like for us. So yeah, those are some of the unexpected -- three of the unexpected things that we didn't realize when we were open sourcing would happen.

**Jerold Santo:** Awesome. Very good. Let's go back to number one, let's go back to the name. What does it mean, Pedro?

**Yaoundé Dada:** It means "the centre" in Greek. We kind of look at Pedro as being the centre of your data pipeline, because of the way that it forms infrastructure/foundation of your analytics project, or ETL pipeline, or whatever you need to build. So Pedro means the centre.

**Jerold Santo:** The centre. And so after you came up with the name, that's when the -- was it a trademark search went out? I'm sure there were other searches as well; you searched on GitHub, and Twitter, and domains... Were these also things that you took into account before picking the name?

**Yaoundé Dada:** Yes. It was actually a lot more involved. Naming in Quantum Black has been quite exciting, because Pedro is one of three main products, and we'll be expanding the range of products that we have.

\[24:02\] So naming is always an issue in Labs, because \[unintelligible 00:24:04.26\] which does all the product engineering... And yeah, the naming exercise was a stakeholder management exercise, because we had to have happy branding, because that was helping with the product marketing and our global head of marketing, Katherine Shelton. But we also had to make sure that the team was also happy to represent the name as well.

So beyond having agreed consistency on a few names, they also had to go through the social media check, they also had to go through reference meaning checks, or even checks in other languages as well, because Quantum Black is a global organization. And then they had to go through the legal check, to check wherever there were trademarks for this name, in the many jurisdictions that McKinsey operates in, before we came to Pedro. So Pedro was marked as the least risky name.

**Jerold Santo:** What were some of the riskier names? Can you share them, or are they just on the cutting room floor, never to be mentioned again?

**Yaoundé Dada:** Some of the more interesting names were -- I think when there was no agreement on names. It consisted of names like Bara no, \[unintelligible 00:25:05.28\] which is a plumbing company... And the list of five names that included Pedro in the end, that went for final legal verification, included Braze, which kind of worked, because it referred to welding, or stitching together pieces, which is what the pipeline does. We had Knit tic as well, which is kind of also playing with that whole thing of knitting things together.

**Jerold Santo:** Knitting...

**Yaoundé Dada:** Yeah, Knit tic. You see, it doesn't work when you try and say it, so that was one of the reasons why this name failed. And then Spindle, because we're trying to reference that whole thing of many threads joining together,

**Jerold Santo:** I like Spindle.

**Yaoundé Dada:** Yeah. But all those names failed the little verification...

**Jerold Santo:** \[laughs\]

**Yaoundé Dada:** And we got Pedro in the end.

**Jerold Santo:** There's no worse feeling than when you come up with the perfect name, and then you go do all your due diligence, and somebody else is using it. You're like "No...!"

**Yaoundé Dada:** Yeah. The checks also included GitHub repositories as well, because we knew we'd have to survive in that sense... So it was really an adventure to find a name, and I'm really glad that we settled on Pedro. It was the one that fit

**Jerold Santo:** Some good things about the name Pedro... I think I even wrote this up at one point \[unintelligible 00:26:14.02\] the anatomy of a good name, and I'll say, two syllables - great; the fact that you can spell it easily after hearing the word - great. It's not ambiguous in that way... But it is intriguing, because when you hear it, you don't know what it means. There's no immediate attachment - at least in my mind; maybe to native Greek speakers there are... But to an American mind there's no immediate attachment to anything, so it kind of stands on its own.

**Yaoundé Dada:** That's true, that's true. Well, we never thought of it; thank you, I will give those reasons to the team.

**Jerold Santo:** \[laughs\] You've got the seal of approval... Let's move on to the point two that you've mentioned, the community side and the documentation, and how to figure out where the community meets, the code of conduct, all of these different things. I'm curious, because you seem to have checked all the boxes; we look at a lot of open source project, and I looked at Pedro and thought "Okay... Apache license. They've got a license, they've got a code of conduct, they have a documentation..." As I said, I've been impressed with the documentation... So it seems like there was at least knowledge of "We need to do this correctly" and then also "Here is our effort at correctly." So I'm curious, was there research gone into how to open source a project, or had people on the team done it before? How did you guys know what boxes to check and which things you really needed to address before you could open source it?

**Yaoundé Dada:** So the motivation for great documentation actually came from our technical lead. For a while he'd been passionate about the idea of creating an end-to-end tutorial... So you'll see chapter three in the documentation takes you through this amazing space flight tutorial. It takes about two hours to run through everything and get you acquainted, from beginner all the way to intermediate functionality in Pedro.

\[27:57\] I think it was Ivan's passion for users and them being able to learn and understand the tool, because Pedro documentation before that had literally just been kind of like the API docs, and the user guide, where we describe how the individual parts of the library - like the pipeline, the nodes and the catalogue - work. So really kudos to Ivan thinking and pioneering that we need to do better in terms of how we explain these things, and also using this as a solution for the fact that we can host a Slack channel when we open sourced.

But in terms of how we set up the code of conduct, and how did we think about best practice with how we set up a GitHub repository, I used to spend weekends going through kind of like people talking about how to do open source community management and what does best practice look like running a community. So it was important for me that code of conduct went in, so that we'd have a way to enforce if something were to go wrong on the repository. Luckily, nothing has... But we'd have a way to communicate with the users by referring them back to the code of conduct, one, and then two, also being able to take action to resolve things.

So yeah, it was just kind of like "How do we have an empathetic view to how someone will perceive a product, and how do they get on the best side of that, and try to put yourself in the users or the first viewers' shoes?"

On this note, additionally, I do know that open source does have diversity issues as well, so I'm really excited to eventually see hopefully PRs from women, or women-identifying people on Pedro.

So yeah, at all times we do also have a style guide for how we communicate with our users, as well. That was also something that we set up. So how do we say "Thank you for contributions", how do we respond to questions as well - and that is a team standard. Because we never want to create an environment where someone is offended and doesn't want to come back and interact with us on our different channels because of maybe a comment, or whatever the case might be. So those were things that we did look at.

**Jerold Santo:** Very cool. So I will say to your third point, which was you being a bit surprised by the level of success or people glomming on and using the project, I would say it probably has to do with the stuff we just talked about - the thoughtfulness and the TLC that you put in around open source, and doing things well. That being said, I'm curious if you had some sort of launch plan, or were there ways that you said "Okay, Pedro is out there. We want people to use this, we want people to try it", were there press releases, was there blog posts, or was this just a thing that grew organically after open sourcing it?

**Yaoundé Dada:** That is a fantastic question, and there was a huge release. It was McKinsey's first open source product, so everyone was very excited. The other thing that we realized in hindsight is that -- I'm really passionate about product marketing because you can kind of solve it as a... It's a user problem. It's "How do I make sure that you're getting the right information, so that I don't waste your time?" And you also learn what value something might have for you, because you consumed it in a short time and in a form that you needed it in.

So I kind of approach product marketing just like I approach product management, and it's "How do we optimize for the time that you have?" I was able to construct a massive marketing campaign with the Pedro team and with our head marketing and with McKinsey branding in order to actually deliver what was our massive open source release in June of last year.

So price releases went out, articles released towards data science, there was social media, there were some webinars done... And yeah, we just Wilde out a little bit on being able to (I think) basically make history for the firm, and release their first open source tool, in a place where McKinsey is recognized as having this amazing intellectual property that we never open source. So it was really just exciting for us, so that's why we went big on that launch.

**Jerold Santo:** \[32:00\] Do you think the success of Pedro will lead to McKinsey open sourcing more things, or this more of a one-off because of the client need?

**Yaoundé Dada:** Good question, and I can actually show you an example where that's not actually the case, because... It must have been now -- we're going on to two weeks ago, we released our second open source project, Causal, which is essentially a Python library that helps data scientists address the question of causality versus correlation in your datasets... And we released this one purely because it was an exercise of how do we showcase some of the R&D work that we have done on client projects, and eventually have made their way into more formal products, because we have been able to try and test those methods.

The really cool thing about Causal is that the research that it's built on was actually presented at Neurons; not at the last Neurons, but the Neurons before, and we had quite a few data scientists that were intrigued about this whole NO TEARS approach for assessing causality. This year we're finally releasing the library that we were able to build using that theory.

So yeah, we're still working out what does our open source strategy look like for the firm. There are still so many interesting questions about "How do we tackle it? What do we decide to open source? What is our process?" Finding out that, because I still think that there are places that we could optimize the process of it better... But this is an exciting place that we find ourselves in. We hope that it inspires many more people within the firm to consider open sourcing.

I think I do get emails with people asking like "How did you open source Pedro?" in hopes that they can do the same. So maybe it was just the first of many, I really do hope.

**Jerold Santo:** For those curious about Causal, I have scooped it up, and we'll include a link in our show notes, so you can click there and check it out.

**Break:** \[34:01\]

**Jerold Santo:** Switching gears a bit, let's talk about fun stuff. You are involved with something that looks very cool, the development of what you call Social Impact Virtual Reality Film, as a Sundance New Frontier Lab fellow. Tell me about that... It sounds intriguing.

**Yaoundé Dada:** It sounds like you've been digging around on the internet, which is cool... \[laughter\]

**Jerold Santo:** Maybe just a little bit...

**Yaoundé Dada:** \[laughs\] So I was a Sundance New Frontier Lab fellow along with a co-creator, one of my best friends, Sharif fa Ali. We've been best friends since like high school \[unintelligible 00:37:20.05\] in 2018. And the reason we were Sundance New Frontier Lab fellows was because we'd been working on - at that point it had been two years - a virtual reality film called Atom. So Atom is based on this Kenyan myth that if you walk around a sacred tree seven times, you change gender. So you go from male to female. And it's kind of like this interesting comment on gender fluidity ideals, which are kind of seen as African.

Obviously, it now tackles this whole thing of why is modern day Kenya so averse to gender fluidity ideals, and homosexuality as well... So there are a lot of issues that we can now dig up; obviously, you look at religion and colonialism as factors that would impact that.

Moving on from there, we were excited (also two weeks ago) to actually head to Sundance 2020 and actually premiere Atom. We've been iterating on the piece since then, and we were able to actually showcase the piece at Sundance. That was a really cool experience, and there's still more work to do, because that was essentially -- Atom is in its fourth iteration right now, and there still will be a fifth, which really focuses on how do we distribute the film to different partners in the U.S., Europe, and also back home for us; Sharif fa is from Kenya, from South Africa, so how do we do that in an accessible way.

**Jerold Santo:** So this was Sundance Film Festival 2020, it just happened a couple of weeks ago... So a fresh thing that just happened. I'm curious how you even film a virtual reality film. And you were talking about iterating - are you filming more things, or...? Tell me about the process.

**Yaoundé Dada:** Sure. The way that Atom is set up - it's built in Unity. It's also a dance piece, so we had access to two dancers who would essentially do motion capture to actually capture how they're moving. You can build an avatar from that and place it in any environment. In our case, we placed it two in the \[unintelligible 00:39:30.18\] which is the sacred tree, are typically placed. That's essentially how the environment was built.

There was also some thought around how do we do different user experiences as well, because we did optimize the piece for the Oculus Quest. We specifically waited for the Oculus Quest to come out, because we knew it was a higher resolution virtual reality headset... So higher than the Go, for instance, but still more accessible in terms of price than the Rift was, the Oculus Rift. So we specifically designed it for that.

\[40:05\] And we also were fascinated about the multiplayer experience, which we've had some moderate success with. I think the next iteration will fully nail down what the multi-user experience is supposed to look like. But that's essentially how you do it. So you can decide -- I think there are many different ways of filming virtual reality experiences. I think you have seen the 360 video documentary pieces which were still released... But a lot of pieces will focus on using motion capture to build avatars, and then eventually constructing environments around the different avatars that you'll have.

**Jerold Santo:** So in terms of presenting that at a film festival, is it just a room with a bunch of these Oculus Quests, and you go in and have -- because it seems like an individual experience, versus a shared experience.

**Yaoundé Dada:** That's a good question. How our piece was constructed is basically that. When we were presenting at the Sundance New Frontier space within this year's festival, we were in the biodigital theatre, which was a specific area set aside for what they call multi-user virtual reality experiences. In Atom we were able to get seven users in at the same time. Seven that could each put on your headset, each have your own set of controllers, and you can each affect the piece based on how you're interacting with it.

In the piece you are ancestors who are basically saying that this way of life is right, and you're following a character called ACICI as they make not a gender-based transformation around the tree, but what we call the journey to be the most honest version of themselves. So you help this character along the journey as they kind of like dance and struggle around the tree, in their journey.

It was important to us to have the multi-user experience. It was a design point for us, because the artistic intention for it is everyone understand what it's like to not be your true self, everywhere. Furthermore, it's just a human experience of sometimes being unsure of yourselves because someone's made a comment, or doubting yourself, or even hating parts of yourself. And you being able to support someone on that journey means we would love for you to be able to know that you can support other people in their lives on their pursuit to be the most honest versions of themselves... And you also recognize that you're not alone in that experience as well, because there are other people going through the same thing.

So that was why we opted for the multi-user experience. We still have some technical challenges with it... The system that we're using currently is quite expensive, which goes against one of our design principles of making this piece accessible. But we'll be looking at different ways to actually try and code it -- kind of like hack the Oculus Quest, if they don't help us in the end, to do the multi-user experience without having additional gear... Because that is really, really important for us in terms of distribution.

**Jerold Santo:** Wow. So how was it received?

**Yaoundé Dada:** Very well received. Sharif fa and I also made certain choices to whether or not we went explicit on the way that we describe some things, versus very abstract... And we kind of like strayed towards the still kind of like abstract-focused, but people got the intent. People understood why they were in the piece, why they were the ancestors, and why it was a multi-user experience.

They also understood how the piece was constructed in terms of ACICI's journey and understood everything that happened there... So we have received really fantastic feedback. We have obviously opened it up and told people that "Hey, we're still iterating on this piece, so any critical feedback that you have, do let us know, so that we can build it into the piece." So yeah, it's been very well received, and we're very happy. This has been a long-time project, but yeah, I'm really excited for 2020 and finally completing Atom and seeing the impact that it was supposed to create.

**Jerold Santo:** \[44:00\] Yeah, I was just going to ask if it seems that this is like a living project, or if it's just one that's still being formulated and will eventually come to its natural conclusion. It sounds like there will be a completion step, when you brush off your hands and say "We're finished."

**Yaoundé Dada:** I don't know, virtual reality experiences - at least the model that currently exists - means that... I guess because the tech is moving, but it's not really moving that fast, it means that they live longer lives than I think mainstream films or mainstream media would... Because your HTC Five, or your ancient Oculus Rift can still watch movies from today, for instance. So in terms of overall end of Atom, I'm not sure that there is, because we are considering different models of distributing the piece in museums, and even schools, as well as working with non-profits as well...

Because the intent of the piece obviously is the journey to be the most honest version of yourself, but we can bring someone to understand that it's actually about how do we deal with LGBTQ issues and accepting people that have different sexuality preferences. So really being able to use it with non-profits is also important for us, too.

So we hope that the piece lives on because the intent and the meaning behind why it was made still remains relevant. My ideal world, I think - not that I know Atom could achieve this; it would be wild if it could - would be that the piece actually wouldn't need to exist, because everyone was just comfortable in their skin and was accepted. But we have to do our part, that's why we hope the piece lives on.

**Jerold Santo:** Very cool, Yaoundé. How do people get in touch with you out there on the Internets? Where can people reach you?

**Yaoundé Dada:** On the internet, I'm quite active on Twitter, so you will find me tweeting away. I'm at @yetudada. I'm on Instagram as well, but I don't really use that one anymore. If you find me on LinkedIn - I know you, only then will I accept you, so Twitter is probably your best bet. \[laughter\] Twitter is probably your best bet. Yeah, that's the easiest place to reach me.

Otherwise, you'll find me on the Pedro GitHub repository, or on Stack Overflow, especially when I'm the Wizard, and I'm answering questions. So yeah, those would be the two channels to find me.

**Jerold Santo:** Very good. Well, thank you so much for joining us today. This has been a very interesting dive into Pedro, and also into Atom and the work you're doing at the Sundance Film Festival and beyond. Good luck to you on both endeavours. Any final words from you before we say goodbye?

**Yaoundé Dada:** Quantum Black Labs specifically, so the product engineering part of Quantum Black - we're hiring. We need help finding amazing people that can do software engineering. So from full stack engineering all the way to even just being Python-focused devs - we're looking for you. We're also looking for product designers as well. If you spike on UX, you will be loved; if you spike on the visual side, you will also be loved. And product managers as well.

We're really growing out the team. And as mentioned, specifically on Pedro we're looking for a developer advocate and dev relations people. And if you can do Python as well as being one of those people, then we love you more. So yeah, if you're interested, I think the best place is to head through to actually the McKinsey website, which would host our job offers... But otherwise you can just ping me on Twitter and send me your CV, and I put it straight through to the recruiters. It makes your life so much easier.

**Jerold Santo:** There you go. Hit her up on Twitter and get that ball rolling. Well, thanks, Yaoundé. This has been awesome. To everybody else, we'll talk to you next week.
