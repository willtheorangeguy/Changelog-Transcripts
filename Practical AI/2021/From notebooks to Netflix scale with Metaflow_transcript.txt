[0.00 --> 5.56]  we can potentially apply ML and AI to all aspects of the business. So I think like we are entering
[5.56 --> 11.42]  a world where like no area of life and business is totally kind of a safe from ML in a sense that
[11.42 --> 15.84]  like we can apply ML to all kinds of things. And now I don't mean like a crazy general AI,
[16.02 --> 19.00]  but I mean like a tiny little optimization problems here and there. And they are like
[19.00 --> 25.58]  really everywhere in all lines of business. Big thanks to our partners, Linode Fastly and
[25.58 --> 30.52]  LaunchDarkly. We love Linode. They keep it fast and simple. Check them out at linode.com slash
[30.52 --> 35.96]  changelog. Our bandwidth is provided by Fastly. Learn more at fastly.com and get your feature
[35.96 --> 41.54]  flags powered by LaunchDarkly. Get a demo at LaunchDarkly.com. This episode is brought to
[41.54 --> 45.36]  you by our friends at Rutterstack and we're calling all data engineers to check out Rutterstack
[45.36 --> 50.12]  Cloud and start building smart customer data pipelines. Rutterstack is warehouse first,
[50.32 --> 55.08]  no more silos. Rutterstack builds your customer data lake on your data warehouse, not theirs,
[55.08 --> 60.46]  enabling all functionality of a CDP with more security and retaining full ownership of your
[60.46 --> 66.44]  data. It's open source and API first. Rutterstack can be easily integrated into your existing
[66.44 --> 71.08]  development processes. And because they're open source, you can see all their code. So you don't
[71.08 --> 75.38]  have to worry about vendor lock-in or black boxes. And best of all, they have transparent pricing.
[75.58 --> 80.74]  Stop paying your CDP a premium to store your data. Rutterstack is free up to 500,000 events
[80.74 --> 85.62]  and pricing scales transparently from there. Learn more and get started at Rutterstack.com.
[85.90 --> 91.88]  Again, Rutterstack.com. That's R-U-D-D-E-R-S-T-A-C-K.com.
[101.70 --> 106.70]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[106.70 --> 112.02]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[112.18 --> 116.72]  and data science happen. Join the community and Slack with us around various topics of the show
[116.72 --> 121.26]  at change.com slash community and follow us on Twitter. We're at Practical AI FM.
[127.14 --> 133.76]  Well, welcome to another episode of Practical AI. This is Daniel Whitenack. I am a data scientist
[133.76 --> 140.38]  with SIL International. And I'm usually joined by my co-host, Chris Benson, who is a tech strategist
[140.38 --> 147.10]  at Lockheed Martin, but he's got the week off. But I do have a wonderful guest for today's discussion,
[147.10 --> 155.76]  which I think is very timely and also very practical. Vila Toulos is with us, who is CEO at Outer Bounds
[155.76 --> 163.18]  and was previously leading the data science infrastructure group at Netflix. He's also
[163.18 --> 170.46]  the author of a really interesting and new book called Effective Data Science Infrastructure,
[170.64 --> 177.08]  How to Make Data Scientists More Productive. Well, that sounds super practical, Vila. Welcome to the
[177.08 --> 181.22]  show. Great to have you here. Yeah, thanks for having me. Well, I know even before the show,
[181.22 --> 187.98]  we were talking about your background and how your sort of background has shaped how you think about
[187.98 --> 194.84]  data science infrastructure, but also how you think about like AI and what really is new, what isn't
[194.84 --> 200.42]  new, what trends have happened and developed over time. So could you just give us a little bit of an
[200.42 --> 206.58]  idea about your background and how you started in this field? Yeah, well, I wonder like how far back I
[206.58 --> 212.48]  should go. But embarrassingly enough, I started at my first startup that worked on artificial neural
[212.48 --> 216.96]  networks already back in 2000. So I mean, that's kind of a long time ago. And believe it or not,
[217.02 --> 221.68]  I mean, this of course, like predates all deep learning and so forth. But people did artificial
[221.68 --> 225.84]  neural networks at the time. And this startup in particular, it was focusing on a very peculiar
[225.84 --> 230.98]  kind of neural networks called self-organizing maps that were quite popular, like in late 1990s,
[230.98 --> 236.20]  early 2000s. And the commercial idea we had at the time is that we could help enterprises with kind
[236.20 --> 240.40]  of a search, like enterprise search, the internet search, stuff like that. So it happened that,
[240.62 --> 243.72]  yes, I mean, companies needed help with that, but I mean, they didn't need neural networks.
[244.28 --> 248.64]  But interestingly enough, ever since then, I've been really like focusing on this question that
[248.64 --> 252.50]  how can we actually like improve the tooling and the infrastructure for people who built these
[252.50 --> 257.22]  models? Since already like back in the day, I saw that like a big challenge that we had is that
[257.22 --> 262.28]  like we had all these amazing researchers, data scientists, whose task was to kind of build these
[262.28 --> 265.92]  models that were supposedly useful in practice. And it took many iterations,
[265.92 --> 271.06]  it took a lot of thinking and like trying out experimenting. And like, of course, like back
[271.06 --> 275.84]  then, I mean, the kind of the tooling was really quite horrible. And now it's much better. But I
[275.84 --> 279.70]  think it's really interesting kind of to see the kind of the whole like trajectory, like where we
[279.70 --> 283.64]  came from and like where we'll be going in the future. And yeah, I mean, it's kind of scary to see
[283.64 --> 287.80]  that like also there are like many things that like haven't actually changed that much. And like
[287.80 --> 289.82]  kind of we have much work ahead of us.
[290.08 --> 294.94]  Yeah, maybe could you share some of those examples? Like what is the same now?
[294.94 --> 301.90]  Maybe a challenge that you're still facing now that was the same as back in those days,
[301.90 --> 306.92]  and maybe something or a couple examples of things that have really dramatically changed?
[307.32 --> 312.12]  Yeah, well, I mean, starting with some things that are the same, amazingly enough, like already back
[312.12 --> 317.00]  in the day, like we were using Python. And of course, that was highly controversial at the time. So I
[317.00 --> 320.48]  mean, Java was pretty new. And like, of course, like actually, like everything that needed to be high
[320.48 --> 325.24]  performance was written in C and C++. So that's actually like a big change, like between then and
[325.24 --> 329.56]  now that of course, like we had to build all the libraries by ourselves. And it was even seen
[329.56 --> 334.20]  as a big kind of like a differentiator and a competitive mode that like we had a more
[334.20 --> 339.38]  performant, more scalable algorithms to optimize these models than anyone else. Nowadays, of course,
[339.38 --> 344.04]  everybody can just use off the shelf, PyTorch, TensorFlow, even like XGBoost,
[344.24 --> 349.24]  scikit-learn just released 1.0. So the library ecosystem, I mean, like it's way ahead,
[349.24 --> 354.64]  like what it used to be. Now, another like a big difference is that we actually spent considerable
[354.64 --> 359.44]  amount of time just setting up the hardware. Amazingly enough, like we had a rack of servers,
[359.44 --> 364.14]  like kind of at the company and like we had to set up the networking and the storage and like the
[364.14 --> 367.78]  compute and the operating systems and all that stuff. And now with the cloud, I mean, again,
[367.78 --> 372.14]  I mean, that's another thing that like has massively changed that like you can get this infrastructure
[372.14 --> 375.98]  that like used to be available only for the largest companies, even at the startup. And like you can
[375.98 --> 381.06]  get like clusters of machines with GPUs and it's just like mind blowing. And now what's really
[381.06 --> 384.74]  exciting today is that on the one hand, like you have this like high level modeling libraries,
[384.74 --> 389.66]  on the other hand, like you have all the hardware available. And now I think that like kind of still,
[389.76 --> 393.78]  it's kind of mind boggling that still, I mean, things aren't that easy. It kind of feels that
[393.78 --> 397.74]  everything is possible, but I mean, nothing is really easy enough. And I think that that is still
[397.74 --> 400.96]  kind of something that like we need to work on. And of course, like one interesting challenge is also
[400.96 --> 404.54]  that there are way more people working on these problems. It used to be only a handful of people.
[404.54 --> 408.38]  I think we had three people at the company at the time who could actually like build these models.
[408.58 --> 411.98]  And now, I mean, it's like probably a hundred, if not a thousand times more people. So definitely
[411.98 --> 419.68]  feels like a new field in that sense. Yeah. And how did your perception of data science and the
[419.68 --> 425.92]  infrastructure in particular needed for data science, how did that shift as then you led the
[425.92 --> 433.28]  team at Netflix? And I mean, now we're talking of course about a much bigger scale, right? But also
[433.28 --> 440.20]  like, yeah, these models are, I assume even at that point, a really critical piece of what makes
[440.20 --> 445.88]  Netflix, Netflix and the value that's added by these models. So how did your perception of
[445.88 --> 448.64]  infrastructure change as you worked on those sorts of problems?
[448.96 --> 453.60]  I think like one interesting thing that maybe not everybody realizes is that like the few things
[453.60 --> 457.58]  that like many people know about Netflix, especially the recommendation and personalization systems,
[457.58 --> 462.18]  they are kind of the tip of the iceberg. And there are like so many other things like where Netflix
[462.18 --> 467.10]  wants to apply potentially ML and related technologies. And like also like wants to
[467.10 --> 470.74]  experiment with new ideas. I think that like one thing that's really interesting is just the kind
[470.74 --> 474.82]  of the diversity of different use cases. If you think about computer vision, natural language
[474.82 --> 479.30]  processing, even things that are not technically machine learning, like operations research,
[479.30 --> 483.06]  how we can optimize schedule, stuff like that. So it's just the fact that like,
[483.06 --> 487.12]  there are like so many different types of problems and then they come in all shapes and sizes. It's
[487.12 --> 491.64]  not always about scale. Also, I mean, it's not always that everything has to be like a super
[491.64 --> 496.02]  kind of a high SLA business critical. I mean, they're like experiments, like a crazy experiments,
[496.50 --> 500.58]  but the interesting challenge is really that like, how do you manage like kind of like the diversity of
[500.58 --> 504.66]  all these things? So that's really interesting. Now, when it comes to the more technical side of
[504.66 --> 509.08]  things, Netflix, like for the longest time has been a hundred percent on AWS,
[509.08 --> 514.86]  like it's a cloud first company and Netflix has been trailblazing like many architectural patterns,
[514.86 --> 519.32]  like when it comes to storing data in the cloud way before like other companies were doing it.
[519.50 --> 524.52]  Also microservices, chaos engineering. So it was really fascinating to be at this company that had
[524.52 --> 528.88]  on the engineering side, like kind of some of the world's leading cloud infrastructure.
[529.30 --> 533.24]  I think honestly, I mean, what makes Netflix interesting is that it all like runs on AWS in
[533.24 --> 536.40]  contrast to let's say Google and Facebook who have their own infrastructure, which is really
[536.40 --> 539.84]  kind of an island and nobody else can do it. But I mean, Netflix is in that sense,
[539.90 --> 544.08]  like a closer to everybody else in the world that like, it is the same AWS at the end of the day
[544.08 --> 547.76]  that Netflix uses that everybody else can use as well. And it's just that like, kind of that they
[547.76 --> 552.56]  have all these like practices and ways of thinking about things and like ways of about building services
[552.56 --> 557.02]  that like makes them really effective. And now when you layer something like a data science and
[557.02 --> 559.78]  machine learning on top of it, I mean, it's really interesting. And of course, I mean,
[559.80 --> 563.70]  that is kind of all those like learnings are reflected in Metaflow, which is the open source library
[563.70 --> 570.40]  that we started building there. Yeah, I do want to get into Metaflow. But before I do, maybe what is
[570.40 --> 576.92]  your perception of how, like maybe back in those days when there was sort of like a building hype
[576.92 --> 582.26]  around data science, a lot of people initially getting into it, companies experimenting, what is
[582.26 --> 589.58]  your perception of like from then to now, how has like the average data scientist ability to work
[589.58 --> 595.44]  with these different pieces of infrastructure that maybe come across their path, like the various
[595.44 --> 602.50]  services in AWS, whether it be EC2 or, you know, object storage or things even all the way up to like
[602.50 --> 608.22]  Kubernetes and EKS and that sort of stuff? How has like the average data scientist from your
[608.22 --> 615.20]  perspective, what they're required to know, or maybe what they come in with knowledge of how has that
[615.20 --> 620.26]  shifted over time? Well, my kind of initial reaction is that I still think that like we are
[620.26 --> 625.16]  in the early days. Yes. I mean, of course, I mean, the fact is that like maybe five, 10 years back,
[625.18 --> 629.88]  if you wanted to do anything in this field, you basically had to know C++ and like you had to
[629.88 --> 635.04]  know the depth of knowledge about, let's say, the CPU read systems was much deeper. And even let's say
[635.04 --> 639.70]  the kind of recommendation systems at Netflix, they run on Spark and like many people use Scala. And
[639.70 --> 644.28]  that's a bit of a different persona, a bit of a different profile than like what we see now
[644.28 --> 650.04]  amongst data scientists who are building this, like a new set of very diverse models, like using
[650.04 --> 656.22]  these Python-based libraries, maybe directly using the cloud and so forth. At the same time, I do think
[656.22 --> 660.34]  that all these things, and especially like being able to leverage the cloud is still harder than it
[660.34 --> 664.98]  really should be. Just thinking about the kind of the amazing amount of like computational power that
[664.98 --> 668.12]  you have there. And like, it's still, I mean, there are like most companies I talk with,
[668.12 --> 671.74]  there's the feeling that like, well, data scientists kind of need to know about Docker
[671.74 --> 675.92]  files, and maybe they need to know about the CICD systems. And I think that there are like
[675.92 --> 680.10]  different points of view. I mean, like if that's actually a feature or a bug, I think that there
[680.10 --> 685.18]  are like so many questions related to the modeling itself that like, at the end of the day, all of us,
[685.18 --> 690.00]  like all human beings, like you kind of need to manage your cognitive bandwidth. And as interesting
[690.00 --> 695.06]  as it might be to kind of for everybody to know about CICD systems, I do think that it kind of takes
[695.06 --> 699.22]  a bit away from the bandwidth that like you should have available for like thinking about the modeling
[699.22 --> 703.48]  problem itself. So I do think that and I do hope that like we managed to kind of raise that like a
[703.48 --> 709.82]  level of abstraction even more. Yeah, I guess in this case, abstraction could be a good thing. And
[709.82 --> 715.14]  even though it is interesting to dive into these different systems and containerization and all that,
[715.52 --> 721.26]  it does take a lot of time. Like you said, yeah, I remember there's like a tweet from Eric
[721.26 --> 726.68]  Bernardson, who said like having a data scientist sort of learn about some of these things like
[726.68 --> 733.16]  Kubernetes and Docker and Terraform and these things is kind of like having like web app developers
[733.16 --> 739.62]  learn about the Linux kernel. It's just like so far apart. It's very tough to expect that. Yeah. At the
[739.62 --> 746.64]  same time, like I have benefited from those times where I've been able to maybe push something
[746.64 --> 753.02]  further on my own, at least into like a prototyping stage within a company and get it in front of
[753.02 --> 760.22]  people to see that value without sort of like reliance on, you know, passing something off to a
[760.22 --> 765.52]  data engineering or a software engineering organization to even create a prototype.
[766.30 --> 770.24]  So maybe there is some like tooling that's improving around that. Like I know there's things like
[770.24 --> 774.28]  Streamlit and other things where you can create something that's very compelling,
[774.28 --> 780.74]  very quickly in terms of like a prototype. But I don't know. One of the things Chris and I discussed
[780.74 --> 788.56]  on the podcast a little while back was maybe why many data projects fail in certain cases is because
[788.56 --> 795.10]  people aren't able to push a project far enough into a prototype stage for people to see like the
[795.10 --> 800.92]  value of something and actually get buy-in from the organization. From your perspective, I know like
[800.92 --> 806.92]  also being the CEO of a company that is trying to help people with their ML infrastructure,
[807.82 --> 813.34]  where do you often see like when you first maybe engage with clients or when you're maybe just making
[813.34 --> 819.76]  an observation about the industry, where do you see the problems in like people not being able to get
[819.76 --> 825.52]  value out of machine learning and AI? Where do things get blocked most often from your perspective?
[825.86 --> 829.50]  I think it's definitely, it's a combination of maybe three different factors. Well, I mean,
[829.50 --> 834.18]  like maybe starting from the kind of the easiest one is technical, that there are technical hurdles
[834.18 --> 837.84]  still. I mean, like it's just like putting the infrastructure together, like it's just building
[837.84 --> 842.64]  the models. Although like technically all the ingredients are there, like many companies are
[842.64 --> 847.54]  still like struggling, like kind of putting the pieces of the puzzle together. But I do think that
[847.54 --> 852.22]  that is in a way, I mean, like the easiest one of the three. So then the second one is definitely
[852.22 --> 856.86]  the kind of the skill set of the people involved. And it's not only that they wouldn't be skilled.
[856.86 --> 860.22]  I mean, I don't think that that's oftentimes the problem, but also like kind of what other things
[860.22 --> 864.66]  they should be focusing on. And especially like when we start talking about actually producing
[864.66 --> 868.64]  business value using machine learning, like really understanding the problem domain, like
[868.64 --> 872.98]  understanding the business needs. I mean, that takes a lot of bandwidth and like still much of the
[872.98 --> 877.18]  time, like these practitioners, they spend on like kind of either like engineering problems or
[877.18 --> 881.46]  like maybe modeling problems that may be fun, but I mean, ultimately might not really kind of
[881.46 --> 886.02]  affect the company's bottom line so much. But then the last problem, I think, and it's the big one,
[886.02 --> 890.66]  it's really the organizational. It's kind of like a leadership question that kind of what you
[890.66 --> 895.06]  mentioned before is that, okay, so why do many of these projects fail? Well, I mean, they don't get
[895.06 --> 899.24]  like a close enough to production. I think that that is absolutely a key. And I think that that was
[899.24 --> 903.34]  one thing that Netflix did really, really well that they have, even at the highest level of the
[903.34 --> 908.98]  organization, they have this experimentation culture and they have this idea and understanding
[908.98 --> 914.86]  that like, well, now first we can potentially apply ML and AI to all aspects of the business.
[915.00 --> 920.58]  So I think like we are entering a world where like no area of life and business is totally kind of a
[920.58 --> 925.14]  safe, like from ML in a sense that like we can apply ML to all kinds of things. And now I don't mean
[925.14 --> 929.64]  like a crazy general AI, but I mean like a tiny little optimization problems here and there,
[929.68 --> 933.80]  and they are like really everywhere in all lines of business. But now the problem is that like you may
[933.80 --> 937.68]  have thousand ideas that, okay, we could do this and that, but how do you know which one of those work?
[937.68 --> 942.32]  And like nobody really knows in advance and like you can't really ask anyone. And the only way to
[942.32 --> 946.64]  know is that like you really need to kind of start experimenting and like not only experimenting in
[946.64 --> 950.72]  a sense that like you hack something, a prototype in a notebook, but oftentimes really the only way
[950.72 --> 955.42]  to know is that you basically push these things to production. And now the production meaning not so
[955.42 --> 959.58]  that like you have a huge team working on something for in six months, but actually like kind of getting
[959.58 --> 964.18]  something to A, B test, let's say. I mean, like if you have, and honestly, I know that like this is
[964.18 --> 967.44]  really like not that easy, but I mean the idea that like you can test this,
[967.68 --> 973.44]  ideas. You can test different like prototypes and pipelines in production alongside like whatever
[973.44 --> 977.36]  system you have in place today. And then you compare the results that it's hugely, hugely
[977.36 --> 981.92]  powerful. And then like have the understanding that like you can interpret the results and decide
[981.92 --> 986.00]  what to do with that. And like have the understanding that like, actually it is by design that like most
[986.00 --> 989.92]  of these things fail. I mean, that's kind of the whole point of experimentation. If you knew that
[989.92 --> 993.60]  everything is going to succeed, I mean, you wouldn't have to experiment, but the idea is that like you can
[993.60 --> 998.08]  afford making so many of these like a tiny experiments that then you can quickly decide
[998.08 --> 1002.32]  that, okay, this doesn't seem worth it. And like, maybe then like you like redirect resources to
[1002.32 --> 1006.24]  something else. But I mean, this is also like a question of product management oftentimes,
[1006.24 --> 1010.00]  having like product managers who really understand how to work with these ML systems.
[1010.00 --> 1026.00]  I mean, all these like organizational muscles are like missing at that many, many companies.
[1026.00 --> 1037.04]  So, you know, signal wire is real time video tech to help you create interactive video experiences
[1037.04 --> 1043.52]  previously not possible. It gives you access to broadcast quality ultra low latency video that's
[1043.52 --> 1050.64]  proven and trusted by Amazon ring doorbell zoom and others. See why the future of video communication
[1050.64 --> 1056.80]  is being built on signal wire. They have easy to deploy APIs, SDKs for the most popular programming
[1056.80 --> 1063.36]  languages and expert support from the OGs of software defined telecom tech. Try it today at
[1063.36 --> 1072.40]  signalwire.com and use code AI for $25 in developer credit. Just visit signalwire.com. That's signalwire.com
[1072.40 --> 1078.96]  and use code AI to receive that 25 bucks. Once again, that's signalwire.com code AI.
[1080.64 --> 1096.80]  So, Bile, you started to mention as we were talking about trends that you're seeing in
[1096.80 --> 1103.52]  infrastructure and ideas around where things get stuck in production. You mentioned Metaflow a couple
[1103.52 --> 1110.48]  times, which I know is a big piece of the puzzle in terms of how you solve these problems, but also a
[1110.48 --> 1115.36]  big part of your career in terms of what you've developed. So could you give us a little bit of
[1115.36 --> 1119.36]  the backstory of Metaflow, sort of the origin story, I guess?
[1119.36 --> 1124.40]  Yeah, I guess like the nice thing is that it's actually like a quite pragmatic, quite bottoms up
[1124.40 --> 1130.96]  in a manner that as I mentioned, Netflix, when I joined Netflix back in 2017, this was before SageMaker,
[1130.96 --> 1135.92]  this was before MLflow, this was before Qflow. This idea of having any kind of, let's say,
[1135.92 --> 1139.20]  especially open source machine learning infrastructure was quite new. I mean, of course,
[1139.20 --> 1143.12]  there were products around like you had data robot, you had Domino Data Labs, obviously,
[1143.12 --> 1147.52]  like you had Databricks and Spark and so forth. But I mean, like the idea that what does the full
[1147.52 --> 1153.52]  stack for ML look like? I mean, that was quite new. So now when I joined Netflix back in the day,
[1153.52 --> 1158.72]  I saw that, okay, so obviously, like the company had like all these like basic foundational pieces of
[1158.72 --> 1164.48]  infrastructure in place. So they had a large data warehouse and S3 based data lake. They had a team
[1164.48 --> 1169.04]  managing a large scale compute infrastructure, basically something like Kubernetes. They had
[1169.04 --> 1173.04]  also teams who had been thinking about workflow orchestration for a long time. So you had all
[1173.04 --> 1176.96]  these pieces. So again, I mean, like technically everything's impossible. So it didn't seem like
[1176.96 --> 1180.80]  the challenge was that, okay, we need to invent some new pieces of tech that like we could do something
[1180.80 --> 1184.88]  that nobody else has done before. That didn't seem to be the problem. But then the problem was really
[1184.88 --> 1188.80]  that they had the organization of data scientists there, like who constantly complained that like,
[1188.80 --> 1193.36]  well, getting anything done was too hard because exactly for the reasons we discussed that like,
[1193.36 --> 1197.12]  okay, how do I run compute? I mean, you go to the compute team, they say that, oh, I mean,
[1197.12 --> 1201.76]  you just have a Docker container and like you put the container here, image here and tag here. And then
[1201.76 --> 1205.52]  like maybe you better go through the CI CD system. And then it already at that point in time,
[1205.52 --> 1210.72]  you had like lost the data scientists. Like, does this make any sense? And the workflow systems,
[1210.72 --> 1214.72]  of course, needed like lots and lots of YAML to kind of define what you want to do.
[1215.44 --> 1218.56]  Even like kind of thinking like, what are the kind of the patterns? Because remember,
[1218.56 --> 1222.48]  like these people are not software engineers by training. So the kind of how you actually architect
[1222.48 --> 1227.76]  software like this was hard. Really the origin story and the idea for Metaflow was that, okay,
[1227.76 --> 1231.04]  assuming that like you have this like a foundational infrastructure available,
[1231.04 --> 1235.84]  like how can you kind of stitch them together in a manner that would present an API to data scientists
[1235.84 --> 1240.64]  that like would kind of like help them to build these applications that they have been asked to build
[1240.64 --> 1245.60]  for the company. And now the other interesting side of the coin was that Netflix has this culture
[1245.60 --> 1250.24]  of freedom and responsibility, which meant that like we didn't want to take away all the freedom
[1250.24 --> 1254.48]  from people saying that like, well, I mean, like there's like a training API and like you can only
[1254.48 --> 1260.00]  call this one API to train your model. It was well known that like different people preferred different
[1260.00 --> 1264.88]  tools for the job. I mean, some people preferred TensorFlow, some people prefer XGBoost. I mean,
[1264.88 --> 1269.20]  depends on the application, of course. So the idea was that, okay, we should allow them to kind of at the
[1269.20 --> 1274.16]  high level, like kind of exercise that freedom and exercise that domain knowledge and expertise in like
[1274.16 --> 1278.40]  choosing those like modeling tools. So like we kind of started having this idea that, okay, we need to be
[1278.40 --> 1282.72]  quite opinionated about the lower layers of the stack. How do you do compute? How do you access data? How do you
[1282.72 --> 1287.44]  do orchestration? And then like leave a lot of space at the top of the stack that, okay, so what kind of
[1287.44 --> 1291.68]  modeling libraries you use and how do you do your feature engineering? And like, maybe even like what are the
[1291.68 --> 1296.08]  KPIs that matter for you when it comes to monitoring models in production? And then like we
[1296.08 --> 1300.56]  started like crafting that stack. And again, I mean, like Netflix, there's no top down like anything. I
[1300.56 --> 1304.80]  mean, there's no CTO, no VP of engineering saying that like everybody must use this thing, but we
[1304.80 --> 1309.52]  started like solving these very practical problems and then kind of like in a very organic manner. I
[1309.52 --> 1313.20]  mean, Metaflow started spreading inside the organization because people thought that, oh, I mean,
[1313.20 --> 1317.36]  this is like a quite like a no-nonsense tool that like helped them to solve exactly the types of problems
[1317.36 --> 1320.24]  that like they had been facing on a day-to-day basis.
[1320.24 --> 1325.60]  Yeah. So there's a whole variety of things that people have created around workflows,
[1325.60 --> 1331.92]  but then there's also a whole set of platforms and projects out there related to like
[1332.48 --> 1339.20]  ML Ops and other things. There's like all sorts of things that maybe data scientists care about from
[1340.24 --> 1346.24]  making sure that they can run their workflow, not on their laptop, which is more maybe infrastructure
[1346.24 --> 1353.60]  compute related all the way to like, hey, how do I version and control experiments? How do I access data?
[1353.60 --> 1359.60]  So how far does Metaflow reach in terms of these different things that data scientists might want
[1359.60 --> 1365.68]  to do? Like what pieces of the puzzle does it try to solve and how can data scientists think about it
[1365.68 --> 1369.20]  in terms of those various buckets of things they're trying to do?
[1369.20 --> 1373.92]  Yeah, that's a good question. I think like because we were faced with this great diversity of different
[1373.92 --> 1378.80]  applications, we couldn't think, let's say, I mean, at my previous company before Netflix, I mean, we were
[1378.80 --> 1382.80]  doing a real-time bidding and like for targeted advertising. And then like in a context like that,
[1382.80 --> 1387.28]  you know exactly the application and you know that, okay, maybe we build a feature store,
[1387.28 --> 1391.12]  like maybe these are exactly the workflows everybody follows. And that's like one type
[1391.12 --> 1394.80]  of a challenge. It actually like might be a great engineering challenge, but I mean, different type of
[1394.80 --> 1398.48]  challenge. In our case with Metaflow, the challenge was that like, we didn't know exactly
[1398.48 --> 1402.16]  the type of machine learning applications people wanted to build. So we started thinking
[1402.16 --> 1406.88]  very much like from the bottom up that like what are commonalities across all applications and
[1406.88 --> 1410.88]  and like really it starts with that. Okay. So I mean, really the question of data and like
[1410.88 --> 1415.92]  now the discipline ways of accessing data. Okay. So how do we do it quickly enough? Let's say you have
[1415.92 --> 1420.08]  some kind of a data warehouse, you have a database, how do you get the data out quickly so you don't have
[1420.08 --> 1425.12]  to wait for 40 minutes for your SQL to execute. So that's one thing that like we were thinking about,
[1425.12 --> 1430.00]  like working with Arrow, like Metaflow comes with the custom S3 library. So you can get your data
[1430.00 --> 1434.64]  super fast, like from S3, small things like that. Then like on the compute, like again,
[1434.64 --> 1438.80]  I mean, like all these models, I mean, not even the ones that like require huge amounts of data
[1438.80 --> 1443.28]  requires a lot of compute. So you may want to do hyper parameter search. So maybe you have a model
[1443.28 --> 1447.84]  ensemble, like maybe you want to build a separate model for every country or maybe for every customer.
[1447.84 --> 1452.16]  So you need to be able to fan out this compute to the cloud. So definitely wanted to solve that part
[1452.16 --> 1457.28]  as well. And we saw that oftentimes it's really, really sensible idea to structure these applications
[1457.28 --> 1461.44]  as a workflow. So, I mean, there's a lot of confusion about these DAGs and workflows these
[1461.44 --> 1465.20]  days that, okay, what does it even mean? And like, there's so many different workflow systems, but
[1465.20 --> 1469.04]  purely as a way to kind of express these ideas, the idea that you structure things as a DAG.
[1469.04 --> 1473.92]  I mean, it makes a lot of sense. So we kind of took that as a kind of a core way of implementing
[1473.92 --> 1478.08]  things. But then like, we definitely wanted to separate the idea that once you deploy these
[1478.08 --> 1482.08]  workflows to production, like running workflows that scaling production is actually an engineering
[1482.08 --> 1485.92]  challenge of its own. And we didn't want to claim that like, well, I mean, Metaflow is the
[1485.92 --> 1490.48]  most like production grade scalable workflow scheduler in the world. So we integrated with
[1490.48 --> 1495.52]  other systems out there and also to ease that path due to production. So that was really another
[1495.52 --> 1499.76]  thing that like what we discussed earlier about how important it is to kind of attest these ideas
[1499.76 --> 1504.16]  as close to production as possible. We knew that, okay, we need to provide a path like all the way to
[1504.16 --> 1508.32]  the end. And that's why we integrated with the existing system. So we wouldn't get the resistance
[1508.32 --> 1512.16]  from engineering teams saying that, oh, you have this piece of Python code, but I mean, no way we are
[1512.16 --> 1516.56]  going to run this in production. So kind of really like thinking about the production best practices,
[1516.56 --> 1520.80]  starting like with very mundane questions like dependency management. Like what if you need
[1520.80 --> 1524.80]  like a very specific version of TensorFlow? Again, I mean, we don't want you to kind of write Docker
[1524.80 --> 1528.96]  files by hand. It's surprisingly hard to do it in a reproducible manner. But I mean, like, how do you
[1528.96 --> 1533.04]  let you use the exact version of the library you need? And then like, yeah, I mean, you mentioned
[1533.04 --> 1536.48]  versioning as well. I mean, like, of course, like there's the idea that, well, you should maybe version
[1536.48 --> 1540.56]  your code, maybe like using Git, but I mean, like, how do you version your models? How do you version
[1540.56 --> 1545.04]  your experiment? How do you version your data even? We felt that like these are such kind of
[1545.04 --> 1549.92]  foundational concerns that like we should also provide an out of the box solution for them.
[1549.92 --> 1554.08]  I think that that's definitely kind of like helps because then the data scientists don't have to
[1554.08 --> 1558.40]  think about it too much. That's kind of like what we have been like doing this far. So if you think
[1558.40 --> 1563.92]  about like compute data orchestration, versioning, and like kind of all kinds of questions related to
[1563.92 --> 1567.36]  pushing things to production, then there are like things at the top of the stack that like
[1567.36 --> 1572.32]  we haven't been so opinionated about. So I mean, many of our users today, they use other model
[1572.32 --> 1577.44]  monitoring tools. They are amazing model monitoring tools. You mentioned Streamlit, Weights and Biases,
[1577.44 --> 1582.56]  many others out there, of course, like specific tools for model explainability, if that's important
[1582.56 --> 1587.04]  to you. And then like, of course, like a feature engineering, like that's a complex topic of its own.
[1587.04 --> 1591.84]  Like there are some customers who use Metaflow with some feature stores that works. And of course,
[1591.84 --> 1595.12]  I mean, like the modeling libraries is something that like you should absolutely use the kind of
[1595.12 --> 1600.40]  the best of the breed tools off the shelves. Yeah. So it sounds like part of the philosophy
[1600.40 --> 1606.40]  here is people are going to be opinionated in their own teams about like, oh, we use Weights and Biases
[1606.40 --> 1611.92]  to do this bits of the monitoring and experiment management, but that's not going to solve these
[1611.92 --> 1618.08]  sort of scale and infrastructure problems and the like workflow running problems that you mentioned
[1618.08 --> 1625.84]  as well. So being able to pull in what you need, I think is really a cool idea. And having that sort
[1625.84 --> 1633.52]  of modular nature of it is really great. So I do want to get into like the actual workflow with Metaflow,
[1633.52 --> 1637.28]  but in terms of how it works under the hood, like let's say that you're setting up
[1637.84 --> 1646.48]  a flow and you've got a series of steps that processing steps, eventually something has to run on a
[1646.48 --> 1651.20]  server, right? And maybe certain, like you're saying, maybe I'm running TensorFlow over here and
[1651.20 --> 1657.44]  it needs a GPU, or maybe I'm doing this like pre-processing of images and I just need to crank
[1657.44 --> 1666.72]  through a bunch of stuff in a sort of batch or maybe even parallel way on CPUs. How do things in code that
[1666.72 --> 1672.96]  is using Metaflow, how do those things eventually end up running on the servers? Is there some sort of
[1672.96 --> 1678.16]  containerization or something going on under the hood or how have you built that abstraction layer?
[1678.16 --> 1681.84]  Good question. Well, I mean, now Metaflow, like since the day one, I mean, it has been built with
[1681.84 --> 1686.88]  this cloud first mindset. I think that like kind of when it comes to things like compute and storage,
[1686.88 --> 1691.84]  I think like we live in a bit of a, like a post scarcity world that it's actually like interesting
[1691.84 --> 1696.24]  when you think about it, that like many of the systems that we even use today, like databases,
[1696.24 --> 1700.96]  even things like Spark and Hadoop, they were built with this idea that you have a constraint resources
[1700.96 --> 1704.96]  and like the really the engineering challenge is that, okay, how do you allow people to kind of
[1704.96 --> 1709.92]  a run compute given that like you have only like a 200 servers or something like that,
[1709.92 --> 1714.24]  and you have to do the resource management very carefully. Then the mindset that like we adapt to
[1714.24 --> 1718.08]  Metaflow, which I think it's really, really useful, especially in the people's productivity point
[1718.08 --> 1723.44]  of view is that you work with the cloud. The cloud provides you at least this like a kind of
[1723.44 --> 1728.88]  abstraction of having like basically infinite scalability. So you can use some cloud-based platform.
[1728.88 --> 1734.96]  Again, I mean, like we rely on like existing systems like Kubernetes, like AWS batch, like what have you.
[1734.96 --> 1739.04]  Do you kind of a farm out the containers to the cloud? You can specify the resources you need.
[1739.04 --> 1743.68]  If your function needs GPUs, you can say that I need GPUs in this case. And in other cases,
[1743.68 --> 1747.36]  maybe you need a lot of memory. And I think that like the interesting challenge with machine learning,
[1747.36 --> 1751.04]  I think that this also like a sets machine learning apart, like from like many previous data
[1751.04 --> 1756.16]  intensive applications is that the needs are so different that like in some types of models are really
[1756.16 --> 1761.44]  IO sensitive. Like maybe you need to read like tons of images, tons of videos, but the model itself may
[1761.44 --> 1766.08]  be simple. In other cases, it might be something super compute intensive, but not IO sensitive. In some
[1766.08 --> 1771.04]  cases, you absolutely GPU or maybe even like some custom crazy hardware. In other cases, it is cost
[1771.04 --> 1775.68]  prohibitive to do that. And it's very hard to have any kind of like a uniform one size fits all. So I
[1775.68 --> 1780.64]  think like having that like scalability that goes in all the different dimensions, like vertical,
[1780.64 --> 1784.96]  horizontal, you name it. So that's super useful and cloud makes that possible. So we rely on these
[1784.96 --> 1789.44]  systems and we take care of like then packaging the code, sending it to the cloud, executing on
[1789.44 --> 1794.32]  the container, handling retries, all that, like kind of a basic, basic plumbing there. And then,
[1794.32 --> 1797.84]  yeah, I mean, the same thing, like with the orchestration, I mean, like the DAG execution at
[1797.84 --> 1802.48]  scale, if you have a hundred thousand DAGs running in parallel, I mean, it's a thing of its own. And like,
[1802.48 --> 1807.20]  there are some systems that do it well. We integrate with AWS step functions. Now we are integrating with
[1807.20 --> 1811.68]  Argo, maybe one day with Airflow. I mean, like what have you. And the idea is that you should be able
[1811.68 --> 1815.44]  to test these things locally. So Metaflow always comes with the local mode. So you can kind of test
[1815.44 --> 1819.76]  and iterate the same way you do in a notebook, but then like kind of when you want scale, like when
[1819.76 --> 1823.36]  you want to kind of something that's like production ready, you can use your existing production
[1823.36 --> 1829.44]  infrastructures. So you were just getting into talking about, hey, you know, maybe you're doing
[1829.44 --> 1836.24]  some experimentation locally in a notebook, and then like eventually you kind of go beyond that and scale
[1836.24 --> 1842.72]  up and all of that. I guess, first off to set the stage, Metaflow is an open source project and people
[1842.72 --> 1848.08]  can go ahead and try it out. And we'll include links in our show notes to where people can find it and
[1848.08 --> 1854.56]  try it out. But let's say I am a data scientist. I understand what we've been talking about so far that,
[1854.56 --> 1862.24]  hey, I'm going to experiment locally, but then eventually I need to run all of this sort of workflow and
[1862.24 --> 1870.64]  series of processing steps on infrastructure that is in the cloud. Could you maybe just walk through like,
[1870.64 --> 1877.28]  what does it look like for a practitioner to use Metaflow? Let's say they've written some Python code, they're
[1877.28 --> 1884.88]  used to working with notebooks, maybe they're sometimes used to writing Python scripts that they run on, maybe
[1884.88 --> 1892.16]  they log into a server and they run it. What does it look like for them to install and integrate
[1892.16 --> 1898.24]  Metaflow into their workflow? What are the prerequisites and how does the integration happen?
[1898.24 --> 1902.08]  Let me start with the kind of a data scientist point of view before getting into deployment and
[1902.08 --> 1907.12]  stuff. So I can give you a timely example that just yesterday I was actually creating an example
[1907.12 --> 1912.08]  like for the book using Keras. And like this was a new data set. I was actually like using the NYC
[1912.08 --> 1917.28]  taxi data set. Like for the example, it's a fun data set publicly available. Everybody probably in this
[1917.28 --> 1921.36]  situation, I actually started exploring the data in a notebook. Of course, notebooks are still great for
[1921.36 --> 1926.40]  like visualizing, like exploring data and so forth. And even like when I started like a drafting the
[1926.40 --> 1930.64]  kind of the model architecture in Keras, I mean, it's really quite nice to be able to iterate that
[1930.64 --> 1935.36]  in a notebook quickly. I was like very conscious about, I wanted to kind of introspect that. Okay.
[1935.36 --> 1938.64]  So, I mean, what are the things that work well in notebooks? What are things that work well on the
[1938.64 --> 1943.44]  Metaflow side? And like, I kind of faced the same problem that like many other people face,
[1943.44 --> 1947.20]  like when using notebooks is that like after maybe three hours of prototyping,
[1947.20 --> 1951.68]  my notebook had this like kind of a mixture of cells that I had been executing out of order.
[1951.68 --> 1953.44]  And like, who knows what the state is?
[1953.44 --> 1958.32]  Yeah, exactly. It was super convenient. It was like, I kind of felt that I'm in this like a garage
[1958.32 --> 1962.32]  hacking something together and like everything is like kind of on the table and it's kind of a messy
[1962.32 --> 1966.88]  setup. At that moment, I mean, it made me super productive, but I mean, it was absolutely 100%
[1966.88 --> 1970.88]  obvious that like there was nothing in that notebook that I would dare to run in production.
[1970.88 --> 1974.32]  I mean, like even the idea that I would somehow like run that because it was the kind of a,
[1974.32 --> 1978.16]  my experimentation process that was reflected in that notebook, I would like to kind of think
[1978.16 --> 1982.96]  about like production a bit differently. So, so then the kind of the idea, like what happened
[1982.96 --> 1987.60]  at Netflix as well. And like what we recommend people doing is that by all means use notebooks
[1987.60 --> 1992.40]  for experimentation, for exploration, like for building prototypes. But then at one point,
[1992.40 --> 1995.68]  like when you kind of have like a rough idea, like what that workflow could look like,
[1995.68 --> 1999.92]  and then really the threshold for that shouldn't be too high. You can almost start copy pasting,
[1999.92 --> 2003.36]  like kind of the snippets, let's say in this case, I mean, just the kind of a 15 lines of code
[2003.36 --> 2008.00]  that defined the kind of the cross architecture, like kind of in a step in a file. And now if you
[2008.00 --> 2012.48]  use something like a visual studio code, actually it's really easy to have like both the kind of the
[2012.48 --> 2017.76]  IDE as well as the notebook side by side. So I can use notebooks for exploration. And then like,
[2017.76 --> 2022.80]  I can still have that like really quote unquote proper IDE, like for writing Python code. And again,
[2022.80 --> 2027.12]  the idea with Metaflow, what we have had since the very beginning is that like, it doesn't require
[2027.12 --> 2031.12]  that you know anything more than like what you would need to know in a notebook. So there are like
[2031.12 --> 2035.36]  no new concepts, no new paradigms. You don't have to change the code, the same libraries and all that
[2035.36 --> 2040.16]  stuff. So I was able to then like kind of take the best parts of like my experimentation and like kind
[2040.16 --> 2044.40]  of put them to this workflow. And now like, thanks to Metaflow, I'm able to kind of start running it
[2044.40 --> 2048.56]  at scale. So, I mean, of course in the notebook, it was rather small dataset that I was testing with.
[2048.56 --> 2052.80]  And now I could take the kind of the same concepts, the same code, then like start testing that with
[2052.80 --> 2057.60]  larger scale. I mean, like I didn't have to wait for my tiny workstation to kind of crunch all the data,
[2057.60 --> 2061.92]  but I could like farm it to the cloud. So overall, I mean, that is quite nice pattern. Like you kind
[2061.92 --> 2065.36]  of get the best of the both worlds. I mean, you can use notebooks where they really shine.
[2065.36 --> 2069.20]  And then in the end, like in the end, an artifact that like you really dare to run in production.
[2069.20 --> 2072.56]  Now, I guess the other side of your question was that, okay, so the deployment. So yeah,
[2072.56 --> 2076.08]  I mean, like indeed, I mean, the easiest way to get started is that you run pip install Metaflow on
[2076.08 --> 2081.60]  your laptop. It works out of the box. There's nothing else that needs to be done. We have also had this
[2081.60 --> 2085.52]  belief that the kind of the needs of an organization, like a grow over time,
[2085.52 --> 2090.72]  you don't necessarily like have to kind of have the most battle hard and most scalable set up on
[2090.72 --> 2095.12]  the day one, but you can start with something simple. And like probably one of the simplest
[2095.12 --> 2099.92]  thing is that like you can sign up to AWS batch and like there are like three configuration things
[2099.92 --> 2103.84]  that you have to set. Or like if you don't want to do it by hand, I mean, there's the Terraform
[2103.84 --> 2108.64]  CloudFormation template. You go to the UI, you click a button and it sets up the kind of the stack for you.
[2108.64 --> 2113.92]  And then you can like start like running compute at scale. And that's really great. So if you have more than
[2113.92 --> 2117.92]  one person working on these things, you probably want to have this centralized metadata tracking so
[2117.92 --> 2122.24]  people can share their results. That's quite convenient. It comes as a part of the CloudFormation,
[2122.24 --> 2126.96]  not too hard. And then like there's the orchestration system. Again, I mean, part of the stack, depending
[2126.96 --> 2131.12]  like how you want to do it, I mean, like you have freedom there to set up in a few different ways.
[2131.12 --> 2134.96]  And then like, of course, like the larger the organization, now the largest organizations there,
[2134.96 --> 2139.92]  they might care about like setting up the data governance rules, like life cycle policies,
[2139.92 --> 2143.92]  thinking about that. Oh, I mean, like how do we like harden the kind of the service deployment?
[2143.92 --> 2148.40]  So it's highly available stuff like that. But I think like realistically, these infrastructure stacks
[2148.40 --> 2152.32]  like you need to start small and they need to be able to grow like with the organization.
[2152.32 --> 2157.04]  I think like many systems have the problem that either they are super easy, but then they don't scale.
[2157.04 --> 2162.08]  I mean, like as your company grows. So I mean, you kind of outgrow them at some point or then they are
[2162.08 --> 2167.28]  like way too enterprise and like you have to scratch your head about the Kubernetes deployments and whatnot before
[2167.28 --> 2172.00]  you can get like even the simplest thing done. So yeah. And I'm looking through your documentation,
[2172.00 --> 2178.80]  which is great, but it seems like there's a sort of concept in Metaflow where, like you said,
[2178.80 --> 2184.88]  in a lot of these workflow management systems, you're writing like YAML, maybe you're writing JSON,
[2184.88 --> 2190.64]  you're writing config files and Docker files to sort of manage these various steps, which is definitely
[2190.64 --> 2195.92]  doable if you want to get into that. But in terms of an approach that you're taking is this sort of
[2195.92 --> 2203.76]  decorator pattern in Python where like you're defining maybe a class that's your data flow
[2203.76 --> 2210.00]  and some steps within that class that are decorated with a Metaflow decorator of step.
[2210.00 --> 2216.64]  And then you're connecting those different steps within your actual Python code to create your workflow,
[2216.64 --> 2221.04]  which is then maybe farmed out to some infrastructure. Did I get some of that right?
[2221.04 --> 2225.44]  Yeah. And like, the interesting thing is that, I mean, there are like so many kind of systems that
[2225.44 --> 2230.08]  look like that. And I always say that like the devil is in the details and many systems, like,
[2230.08 --> 2234.16]  let's say, I mean, like there are tons of systems that let you specify workflows in YAML. And like,
[2234.16 --> 2238.64]  oftentimes they say that, oh, I mean, like you can run any Docker container and like you can run any code
[2238.64 --> 2243.52]  inside the Docker container that makes a step, which kind of like as a user, like, well, I mean,
[2243.52 --> 2246.88]  it kind of like a push is the hardest problem, like to you that, okay, wait a minute. So I mean,
[2246.88 --> 2250.72]  like how do I define what code runs in this container and like, where do I push my container?
[2250.72 --> 2254.96]  And like, what are the dependencies I need inside the container and how do I move data like between
[2254.96 --> 2259.20]  these containers? So in a way, I mean, just like having a workflow, I mean, that's kind of the easy
[2259.20 --> 2263.68]  part. That's like why I wanted to have this, like a self-contained thing in Metaflow that you have
[2263.68 --> 2268.08]  everything in one place. So you define the code, you define the dependencies, you define the resources,
[2268.08 --> 2272.40]  you define the workflow, because then you kind of get the unit that you can actually like run the full
[2272.40 --> 2276.72]  thing in production and it does something useful. And by the way, I mean, like one thing that I definitely,
[2276.72 --> 2280.16]  I want to mention, which is really important is that this is never a waterfall. I mean,
[2280.16 --> 2285.04]  it's never so that you prototype and then you deploy and then you declare mission accomplished.
[2285.04 --> 2289.92]  But I mean, if the project is successful at all, I mean, what inevitably happens is that either
[2289.92 --> 2294.32]  something fails in production, in which case you have to go back and start debugging or like
[2294.32 --> 2298.16]  the business stakeholder, whoever comes to you saying that, okay, now we want better results.
[2298.16 --> 2302.48]  Can we improve accuracy? Can we add this new dataset, whatnot? So you kind of have to start
[2302.48 --> 2306.32]  iterating again. And that's really the challenge, like with many systems that like,
[2306.32 --> 2309.92]  even if you are able to do that one deployment, how do you come back from production? Everybody
[2309.92 --> 2314.08]  always talks about going to production, but how do you come back from production and then like
[2314.08 --> 2318.56]  keep iterating and like maybe start having multiple versions running in parallel. So it's all these
[2318.56 --> 2322.48]  like a small things that like really matter a lot. Like when you think about like running ML,
[2322.48 --> 2328.40]  like for real. Yeah, definitely. I totally agree with that. So we talked about how you might set up your
[2328.40 --> 2334.56]  workflow in Metaflow. You know, you can pip install Metaflow locally, connect it to AWS,
[2334.56 --> 2339.84]  cloud resources, cloud resources, in terms of that step from like, let's say, because you talked about
[2339.84 --> 2346.72]  being in the notebook and then kind of moving into this Metaflow workflow. But then eventually,
[2346.72 --> 2352.08]  like, let's say that I create a pipeline that I really like, and I know that I need to run it,
[2352.08 --> 2360.96]  like triggered when this happens, or I need to run it like every Friday to, you know, do this or that.
[2360.96 --> 2366.00]  What does that look like? Because I assume like you could run your Python code locally with these
[2366.00 --> 2372.72]  Metaflow decorators that gets sort of farmed out to resources in the cloud and tracked in various ways.
[2372.72 --> 2379.20]  But what does it look like to go from that to some sort of automation or something that's running kind
[2379.20 --> 2383.76]  of hands off and you're not running, you know, Python, whatever locally?
[2383.76 --> 2388.64]  Yeah. I can paint you a picture that I saw at Netflix that worked really well. Now I know that like,
[2388.64 --> 2392.80]  not many companies are yet at this stage. I do hope that like kind of the world will advance over
[2392.80 --> 2397.20]  the next three years or so. But I do think like what's really, really useful is that you have
[2397.76 --> 2402.32]  some kind of a centralized workflow scheduler. I know that like many organizations are struggling
[2402.32 --> 2406.40]  with this question that like, should they have like many different infrastructure stacks and like
[2406.40 --> 2411.36]  kind of different departments have their own and ML has its own and data engineers have their own.
[2411.36 --> 2416.00]  But the fact is that like ML is not an island. And especially if you want to use these things in
[2416.00 --> 2420.16]  production, I mean, like producing like real business value, you have to integrate with
[2420.16 --> 2424.88]  whatever is the outside reality out there. So there's a lot of value in having kind of a
[2424.88 --> 2429.84]  decentralized system. And like what the centralized system needs to do is only to take care of like
[2429.84 --> 2434.64]  this seemingly simple task, which is that like you have workflows and like this system needs to kind
[2434.64 --> 2439.20]  of keep the workflows running, farming out and the compute due to kind of whatever like is your compute
[2439.20 --> 2445.84]  backend. I mean, Kubernetes or AWS patch or whatever. And now the beauty of this setup is that oftentimes this
[2446.00 --> 2451.44]  data science workflows run in tight conjunction with data engineering workflows. So you have ETL and
[2451.44 --> 2456.24]  like you can imagine that like you have maybe daily ETL that like take some raw data, take some like
[2456.24 --> 2461.68]  whatever streaming event data and like kind of a moshasis that new tables. And whenever that table
[2461.68 --> 2466.48]  updates, then like maybe you want to update your models. And then in the best case, like there is
[2466.48 --> 2471.44]  the triggering mechanism that automatically, whenever the data updates, then like triggers the ML update as
[2471.44 --> 2475.52]  well. And there's maybe some piece of information like carried around, like saying that, okay,
[2475.52 --> 2479.92]  these are the new partitions available, or this is the latest hour or like however you want to do this.
[2480.40 --> 2484.88]  And then like, if you have this like a centralized scheduler, if you have this triggering mechanism in
[2484.88 --> 2490.32]  place, you can start constructing this almost like a web of workflows that like comprises both of the data
[2490.32 --> 2495.28]  engineering side of the house ETL. And even now, if you want to use something like a DBT or a great
[2495.28 --> 2500.96]  expectations, you can kind of tie that really nicely upstream. So you have like a really nice ETL, like
[2500.96 --> 2505.20]  always data quality is there. And then like you have something like, let's say the ML workflows
[2505.20 --> 2509.28]  managed by Metaflow. And then like oftentimes, even like what happened at Netflix is that there's kind
[2509.28 --> 2514.40]  of the ETL after that it might be that, let's say you do produce some batch predictions and now you kind
[2514.40 --> 2519.92]  of have to load those batch predictions to another place. Or let's say in some cases, like some decision
[2519.92 --> 2524.24]  support systems, even like wanting to have those predictions in Tableau or Airtable or something.
[2524.24 --> 2527.68]  So you have another piece that then takes those results and pushes them to something else.
[2527.68 --> 2531.44]  And now of course, like as the complexity grows, then like you want to layer like
[2531.44 --> 2536.64]  observability tools on top of this alerting tools that, okay, what if something is late? I mean,
[2536.64 --> 2540.16]  like how can you trace like what's going on? And of course, I mean, there's like a lot of
[2540.16 --> 2544.32]  additional infrastructure that you need there. And now if I'm looking at this like workflow
[2544.32 --> 2549.28]  orchestration landscape in the kind of the world overall, I mean, I think we are not quite yet there,
[2549.28 --> 2553.76]  like in many companies, many companies have maybe multiple air flows that are not connected.
[2553.76 --> 2558.08]  Many companies still use this like cron based scheduling that like, it's always like runs at
[2558.08 --> 2562.96]  3am, no matter what it like runs at the same time, which is kind of silly. Also the observability
[2562.96 --> 2567.52]  parts are missing. But I think that that vision is really great. I think it really helps a lot in
[2567.52 --> 2572.08]  like kind of a tying the ML, like really close to the rest of the organization. So it's not like
[2572.08 --> 2574.88]  an island, like in some world garden somewhere. So.
[2574.88 --> 2581.84]  Yeah, well, I appreciate that very much. I know that we've covered a lot of different topics today.
[2581.84 --> 2587.20]  I do want to mention again, your book, which is effective data science infrastructure,
[2587.20 --> 2591.84]  how to make data scientists more productive, we'll include a link in our show notes to that
[2591.84 --> 2597.12]  because this is something our listeners, I think we'll really get into because it is so practical.
[2597.12 --> 2601.28]  I'm just looking at the flow of your book right now, which goes all the way from sort of
[2601.28 --> 2607.84]  notebooks to workflows to Metaflow to production and scaling up, which I think is a super practical
[2607.84 --> 2612.96]  book. So thank you for your work on that. Our listeners, you'll definitely want to check it out
[2612.96 --> 2621.28]  because we do have a 40% off discount code for the book from Manning. You can use pod practical AI 19,
[2621.84 --> 2629.04]  the code pod practical AI 19 for 40% off of the book, which is pretty cool. Well, maybe to end,
[2629.04 --> 2634.56]  we usually like to ask our guests some future looking question. And I think you've already
[2634.56 --> 2640.64]  started to go there in terms of where you would love to see infrastructure go, but maybe in terms
[2640.64 --> 2645.76]  of data scientists and the infrastructure that they're working with, what is what you're hoping
[2645.76 --> 2652.08]  to see maybe in a couple of years in terms of data scientists workflow? How do you see that abstraction
[2652.08 --> 2658.72]  layer advancing and changing over that time period? Yeah, I think that there's the work to be done at all
[2658.72 --> 2662.88]  layers of the stack. Again, I mean, as mentioned a few times, like during this episode, I mean,
[2662.88 --> 2667.36]  like I'm excited about the fact that like we have so much compute available. So I think like we can
[2667.36 --> 2672.24]  make that even easier. That's exciting. Definitely a lot of work to be done on the orchestration side,
[2672.24 --> 2677.36]  like tying together ETL, ML. I mean, there's just like a lot of work to be done there. Overall,
[2677.36 --> 2682.32]  I think like at the higher levels, I think that of course, the fact is that like many companies,
[2682.32 --> 2685.92]  and if not most companies out there are still like struggling with the questions that like,
[2685.92 --> 2691.28]  how do they use ML to power their business, not only like produce demos. And I think that that goes
[2691.28 --> 2696.00]  back to that, like even like organizational, like a mindset change, like with the experimentation
[2696.00 --> 2700.96]  culture and like, how do you divide work between engineers and data scientists, data engineers? So
[2700.96 --> 2706.72]  I'm super curious to see how that evolves. And like, I'm already now when I'm talking to companies,
[2706.72 --> 2711.60]  I mean, I'm always fascinated by all kinds of ideas and like all kinds of like kind of a business
[2711.60 --> 2715.12]  opportunities that like people are coming up with. And like some ideas, of course,
[2715.12 --> 2718.96]  like don't end up working so well, but I mean, there are like some like amazingly like promising
[2718.96 --> 2723.36]  ideas out there. And I'm sure that like kind of these will only grow tenfold, hundredfold
[2723.36 --> 2727.28]  over the next three years. So I think it's like pretty much inevitable. And like the kind of a
[2727.28 --> 2731.44]  parallel that I always draw is that it's like kind of due to e-commerce and like the web. I mean,
[2731.44 --> 2736.00]  like back in 2000, like even setting up an e-commerce store, like it took a lot of engineering work.
[2736.00 --> 2740.80]  Today, you just like sign up to Shopify or like kind of you go to Squarespace and like you don't
[2740.80 --> 2744.00]  have to write a line of code and you can get something that works amazingly well. And I think
[2744.00 --> 2747.76]  it's inevitable that like we will enter like with machine learning infrastructure as well,
[2747.76 --> 2752.80]  but maybe it will take another five to ten years. Yeah. Well, I definitely look forward to that time.
[2752.80 --> 2757.84]  That'll be a good time. But thank you so much for joining us, Ville. It's been really wonderful to
[2757.84 --> 2763.60]  chat about your projects and your thoughts on data science infrastructure. I look forward to seeing how
[2763.60 --> 2766.72]  Metaflow grows and what you do in the coming years. Thank you so much.
[2766.72 --> 2767.52]  Thanks, Daniel.
[2767.52 --> 2777.92]  Thank you for listening to Practical AI. We have a bundle of awesome podcasts for you at changelog.com,
[2777.92 --> 2784.00]  including our brand new show, Ship It with Gerhard Lezou, a podcast about getting your best ideas into
[2784.00 --> 2789.68]  the world and seeing what happens. It's about the code, the ops, the infra, and the people that make it
[2789.68 --> 2794.00]  happen. Yes, we focus on the people because everything else is an implementation detail.
[2794.00 --> 2799.52]  Subscribe now at changelog.com slash ship it or simply search for ship it in your favorite podcast
[2799.52 --> 2804.32]  app. You'll find it. Of course, the galaxy brain move is to subscribe to our master feed. It's all
[2804.32 --> 2811.28]  changelog podcasts, including Practical AI and Ship It in one place. Search changelog master feed or head
[2811.28 --> 2817.20]  to changelog.com slash master and subscribe today. Practical AI is hosted by Daniel Whitenack and Chris
[2817.20 --> 2821.44]  Benson with music by Breakmaster Cylinder. We're brought to you by Fastly, LaunchDarkly,
[2821.44 --> 2824.32]  and Linode. That's all for now. We'll talk to you again next week.
[2847.20 --> 2853.44]  Game on.
[2853.44 --> 2853.52]  Game on.
