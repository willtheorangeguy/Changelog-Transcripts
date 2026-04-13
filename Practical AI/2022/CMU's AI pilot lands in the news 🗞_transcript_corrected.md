[0.00 → 9.26] I will say kind of obliquely in the military space, we're doing autonomous stuff as is reported in the general news all the time in terms of aircraft.
[9.26 → 11.36] And I think that's fairly well understood.
[12.00 → 28.84] In the civilian space, though, if you imagine in the future being on an autonomous airliner, they say that this model can safely avoid collisions, predict the intent of other aircraft, track those aircraft and coordinate with those aircraft's actions, communicate over the radio.
[28.84 → 31.58] It uses natural language processing to do that.
[31.68 → 34.30] It has a vision system that uses six cameras.
[34.88 → 37.44] So it's a pretty cool problem to solve.
[37.68 → 46.86] I know people shudder when I say this, but I think that it is not so far out that all of us will be getting on airliners that are almost entirely automated.
[47.30 → 51.70] And so this is one of those big steps toward trying to do that.
[58.84 → 69.66] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive and accessible to everyone.
[70.02 → 70.82] Subscribe now.
[71.00 → 74.80] If you haven't already, head to practicalai.fm for all the ways.
[75.18 → 80.80] Special thanks to our partners at Vastly for delivering our shows superfast to wherever you listen.
[81.14 → 82.94] Check them out at fastly.com.
[82.94 → 85.36] And to our friends at fly.io.
[85.70 → 89.32] We deploy our app servers close to our users and you can too.
[89.66 → 91.56] Learn more at fly.io.
[97.70 → 102.12] Welcome to another fully connected episode of Practical AI.
[102.56 → 109.24] This is where Chris and I keep you fully connected with everything that's happening in the AI community.
[109.24 → 117.58] We'll discuss a few things that are in the AI news and dig into some learning resources to help you level up your machine learning game.
[118.22 → 119.10] I'm Daniel Whiten ack.
[119.22 → 122.20] I'm a data scientist with SIL International.
[122.78 → 127.90] And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[128.46 → 129.14] How are you doing, Chris?
[129.60 → 130.50] Doing great, Daniel.
[130.56 → 131.12] How are you today?
[131.62 → 133.02] I am doing great.
[133.26 → 137.56] I don't know if our listeners listened to a couple episodes ago.
[137.56 → 145.10] We had a bird family setting up camp on our deck at our apartment and having two eggs.
[146.12 → 149.34] So one of those eggs, unfortunately, didn't make it.
[149.40 → 150.96] But one turned into a bird.
[151.62 → 153.58] And that bird flew the coop.
[153.74 → 157.74] And now they have decided to start another family on our porch.
[157.90 → 163.46] Because apparently it's a great place to start a family of doves, I guess.
[163.84 → 164.56] It's the coop.
[164.78 → 165.66] The great hatchery.
[166.00 → 166.20] Yeah.
[166.20 → 167.34] So I have another chance.
[167.42 → 174.32] I never got to get out my computer vision kit and cameras and monitoring last time around.
[174.44 → 176.20] So maybe I'll have another chance here.
[176.20 → 181.02] Because I suspect that the same pattern is repeating.
[181.50 → 181.84] Gotcha.
[182.42 → 183.54] Looking forward to that.
[183.92 → 187.34] We need to post pictures of it, you know, or put some video in or something.
[187.34 → 197.58] If anybody has any suggestions out there for alerting or monitoring based on activities of doves in a nest, let me know.
[197.90 → 201.32] And I can set up the Raspberry Pi and all that stuff on my deck.
[201.84 → 202.30] Excellent.
[202.30 → 214.46] Chris, every once in a while we get to do one of these shows where we bring out an assortment of topics that have caught our attention over the past couple of weeks.
[214.46 → 226.42] And I think it's a good time to do that because, you know, there's a lot, continues to be a lot coming out related to infrastructure and new models and new products and all sorts of things.
[226.42 → 229.02] So, yeah, good time to do that.
[229.32 → 243.80] One of the first things I wanted to highlight, which came out from actually a company that was a guest on the podcast a while back, Base 10, released a new open source project called Trust.
[243.80 → 268.46] So, if you go to GitHub under Base 10 Labs and then Trust, you'll find this project, which they kind of market as a seamless bridge from model development to model delivery and an open source standard for packaging models built in any framework for sharing and deployment in any environment, local or production.
[268.92 → 271.52] So, what are your thoughts when you see this, Chris?
[271.58 → 272.56] What comes to mind?
[272.56 → 273.42] I love it.
[273.42 → 275.08] I think it's very much needed.
[275.56 → 283.98] I've been putting a lot of thought lately into the need to make all of this stuff that we talk about much easier for people to get into.
[284.78 → 297.64] And so, I think trust is a fantastic way of kind of getting that going, moving from environments that are already in, like Jupyter Notebooks, out into production without having to go back to a web framework and do all that work and stuff.
[297.72 → 298.82] So, that's good stuff.
[299.60 → 299.88] Yeah.
[299.88 → 300.00] Yeah.
[300.32 → 306.30] And, you know, they include emojis on their README so you know it's friendly and accessible.
[306.42 → 306.62] How can you go wrong?
[306.62 → 306.86] Exactly.
[306.86 → 307.42] Yeah.
[307.42 → 307.54] Yeah.
[307.54 → 307.62] Yeah.
[307.62 → 308.62] Yeah.
[308.62 → 314.04] I've actually, since we talked with Base10, I've used their product a little bit.
[314.04 → 325.54] And I know that just from looking at this, I'm assuming that they're sort of eating their own dog food because, you know, some of the convenience that's built in their product is, you know, not all of it.
[325.54 → 331.52] But some of it is released in this package, which is pretty cool and kind of allows.
[331.52 → 342.44] So, there are certainly a lot of frameworks out there to do model serving or deployment or like model registry sort of things.
[342.44 → 351.78] Some of them kind of assume that you have a bit of infrastructure chops, I think, to start with.
[351.78 → 357.68] Like, you know, maybe figuring out how to run something on Kubernetes or something like that.
[357.68 → 360.94] And that's a big step for a lot of people.
[361.20 → 366.96] So, I think this, that it's really targeting, hey, you're running maybe something in a Jupyter notebook.
[367.30 → 370.84] How do I export this model and deliver it?
[371.14 → 380.82] I also think that, you know, some of these things around model deployment miss some key aspects.
[380.82 → 392.06] So, like, Trust talks about bundling secret management into the API keys into their deployments, which I think is really, really important.
[392.28 → 398.42] So, like, it's not that difficult for people to figure out how to build like a Flask app with their model.
[398.60 → 407.76] But then figuring out like testing and deployment and API keys and securely managing like the API, that's a whole nother ballgame.
[407.76 → 413.08] Yeah, I'm really impressed that they've kind of built a lot of this in.
[413.24 → 418.88] They've put a fantastic capability out in Trust in terms of being able to address that.
[419.20 → 420.50] It's something I've been thinking about.
[420.98 → 426.34] Right now is a slight sideline on this that is relevant, I think.
[426.76 → 427.84] I'm doing something.
[427.94 → 432.62] I'm learning something new through beginner's eyes because, you know, both you and I program in several languages.
[432.62 → 438.94] And we came together originally in the Go programming community, which is how we got to know each other.
[439.28 → 441.84] And right now for a different thing, I'm learning Rust.
[442.22 → 447.22] And so I've been diving into Rust, but it's forced me back into that beginner mindset.
[447.86 → 451.78] And I've brought that back into these other things that we talk about a lot lately.
[452.02 → 456.44] And I've been looking at a lot of the AI and deep learning kind of through that beginner's mindset.
[456.80 → 457.66] And there's such a need.
[457.66 → 461.28] We're still leaving out a lot of people on these capabilities.
[461.50 → 463.60] And things like Trust are amazing solutions.
[463.78 → 472.40] I think we need others as well, just so that people with different levels of skill, different skill levels and such can find it accessible.
[472.64 → 475.90] So Trust is one part of that solution, it looks like.
[476.26 → 476.46] Yeah.
[476.46 → 484.90] And just to give people like a since you're listening, a sort of visual picture of what this might look like.
[484.90 → 495.92] If you're in sort of Python and you create a model, you can import the trust package and then sort of use this make trust command or method.
[495.92 → 502.12] You can point to the directory where your, you know, where your model or where your code is.
[502.36 → 513.76] And then that will sort of serialize and package the model and freeze like dependencies within a Docker image and all of that, which can be complicated in and of itself.
[513.76 → 519.38] And then you can call that and or deploy it via a variety of ways.
[519.50 → 525.34] I mean, in clouds and like really simple ways to run things like ECS or GCP Cloud Run.
[525.50 → 528.40] Of course, you could run it in base 10 as well in their own infrastructure.
[528.40 → 538.14] But it has that because it's sort of freezing all of these dependencies and your model package in a Docker image.
[538.14 → 547.42] Then you have the ability to kind of run this all sorts of places, whether that's local or in these cloud solutions or in base 10 or wherever.
[547.42 → 549.68] So, yeah, I think it's pretty cool.
[549.92 → 565.98] And it's, yeah, an approachable way to get into this model delivery stuff for those that maybe are, you know, hitting that pain of, hey, I've got my model in a Jupyter notebook, but I don't know what to do next sort of situation.
[566.90 → 569.76] So I have a random question for you.
[569.84 → 570.04] Sure.
[570.04 → 578.70] As we're looking at things like trust and recognizing that most of our community here is mainly Python oriented, you know, for the development stuff.
[578.70 → 588.32] Do you think that anytime soon we will start expanding some of the development and then, you know, deployment and packaging tools into other languages?
[588.52 → 589.44] Or do you think that's likely?
[589.68 → 598.16] Or do you think we have a way to go before we get to something where we're starting to look at kind of multi-language community rather than the Jupyter focus we've had for so many years?
[598.16 → 601.24] Yeah, it's an interesting question.
[601.58 → 603.60] I think there are certain sets of tooling.
[603.86 → 611.04] Like I know that there's tooling now in Go where you can import like hugging face transformers models and such.
[611.22 → 614.60] And so there's more interoperability.
[615.26 → 626.72] There are certainly a lot of ways to run models in various other systems, whether those be like or languages like JavaScript or Go or Rust or other things.
[626.72 → 630.74] But that kind of like model development workflow.
[630.82 → 631.36] I think so.
[631.86 → 635.28] In my mind, still seems very much Python focused.
[635.28 → 639.40] I don't see a lot of motion away from that.
[639.68 → 643.22] I do see certain trends happening.
[643.68 → 655.00] Like language things seem to be more focused on Python now in terms of the model development side and maybe like interoperability on the inference side.
[655.00 → 657.16] Are you seeing similar things?
[657.76 → 660.06] Yeah, that seems accurate to me as well.
[660.60 → 661.26] Yeah, I am.
[661.60 → 673.46] It's just as like going back to my Rust learning experience as I'm having to delve into, you know, out of something I know well and into something that puts me back into first grade, so to speak.
[673.46 → 678.76] I've been thinking about the fact that we're still leaving behind communities of people.
[679.30 → 696.28] And I'm really curious to see what other options, you know, some different organizations or companies or just inventive individuals come up with to let us be more inclusive with people that are maybe not traditionally, you know, have this space accessible to them.
[696.92 → 697.02] Yeah.
[697.02 → 697.06] Yeah.
[697.58 → 701.84] Just out of curiosity, Chris, what has your experience been like with Rust?
[702.38 → 711.66] Well, without taking us too far off the main line of our topic area, just as a new thing, they take a different approach.
[711.82 → 718.48] I can see it's one of those languages that always wins the most loved, you know, when people are rating their languages and stuff.
[718.48 → 721.86] And I can see why, but it is a substantial learning curve.
[722.16 → 739.50] And it has made me very empathetic to people who are having to deal with other learning curves, such as this one that we're talking about in general, because it, unlike Go, which tends to be fairly small by design and kind of have one way of doing everything and does some stuff for you that's pretty nice.
[739.50 → 750.18] Rust kind of takes the opposite approach and gives you every possible option out there to optimize what you're doing, which is important for certain use cases, including one that I'm working on.
[750.98 → 752.88] And so it's been interesting.
[753.06 → 757.52] It's put me back in the'm going to take a big thing and learn it new.
[757.52 → 777.20] And it made me think about if you're not a Pythons and super savvy in the juxtaposition of where Python intersects with the deep learning world in general, then this is still we're still in a moment where we're this really huge, important field that's revolutionizing technology.
[777.54 → 780.16] It's still quite inaccessible to a lot of people, I think.
[780.24 → 782.26] And so it's just a reminder.
[782.46 → 784.06] That's why it's on the top of my mind today.
[787.52 → 817.50] Well, thinking about like this model delivery side of things, it gets me thinking also about how,
[817.52 → 836.36] you know, we've seen an increasing number of things in the news and in conversations about ML ops and Git ops and CCD impacting kind of AI and the ML world and people thinking more about this operations side of things.
[836.36 → 856.96] I wonder, you know, I still encounter a lot of AI practitioners or data scientists who are really kind of trying to get a grip on what is CCD, and how does that side of automation, or how should it or could impact their development workflows?
[856.96 → 867.94] Might be worth talking for a second about, you know, CCD and what that exactly means and how it might impact practitioners workflows.
[868.38 → 869.22] What do you think?
[869.86 → 871.08] I totally agree with you.
[871.08 → 894.58] And we've actually talked a little bit about this on previous episodes about the general feel that there has to be a convergence between CCD and ML ops instead of them being kind of thought of as separate subfields, if you will, because we're going into a future where they're not two totally separate things that are always on their own tracks and on their own infrastructures.
[894.58 → 897.98] Models are going to be in everything we do going forward.
[898.48 → 905.40] And so the idea of software and models being completely separate with their own infrastructures is a little bit.
[905.94 → 906.54] I don't know.
[906.56 → 907.64] It seems antiquated to me.
[908.10 → 920.86] I think there's a movement that we're seeing right now where they're starting to integrate or ML ops and CCD in general are starting to come together as people realize that, yes, I'm going to be deploying software and yes, I'm going to be deploying models.
[920.86 → 924.02] Most often they will be happening together and at the same time.
[924.56 → 927.32] And so, I must have something that works for all of the above.
[927.92 → 929.70] And I think that that's a bit of a challenge.
[929.96 → 935.74] If for no other reason, there are some cultural differences in how we approach and what the priorities are and stuff.
[935.80 → 942.00] And so there's kind of two worlds smashing together, trying to find something that works for all.
[942.00 → 955.78] So, Chris, I want to maybe describe some of what I've been doing recently with like this intersection of automation and CCD and machine learning or AI models.
[955.98 → 962.60] And I'd love to get your critique of that and help me know how I can how I can do better or maybe just initial thoughts.
[962.60 → 977.88] So a lot of what we've been doing recently, we're always kind of tweaking this workflow is we have an ML ops solution, and we're really thinking of that ML ops solution as our experimentation and model training platform.
[977.88 → 986.86] So like this is where a lot of jobs will necessarily fail because we're trying like weird thing, weird and crazy things.
[987.06 → 995.18] And we like to have queues of GPUs where we can queue up experiments and train new models or do pre-processing of new data sets.
[995.18 → 1011.30] Eventually, we get to a state where we sort of figure out what we're doing, and we know there's a certain type of model that we are training successfully and would like to integrate into some system or service that we support.
[1011.30 → 1025.90] And so our ML ops solution kind of provides as an output of these training jobs, like a hash of a bundle that is like the model bundle output that we have trained.
[1026.46 → 1035.10] Right. So by hash, I just mean like a series of numbers, letters that that points to a unique bundle that we've trained.
[1035.10 → 1048.06] And so we can look up in our ML ops system like this model bundle, you know, whatever the hash is, was trained, you know, on this date with this model and this is how the task went and all that.
[1048.20 → 1056.02] And it connects also back to our Git repo where we have the training code with the exact commit ID that trained that model.
[1056.12 → 1061.72] So we've got like the code that trained it, the output of the model and the hash of that model.
[1061.72 → 1066.18] But then like that's the trust project was just talking about.
[1066.28 → 1068.34] That's not like model delivery. Right.
[1068.72 → 1079.64] So in terms of connecting more to the CCD things, at that point, our model is really just like an artifact is used in software.
[1079.64 → 1082.42] Right. Is used in various software functions.
[1082.42 → 1086.82] So we also have a usually a separate GitHub repo.
[1086.82 → 1091.46] So maybe it's an API we're supporting or an application or something like that.
[1091.52 → 1094.08] The thing that's integrating our model.
[1094.68 → 1101.80] And then we use GitHub actions, but other people use like Jenkins or Travis or something for CCD.
[1101.80 → 1116.80] But what happens is we have GitHub actions, which for those of you that don't know is like it's integrated into GitHub, but it's a continuous integration, continuous delivery system similar to Travis or Jenkins or whatever.
[1116.80 → 1128.24] And so when we push a change into that repo, GitHub automatically runs a series of tests that we specify in GitHub actions.
[1128.52 → 1135.00] So these are like unit tests for our Python code and then deploys the updated version of the application.
[1135.00 → 1138.42] Let's say it's an API. It deploys an updated version of the API.
[1139.18 → 1153.02] Now, what's interesting, I think, where this connects with machine learning and the model bundle is like if we update that API to use a new model, what I kind of recommend our team do.
[1153.02 → 1158.92] And we don't have it integrated everywhere because, you know, we have limited time.
[1159.02 → 1166.68] But in an ideal scenario, what we'd have is a sort of minimum functionality test for this updated model.
[1166.82 → 1178.06] So like if it's a sentiment analysis model, I would have a series of like a table of tests that would say like, you know, one sample is like this is a really great thing and it's so awesome.
[1178.06 → 1184.32] And that should be rated as positive sentiment always, regardless of what model I update, it should always get that right.
[1184.92 → 1198.44] And so that way, if I update a model and I say I point my API to the new model bundle in CCD, it'll run that minimum functionality test against the functions that are calling my model.
[1198.44 → 1209.76] That way, if I accidentally point it to a terrible model that can't even pass like minimum functionality, then it fails the build, and it won't deploy with the new model.
[1210.12 → 1225.38] Right. And so it's almost like a table driven test that's used in like APIs and such, except it's really a test against the functionality of the model versus the functionality of the actual application.
[1225.38 → 1228.80] So have you seen it approached in other ways?
[1228.90 → 1233.34] I'm always curious to kind of learn, learn what people are doing in this respect.
[1233.94 → 1239.94] So I'm going to say nice things about what you're saying, and I'm going to do this despite the fact that you're my host, my co-host on this.
[1240.24 → 1242.62] So I would say this to anybody.
[1242.88 → 1250.82] No, I think that you have the benefit of having been a software developer as long, you know, as you've been a data scientist.
[1251.14 → 1253.44] And so you're able to see both sides of that.
[1253.44 → 1256.38] I think that's often absent, that perspective.
[1256.86 → 1266.28] So what you've described, you know, you've picked your you've picked some specific technologies that you want to use to support CCD efforts, which are fine.
[1266.36 → 1273.80] And I think that there's a bunch of different options there that are all more or less equally good, you know, with some pros and cons to each one as normal.
[1273.80 → 1284.36] But you've integrated it so that you're you're not only testing the software, but you're testing your data by testing how that data is running through the model and inferencing.
[1284.74 → 1288.00] So that is a very, very cohesive system.
[1288.00 → 1290.36] Unfortunately, here's the bad news.
[1290.42 → 1297.38] I think that your approach is a little bit more of the exception to the rule in the broader industry out there.
[1297.38 → 1310.18] I think that, you know, this is I've seen this at a number of organizations where the skill sets of understanding that are still kept in kind of in separate groups, separate departments, maybe even whole separate organizations.
[1310.18 → 1326.32] And I think the benefit of being working for a relatively, you know, small organization, you know, not a giant Fortune 500 thing is that you're able to keep everything close enough together and your expertise is able to intertwine to solve that well.
[1326.86 → 1331.54] I think that that it is a good guideline for others to look at.
[1331.70 → 1336.80] Yeah, if you ever find I know you have all the spare time on your hands, but should you ever find it?
[1336.80 → 1358.94] I think maybe actually publishing a little thing on that would be a useful tool for people to kind of see how you've approached it other than just listening to the podcast here, because you're kind of hitting you're hitting the software best practices, and you're hitting the data science best practices together and treating the model as an artifact that needs to work for testing in that software deployment process and delivery.
[1358.94 → 1361.66] So anyway, yeah, I love what you're doing there.
[1361.66 → 1369.92] Yeah, I think if there was a takeaway for people that might get them thinking like you don't have to do things exactly that way.
[1370.00 → 1371.68] And I'm sure there are better ways to do it.
[1372.02 → 1385.60] But I think one thing I've learned over time is like if your model is being used in software, and you can update your model without that software being retested in some way,
[1385.60 → 1389.36] there's like a huge risk and problem, right?
[1389.64 → 1397.54] Because you could just run another like training run and there your model gets updated and all of a sudden like your software product breaks.
[1397.76 → 1401.92] But the software team or the other people working on it, they're all transparent to them.
[1401.92 → 1408.36] So like that, that sort of that step, whatever it is, whether that that could even be manual, right?
[1408.42 → 1415.48] Like you don't update the model in one S3 bucket until you run this script to test it, and then you update it.
[1415.56 → 1418.30] Like it could be manual in that way, if nothing else.
[1418.30 → 1418.62] Right.
[1419.26 → 1421.82] But there needs to be some process there.
[1422.24 → 1429.20] Yeah, that can be brutally hard to debug something like that, because if you only have that that insight, if you're going to your example,
[1429.20 → 1438.90] if you're the software team, and you haven't made any changes and yet now you're deployed and delivered software has just broken, and you don't have insight into the fact that the model changed,
[1439.24 → 1443.00] you can waste weeks of time trying to figure out what happened on that.
[1443.00 → 1449.06] So it's a huge productivity hit not to have that point of integration and to apply those best standards.
[1449.42 → 1454.12] In the scheme of things, it's still complicated, more so than it should be.
[1454.12 → 1464.26] But it's cheap in the sense of the things that you need to run and store and keep up with it in that versioned manner is not hard today.
[1464.56 → 1466.74] That is a capability that anyone can afford.
[1466.98 → 1473.52] And to not have the discipline to do that can result in some real challenges that waste a lot of time there.
[1473.70 → 1475.44] So I'm with you on that.
[1475.44 → 1485.68] I think that having those integrated and having the discipline to do them together and make sure that it runs at the end is pretty vital to moving as fast as we can.
[1485.68 → 1515.08] Well, Chris, I sort of went down the infrastructure rabbit hole, as I often do.
[1515.08 → 1518.78] And my team will tell you that I often go down that rabbit hole.
[1518.92 → 1527.76] But there is a lot going on else in the AI world that has sort of hit our desks over the past weeks.
[1528.16 → 1539.94] You forwarded something to me related to some of what you've been following in the aerospace kind of industry or your own interest in piloting and that sort of thing.
[1540.38 → 1541.98] You want to describe that a little bit?
[1542.44 → 1543.36] Yeah, I'd be happy to.
[1543.36 → 1544.96] I ran across something.
[1545.22 → 1567.56] Carnegie Mellon University, which is by any measure one of the top AI schools, often described as the top AI school in the world, definitely in that top half dozen without question, released a paper on something that they had been doing in their robotics organization, which entitled AI Pilot Can Navigate Crowded Airspace.
[1567.56 → 1574.90] And of course, this appealed to me both from the AI perspective, the fact that I am a pilot and the fact that I work for an aerospace company.
[1575.04 → 1576.86] So it hit me on a bunch of fronts.
[1576.86 → 1590.48] And so in this one, what they did was they put together a model and trained it and have been testing it in simulation that enables an autonomous aircraft to navigate crowded airspace.
[1590.48 → 1603.22] And so and for those who don't fly as pilots, you know, airspace around airports gets very crowded, and you really have to work hard to maintain separation and keep things safe and such.
[1603.22 → 1605.24] So this is a non-trivial problem.
[1605.36 → 1609.60] People that don't pilot will look up and go, well, you got the whole sky there.
[1609.70 → 1610.76] You know, how bad can it be?
[1610.86 → 1615.64] But you're also in fast moving vehicles, and you're all moving on in the same patterns.
[1615.64 → 1618.34] And so you can have a problem very quickly.
[1618.84 → 1622.34] So this is a pretty important challenge to overcome.
[1622.74 → 1625.68] And it's one that we know that the industry is pushing forward.
[1625.82 → 1632.06] So I will say kind of obliquely in the military space where you're not necessarily in air patterns and stuff.
[1632.18 → 1638.22] We're doing autonomous stuff, as is reported in the general news, all the time in terms of aircraft.
[1638.54 → 1640.32] And I think that's fairly well understood.
[1640.32 → 1658.48] In the civilian space, though, if you imagine in the future being on an autonomous airliner and you and 200 of your best friends are flying around, and you have AI models that are driving this, it's not as hard to move between busy airspaces.
[1658.48 → 1664.42] As you're moving across the maybe across the countryside or something, you're kind of out there by yourself.
[1664.64 → 1665.52] There's not as much to do.
[1665.52 → 1671.46] But on the start of that journey and on the end of that journey, there are a lot of other aircraft in proximity to you.
[1671.54 → 1674.42] So the ability to do this is pretty important.
[1674.90 → 1686.82] They say that this model can safely avoid collisions, predict the intent of other aircraft, track those aircraft and coordinate with those aircraft's actions, communicate over the radio.
[1686.94 → 1689.54] It uses natural language processing to do that.
[1689.54 → 1693.74] It has a vision system that uses six cameras to visually track.
[1693.74 → 1700.38] And one other distinction in general with flying, there are two kinds of systems for flying.
[1700.54 → 1704.04] One is instrument flight rules, which is what you would think of with airliners.
[1704.10 → 1710.36] And one is kind of what us private pilots, the little guys, so to speak, do, which is visual flight rules.
[1710.78 → 1713.76] And you tend to have visual flight rules lower down to the ground.
[1713.76 → 1720.08] And so this system, we've had flight, automatic flight control systems and airliners for decades that fly.
[1720.20 → 1724.24] But those tend to be high up in the sky, and you're kind of alone traffic wise.
[1724.40 → 1726.12] This is designed to do visual.
[1726.46 → 1736.60] Can work with instruments, can work with radios, can work with cameras to do the visual stuff and make all the decision-making in real time right there to keep everybody in the sky safe.
[1736.60 → 1739.72] So it's a pretty cool problem to solve.
[1739.84 → 1750.92] And it's one that eventually, I know people shudder when I say this, but I think that it is not so far out that all of us will be getting on airliners that are almost entirely automated.
[1751.12 → 1754.34] They might have a human in the cockpit because it makes us feel better.
[1754.34 → 1757.82] But eventually, that just won't be really needed.
[1758.04 → 1762.44] And so this is one of those big steps toward trying to do that.
[1762.56 → 1771.58] And they're combining, going back to a theme that we've been talking about lately, they are combining natural language processing models with visual processing models.
[1771.58 → 1772.94] They're integrating those.
[1773.12 → 1780.84] And they're being able to use that system across multiple domains to affect a real world solution here.
[1780.84 → 1787.16] So I think this is very much in line with the kinds of innovations that we've been looking at over this past year.
[1787.56 → 1788.08] Yeah.
[1788.20 → 1792.52] So I have a couple of follow-up questions on this, which is fascinating.
[1792.82 → 1799.10] One is, I just want to maybe get your perspective since you're more plugged into the space and have interest in the area.
[1799.10 → 1814.92] I know that it's been talked about a while, for quite a while, that the sort of short or last mile kind of trips like in a city, in a large city, you could have like air taxis, right?
[1815.04 → 1819.14] Which are basically like humans in a big drone, right?
[1819.18 → 1820.64] And flying around the city.
[1820.64 → 1831.78] My understanding is any reasonable person would say, well, there needs to be computer systems within that that would coordinate and manage the safety of all the routes.
[1831.94 → 1836.88] And if there are a bunch of things flying around in the air, it gets very complicated in a crowded space.
[1837.06 → 1840.14] So maybe this gets us closer to that.
[1840.38 → 1841.06] Do you have any thoughts?
[1841.74 → 1842.30] It does.
[1842.48 → 1844.36] And so I will comment.
[1844.46 → 1849.48] I'll both answer your question, and I'll make a reference that not even you know about me, not just the listeners.
[1849.48 → 1863.10] The specific issue there is you're talking about massively scaling up the number of platforms, as I would say, in my industry that are in that space, which is my specialty.
[1863.68 → 1871.60] It is if you were to say instead of having 10 things in a given closed space, it could be airspace, could be on the ground.
[1871.90 → 1875.36] What if there were 10,000 in the same space?
[1875.76 → 1878.62] Maybe not all big, but maybe many are very small autonomous.
[1878.62 → 1879.68] How do you manage that?
[1880.14 → 1884.22] That's specifically where my current focus and expertise lies.
[1884.48 → 1895.32] And so this is a control system for aircraft that can enable things like autonomous taxis and package delivery and all these other things.
[1895.50 → 1897.70] It doesn't solve the whole problem.
[1898.10 → 1901.40] It kind of solves how do you make decisions from one platform.
[1901.40 → 1908.20] It doesn't necessarily solve all the integration things when you have a massively scaled situation there.
[1908.32 → 1910.06] But it's an important step.
[1910.26 → 1920.98] It's really, really crucial to enable this future of civil aviation, which includes all of these low flying drones, package deliveries, kind of like when we look at a Hollywood movie.
[1920.98 → 1925.20] Maybe, you know, these futuristic science fiction movies, maybe Star Wars.
[1925.40 → 1929.26] And they have all the city is just full of flying things everywhere at every level.
[1929.42 → 1930.50] We're heading that way.
[1930.68 → 1932.70] But we need to get some of these technologies in place.
[1932.80 → 1937.02] And this is a key, crucial Lego in that pile of Legos to build that.
[1937.02 → 1950.06] Yeah, my second follow-up question to that, which is, it's funny that this came up today when we're chatting because, so I always listen to podcasts when I'm in the shower, which is a weird way to start this subject.
[1950.22 → 1953.72] But one of the ones I really like is Dark net Diaries.
[1953.88 → 1957.48] I love Dark net Diaries and, you know, just the stories there.
[1957.48 → 1959.86] But I listened to one this morning.
[1959.96 → 1963.48] It's actually from a while ago with a guy named Sammy.
[1963.82 → 1970.48] And he created this sort of proof of concept, which you can look at on GitHub, where it's called Skyjack.
[1971.32 → 1974.06] And essentially what he showed at the time, this is a while ago.
[1974.12 → 1975.62] I'm sure things have gotten better now.
[1975.74 → 1983.56] But he showed that he could put a drone up in the air with an antenna on it and a Raspberry Pi.
[1983.56 → 1992.60] And basically wherever he would fly it, he would hijack the other drones around because the signals he would intercept, and he could actually take control of them.
[1993.14 → 1997.14] And so it's one of these things like anything that's connected is hackable, right?
[1997.20 → 2008.12] And so also as you kind of increase the number of things in an area, I think certain people might think, oh, that's dangerous because a computer is automating the flying.
[2008.12 → 2017.12] I think the dangerous part is not the computers automating the flying, but humans hacking into the computers automating the flying, maybe.
[2017.36 → 2022.82] So I don't know from your perspective how like security impacts these sorts of systems.
[2023.02 → 2030.06] But as you kind of automate, yeah, as you automate things in this area, the computer can obviously do, well, maybe not obviously,
[2030.22 → 2036.64] but I buy into the fact that a computer can do a better job at this sort of flight control than a human.
[2036.64 → 2040.58] But it makes it sort of hackable as well, right?
[2041.24 → 2041.88] It does.
[2042.18 → 2053.14] And if anyone doubts that computer and model together are better at this point, you can go back, you can Google DARPA alpha dogfight.
[2053.14 → 2062.38] And a couple of years ago, there was a public, it's on YouTube, there was a public demo where, and we've talked about this briefly on the show before,
[2062.74 → 2069.56] where they had automated a bunch of companies, brought their autopilots, they put them on an F-16 simulator,
[2069.88 → 2071.60] and they competed against each other.
[2071.68 → 2075.06] And then they had to compete against an Air Force instructor.
[2075.32 → 2079.84] And that Air Force instructor was the equivalent of what we would think of as a Navy Top Gun instructor.
[2079.84 → 2082.12] It was a weapons school instructor.
[2082.86 → 2090.22] And the top one that went against the human absolutely demolished him in a dogfight.
[2090.68 → 2093.42] I mean, demolished him five times in a row.
[2093.76 → 2096.20] It was, I mean, just, it was like stunning to watch.
[2096.78 → 2103.12] And so, yes, computers can currently do this better than humans can, even if you're the best human in the world.
[2103.62 → 2105.58] So that's already a done deal.
[2105.80 → 2107.64] And it's just being improved upon since.
[2107.64 → 2118.74] So when people are worried about computers flying these things, I would much rather, I'm that one person who would much rather for this technology to be flying the airliner I'm in than the human,
[2118.86 → 2121.94] because I know what the difference is in capability.
[2122.28 → 2124.26] So it doesn't solve everything.
[2124.26 → 2132.96] And it doesn't solve what happens at massive scale when you're struggling to get to handle all the things in the airspace together.
[2132.96 → 2135.58] But it's pretty crucial.
[2135.86 → 2144.48] And I think your point about the cybersecurity, cybersecurity is huge when it comes to aviation and autopiloting, because it's a natural thing to hack.
[2144.56 → 2152.30] And in my space, which is defence oriented, you would assume that your adversary is always going to actively try to do exactly that.
[2152.38 → 2154.42] So it's just built in to the equation.
[2154.42 → 2157.92] We're automatically handling that as we solution for it.
[2158.28 → 2161.34] And that will obviously roll out into the civilian space as well.
[2161.76 → 2166.94] And air taxis and package delivery, all of that has to have that cybersecurity capability.
[2167.80 → 2168.28] Fascinating.
[2168.62 → 2171.20] I'm glad we went down that rabbit hole.
[2171.66 → 2172.52] It's fun, isn't it?
[2172.52 → 2173.84] I love talking about that.
[2174.12 → 2174.36] Yeah.
[2174.36 → 2182.94] One thing I wanted to highlight, maybe just somewhat quickly before we get on to learning resources, is I took a look recently.
[2183.28 → 2187.14] It popped up in my Twitter feed, one of the things.
[2187.36 → 2190.06] But I looked through the whole set of demos.
[2190.34 → 2195.46] And I would recommend people go and check out some of the NVIDIA AI demos that are coming out.
[2195.58 → 2199.04] We'll link to that in our show notes.
[2199.04 → 2205.04] I was kind of like, I don't know if I just hadn't looked at it in a while, but I looked there, I was like, oh, wow.
[2205.34 → 2207.64] And then, oh, wow, there's another, oh, wow.
[2208.04 → 2215.54] That's sort of like all sorts of things I wasn't, I mean, I sort of peripherally knew were going on, but really powerful kind of demos.
[2215.92 → 2226.00] One being kind of this way of taking like sketches and turning them into photorealistic images.
[2226.00 → 2231.00] This is kind of related to some of the like image stuff that we've been seeing recently.
[2231.20 → 2245.30] But another really cool one I thought was this vid to vid cameo thing, which you could sort of synthesize a talking head based on an image of yourself that you could use in, for example, like Zoom calls.
[2245.30 → 2257.66] So you could just have liked your talking head synthesized based on imagery versus like your actual video on the Zoom call, which I thought was really, fascinating.
[2258.22 → 2260.48] And I don't know, something I kind of want to try.
[2261.18 → 2262.16] No, I agree with you.
[2262.22 → 2270.80] I'm so glad that this podcast is audio only because if it wasn't, we would absolutely definitely need to implement that to make us presentable.
[2270.80 → 2277.22] So, yeah, we have faces that are made for radio, so to speak, or podcasting in this case.
[2277.80 → 2280.68] But yeah, that's, you know, we're already kind of seeing that.
[2280.80 → 2285.32] I mean, using Zoom, a lot of folks are using Zoom and other platforms like that at work.
[2285.64 → 2291.60] And I always have alterations that I'm making to make it more interesting and stuff.
[2291.66 → 2295.24] And some of them actually do the facial fixes in real time.
[2295.24 → 2298.96] So, yeah, that sounds like something that I definitely need.
[2299.74 → 2304.42] My wife would, I'm sure, she's always telling me, oh, gosh, you need to look better than that.
[2306.08 → 2307.52] No comment from my end.
[2308.02 → 2311.86] Well, let's maybe hit a few learning resources as we close out here.
[2311.92 → 2317.12] I think going straight off of the NVIDIA stuff, which is mostly vision and 3D things,
[2317.60 → 2321.62] I wanted to highlight this paper that I saw trending on papers with code.
[2321.62 → 2325.72] It's a survey paper, so it's a little bit maybe more approachable in some ways.
[2326.30 → 2328.72] 3D vision with transformers, a survey.
[2329.56 → 2333.62] This is from Gene Labour et al.
[2334.04 → 2338.68] And they go through and talk about all of this sort of 3D representations
[2338.68 → 2343.56] and using transformers on 3D data for vision.
[2344.06 → 2345.46] It's fascinating.
[2345.46 → 2353.76] And if you're kind of wanting to get an overall picture of some of the things going on in this space with 3D data,
[2354.42 → 2361.52] I think that's a fascinating place to get some of that information all in one sort of shot.
[2362.14 → 2367.76] The other thing I was going to mention, which is not related to vision,
[2367.76 → 2375.60] but back in my sort of world of NLP is it's going to be a natural language processing with transformers course.
[2375.94 → 2380.36] It's going to be in September through October 2023.
[2381.12 → 2384.26] And there's some people from Hugging Face that are teaching that.
[2384.66 → 2386.00] It looks pretty awesome.
[2386.12 → 2388.82] So it's like live teaching sort of thing.
[2388.82 → 2394.96] So, yeah, I would definitely recommend check that out if you're interested in it is paid.
[2394.96 → 2399.10] But if you're interested in that sort of paid live learning opportunity,
[2399.10 → 2404.80] then it seems like a perfect one to learn some of the latest stuff.
[2405.34 → 2408.86] Yeah, good people teaching it there in terms of if you're going to spend money on it,
[2408.90 → 2411.52] spending it for people that are at the top of their field.
[2411.72 → 2412.30] That are legit.
[2412.50 → 2413.34] Yeah, exactly.
[2414.10 → 2415.66] So cool, Chris.
[2415.86 → 2418.16] Well, that's all I had for today.
[2418.16 → 2424.60] I enjoyed the various rabbit holes we went down and learned a little bit about aviation along the way.
[2425.28 → 2427.10] So, yeah, I appreciate the conversation.
[2427.80 → 2428.56] Yep, absolutely.
[2428.78 → 2429.78] Keep flying high, Daniel.
[2429.86 → 2430.76] I'll talk to you next week.
[2430.82 → 2431.32] All right.
[2431.76 → 2432.22] Bye-bye.
[2432.36 → 2432.64] Bye-bye.
[2441.36 → 2442.22] All right.
[2442.36 → 2443.94] That is our show for this week.
[2443.94 → 2446.50] If you dig it, don't forget to subscribe.
[2446.50 → 2449.76] Head to practicalai.fm for all the ways.
[2450.28 → 2455.68] And if Practical AI has benefited your life, pay it forward by sharing the show with a friend or a colleague.
[2456.02 → 2459.00] Word of mouth is the number one way people find shows like ours.
[2459.40 → 2462.26] Thanks again to Vastly for fronting our static assets,
[2462.56 → 2465.02] to Fly.io for backing our dynamic requests,
[2465.58 → 2467.10] to Break master Cylinder for the beats,
[2467.34 → 2468.26] and to you for listening.
[2468.48 → 2469.16] We appreciate you.
[2469.40 → 2470.36] That's all for now.
[2470.36 → 2472.12] We'll talk to you again on the next one.
