[0.00 → 5.24] It's not proper continuous integration if it takes more than 10 minutes to get feedback,
[5.24 → 10.28] which is essentially about drawing a line somewhere, saying what's good enough.
[10.68 → 17.74] And the idea is its good enough if, as a developer, you don't completely lose focus while you wait.
[18.16 → 20.10] And it's kind of around 10 minutes.
[20.58 → 27.70] And if you wait any longer, you might still remain focused for 15, but going more, it just sucks.
[27.70 → 37.66] For me, from a developer point, it's like somebody took away my keyboard, and I'm not able to do my work, do what I enjoy, which sucks.
[39.96 → 42.66] BAM with for Changelog is provided by Vastly.
[42.96 → 44.84] Learn more at Fastly.com.
[45.08 → 47.36] Our feature flags are powered by Launch Darkly.
[47.64 → 49.46] Check them out at LaunchDarkly.com.
[49.70 → 51.54] And we're hosted on Leno cloud servers.
[51.94 → 55.46] Get $100 in hosting credit at Leno.com slash Changelog.
[55.46 → 57.32] What's up, Gophers?
[57.32 → 63.66] Our friends over Gravitational made a big transition at the end of 2020 to rebrand as Teleport
[63.66 → 67.06] and shared a new product announcement to showcase the direction they're taking.
[67.42 → 74.06] Teleport is operating from a vision of being able to run and access software anywhere in a secure and compliant manner,
[74.38 → 76.48] something they call environment-free computing.
[76.86 → 83.32] With Teleport, engineering teams can quickly access any resource anywhere using a unified access plane
[83.32 → 90.22] that consolidates access controls and auditing across all environments, infrastructure, applications, as well as data.
[90.56 → 97.24] Teleport server access lets you SSH securely into Linux servers and smart devices with a complete audit trail.
[97.58 → 103.52] Teleport Kubernetes access lets you access Kubernetes clusters securely with complete visibility to access and behaviour.
[103.52 → 110.30] And finally, Teleport application access lets you access web apps running behind NAT and firewalls with security and compliance.
[110.30 → 114.36] Try Teleport today in the cloud, self-hosted, or open source.
[114.70 → 117.30] Head to goteleport.com to learn more and get started.
[117.68 → 119.66] Again, goteleport.com.
[138.14 → 139.04] Let's do it.
[139.04 → 140.70] It's go time.
[141.44 → 142.84] Welcome to go time.
[143.02 → 146.16] Your source for diverse discussions from around the go community.
[146.72 → 151.12] We record the show live on Tuesdays at 3 p.m. U.S. Eastern.
[151.48 → 154.94] Watch along with your eyeballs at YouTube.com slash changelog
[154.94 → 159.96] and participate in the live chat by joining the go time FM channel of go for slack.
[160.44 → 162.06] Okay, let's talk CCD.
[163.06 → 164.12] Here we go.
[164.12 → 164.16] Here we go.
[169.04 → 173.48] Hello, everybody.
[173.76 → 174.78] Welcome to go time.
[175.02 → 177.34] Today we are joined by Marco Anastasia.
[177.48 → 178.44] Marco, do you want to say hi?
[178.94 → 179.60] Hello, everyone.
[179.76 → 180.54] Thanks for having me.
[181.10 → 183.50] And we're also joined by Jerome Jettison.
[183.86 → 184.84] Jerome, you want to say hi to everybody?
[185.18 → 185.70] Hi, everyone.
[185.70 → 192.22] So Marco is the co-founder of Semaphore, which is a continuous integration, continuous deployment service.
[192.82 → 195.70] And Jerome was part of the team that created Docker.
[196.14 → 198.02] He plays a dozen musical instruments.
[198.34 → 200.56] And you also teach containers and Kubernetes.
[200.70 → 201.16] Is that correct?
[201.42 → 202.04] Yep, absolutely.
[202.04 → 202.32] Okay.
[202.76 → 205.78] And then we're also joined by Chris Brando, our other host.
[206.06 → 206.66] Chris, you want to say hi?
[206.84 → 207.50] Hello, everyone.
[208.04 → 208.36] All right.
[208.46 → 214.58] So if it wasn't clear by the guests, today we're going to be talking about continuous integration and continuous deployment.
[215.10 → 218.02] So I guess to kick it off, let's just start with something basic.
[218.28 → 221.00] What is continuous integration and continuous deployment?
[221.00 → 233.18] So continuous integration is essentially a process of frequently integrating each other's work as developers into some kind of central branch.
[234.24 → 244.62] And for a lot of us, as a developer, when you think about it, the association is tests and building and testing your code.
[245.78 → 248.22] And yeah, that's kind of why is that?
[248.22 → 258.42] That's because in order for us to integrate often, we need to kind of figure out very quickly if what we're integrating works.
[258.42 → 265.60] So that's what kind of got us to the practices of automation and having automated tests.
[267.18 → 276.20] Continuous delivery is kind of a broader method of developing software in which you apply a set of practices,
[276.20 → 283.96] one of which is continuous integration, where you make sure that your code is always in a deployable state.
[284.78 → 294.66] And typically that in practice, that means that at least your deployment process, which follows after running tests,
[294.78 → 299.60] is also automated and usually simple enough and robust enough.
[299.60 → 305.10] So a follow-up question I would have is, why is it that we always see these terms together?
[305.44 → 314.62] Like CI, CD is almost like a single term these days when it sort of sounds like they're actually separate things that just kind of get bundled together.
[315.30 → 315.52] Yeah.
[315.52 → 324.62] I think, for example, in my kind of personal journey as a developer, I first discovered continuous integration.
[325.68 → 335.64] And, you know, I was led to it by through basically realizing the importance of automated tests and, you know, getting feedback often.
[335.64 → 342.64] And I think that's like probably it's a, you know, frequent case.
[343.32 → 352.18] On the other hand, deployment is, you know, even when you're having a prototype, and you don't have any tests, and you're not even thinking about CI, you are.
[352.80 → 354.06] And maybe it's a web app.
[354.16 → 355.50] Maybe it's a hobby project.
[355.68 → 359.52] You know, the way you're deploying it basically continues deployment typically, right?
[359.58 → 362.42] So maybe you do a git push and it goes live.
[362.42 → 374.40] So there's some kind of mix in terminology because these two things are typically done together in teams of a certain size and code bases of a certain size.
[374.92 → 387.82] It's just that when you maybe talk about just continuous delivery, for example, it's maybe too ambiguous for people to also assume that, you know, to understand that it includes CI.
[387.82 → 392.54] So the way I see it, it's like, you know, just so we know what we're talking about.
[393.30 → 393.58] Okay.
[394.04 → 403.14] So if we're looking at this, you know, CI, CD, what problems do it solve that would sort of cause a company to want to look into it?
[403.38 → 406.34] Why is it something that's taken off and, you know, been adopted so much recently?
[406.34 → 423.96] I think it's all a matter of developer velocity, like being able to ship things faster so that we shorten the time it takes between the moment when I hit save in my code editor and the moment when I can see if my stuff works or not.
[423.96 → 431.26] I remember when I was a teenager, I was lucky to have my dad who wrote code, among other things.
[431.50 → 438.20] And I remember somewhere I saw something on like, I think it was an ad for Turbo Pascal.
[438.58 → 443.40] And there was something like, oh, that thing can compile, I don't know, like 57,000 lines per second.
[443.40 → 455.40] I don't remember the exact figures because that was a long time ago, but I remember back then I was thinking, what's the point of a thing that can compile more code that I'm maybe ever going to write my entire life in one second?
[455.88 → 457.62] Why is that an important figure?
[457.62 → 476.32] And long after, I kind of thought, well, maybe it matters because usually when we compile a big code base, you know, the XKCD joke when you see like the folks on their office chairs, and they're like fighting with sword sticks and the boss comes up and is like, hey, what are you doing here?
[476.36 → 478.58] Like, oh, we're just waiting for to compile to finish.
[478.68 → 479.70] And they're like, oh, OK, fine.
[480.18 → 483.74] So back then we were waiting for stuff to finish compiling.
[483.74 → 489.08] And today we are waiting for, you know, like knowing that the code works.
[489.28 → 493.66] So it has to go through build and maybe some deployment and some test environment.
[493.92 → 498.36] And then we need to wait for like people to actually QA the code, et cetera.
[498.76 → 503.90] So if we can automate as much of these steps as possible, we're saving time.
[503.90 → 524.76] If I can hit save, push to a branch or whatever, and then I know that there is a bunch of automation that's going to build my code, test it, deploy it in some staging environment, and then send me, you know, a notification, whether it's Slack or whatever, to let me know, hey, your code is deployed on this staging environment.
[524.98 → 525.86] Now you can have a look.
[525.86 → 528.46] Maybe it's me who's going to have a look.
[528.56 → 537.50] Maybe it's somebody from QA or some co-worker or the peer or the manager who asked me to deliver that specific feature.
[538.48 → 555.02] And so if we can shorten that time, you know, if instead of taking a whole day because I have to open a Jira ticket for somebody to put my stuff in production, if it's done automatically in five minutes, then it means I can iterate every five minutes instead of iterating every day.
[555.02 → 557.08] So I can iterate multiple times an hour.
[557.28 → 563.38] I can make multiple experiments and multiple mistakes multiple times an hour instead of just once per day.
[563.86 → 565.82] So to me, that's what it's all about.
[565.94 → 576.00] It's making it so that I can try many things quickly and that I can fail fast and fix my bugs and try again.
[576.00 → 585.08] And at the end of the day, I was able to try and fail and eventually succeed maybe 10, 20, 50 times instead of just one time.
[585.72 → 586.16] That makes sense.
[586.72 → 600.74] So like when you were talking about that, you mentioned pushing to a staging environment and, you know, having QA and processes that in general, at least in my head, I sort of associate with larger projects rather than, you know, a small project with one or two developers, perhaps.
[600.74 → 607.14] Would you say that this is something that becomes more valuable as the team size grows and the project scale grows?
[607.22 → 610.06] Or is it something you tend to use no matter what the team size?
[611.10 → 611.46] Both.
[611.72 → 615.52] I would say like a while ago, yeah, I would have agreed like, oh, this sounds extremely complicated.
[615.66 → 618.18] I don't know if I want that for my little pet project.
[618.18 → 623.78] And I think there were a couple of things that made me kind of change my mind about that.
[623.86 → 630.74] The first one was, I think, when I saw Heroku more than a decade ago, just when I joined.cloud.
[630.86 → 632.96] So the company that would eventually become Docker.
[633.62 → 637.46] And Docker was initially a past company like competing with Heroku.
[637.46 → 645.74] And the ability to just push my code and instead of pushing it to a repo, I push it to something that builds and deploys it.
[646.00 → 647.10] That was great.
[647.28 → 648.86] And that was really easy to do.
[649.02 → 651.54] And that was the whole point of Heroku.
[651.72 → 657.74] And that's what.cloud was emulating and adding support for other languages and so on and so on.
[658.16 → 662.40] And that worked even for tiny little projects.
[662.40 → 684.68] In a way, I would almost say, especially for tiny little projects, what I mean is that, for instance, if somebody wants to get started with Django or Rails or your favourite JavaScript framework of the week, or even with Go now, you have to think about, okay, where and how am I going to deploy that?
[684.68 → 695.22] Sure, if I'm just deploying one microservice API backend, it's just one Go service and nothing else, there aren't really many questions to ask.
[695.68 → 705.12] But if I have, let's say, this little API endpoint and maybe some static assets that go through a little optimization pipeline and whatever, then it starts making sense.
[705.12 → 717.18] Like, if I can push instead of run a bunch of manual commands and a bunch of scripts and need a bunch of API keys and whatever, and then eventually see my thing deployed.
[717.44 → 729.24] Like, if I can simplify that, I kind of, I lowered the bar to get something deployed live that folks can see and that they can work on.
[729.64 → 732.56] So I think even for small projects, that makes a lot of sense.
[732.56 → 745.20] I think this is a very important point in a way, like, even if you don't maybe initially plan or at all to write tests, it's really a good idea to set up a deployment pipeline.
[745.84 → 748.52] Assuming you're building something for other humans, right?
[748.52 → 753.90] So if you just, you know, then the idea is just made that process.
[754.12 → 764.22] Like, once you're done writing the codes, you know, automate everything that needs to happen next until, you know, other people can see it or use it.
[764.54 → 766.62] Make it, you know, basically one command.
[767.74 → 776.90] And the thing that, you know, typically does all the work, if it's multiple steps in between, then, you know, that's the task for the CD pipeline.
[776.90 → 783.80] So are there situations where you think that using continuous integration or continuous deployment is a bad idea?
[784.28 → 788.34] Or maybe not a bad idea, but perhaps something that might not provide as much value?
[788.34 → 796.52] Perhaps when it takes a lot of effort for some reason, you know, like, it's the kind of thing that it's a good idea to do it.
[796.52 → 812.84] But if it makes you jump through extremely complex hoops and, you know, if it makes you waste a lot of time because of the setup or because of this very peculiar, special setup that you have, then, yeah, then I could question it.
[813.20 → 815.08] But this shouldn't become an excuse.
[815.20 → 818.00] Like, we shouldn't say, oh, my app is special so I can do CI.
[818.00 → 821.70] It's more like, well, I prefer the yes and approach.
[821.92 → 826.82] Like, well, yes, I should do CI, and currently I cannot because this and this.
[826.90 → 831.08] But once I have solved this special problem, then I will be able to do it.
[831.40 → 835.56] For instance, in the Kubernetes ecosystem, a while ago, I had this thought.
[835.62 → 842.32] I was like, wow, I really wish I could run a bunch of tests on the brand-new Kubernetes clusters each time.
[842.32 → 850.00] Imagine, like, you push your code and the thing is going to deploy a complete cluster and test the code on the cluster and then tear down the cluster.
[850.64 → 861.36] And a few years ago, that seemed, I wouldn't say impossible, but kind of ridiculous maybe because, like, okay, this is going to take a lot of resources, a lot of time, et cetera, et cetera.
[861.36 → 874.70] And today, you can use something like Kind, for instance, to do that very easily and very quickly just because things evolved a lot, and we got lots of contributions, new projects, et cetera.
[875.18 → 885.88] And so things that seemed extremely complicated and expensive a while ago now are super commonplace and relatively easy to do.
[885.88 → 897.66] And so I think it's great to not set anything in stone and accept the yes, I cannot do it today because X, but once we solve X, then I will be able to do it.
[898.16 → 904.74] Yeah, I would also add that there are also consider that there are different flavours, for example, of continuous delivery.
[904.74 → 918.56] Maybe you're working in an industry where, you know, it's just not possible, like regulations do not allow or, you know, you don't want to maybe continuously deploy changes to the code that runs the airplanes or medical devices.
[918.56 → 927.34] And on the other hand, continuously deploying changes of a complex code base, which has no tests is a very, is a huge risk.
[927.82 → 937.92] And, you know, such teams are not really continuously deploying, but, you know, they are aware of the risks, and they have usually a very elaborate kind of process.
[938.10 → 943.66] You know, maybe they do it weekly or monthly and there are several people involved who need to sign off.
[943.66 → 949.64] There's a, you know, QA team going through scenarios, checking everything all the time.
[950.78 → 956.52] So there are different, you know, like kind of, I would say, maturity levels in each situation.
[957.12 → 963.98] For the CI, it's like, I would maybe rephrase it, like, does it make sense to write automated tests for that project?
[964.26 → 966.62] And then maybe it becomes a little more clear.
[966.62 → 972.98] So maybe you, you know, if you're just prototyping, you don't exactly know what you're going to end up with.
[973.46 → 978.34] Writing tests may not be, it may not be the right time to be, you know, test driven.
[979.12 → 987.92] But as soon as you have some clarity on what you're building and, you know, you're working towards having that somehow, you know, see the light of day, you know,
[987.92 → 1000.44] again, in the hands of some kind of user, whether the user is another developer or just a user where you basically have some kind of agreement that what you're going to write should work.
[1000.86 → 1004.16] I kind of see no reason not to write at least some tests.
[1004.98 → 1011.94] And, you know, if it's a kind of maybe a lack of practice or skill, you know, you know, fine, you know, but that's maybe a different subject.
[1011.94 → 1013.36] Like, how do you get better at it?
[1013.36 → 1021.68] Marco, you mentioned like deploying in cases where like regulations don't allow it, for example, deploying to an airplane, like software for that.
[1022.32 → 1028.12] I think, at least in my mind, most of the time when I think about CCD, it's like more web apps.
[1028.46 → 1028.56] Yeah.
[1028.72 → 1030.86] But I know that it can be used in other scenarios.
[1031.16 → 1037.66] So like, do you have any experience or can you sort of speak to what that setup might be like and what delivery means in that sense?
[1037.66 → 1050.28] You can only kind of think about from the customers of Semaphore who are working in some other types of some maybe non-usual industries, at least in for most developers.
[1051.20 → 1053.64] But on top of my head, I wouldn't know.
[1053.80 → 1063.76] Like in most cases, like a lot of industries are kind of being transformed and, you know, everybody's writing some kind of web app, some kind of maybe mobile app.
[1063.76 → 1073.62] I was recently talking to some people who were working on some satellite technology, which were you kind of, it's not a web app, it's not Linux or anything.
[1073.80 → 1076.64] It's, you know, a real-time operating system.
[1076.64 → 1093.74] In that case, in such scenarios, also kind of recalling some experiences from my early career when I worked on some embedded systems, writing tests is not so widespread in those projects.
[1094.02 → 1095.62] It's more about manual QA.
[1096.20 → 1102.12] And then there is some kind of release cycle, definitely less frequent than daily.
[1102.12 → 1102.76] Okay.
[1102.76 → 1120.62] I was about to mention, like, when you deploy stuff that runs in space or in airplanes or something like that, you can definitely do CI, but CD is not really an option just because the deployment itself can't happen as easily and automatically as pushing to a server.
[1120.62 → 1135.64] And so that's actually a bunch of industrial processes and industrial code where, yep, like, ideally you can do some CI, but it's often pretty complicated because you have to mark a bunch of things.
[1136.10 → 1145.38] And then CD is not really an option because it's, the code runs in air-gapped environment, or maybe I should sometimes say space-gapped environment.
[1146.10 → 1148.68] So these are very specific environments, of course.
[1148.68 → 1157.42] Yeah, but I was actually recently looking up, there's this language called Verilog, which people use to write basically chips.
[1157.76 → 1162.80] You define chips in code and there is a TDD framework for Verilog as well.
[1163.02 → 1166.60] So, yeah, things have progressed everywhere, I would say.
[1166.88 → 1170.90] I think another area where you might do CI and not do CD is library development.
[1170.90 → 1182.08] So if you're not building something that's going to actually run on a server somewhere, but someone else is going to consume, that would definitely be a candidate for like, I still want to run all my tests and make sure everything's working, but I'm not going to deploy anywhere.
[1182.14 → 1185.58] I'm not going to make a release for every commit I merge or issue I close.
[1185.58 → 1194.90] I've seen some software where they like, do a build of like the binaries they're going to have, and then they actually have tests that run with the binaries that like stub out some stuff.
[1195.00 → 1197.74] So like when they're calling Git or whatever else.
[1197.74 → 1202.10] So they still almost do continuous delivery in the sense that they make a binary.
[1202.42 → 1204.52] It's just not one that actually gets shipped to users.
[1205.04 → 1209.18] So it's like a weird middle ground where it does most of the things.
[1209.26 → 1212.46] They just don't, you know, you don't want to release a new version to your user every two hours.
[1212.56 → 1213.50] That would be pretty awful.
[1214.04 → 1216.30] But you can still get some of the benefits.
[1216.30 → 1222.10] And then finally, like once a week, actually bundle it all up to be one final binary that, you know, has been tested all week long.
[1227.74 → 1231.28] Hey, Gophers, this episode is brought to you by our friends at Launch Darkly.
[1231.62 → 1235.98] Feature management for the modern enterprise, power experimentation and production.
[1236.38 → 1237.10] Here's how it works.
[1237.50 → 1242.32] Launch Darkly enables development and operation teams to deploy code at any time.
[1242.32 → 1253.56] Even if a feature isn't ready to be released to users, wrapping code with feature flags gives you the safety to test new features and infrastructure in your production environments without impacting the wrong end users.
[1253.56 → 1261.58] When you're ready to release more widely, simply update the feature flag and the changes are made instantaneously by the real-time streaming architecture.
[1261.96 → 1266.48] Eliminate risk, deliver value, get started for free today at LaunchDarkly.com.
[1266.48 → 1268.26] Again, LaunchDarkly.com.
[1283.56 → 1298.96] So when we're looking at CI and CD, like what is the typical setup you guys see?
[1299.54 → 1303.08] What tools are being used and, you know, why are those tools useful?
[1303.74 → 1307.00] I don't know if there is really a typical setup to me.
[1307.00 → 1314.78] Like the core thing is that there is always an ocean of a pipeline, even if it's not really all that way, but it's a sequence of operations that we run.
[1315.52 → 1326.00] And I think you can, if you look at the configuration options and how people run, whether it's Semaphore, Travis, Jenkins, et cetera, it's always the same of our principle.
[1326.18 → 1328.44] It's like, okay, we prepare the environment.
[1328.44 → 1331.04] You run the things, you run a bunch of tests.
[1331.16 → 1340.54] Maybe there is some metrics going on because you have many combinations of versions of things to test, and you need to collect all these logs.
[1340.68 → 1343.26] And at the end, you get like a yay or nay.
[1344.04 → 1351.68] And then in tooling, what I've seen is that there is what I would call maybe the venerable ones, the ancient ones.
[1351.68 → 1362.40] And so I'm thinking, for instance, yeah, tools like Travis or Jenkins, for instance, just to give one in the SaaS space and one in the more like on-prem space.
[1362.66 → 1370.60] And then there have been a lot of new tools that appeared to leverage new stuff.
[1370.78 → 1372.54] Like obviously containers happened.
[1372.74 → 1374.92] So we want a way to leverage that.
[1374.92 → 1383.66] And very often the more ancient platforms did not allow that or at least not that once or not elegantly.
[1384.14 → 1394.58] And so that made a space for a bunch of new players to be like, okay, we're going to support containers and a bunch of other technologies like from day one.
[1394.58 → 1407.94] And in a way that makes sense for people who actually write Dockerfile and want to run their code in containers, as opposed to just want to tick a box saying like, oh, yes, our CI thing supports containers.
[1408.10 → 1409.88] But that just means they're using it somewhere.
[1410.62 → 1421.28] So that's, yeah, on the tools themselves, it would be this kind of 2D, you know, like a matrix with kind of on-prem and then more SaaS-oriented,
[1421.28 → 1425.40] even though many tools actually go play on both sides.
[1426.12 → 1437.86] And to me personally, I kind of see it's not a very clear line, but, you know, like the pre-container and the post-container environments almost.
[1438.44 → 1439.26] It's pretty telling.
[1439.92 → 1445.40] When I first started seeing CI, like for the first time, I know it was with a lot of tools like Travis,
[1445.40 → 1451.36] where it definitely felt like you could just take what you had, and it would somehow magically make it work.
[1452.28 → 1456.18] Whereas now it seems like most of the new products just have to support containers.
[1456.54 → 1461.86] And then it almost feels like since that's become so widely adopted, one of the upsides, at least to using them,
[1461.90 → 1466.18] is that you can generally sort of pick and choose the tools that seem right for your setup.
[1466.82 → 1471.10] Whereas I know before, like when you're using Travis, like it would magically work most of the time.
[1471.10 → 1475.16] But if something didn't work, it could sometimes be a pain to figure out,
[1475.26 → 1480.32] well, how do I test this really weird scenario where I need, you know, some random software installed on the server.
[1481.12 → 1482.64] So, yeah, I definitely say that.
[1482.96 → 1490.78] Is that true in your opinion that the ecosystem has sort of evolved because of how prevalent like Docker and containers have become?
[1491.72 → 1491.88] Sure.
[1491.88 → 1503.82] Docker was very disruptive for the CI and CD space because it introduced basically an entirely new abstraction process of,
[1503.82 → 1506.14] you know, building, testing, deploying software.
[1506.60 → 1515.00] Like typically developers previously did not deal with, you know, the things that Docker represents.
[1515.00 → 1525.00] And so for, you know, all the CI, for example, Semifor is a cloud-only service.
[1525.88 → 1528.04] So that's kind of what I know best.
[1529.00 → 1538.98] And for example, there's this, the early cloud-based services like Travis or Semifor had very simple kind of capabilities.
[1538.98 → 1549.50] Like you could, in terms of the kind of workflows that you could run, basically you could have a sequence of steps or maybe a sequence of parallel jobs.
[1550.12 → 1551.20] And that's pretty much it.
[1551.34 → 1557.22] Maybe some services had also a separate deployment step, but some even didn't have that.
[1557.22 → 1570.26] And so if you, you know, in case of Docker containers, even if you don't have that problem, John, that you described, like there's something weird, and maybe I want to kind of define my own environment with a container.
[1570.52 → 1575.94] Like maybe I'm just, you know, I don't have that problem, but I need to build a container.
[1576.22 → 1578.42] So, you know, that's what I need to ship to production.
[1579.16 → 1585.74] When you start, like when you do a build, so you build a container and then maybe you have a relatively large test suite.
[1585.74 → 1587.50] So you want to parallelize it, right?
[1588.00 → 1598.74] So you need to, you would ideally build a container once and then like the term is fan out to several parallel jobs and reuse that container.
[1599.46 → 1603.98] Like not rebuild it like five times, but, you know, reuse it five times.
[1604.32 → 1615.28] That's where, you know, early version of Semifor, for example, we basically had to reinvent what Semifor was at one point a few years ago because of this and some other scenarios we wanted to support.
[1615.74 → 1616.70] Like this was not possible.
[1616.94 → 1619.52] Like you had to rebuild a container in all the parallel jobs.
[1619.52 → 1626.42] And then that's like when you're actually working with containers all day, it's like it's not really acceptable.
[1626.42 → 1635.14] And then it suddenly doesn't matter how good and useful and beneficial to you, you know, that CI tool was previously.
[1635.30 → 1636.98] Suddenly it's just like not the right fit.
[1636.98 → 1648.52] But from the CI provider standpoint, to make that new scenario possible and a bunch of others that are kind of related and maybe not so obvious, it's a lot of work.
[1648.92 → 1660.74] So, you know, some of us who were doing, you know, cloud-based CI, you know, we had to basically reinvent our solutions or not, you know, some have not done it.
[1660.74 → 1664.12] So, or some new players obviously appeared.
[1664.36 → 1668.42] It was a pretty, you know, important change in the industry.
[1668.42 → 1681.76] So when you're talking about running this continuous integration, and you had said that even if you don't need a separate environment, like, you know, you can basically fan out the builds.
[1682.18 → 1684.08] Why is that speed important?
[1684.08 → 1698.08] Like, I guess the way I would phrase this is I've definitely been in teams that have quick, like, feedback from continuous integration and then other teams where continuous integration is something where you push your code, and then you check 15 minutes later to see what's happening.
[1698.46 → 1701.94] So can you sort of speak to, like, how that affects the developer experience?
[1702.12 → 1712.14] I think it comes back to what I was explaining earlier about iterating faster and being able to try and experiment more things in a given day.
[1712.14 → 1718.84] There is a kind of quest for the fastest deployment time.
[1719.06 → 1739.40] I think that's almost verbatim the title of a talk by Helen Corps who works at Tilt and has this amazing talk which is about how long or rather how short can it be between the moment when I push the button and my code ends up running on my Kubernetes cluster.
[1739.40 → 1746.70] And I think the answer is something like you can go all the way down to four seconds or something like that.
[1746.70 → 1752.22] Of course, in that case, we're not talking about CI or, you know, it's a kind of very special case.
[1752.62 → 1756.06] But that address is exactly like that need for speed.
[1756.22 → 1762.46] It's like, and I think, you know, like for most of the codes that we write, this is maybe not required.
[1762.84 → 1765.16] You know, because I can test things locally.
[1765.38 → 1768.80] Ideally, I can just like save, build, and I try my thing and it works.
[1768.80 → 1784.26] But if I'm working on something more complex that interacts with an environment that is really hard to mark, like for instance, I don't know, let's say you write a Kubernetes operator because that's a super fashionable thing these days and many people do that.
[1784.40 → 1789.66] So you end up like writing your thing in Go, and then you need to run it on a Kubernetes cluster.
[1789.66 → 1794.78] And so especially when you learn in the beginning, I did that recently.
[1795.30 → 1805.16] And I honestly, you know, it's the kind of thing where you're trying to put things together from the docs and the sample code that you've seen and the idea you have in your head of how it works.
[1805.58 → 1810.94] But a number of times when I just like to put a line here and honestly, I had no idea what it would do.
[1810.94 → 1821.34] I was hoping it would get me closer to what I wanted, but I really had no other option than like trying it out and, you know, like poking at it and see what happens.
[1821.88 → 1827.50] So in that case, of course, I'm not in CI, but I'm in hopefully some kind of CD.
[1827.70 → 1829.90] Like if I can work locally, that's great.
[1829.90 → 1847.64] But if I need to interact with a big cluster that has a bunch of like pods and containers and load balancers, et cetera, then I, I mean, in that case, I need to deploy to maybe not the real thing, but at least a thing that is real enough for my tests.
[1847.64 → 1849.54] And then I want that to be fast.
[1849.68 → 1863.32] Because again, if I'm in that learning stage where I'm at the point, you know, of print debugging and things like that, that ideally we shouldn't do them, but sometimes we still have to fall back to that.
[1863.58 → 1867.94] And well, in that case, I want things to build and deploy really quickly.
[1868.22 → 1872.22] And I'm willing to take a lot of shortcuts to make that happen.
[1872.22 → 1876.60] Just like in the example I was giving, for instance, I don't, I'm not talking about CI yet.
[1876.60 → 1877.98] I'm, I'm just learning.
[1878.26 → 1884.88] And I think it's also an important point in modern CI and CD pipelines.
[1884.88 → 1901.00] It's the how can we shortcut some parts or how can we make the thing suitable both for, you know, for local development experimentation and then get that as close as possible to the CI and CD form.
[1901.50 → 1904.42] And I think like it's a need that I felt a lot of time.
[1904.42 → 1906.82] I was mentioning like Tilt recently.
[1907.28 → 1921.56] It's one of the tools which fills a big gap in the, well, container, but particularly Kubernetes ecosystem, because we still don't have a really nice developer experience with Kubernetes the way we, we had with Compose and Docker.
[1921.56 → 1925.90] And so when I saw that tool Tilt, I was like, wow, this is really great.
[1925.94 → 1928.82] And I started to kind of use and almost abuse it.
[1928.88 → 1934.94] And then I started to wonder, well, I described my whole stack with that tool, which is just for development.
[1934.94 → 1939.08] But now I want to make that into a deployment tool.
[1939.32 → 1941.12] Do I have to start all over again?
[1941.52 → 1944.74] And it turns out that other folks had similar ideas.
[1944.74 → 1965.84] And I realized, even though at first it was like a development tool, folks added some CI commands so that you can basically, you can say, okay, instead of just spinning up all my services and containers, et cetera, and then work with this development cycle, iteration, change code, save, et cetera.
[1965.84 → 1976.06] Now you work more in a CI mindset where you run the tool to bring everything up once, perhaps run your tests and shut everything down.
[1976.56 → 1989.10] I think there's going to be a lot of evolution in that space because we have great CI tools, great CD tools, great local development tools, great this and that.
[1989.10 → 1995.70] But more and more, we need tools that are able to do both, like that can salsa and tango, not just one or the other.
[1995.84 → 2003.48] So one question I have is that, like most of the time when we're talking about CI, CD, like we're sort of thinking about something that we can run locally.
[2003.82 → 2008.54] And then we can sort of deploy it to sort of see how it works, you know, as a released product at that point.
[2008.86 → 2012.18] But you had mentioned like developer speed and like some of those different use cases.
[2012.46 → 2023.22] I guess one that I've always sort of questioned is, could there be a case where CI, CD almost replaces somebody running stuff locally if we got the feedback loop quick enough?
[2023.22 → 2035.66] And I guess one of the examples that came to mind for me was in a previous episode, we talked with the creator of Play With Go, which I think stemmed from Play With Docker, which I believe you have some familiarity with, Jerome.
[2036.34 → 2038.30] I don't remember if you were one of the creators of it.
[2038.44 → 2038.98] Is that correct?
[2038.98 → 2049.64] Well, it was created by two Docker captains, and I would butcher their names, so I don't want to pronounce them, but Marcos and Jonathan.
[2050.34 → 2062.90] And I helped a little bit in some points, but mostly by cheering and encouraging them because I think that what they made was really amazing at the time when all these tools like Katakana and so on were emerging.
[2063.48 → 2064.68] So yeah, I see what you mean.
[2065.08 → 2067.90] Yeah, I was sort of thinking about the Play With Go version, at least.
[2068.04 → 2072.84] It uses like Slang and some other stuff so that when you're writing a guide, it builds that all and pushes it.
[2073.32 → 2080.44] But at least right now in its current state, actually writing a guide means that you have to pull the whole thing, get it running locally, get all the scripts running locally and all that.
[2080.90 → 2090.72] Whereas if you want to sort of lower the barrier to entry, it would be ideal if somebody can just write the script and like have some sort of CI, CD pipeline that just spits out something and says, well, this is what it looks like roughly.
[2090.72 → 2093.50] Maybe it's not perfect, but it allows them to skip that.
[2094.04 → 2096.36] You know, I just want to write a two-page guide.
[2096.48 → 2099.84] I don't really want to have to figure out how to install this entire system and set it all up.
[2100.22 → 2101.02] Yeah, absolutely.
[2101.20 → 2101.80] I agree.
[2101.94 → 2107.30] I think in a way containers made it easy to do that between scare quotes like normal code.
[2107.30 → 2113.86] But now if my code is doing things with containers, then how do I put that in containers itself?
[2114.44 → 2119.02] And so that's how we had like projects like Docker and Docker and things like that.
[2119.18 → 2127.52] Or for instance, another project that I've seen recently and which I think for now is kind of flying under the radar.
[2127.52 → 2132.20] But when people will see what it can do, it's going to blow up.
[2132.28 → 2143.04] It's something called Symbol, which lets you basically to simplify, it lets you run the equivalent of privileged containers, but kind of safely or at least in a safer way.
[2143.04 → 2147.68] Which means that all the stuff like Docker in Docker or Kubernetes in Docker or etc.
[2148.08 → 2151.18] Other workloads where you typically think, oh, I need a VM.
[2151.62 → 2155.86] These things could be now like they could run in containers.
[2156.24 → 2159.72] And that's going to make a bunch of things doable.
[2159.90 → 2165.18] Just like I was seeing earlier, like a few years ago, I was like, no, I can't do that because that seems impossible.
[2165.18 → 2176.94] And then today with the new tools, the new, you know, it could be some kernel feature that you didn't see coming up and then unlock some fascinating use cases, etc.
[2177.58 → 2183.22] And so, yeah, CI and dev, I think these things are going to get closer and closer.
[2183.76 → 2187.22] Yeah, I would add to John's initial question.
[2187.22 → 2193.90] Like, I think large web apps, you know, over time, they develop a large test suite.
[2194.42 → 2201.14] You know, you have a lot of unit tests, which are maybe not so complex to, you know, run locally.
[2201.56 → 2208.50] But usually like end-to-end tests or acceptance tests are the, you know, more demanding ones.
[2208.50 → 2222.50] And what I've seen, like from our own internal experience, also, you know, a bunch of, a lot of some users is if you're developing some kind of SaaS, developers typically don't run the whole test suite locally.
[2222.78 → 2230.50] They just push the CI on feature branches because in CI, they have a very elaborate kind of parallelization and optimization.
[2230.50 → 2238.56] So, if they would run everything sequentially, you know, the total time would maybe even be above an hour.
[2239.42 → 2243.22] But in CI, they actually got it down to, you know, around 10 minutes.
[2243.50 → 2247.18] So, it's just more convenient to push and wait for feedback.
[2247.78 → 2251.16] It's also nice because in that case, you can sort of push and go back to work.
[2251.40 → 2251.58] Yeah.
[2251.78 → 2256.32] Whereas like running locally, at least you have to have a second tab or something open to let it happen.
[2256.44 → 2259.42] And it might slow down your computer, depending on what you were developing on.
[2259.42 → 2265.64] Because I know some people are running on like Chrome books and things like that where, you know, sometimes it's a little trickier.
[2266.12 → 2271.68] So, I guess to ask a question related to that and sort of step back at talking about tools again.
[2272.14 → 2275.26] If you were choosing tools today, let's say you have a web app.
[2275.46 → 2279.00] So, I think a lot of listeners build web applications or something along those lines.
[2279.32 → 2284.16] And you wanted to start off with continuous integration, continuous deployment or delivery.
[2284.16 → 2286.22] How would you go about choosing tools?
[2286.38 → 2292.04] And like where do you think they're going to get the most like bang for their buck if they're just trying to get something starting out?
[2292.24 → 2294.14] Like how would you go about thinking through that process?
[2294.92 → 2295.66] Excellent question.
[2295.82 → 2304.90] Like for me, like my personal approach is to try to aim for the simplest tool that would do the job.
[2304.90 → 2315.46] Not too simple because otherwise I can do what I do, but also not too complex because it's really easy to fall down the rabbit hole of complexity.
[2316.16 → 2323.74] Like for instance, I've seen so many folks going with Kubernetes or Docker just because they thought it would be the thing to do.
[2323.82 → 2324.44] Like it's fashionable.
[2324.44 → 2327.16] And then when we look at, okay, what are you running in it?
[2327.22 → 2333.74] And like, well, we just have, for instance, like Go microservices, or maybe it's only Python.
[2334.04 → 2341.92] And then when we look at it, like, well, are you really going to get something from, again, Kubernetes or Docker or whatever?
[2342.38 → 2346.46] Because maybe you are in one of these scenarios where you don't need that extra complexity.
[2347.16 → 2349.52] And in that case, I would be happy to do without.
[2349.52 → 2358.28] Like I'm happy to use something like Docker when there is a mix of different languages and some, let's say, exotic databases and things like that.
[2358.44 → 2365.56] Because when I land on a project like that, I know that it's going to take minutes, not hours or days to bring up the dev environment.
[2366.30 → 2372.60] But if all I have to do is like go get, go build, it's pretty hard to get easier than that.
[2372.98 → 2376.28] So I don't think I would point to a specific tool.
[2376.28 → 2379.96] You know, like I won't tell you like, oh, you should absolutely use that thing or that thing.
[2380.06 → 2390.54] But rather think about what's the easiest tool that's going to work for me and try to not overcomplicate things.
[2391.34 → 2393.10] So Marco, I assume you're a bit more biased.
[2393.78 → 2393.98] Yeah.
[2394.36 → 2395.52] Maybe I'm wrong, but.
[2395.90 → 2396.26] Sure.
[2396.58 → 2398.22] Where do you see Semaphore fitting into it?
[2398.26 → 2403.18] Like what's kind of like your bread and butter use case that you think people would be like, yes, you should definitely go check this out?
[2403.18 → 2403.86] Yeah.
[2403.86 → 2404.00] Yeah.
[2404.18 → 2406.24] I'll just maybe add to Jerome's point.
[2406.42 → 2410.86] Like if you are just beginner in this whole area, maybe not even think about CI and CD.
[2411.12 → 2416.60] Just maybe first invest time in learning, you know, test driven development.
[2416.86 → 2424.44] It's going to level up your skills in designing code and thinking about systems and making, you know, writing cleaner code.
[2424.44 → 2436.56] And if you got that mostly right, then, you know, just make sure that the way you run tests or build your application from scratch is very simple.
[2436.70 → 2439.76] Like one, ideally one line, one command.
[2439.76 → 2453.70] And if you have that kind of, you know, if you're not leaking any complexities, you know, but you keep it simple like that, then choosing a tool, it's going to be like, you'll get it done in like one hour in the afternoon.
[2454.26 → 2462.34] Whatever you kind of are maybe familiar with somehow or heard about or is able to get you to a passing build very quickly.
[2462.34 → 2466.48] I can kind of share how I see kind of companies evaluate choices.
[2467.14 → 2470.20] Typically, they look at, you know, what are they building today?
[2470.52 → 2474.40] You know, what are the technical requirements of their systems?
[2474.88 → 2481.72] And most of Semifor's customers are building some kind of SaaS or, you know, they're some kind of technology company.
[2481.72 → 2485.20] They usually have relatively large code base.
[2486.04 → 2495.68] And because in that case, they benefit from Semifor the most because Semifor is the fastest, basically cloud-based CI service.
[2496.40 → 2498.08] Everybody is free to fact-check that.
[2498.34 → 2501.52] And so, you know, typically people have different teams.
[2501.60 → 2503.12] Maybe they're building mobile apps.
[2503.28 → 2506.06] You know, it depends on what frameworks, what languages they're using.
[2506.06 → 2514.20] Once you put all that on paper, there are usually some edge cases where, you know, not suddenly not every tool fits the bill.
[2514.76 → 2517.62] You also need to figure out, like, can you use cloud-based?
[2517.74 → 2519.68] Like, can you outsource the whole process?
[2519.88 → 2522.86] Or is something forcing you to do it yourself?
[2523.44 → 2524.86] That's an important junction.
[2525.68 → 2533.04] And once you're kind of through all that, if more than one option remains, I would kind of evaluate just what's the user experience?
[2533.04 → 2535.70] Is it easy enough for developers to use?
[2535.84 → 2547.02] Or it's like developers don't want to work with pipelines, but, you know, it's more like pushing you to have, like, a magical person or a team working on pipelines, which is not so great, in my opinion.
[2547.52 → 2551.52] I think developers should own, basically, the pipelines of the project, have full autonomy.
[2552.58 → 2554.62] And, you know, just see performance, basically.
[2554.90 → 2557.60] If there are differences, there are huge differences.
[2558.22 → 2561.38] In some cases, even 2x among cloud services.
[2561.38 → 2568.74] So I think it matters a lot if you're getting feedback in 15 or 30 or, you know, minutes.
[2568.94 → 2575.00] It's definitely a big difference between 15 and 30 minutes if you're waiting to figure out if something works.
[2575.44 → 2581.96] As a developer, I can imagine that would, I mean, it could almost change your productivity by, like, you know, 2, 3x factors at times.
[2582.36 → 2582.48] Yeah.
[2582.48 → 2591.40] Marco, you mentioned that, like, if you focus on getting your app set up, like, basically having it set up well ahead of time.
[2591.62 → 2592.72] So you have tests there.
[2593.26 → 2595.88] Your code is, it's relatively simple to run those tests.
[2595.88 → 2603.68] Are there any other, like, pitfalls or mistakes people make that when they go to start looking at CI, CD, leads to issues?
[2603.94 → 2614.10] Well, one thing that maybe people who are not, who have not been previously practicing CI usually do, they work in very long living branches.
[2614.10 → 2622.84] So they accumulate a lot of changes in feature branches, which just makes it more difficult to, you know, integrate.
[2623.56 → 2625.56] And so that's something to avoid.
[2625.94 → 2630.32] I casual, like, in conversation, I do use the term feature branch.
[2630.32 → 2632.64] But I don't know.
[2632.88 → 2641.98] For me, a feature branch is something that, you know, you do get checkout, and you're going to merge, like, maybe, you know, one hour later, not one month later.
[2642.64 → 2642.84] Yeah.
[2642.88 → 2646.90] Just make sure that you work in small batches of changes.
[2647.66 → 2659.42] You don't have to, you know, you can basically hide undeveloped features behind, you know, simple if statements and basically just carry on, you know, merge.
[2659.42 → 2660.66] Merge piece by piece.
[2661.24 → 2664.00] We talked about avoiding unnecessary complexity.
[2664.62 → 2665.78] I'm sure I'm talking about it.
[2666.12 → 2678.32] The feature branches is a it's definitely a good one to keep in mind because I kind of am in the same mindset as you, where even if you're going to spend more than an hour on a feature branch, I try to keep it as something that, like, I want it to be merged as one single commit.
[2678.86 → 2680.82] So, like, that describes everything being done.
[2680.90 → 2686.06] And if you have too much code for that, it kind of is a sign that you're keeping that feature branch open way too long.
[2686.06 → 2692.02] And that doesn't mean, like, inside the branch it ends up being one commit as I'm developing, you know, because sometimes I'll just want to save my work or whatever.
[2692.16 → 2694.82] But eventually I'll squash the whole thing and merge it in.
[2694.88 → 2702.76] So I want it to kind of be one commit at that point that describes hopefully one small feature or, like, some part of the feature, I guess, being described there.
[2703.30 → 2703.88] Flaky test.
[2703.88 → 2705.52] A flaky test.
[2705.62 → 2707.40] I was going to say, that's the one that I've seen the most.
[2707.98 → 2717.02] Where CI became useless for me was when I worked on a project that we would actually deploy and then maybe 50% of the time the CI would fail.
[2717.78 → 2727.58] And at that point, it wasn't useful feedback because you couldn't tell, is it, well, is it something broken or is it just a test that doesn't run correctly all the time?
[2727.58 → 2736.20] And it kind of made that CI like a weird, you'd wait 10 minutes, get your feedback, and then be like, well, now I just need to run the test again to see if that was actually broken or, you know, if it wasn't.
[2736.26 → 2743.06] And when we're talking about speed, that means that half your tests are going to take 20 minutes now potentially to just sort of double check if it's correct or not.
[2743.06 → 2757.04] Yeah, and we talk about the same kind of things around, like, monitoring and observability and how, like, you know, like false positives, like when your monitoring system pings you or pages you, especially in the middle of the night.
[2757.20 → 2759.68] If it's a fluke, it's going to be terrible.
[2759.88 → 2763.74] Well, first, because it sucks to be pinged by a machine in the middle of the night.
[2763.74 → 2772.56] And then especially if you know that half of the time, even if it's just 10% of the time, you know it's a fluke.
[2772.64 → 2784.62] So now it's like the story of the child who cries wolf, basically, because since the monitoring is nagging you constantly, then you don't pay attention when it becomes important.
[2784.62 → 2793.96] And I think for the test scenario that you mentioned here, like, same thing, like, and even like the behaviour you describe is nonsensuous because it's like, well, I'm going to run my test again.
[2794.08 → 2800.50] But some folks might just be like, well, if the test can't be trusted, I'm just going to stop paying attention altogether and not care.
[2800.80 → 2805.40] So in that case, yeah, we need to fix these tests.
[2805.40 → 2814.88] I think to bounce on something that was said earlier, like, I'm also a huge fan of the developers owning the CI and the surrounding process.
[2815.34 → 2830.80] However, I'm also very pro bringing in, you know, like, maybe for a short engagement, like bringing in some expert commando team to help you figure out what you need and how to set it up.
[2830.80 → 2836.88] And, you know, like quickly explain to developers, like, this is how you're going to be autonomous on that.
[2837.34 → 2845.40] Like, I've done that for container stuff, let's say, like, numbers of times, just because, yeah, these ecosystems are so big.
[2845.58 → 2850.34] So ideally, in the best possible world, we would do our research and pick the solution.
[2850.34 → 2863.38] But sometimes it really helps if someone can sit down with you and listen to what you're using and the code you're trying to run and then tell you, OK, I think I can at least help you narrow down your search to this and this and that.
[2863.46 → 2865.00] And personally, this is how I would do it.
[2865.40 → 2868.84] And then if they do it for you, empower you to maintain it after.
[2868.84 → 2881.00] It's like to speak of what I know, like, yeah, writing the first Docker file from scratch can be extremely difficult, especially doing it well with all the multistage bells and whistles, etc.
[2881.48 → 2889.74] However, once you have that Docker file, adding one extra dependency or changing it or something, that's way, way, way easier.
[2890.40 → 2892.64] So that's there's a little bit of both here.
[2898.84 → 2911.06] This episode is brought to you by our friends at Equinix Metal, globally interconnected, fully automated bare metal.
[2911.40 → 2916.06] Equinix Metal gives you hardware at your fingertips with physical infrastructure at software speed.
[2916.44 → 2921.46] Accelerate your workloads with fully automated bare metal that's secure, powerful and cost-effective.
[2922.00 → 2925.10] This is the promise of the cloud delivered on bare metal.
[2925.10 → 2932.82] Equinix Metal makes it easier than ever to take advantage of the unmatched global reach and connectivity ecosystem made possible by Equinix,
[2932.94 → 2938.06] which includes more than 220 data centres across 63 metros, making interconnection easy.
[2938.38 → 2941.34] And they're obsessed with making bare metal even more awesome.
[2941.70 → 2942.92] Seriously, check out these features.
[2943.46 → 2948.58] 60 Second Deploys, Hourly Pricing, A Customer Success Team that Engages Over Slack,
[2948.94 → 2954.66] x86 Intel, AMD and ARM, Single Tenant, NVMe and SSD Storage,
[2954.66 → 2959.90] RESTful API, First Class DevOps Integrations, Equinix Fabric Integration,
[2960.36 → 2963.76] support for enterprise OSes and open source Linux OSes,
[2963.96 → 2968.02] air-gapped installs without a public IP, no installed agent or keys,
[2968.38 → 2971.82] extensive open source love and support, plus so much more.
[2972.12 → 2974.76] Visit info.equinixmetal.com slash changelog.
[2974.84 → 2978.46] Get $500 in free credit to play with, plus a rad t-shirt.
[2978.76 → 2981.78] Again, info.equinixmetal.com slash changelog.
[2981.78 → 3011.76] I have a question, I guess like related to CCD around,
[3011.76 → 3017.82] build systems and like at what point it makes sense to bring in like maybe something better
[3017.82 → 3022.88] than a make file or a shell script like Basel or Pants or Buck or all of those things.
[3022.96 → 3028.30] Because that seems very connected to the CCD kind of pipeline and equation.
[3028.30 → 3030.94] Yeah, that's super connected.
[3031.14 → 3038.28] And I really liked how you mentioned Basel because I had a friend who kind of helped me understand
[3038.28 → 3043.80] what exactly was the point of Basel because from outside I had seen some container examples
[3043.80 → 3048.48] because for a while in the previous years, all I was doing was containers basically.
[3049.18 → 3053.42] And I couldn't really understand, okay, what's the point of using Basel for containers?
[3053.42 → 3054.58] That seems super complicated.
[3055.16 → 3060.42] And then my friend basically explained to me, well, if you have a team of, let's say, 100,
[3060.76 → 3064.56] 200 developers constantly like shipping code,
[3064.74 → 3069.98] and you have this test suite which kind of grows and grows and grows and grows,
[3070.42 → 3075.84] and now each time you change like one line of code in this little tiny dependency
[3075.84 → 3078.76] at the bottom of the code base, you end up having to rerun everything.
[3079.22 → 3081.64] And quickly that complexity blows up.
[3082.00 → 3085.10] It may be not exponential, but at least it's not linear anymore.
[3085.56 → 3089.64] And so you quickly get from the point where your test suite might take, you know,
[3089.66 → 3092.40] in the beginning it's a few minutes, and then it's a few hours,
[3092.54 → 3094.02] and then suddenly it's a few days.
[3094.10 → 3096.74] And then you're like, no, we can't do this anymore.
[3097.20 → 3102.34] And with something like Basel, then you can express dependencies in a really nice way
[3102.34 → 3107.22] so that, like, to me, it was to understand that, yeah, something like Make and Make Files
[3107.22 → 3109.32] helps me to rebuild just what I need.
[3109.58 → 3112.70] And with something like Basel, I can take this one step further
[3112.70 → 3117.04] and not only build what I need, but also test only what I need
[3117.04 → 3120.04] and build only the artifacts that I need, et cetera, et cetera.
[3120.04 → 3125.32] And I can bring back down that incredibly long test time.
[3125.46 → 3127.90] I can bring it back to something reasonable,
[3127.90 → 3133.26] and my developers can, again, wait just minutes instead of days to see results.
[3133.66 → 3135.86] The flip side is, of course, the complexity of the tool.
[3136.32 → 3138.32] The situation of my friend, like, they basically,
[3139.00 → 3141.70] I had the impression that there was, like, one full-time engineer
[3141.70 → 3144.32] kind of maintaining the Basel build system for them,
[3144.32 → 3148.64] which for, you know, if you're talking about hundreds of engineers
[3148.64 → 3152.06] shipping code behind that, like, that's reasonable
[3152.06 → 3154.04] because tooling is so important.
[3154.04 → 3159.04] But I've also seen the other extreme where you have folks
[3159.04 → 3163.06] who can't even comfortably write Docker files,
[3163.26 → 3167.10] and there was this one dude who showed up with Basel
[3167.10 → 3168.40] and was like, oh, this is awesome.
[3168.50 → 3170.04] I'm going to put Basel files everywhere,
[3170.32 → 3172.02] and nobody can understand or maintain it,
[3172.06 → 3175.32] and it's just a crusty bleep because, yeah,
[3175.40 → 3177.56] because people just kind of run it and pray,
[3177.68 → 3180.72] and when they need to tweak something, it gets complicated.
[3180.72 → 3186.80] But, yeah, it's a continuum, like, from Make files, Basel, containers,
[3187.30 → 3189.60] all the container build systems that we have now
[3189.60 → 3192.44] because even though I keep talking about Docker files, et cetera,
[3192.56 → 3193.96] but we have other things now as well.
[3194.36 → 3196.14] So it's meshed in here.
[3196.56 → 3200.10] Yeah, I don't have experience with Basel,
[3200.32 → 3203.00] or we're still using Make, so...
[3203.00 → 3204.18] It sounds like it's one of those things
[3204.18 → 3206.38] where it starts to become obvious
[3206.38 → 3208.06] that you need something else when it happens,
[3208.14 → 3209.36] if things are getting too slow.
[3209.36 → 3209.64] Yes.
[3210.12 → 3212.22] And I personally haven't been in that situation yet either,
[3212.36 → 3214.54] so I'm thankful for that.
[3214.62 → 3216.70] But at the same time, it's nice to know there are tools available.
[3217.38 → 3219.88] I just wanted to say that about flaky tests,
[3219.88 → 3224.50] what I think most people don't know is from CI provider,
[3224.84 → 3227.30] I was, you know, over time, I was able to see that
[3227.30 → 3231.08] it's basically everybody, every organization has them,
[3231.18 → 3234.78] and people are usually kind of ashamed that they have flaky tests.
[3234.78 → 3237.66] So I'm just here to tell you, you're definitely not alone.
[3238.36 → 3241.84] It's just part of the work, part of, you know, the complexity.
[3242.24 → 3245.56] It's just, you know, about how you deal with it.
[3245.88 → 3248.46] And yeah, definitely just want to encourage people
[3248.46 → 3251.24] to invest a little bit of time to, you know,
[3251.48 → 3254.42] in maintenance of their tests or code as well.
[3254.42 → 3259.40] So they need maintenance and some polish.
[3260.00 → 3261.48] It's definitely something good to keep in mind.
[3261.70 → 3262.98] And I think you're probably right.
[3263.10 → 3264.74] I don't think I've ever seen an organization
[3264.74 → 3267.32] that doesn't eventually introduce a flaky test.
[3267.66 → 3269.38] Now, they might be quicker at removing it,
[3269.42 → 3271.18] but I think they do get introduced over time.
[3271.56 → 3271.70] Yeah.
[3272.64 → 3273.08] Okay.
[3273.32 → 3275.26] So I'm going to play this intro theme for everybody,
[3275.46 → 3278.36] and then we can jump into your unpopular opinions.
[3278.36 → 3284.00] Unpopular opinions.
[3284.00 → 3285.10] You what?
[3285.22 → 3286.94] I actually think you should probably leave.
[3290.12 → 3291.84] Unpopular opinions.
[3295.60 → 3296.20] Okay.
[3296.74 → 3298.34] So Jerome, Marco,
[3298.78 → 3301.14] do you have any unpopular opinions you'd like to share?
[3301.50 → 3302.96] And whenever we do this,
[3303.52 → 3306.58] typically Jared will take your unpopular opinion,
[3307.02 → 3308.34] make it into a little Twitter poll,
[3309.04 → 3310.60] and he'll poll the, you know,
[3310.62 → 3312.76] anybody who's following the Go Time FM Slack channel,
[3313.00 → 3314.00] or not Slack, the Twitter,
[3314.66 → 3316.50] he'll poll them to see if it's unpopular.
[3316.78 → 3319.58] So I will warn you that most of that audience
[3319.58 → 3320.62] is going to be Go developers.
[3321.36 → 3324.76] So sometimes opinions that might be unpopular overall
[3324.76 → 3326.28] aren't unpopular there,
[3326.46 → 3328.94] but it's completely fine if it's not unpopular.
[3329.18 → 3331.22] We're just interested in different opinions
[3331.22 → 3332.16] than what the norms are.
[3332.72 → 3336.24] Well, mine would be that we have to stop insisting
[3336.24 → 3337.74] that updates, et cetera,
[3337.88 → 3341.28] need to be distributed over HTTPS.
[3341.82 → 3343.24] And very often when I say that,
[3343.30 → 3346.02] all my security friends and even non-friends are like,
[3346.08 → 3347.30] no, you don't know what you're talking about.
[3347.36 → 3348.90] It's very important because we have this
[3348.90 → 3349.84] and this and this attacks.
[3350.32 → 3351.50] And then when I explain,
[3351.58 → 3352.24] I'm like, no, no, no.
[3352.90 → 3354.86] Sure, you distribute the metadata,
[3355.10 → 3356.14] you know, list of packages,
[3356.50 → 3357.96] versions, checksums,
[3358.22 → 3359.56] over HTTPS, all you want.
[3359.56 → 3361.10] But the big bits,
[3361.68 → 3365.86] you can serve that of their HTTP, FTP, et cetera.
[3366.54 → 3369.94] And the reason being that serving over HTTPS
[3369.94 → 3371.54] costs a lot of money,
[3371.74 → 3374.22] not because TLS is complicated or whatever,
[3374.40 → 3377.08] but because if you're using HTTP or FTP,
[3377.20 → 3380.14] you can just let the world mirror your stuff.
[3380.34 → 3383.62] That's the way that Debian and Slackware
[3383.62 → 3386.20] and all these distros have operated for decades
[3386.20 → 3387.96] like on the shoestring,
[3387.96 → 3389.40] like as a fault for the budget.
[3390.10 → 3391.60] If you take the Docker Hub,
[3391.90 → 3394.26] and I'm not going to give you numbers
[3394.26 → 3395.50] from when I was at Docker
[3395.50 → 3398.90] because I don't even know if I knew these numbers
[3398.90 → 3400.34] and even I wouldn't remember,
[3400.46 → 3402.02] but just taking the public numbers
[3402.02 → 3403.30] from the beginning of this year,
[3403.86 → 3406.14] Docker said in some peer stuff
[3406.14 → 3409.38] that they had like 15 petabytes of images
[3409.38 → 3411.36] on the Docker Hub.
[3412.00 → 3414.70] So storing that on S3
[3414.70 → 3418.16] would be at least $300,000 a month,
[3418.56 → 3419.64] not counting transfer.
[3420.16 → 3422.38] Transfer, again, I took some numbers
[3422.38 → 3423.34] that Docker published
[3423.34 → 3424.40] in the beginning of this year,
[3424.74 → 3426.92] like 8 billion pools per month.
[3427.58 → 3431.60] And I went with like on average 10 legs per pool,
[3431.70 → 3432.64] which is really low.
[3432.90 → 3436.98] That gives you a bill of $4 million per month
[3436.98 → 3438.88] just to operate the Docker Hub.
[3438.88 → 3441.42] And these are pretty optimistic estimations.
[3442.14 → 3447.14] So if only that was mirrorable easily
[3447.14 → 3449.32] over plain HTTP, FTP, et cetera,
[3449.44 → 3452.68] and you just serve the metadata over TLS
[3452.68 → 3456.62] and perhaps have an origin copy over TLS
[3456.62 → 3458.06] for the one odd scenario
[3458.06 → 3461.98] where somebody is running this attack against you,
[3462.06 → 3464.24] where they prevent you from updating, et cetera.
[3464.24 → 3467.80] I'm not saying that this would have changed
[3467.80 → 3469.02] the fate of Docker,
[3469.20 → 3471.20] but I'm curious to see what the parallel universe
[3471.20 → 3473.66] where things have been made differently
[3473.66 → 3474.90] in that regard looks like.
[3475.32 → 3476.54] A world where you can have something
[3476.54 → 3477.32] like the Docker Hub,
[3477.40 → 3480.12] but that doesn't end up costing
[3480.12 → 3483.66] like in the six, seven, eight digits range
[3483.66 → 3485.90] per month to some company somewhere.
[3486.78 → 3488.26] So do you have any guesses
[3488.26 → 3490.00] as to how much that would actually save?
[3490.74 → 3491.52] Like, do you think it would like
[3491.52 → 3492.90] cut the costs in half or?
[3492.90 → 3495.86] Oh, I think it would save like 99%
[3495.86 → 3497.06] or something like that,
[3497.46 → 3500.78] which sounds like completely like what?
[3501.14 → 3504.00] But if you look at like Linux distros
[3504.00 → 3506.36] and I'm talking about stuff like Debian,
[3506.54 → 3508.16] Slackware, et cetera, Arch Linux,
[3508.84 → 3510.86] I'm not aware of, you know,
[3510.90 → 3513.02] like there is not a Debian Inc.
[3513.50 → 3516.26] or Arch Linux LLC or whatever
[3516.26 → 3518.14] paying for all the mirrors, et cetera.
[3518.28 → 3519.76] It's just like, you know,
[3519.82 → 3522.38] like companies, universities, labs,
[3522.38 → 3525.06] and all kinds of ISPs, et cetera,
[3525.34 → 3527.38] who decide to just mirror that
[3527.38 → 3530.42] because they feel like it's the public good.
[3530.58 → 3532.02] It's the commons.
[3532.26 → 3533.64] It's something that we maintain
[3533.64 → 3536.18] because like I, at some point
[3536.18 → 3538.52] when I was running a hosting company
[3538.52 → 3539.52] in France a while ago,
[3539.58 → 3541.08] yeah, we had mirrors as well
[3541.08 → 3543.48] because first for our own convenience,
[3543.66 → 3544.98] because when we deployed machines,
[3545.08 → 3546.54] it was so convenient
[3546.54 → 3548.56] to have something in our network.
[3548.56 → 3549.92] And it was also good
[3549.92 → 3551.48] to put that available for others.
[3552.00 → 3553.62] So at the end of the day,
[3553.62 → 3555.38] I think it would slash the costs
[3555.38 → 3557.72] by maybe 100 or 1,000,
[3557.84 → 3558.48] something like that.
[3558.68 → 3560.56] I think this is a very important message
[3560.56 → 3562.44] for whoever is building
[3562.44 → 3564.56] maybe the next company
[3564.56 → 3565.62] that's, you know,
[3565.70 → 3567.88] with the goal of being
[3567.88 → 3569.94] kind of backbone in the community.
[3571.08 → 3572.08] Thinking, yeah,
[3572.38 → 3573.88] I'm thinking about NPM as well.
[3573.88 → 3576.48] And I don't know how much it might cost,
[3576.60 → 3577.96] but I'm scared to think about it.
[3578.86 → 3579.50] Yeah, yeah.
[3579.60 → 3582.24] I mean, I remember being, you know,
[3582.62 → 3586.90] a college student downloading Canton Linux,
[3587.30 → 3589.28] obviously looking to download
[3589.28 → 3591.82] from the mirror of my local university.
[3592.62 → 3592.84] Yep.
[3592.94 → 3595.38] But, you know, okay, today we have,
[3595.62 → 3597.66] I guess most people have faster internet.
[3597.66 → 3601.16] And, but still, I think it's,
[3601.50 → 3604.38] every organization would want to download
[3604.38 → 3608.00] from the closest source.
[3609.58 → 3612.56] I think it's not even a question of like a budget
[3612.56 → 3613.74] or, you know, it's just,
[3614.18 → 3616.24] it is going to be faster and more convenient.
[3616.72 → 3617.94] So I can definitely say
[3617.94 → 3619.34] when I've worked at companies
[3619.34 → 3620.90] that have some of that stuff mirrored internally,
[3620.90 → 3622.34] that's also like,
[3622.36 → 3624.18] you can tell when you're getting stuff,
[3624.22 → 3625.46] which ones are mirrored internally
[3625.46 → 3626.44] versus which ones aren't
[3626.44 → 3628.34] because it's like a drastic difference.
[3628.74 → 3628.82] Yeah.
[3629.64 → 3631.60] And so if only Docker,
[3632.00 → 3633.32] and in that case, I would say,
[3633.80 → 3638.00] if I had tried to make my case back then
[3638.00 → 3639.34] to my coworkers,
[3639.52 → 3641.40] when we designed that whole protocol,
[3641.58 → 3643.44] if only it had been plain HTTP
[3643.44 → 3644.92] for the data bits,
[3645.38 → 3647.38] then it could have been mirrored transparently.
[3648.12 → 3649.50] But yeah, I'm curious to see
[3649.50 → 3650.76] what that parallel universe looks like.
[3651.22 → 3652.94] Isn't that why they just recently did the changes?
[3652.94 → 3654.80] Or I'm assuming that's why they did change recently
[3654.80 → 3655.96] that you have to be signed in
[3655.96 → 3657.08] after like 200?
[3657.80 → 3658.58] I guess, yeah.
[3658.78 → 3660.00] I guess at some point it's,
[3660.08 → 3661.90] I mean, it's just so much money.
[3662.00 → 3664.78] And especially because we in the CI space
[3664.78 → 3667.66] are also guilty as charged.
[3667.92 → 3669.30] Like the number of times
[3669.30 → 3670.62] where I've set up a pipeline
[3670.62 → 3672.26] and when I look at it,
[3672.30 → 3672.82] I'm like, well,
[3673.46 → 3674.38] this kind of sucks
[3674.38 → 3676.32] because I end up pulling these images
[3676.32 → 3678.16] from the Docker hub each time.
[3678.24 → 3681.38] Is there any way I could like not do that?
[3681.38 → 3683.36] And it turns out that it's complicated.
[3683.68 → 3685.04] Like I remember like having,
[3685.34 → 3685.58] you know,
[3685.62 → 3687.62] like these Linux install parties
[3687.62 → 3688.44] where you get together
[3688.44 → 3689.62] with a bunch of nerdy friends
[3689.62 → 3690.06] and you're like,
[3690.12 → 3691.32] hey, we're going to install Linux.
[3691.44 → 3692.20] It's going to be fun.
[3692.54 → 3693.90] And I remember setting up
[3693.90 → 3695.58] a transparent proxy for that
[3695.58 → 3697.20] and it was fairly easy
[3697.20 → 3699.42] and nobody had to do anything
[3699.42 → 3700.84] and everybody could just
[3700.84 → 3702.84] pull the packages from the proxy.
[3703.32 → 3704.88] Try and do that for the Docker hub.
[3704.88 → 3707.70] You can't because it's over HTTPS.
[3708.34 → 3710.40] So, well, you can,
[3710.48 → 3711.64] but it gets really tricky.
[3711.96 → 3713.88] You have to set up
[3713.88 → 3715.40] a transparent TLS proxy,
[3715.74 → 3716.72] inject certificates,
[3716.72 → 3719.12] and suddenly the older security
[3719.12 → 3720.36] that you had,
[3720.72 → 3720.88] you know,
[3720.88 → 3722.60] your hard-earned security
[3722.60 → 3724.96] that you got from TLS
[3724.96 → 3726.02] goes down the drain
[3726.02 → 3727.64] because you're adding
[3727.64 → 3728.70] this kind of backdoor
[3728.70 → 3729.66] so that you can have
[3729.66 → 3730.68] the caching proxy.
[3731.08 → 3732.08] So, yeah,
[3732.72 → 3733.38] that's nice working.
[3733.88 → 3734.66] That makes me wonder,
[3734.88 → 3736.46] if the middle road
[3736.46 → 3737.68] that, say, modules went
[3737.68 → 3738.38] where it's like
[3738.38 → 3740.22] still has that security
[3740.22 → 3740.88] and it's still,
[3741.02 → 3741.88] but it's also able
[3741.88 → 3742.72] to be distributed,
[3742.90 → 3744.88] is that like a good middle road
[3744.88 → 3745.22] or do you think
[3745.22 → 3746.14] it should still just kind of
[3746.14 → 3747.42] be strictly HTTP?
[3748.12 → 3749.10] I guess it's also
[3749.10 → 3751.12] maybe a size problem.
[3751.56 → 3753.10] The issue is kind of
[3753.10 → 3756.12] magnified for container images
[3756.12 → 3757.46] because it's so easy
[3757.46 → 3758.46] to end up with like
[3758.46 → 3759.88] a four gigs container images
[3759.88 → 3761.34] and you haven't even started
[3761.34 → 3762.42] putting your code in it.
[3763.02 → 3764.34] And then you end up
[3764.34 → 3764.94] with a pipeline
[3764.94 → 3766.02] that just pulls
[3766.02 → 3767.50] these four gigs
[3767.50 → 3768.56] like 20 times
[3768.56 → 3770.66] because that's how things work.
[3770.84 → 3773.64] And when nobody's paying for it,
[3773.70 → 3774.62] nobody has an incentive
[3774.62 → 3776.62] to try to improve that.
[3776.98 → 3778.00] The main incentive is,
[3778.10 → 3779.96] maybe I could make smaller images
[3779.96 → 3780.96] because this pipeline
[3780.96 → 3782.02] is getting slow
[3782.02 → 3782.82] and I have a hunch
[3782.82 → 3784.32] that if my images
[3784.32 → 3785.04] were smaller,
[3785.44 → 3787.10] my CI would run faster.
[3787.10 → 3788.58] but yeah,
[3788.64 → 3789.32] at the end of the day,
[3789.48 → 3790.62] someone's paying for it
[3790.62 → 3792.04] and at some points
[3792.04 → 3793.50] I get that the here
[3793.50 → 3794.32] like Docker Info
[3794.32 → 3796.38] was just footing that bill
[3796.38 → 3798.06] and so that's where we are now.
[3798.90 → 3799.30] Marco,
[3799.54 → 3800.98] do you have an unpopular opinion
[3800.98 → 3801.64] you'd like to share?
[3801.64 → 3802.48] Yeah,
[3802.56 → 3803.06] I have one
[3803.06 → 3804.28] which is kind of
[3804.28 → 3806.00] in tune
[3806.00 → 3807.64] with our today's topic.
[3808.16 → 3808.32] Although,
[3808.50 → 3808.64] yeah,
[3808.66 → 3810.26] we'll see how often
[3810.26 → 3812.34] this happens
[3812.34 → 3813.04] when you're writing
[3813.04 → 3814.76] maybe small Go services.
[3815.20 → 3815.30] So,
[3816.00 → 3816.80] mine is that
[3816.80 → 3817.96] it's not proper
[3817.96 → 3819.12] continuous integration
[3819.12 → 3819.90] if it takes
[3819.90 → 3821.08] more than 10 minutes
[3821.08 → 3822.10] to get feedback
[3822.10 → 3823.68] which is essentially
[3823.68 → 3824.18] about,
[3824.24 → 3824.46] you know,
[3824.52 → 3825.82] drawing a line somewhere,
[3826.18 → 3826.90] you know,
[3826.90 → 3827.38] saying,
[3827.56 → 3827.84] you know,
[3827.90 → 3829.22] what's good enough
[3829.22 → 3831.16] and the idea is
[3831.16 → 3832.58] it's good enough
[3832.58 → 3832.98] if,
[3833.46 → 3833.64] you know,
[3833.68 → 3834.36] as a developer
[3834.36 → 3836.02] you don't completely
[3836.02 → 3836.80] lose focus
[3836.80 → 3838.20] while you wait
[3838.20 → 3840.52] and it's kind of
[3840.52 → 3841.32] around 10 minutes
[3841.32 → 3843.20] and basically
[3843.20 → 3844.94] if you wait
[3844.94 → 3845.74] any longer,
[3846.20 → 3846.84] I mean,
[3847.20 → 3848.00] you might still,
[3848.16 → 3848.48] you know,
[3848.52 → 3849.80] remain focused for 15
[3849.80 → 3850.10] but,
[3850.22 → 3850.38] you know,
[3850.42 → 3851.14] going more,
[3852.06 → 3852.78] it just sucks
[3852.78 → 3853.54] like for me
[3853.54 → 3854.00] as a
[3854.00 → 3854.44] you know,
[3854.64 → 3855.68] from a developer point
[3855.68 → 3856.82] it's like somebody
[3856.82 → 3857.92] took away my keyboard
[3857.92 → 3858.80] and I'm not able
[3858.80 → 3859.38] to,
[3859.38 → 3860.08] you know,
[3860.08 → 3860.84] do my work
[3860.84 → 3861.86] like do what I enjoy
[3861.86 → 3862.78] which sucks.
[3863.12 → 3863.96] It's about around the time
[3863.96 → 3864.52] it would take to go
[3864.52 → 3865.58] make a coffee or something
[3865.58 → 3866.48] a coffee or tea
[3866.48 → 3866.84] or something
[3866.84 → 3867.44] and come back
[3867.44 → 3868.72] and if it's not done then
[3868.72 → 3869.38] then we got an issue.
[3870.10 → 3870.46] Exactly.
[3870.80 → 3870.98] Yeah.
[3871.48 → 3872.48] I think that makes sense.
[3872.66 → 3872.88] I mean,
[3872.90 → 3873.50] it is hard,
[3874.12 → 3874.82] it's something that's hard
[3874.82 → 3875.50] to explain to somebody
[3875.50 → 3876.38] who's not a developer
[3876.38 → 3877.26] that like
[3877.26 → 3879.28] how distracting it can be
[3879.28 → 3880.22] to go do something else
[3880.22 → 3880.82] for a half hour
[3880.82 → 3881.38] and then come back
[3881.38 → 3882.42] to what you were trying to do.
[3883.44 → 3884.68] I'm guessing most developers
[3884.68 → 3885.32] have like struggled
[3885.32 → 3886.06] to explain that
[3886.06 → 3886.72] to somebody else
[3886.72 → 3887.50] but it is a
[3887.50 → 3888.84] a real pain point
[3888.84 → 3889.76] where if you have to wait
[3889.76 → 3890.32] too long
[3890.32 → 3892.26] it's hard to keep that focus.
[3893.44 → 3893.66] Yeah.
[3893.88 → 3894.12] Yeah.
[3894.24 → 3894.56] I mean,
[3894.66 → 3895.88] the way you could maybe
[3895.88 → 3897.12] explain it to somebody
[3897.12 → 3898.16] who's not a developer
[3898.16 → 3898.96] is like
[3898.96 → 3900.32] okay,
[3900.32 → 3901.48] let's say it's one hour
[3901.48 → 3902.50] you know
[3902.50 → 3906.04] and there's 12 of us
[3906.04 → 3907.72] like working on a project
[3907.72 → 3909.66] and you know
[3909.66 → 3911.28] how many working hours
[3911.28 → 3911.80] do we have?
[3912.02 → 3912.22] Maybe,
[3912.42 → 3912.74] you know,
[3912.74 → 3913.92] at most eight.
[3915.06 → 3915.58] So,
[3916.08 → 3916.52] technically
[3916.52 → 3917.44] it's not possible
[3917.44 → 3918.44] for all of us
[3918.44 → 3919.38] to push
[3919.38 → 3920.38] and merge something
[3920.38 → 3921.10] in one day.
[3921.60 → 3921.64] Like,
[3921.78 → 3921.96] so,
[3922.56 → 3923.18] what's,
[3923.42 → 3923.68] you know,
[3923.78 → 3925.08] think about the implications
[3925.08 → 3925.66] of that
[3925.66 → 3925.94] and
[3925.94 → 3927.82] how often
[3927.82 → 3928.28] we're gonna
[3928.28 → 3930.38] basically check in
[3930.38 → 3930.74] and
[3930.74 → 3932.28] do stuff together.
[3932.48 → 3932.70] So,
[3932.84 → 3933.18] it's,
[3933.42 → 3933.60] yeah,
[3933.74 → 3934.74] I think it's pretty
[3934.74 → 3935.56] quickly
[3935.56 → 3936.60] you can run into
[3936.60 → 3937.50] very kind of
[3937.50 → 3938.54] hard limitations,
[3938.90 → 3939.08] right?
[3939.22 → 3939.44] You know,
[3939.48 → 3940.88] or if you have flaky tests
[3940.88 → 3941.76] as we talked about,
[3942.12 → 3943.36] you need to rerun
[3943.36 → 3943.70] and,
[3943.82 → 3944.92] but there are two other guys
[3944.92 → 3945.90] rerunning stuff
[3945.90 → 3946.46] on master
[3946.46 → 3946.96] and,
[3947.12 → 3947.30] you know,
[3947.56 → 3948.52] it's 3 p.m.
[3948.60 → 3948.96] So,
[3949.32 → 3949.56] you know,
[3949.60 → 3950.10] might as well
[3950.10 → 3950.80] just go home.
[3951.28 → 3952.16] In the scenario you described,
[3952.24 → 3953.10] it could even get to the point
[3953.10 → 3954.58] where code's still running
[3954.58 → 3955.10] the next morning
[3955.10 → 3956.24] when people come into the office,
[3956.42 → 3957.12] which would be
[3957.12 → 3957.98] even worse.
[3958.70 → 3959.06] Like,
[3959.08 → 3959.66] if it's long enough
[3959.66 → 3960.40] and you have enough people,
[3960.90 → 3962.44] that could potentially be real
[3962.44 → 3963.14] because you can't,
[3963.20 → 3963.32] like,
[3963.90 → 3964.86] as soon as something gets committed,
[3964.98 → 3965.80] you pretty much have to run
[3965.80 → 3966.58] against that new commit
[3966.58 → 3967.10] at that point.
[3967.16 → 3967.26] So,
[3967.32 → 3967.88] it's not like you can
[3967.88 → 3968.82] parallelize all this
[3968.82 → 3969.74] and,
[3969.74 → 3970.24] you know,
[3970.24 → 3970.96] count it as correct.
[3971.76 → 3972.60] That's why maybe,
[3972.74 → 3972.82] like,
[3972.88 → 3973.76] the thing of being able
[3973.76 → 3974.60] to cut corners,
[3974.96 → 3975.12] like,
[3975.18 → 3975.90] I'm thinking,
[3976.46 → 3976.70] you know,
[3976.72 → 3978.16] if you're adding commits
[3978.16 → 3980.16] to a feature branch
[3980.16 → 3981.00] or whatever,
[3981.30 → 3982.20] it might make sense
[3982.20 → 3983.22] to just cancel
[3983.22 → 3985.36] whatever had been scheduled
[3985.36 → 3986.26] in that branch before.
[3987.08 → 3988.38] And I guess it's,
[3989.52 → 3990.52] you know,
[3990.52 → 3993.42] each time we accomplish something
[3993.42 → 3994.82] and get a progress
[3994.82 → 3995.42] in the tuning,
[3995.56 → 3995.76] we're like,
[3995.84 → 3995.98] okay,
[3996.04 → 3996.50] now we have,
[3996.56 → 3996.70] you know,
[3996.74 → 3996.84] like,
[3996.88 → 3997.26] for instance,
[3997.40 → 3998.70] a matrix of different versions,
[3998.86 → 3999.10] et cetera.
[3999.10 → 4001.50] we always can imagine
[4001.50 → 4003.46] like a new feature,
[4003.68 → 4004.30] a new thing
[4004.30 → 4005.72] that we did not even
[4005.72 → 4006.66] think about before.
[4007.04 → 4007.92] But now that we have
[4007.92 → 4008.50] this foundation,
[4008.50 → 4009.32] we're already thinking
[4009.32 → 4010.84] about building the next floor,
[4010.96 → 4011.60] the next level
[4011.60 → 4012.66] on top of that.
[4013.26 → 4013.44] And yeah,
[4013.76 → 4013.98] you know,
[4013.98 → 4014.72] I don't know if
[4014.72 → 4015.72] the 10-minute CI,
[4015.94 → 4016.48] is it really
[4016.48 → 4017.46] an unpopular opinion
[4017.46 → 4018.22] or is it unpopular
[4018.22 → 4019.50] because it's hard to do
[4019.50 → 4020.26] and people are like,
[4020.34 → 4020.44] no,
[4020.48 → 4020.58] no,
[4020.58 → 4020.68] no,
[4020.68 → 4021.66] I'm not going to commit
[4021.66 → 4022.02] to that
[4022.02 → 4023.00] because that's way too hard.
[4023.70 → 4023.84] Yeah,
[4023.92 → 4024.48] that's probably,
[4024.88 → 4025.08] you know,
[4025.08 → 4026.74] there's a lot to it.
[4026.74 → 4027.86] People kind of,
[4028.18 → 4028.92] when I talk about it,
[4028.94 → 4030.56] people kind of get defensive
[4030.56 → 4031.02] like,
[4031.22 → 4031.60] oh no,
[4031.68 → 4032.80] you don't know my code,
[4032.84 → 4034.02] it has to be this way
[4034.02 → 4034.34] or,
[4034.52 → 4034.70] you know.
[4035.32 → 4036.08] It's one of those things
[4036.08 → 4036.80] where in theory,
[4036.98 → 4037.84] everybody likes it,
[4038.18 → 4039.08] but in practice,
[4039.20 → 4040.10] nobody's willing to actually
[4040.10 → 4041.06] like put in the effort
[4041.06 → 4041.98] to make sure it happens.
[4042.26 → 4042.64] Absolutely,
[4043.00 → 4043.20] yeah.
[4043.44 → 4044.16] Which is where it would be
[4044.16 → 4044.92] because it's,
[4045.72 → 4046.36] I guess,
[4046.44 → 4046.62] Marco,
[4046.68 → 4047.24] you're saying that
[4047.24 → 4048.50] it should be important enough
[4048.50 → 4049.24] that you put in the effort
[4049.24 → 4050.14] to make sure it happens.
[4050.86 → 4051.12] Yeah,
[4051.36 → 4051.58] yeah,
[4051.58 → 4052.48] but it can partly
[4052.48 → 4053.76] be made easier
[4053.76 → 4055.36] with a tool
[4055.36 → 4056.64] if you want to,
[4057.16 → 4057.86] you don't need to run
[4057.86 → 4059.26] all the tests all the time,
[4059.48 → 4060.88] all the tests immediately.
[4061.38 → 4061.84] For example,
[4062.56 → 4064.36] your tool should let you run
[4064.36 → 4066.18] unit tests first
[4066.18 → 4069.34] and efficiently proceed further
[4069.34 → 4071.48] to maybe end-to-end tests
[4071.48 → 4074.24] because if you have a problem
[4074.24 → 4075.24] in unit tests,
[4075.32 → 4076.60] it's probably fundamental enough
[4076.60 → 4077.50] that it doesn't matter,
[4077.66 → 4078.04] you know,
[4078.08 → 4078.58] what's the
[4078.58 → 4079.56] what the result is
[4079.56 → 4080.84] on the end-to-end stuff.
[4081.54 → 4081.74] So,
[4082.54 → 4082.76] yeah,
[4082.82 → 4083.92] there are things like that
[4083.92 → 4085.62] or if you have multiple projects
[4085.62 → 4086.32] in a repository,
[4087.18 → 4087.40] yeah,
[4087.48 → 4089.18] the tool should let you say,
[4089.28 → 4089.58] you know,
[4089.80 → 4091.38] run this part.
[4092.06 → 4093.68] If this directory changed,
[4093.78 → 4094.68] then do this,
[4094.76 → 4095.86] but don't do anything else.
[4096.30 → 4097.64] I feel like a part of this too
[4097.64 → 4098.34] is like
[4098.34 → 4100.44] code maintenance over time.
[4100.56 → 4102.16] Like the reason you wind up
[4102.16 → 4102.66] at like,
[4103.04 → 4103.26] oh,
[4103.36 → 4104.60] my CI pipeline
[4104.60 → 4106.02] is taking like 20 minutes
[4106.02 → 4106.66] or an hour
[4106.66 → 4107.32] is usually like,
[4107.40 → 4107.52] oh,
[4107.56 → 4107.72] well,
[4108.12 → 4109.72] you didn't design parallelism
[4109.72 → 4110.64] into your tests
[4110.64 → 4111.88] or even into your unit tests,
[4111.92 → 4112.04] right?
[4112.04 → 4112.34] Like I,
[4112.46 → 4114.08] I'm definitely guilty of that
[4114.08 → 4114.54] where it's like,
[4114.58 → 4114.68] oh,
[4114.68 → 4115.42] I'm just writing tests
[4115.42 → 4115.78] and I,
[4115.82 → 4116.94] I've written this code
[4116.94 → 4117.34] in a way
[4117.34 → 4118.04] where it's just like,
[4118.18 → 4118.40] oh,
[4118.48 → 4118.82] it's,
[4118.86 → 4120.08] it's using some global state
[4120.08 → 4120.34] or whatever.
[4120.44 → 4121.50] So everything has to,
[4121.50 → 4122.12] you know,
[4122.16 → 4123.14] run synchronously
[4123.14 → 4124.14] one after the other.
[4124.22 → 4124.44] And oh,
[4124.44 → 4124.72] I could,
[4124.92 → 4126.48] I could spend the 10 minutes now
[4126.48 → 4126.70] and,
[4126.78 → 4127.72] and fix that,
[4127.78 → 4128.62] but now I don't feel like
[4128.62 → 4129.18] I need to do it.
[4129.20 → 4129.92] And then like three months
[4129.92 → 4130.50] down the road,
[4130.50 → 4131.96] it's like everything's been built up
[4131.96 → 4132.86] around this concept
[4132.86 → 4133.36] and now it's like,
[4133.40 → 4133.50] oh,
[4133.50 → 4133.84] this is,
[4134.26 → 4135.46] this is a giant project
[4135.46 → 4137.44] to like to remove this,
[4137.60 → 4138.78] this global state.
[4139.24 → 4140.80] So now I just don't really
[4142.04 → 4142.78] upper because of it
[4142.78 → 4143.54] when I could have just,
[4143.86 → 4144.08] you know,
[4144.08 → 4145.34] spent that 10 or 20 minutes
[4145.34 → 4146.72] to have not introduced
[4146.72 → 4147.38] that global state
[4147.38 → 4148.10] in the first place.
[4148.22 → 4149.18] It always reminds me
[4149.18 → 4150.32] of like those slippery slopes
[4150.32 → 4151.40] and that first step
[4151.40 → 4152.78] just like makes you slide
[4152.78 → 4153.42] all the way down.
[4154.34 → 4154.80] Some of them are hard
[4154.80 → 4155.50] to avoid too.
[4155.80 → 4157.32] Like an example I can give
[4157.32 → 4158.34] is if you want to run a test
[4158.34 → 4159.34] with like a real database,
[4159.50 → 4160.54] then you need to have
[4160.54 → 4161.60] a database spun up
[4161.60 → 4162.00] and,
[4162.00 → 4162.58] you know,
[4162.60 → 4164.08] spinning up one Postgres database
[4164.08 → 4165.18] to test with is pretty easy,
[4165.30 → 4166.20] but you might not want to run
[4166.20 → 4167.22] six tests in parallel
[4167.22 → 4168.08] because they might interfere
[4168.08 → 4168.60] with each other.
[4168.98 → 4169.46] So like,
[4169.50 → 4170.44] it's an easy way to be like,
[4170.48 → 4170.62] okay,
[4170.64 → 4170.78] well,
[4170.78 → 4171.36] this makes sense.
[4171.42 → 4171.76] We're just going to have
[4171.76 → 4172.48] the one database
[4172.48 → 4173.84] and spinning up four
[4173.84 → 4174.66] is going to be kind of annoying.
[4174.74 → 4175.54] So let's not do that.
[4176.08 → 4177.08] But there are some tools.
[4177.16 → 4178.04] Like I think Docker test
[4178.04 → 4179.14] can actually help with that.
[4179.74 → 4180.82] If I recall correctly,
[4181.08 → 4181.80] I think it can spin up
[4181.80 → 4182.84] multiple copies of Postgres.
[4183.10 → 4184.00] I'd have to go look,
[4184.28 → 4184.92] but I don't remember.
[4185.22 → 4186.48] It used to be one of my demos
[4186.48 → 4187.14] in the early,
[4187.20 → 4188.40] early, early Docker days
[4188.40 → 4189.10] when I was like,
[4189.18 → 4189.34] hey,
[4189.44 → 4190.64] so I was,
[4190.74 → 4192.70] I was loading data
[4192.70 → 4194.46] in a Postgres database
[4194.46 → 4196.12] and then doing a Docker commit
[4196.12 → 4198.42] and then spinning up
[4198.42 → 4199.42] like 10 containers
[4199.42 → 4200.64] with that load of the data
[4200.64 → 4201.66] because it makes
[4201.66 → 4202.42] for a cool demo.
[4203.08 → 4203.88] But then it also
[4203.88 → 4204.76] kind of judges up
[4204.76 → 4205.74] the message a little bit
[4205.74 → 4206.50] because you don't really
[4206.50 → 4207.78] want to Docker commit
[4207.78 → 4209.68] your database data
[4209.68 → 4210.84] in the container image
[4210.84 → 4211.62] except for
[4211.62 → 4213.02] that kind of scenario.
[4213.36 → 4213.90] But yeah,
[4214.04 → 4214.98] there are some interesting
[4214.98 → 4215.68] things to do there.
[4216.36 → 4216.54] All right.
[4216.60 → 4216.74] Well,
[4216.86 → 4217.12] Jerome,
[4217.36 → 4217.60] Marco,
[4217.78 → 4218.94] thank you for joining us.
[4219.28 → 4219.82] It's been great
[4219.82 → 4221.42] talking about CI and CD
[4221.42 → 4222.16] with you two both.
[4222.68 → 4223.04] Hopefully,
[4223.84 → 4224.42] everybody else
[4224.42 → 4225.06] who was listening
[4225.06 → 4226.22] had a good experience
[4226.22 → 4227.10] and learned a lot.
[4227.10 → 4228.50] We'll see you next time
[4228.50 → 4229.02] on Go Time.
[4232.96 → 4234.80] If this is your first time
[4234.80 → 4235.58] listening to Go Time,
[4235.86 → 4236.82] subscribe now
[4236.82 → 4238.36] at gotime.fm
[4238.36 → 4239.90] or search for Go Time
[4239.90 → 4241.54] in your favourite podcast app
[4241.54 → 4243.20] and hit the subscribe button there.
[4243.48 → 4244.24] You'll find us.
[4244.64 → 4245.00] And hey,
[4245.10 → 4245.76] while you're there,
[4246.08 → 4247.06] leave us a five-star review.
[4247.38 → 4248.14] We'd appreciate that.
[4248.60 → 4249.74] This episode was hosted
[4249.74 → 4250.88] by John Calhoun
[4250.88 → 4251.86] and Chris Brando.
[4251.98 → 4253.30] It was produced by Jared Santo
[4253.30 → 4254.20] with music
[4254.20 → 4255.32] by Break master Cylinder.
[4255.32 → 4256.78] Go Time is brought to you
[4256.78 → 4257.60] by awesome sponsors.
[4257.96 → 4258.80] Thanks to Vastly,
[4259.10 → 4259.46] Linde,
[4259.66 → 4260.54] and Launch Darkly.
[4261.16 → 4262.30] Next week on the pod,
[4262.42 → 4262.98] Matt hosts
[4262.98 → 4264.30] a fascinating conversation
[4264.30 → 4265.16] about Q,
[4265.38 → 4266.38] that's C-U-E,
[4266.58 → 4268.18] configuration superpowers
[4268.18 → 4269.02] for everyone.
[4269.48 → 4270.46] Stay tuned for that one.
[4270.52 → 4271.26] You don't want to miss it.
[4271.66 → 4272.88] It's hitting your podcast feed
[4272.88 → 4273.70] next week.
[4273.70 → 4303.68] We'll be right back.
[4303.70 → 4333.68] We'll be right back.
[4333.70 → 4363.68] We'll be right back.
