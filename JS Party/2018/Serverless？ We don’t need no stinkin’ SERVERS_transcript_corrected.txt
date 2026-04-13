[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com, and we're hosted
[11.42 → 17.26] on Linde servers. Head to linode.com slash Changelog. This episode is brought to you by
[17.26 → 21.98] Gauge. Gauge is a free and open source test automation tool by ThoughtWorks with a goal
[21.98 → 26.58] of taking the pain out of test automation for acceptance tests. To help with this,
[26.58 → 30.74] Gauge supports specifications and markdown, which are easy to read and easy to write.
[31.12 → 36.66] Reusable specifications to simplify your code, which makes refactoring easier and less code
[36.66 → 42.48] means less time maintaining your code. And finally, integrations. Use Gauge with your favourite
[42.48 → 50.02] tools and IDEs in the ecosystem of your choice, like Selenium and Sari Pro. CI and CD tools like
[50.02 → 56.38] Good, Jenkins, Travis, and IDE support for Visual Studio, VS Code, IntelliJ, and more.
[56.58 → 61.04] The team behind Gauge believes in using web technology to test web applications.
[61.60 → 69.08] Head to gauge.org slash JS Party to learn more and give it a try. Once again, gauge.org slash JS Party.
[69.08 → 89.42] Welcome to JS Party, a weekly celebration of JavaScript and the web. Tune in live on Thursdays at 1pm
[89.42 → 95.84] Eastern, 10 a.m. Pacific at changelaw.com slash live. Join the community and Slack with us in real time
[95.84 → 102.62] during the show at changelaw.com slash community. Follow us on Twitter. We're at JSPartyFM. And now on to the show.
[102.62 → 111.18] Hello and welcome to another week of JS Party, where every week we are throwing a party about
[111.18 → 116.16] JavaScript and the web. I'm your host for this week, Ball, and I'm joined with our regular
[116.16 → 123.50] panellists, Nick Needed. Hello. And Christopher Hitler, aka Bone skull. Hello. I love that moniker.
[123.72 → 129.62] We also have a special guest with us today. Jeremy Daly is joining us. He is the CTO of Alert Me. News
[129.62 → 134.74] and a longtime advocate of serverless, which will be our topic for the day.
[134.94 → 140.06] Hey guys, thanks for having me. Thanks for joining us, Jeremy. So let's kind of kick things off with
[140.06 → 145.84] a question, which is what the heck is serverless? Because I mean, just coming at this longtime guy,
[145.92 → 150.80] like obviously there's still a server involved, right? There is. Yeah. So it's sort of one of those
[150.80 → 156.08] things where a lot of people, I don't want to say get upset, but a lot of people, you know, use the
[156.08 → 160.80] semantics of the term to kind of argue against it, which is kind of silly because if you think about
[160.80 → 165.22] wireless technology, and I know this is used multiple times, but there's still wires in
[165.22 → 170.94] wireless technology. It's just you as the end user don't have to deal with those wires. And so I like
[170.94 → 175.40] to look at serverless similar to that, where obviously there are servers behind the scenes that
[175.40 → 180.86] are doing things, but you as a developer, you don't have to worry about provisioning servers. So
[180.86 → 186.26] the difference between provisioning something like an EC2 instance, for example, where you have to
[186.26 → 191.10] launch that, you have to pay for it 24 hours a day, you have to install the updates, you have to worry
[191.10 → 195.24] about all the permissions and everything that's going on there. With serverless, you actually just
[195.24 → 202.48] write some code, and you tell AWS or Google Cloud Platform or whoever to say, hey, when this particular
[202.48 → 208.58] thing happens, I want you to take it in, run my code, and then spit something back out. So you're only
[208.58 → 213.66] paying when your code is actually executing, and you don't have to worry about having that,
[213.84 → 216.04] all those servers backing that for you.
[216.66 → 221.12] Yep. That makes a ton of sense. I've heard it described also as kind of functions as a service.
[221.36 → 225.14] We've gone from all these different layers, but if I just have my functions.
[225.62 → 228.88] Yeah. Well, so just something about functions as a service. So functions as a service,
[229.22 → 235.10] sometimes people equate those to serverless, and it's not, functions as a service is part of
[235.10 → 239.54] serverless. I mean, that's why we look at serverless. Sometimes people call it service
[239.54 → 244.60] because the idea is to say that, yes, functions as a service are these little containers that will
[244.60 → 249.00] run for you. They'll execute your code. You don't have to worry about it, but then you need to
[249.00 → 252.82] interact with other services in order to make something valuable happen. So whether you're
[252.82 → 257.88] writing to a database or you're writing to some sort of stream, or you're reading information in
[257.88 → 261.66] from something, there are a bunch of other services that are involved there. But again,
[261.66 → 267.34] those are all managed services. So sometimes people say functions as a service kind of acts
[267.34 → 271.90] as the glue that kind of sticks all that stuff together, but it does go beyond just the function
[271.90 → 276.58] aspect of it. How does this term differentiate from microservices or is this just a way to
[276.58 → 281.88] facilitate microservices? So that's actually kind of interesting where serverless takes us and
[281.88 → 286.44] without getting maybe too deep. So microservices obviously are taking a larger application,
[286.88 → 291.42] finding the seams in it and splitting it up so that your billing service is separate from
[291.42 → 296.16] your catalogue service or something like that. So serverless is a way in which you can deploy
[296.16 → 300.86] microservices, and you can certainly take a number of functions or a single function with some
[300.86 → 305.92] additional managed services and create a microservice there. And of course, it's much easier to communicate
[305.92 → 312.98] between functions using something like Lambda, for example, because you can call them from each other.
[312.98 → 317.82] But the difference between microservices is that microservices are sort of monolithic
[317.82 → 323.50] applications in themselves. So they're not distributed, and they usually have to be replicated either
[323.50 → 328.10] horizontally, or you've got to up the server requirements in order to get more performance
[328.10 → 334.32] out of them. Whereas with something like serverless, there's this new concept of nanoservices where you're
[334.32 → 340.00] basically saying parts of my microservice might need to scale more than other parts of it. So maybe I have
[340.00 → 345.24] an image processing component or some sort of machine learning component, and that requires more
[345.24 → 351.58] resources in order to process that. If I had all of that package into a single microservice in like a
[351.58 → 356.40] container, for example, I would have to scale the entire container. So all parts of that application
[356.40 → 360.94] would have to scale, or that service would have to scale in order to handle it. Now with this idea of
[360.94 → 366.20] nanoservices, you can take that microservice, put it out there in a serverless environment, and then
[366.20 → 371.46] when an individual component of that microservice needs to scale, that's where we sort of consider those
[371.46 → 376.28] nanoservices and those can scale just independently, even though they're part of that larger service.
[376.76 → 382.32] I think you just blew my mind with this nanoservices thing. Either that or I'm just horrified. But
[382.32 → 387.14] basically, so you're saying that we have these microservices and basically what they're doing is
[387.14 → 390.36] they're calling out to functions as a service?
[390.80 → 396.02] Well, yeah. So, I mean, a microservice, if you think about it, is just a small monolithic
[396.02 → 401.50] application, right? So it does something specific. It's your billing service. So it keeps the ledger,
[401.66 → 407.40] it creates invoices, it does all that kind of stuff. So you can build a series of individual
[407.40 → 412.50] functions. So rather than having that all in one big Java app or PHP or whatever you use,
[412.64 → 417.06] Node, if you're writing a Node, whatever, that rather than having that all in one giant function or
[417.06 → 423.40] one giant app, you can split that up into individual functions. And again, functions is probably the wrong
[423.40 → 428.72] term here because a function in serverless could run multiple subroutines if you want to think about
[428.72 → 432.66] it that way. So it's like functions within functions. But the idea is a function is this
[432.66 → 438.68] individual unit that can execute any amount of code on its own. So you take five or six functions or
[438.68 → 444.54] whatever it is, and that can be your entire billing service. And so that you sort of consider your
[444.54 → 451.38] microservice. But you don't have to launch that microservice into a container or onto a server.
[451.38 → 456.82] You launch all of those components of the microservice independently into the serverless
[456.82 → 463.44] environment like Lambda or Our or something like that. And now those all act as one service.
[463.54 → 468.30] They can communicate with one another, but then they can also scale individually. And then,
[468.40 → 472.14] of course, you can communicate across other services using, you know, whether they're messaged
[472.14 → 478.98] buses or SQS or SNS or Lambda or, excuse me, or Kinesis or any of those things to actually
[478.98 → 485.00] communicate between not only your individual services, your individual functions, but also
[485.00 → 487.84] the larger microservices, if that makes sense.
[488.50 → 492.54] So we had this evolution where we had this monolithic application, which was like all the
[492.54 → 498.38] things are in one bundle. And that turned out to be hard to scale from both a technical
[498.38 → 504.54] perspective of this is a very expensive thing that we need to put more servers on. And if one piece
[504.54 → 509.82] needs to scale, we scale it all. And also from kind of management perspective of like teams working
[509.82 → 513.84] on different pieces. So then we split that, and we said, okay, now we're going to go to microservices
[513.84 → 520.12] where each one of this sort of vertical slices can scale independently, and it can scale,
[520.24 → 522.46] have a different team, but it can also have different services.
[522.46 → 530.68] And what I'm hearing from you now, Jeremy, is this idea of serverless is taking that final
[530.68 → 534.84] thing and saying, you know what, maybe a microservice is the wrong concept because that's
[534.84 → 541.12] still like at the level of here's a self-contained thing. It's just, we've sliced it apart. What if we
[541.12 → 545.50] just take any piece of functionality and split that out and let that scale independently and be worked
[545.50 → 551.96] on potentially independently and just kind of go all the way down to the bare atoms that we're making
[551.96 → 556.14] up our program and have each of those independent? Is that a fair assessment?
[556.48 → 559.70] I think that's actually a great way to look at it. The only thing I would add to that is, and again,
[559.74 → 564.74] this is probably more confusing because of the implementation than it is from actually doing
[564.74 → 570.48] it in practice. But typically with a microservice, you'd have a small team own a microservice all the
[570.48 → 575.34] way, everything from the database to the code, you know, to the implementation. So, and that's still
[575.34 → 581.58] possible here. It's just that there's no sort of application level division or microservice division
[581.58 → 588.98] when you put functions, like I'll use AWS Lambda, for example, when you upload five functions that
[588.98 → 593.96] you say are part of this microservice into AWS Lambda, they just go into one big giant list
[593.96 → 599.44] of functions that are available, but you can tag those functions and AWS actually just launched
[599.44 → 603.66] their applications tab, which tries to kind of consolidate functions that are part of the same
[603.66 → 609.56] service. But what you would do is your microservice team that's working on, again, to go back to the
[609.56 → 613.84] example of the billing function, you might be working on five functions, plus you have an RDS
[613.84 → 621.38] Aurora database that backs it. You would want those functions to be sort of contained in a sense that
[621.38 → 625.02] one team would manage them. You'd probably put them into one Git repository or something like that.
[625.26 → 629.20] And all the interaction with that billing database would happen from those five functions.
[629.56 → 635.48] But you then upload those five functions that can scale independently. But the idea is that you might
[635.48 → 639.82] have other teams that are uploading other functions, but your microservice team would own those five
[639.82 → 644.30] functions in the database and anything else that supports it. So would you build the functions that
[644.30 → 650.24] manage your database connections or talking to the specific database? And then would other functions
[650.24 → 655.16] talk through that? Or would they somehow have... How would you share functionality between that if,
[655.52 → 657.88] say, another set of functions needed to communicate with that database?
[658.24 → 662.16] Yeah, no, that's a great question. And that's what I was trying to kind of get the point across.
[662.16 → 666.94] So if you build a function that is sort of the gateway into your billing function,
[667.30 → 671.68] you would want other services to communicate with that function. Now you can communicate with
[671.68 → 677.02] it directly without ever having to leave the environment. You could put an API gateway in
[677.02 → 682.88] front of it so that it could actually be accessible using like a REST API. But the point is, is that if you
[682.88 → 687.96] have your catalogue service and your catalogue service needs to get some sort of billing information,
[687.96 → 693.42] you wouldn't write any of your functions in the catalogue service to access the database that
[693.42 → 699.08] supplies information to the billing service. Instead, you would use, you would communicate with
[699.08 → 704.02] a function in the billing service that would then communicate with the database. So that way you can
[704.02 → 709.02] keep those separations of concerns. And then you don't have to worry about, you know, one team trying
[709.02 → 713.08] to share a database or two teams trying to share the same database. Interesting.
[713.08 → 718.14] So typically what you would do for a microservice, it's just, it's just the it breaks down into
[718.14 → 722.74] these NATO services now, which it can become confusing because now you've got individual
[722.74 → 728.84] components, but you still want to kind of have them all part of a larger microservice so that
[728.84 → 732.18] a team can own them and can own the data that supports them.
[732.50 → 737.58] Got it. So where previously your team scaling and your technical scaling were along the same lines,
[737.58 → 741.28] this is saying, let's break out the technical scaling, but we still want to kind of group
[741.28 → 743.90] these things for team scaling purposes. Yeah. Yeah.
[744.18 → 748.72] Quick question. As you've been talking, there've been some parts that sound like they're probably
[748.72 → 751.88] kind of generic to serverless and some things where you're talking about, you know, something
[751.88 → 757.06] in specific like Lambda or something like that. Are there ways that the different implementations
[757.06 → 761.78] differ across these different cloud providers or have we more or less converged to the same functionality?
[761.78 → 770.78] So there is certainly differentiation between AWS and IBM and Google cloud platform. The most of it's
[770.78 → 775.98] the same. I mean, the general idea is you write some sort of, you write some code, and you upload it
[775.98 → 780.86] into a function, and it's even driven architecture, right? So an event comes in and that could be,
[780.98 → 788.02] that could be somebody uploads a file into an S3 bucket or somebody posts something to an API gateway,
[788.02 → 792.04] or, you know, there's a message that comes in from a message bus or something like that.
[792.04 → 797.06] So whatever those events are that come in, the basic idea of serverless is it's a function that
[797.06 → 803.04] receives an event, does something with it, and then return something back. And so pretty much all
[803.04 → 809.26] implementations of it are the same in that regard. But like Lambda, for example, was out in 2014,
[809.48 → 815.20] way ahead of pretty much anybody else. So they've got a number of services that really complement it,
[815.20 → 820.26] right? So you have, you know, their cloud watch function to easily do or cloud watch to easily log
[820.26 → 826.22] data. They've got their simple queue service, which allows you to do, you know, like a message bus or
[826.22 → 831.98] queues. They have SNS, which is the ability to multicast events to multiple Lambdas or other
[831.98 → 838.56] locations. They have their Kinesis streams. And then they of course have Aurora serverless and Dynamo DB,
[838.82 → 844.26] which is their highly scalable serverless, you know, sort of NoSQL database. So they have a lot more
[844.26 → 850.48] services that you can use in that regard. But then, you know, Opening and Google Cloud Functions and
[850.48 → 855.54] Microsoft Reserve Functions, they're all very, very similar. And they all have slightly different
[855.54 → 861.50] implementations. Some of them run for longer. Google Cloud Functions automatically has a built-in
[861.50 → 867.38] HTTP REST API. So that's how you can access those functions as well as access them, you know,
[867.38 → 871.66] through other events. But for the most part, it's pretty much the same. And there's actually,
[871.66 → 877.98] and speaking of serverless Inc, capital S, there is a committee out there that's working to
[877.98 → 885.46] standardize events for serverless functions. So that's out there now. And so hopefully,
[885.88 → 891.44] that'll kind of push all the providers to at least standardize the way that events are received,
[891.68 → 894.32] which I think would be a good point in kind of consolidating the market.
[894.78 → 898.04] That's kind of what I was going to ask. I don't have a ton of experience with serverless
[898.04 → 902.76] functionality. But I have played around with Netlify a little bit. And I think with like the
[902.76 → 908.84] JavaScript API to tie into that, you basically like to create a function that accepts the event
[908.84 → 912.96] that's happening, I think maybe a context, and then it gives you a callback as an argument to it. And
[912.96 → 917.62] that callback is how you respond with something. Is that what they're working to standardize is
[917.62 → 924.26] basically like, how you define a function and how it will be run and receive the inputs from like a
[924.26 → 928.20] rest call or from some other event that might be happening and then how you respond to that?
[928.56 → 932.66] Yeah, I think that's I think that's the basic idea is to say that when an event comes in that
[932.66 → 938.42] is for X or for Y or whatever that event is, that it would be in a similar format. So similar maybe to
[938.42 → 943.60] what they did with RDF standards and things like that to try to say when you're representing a product
[943.60 → 946.70] that this is what a product should look like, these should be the fields, this should be the
[946.70 → 952.28] nomenclature that you use to describe these things. And so right now, obviously,
[952.28 → 959.12] the functionality or the event that comes in from an SQS, which would be a simple queue service,
[959.48 → 965.14] is different from even within Amazon is different from it is when you get a message in from Kinesis,
[965.18 → 970.92] or when you get a Dynamo DB stream or something coming in. So the idea here, I think, is to say,
[971.28 → 978.24] if you're going to say, hey, an image or a file was added here, or here is a REST API call that was
[978.24 → 984.06] made, this is what it should look like, this is the data it should contain, so that you could then
[984.06 → 991.04] say, I'm going to take my function from provider A and move it to provider B with not as much pain
[991.04 → 994.12] as kind of changing, you know, changing how it processes those events.
[994.44 → 995.18] Yeah, that'd be great.
[995.74 → 1001.44] All right, this is probably a good time to roll into a quick break. After the break, we'll come back and
[1001.44 → 1007.26] keep drilling into your brain of how this stuff actually works and maybe start digging into what
[1007.26 → 1011.88] is the value proposition. We've talked a lot about how this thing works, how it's different,
[1012.20 → 1015.52] but let's look at the value once we get back from the break.
[1015.52 → 1026.92] This episode is sponsored by our friends at Rollbar. How important is it for you to catch
[1026.92 → 1031.54] errors before your users do? What if you could resolve those errors in minutes and then deploy
[1031.54 → 1035.58] with confidence? That's exactly what Rollbar enables for software teams. One of the most
[1035.58 → 1041.36] frustrating things we all deal with is errors. Most teams either A, rely on their users to report
[1041.36 → 1046.74] errors or B, use log files and lists of errors to debug problems. That's such a waste of time.
[1047.04 → 1052.82] Instantly know what's broken and why with Rollbar. Reduce time wasted debugging and automatically
[1052.82 → 1058.68] capture errors alongside rich diagnostic data to help you defeat impactful errors. You can integrate
[1058.68 → 1063.22] Rollbar into your existing workflow. It integrates with your source code repository and deployment
[1063.22 → 1068.88] system to give you deep insights into exactly what changes caused each error. Give Rollbar a try
[1068.88 → 1074.38] today at no cost to you. No credit card is required. Our listeners get access to the Bootstrap plan with
[1074.38 → 1081.08] a hundred thousand events for free for 90 days. To get started, head to rollbar.com slash change lock.
[1091.98 → 1097.76] All right, welcome back. So just before the break, we talked about getting into value. Unfortunately,
[1097.76 → 1103.14] one of our panellists had his internet go out due to construction, but he sent in a question and I want
[1103.14 → 1107.94] to kind of put it there. So we talked about how this is kind of like taking this concept that we had
[1107.94 → 1113.34] of microservices and taking it down even more. And he was bringing up the point of, you know, what is the
[1113.34 → 1118.54] value prop of this as compared to just continuing to split down microservices into more microservices?
[1118.74 → 1124.62] I think it's a bit of a different model, but can we sort of explore like what's the point of serverless?
[1124.62 → 1130.38] Yeah. So, I mean, for me, and I think this is true of a lot of people, that the speed of development
[1130.38 → 1136.42] is really, really fast, right? So if you think about, well, and also take a step back. So this puts
[1136.42 → 1142.14] developers a lot closer sort of to the operational side of things. So if you figure your traditional,
[1142.14 → 1148.08] you know, sort of development firm or development team, you usually have, you know, we've invented this
[1148.08 → 1152.66] thing called DevOps where, you know, you try to get these developers or also do operations, and they try to,
[1152.66 → 1158.16] you know, get you through the CCD process and get things deployed. You still have to deploy a server.
[1158.16 → 1162.40] Or if you want to go down, you know, the container orchestration route, and you want to, you know,
[1162.40 → 1167.88] do Kubernetes or something like that. Now you've got labels and pods and all these other things that
[1167.88 → 1173.56] have to be created and orchestrated and containers built in order to run code. And so it gets really,
[1173.68 → 1179.56] really complicated. And you can spend months just trying to set up your environment in order to
[1179.56 → 1184.24] do something as simple as, again, bad example, but process an image or convert an image.
[1184.70 → 1190.34] So with serverless, you can write a function that converts an image or does a simple transformation
[1190.34 → 1196.36] for an ETL task, for example. And if you use a framework like serverless, capital S, or you use
[1196.36 → 1202.00] AWS SAM or, you know, Claudia JS or some of these other ones, you type a couple of commands in the command
[1202.00 → 1208.68] line and that deploys that application or that function to Lambda or to Opening or wherever to,
[1208.68 → 1214.42] wherever you want it to go. And then it's immediately available. So you can build applications.
[1214.42 → 1218.78] And of course, like we said, the more functions you write or the more complex you make your
[1218.78 → 1223.94] applications, you know, the more robust they get, but you can go ahead and build these things
[1223.94 → 1230.56] in minutes as opposed to potentially waiting quite some time for an operations team or a DevOps team
[1230.56 → 1237.74] to set up an environment for you to actually launch code. And the benefit of that there comes with
[1237.74 → 1244.06] auto-scaling as well. So if I have to write an ETL task, or I'll give you an example. I had a startup
[1244.06 → 1249.46] several years ago, right about the time that AWS was starting to get popular, and they didn't have
[1249.46 → 1254.68] any of this stuff. So we actually did an image processing component and our image processing
[1254.68 → 1260.52] component would reach out to Facebook and Instagram and to Picas, would download all your images that
[1260.52 → 1264.80] were associated with your accounts. And we would run them through a series of processing scripts.
[1264.80 → 1270.32] We had two giant image servers that were just chugging that if we had a lot of activity,
[1270.64 → 1275.30] they would basically choke, right? And so you'd have a bunch of backed up things that needed to run.
[1275.64 → 1280.20] So the same is actually kind of true now. If you think about even auto-scaling, if I have,
[1280.28 → 1285.16] you know, something like Elastic Beanstalk, or I'm using Ops Works or something where I have
[1285.16 → 1290.96] horizontally scaled services, I have to scale those up physical servers or virtual servers,
[1290.96 → 1296.84] but essentially have to launch more servers in order to scale those up. And that's not a difficult
[1296.84 → 1301.24] thing to do. It's just, it takes, you know, five minutes to start up a new server or a new virtual
[1301.24 → 1306.48] machine. And by the time that happens, I've already kind of lost the real-time aspect of it.
[1307.08 → 1313.50] With Kubernetes or with Docker, or if you're using like ECS or even the EKS service at Amazon,
[1313.82 → 1317.44] those will launch very quickly. So it's a little bit better, but with serverless,
[1317.44 → 1323.24] I could just write that image processing system. Now I could write that in an hour maybe and launch
[1323.24 → 1327.58] it. And I wouldn't have to worry about any operational stuff because that will just continue
[1327.58 → 1332.28] to scale as more concurrent requests come in. Having spent about a month wrapping my head
[1332.28 → 1336.28] around Kubernetes and trying to get stuff up and all of that, that sounds pretty darn appealing.
[1336.28 → 1340.78] I have to say. Yeah. And if you look at it from the business case, which is sort of the way I like
[1340.78 → 1345.66] to look at it. So I'm a, you know, I have traditionally been, I started as a developer, had my own web
[1345.66 → 1349.96] development company, you know, grew that. Then I started some startups. And so I've been in the
[1349.96 → 1354.78] CTO role in a number of positions. And when you're in the CTO role, you're forced to think about the
[1354.78 → 1360.62] business value of things. And just thinking about how much money past companies I've worked for or
[1360.62 → 1367.28] started have invested in operations. It's kind of crazy, right? I mean, we lost a lot of time just
[1367.28 → 1371.90] trying to figure out how to get our database to scale correctly or how to, you know, distribute the
[1371.90 → 1378.00] workload for our retail tasks or something like that. And so some people say, well, serverless is
[1378.00 → 1383.34] no ops, which is not true, but it certainly is fewer ops, right? So most of what you need to do,
[1383.42 → 1388.34] the developer can actually handle. And you might want a cloud guy that can, or a cloud professional
[1388.34 → 1392.70] that can come in and say, all right, well, we want these IAM roles, or we want, you know,
[1392.74 → 1398.08] some tweaking, there's some tweaking of knobs you can do. But for the most part, the idea is to say,
[1398.08 → 1403.42] you don't have to worry about 95% of the infrastructure anymore. You just upload that
[1403.42 → 1408.26] code, and it goes live, which saves your development teams a ton of money, saves you a ton of money,
[1408.48 → 1413.32] you know, or a ton of time to solve business problems as opposed to technical problems.
[1413.46 → 1419.06] And then the cost aspect of it is huge. If you have spikes in traffic, you can certainly plan
[1419.06 → 1423.82] your scaling so that, you know, when you know you get heavy traffic, maybe around noontime or
[1423.82 → 1430.46] certain times, you can sort of pre-warm your servers or your infrastructure so that you scale
[1430.46 → 1435.62] out a little bit so you can handle that load. But you are wasting a ton of money spending,
[1436.18 → 1440.06] especially when it isn't under that heavy load. So you just got all this idle time.
[1440.56 → 1446.96] With serverless, you're only paying for when it executes, which it saves a lot of money. And so if you
[1446.96 → 1453.62] factor in, you know, 95% reduction or whatever it is in operational costs, plus you're not paying for
[1453.62 → 1460.12] any idle time. Serverless, if you run it at scale, might cost you a little bit more than just running
[1460.12 → 1466.76] a couple of EC2 servers. But if you factor in total cost of ownership and get rid of all of that other
[1466.76 → 1472.56] work, all of that operational work and all of that planning and things like that, the value is huge.
[1472.68 → 1477.66] So your actual cost savings are, you know, gigantic compared to, you know, sort of going that standard
[1477.66 → 1477.92] route.
[1477.92 → 1481.64] By the way, I see that Chris managed to get his internet back. So he's back with us.
[1481.64 → 1485.94] Cool. So this sounds exciting, you know, as somebody who does deal with a lot of business
[1485.94 → 1490.44] management, what are the downsides? Like is local development hard? Are there any pain points?
[1490.44 → 1492.84] Like what, what does this cost us?
[1493.22 → 1499.62] Yeah. So I think that is actually a perfect point in terms of local workflows. It's easy to
[1499.62 → 1504.26] write a single function. There's plenty of, uh, of, uh, frameworks out there against serverless
[1504.26 → 1509.64] capital S being one of the most popular ones, AWS, their serverless application model, or SAM,
[1509.64 → 1514.28] they have a local development capabilities, excuse me. And there are a bunch of other ones out there
[1514.28 → 1518.52] as well. So you can write a function, and you can execute it locally and everything is great.
[1518.60 → 1522.94] You can simulate an event, and then it will spit back something for you. But as soon as you say,
[1523.06 → 1529.78] well, I need to write to this queue, or I need to access information from Dynamo DB, or I've got to do,
[1529.84 → 1535.14] you know, some other calculation where I'm interacting with, maybe I'm writing a function that interacts with
[1535.14 → 1539.42] three other functions or a couple of other services, whether it's through API calls or through
[1539.42 → 1543.86] direct function calls. So now it starts to get a little bit complicated. And again, there are tools
[1543.86 → 1547.88] out there that people are working on better tools to do it. Uh, sometimes you have to do a lot of
[1547.88 → 1553.68] mocking and stubbing in order to make the local aspect of this work a little bit better, but there's
[1553.68 → 1560.60] also, um, a lot of cloud-based solutions to this as well. So, you know, Stacker and AWS has their
[1560.60 → 1565.60] cloud nine service that allows, you know, sort of online or web-based IDE that you can do some of
[1565.60 → 1571.12] that stuff with. So it's getting better, but it's certainly that aspect of it. Local development is
[1571.12 → 1577.34] sort of, sort of pain, but beyond the idea of just kind of working locally, serverless right now
[1577.34 → 1583.32] does have its limits. So, uh, AWS just announced that you can now run a function for 15 minutes as
[1583.32 → 1589.78] opposed to the traditional five. And I think IBM, those run for 10 minutes, but Google cloud functions,
[1589.78 → 1594.36] I think is still five. So there are some limitations there. There are limitations on the amount of memory
[1594.36 → 1599.52] you can use. There are limitations on the number of CPU cycles that you kind of get with each function.
[1600.02 → 1605.92] So there are some limitations and that means it isn't necessarily perfect for every workload,
[1606.02 → 1612.38] but they're also sort of arbitrary limits, right? So just because it can only run for 15 minutes is
[1612.38 → 1620.04] probably more of a provisioning or a sort of resource planning restraint that, uh, or constraint
[1620.04 → 1626.20] that AWS has because they say, well, we can't just run servers with enough capacity that somebody could,
[1626.20 → 1630.90] you know, tie one up for an hour and a half. We need to kind of, we need to kind of balance that
[1630.90 → 1636.04] because they're paying for idle time. You're not, which I kind of mentioned the last point about the
[1636.04 → 1644.38] cost savings is now the cloud provider is taking the risk on idle time as opposed to the, the company
[1644.38 → 1649.64] that's buying that time. So there's a there's a huge win there, obviously. But again, with some of
[1649.64 → 1655.76] those limitations, serverless isn't necessarily right for everything. So to run it locally, uh,
[1655.76 → 1660.14] sorry to go, to go back to that. You said that you'd either have to run all the functions that you,
[1660.34 → 1663.34] the one you're working on may need to hit, or you might need to mock those in some way.
[1663.34 → 1668.98] Is there any like helpers with that? And I assume that they would be specific to like the types of
[1668.98 → 1673.18] functions, whether they're Lambda functions or, or Google cloud or, or the other, whatever other
[1673.18 → 1678.98] provider, are they specific to those? Yeah. I mean, and so also sort of be clear about how these
[1678.98 → 1684.38] functions work. Essentially what it is, is its just a handler. So it's actually, so there's a handler
[1684.38 → 1690.54] function within your code. And when the function gets triggered, the system knows to call that
[1690.54 → 1694.66] function within your code. And then from there, you can call other functions and have other
[1694.66 → 1699.08] requirements and things like that. But the basic idea is you're just running whatever code you're
[1699.08 → 1704.40] running. So you're running, you know, JavaScript or your, or node you're running Python or go,
[1704.54 → 1709.34] those applications will just run locally on your machine. So you have to have obviously that, um,
[1709.62 → 1714.32] you have to have that runtime installed so that you can execute that code. But so when you do that,
[1714.32 → 1719.88] these other cloud providers, where you're going to host the code really doesn't matter when you run
[1719.88 → 1725.40] it locally, it's when you are trying to reach out to another service that needs to exist. So
[1725.40 → 1731.28] if you're using Dynamo DB, for example, there's a local version of Dynamo DB that you can download and
[1731.28 → 1736.64] run, but let's say you're accessing MySQL or Postgres, you can just run a local copy of that and then
[1736.64 → 1741.32] locally point to it so that you don't have to, you know, connect remotely. One of the things that I do
[1741.32 → 1744.72] in my development a lot is, especially because I interact with, you know, I do a lot with
[1744.72 → 1749.34] microservices. I will write a microservice and, you know, test it locally and have it do what it
[1749.34 → 1754.22] needs to do. And then I'll publish that, you know, whether it's in dev or in staging or sometimes in
[1754.22 → 1758.68] production, depending on what we're doing with it. And then the great thing is, is that when you run
[1758.68 → 1767.00] another microservice locally, you can make that remote call to that live microservice. So, you know,
[1767.00 → 1770.98] so it does give you the ability, of course, if you lose your internet connection or the
[1770.98 → 1774.26] function becomes unavailable for some reason, then obviously it's harder to test. But I mean,
[1774.26 → 1779.16] I'm a big proponent of writing a lot of stubbed tests, doing a lot of unit testing and things like
[1779.16 → 1784.80] that, and then sort of running a full integration test that actually will access live services in
[1784.80 → 1790.02] order to do it. But there are some things you can do, you know, you can run local APIs, you can run,
[1790.02 → 1795.70] you know, local versions, like I said, of Dynamo DB or some other services. But it is, it's not,
[1795.70 → 1802.14] I'd say it's not any more difficult than trying to test microservices written in, you know, in a more
[1802.14 → 1802.98] traditional sense.
[1802.98 → 1809.92] One restriction that I noticed when doing some Lambda development was basically the version of
[1809.92 → 1818.44] node that you want to use is not necessarily the version of node that Amazon is running. I imagine
[1818.44 → 1823.80] platforms like, I don't know if that's the same for Google Cloud or Azure, but I think with
[1823.80 → 1829.78] Open Whisk anyway, you have some sort of, at the very least you can run your own instance of it and
[1829.78 → 1836.74] kind of have a better, more granular control over your environment. But yeah, that's one problem I
[1836.74 → 1843.40] ran into when it's like, why isn't AWS upgrading node, you know, nodes, this version of node that
[1843.40 → 1846.04] they're running is about to become unmaintained, you know?
[1846.24 → 1851.08] Yeah. No, no, that's a good question. And actually, that was one of the things that frustrated me
[1851.08 → 1857.52] quite a bit because I was writing node functions with, you know, async and await when I first
[1857.52 → 1862.64] started using Lambda, because you could polyfill, or you could, you know, you could run the latest
[1862.64 → 1869.26] version. And when AWS launches Lambda, it was at like 4.3. And so you couldn't do quite a bit,
[1869.32 → 1874.86] quite a bit of things. Then they upgraded to 6.1, and they still didn't have async await, which made me,
[1874.86 → 1880.34] when I switched to writing a lot of things for serverless, I had to switch back to promises.
[1880.84 → 1884.92] And so I was writing a lot of things with Bluebird and things like that in order to manage,
[1885.02 → 1891.82] you know, the processes there. Quite a while ago, they've upgraded to 8. This is Lambda. And I know
[1891.82 → 1897.62] that Google Cloud Functions is now on 8. So most of that new functionality is there. But I think part of
[1897.62 → 1903.02] the reason why they do that is it needs to be highly stable. And I think they may need to make some
[1903.02 → 1908.30] adjustments to it in terms of how it operates, in terms of how much memory it uses. And I guess,
[1908.36 → 1910.84] you know, they're running it through their hypervisors and all kinds of things like that.
[1910.90 → 1914.76] So I think they just need to be smart about it. And that's why it takes a little bit of time to
[1914.76 → 1920.06] upgrade. But I will say that Node 8, I know there are some new things that have come out, but Node 8 is,
[1920.34 → 1925.54] and it's 8.1 that they're running on Lambda. I found I can do pretty much anything I want with it.
[1925.54 → 1930.52] So it would be nice if they were always up-to-date, but it's at a point now where,
[1930.52 → 1935.52] you know, I know Node's getting better, but version 8.1 is pretty good, gives us async,
[1935.64 → 1940.12] away, gives us classes, you know, gives us some of those more modern things that makes development
[1940.12 → 1947.36] easier. Right. Yeah. I had resorted to actually transpiring my code with Babel and then just like
[1947.36 → 1949.18] uploading a bundle. Yeah.
[1949.94 → 1954.30] So, yeah, I'm glad to hear that things have moved forward.
[1954.72 → 1959.36] I think one other benefit that you might've mentioned that I didn't really realize until
[1959.36 → 1966.16] you said it is that with you being able to kind of have functions or services that are just
[1966.16 → 1971.58] oriented to one specific thing and aren't really reliant maybe on other ones in, except for on the
[1971.58 → 1976.58] edges and the ways that you communicate in and out of them, it does allow you to diversify your,
[1976.80 → 1981.56] the technology you're using, whether you want to switch between languages or switch between like
[1981.56 → 1987.12] frameworks or start migrating to a new language or framework. That's a benefit that I hadn't really
[1987.12 → 1990.92] considered. Yeah, no, actually that's one of the that's one of the huge benefits there. So again,
[1990.92 → 1995.20] you think about your traditional microservice, everything you do in that microservice, you're
[1995.20 → 1998.66] usually going to choose sort of one runtime, right? And you're going to say, we're going to write
[1998.66 → 2003.10] everything in Python or everything's going to be in Node or whatever. And you do that because again,
[2003.10 → 2008.00] you don't want your containers or your services or the services, servers that the services are
[2008.00 → 2011.76] running on. You don't want them to have too many runtimes installed so they can do all these
[2011.76 → 2016.88] different things. So, but with something like serverless, you can say, look, the tool that
[2016.88 → 2020.76] accesses or the function that accesses the database and writes this stuff here, you know,
[2020.80 → 2026.20] Node is fine for that, that that's okay. But then we have maybe some sort of number crunching thing
[2026.20 → 2030.74] that we need to do in order to compile some reports and, and maybe Python would be better in
[2030.74 → 2036.18] order to write that in. So now within one microservice, you could have multiple languages being
[2036.18 → 2040.16] used and those functions can communicate with one another, you know, just through a simple HTTP
[2040.16 → 2046.82] call through the, you know, through the SDKs. So it's very, very easy for you to diversify that way.
[2046.94 → 2052.48] So that's within a single service, but even more practical probably is to say, look, we have a team
[2052.48 → 2058.90] that is writing this particular service, and they think it's better to write it in Java or .NET or
[2058.90 → 2064.52] whatever. And then we've got another team that is a, is a JavaScript team or whatever. So that's really
[2064.52 → 2069.58] great because now you can have a diverse set of, you know, technologies. You don't want to get too
[2069.58 → 2073.22] many, but you could have a diverse set of technologies. But what's really great about
[2073.22 → 2078.32] this idea of splitting up functions into tiny units is to say, okay, somebody wrote this
[2078.32 → 2084.44] function in Python a year ago, and we have a new guy came in, and we need to make some changes to it.
[2084.50 → 2088.56] Could probably rewrite that entire function in a couple of hours because it's so small,
[2088.66 → 2091.40] you know, it's a couple of hundred lines of code, not even maybe a hundred lines of code.
[2091.40 → 2096.80] So you could rewrite that function in a new, in a new language and then run your unit test
[2096.80 → 2100.96] against it. And yeah, it worked. It does exactly what we needed to do. So that's another great
[2100.96 → 2105.68] thing about this is where you're really minimizing this, you know, this, the code surface, right? So
[2105.68 → 2110.78] you do less and less in code and more with these managed services that it connects to,
[2110.84 → 2116.20] then it makes it extremely efficient for developers to kind of go in and make changes, swap things out.
[2116.20 → 2121.08] And then you're also not looking through, you know, that, uh, that library file that is,
[2121.16 → 2125.50] you know, 10,000 lines long with no comments and things that aren't even being used anymore,
[2125.50 → 2128.62] but you're afraid to remove them because you don't know if they're not being used anymore.
[2128.80 → 2131.10] This is just much more obvious when you take this approach.
[2131.48 → 2133.10] I feel like you're calling out my code base right now.
[2134.22 → 2135.18] We all have them.
[2136.28 → 2140.76] That actually raises kind of an interesting question, which is how do you manage these code bases?
[2140.94 → 2145.58] Like, is this a bunch of folders in a single repo? Do you have repos for every function? Like,
[2145.58 → 2147.80] how are you even thinking about these things?
[2148.32 → 2153.10] So actually that is one of the things that's sort of the downside to this. So what I do and
[2153.10 → 2158.94] what a lot of people recommend is to create a separate Git repository for each microservice that
[2158.94 → 2163.84] you're creating. And then if you're using, so serverless, for example, framework, serverless
[2163.84 → 2170.26] framework, capital S uses, um, a serverless.yaml file, which you specify all the functions and you
[2170.26 → 2175.98] can also specify, uh, specify cloud, um, cloud formation templates in there as well. So if you
[2175.98 → 2181.76] need to generate an SQS queue, or you need to generate a, um, SNS or any other services, you need
[2181.76 → 2188.94] a Dynamo DB table, you can do that all in one file. So you typically have your service all sort of
[2188.94 → 2195.32] defined within one serverless.yaml file. It's very similar when you're doing a SAM template,
[2195.32 → 2199.68] you define all your functions, everything in a single SAM template along with your cloud formation
[2199.68 → 2205.00] resources. And so you have all those functions in, and I like to split up my functions into separate
[2205.00 → 2212.08] files too. Sometimes people will identify a function that points to a handler within a larger file that
[2212.08 → 2215.84] has multiple functions in it. So you have a lot of flexibility there, but I always separate them
[2215.84 → 2221.80] into, into smaller ones. So now you have just this folder, this Git repo that has this set of
[2221.80 → 2226.18] functionality in it. You tag your functions. So you know that it's part of a particular service
[2226.18 → 2230.92] and so forth, but that's the best, in my opinion, that's how I do it. I found that to be the best way
[2230.92 → 2235.52] to do it. If you start kind of commingling them in a larger mono repo or something like that,
[2235.70 → 2241.96] then it just kind of gets confusing in terms of which service does which. But if you own that Git repo,
[2242.22 → 2247.60] and again, this can get difficult to manage because sometimes you have a hundred microservices. So now you
[2247.60 → 2251.62] have a hundred Git repos, which seems a little bit crazy, but I still found this to be the best.
[2251.80 → 2256.66] So now you can go in, and you can document that. You can specify what the, you know,
[2256.66 → 2260.90] the well-defined interface, how people are supposed to communicate with it, what the events should look
[2260.90 → 2265.62] like going in, what events will look like coming out. So you can really own that and give that to
[2265.62 → 2269.44] one team and then version it separately. And of course with microservices, you know, you can have
[2269.44 → 2274.22] a hundred microservices running, and then I can go ahead and swap services in and out. So long as I,
[2274.44 → 2279.38] you know if I've made a contract with any other microservice, I know that, um, I know that it's going to
[2279.38 → 2283.32] accept the input, and it's going to respond in a way that it can understand.
[2284.32 → 2288.10] Yeah. I worry a little bit, and I don't have much experience actually implementing serverless,
[2288.14 → 2291.28] but I worry a little bit that we're going to have, you know, the old joke about microservices,
[2291.44 → 2295.42] right? Which is like, you have a problem. So you implement microservices. Now you have a hundred
[2295.42 → 2295.94] problems.
[2296.24 → 2296.64] Exactly.
[2296.64 → 2302.34] This might take that even to another level, at least in terms of like conceptual management of
[2302.34 → 2302.96] the code.
[2303.36 → 2308.04] Yeah. I mean, I totally agree with you. And I mean, I had kind of gone back and forth about,
[2308.16 → 2312.18] you know, the best way to organize stuff. Cause in some cases, if you think about,
[2312.28 → 2317.56] just think about simple REST API. So a lot of times there's this argument for serverless functions
[2317.56 → 2323.54] to say, okay, so if I have a REST API that looks up a customer, then I should point that to
[2323.54 → 2329.22] a serverless function that just looks up the customer. And then if I need to add a new customer,
[2329.38 → 2333.52] I should have another endpoint there. And that should point to a different function that handles
[2333.52 → 2338.52] just adding a customer. And so the idea is to keep these functions as small as possible.
[2338.84 → 2344.00] But the problem is, is that then you end up, if you've got a complex API, you may have, you know,
[2344.10 → 2351.10] 40 functions as part of a single API, as part of a single microservice. And that becomes to me a
[2351.10 → 2355.84] little bit unwieldy. And there's a lot of shared code you want in there, you know, the database
[2355.84 → 2360.74] connection information or configuration information. So there's a lot of that you want to share.
[2360.94 → 2364.98] And you can certainly have a shared library between those different functions that get
[2364.98 → 2369.42] deployed when you deploy the function. But I like to consolidate sometimes. So I like to say,
[2369.50 → 2375.16] look, if I've got an API that needs to do maybe an admin of a user, so it can add a new user,
[2375.22 → 2379.04] can remove a user, it can update their profile image, whatever you want to do there.
[2379.04 → 2383.88] Sometimes I'll stick all of those routes into a single, into a single Lambda function,
[2383.88 → 2388.28] because you also have this problem of cold starts, which we haven't really talked about yet.
[2388.40 → 2393.24] But when a new function that isn't warm, that hasn't been used in a while, when somebody tries
[2393.24 → 2397.70] to access that function, it might take a couple of seconds sometimes before that function becomes
[2397.70 → 2403.84] available. And so if you're using functions as the backend for an API, you want to keep those
[2403.84 → 2408.46] functions warm, you don't want those to get cold, because then it could take some time and
[2408.46 → 2412.62] there'd be higher latency in order to get a response back. So by consolidating functions
[2412.62 → 2417.30] or routes into a single function that again, accesses a library and so forth, I've still
[2417.30 → 2421.58] found the performance to be perfect. And then the management of it is a heck of a lot easier.
[2422.14 → 2426.26] Has anyone created some sort of, maybe if you have the situation where you have this
[2426.26 → 2432.58] microservice, for instance, and maybe it does, you know, the four CRUD operations or what have you,
[2432.88 → 2437.14] has anyone created some sort of abstraction that says, okay, you just write your code and you
[2437.14 → 2442.20] pretend it's a single code base. But what we're going to do is essentially split this up into,
[2442.80 → 2449.62] you know, like, basically, there's like a tool or something that would split it up behind the scenes
[2449.62 → 2455.80] based on the endpoint. And so it's kind of like, allows you as a developer to look at it as a single
[2455.80 → 2461.50] entity, like basically, just so you can reason about it a little better. And then maybe it implements,
[2461.50 → 2467.88] say, sharing of code between things. And then but it actually kind of so you don't have to think
[2467.88 → 2473.50] about it, it would split up your service into multiple, multiple functions. Has anyone attempted
[2473.50 → 2475.98] anything like that? Or is there anything out there that does this?
[2475.98 → 2482.62] Well, so to some degree, I mean, if you think about like a web framework, like Express, for example,
[2482.82 → 2487.26] you know, so the idea is Express is generally, you define all your routes, and then you kind of
[2487.26 → 2492.30] offload those to separate files that will actually do the processing of those routes. And you would
[2492.30 → 2498.34] share your library there. So I actually wrote an open source project, it's called Lambda API,
[2498.34 → 2505.90] and you can go to bit.ly slash Lambda API. And it's specifically for AWS and Lambda. But what it is,
[2505.94 → 2512.98] is it's essentially a very, very lightweight version of Express. And so when I am writing APIs, as I just,
[2512.98 → 2517.70] you know, said about kind of consolidating all the routes into one Lambda function, what I'll do is
[2517.70 → 2523.94] I'll do that and then use Lambda API, which maps the, you know, maps the routes just like it would for
[2523.94 → 2531.44] Express or Testify or any of those. And then I'll break the actual business logic out into separate
[2531.44 → 2538.34] library files. And so if I want to be able to access the service from an API from the REST API,
[2538.34 → 2544.42] I have one file that will do all that routing for me. So it makes it a little bit easier from a sort
[2544.42 → 2549.18] of an original or initial setup standpoint. And then of course, I can communicate with those
[2549.18 → 2555.34] individual functions. But then I also would potentially launch those as separate functions
[2555.34 → 2560.20] so that I could communicate with them directly through the SDK. So it's not exactly what you're
[2560.20 → 2563.58] talking about. But I see what you're saying, where you just want to kind of write an application
[2563.58 → 2567.90] then have it split it up automatically for you. I think there's just a lot of code sharing that
[2567.90 → 2573.58] needs to happen there. And so I think that you want to know where those separations
[2573.58 → 2578.30] are. But again, the part of the, and I don't want to get too deep into this. But one of the
[2578.30 → 2583.38] things that you often find with microservices and teams that are building microservices are shared
[2583.38 → 2588.20] code bases where there might be some sort of database connection layer. And whether you're
[2588.20 → 2592.64] connecting to a different database or not isn't the point. There's just somebody wrote code that does
[2592.64 → 2596.90] the database connection. So in a monolithic application, you just include that and that's
[2596.90 → 2600.92] available for every service that you kind of have running in the monolith. When you break that
[2600.92 → 2606.10] out now, sometimes you have to have, you know, 10 different services that need to share code in
[2606.10 → 2610.66] order to do this database connection. And so the problem with doing that is obviously, if somebody
[2610.66 → 2614.24] changes the code, because they need to do something there, then all of a sudden you get all this code
[2614.24 → 2618.34] that's out of sync. So you can, you know, go down the road of versioning and things like that,
[2618.34 → 2622.40] so that everybody could have their own version of it. But you're always working on the main
[2622.40 → 2628.06] repository if you need to update that. But within an individual microservice, you can write your own
[2628.06 → 2634.02] shared libraries, right? So if you write a Lambda function that accesses, you know, let's say does
[2634.02 → 2639.00] some process where it finds some matches in a database. If there's a snippet of code that does
[2639.00 → 2645.62] that, you can have that snippet of code be triggered when somebody calls that from an API and an API
[2645.62 → 2650.12] event comes in, and you can have it trigger that bit of code. But then you could also share that code
[2650.12 → 2658.02] with another Lambda function that's meant to respond when there is a when there's a kinesis event that
[2658.02 → 2663.48] comes in or some other event that comes in, or it's called directly from another function. So within the
[2663.48 → 2669.22] microservice, reusing code is pretty simple. And when you deploy your microservice, you generally
[2669.22 → 2674.58] redeploy all of your functions so that any new updates are part of it. But because it's all owned by
[2674.58 → 2679.60] the same team or should be owned by the same team, managing that is a lot easier. I don't know if
[2679.60 → 2684.20] that answered your question in any way, shape or form. It's hard to say. I need to look at this
[2684.20 → 2690.42] this Lambda API thing, but I'll check it out here. I think we're at a good spot to take another quick
[2690.42 → 2696.20] break. And then when we come back, we will dive a little bit deeper into this concept of architecture.
[2696.20 → 2702.80] What does it look like to implement an application using serverless? And do you build your whole
[2702.80 → 2708.22] application? How does one architect to take advantage of this? But we'll see you after the break.
[2709.60 → 2721.00] This episode is brought to you by DigitalOcean, the simplest cloud platform for developers and teams
[2721.00 → 2728.20] deploy, manage, scale faster and more efficiently on DigitalOcean. Managing infrastructure is easy
[2728.20 → 2732.68] for teams, whether you're running one virtual machine or thousands. Use our special link to get
[2732.68 → 2740.46] $100 credit for DigitalOcean and try it today for free. Head to do.co slash changelog. Once again,
[2740.80 → 2747.94] do.co slash changelog. So I have some pretty awesome news to share. We are now partnered with Algeria.
[2748.24 → 2754.42] If you've ever searched Hacker News, Tee spring, Medium, Twitch or even Product Hunt, then you've
[2754.42 → 2760.72] experienced the results of Algeria's search API. And as we expand our content, we knew that one day
[2760.72 → 2765.22] we'd have to either roll our own search solution on top of Postgres or we can partner up with Algeria.
[2765.72 → 2770.50] And I'm happy to report that phase one of our search is now powered by Algeria. We're able to
[2770.50 → 2776.24] fine tune our indexing, gain insights from search patterns and analytics. We can create custom query
[2776.24 → 2780.92] rules to influence ranking behaviour, as well as improve our search experience by adding synonyms
[2780.92 → 2785.28] and alternative corrections to queries. Sure, we could build search ourselves, but that would mean we would
[2785.28 → 2789.58] be busy doing that instead of shipping shows like you're listening to right now. Huge thanks to our
[2789.58 → 2793.74] friends at Algeria for working with us. Check the show notes for a link to get started for free
[2793.74 → 2796.30] or learn more by heading to algolia.com.
[2808.80 → 2814.32] Okay, welcome back everyone. Back on JS Party talking about serverless. I want to explore with
[2814.32 → 2820.52] you, Jeremy, a little bit of a question of how do we use this in the broader ecosystem of product
[2820.52 → 2826.26] development? You know, if we're starting to flood in serverless, is this something that is like,
[2826.44 → 2830.90] you're going to re-architect your system entirely to take advantage of serverless? Is this something
[2830.90 → 2835.14] where you're going to design something that you have your standard application, but it's calling
[2835.14 → 2839.14] out for little pieces? Like how does this play into the way that we fully build applications?
[2839.14 → 2844.52] Yeah. So first, I would highly suggest about, you know, version two syndromes and saying,
[2844.62 → 2849.32] hey, let's just rewrite our whole application. Because chances are most of your application is
[2849.32 → 2854.30] probably running just fine or, you know, it's at least running. So an important thing to remember
[2854.30 → 2859.50] with serverless too, or I mean really any technology you want to integrate in sort of slowly is it's not
[2859.50 → 2864.90] an all or nothing proposition. So it's not like everything has to be serverless and or vice versa. So
[2864.90 → 2869.08] the way that I would suggest, especially if you're a new team, and you're looking at this,
[2869.18 → 2873.38] whether you're already running microservices or you're running a monolith or whatever you're doing,
[2873.72 → 2878.74] you know, look at what parts of your application that, you know, you want to improve, pick a small
[2878.74 → 2883.46] part of it. And maybe it's an ETL task, maybe it's some sort of processing task. And then you can build
[2883.46 → 2889.50] out, you know, a serverless or a small serverless microservice or application that handles that piece of
[2889.50 → 2894.12] your system. And then using something like the Strangler pattern where you would, you know,
[2894.12 → 2899.62] maybe use API gateway to send, you know, most of your traffic, most of your API traffic goes to
[2899.62 → 2905.18] your old monolith or your other microservices. And then you take one route, and you route that into
[2905.18 → 2909.56] your, your serverless, you know, the serverless application that you built. So again, that it's
[2909.56 → 2914.32] important piece of it because I do think that over time you might look and say, well, we have a problem
[2914.32 → 2919.26] scaling this one particular piece of our application. And maybe my monolith works perfectly fine for
[2919.26 → 2923.74] everything else. But when I have to do X, I get bottlenecks. So maybe that would be a good
[2923.74 → 2928.58] candidate to split out and take advantage of that sort of near limitless scaling that serverless gives
[2928.58 → 2928.92] us.
[2929.24 → 2934.60] Interesting. I had to quickly Google the Strangler pattern because that was, that's a new one to me.
[2934.72 → 2939.66] So that's essentially if I'm understanding it properly, it's like basically giving you a way
[2939.66 → 2945.88] to migrate pieces at a time via having a routing layer in between your application and other things.
[2945.96 → 2946.38] Is that right?
[2946.52 → 2947.12] That's correct. Yeah.
[2947.12 → 2953.04] Cool. Okay. So coming from an existing thing, pick a piece that you want to scale better or
[2953.04 → 2957.82] something and tackle that. What about when you're thinking about building an application from scratch?
[2958.32 → 2964.20] Is this, you know, is serverless something where you would, for example, build a whole web app that's
[2964.20 → 2969.26] all serverless? Or is this something that fits into a broader ecosystem? Like how do you deal with
[2969.26 → 2972.24] things like authentication and all that other kind of nonsense?
[2972.24 → 2977.00] Yeah. So, I mean, it all depends obviously on what you're building, but if I, if I'm working
[2977.00 → 2983.26] on a new Greenfield application, I'm going to ask myself the question, can this be built in serverless?
[2983.34 → 2988.32] If the answer is yes, then you build it in serverless. If the answer is no, then you ask yourself that
[2988.32 → 2993.88] question. Can I build it in serverless? Because you probably can. So it's sort of a thing to me where I
[2993.88 → 3000.28] can't see many applications that the majority of them couldn't be built in serverless. I do think there
[3000.28 → 3003.86] are some limitations again, especially with long-running tasks and things like that.
[3004.18 → 3010.10] But serverless Inc is launching V2 of their framework, which is going to be cloud-agnostic.
[3010.10 → 3015.02] And one of the features they have there is you can actually launch your functions either as Lambda
[3015.02 → 3020.20] functions, which would be the traditional serverless, or you can launch them as Margate functions or Margate
[3020.20 → 3026.04] containers. So it would actually launch your function into a Margate container. So you are using Margate
[3026.04 → 3030.18] into a container so that you could run that as long as you wanted to. So it basically would build
[3030.18 → 3034.78] the container and launch a little server for you and scale that. So that's also kind of a new thing
[3034.78 → 3038.52] where, where serverless might be heading, where containers might be part of this. But anyway,
[3038.62 → 3042.64] so if I'm building a new application though, there's pretty much everything I would, I would look at it
[3042.64 → 3047.88] and say, you know, what do I need to actually process? What are the business rules that I, or the
[3047.96 → 3052.78] what's the business logic that I have to write? Because I think a lot of times people start planning an
[3052.78 → 3056.68] application, they say, okay, well, what database should we use or what programming language should
[3056.68 → 3060.62] we write it in? With serverless, I think you can just basically say, okay, what do I, what do I want
[3060.62 → 3065.84] to solve? And then you can find a bunch of managed services and pieces that you can kind of glue
[3065.84 → 3070.34] together. And you really don't have to write that much code in order to get a working application.
[3070.90 → 3075.68] And if you're obviously going to, well, most likely have a front end to your application,
[3076.00 → 3081.20] whether it's a React app or Vue or Angular or whatever you're using, then you start thinking about,
[3081.20 → 3087.56] okay, how can I have serverless back my CDNs, right? So how can I, how can I put stuff out on,
[3087.64 → 3095.24] in an S3 bucket or on one of the other CDN providers and say, that can be my single page
[3095.24 → 3099.78] app. Maybe that can get, that can go beyond a single page app because another component,
[3099.92 → 3105.36] I'm rambling here a bit, but this talking about this gets me sort of excited because I think this
[3105.36 → 3110.02] is definitely the future. If you look at something like Cloudflare workers or Lambda Edge,
[3110.02 → 3118.44] which is sort of the global distributed CDN that will call serverless functions as different
[3118.44 → 3123.42] events happen. So you can call a serverless function when somebody tries to access a cached
[3123.42 → 3129.76] object somewhere and that can change the headers. It can detect, you know, where, what region they are
[3129.76 → 3136.02] and route them differently. It can perform AB routing so that it goes different places. It can know that
[3136.02 → 3140.82] it's a mobile app or a mobile device that's accessing it. So do something different there.
[3140.90 → 3146.32] But not only that, it can actually wait for the response from the origin and then do something with
[3146.32 → 3150.58] the response from the origin to say, okay, I've loaded an image, but now I want to add,
[3150.68 → 3156.66] you know, these five or six headers to it, or I want to change the caching behaviour of it because
[3156.66 → 3161.84] it's being accessed from a mobile device or being accessed from the EU rather than being accessed from
[3161.84 → 3167.30] the United States or something like that. So you start layering in this now where you have all of
[3167.30 → 3171.94] these backend services that are glued together with serverless. And then you have all of these
[3171.94 → 3177.80] front end cloud, you know, or excuse me, these CDNs that are out there that they can host the front
[3177.80 → 3183.06] end of it. And not only can they make API calls and do things like that, but they can also interact
[3183.06 → 3188.84] just as part of the just as part of the execution of loading something there. So you can handle your SEO.
[3188.84 → 3194.08] You can, I just, the, the, the possibilities are quite limitless when it comes to that stuff.
[3194.14 → 3198.50] And I'll talk about authentication, but I'll stop in case you, you had any questions in between.
[3199.08 → 3203.00] Well, you might be about to cover this, but one question I had is like, how much
[3203.00 → 3207.42] of your application logic can you actually even push out to the edge? Cause one of the things that
[3207.42 → 3212.96] gets me thinking about is like, you know, one of the major limitations on performance where we've
[3212.96 → 3216.62] gotten to is literally the speed of light, right? Like you can't speed up the speed of light.
[3216.62 → 3223.20] So if somebody is over in the EU or in Africa or wherever accessing your application back on,
[3223.68 → 3228.94] you know, in the U S somewhere, like that's built in a bunch of latency. But if you can actually
[3228.94 → 3234.40] push a lot of that logic out all the way to the CDN, like when I first saw stuff about Lambda at edge,
[3234.42 → 3238.40] I was just, my mind was blown. I was like, you mean I can actually be running my application
[3238.40 → 3240.48] where the user is not where I am.
[3240.48 → 3246.04] Correct. I mean, it's to a certain extent. And so you certainly don't want your Lambda function
[3246.04 → 3252.48] that is, is being accessed, um, you know, in, in Tokyo or something like that. You don't want that
[3252.48 → 3258.26] to be calling a database that's hosted in U S East one, you know, that's hosted in Virginia,
[3258.26 → 3262.32] because you're going to have, you're going to have latency there. So you've got a very limited set of
[3262.32 → 3267.22] time in which you can execute some sort of code. But the great thing about it is if you are,
[3267.22 → 3272.56] let's say that you want to, um, you know, uh, globally distribute content, right? So if you're,
[3272.82 → 3277.70] if you, if it's a blog, or it's a content on your website or whatever, you know, even a response from
[3277.70 → 3282.96] the API, which might be a JSON, some sort of JSON that has, um, you know, formatted, you know,
[3282.96 → 3287.98] you formatted blog post in it or something like that, even a call back to the origin originally to
[3287.98 → 3295.46] load that the first time you can then cache it. So you could from the edge, make an API call to your
[3295.46 → 3300.98] API that runs in Oregon or that runs in Ohio or wherever you're running, um, your data centre,
[3300.98 → 3306.14] where that runs that can make that call. And so, yeah, maybe the first time somebody accesses that
[3306.14 → 3311.40] page, and it's got to load that JSON file, it's going to, or the, the, uh, API response. Yeah.
[3311.40 → 3317.68] Maybe it takes a second to, to load that, but then every other time until it expires or, you know,
[3317.68 → 3321.62] and you can set that, you can set that on each individual piece of content. You've got a lot of
[3321.62 → 3327.22] power, uh, on the edge there, you know, that will load instantaneously the next time it comes around,
[3327.26 → 3332.74] the next time it gets loaded. So you want to be careful about how much you're doing in, you know,
[3332.74 → 3336.42] how much you're trying to do in real time on the edge, because you'll lose that, the benefit of that,
[3336.48 → 3341.44] uh, of the saved latency, but you certainly can cache bits of your data. I mean, I think about my
[3341.44 → 3347.40] own blog. I don't, it loads it from a MySQL database every time you load a page, which is
[3347.40 → 3351.72] ridiculously inefficient. And again, it's just WordPress. So that's, you know, kind of plagued
[3351.72 → 3357.00] by that, but it would be so much easier for me to just cache that information, um, and have it as
[3357.00 → 3363.42] a cache static page because 99% of that page doesn't change. And if I did have to change something
[3363.42 → 3368.92] small, well then I could make an API call, but the page would load. And then if it takes, you know,
[3369.16 → 3374.40] 500 milliseconds for it to load some bit of dynamic, you know, display because it has to make an API call,
[3374.40 → 3378.58] even if it's from the edge, well then, then let it, but, um, but yeah, you can put a lot of that
[3378.58 → 3382.74] functionality, right, you know, right out there on all those edge servers. Essentially, like you could
[3382.74 → 3386.74] run the equivalent of a service worker with a little proxy there, except instead of it being
[3386.74 → 3391.70] per browser, it's like per location on the CDN. Correct. Yeah. It's very, it's very exciting.
[3391.92 → 3396.02] There are a lot of very cool things that can be done with that. Would functions typically be
[3396.02 → 3400.04] authenticated before they're, they're run, or is that something that the function itself would have to
[3400.04 → 3403.74] handle? Yeah. So that's actually another good question. So the way that authentication works,
[3403.74 → 3409.98] at least in AWS, and I'm more familiar with AWS, that's the primary one that I use. So if you're
[3409.98 → 3415.22] accessing functions from one another, so if you're calling your billing service from your catalogue
[3415.22 → 3420.44] service, something like that, the IAM roles are all built in, right? So you have to give a function
[3420.44 → 3425.28] permission to access, uh, you know, to call the Lambda SDK and so forth, the invoke function
[3425.28 → 3431.52] permission. But if it's outside, there is no access to your Lambda functions from the outside.
[3431.52 → 3437.28] They actually all run behind a control plane where there's no direct network access to them,
[3437.36 → 3444.04] which makes them highly secure. So in order for you to load or trigger a Lambda function from the
[3444.04 → 3449.22] outside, you have to route it through something like API gateway. So API gateway has a bunch
[3449.22 → 3455.02] of built-in functionality where you can have that load and authentication function. So the first time
[3455.02 → 3459.78] somebody tries to make a call to one of your endpoints, that will actually go and run a Lambda function
[3459.78 → 3466.20] that can, you know, look at a JS, you know, a web token, or it can look at, you know, it can do OAuth
[3466.20 → 3471.20] or something like that, where it can read whatever types of authentication headers you're sending in,
[3471.26 → 3477.54] and then make the decision whether that has access to specific routes. And then you
[3477.54 → 3483.32] basically just send it back, you know, just a policy document. And then, then AWS, then the AWS API
[3483.32 → 3489.46] gateway will decide whether you can access specific routes. So that's a it's a really great way to do it,
[3489.46 → 3493.84] where your Lambda functions can be pretty dumb. They don't have to know whether somebody has access
[3493.84 → 3501.12] to it. They just know that if the API gateway allows them to route an event to it, then they're
[3501.12 → 3505.96] authenticated. And of course you could add in, you get access to all the headers and everything that gets sent to you
[3505.96 → 3511.26] within that Lambda function. So if there was some, including the policy document, so if there was something in there
[3511.26 → 3515.82] where it's like, they have the ability to read, but they don't have the ability to write, then within your function,
[3515.82 → 3520.50] you may want to add, you know, those ACLs there, but for the most part, you would handle that at the
[3520.50 → 3526.36] gateway level. Awesome. So we're going to have to wrap pretty soon. Are there any major things going
[3526.36 → 3531.86] on in the serverless world that, you know, either sort of big advancements that happened recently that
[3531.86 → 3536.62] people might not have heard about or stuff that's, you know, in progress about to hit that you want to
[3536.62 → 3540.48] share? Well, so a couple of things, I want to mention a few companies that are doing some really
[3540.48 → 3546.26] interesting work with serverless observability. So with our traditional applications, and we're
[3546.26 → 3551.34] running servers, or even if we're running containers, we can install all kinds of daemons and bots and all
[3551.34 → 3556.58] kinds of things that are running there that can listen and know what our CPU usage is and know if
[3556.58 → 3560.32] we're, you know, exceeding memory or if there's something happening there. And that just gives us a
[3560.32 → 3565.40] bunch of reporting. With serverless, obviously the functions themselves are ephemeral. So they spin up
[3565.40 → 3569.90] and then when no one's using them, they go to sleep again, or they actually disappear completely.
[3569.90 → 3576.94] So you can log information to, you can log information to CloudWatch logs and then kind
[3576.94 → 3582.72] of go through it. But seeing the whole sort of process from request to processing and then maybe
[3582.72 → 3586.68] through a couple of different services, managed services, and then being able to see the result.
[3586.88 → 3590.52] And then if there's something that happens there, tracking the billing, there's just all kinds of
[3590.52 → 3595.30] things that you really don't have good access into other than sort of pouring through the
[3595.30 → 3600.82] logs yourself. And even that is sort of a pain. So there are a bunch of companies. Dash bird is one
[3600.82 → 3607.16] that has an observability platform. Epsilon just launched their product yesterday, actually, which is
[3607.16 → 3612.40] a serverless observability and tracing platform. And they do some pretty cool things in the space.
[3612.72 → 3616.84] There's a company called Tundra, which was a spinoff of Ops Genie, which just got bought by
[3616.84 → 3621.64] Atlassian. So there are a bunch of companies in the space. Plus there's a whole security aspect
[3621.64 → 3625.96] around this, which we didn't really talk about. And a company called Pure Sec, they're out of Israel
[3625.96 → 3630.26] as well. ORI Segal is the CTO over there. And they're doing some really great work in terms
[3630.26 → 3634.72] of building tools that help with things like event injection and other things that could
[3634.72 → 3639.12] potentially, you know, remote code execution, other things that are still possible and are
[3639.12 → 3643.68] attack vectors against serverless. So there are a lot of companies that are building some really,
[3643.68 → 3649.00] really cool stuff. A lot of companies getting funded. So Pure Sec just got funded with another
[3649.00 → 3653.48] $7 million, I think. So, and then obviously serverless has raised money and a couple others.
[3653.62 → 3659.02] So there are some interesting things happening, some cool tools being built. AWS Lambda just
[3659.02 → 3663.14] announced their 15-minute execution times, which is kind of a big thing, as well as that
[3663.14 → 3669.16] application view. And one of the guys I know at AWS has said, you know, look, reinvent is coming
[3669.16 → 3674.16] up in a couple of weeks here, five weeks or whatever it is. And they haven't even scratched
[3674.16 → 3676.72] the surface of what they're going to, you know, what they're going to launch. They said they're
[3676.72 → 3679.90] basically going to blow people's minds with new stuff that's coming down the pike for,
[3679.90 → 3685.08] for serverless. So it should be some exciting times very, very soon, or it already is,
[3685.24 → 3686.64] but there'll be more exciting times.
[3687.02 → 3691.42] Very cool. And what's the if someone wants to get started with this and just kind of play around
[3691.42 → 3694.50] it, what is the easiest way in your opinion to do that?
[3694.64 → 3695.82] Yeah. So please don't say Lambda.
[3696.34 → 3700.88] I'm not going to say Lambda. I'm going to say serverless framework, because I do think that
[3700.88 → 3706.22] the serverless framework version one that that's out now, it's very easy for you just to say,
[3706.22 → 3710.30] I want to launch to Lambda. I want to launch to Azure. Furthermore, I want to launch to Google cloud
[3710.30 → 3715.06] functions or whatever. They're all different levels of functionality that you can do. Obviously,
[3715.34 → 3719.90] again, Lambda is light years ahead of some of these, and there are a lot more capabilities
[3719.90 → 3723.82] there, but certainly if you just want to kind of play around with it and write a couple of
[3723.82 → 3728.02] functions and see how they kind of all work with one another, any of the cloud platform
[3728.02 → 3732.38] providers are great. I mean, the major ones are doing some great work. Microsoft has got
[3732.38 → 3738.38] some good stuff with Azure and the IBM Opens stuff is very, very good. And they've got some
[3738.38 → 3742.00] cool stuff with durable functions and there are all kinds of great stuff that's kind of happening,
[3742.34 → 3746.34] which is why we do need some consolidation or not consolidation, but some standardization
[3746.34 → 3751.94] so that it'll be easier to kind of go between different providers. But I would say download the
[3751.94 → 3757.28] serverless framework, serverless.com. And there are a bunch of help guides out there. There's a bunch of
[3757.28 → 3763.38] get-started guides and things like that. It's super simple to play around with, but there is,
[3763.78 → 3768.30] don't be afraid of the frameworks. Don't be afraid of the deployment and stuff like that.
[3768.52 → 3773.88] It's just writing code. So write some code that takes the event in and do something with it,
[3773.96 → 3779.78] spit something back out, and you'll be surprised how easy it is to get started with this. And what's
[3779.78 → 3785.06] nice about serverless framework is once you're ready to actually put it up on the web, and you want to
[3785.06 → 3792.46] actually see it in real time, you just SLS deploy or serverless space deploy. And it just puts it up
[3792.46 → 3796.32] there for you. It handles all the deployment, all the configuration. And then you just,
[3796.44 → 3800.16] you get a URL endpoint back, and then you can go ahead and start playing around with it.
[3800.80 → 3804.52] One last question that came in from the Slack. If somebody's listened this far,
[3804.62 → 3808.76] is there anything that we haven't covered that they should not leave without knowing? Like
[3808.76 → 3812.96] particular resources, talks to go listen to, other types of things?
[3812.96 → 3818.62] Yeah. So there is a ton of, there's a ton of information out there and I, we probably just
[3818.62 → 3824.42] scratched the service of most of this stuff with serverless, but there are, there were a number of
[3824.42 → 3830.22] conferences that have been based around serverless, which if you want to watch some videos, serverless
[3830.22 → 3836.44] cone, which was, they just had their last one in San Francisco. I think it was in August. If you search
[3836.44 → 3842.34] for serverless cone, San Francisco, 2018 or something like that, you should be able to find
[3842.34 → 3848.18] on a cloud, a cloud. Guru, all the videos from it. And there are a bunch of 30 minute talks,
[3848.24 → 3852.08] a few five-minute lightning talks, and they talk about everything. And you've got everyone from
[3852.08 → 3857.06] Simon Wardley speaking to, um, you know, I think Ben Shoe was there. I mean, there's just a whole
[3857.06 → 3861.56] bunch of guys in the space that really, really know their stuff. That would be a great place to kind
[3861.56 → 3867.80] of go and watch a number, a number of videos, uh, that would really go deep into, you know, some of
[3867.80 → 3872.72] the challenges and some of the benefits and all the other things around serverless. Awesome. Well,
[3872.80 → 3879.22] thank you, Jeremy, for joining us for this week's JS party. Uh, Nick and Chris, awesome as always,
[3879.22 → 3885.86] and we'll catch you all next week. Thank you guys. Thanks. All right. Thank you for tuning in to JS
[3885.86 → 3893.32] party this week. Tune in live on Thursdays at 1 PM us Eastern at changelog.com slash live. Join the
[3893.32 → 3897.56] community and slack with us in real time during the shows head to changelog.com slash community
[3897.56 → 3902.86] and do us a favour, share this show with a friend or just an Apple podcast, go into overcast and
[3902.86 → 3908.52] favourite it. And thank you to fast our bandwidth partner head to fastly.com to learn more. And we
[3908.52 → 3912.94] move fast and fix things right here at changelog because of roll bar. Check them out at rollbar.com.
[3912.94 → 3918.38] We're hosted on Leno cloud servers at the leno.com slash changelog. Check them out and support this
[3918.38 → 3923.38] show. Our music is produced by break master cylinder, and you can find more shows just like this
[3923.38 → 3926.72] at changelog.com. Thanks for tuning in. We'll see you next week.
