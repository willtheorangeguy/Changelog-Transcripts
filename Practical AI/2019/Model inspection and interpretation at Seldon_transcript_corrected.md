[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CI, CD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.18 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.46 → 102.28] And now onto the show.
[106.94 → 109.22] Welcome to Practical AI.
[109.60 → 113.72] I am Daniel Whiten ack, a data scientist with SIL International.
[114.10 → 116.66] And I'm joined by my co-host, Chris Benson,
[116.66 → 121.94] who is a chief strategist for AI and high performance computing at Lockheed Martin.
[122.16 → 122.94] Hey, Chris, how are you doing?
[123.16 → 123.78] I'm doing fine.
[123.82 → 124.50] How's it going, Daniel?
[124.50 → 125.60] It's going good.
[125.68 → 126.32] No complaints.
[126.52 → 133.18] It's been kind of gloomy weather here for a while in Indiana, but, you know, such as this time of year, I guess.
[133.90 → 134.66] Sounds good.
[134.76 → 138.24] I'm about to head out of town for Lifeworks in Boston.
[138.36 → 139.20] We're going to give a talk.
[139.48 → 142.58] And it'll be over by the time this episode comes out.
[142.74 → 146.82] But right now, I'm looking forward to heading off and doing that and meeting a bunch of people up there.
[147.08 → 147.38] Awesome.
[147.38 → 152.00] Well, I'm super excited about our guests and our topic today.
[152.76 → 159.44] As our listeners know, we have a particular passion for the practical side of AI, hence the name of the podcast.
[160.20 → 167.44] We realize that, you know, a lot of times the blockers for AI projects are not necessarily the sophisticated modelling,
[167.66 → 171.74] but the whole productionizing things and operationalizing things.
[171.74 → 179.04] And one of the companies that's really leading the way in this area, at least I feel like, is a company called Selden.
[179.66 → 185.86] And today we have Janice Klaus, who's a data scientist at Selden, joining us.
[185.98 → 186.54] Welcome, Janice.
[186.82 → 187.06] Hi.
[187.14 → 188.30] I'm very pleased to be in the show.
[188.64 → 188.94] Awesome.
[189.12 → 191.02] Well, we're really happy to have you.
[191.36 → 201.32] Maybe we could start things off by just hearing a little bit about your background and how you eventually got into AI and data science things.
[201.74 → 203.38] Yeah, sure thing.
[203.96 → 207.34] So my background is actually in mathematical modelling.
[208.14 → 212.54] So I did my PhD at the University of Warwick here in the UK.
[213.16 → 225.70] And there's a doctoral training centre for complexity science, which is basically applied math to real world systems.
[225.70 → 234.44] And with a particular interest on sort of systems that are made up of simple rules, but that can result in interesting emergent behaviour.
[234.82 → 237.06] So just to give you a couple of examples.
[237.38 → 247.64] So people in my cohort worked on various problems sort of ranging from traffic modelling to modelling the spread of infectious disease.
[248.18 → 251.56] One of my papers was also roughly related to that kind of thing.
[251.74 → 254.22] So that's my background.
[254.22 → 254.82] Awesome.
[255.30 → 263.22] And did that sort of academic training, did that transfer naturally into kind of industrial data science work?
[263.34 → 275.58] I know a lot of people, including myself, maybe had some kind of awkwardness or weirdness and kind of trying to transition from academic science into data science and industry.
[275.80 → 279.12] So it sounds like your work maybe was more applied, though.
[279.12 → 288.12] Yeah, I can definitely relate with what you're saying, because the incentives in academia and in the industry are completely different.
[288.12 → 299.10] But the great thing about my department was that it was very multidisciplinary and people were working on all kinds of things.
[299.10 → 304.10] So I mentioned things like epidemiology research.
[304.10 → 311.00] But also there was a small group of people doing machine learning research with also some industry applications.
[311.00 → 321.20] So that this was a smaller portion of the centre because we didn't have as many staff members doing research in machine learning.
[321.20 → 323.20] But there were some good ones.
[323.20 → 339.68] And towards the end of my PhD, I started taking more interest into machine learning and started going to paper clubs and be more interested in student talks about the topic.
[339.68 → 349.06] And as I was looking for a job in the industry and preferably a modelling job, I realized that this is the best way of going about it.
[349.18 → 354.92] And I should really, really pick up the subject in my spare time if I can.
[355.74 → 362.14] So, so, Janice, I was wondering, as we were prepping for getting online and talking to you about this,
[362.46 → 369.44] is by chance the company named Selden in any way related to the Harry Selden figure in the Foundation series?
[369.68 → 372.42] Yeah, I was partially expecting this question.
[372.62 → 375.04] And that's that's exactly that's exactly true.
[375.48 → 382.60] In fact, I'll tell you before I joined Selden, I had not read the Foundation series, even though I'd heard about it.
[383.10 → 387.62] And soon after I joined, I asked this exact same question.
[388.28 → 390.58] And afterwards, I read the book.
[390.70 → 390.98] So.
[391.40 → 393.46] So, yeah, thanks for the question.
[393.98 → 394.42] No worries.
[394.56 → 397.72] And just for listeners, it had been a while since I'd read the series.
[397.72 → 401.40] It's a fantastic series been around forever by Isaac Asimov.
[401.52 → 410.86] And so I was just the idea there is that this figure, Harry Selden, is what's called a psychohistorian.
[411.28 → 415.90] And it's essentially evaluating society based on on on mathematics.
[415.90 → 418.60] And so they're in a galactic empire.
[418.60 → 424.38] And it's its kind of he predicts that it's about to fall, and it's going to be 30,000 years of chaos.
[424.38 → 434.86] And he uses this psychohistory analysis to figure out a way to take certain actions to narrow the chaos down to a mere millennium.
[434.86 → 438.84] And so the series is about what he does.
[438.84 → 443.44] And he creates these two foundations at each end of the galaxy filled with scientists and engineers and stuff.
[443.44 → 449.00] But just since we made the reference, I wanted to relay that to anybody who had not read the book series.
[449.00 → 458.76] Yeah. So it sounds like I mean, a kind of central piece of that story is prediction, maybe kind of bridging that gap.
[458.84 → 463.32] I'm assuming that's kind of the reason why the Selden name was chosen.
[463.32 → 470.78] But, you know, as you so kind of filling in the gaps of your story, Yanis, you came to Selden.
[470.94 → 477.24] What is Selden's relation to what they're trying to do in machine learning and A.I.
[477.24 → 483.48] and assuming it's related to that because of the name and the relation to prediction and all of that?
[484.70 → 485.38] Yeah, sure.
[485.38 → 491.68] So the Selden name is actually very fitting, as you say, because it's all about predicting the future.
[491.68 → 500.70] But what we are doing at Selden is we are doing machine learning deployment primarily.
[500.70 → 509.46] And this is everything that happens after your data scientists have finished their job and developed some models,
[509.82 → 517.54] train them and achieve good enough performance so that they're ready to go out and be applied in the business.
[517.54 → 523.08] But there 's's a lot that needs to be done for that step to materialize.
[523.08 → 526.50] So typically a data science model.
[526.50 → 535.52] Well, there's this whole setup of how you deal with the data and then the modeling scripts,
[535.52 → 539.56] which are typically Python or maybe R scripts or maybe some other languages.
[540.56 → 545.72] And after the training is done, then you have maybe some artifacts, some model weights,
[545.72 → 549.58] which you can then load again and then make predictions.
[549.58 → 558.42] But that doesn't really make it easy for people inside the business to use the model.
[558.42 → 565.04] So what needs to be typically done is productionizing the model, which would in the simplest case involve
[565.04 → 572.20] wrapping it with some light API, like a REST endpoint, for example,
[572.20 → 579.92] so that it can start living in the company's infrastructure and other business apps can start communicating with it by sending requests,
[580.06 → 583.92] getting predictions back and then those predictions being acted on.
[583.98 → 591.10] Could you extend that a bit and kind of talk about what the products that Selden has are, and what projects it's engaged in
[591.10 → 598.30] and kind of give us a sense of what your customers or users are and why they're coming to you?
[598.38 → 603.02] You know, what is it they're trying to solve when they engage in your products and projects?
[604.02 → 605.00] Yes, of course.
[605.00 → 615.94] So Selden is an open core business, meaning that our primary product, which the company is built on, is open source.
[615.94 → 621.64] It's called Selden core, and it's a machine learning deployment platform that runs on top of Kubernetes.
[622.54 → 631.38] And it basically enables people to wrap up their trade models, which can be trained using any framework.
[631.38 → 638.28] So you can be your data scientists can work in Python or R or even Java or any other framework.
[638.80 → 640.06] And then even Java.
[640.34 → 642.96] Well, yes, even if you feel like it.
[642.96 → 648.96] Yes. And because it's model agnostic, we don't get in the way of the data science modelling part.
[649.50 → 656.14] What we're interested in was once that data science part is done, you can wrap up your models into Docker images
[656.14 → 658.50] and then deploy them using Selden core.
[659.42 → 664.24] And the models will be running on Kubernetes seamlessly.
[664.48 → 666.94] And you can start using them in your business.
[666.94 → 674.08] Yeah. And I mean, so I've kind of heard of Selden like a little bit in the past.
[674.08 → 681.10] But leading up to this conversation, I tinkered around with some more of what Selden is doing and was super impressed.
[681.10 → 691.22] So much so that I'm encouraging one of the teams that I'm I'm working with to use some of this for deployments, because, you know, it was like really.
[691.22 → 703.90] So I had a model for like reading comprehension and, you know, getting that into production was as easy as writing a particular, you know, Python class with a predict function.
[703.90 → 713.26] And then and then using some of Selden's tooling to basically just specify that, hey, I want to rest API on this port.
[713.38 → 716.10] And my class is called this name.
[716.10 → 720.36] And then and then Selden kind of took care of the rest and that deployment piece.
[720.36 → 722.92] So I was super impressed with the whole workflow.
[722.92 → 724.12] And I'm sure I've missed.
[724.44 → 728.34] You can tell me what other pieces of Selden I missed.
[728.34 → 732.24] I'm sure I only touched on a little bit of what you offer.
[732.24 → 737.40] Yeah, and that's very great to hear that you are getting some value out of it already.
[737.40 → 739.20] So continuing on that.
[739.20 → 744.00] So Selden core is the open source deployment platform.
[744.00 → 761.10] And then on top of that, we are building an enterprise layer, which is supposed to make things that that little bit easier and also more accessible to people that are not necessarily that familiar with the command line.
[761.10 → 770.72] So what we envision with the enterprise option is a centralized place to monitor all your models in deployment.
[770.72 → 800.02] So both monitoring them, sending off new deployments or decommissioning old ones and having a rich interface of inspecting the models, how they're doing, and also have team collaboration and authentication of different levels of permission, who's allowed to put new models in production, who's allowed to decommission the models and that kind of that kind of stuff.
[800.02 → 822.02] Cool. And I know that Chris and I have talked several times on this show, I think, and in our conversations outside the show about this sort of weird friction that exists between engineering teams and data science or AI teams often in that, you know, the tooling that the AI people are using is really weird.
[822.02 → 828.38] In comparison to what engineering teams are used to, like, you know, what are these Jupiter things floating around?
[828.38 → 836.50] What do they do? And that creates a lot of friction oftentimes in terms of actually building value out of the AI stuff.
[836.50 → 845.78] So in terms of who's kind of latching onto this tooling that you're building, do you see kind of people coming from both of those sides?
[845.78 → 858.44] So from like maybe a DevOps side and those trying to productionize what data science teams have passed off to them and maybe, but maybe there's people also from the AI side, or what are you kind of seeing in terms of trends in that sense?
[858.44 → 888.42] Yeah, that's a very interesting question, actually.
[888.42 → 891.30] Sure.
[891.30 → 898.50] smaller companies in that regard. So in bigger enterprises, typically places like banks,
[899.06 → 904.10] there appear to be quite a lot of silos between teams. So data scientists, for example, would only
[904.10 → 910.28] be responsible for the development of models. And once they're kind of happy, then they just
[910.28 → 915.74] chuck it over the wall to the DevOps people or the engineers who actually have to put it in
[915.74 → 921.88] production. And that's not always the best way of doing things. As the data scientists then don't
[921.88 → 927.66] get any feedback on how the models are doing, and the data engineers don't get feedback about, well,
[927.80 → 933.10] how you actually, what is this thing? How do you productionize it? Whereas in smaller companies,
[933.10 → 940.32] it seems to be people are doing many, many roles at once. And this is something that when I joined
[940.32 → 946.16] at Selden last year, I also had to pick up. So instead of just doing pure data science and
[946.16 → 952.42] modelling, I had to basically had to take up the engineering best practices because we are at
[952.42 → 961.44] part an engineering company. But yeah, the people are varied. So Janice, how did Selden actually get
[961.44 → 966.62] interested in doing model inspection and interpretability? What was the motivation
[966.62 → 973.60] that drove the company in that direction? So to answer this question best, it's maybe
[973.60 → 978.84] fruitful to discuss a bit more about the capabilities of our open source deployment platform.
[979.04 → 979.90] Absolutely. Sure.
[980.24 → 986.30] So when people think about productionizing models, usually they think of single models. So you have
[986.30 → 993.74] a model, you wrap it up in a single Docker image, and then you deploy it. So if it's a TensorFlow
[993.74 → 999.34] model, maybe you use TensorFlow serving, for example. Or if it's a Python model, maybe you write a
[1000.22 → 1008.38] flask cap. And then that's kind of it. It's a single model, you send requests of data through and get
[1008.38 → 1014.86] predictions back, and then you use them in whatever way you see fit. With Selden Core, there's a lot more
[1014.86 → 1023.26] functionality that you can have. With Selden Core, we have this inference graph abstraction, which is part of
[1023.26 → 1031.74] every deployment. And it can be as simple as a single model, which is probably most use cases in the
[1031.74 → 1038.78] business. But you can do a lot more interesting things. For example, you can have several models running in
[1038.78 → 1046.62] parallel. And then you might want to make predictions using all of them. And then before returning the
[1046.62 → 1051.66] prediction, you might want to combine all of them using some custom business logic. For example, well,
[1051.66 → 1058.54] it could be as easy as majority vote, or it could be just returning all predictions. So you get
[1058.54 → 1066.54] resembling at inference time for free. Another way you can use it is instead of resembling models at
[1066.54 → 1073.58] prediction time, you can route traffic to models. So you could have, say, two models and have a router.
[1074.30 → 1079.26] It could be an A-B test, for example. If you've developed one model and then put a second one
[1079.26 → 1087.26] model in alongside it, you want to split traffic 50-50 and see which one performs best. Or you could have
[1087.26 → 1095.74] custom business logic. Maybe you have several models, and you know that one model does best at a
[1095.74 → 1101.58] particular time of day, for example. And another model does better at a different time of day. So
[1101.58 → 1110.38] that's kind of domain expertise that can be coded into the routing. Or similarly, if it's, for example,
[1110.38 → 1116.46] a recommendation use case, maybe you have a couple of models and some of them do better on certain
[1116.46 → 1121.98] demographics than... and some of them do better on other demographics. And then you can code that into your
[1121.98 → 1129.50] custom business logic router as well. So you can do quite a lot of interesting things with Selden
[1129.50 → 1138.38] Core beyond single model serving. Yeah, so in terms of the... so you just recently, you know,
[1138.38 → 1143.42] released and are promoting this Alibi project, which it's described as being concerned with model
[1143.42 → 1149.66] inspection and interpretability. So is the kind of... I've heard of interpretability in terms of
[1149.66 → 1156.62] kind of interpreting individual models, maybe sort of black box models that you try to gain some
[1156.62 → 1161.18] insight into. But then what is the difference when you're meaning kind of model inspection versus
[1161.18 → 1166.22] model interpretability? Does inspection have to do with this kind of routing logic and where things
[1166.22 → 1172.38] act... like which models actually got used for a particular prediction? Or what's the difference there
[1172.38 → 1181.26] and the distinction? Yeah, so that's a very good question. So when engineers talk about monitoring
[1181.26 → 1187.82] live systems, then they typically think of things like, for example, requests per second and the total
[1187.82 → 1193.98] load on the nodes that the models are living on and that kind of stuff. But when you're approaching the
[1193.98 → 1200.38] question of monitoring machine learning models from a data science perspective, then there are a lot of
[1200.38 → 1206.06] very interesting and useful things that you might want at inference time rather than just raw predictions.
[1206.06 → 1213.98] So, and this is what I sort of mean about monitoring and interpreting machine learning models. So just to
[1213.98 → 1220.62] give you a few examples. So one is, we've already touched upon it, and we'll go into detail, is about
[1220.62 → 1228.14] model explanations. So you might want to go through your request logs historically and see, okay, well,
[1228.14 → 1236.38] why did this model make this particular prediction on this particular instance? And you could have a
[1236.38 → 1244.30] component in the Selden core graph that is a model explainer, and then you can basically send that historic
[1244.30 → 1251.50] request through and get a model explanation back as to roughly the logic that it took at that particular time.
[1251.50 → 1261.34] Other use cases are, you might be interested in whether your data distribution is evolving in time. So if it's
[1261.34 → 1269.02] changing, your model might become stale, and then you might want to flag it for retraining or decommissioning. So
[1269.02 → 1278.22] you would use components that do outline detection on the data or more generally concept drift on the data. So if your data
[1278.22 → 1284.94] distribution is constantly changing over time to create those alerts and those can all be part of your
[1284.94 → 1287.10] deployment, of your Selden deployment.
[1287.10 → 1292.46] So what does the tooling look like for these sorts of things? I mean, obviously it sounds like,
[1293.34 → 1296.70] you know, I know we're about to get into Alibi, and it's probably leading the way, but could you kind
[1296.70 → 1303.58] of describe the landscape of tooling and, you know, is it custom logic in many cases, or how are people
[1303.58 → 1308.62] dealing with things if they're not using Alibi? Yeah, that's actually quite a broad question. And
[1308.62 → 1313.90] in my mind, I always split these sorts of questions into two parts. There's really the
[1314.62 → 1319.90] there's the engineering part and then there's the data science part. And on the engineering side,
[1319.90 → 1329.98] it really is about, okay, how do we, what sort of components do we need that will talk to a model
[1329.98 → 1337.02] in production and how, how will that look inside say the, the Selden deployment inference graph?
[1337.02 → 1341.74] And maybe sometimes these components need to be stateful as well, which complicates things.
[1342.70 → 1349.18] And then on the data science part, it's about, it's less about the engineering of these components,
[1349.18 → 1354.70] but more about the algorithms. So what do you actually use if you want an outlier detection running
[1354.70 → 1360.70] alongside your model and detect, detecting anomalous data instances? So, so that's, that's the really
[1360.70 → 1366.94] the data science piece. And we've done some work specifically on outlier detection for Selden core,
[1366.94 → 1375.26] and we have examples on our GitHub about that. And with Alibi, we're sort of doing more, but more in the
[1375.26 → 1383.42] direction of model explanation. Yeah. So maybe just describe it as I'm thinking about like, so I'm thinking
[1383.42 → 1390.22] about like Selden core and how it gives you these deployments, which might be like one model or
[1390.22 → 1396.14] multiple models tied together with business logic. Let's say I'm already using Selden to do those sorts
[1396.14 → 1404.86] of things. So how does Alibi fit into that? Is it like a component that's kind of like a library that you
[1404.86 → 1410.30] call from like within those components? Is it kind of something that runs on the side and reaches out
[1410.30 → 1416.22] to those things and tells you certain things or, or analyzes logs? Like what is the how does it kind
[1416.22 → 1424.94] of operate within this, within this ecosystem? Yeah, good question. So, so with Alibi specifically,
[1426.14 → 1435.50] so we got interested in model explanation as, as a company maybe around about four months ago,
[1435.50 → 1442.30] and we sort of thought, well, okay, it would be good to support model explanations for model,
[1442.30 → 1448.06] for deployed models in our enterprise product. And then, so on the data science team, we did,
[1448.06 → 1454.62] we did a bit of research of what kind of techniques are out there. And in the academic literature,
[1454.62 → 1459.98] there's actually a lot, a lot going on. And there's a whole host of things that you could try
[1459.98 → 1466.38] to try and interrogate what your model was doing. But when it came to the open source code, it's mostly
[1466.38 → 1474.94] research code. So it's, it's not easy to use. So what we decided is that if we want to approach this
[1474.94 → 1483.58] seriously, then, and basically we need to recreate some of those algorithms. And so Alibi was born as an
[1483.58 → 1490.86] open source Python package for some of the, the more famous or well-known algorithms for model
[1490.86 → 1497.26] explanation. So it's, it's a completely standalone library. So you don't need to be interested in
[1497.26 → 1502.62] model deployment or any kind of product ionization to try and use it. And you can use it in a, in a
[1502.62 → 1507.58] Jupyter notebook. You can play around with some models that you've trained in the same notebook and see,
[1507.58 → 1514.70] see what kind of explanations your models can offer on the decisions that they made. But the
[1514.70 → 1521.18] the way that it ties in together with, with Selden core and eventually Selden deploy, which is the
[1521.18 → 1528.22] our enterprise layer is that it will be the backend for producing these explanations of, of your models
[1528.22 → 1529.50] that are running in production.
[1529.50 → 1544.14] The data engineering podcast is a weekly deep dive on modern data management with the engineers and
[1544.14 → 1548.38] entrepreneurs who are shaping the industry. Go behind the scenes on the tools, techniques,
[1548.38 → 1553.50] and difficulties of data engineering. So you can learn and keep up with the knowledge to make you and
[1553.50 → 1558.86] your business successful. Can you give a bit of an outline about the motivation for choosing
[1558.86 → 1562.30] Jupyter Notebooks in particular as the core interface for your data teams?
[1562.30 → 1567.34] Yeah. And actually, uh, when I first joined, uh, Netflix, it was sort of tossed at me, and I was
[1567.34 → 1570.70] definitely like, well, are we crazy? And the answer was like, we might be a little crazy.
[1570.70 → 1577.50] Go to dataengineeringpodcast.com to listen, subscribe, and share it with your friends and colleagues.
[1589.50 → 1596.22] So I noticed on the Alibi website, uh, you, you note that Alibi provides, and this is kind of the air
[1596.22 → 1603.34] quotes here, consistent API for interpretable email methods. And so, you know, what's in that API and
[1603.34 → 1608.30] is it an API that's used during training or testing or, or what other, what other scenarios are you,
[1608.30 → 1609.18] are you there for?
[1609.18 → 1616.38] Yeah. Well, API is maybe a bit of a grandiose term. Uh, it literally, uh, refers to, to the way we've
[1616.38 → 1621.58] structured these, uh, these various kinds of, uh, explanation algorithms within the library.
[1621.58 → 1627.74] So it's as simple as, uh, so you could, you could think of it in terms of the scikit-learn API,
[1627.74 → 1633.82] which we all know, which is, which, which typically has two steps for any given, uh, model or estimator.
[1633.82 → 1639.50] You have the fit step, which takes in a training set, and then, then you have the prediction step.
[1639.50 → 1646.30] So you can, you can, uh, make predictions on new instances, uh, and with, uh, model explanations,
[1646.30 → 1651.90] it's, it's, it's a reasonably similar process, actually. So, so some explanation methods require
[1651.90 → 1658.06] access to the training set to be useful. So you would have a similar fit step, uh, not always, but
[1658.06 → 1665.02] in some methods, and then really explanation time explanation, almost exactly maps to to predict,
[1665.02 → 1670.94] uh, steps. So you would have, uh, rather than model dot predict, you would have an explainer dot explain
[1671.34 → 1677.74] and pass in a single instance that you want to be explained, uh, why the model made the prediction
[1677.74 → 1683.74] that it did. Cool. Uh, is this kind of model agnostic in the same way that, you know, seldom
[1683.74 → 1689.34] deployments are in the sense that if you want to use TensorFlow or PyTorch or whatever, um, then you,
[1689.34 → 1694.38] these things kind of work out of the box, or is this kind of restricted to particular,
[1694.38 → 1700.06] like reference implementations or that sort of thing? Yeah, that's a very good question to ask.
[1700.06 → 1706.54] Um, so in the first iteration of Alibi, uh, we're now in version two, but we're still
[1707.26 → 1713.26] mostly focusing on what we call black box explanation methods. So, and when I say black box,
[1713.82 → 1718.30] I don't mean a complicated neural network that you've created. What I mean is that all you have
[1718.30 → 1723.98] is access to a predict function and this can be very general. It can be, it can be, uh,
[1724.62 → 1729.82] literally something that just takes in arrays and, and, and spits out other arrays. So it can be,
[1730.46 → 1737.66] it can be as general as a as an API, uh, that's already sort of running in production. So, uh, so we
[1737.66 → 1744.62] have a couple of methods in Alibi that all work on these sorts of black box, uh, black box models. So it's,
[1744.62 → 1751.66] it's, uh, it's very portable. We, we do have in our roadmap more, uh, model specific methods, because once,
[1751.66 → 1757.74] once you start to know a bit more about what your model actually is, then, then you have a lot more
[1757.74 → 1762.46] leeway and a lot more interesting methods as well that you can apply if you, if you know the model
[1762.46 → 1768.94] architecture or, uh, or the loss function, for example. So, uh, now that we've kind of talked a
[1768.94 → 1775.34] a lot about what Alibi is in general, what the API is like and how you integrate it into your workflow.
[1775.34 → 1781.02] Um, I'd be interested because we've talked about, you know, model interpretability in general on,
[1781.02 → 1787.34] on this, uh, show before, but I'd love to dive into a few more specifics because this is, you know,
[1787.34 → 1793.66] really a practical project that people can use. So one of the things that you talk about, so you talk
[1793.66 → 1798.46] about a lot of different methods, um, maybe one that we could start with is you talk about anchors
[1798.46 → 1803.98] and anchor explanation. Um, could you kind of describe what, what that is in general and when
[1803.98 → 1810.54] it might be useful? Uh, yeah, sure. And, uh, just, just before I dive into the anchor method in particular,
[1811.18 → 1818.38] um, I just want to pick apart a bit what, what, what we really want from model explanations, right? So,
[1818.38 → 1822.94] yeah, that'd be great. So, so there's, there's, there's sort of a couple of different notions of,
[1823.50 → 1830.30] uh, model explanation. Um, in particular, people talk about global explainability where you
[1830.30 → 1835.98] typically want to know how the model performs sort of on average, say on the whole,
[1835.98 → 1840.62] whole of training set to try and draw some conclusions from it. Um, and then there's the
[1840.62 → 1846.94] local explanation, which, uh, is, uh, uh, which has been the focus of Alibi in the first few releases,
[1846.94 → 1852.70] uh, which is, uh, answering the question given a specific instance and a model prediction.
[1853.10 → 1858.06] Why did the model make this prediction? Uh, but, uh, as you can already tell that this,
[1858.06 → 1862.38] this question is not well-defined. I mean, you can't really answer it. Why, why the model made
[1862.38 → 1867.58] the prediction? You need to try and pick it apart a bit more. So, so one thing you can do is you can
[1867.58 → 1874.94] try and ask human interpretable questions, what that you would like about this model decision, uh, to be
[1874.94 → 1880.46] answered. And then given those questions, you can, you can try and find algorithms that sort of
[1880.46 → 1886.94] approximate the answers to those kinds of questions. So, so for example, um, you might ask,
[1886.94 → 1893.66] okay, given this instance and this prediction, what is sort of a minimal subset of features and their
[1893.66 → 1899.82] values, uh, given which the model will make the same prediction regardless of everything else.
[1899.82 → 1904.38] So that's, that's what we call an, an, an anchoring question. So that's where the
[1904.38 → 1910.38] anchor technique comes in. So you ask an interpretable question, and then you go ahead
[1910.38 → 1913.02] and see, okay, how can I write an algorithm to do this?
[1913.02 → 1919.74] So in that case with the anchor explanation is like, what's the sort of, uh, how would you kind
[1919.74 → 1924.94] of phrase these, these anchor questions, I guess, or what would be the, the thing that you would be
[1924.94 → 1930.14] looking to come out of alibi that would help you kind of with that explanation or, or make that,
[1930.14 → 1936.06] um, explanation, uh, logically. Um, so, so the great thing about this is that these interpretable
[1936.06 → 1941.42] questions are asked when you want to design a new explanation method, but once the method is,
[1941.42 → 1945.90] is, is, is designed, you only need to be aware of what question that method is answering.
[1945.90 → 1953.90] So, um, so the anchors' method would return say a small subset of features of the original instance
[1953.90 → 1960.14] and their values, which would, uh, result in the same model prediction, say 95% of the time.
[1960.14 → 1966.38] So let me just give you a quick example. Uh, one example that we also have on the, on the website.
[1966.38 → 1973.82] So it's the, um, sort of semi-famous, uh, census, uh, income data set, uh, from the early nineties
[1973.82 → 1980.46] composed in the U S, and it's, it's a binary classification problem of predicting whether a
[1980.46 → 1987.34] given individual will be, uh, a low income individual or a high income individual. And the threshold is, uh,
[1987.34 → 1994.86] whether they make, uh, less than or more 50, more than $50,000 a year. So, and, and the, the various
[1994.86 → 2002.38] features of each individual are their, uh, education level, their occupation, their relationship status,
[2003.10 → 2008.22] um, but also their gender and race and, um, various kinds of other features. So,
[2008.22 → 2014.62] so it's, uh, it's a fairly standard setup. You've got tabular data, and can train a binary classifier
[2014.62 → 2022.30] to, to, to solve this problem. So once you have your classifier trained, you can then pick individual
[2022.30 → 2029.02] instances and run the anchor algorithm to try and find for each instance, which, which really are the
[2029.02 → 2034.86] pertinent set of or subset of features that were important for this particular prediction.
[2034.86 → 2045.18] So for example, I, I might pick a, uh, say, uh, a woman who's, uh, mid-thirties, who's been separated
[2045.66 → 2053.50] and maybe her profession is, uh, working in the government and I, I run the model, and it says,
[2053.50 → 2059.58] okay, it's a it's a lower income individual. Then I run the anchor explanation and what I get out is,
[2059.58 → 2067.50] okay, my anchor for this explanation is that their marital status is separated and their work
[2067.50 → 2073.42] category is government work. And with those two present, the model will make the same decision
[2073.42 → 2078.22] 95% of the time, regardless of all the other features. So that's where the name anchor comes
[2078.22 → 2084.38] from. It anchors this decision to, to really what makes, what makes the most, uh, importance for this
[2084.38 → 2085.98] particular, uh, individual.
[2085.98 → 2091.50] So wondering if you could, uh, kind of tell us a little bit about maybe a different method that
[2091.50 → 2095.74] you've implemented that might be useful in a different situation or, or possibly in the same
[2095.74 → 2098.30] situation differently. I don't know if that made a lot of sense, but.
[2098.30 → 2104.94] Um, yeah, sure. So, uh, I can, I can talk through another, uh, method or, or rather a couple of methods
[2104.94 → 2112.38] that we have in Alibi. Um, so when we first kicked off Alibi, we, we sort of wanted to implement methods
[2112.38 → 2117.42] that didn't really have good implementations, but that were interesting and had received
[2117.42 → 2123.82] attention in the academic community. So, so anchors is one such method. Um, and, uh, actually it was,
[2123.82 → 2130.22] it was, it was, uh, I'm not sure if, if you know, it was designed by, uh, by the same people behind
[2130.22 → 2137.26] Lime, which, uh, sort of kicked off the whole interpretability, uh, of machine learning, uh, area.
[2137.26 → 2142.06] Yeah. That's the, uh, I'm trying to remember as the one that kind of, uh, gives you linear
[2142.06 → 2146.86] estimations of certain, uh, relationships or, or, or something like that.
[2146.86 → 2152.14] Yeah. So what Lime does it, it kind of fits a surrogate model, uh, a linear surrogate model
[2152.14 → 2157.74] around the, around the instance. It's basically trying to approximate the non-linear decision
[2157.74 → 2163.42] boundary with, uh, with a linear one. So it, and, and then the weights of that linear model can
[2163.42 → 2169.58] get interpreted as, as, as, uh, feature importances. So, so it was, uh, it was sort of, uh, it's sort
[2169.58 → 2174.30] of a very familiar technique, but it has its, uh, its shortcomings. And then the authors of the
[2174.30 → 2181.10] of Lime, um, came up with anchors, which they feel is, is sort of a better, better solution for
[2181.10 → 2187.10] this problem. Cool. So we've talked about the, the anchor explanation, you list a few different
[2187.10 → 2191.42] methods. Like you were saying, there are multiple methods that are implemented in Alibi. There's,
[2191.42 → 2196.38] you know, the trust scores and counterfactual instances and other things, but I was wondering,
[2196.38 → 2201.26] maybe, maybe as we kind of move towards the end of our, of our conversation here,
[2201.26 → 2207.82] if you could just give us a little bit of an idea of, you know, where Alibi is, is heading and,
[2207.82 → 2214.38] and maybe also like what, what Selden has in mind kind of for the, for the future of Selden core and
[2214.38 → 2221.26] Alibi and maybe, maybe other things like, where are you headed? Um, yeah. So for Alibi, we have a reasonably,
[2221.42 → 2228.30] ambitious roadmap. I mean, I mentioned sort of our API mimics the scikit-learn API, but for, uh,
[2228.86 → 2234.06] for model explanation. So we, we kind of in an ideal world, we would be the scikit-learn of model
[2234.06 → 2240.38] explanations, bringing, bringing various techniques together in one place, uh, for people to, to use
[2240.38 → 2246.30] and compare and contrast what makes sense for the use case. So other than that, uh,
[2246.30 → 2251.66] So that would be like, like scikit-learn you can, you know, if you're wanting to do classification,
[2251.66 → 2257.50] you can choose from any of, you know, whatever it is. I actually don't know how many, like 20 or 30 or
[2257.50 → 2263.74] whatever, uh, implemented, uh, methods for, for classification. So you're kind of imagining Alibi
[2263.74 → 2270.78] would kind of have that zoo of explainability methods that you could kind of call using a standardized
[2270.78 → 2276.06] API. Is that, is that kind of the thought? Uh, yeah, yeah. That's kind of our, our ambition
[2276.06 → 2282.94] with, with Alibi eventually. Cool. Cool. Yeah. What about, um, you know, Selden, uh, Selden in general,
[2282.94 → 2287.10] are there, are there other things on the, on the horizon that you can share or, or maybe just things
[2287.10 → 2291.18] that you're excited about in the AI community or at Selden specifically?
[2291.18 → 2297.42] Yeah. So, so I'm not sure if you're aware, but this week is actually the, uh, the, uh,
[2297.42 → 2304.70] COAX event, uh, here in London, which is the sort of festival of AI where, uh, lots of companies
[2304.70 → 2312.22] sort of go in and, uh, and present the sort of emerging technology to, to facilitate all kinds of,
[2312.22 → 2316.46] um, machine learning use cases in the industry. So what we're actually,
[2316.46 → 2324.38] uh, doing that this week is we're demoing a sort of first, uh, sort of version of our enterprise,
[2324.38 → 2331.74] uh, product Selden deploy, which, which has also anchored explanations running with a live request.
[2331.74 → 2336.46] So that's, that's, that's kind of quite exciting from a product development perspective.
[2336.46 → 2341.66] So I guess as you are, are looking at that, is that, I'm just, I was curious with that particular,
[2341.66 → 2346.38] uh, event, is that, uh, is that more of a conference or is it more of, um,
[2346.46 → 2351.26] kind of companies coming together to just demo their, their thing? What, what, what style of
[2351.26 → 2355.34] event is it? And is this kind of, are you essentially taking the opportunity to announce
[2355.34 → 2358.62] new product, uh, features in that with, with the one that you just talked about?
[2358.62 → 2364.86] Um, yeah, so it's, it's, it's, it's kind of a bit of both. There are speakers, mostly industry speakers,
[2364.86 → 2371.50] but, but it's also, uh, so companies have their own stands where they can demo their technology and
[2371.50 → 2377.82] and that kind of stuff. So, um, I expect that to be fewer people from this sort of pure machine
[2377.82 → 2383.34] learning research community, especially as it also coincides with, uh, ICML this week.
[2383.34 → 2387.98] Cool. And, uh, I mean, first off, congrats on the, the announcement. That's really,
[2387.98 → 2393.58] it's really exciting. Uh, I can't wait to see, uh, what's next and the hype around, around that for
[2393.58 → 2398.62] sure. Um, but, uh, let's say people, um, are listening to the podcast. They want to,
[2398.62 → 2403.98] you know, get hands on with Alibi and or Selden core and or Selden enterprise. What,
[2403.98 → 2409.98] what are the best ways for people to kind of, uh, get, get up and running with Selden or,
[2409.98 → 2413.26] or Alibi? Where can they, where can they find resources and get help?
[2413.26 → 2419.74] Um, yeah, probably the best resources are, is our docs. So you can just go on docs.selden.io,
[2419.74 → 2426.06] and that will take you to the relevant documentation, either for Alibi or for Selden core, whichever
[2426.06 → 2430.46] takes your, takes your fancy. So it has, uh, it has a lot of information to, to get you up and
[2430.46 → 2435.82] running. Cool. And do you have any, um, uh, no worries if, if you don't, but as you've kind of
[2435.82 → 2441.82] explored this whole area of, you know, interpretability and explainability, um, do you
[2441.82 → 2447.42] have any recommendations maybe for people that are interested in learning more about that subject in
[2447.42 → 2453.18] general, as far as resources where they could learn about what has been done or what people are
[2453.18 → 2457.26] researching? What's, what's the best way to find those, that sort of information?
[2457.26 → 2463.98] Um, yeah. So one thing I can definitely recommend and something that we kind of got a lot out of
[2463.98 → 2469.82] when we were first developing Alibi is Christoph Moldau's book on interpretable machine learning.
[2469.82 → 2475.10] So it's, as the title says, it's about, it's a book about interpretability techniques, and it's, uh,
[2475.10 → 2479.82] it's fully open source. It's available online, and it's, it's really well written. So if people want
[2479.82 → 2484.06] to get into the topic, then I think that's the best, best place to start by far.
[2484.06 → 2489.98] Awesome. Well, uh, thank you so much for, for joining us today. I know I'm excited to,
[2490.62 → 2496.70] to dig in more to Selden and to, to Alibi. Now I understand a lot more about kind of how,
[2496.70 → 2502.70] how it fits into my, into my workflow. Um, I encourage people if you have, uh, questions about,
[2502.70 → 2507.98] uh, or, or thoughts about Alibi or, or Selden, of course they have their, uh, Slack channel,
[2507.98 → 2513.74] but we also have our, um, practical AI Slack channel, um, which you can find at changelog.com
[2513.74 → 2519.26] slash community and our LinkedIn page as well. Um, if you just search for practical AI. So we'd love
[2519.26 → 2524.94] to hear your thoughts on, uh, machine learning, interpretability and inspection. Um, really
[2524.94 → 2530.14] appreciate, uh, really appreciate you joining us, uh, Janice and hope to stay in contact and really
[2530.14 → 2535.90] looking forward to seeing what, what Selden, uh, does in the future. Um, yeah, thanks very much for
[2535.90 → 2542.06] having me on the show. And I would just like to quickly thank my coworkers, Arno van Levered and
[2542.06 → 2549.10] Giovanni Vacant, who both are working on the Alibi project and without whom I haven't done the work.
[2549.10 → 2553.74] Awesome. Appreciate that. And, uh, I, I really hope that we can run into you at a
[2553.74 → 2558.30] at a conference sometime and, and, uh, and catch up. Thank you so much for joining us.
[2558.30 → 2559.58] Okay. Great. Thank you.
[2559.58 → 2566.30] All right. Thank you for tuning into this episode of practical AI. If you enjoyed this
[2566.30 → 2570.86] show, do us a favour, go on iTunes, give us a rating, go in your podcast app and favourite it.
[2570.86 → 2574.46] If you are on Twitter or social network, share a link with a friend, whatever you have to do,
[2574.46 → 2578.46] share the show with a friend. If you enjoyed it and bandwidth for changelog is provided by
[2578.46 → 2583.50] Vastly learn more at fastly.com, and we catch our errors before our users do here at changelog because of
[2583.50 → 2589.42] roll bar, check them out at robot.com slash changelog. And we're hosted on Linde cloud servers.
[2589.42 → 2594.78] Head to leno.com slash changelog. Check them out, support this show. This episode is hosted by
[2594.78 → 2600.46] Daniel Whiten ack and Chris Benson. The music is by Break master Cylinder, and you can find more shows
[2600.46 → 2606.14] just like this at changelog.com. When you go there, pop in your email address, get our weekly email,
[2606.14 → 2611.58] keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2611.58 → 2613.58] Thanks for tuning in. We'll see you next week.
[2619.42 → 2621.42] Bye.
