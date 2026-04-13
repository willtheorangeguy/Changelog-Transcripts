[0.00 --> 7.12]  Or a more simpler explanation is that an enterprise is when whenever you're chained to the CEO,
[7.50 --> 13.00]  goes through a director, senior director, some kind of VP, and then their boss who's a VP,
[13.44 --> 18.36]  and then their boss who's a VP, and then maybe a C-level person, then you're enterprise.
[18.84 --> 20.32]  Even if you only have one product.
[21.18 --> 21.70]  Layers.
[22.12 --> 25.66]  I've seen five team startups that has that kind of a hierarchy.
[27.98 --> 28.88]  That's unfortunate.
[28.88 --> 32.36]  And you know, it's funny, you laugh, but yeah.
[36.40 --> 39.24]  Bandwidth for Changelog is provided by Fastly.
[39.62 --> 41.50]  Learn more at Fastly.com.
[41.74 --> 44.82]  We move fast and fix things here at Changelog because of Rollbar.
[44.96 --> 46.64]  Check them out at Rollbar.com.
[46.88 --> 49.06]  And we're hosted on Linode Cloud servers.
[49.40 --> 51.40]  Head to Linode.com slash Changelog.
[54.10 --> 56.70]  This episode is brought to you by DigitalOcean.
[56.70 --> 61.80]  DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[62.18 --> 69.18]  They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA,
[70.02 --> 73.48]  and 24-7, 365 world-class support to back that up.
[73.74 --> 79.20]  DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[79.20 --> 83.04]  Head to do.co slash Changelog to get started with a $100 credit.
[83.40 --> 85.50]  Again, do.co slash Changelog.
[97.88 --> 98.80]  Let's do it.
[99.38 --> 100.42]  It's go time.
[100.42 --> 105.88]  Welcome to Go Time, your source for diverse discussions from around the Go community.
[106.22 --> 107.74]  One quick note before we get started.
[108.12 --> 113.82]  This conversation was recorded back on March 10th, which was less than a month ago, but feels like a lifetime now.
[114.00 --> 118.62]  We rushed out the Working From Home episode since it was of the moment, and this one is more evergreen.
[119.04 --> 123.28]  So if you're wondering why there's no talk of coronavirus and global pandemics, that's why.
[123.58 --> 125.08]  Okay, here we go.
[125.08 --> 135.92]  Hello, and welcome to this episode of Go Time.
[136.14 --> 137.66]  I am your host, Johnny Borsico.
[138.26 --> 140.12]  Joining me is Mr. Matt Ryer.
[140.18 --> 140.66]  How are you, Matt?
[141.06 --> 141.42]  Hello.
[141.64 --> 142.28]  I'm good, thanks.
[142.32 --> 142.70]  How are you?
[143.58 --> 144.20]  I'm okay.
[144.30 --> 146.48]  I'm feeling quite chipper today.
[147.40 --> 149.28]  Joining us is a special guest.
[149.86 --> 154.20]  In some circles, he doesn't need any introduction, but we're going to give him one anyway.
[154.20 --> 155.76]  Not in this circle.
[156.22 --> 157.48]  Not in this circle.
[159.20 --> 162.32]  So our guest today is Mr. Brian Lyles.
[162.60 --> 171.20]  Brian is currently a senior staff engineer at VMware, where he actually runs multiple projects, including Octent, which you might have heard about quite recently.
[171.40 --> 173.96]  He actually unveiled it on Twitter for all to see.
[174.44 --> 180.48]  And I think the project has been getting some popularity and getting some contributions from the broader Kubernetes community.
[180.64 --> 181.30]  So that's awesome.
[181.44 --> 182.96]  So we'll probably touch on that, too, a little bit.
[182.96 --> 191.58]  But Brian is known to talk on a number of different things, from machine learning to developer health to programming techniques.
[192.58 --> 199.62]  I first came across Brian back in our Ruby days, where he was talking about tests all the effing time.
[199.62 --> 201.94]  So, yeah.
[202.08 --> 206.32]  So Brian's been around quite a while, and I've had the pleasure of knowing him for a few years as well.
[206.82 --> 209.64]  And for those of you who don't know about Brian, do check him out on Twitter.
[210.40 --> 214.42]  He's hilarious, and he'll get you to think with some of the tweets as well.
[214.74 --> 216.54]  So, Brian, thank you, and welcome to the show.
[217.42 --> 217.98]  Oh, wow.
[218.12 --> 220.52]  That was a great introduction, Johnny.
[221.00 --> 221.28]  Yeah.
[221.28 --> 225.24]  If I could blush, if I was not brown, I would be blushing right now.
[226.58 --> 230.42]  I can blush, but I've never needed to because Johnny's never been nice to me.
[231.80 --> 232.80]  That's not so far.
[234.42 --> 239.38]  No, the way you should look at it is if I'm not in the act of being mean to you, that means I'm being nice to you.
[239.64 --> 241.44]  Oh, just like a sensible default.
[241.44 --> 243.40]  Yeah, yeah, I should look at that.
[243.58 --> 244.26]  Yeah, yeah.
[244.44 --> 251.98]  So today, we have Brian on the show because we've been kind of stomped on something.
[252.22 --> 258.36]  We're trying to figure out what Go in the Enterprise means.
[258.58 --> 262.16]  What does that even mean, Go in the Enterprise?
[262.44 --> 266.86]  If you Google it, you'll find a bunch of different opinions and things.
[266.86 --> 274.62]  Some would say Go was even built for the Enterprise, about the people who are trying to solve Enterprise, you know, quote unquote problems.
[275.00 --> 277.42]  But I don't think I've ever written Go differently.
[277.58 --> 280.02]  Whenever I've written Go, I'm like, oh, I'm writing for the Enterprise now.
[280.14 --> 283.52]  A bunch of different things that I'm not doing when I'm writing for non-Enterprise.
[283.72 --> 285.12]  Like, what does that even mean?
[285.24 --> 286.88]  Brian, please enlighten us.
[287.62 --> 287.90]  All right.
[288.08 --> 291.96]  So, I don't know, actually, what Go in the Enterprise means.
[292.38 --> 294.46]  Johnny said, come up with a topic, Brian.
[294.46 --> 299.26]  And I went over all the other topics and I said, well, no one's ever talked about this.
[299.68 --> 300.80]  We'll just explore it together.
[301.42 --> 310.16]  But I will say that I've worked in, now, I've worked in two enterprises where Go was not a foreign language.
[310.30 --> 314.92]  Where I work at VMware right now, we have multiple business units using Go.
[315.16 --> 320.96]  And then when I was at Capital One, yeah, actually, yeah, I've been there way long enough so I can say this now.
[320.96 --> 327.18]  Things that your credit card transactions run through are now based on Go.
[327.66 --> 328.72]  And I think that's interesting.
[329.50 --> 338.62]  And the reason why, actually, why I thought this was an interesting thing to talk about, because whenever I fire up whatever I decide to write Ruby in in a day,
[338.62 --> 343.40]  and I write code or I write for an open source project, you code in one way.
[343.40 --> 351.86]  But whenever you introduce this horrible thing called people, and then a lot of people to your process, things change.
[352.82 --> 357.82]  So, that's why I wanted to, and I knew I would have Johnny here, and I guess I would have Matt here.
[357.82 --> 365.58]  So, I just wanted to throw out some ideas that I've seen, and then we could talk about those types of things for a little bit.
[366.08 --> 368.94]  Does enterprise mean big money or something, right?
[368.98 --> 372.96]  Big money, big corporations, big expenditures.
[373.46 --> 376.72]  Because personally, when I think of enterprise, that's what comes to mind.
[376.72 --> 384.08]  I'm like thinking big corporations, big tech companies, maybe non-tech companies that have lots and lots of software, lots and lots of process and people,
[384.28 --> 386.62]  and getting anything done takes months or years.
[386.98 --> 387.74]  That's what comes to mind.
[388.64 --> 391.20]  Yeah, you know, that's an interesting, what is an enterprise?
[391.70 --> 392.20]  I don't know.
[392.20 --> 402.64]  I do think that once your company has multiple business units, because they're chasing revenue in multiple directions,
[402.96 --> 407.52]  they've reached out beyond that one thing that they were known for.
[407.74 --> 409.64]  So, VMware started with VMs.
[410.22 --> 413.74]  Now, VMware does software-defined data centers.
[413.94 --> 417.42]  So, it's networking, compute, and storage.
[417.42 --> 426.44]  And now, Kubernetes and protecting office devices and whatever hyper-converged infrastructure is and a few other things.
[426.50 --> 427.48]  We're now our enterprise.
[428.30 --> 433.04]  And generally, what it is is that whenever your revenue line is separate,
[433.20 --> 443.18]  like we can totally separate our cloud native revenue line from what we're doing in vSphere and your clusters.
[443.50 --> 445.26]  Maybe, but maybe that's what it is.
[445.26 --> 454.08]  Or, a more simpler explanation is that an enterprise is when whenever your chain to the CEO goes through a director,
[454.26 --> 460.18]  senior director, some kind of VP, and then their boss who's a VP, and then their boss who's a VP,
[460.64 --> 465.62]  and then maybe a C-level person, then your enterprise, even if you only have one product.
[466.48 --> 467.00]  Layers.
[467.00 --> 470.98]  I've seen five team startups that has that kind of a hierarchy.
[473.36 --> 474.18]  That's unfortunate.
[474.46 --> 477.66]  You know, it's funny, you laugh, but yeah.
[479.60 --> 480.00]  Yeah.
[481.40 --> 486.92]  I also think, for me, security also comes up a lot, again, with enterprises.
[486.92 --> 493.10]  It seems to be a thing that it's almost there's a suggestion that startups don't care about it being secure.
[493.38 --> 497.48]  It's only when it's an enterprise do they suddenly have all this concern.
[498.12 --> 500.42]  Oh, well, here's a secret fact here.
[500.54 --> 502.90]  And I am not speaking for my employer when I say this.
[503.14 --> 504.44]  I'm just speaking in general.
[504.56 --> 505.32]  Brian, that guy.
[506.58 --> 508.52]  Most companies don't care about security.
[508.52 --> 514.28]  They care about SOX compliance and HIPAA compliance, and they care about regulators,
[514.60 --> 517.94]  and they care about people who can cost them money if they don't get it right.
[518.10 --> 522.72]  And this is not a negative on all the great security people that I know and don't know.
[523.00 --> 525.32]  I think there's people out there doing a great job.
[525.32 --> 530.58]  But really, a lot of companies, they don't care about security as a thing.
[530.90 --> 532.42]  They care about it as a liability.
[533.00 --> 538.00]  And when it becomes a liability, then that's whenever they start investing lots of money and people into it.
[538.52 --> 545.94]  But wouldn't you say, not to go down too deep of a security tangent here, but when I think of developing software,
[546.74 --> 551.08]  I like the boundaries that security provides.
[551.56 --> 555.32]  Once I know what the boundaries are, then I feel free to explore up to that boundary.
[555.50 --> 556.58]  It's liberating in some way.
[556.72 --> 560.92]  If I know what the constraints are, if I know what security review is going to entail,
[561.34 --> 566.66]  because I know I can't just ship my software out there and assume that there are no holes in it
[566.66 --> 568.98]  and assume that it's just going to do the right thing all the time.
[569.10 --> 571.60]  And if somebody tries to crack it, I'm not perfect.
[571.78 --> 575.12]  I don't think any team out there is perfect in how they create their software.
[575.42 --> 577.66]  Security is not a switch you just flip.
[577.72 --> 580.20]  You can't buy it off the shelf and apply it to your product and you're done.
[580.50 --> 582.02]  It's a continuous process.
[582.24 --> 583.98]  It's something that mitigates.
[584.24 --> 587.72]  So I feel comfortable working within that boundary.
[587.72 --> 592.66]  Shouldn't that be how we view things like security and compliance and all these other things?
[593.42 --> 593.66]  Yes.
[593.86 --> 595.72]  And not to go super deep into this.
[596.12 --> 597.92]  In a perfect world, yes, of course.
[598.20 --> 599.28]  Actually, it is liberating.
[599.80 --> 605.90]  But in the real world that we live in, there's people and there's ulterior motives.
[606.52 --> 608.40]  And it is a little more complicated than that.
[608.84 --> 613.40]  But there are better parts of enterprise, like go in the enterprise.
[613.40 --> 616.50]  So I actually had a premise.
[617.26 --> 618.96]  My premise is this.
[619.58 --> 622.56]  We have lots of companies out there.
[622.70 --> 631.04]  Whenever you say enterprise development, what they think of, first off, is they think of Java, like really deep Java.
[631.44 --> 637.24]  And I say this as a company now where we own a Spring Cloud Platform.
[637.24 --> 643.10]  There are many enterprises that do literally everything on Spring Cloud Platform.
[643.96 --> 649.26]  But I'm actually here to say that Go, what are we, almost 11 years in now?
[649.52 --> 655.70]  Go, in many cases, is a viable language and ecosystem for enterprises.
[656.08 --> 658.48]  And I think we actually just got here recently.
[658.96 --> 661.68]  But I think now is a good time.
[661.76 --> 666.80]  And that's why I wanted to actually think about and riff on with you all today.
[666.80 --> 669.54]  And I have my first controversial item.
[670.34 --> 675.04]  And this is something we could do years ago, but I will throw it out there right now and see what you all think.
[675.08 --> 681.20]  And it's actually the same concept that I was brought on GoTime to speak about a few years ago with Brian.
[681.20 --> 696.76]  Whenever you have a monorepo, I love that word, and you have the right amount of tooling for it, Go becomes very, very powerful because it's strongly typed and fast compile times.
[696.76 --> 698.76]  And it generates binaries.
[698.76 --> 699.52]  And it generates binaries.
[699.80 --> 700.92]  There's no need for a runtime.
[701.40 --> 706.26]  These three things right here are great for whenever you have to code with lots of other people.
[706.52 --> 715.40]  You can define not the soft APIs that we defined in Python, JavaScript, and Ruby, but we actually can get some firm, strongly typed APIs.
[715.40 --> 731.96]  And then when you put this all in a monorepo and it's all in the same place, then what you get is that in a perfect world, of course, you get this thing where if I'm depending on a library that someone else is using, I can always make sure it's up to date.
[732.92 --> 736.76]  And yes, there are definitely arguments of why that might not happen or why it's hard.
[736.96 --> 737.90]  And I can do that.
[737.90 --> 757.80]  And then another thing, which is actually super important, I think, for many large enterprises now, especially when we're all trying to move to this cloud native technology, so there's a lot of containers and things like Kubernetes, being able to generate a binary that I can actually run and not have a runtime, oh my gosh, this is amazing.
[758.22 --> 761.30]  So this is why I just want to talk about Go in the enterprise.
[761.30 --> 769.20]  That's a very good observation because a lot of folks are going to think enterprise Java, right?
[769.26 --> 772.14]  When you say the word enterprise and programming and things like that.
[772.44 --> 777.24]  Like back in my Java days, you know, even some of the product launches had the word enterprise in them.
[777.32 --> 782.08]  Like you were doing, you know, enterprise Java beans, you know, enterprise service bus and this and that.
[782.08 --> 788.48]  It's like, you know, the name alone, right, implied that you were programming differently, right?
[788.48 --> 796.88]  Or you had different concerns or additional concerns that you had to worry about when you were doing enterprise versus non-enterprise sort of Java development.
[797.48 --> 809.04]  Now, in Go, is there a material difference in how you program, say, your startup's business logic in Go or your network layer or whatever the case may be?
[809.28 --> 814.26]  Is there a material difference between how you do that, say, at a Google, at a Salesforce, at a VMware?
[815.44 --> 817.26]  You know, I don't think so.
[817.26 --> 828.84]  I think that there is this misconception that in large enterprises, you have that large enterprise development teams aren't capable of producing code.
[829.12 --> 836.00]  So we give them Java so we can give them all the pacifiers and all the handholding they need.
[836.00 --> 840.10]  But actually, after seeing this, I mean, I worked at a large bank.
[840.74 --> 845.72]  And after seeing what these teams were capable of, no, I don't see anything, any difference.
[846.08 --> 848.52]  I mean, most of them spent their day inside of IntelliJ.
[849.14 --> 849.90]  I mean, that's cool.
[850.26 --> 854.36]  I spend most of my day inside of GoLand, made by the same people.
[854.48 --> 855.94]  It's literally the same editing engine.
[856.64 --> 857.78]  It's the same thing.
[857.78 --> 862.86]  And I think we need to remove those misconceptions because that's all it is.
[863.08 --> 866.46]  I hate to use the term FUD, the whole fear, uncertainty, and doubt.
[866.96 --> 868.00]  But that's all this is.
[868.36 --> 873.44]  We use Java because it's the old IBM saying, no one got fired for buying IBM.
[873.94 --> 876.54]  And, oh, we're using Java because everyone else is using Java.
[876.54 --> 882.96]  But now in 2020, I think that's the year, there's multiple viable options out there.
[883.08 --> 887.48]  And I mean, I'm talking about what Microsoft is doing with .NET and this dude over there,
[887.54 --> 889.86]  David Fowler, amazing stuff.
[890.22 --> 891.22]  What Go is doing.
[891.56 --> 896.26]  And I only bring up this because a friend of mine now works on the Go team, Carlos Amadee.
[896.56 --> 901.42]  And if you've seen an email from him lately, he is actually, you know, he's shipping Go right now.
[901.92 --> 902.98]  And then there's other languages.
[902.98 --> 909.26]  I think it's time to not diversify because diversification is bad whenever you're in a big place.
[909.38 --> 912.50]  But I think it's time that we can explore other big projects.
[912.64 --> 918.80]  Because look right now, what do you think one of the, is Kubernetes almost the largest project on GitHub right now?
[918.94 --> 920.52]  They're doing fine-ish.
[921.48 --> 925.56]  Brian, earlier you mentioned that now Go's kind of got there.
[925.66 --> 926.66]  It's now at the enterprise.
[926.96 --> 928.10]  What had to happen?
[928.28 --> 929.88]  What was it lacking before that?
[929.88 --> 935.38]  And is it just a sort of maturity thing and community kind of adoption and things?
[935.98 --> 936.16]  All right.
[936.24 --> 939.10]  Well, I think there's only one thing that I'm really thinking about.
[939.38 --> 941.88]  And that was sort of kind of fixed recently.
[942.62 --> 946.50]  So in 2015-ish, I wrote this blog post.
[946.56 --> 952.08]  It was pretty popular when I was at DigitalOcean about DigitalOcean moving to Go.
[952.46 --> 954.70]  And I didn't do that work by myself.
[954.92 --> 956.36]  Matter of fact, I tried to do none of it.
[956.36 --> 962.28]  But I was definitely the person who got everybody on board with moving DigitalOcean to a monorepo.
[962.64 --> 970.54]  And the reason we had to move to the monorepo in the way that we did is because Go package management, five years ago, it was horrible.
[971.50 --> 973.90]  I mean, yeah, I could make stuff, but it was bad.
[973.90 --> 984.06]  And then just until recently, now with the introduction of Vgo and now we have how we have modules in Go, it took us a little bit of time to get used to it.
[984.26 --> 992.50]  And I won't say it's perfect, but I will say that it's more than good enough now that we can actually do dependency management in Go in a proper way.
[992.50 --> 1001.08]  And then you think about what the introduction of the Go private environment variable and local caching.
[1001.56 --> 1009.00]  OK, now my enterprise doesn't have to take down the world's infrastructure to actually be able to do modules properly.
[1009.16 --> 1015.76]  Or even better yet, I can use that Athena thing and now I can have a private proxy where I can actually do this.
[1016.06 --> 1018.12]  So the infrastructure is now getting there.
[1018.12 --> 1020.86]  And I really, really appreciate that.
[1020.98 --> 1029.12]  And that's what I'm saying that Go wasn't ready until, so I guess in the last year or so where we've, we're just right there right now.
[1029.18 --> 1034.22]  We're at the point where I'm like, yeah, I can actually recommend this to you and not laugh when you turn your back.
[1035.30 --> 1040.42]  And do you think that the fact that Go was open source was something that held it back?
[1040.76 --> 1047.62]  And I'm speaking like in the past, I've worked in some big companies and this may not be as true.
[1047.62 --> 1048.54]  And hopefully it isn't.
[1048.64 --> 1054.32]  But definitely there used to be this attitude of, you know, open source wasn't proper software.
[1054.74 --> 1056.96]  And if you want proper software, you have to pay for it.
[1057.18 --> 1060.62]  Do you think that held Go back at all when it came to the enterprise?
[1061.38 --> 1061.72]  It did.
[1062.10 --> 1062.86]  And guess what?
[1063.24 --> 1065.70]  50 years ago, black people had to sit at the back of the bus.
[1066.08 --> 1067.10]  Or no, it's more than that now.
[1067.20 --> 1069.34]  Now I would say 60, 70 years ago.
[1069.96 --> 1070.76]  Was it right then?
[1070.86 --> 1071.08]  No.
[1071.14 --> 1071.82]  Is it right now?
[1071.92 --> 1072.22]  No.
[1072.36 --> 1073.20]  And it's the same thing.
[1073.20 --> 1081.32]  The reason why a lot of these things held true for so long is because someone influential said these things.
[1081.66 --> 1082.28]  And was it right?
[1082.46 --> 1082.86]  No.
[1083.16 --> 1090.74]  And actually, it's great now because as we go into this new decade, we're seeing that there's a lot more diversity and development.
[1090.74 --> 1095.48]  Because of David Fowler that I mentioned from Microsoft earlier, I actually follow .NET development.
[1096.22 --> 1100.12]  And just think a few years ago, .NET, wow, is that a great idea?
[1100.38 --> 1101.60]  I don't even want to run Windows.
[1101.76 --> 1105.44]  You know, now people are successfully deploying it off of Windows.
[1105.44 --> 1110.32]  And there's some really cool tech in there made by some really good people.
[1110.72 --> 1113.26]  And we need to start looking in other directions.
[1113.72 --> 1116.66]  And also because, think about it, Java, what are they ready to do?
[1116.72 --> 1117.30]  Java 14?
[1117.88 --> 1119.40]  Look at what Java 14 is doing.
[1119.68 --> 1123.62]  They're getting to the point now where they're like, uh-oh, the world is catching up.
[1123.74 --> 1125.66]  Maybe we need to do some great things.
[1125.66 --> 1134.38]  And some of the new language features coming in the new version of Java are definitely, you can definitely see that languages like Go had some impact on them.
[1134.38 --> 1138.68]  But, you know, Java has had generics for forever, so I rest my case.
[1139.02 --> 1139.30]  Or Douglas.
[1139.84 --> 1145.06]  Yeah, that's definitely true of the different kind of languages, language features and things.
[1145.36 --> 1148.22]  I've seen Swift also has like a defer statement.
[1148.28 --> 1149.46]  It doesn't quite work the same.
[1149.62 --> 1155.74]  But the trouble is they tend to add on to what they already have, don't they, with these other languages.
[1156.24 --> 1160.22]  One of the nice things about Go is that it is quite a tiny little language.
[1160.22 --> 1171.38]  And there aren't too many ways of doing one thing, which turns out to be quite important because taking choice away means, oh, then it's kind of obvious what you're going to use to solve a particular problem.
[1172.64 --> 1174.58]  What is the Java features?
[1174.70 --> 1176.48]  Do you know what sort of things are they adding to it?
[1176.78 --> 1177.34]  You know what?
[1177.92 --> 1178.28]  No.
[1178.46 --> 1180.16]  I didn't come prepared to talk about that.
[1180.28 --> 1181.04]  Yeah, that's all right, mate.
[1181.04 --> 1187.08]  But I do remember, and someone's going to check me on this and tell me on Twitter, and I'm going to tell you right now, I don't care.
[1187.84 --> 1194.52]  What we're thinking about is one of the biggest complaints with Java is the dash x mx flag.
[1195.36 --> 1201.78]  And, you know, whenever you're actually saying how big this thing is going to be and that Java needs a runtime.
[1201.78 --> 1207.42]  And I think, actually, as we move on in years, I think Java is going to move past that.
[1207.52 --> 1213.08]  We're just going to assume that the JRE is part of the linking, and we're just going to give you a binary that runs on your platform.
[1213.68 --> 1217.66]  And I see them moving there, and I think it's actually a pretty good idea.
[1217.74 --> 1220.34]  But years ago, I can definitely see why they had a JRE.
[1221.16 --> 1222.20]  But you know what?
[1222.32 --> 1226.20]  It's Oracle, and I don't understand how they are doing their development.
[1226.20 --> 1230.16]  But I do know that there's definitely some super smart people over there.
[1230.28 --> 1232.68]  So hopefully they're trending toward the right direction.
[1233.46 --> 1241.70]  Speaking of enterprise, I mean, you know, Oracle, you're almost at the pinnacle there of what you can think of as enterprise.
[1242.40 --> 1249.74]  So with all these projects, right, and I'm talking about the projects that you don't have to go and pay for, right, to bring back what you were talking about earlier.
[1249.74 --> 1254.92]  For open source projects to succeed, like Go, for example, is an open source project.
[1255.18 --> 1257.58]  It still has a corporate benefactor.
[1257.70 --> 1259.38]  It still has a corporate entity behind it.
[1259.66 --> 1274.60]  From what I can see, be it Go, be it, you know, other languages with backing from corporations, it seems like those are the projects that are faring quite well nowadays than the non-funded, the non-backed project.
[1274.78 --> 1277.12]  Is that me, or is that something that you're noticing as well?
[1277.12 --> 1277.64]  Yeah.
[1278.06 --> 1279.52]  You know, I'm going to tell you all a secret.
[1279.74 --> 1282.14]  It takes money to develop stuff.
[1282.50 --> 1284.92]  And you're like, no, no, no, I developed this on my weekend.
[1285.04 --> 1285.98]  All right, that's cool.
[1286.34 --> 1290.40]  But to have a large, sustainable project, it takes lots of money.
[1290.78 --> 1300.24]  So I don't know how big the Go team is, but I know that from the first time I went to GopherCon to right now, it's a huge difference.
[1300.24 --> 1307.40]  And you think to have all these hugely popular open source software projects.
[1307.40 --> 1311.12]  The reason why they all come from companies is because they need a lot of money.
[1311.12 --> 1320.78]  And this is also why you have groups like the Linux Foundation, CNCF under them, or to a lesser extent, the Apache Foundation.
[1320.78 --> 1328.64]  Because it takes money to not only write the code, because if you think writing the code is the easy part, ha, ha, ha.
[1328.96 --> 1332.40]  But to take care of governance, all the legal aspects.
[1332.76 --> 1334.50]  And who's going to pay for your security review?
[1334.50 --> 1337.24]  And people don't think about that.
[1337.34 --> 1338.76]  They think about, oh, no, this is easy.
[1338.86 --> 1340.24]  I can just write this on the weekend.
[1340.72 --> 1342.58]  And you can to a certain level.
[1343.06 --> 1347.18]  But when a project like Go, think about all the pieces of Go.
[1347.34 --> 1349.08]  There's the build infrastructure.
[1349.80 --> 1352.04]  There is low-level language things.
[1352.12 --> 1357.44]  There's people who are getting their PhDs to think about how to make a better defer.
[1357.44 --> 1358.46]  I'm just guessing.
[1358.72 --> 1359.46]  I don't really know.
[1359.66 --> 1361.90]  Or how do we actually do generics?
[1361.94 --> 1364.52]  You can't just code that up on a whim.
[1365.50 --> 1373.14]  And then there's all the other support things, like the module infrastructure or the module depth infrastructure that we have for Go.
[1373.28 --> 1374.82]  Someone has to take care of that.
[1374.90 --> 1376.24]  And then all the advocacy.
[1376.96 --> 1381.16]  Someone has to go out and talk about how we are using these things.
[1381.42 --> 1387.14]  And work with their internal partners at Google to make sure that they're using it in a certain way.
[1387.14 --> 1391.48]  When projects get to a certain size, we realize that it's not easy anymore.
[1392.08 --> 1393.26]  Like Kubernetes itself?
[1393.66 --> 1398.20]  Just go look at their repository, like the Kubernetes slash Kubernetes repository on GitHub.
[1398.58 --> 1401.18]  And then look at all the work that goes into that.
[1401.80 --> 1404.18]  You can't do that without financial backing.
[1404.60 --> 1409.50]  And then I know that at one time Google was putting the bill for Kubernetes backend.
[1409.78 --> 1410.68]  It was not cheap.
[1410.94 --> 1414.96]  I mean, like, Johnny, you and I weren't going to chuck in a couple bucks and pay for that.
[1415.16 --> 1416.06]  No, no, no, no.
[1417.14 --> 1424.58]  How much time does your team spend building and maintaining internal tooling?
[1424.84 --> 1426.84]  I'm talking about those behind-the-scenes apps.
[1427.10 --> 1428.86]  The ones no one else sees.
[1429.12 --> 1431.62]  The S3 uploader you built last year for the marketing team.
[1431.86 --> 1435.34]  That quick Firebase admin panel that lets you monitor key KPIs.
[1435.58 --> 1440.62]  Maybe even the tool your data science team hacked together so they could provide custom ad spend analytics.
[1441.22 --> 1443.16]  Now, these are tools you need so you build them.
[1443.16 --> 1444.30]  And that makes sense.
[1444.84 --> 1451.36]  But the question is, could you have built them in less time, with less effort, and less overhead and maintenance required?
[1451.68 --> 1453.86]  And the answer to that question is, yes.
[1454.34 --> 1455.60]  That's where Retool comes in.
[1455.98 --> 1459.46]  Rohan Chopra, engineering director at DoorDash, has this to say about Retool.
[1459.46 --> 1468.30]  Quote, the tools we've been able to quickly build with Retool have allowed us to empower and scale our local operators, all while reducing the dependency on engineering.
[1468.74 --> 1469.10]  End quote.
[1469.10 --> 1475.84]  Now, the internal tooling process at DoorDash was bogged down with manual data entry, missed handoffs, and long turnaround times.
[1476.16 --> 1485.36]  And after integrating Retool, DoorDash was able to cut the engineering time required to build tools by a factor of 10x and eliminate the error-prone manual processes that plagued their workflows.
[1485.78 --> 1489.88]  They were able to empower back-end engineers who wouldn't otherwise be able to build front-ends from scratch.
[1490.26 --> 1495.24]  And these engineers were able to build fully functional apps in Retool in hours, not days or weeks.
[1495.24 --> 1499.42]  Your next step is to try it free at retool.com slash changelog.
[1499.56 --> 1502.02]  Again, retool.com slash changelog.
[1521.16 --> 1522.28]  Maybe I'm jaded.
[1522.52 --> 1524.34]  I've been on this earth for a few years.
[1524.34 --> 1525.26]  So I've seen a few things.
[1525.92 --> 1528.36]  So once you accept money, right?
[1528.58 --> 1532.70]  That means they, or the proverbial they, can tell you what to do, right?
[1532.70 --> 1544.64]  Do you think that this model, based on what we're seeing out there right now, the examples of open source projects that are backed by some sort of corporate benefactor,
[1544.64 --> 1555.42]  do you think that model is going to retain what works best for everybody instead of just what works for the corporate benefactor, right?
[1555.56 --> 1563.36]  So, for example, I'm sure there are some who do not like the way the Go team, right, does certain things with the Go language, right?
[1563.36 --> 1565.38]  They're all on Hacker News right now.
[1565.38 --> 1566.06]  Yep.
[1566.70 --> 1567.22]  Yep.
[1567.64 --> 1573.38]  I mean, yeah, there's no shortage of opinions on things like Go modules, for example.
[1573.72 --> 1581.94]  And, you know, like cementing import versioning is a hot topic these days, you know, which kind of, you know, kind of makes a few people, you know, kind of not happy with that.
[1581.94 --> 1593.00]  Right. But to them, it may seem like, okay, well, the Go team decided to do something that works against the broader community's interests, something that may work well at Google, but not for everybody else.
[1593.12 --> 1594.88]  But you're always going to have these things.
[1595.02 --> 1596.68]  So is it fair, right?
[1596.82 --> 1605.90]  Is it naive of me to think that the corporate benefactor is going to always be looking after the best interests of the entire community and not just for things that work well for it?
[1606.70 --> 1610.04]  Corporate benefactor is never looking out for the community.
[1610.04 --> 1611.06]  Oh, no, no, no.
[1611.06 --> 1620.56]  So companies, CEOs have fiduciary responsibilities to make money for their shareholders, or you can go to jail in the United States.
[1621.00 --> 1622.46]  Well, if you don't make enough money?
[1622.96 --> 1624.84]  Well, the board will get rid of you.
[1625.70 --> 1629.62]  But you mean there's like a legal duty, though, to look after shareholders?
[1629.82 --> 1632.78]  Yeah, your job is to do things that make more money.
[1633.04 --> 1635.08]  This is why companies should not be considered people.
[1635.40 --> 1637.48]  They do not work on the same set of ethics.
[1637.48 --> 1639.46]  It's just how the law works in the United States.
[1639.88 --> 1640.48]  And that's fine.
[1641.06 --> 1642.50]  But think about this way.
[1642.98 --> 1657.54]  If your company, companies aren't looking at big open source projects, whether it be, and this is just speculation, but Google looking at Go, Google and whoever else looking at Kubernetes, they're not doing this to be nice to the community.
[1657.54 --> 1665.70]  They're doing it because if you support this project properly, ultimately, you have one of two things.
[1665.70 --> 1675.20]  You either have a better funnel of people who are coming to use things that you can charge money for, or you have better integration with other parts of the industry.
[1675.46 --> 1678.30]  So, for example, with Kubernetes, it's actually like with Linux.
[1678.30 --> 1694.68]  Linux made it easier for us to have a good operating system that was free, that allowed us to build and work on all sorts of different types of hardware.
[1694.68 --> 1695.52]  Think about that.
[1695.90 --> 1698.44]  We didn't have to pay Microsoft to do these things.
[1698.84 --> 1703.90]  Kubernetes is now taking that a level up where now I can actually install Kubernetes.
[1704.40 --> 1707.94]  And I'm going to really gloss over this because we're not selling Kubernetes right now.
[1707.94 --> 1709.70]  But I can install Kubernetes.
[1710.32 --> 1715.50]  And with that, I can run workloads that span over multiple machines.
[1715.70 --> 1716.80]  It's making it easier.
[1717.20 --> 1721.92]  It's actually the industry is looking at that as actually a boon.
[1722.02 --> 1723.88]  It helps us sell this type of thing.
[1724.00 --> 1725.52]  It helps us do these things better.
[1725.82 --> 1726.68]  And I think that's great.
[1726.80 --> 1730.76]  And actually, last year at KubeCon, I alluded to this in a talk.
[1731.14 --> 1733.84]  Industry is a bunch of verticals.
[1734.56 --> 1735.22]  Think about this.
[1735.22 --> 1742.68]  Your company, whatever they're doing, they're looking up and down at how do we take from zero to 100 to make as much money as we can.
[1743.14 --> 1745.28]  But they realize that they're not by themselves.
[1745.40 --> 1746.06]  They're not islands.
[1746.60 --> 1748.48]  And what the ecosystem is, the horizontal.
[1749.12 --> 1758.46]  Now, there's certain things that we need to worry about in a horizontal, whether it be our operating systems or our platform or platforms like Kubernetes or certain standards.
[1758.92 --> 1759.74]  Like, think about this.
[1759.74 --> 1764.86]  If we didn't have an SMTP standard, how in the world did we send mail?
[1765.94 --> 1774.58]  Or, you know, or even better, if we didn't have a TCP or any of the OSI stack, how would we actually communicate?
[1774.58 --> 1780.34]  So there are certain things that we realize as companies in the industry that we need to standardize on.
[1780.68 --> 1784.14]  And then we compete around the edges or we bring another angle to it.
[1784.44 --> 1785.22]  And you know what?
[1785.30 --> 1787.38]  I don't think that's a problem.
[1787.76 --> 1793.88]  I think that if we try to judge companies and what they do as people, yeah, it looks like companies are jerks.
[1793.88 --> 1801.30]  But if you look at companies as doing what they're supposed to do to actually make money, yeah, I guess they're doing a good job.
[1801.44 --> 1802.44]  And here's the best part.
[1802.92 --> 1804.44]  We don't have to like any of it.
[1804.52 --> 1806.30]  That's the biggest thing that I think.
[1806.30 --> 1811.30]  And here's a soapbox that I will stand on that us as adults, we need to understand.
[1811.52 --> 1813.44]  And especially as a black dude, I can just tell you this.
[1813.66 --> 1815.30]  A large part of the world sucks.
[1815.36 --> 1816.32]  It wasn't made for me.
[1816.68 --> 1817.88]  And you know what I learned to do?
[1818.02 --> 1819.74]  I learned to maneuver within it.
[1820.26 --> 1823.96]  You know, there's things that I cannot change without killing myself literally.
[1824.94 --> 1825.88]  So guess what?
[1826.04 --> 1827.76]  Knowing that, now what do I do?
[1827.88 --> 1828.82]  And actually, you know what?
[1828.84 --> 1829.26]  It's crazy.
[1829.40 --> 1831.56]  All these developers out here should embrace that.
[1831.78 --> 1832.78]  We love constraints.
[1833.74 --> 1836.58]  And we actually work better in constraints.
[1836.58 --> 1842.18]  And I've actually used these constraints society has given me to do better things in certain places.
[1842.68 --> 1848.56]  And what we should do, you know, in our computing with our languages is we should, in our technologies, we should be doing the same thing.
[1848.96 --> 1850.48]  And yeah, it sucks.
[1850.82 --> 1851.46]  But guess what?
[1852.12 --> 1852.80]  That's okay.
[1852.80 --> 1854.64]  Not everything is made for you.
[1855.28 --> 1856.28]  It's made for society.
[1856.44 --> 1859.24]  And we should look at how it's benefiting society as a whole.
[1859.60 --> 1863.62]  And I know there's another whole huge capitalist conversation that needs to be had here.
[1863.74 --> 1864.34]  But guess what?
[1864.58 --> 1866.36]  That's not what go time is for.
[1868.76 --> 1870.40]  And we appreciate that.
[1870.98 --> 1875.18]  We do have a segment on the show called Unpopular Opinions.
[1875.26 --> 1878.20]  But I think you might have been dropping maybe a couple already.
[1878.58 --> 1881.62]  Maybe we should change it to Popular Opinions for Brian.
[1881.62 --> 1884.62]  I actually had another one too.
[1884.78 --> 1885.84]  So we can do that later.
[1886.78 --> 1887.04]  Yeah.
[1887.08 --> 1887.48]  Okay, good.
[1887.52 --> 1887.90]  We'll do that.
[1888.06 --> 1888.40]  Good.
[1888.44 --> 1889.26]  We'll reserve it.
[1889.26 --> 1894.28]  On that about the enterprise kind of playing nicely with communities.
[1894.28 --> 1909.32]  One of the biggest resistances I've seen in the past to people adopting open source or contributing even to open source is this kind of, it's almost a blanket default attitude that all of our software is our IP.
[1909.32 --> 1910.32]  And it's valuable.
[1910.32 --> 1910.78]  And it's valuable.
[1911.02 --> 1912.70]  And we need to protect it.
[1912.86 --> 1920.80]  You know, it's a kind of default position that companies take, often by people that don't necessarily understand the nuances in that.
[1921.02 --> 1924.02]  So that's part of that, I think, is, and I've seen this happen.
[1924.02 --> 1925.22]  And it's definitely getting better.
[1925.34 --> 1929.90]  And Corey on the Slack channel mentioned Rails and Ruby.
[1930.26 --> 1933.98]  And maybe Ruby did pave the way a little bit for Go.
[1934.14 --> 1935.92]  Ruby was this open source project.
[1936.06 --> 1941.34]  Ruby on Rails, of course, the framework that everyone was, became popular kind of at a grassroots level.
[1941.34 --> 1945.10]  And it took a long time to get into enterprises.
[1946.14 --> 1947.12]  Compare that to Go.
[1947.30 --> 1952.68]  Go's kind of gone almost, well, it hasn't taken as long as it probably took Ruby.
[1952.90 --> 1955.28]  So I feel like maybe Rails did help us there.
[1955.40 --> 1964.94]  But I think the attitude shift that I've seen is suddenly people realize not everything's going to be that valuable to the company.
[1964.94 --> 1971.88]  Some things, like you say, Brian, you're better off collaborating with because then you all get the benefit of that particular problem being solved.
[1972.14 --> 1973.30]  So I think it's a great one.
[1973.36 --> 1976.16]  But that's the attitude, I think, that we need to bear in mind.
[1976.46 --> 1979.30]  So I have another metaphor for you.
[1980.50 --> 1984.66]  The other day, I went and bought a sampler, an MPC1.
[1985.44 --> 1986.38]  And it was not pricey.
[1986.44 --> 1987.06]  Go look it up.
[1987.16 --> 1988.88]  And you're going to be like, Brian, you have too much money.
[1989.36 --> 1992.34]  And no, I just like having hobbies.
[1993.10 --> 1994.22]  I bought the sampler.
[1994.22 --> 1995.70]  Is it an audio sampler?
[1995.88 --> 1996.74]  An audio sampler.
[1997.22 --> 2001.14]  So I'm going to, in my spare time now, I'm going to make hot beats.
[2001.76 --> 2002.68]  That's what I'm going to do.
[2002.78 --> 2004.18]  You can call me Kanye Junior Junior.
[2004.78 --> 2008.96]  You know, the less self-hating, more righteous beat maker.
[2008.96 --> 2009.48]  More righteous.
[2010.04 --> 2010.54]  More righteous.
[2011.08 --> 2011.62]  More righteous.
[2013.18 --> 2015.96]  So I bought this thing, this box.
[2016.22 --> 2019.14]  It's about, it's the size of like 11 by 11.
[2019.60 --> 2021.20]  It has lots of buttons on it.
[2021.20 --> 2028.74]  And I went to go make a beat the other day and realized I can't even figure out how to sample.
[2029.24 --> 2029.62]  Okay.
[2030.24 --> 2035.84]  So I go to YouTube and I learn and I'm watching this guy and I'm like, holy crap, this is hard.
[2035.84 --> 2040.94]  But here's the thing is that our software is this beat, is a sampler.
[2041.96 --> 2044.44]  You make a software and it's a sampler.
[2044.72 --> 2045.40]  What does it do?
[2045.74 --> 2051.46]  Well, until you can actually use it in a proper way, in a novel way, it's not useful.
[2051.46 --> 2056.06]  So I can make a song that you could hear on the radio, literally can make songs that you
[2056.06 --> 2058.30]  hear on the radio off of this machine.
[2058.58 --> 2063.00]  But because I don't have the knowledge and the expertise and all the practice, you know,
[2063.04 --> 2065.28]  I'm just over here entertaining myself with loud noises.
[2065.64 --> 2067.44]  And I think it's the same thing with software.
[2067.62 --> 2070.62]  We approach software like my software is my IP.
[2070.62 --> 2076.08]  I said, unless it's encryption codes or things that we can't export or something that was
[2076.08 --> 2079.98]  really novel, like PageRank when it first came out back in the 90s.
[2081.14 --> 2083.40]  Most of your software is not that serious, dude.
[2083.46 --> 2086.48]  And probably to tell you the truth, and I did say dude, I meant that.
[2086.92 --> 2089.46]  And to tell you the truth, that's probably not very good.
[2090.16 --> 2091.76]  And that's something that we need to realize.
[2091.84 --> 2095.18]  It's how we employ our software, how we are helping our users.
[2095.90 --> 2097.06]  That is just a tool.
[2097.06 --> 2102.14]  We just happen to be using software to help our users out because they're using computers.
[2102.46 --> 2103.46]  It works that way.
[2104.02 --> 2107.88]  But just the ability to have source is not super helpful.
[2108.58 --> 2111.54]  Or it's not a thing that should be a differentiator.
[2111.84 --> 2114.26]  And companies want to actually optimize for that.
[2114.56 --> 2118.00]  And the reason they do is because it goes back to this whole thing.
[2118.06 --> 2120.24]  I'm reading a book called Good Strategy, Bad Strategy.
[2120.64 --> 2122.34]  And I've read a couple of strategy books.
[2122.68 --> 2124.62]  It's because we're not good at strategy.
[2124.62 --> 2128.48]  We don't understand how to actually get from here to there.
[2128.62 --> 2129.86]  We paint goals.
[2130.28 --> 2131.44]  I should be stronger.
[2132.46 --> 2134.06]  And I'm going to work out.
[2134.70 --> 2136.48]  And then we don't really follow through.
[2136.70 --> 2139.68]  And we don't have actionable plans to actually get stronger.
[2140.20 --> 2140.72]  And the same thing.
[2140.78 --> 2141.94]  Companies do this all the time.
[2142.12 --> 2143.18]  Developers do this all the time.
[2143.28 --> 2143.66]  We're lazy.
[2143.84 --> 2144.44]  We're people.
[2145.60 --> 2150.68]  And I'm not going to try to argue any company's lawyer down because I would lose.
[2150.68 --> 2158.96]  But I think that we can see by having something like Kubernetes or something like Go or something like what Microsoft has done with .NET.
[2159.20 --> 2160.56]  Isn't it all open source now?
[2160.70 --> 2161.52]  Think about that.
[2161.94 --> 2162.70]  It doesn't matter.
[2163.30 --> 2164.16]  Because guess what?
[2164.34 --> 2167.22]  We are architecting now at a level that is so high.
[2167.50 --> 2168.20]  Who cares?
[2168.62 --> 2170.64]  You know, who cares what letters people are using?
[2170.64 --> 2173.20]  I want novel applications of this thing.
[2173.86 --> 2179.82]  And then soon, you know, maybe in 20 years, we might not even think about software in the same way we think about software now.
[2180.08 --> 2181.06]  And this is all silly.
[2181.32 --> 2182.06]  But you know what?
[2182.18 --> 2183.32]  It keeps people entertained.
[2183.52 --> 2185.48]  And it definitely makes lots of money.
[2185.82 --> 2188.04]  So that's why people are sticking to it.
[2188.82 --> 2189.80]  That's controversial.
[2190.26 --> 2190.78]  A little bit.
[2190.92 --> 2191.58]  And you know what?
[2191.68 --> 2192.34]  It's fine.
[2192.94 --> 2193.64]  I like it.
[2194.02 --> 2196.78]  If you're a language geek, right?
[2196.90 --> 2198.92]  Admittedly, this is niche, right?
[2198.92 --> 2212.62]  If you're a language geek and you sort of, you know, you revel in the esoteric knowledge of how language does, you know, things and its constructs and all these things, then yeah, maybe writing code, maybe just the source alone is valuable to you.
[2212.68 --> 2214.52]  But again, very niche.
[2214.90 --> 2219.94]  And that's not going to really be of value to anybody other than yourself, right?
[2219.98 --> 2221.54]  So it's okay to play.
[2221.64 --> 2222.52]  It's okay to experiment.
[2222.78 --> 2227.34]  But, you know, not everything we write as software developers is of value, right?
[2227.34 --> 2231.66]  And I think that perhaps that is something that we always think that by virtue of writing code, right?
[2231.70 --> 2233.38]  We're giving this gift to humanity.
[2233.68 --> 2234.88]  Well, not exactly.
[2235.72 --> 2237.98]  It actually has to be useful beyond you.
[2238.16 --> 2240.66]  And just writing the code, that's just a start.
[2240.72 --> 2241.92]  That's where you begin, right?
[2242.02 --> 2245.84]  Like, can it be used and produce value for others, right?
[2245.96 --> 2251.62]  Every time I hear somebody say, oh, Facebook and Twitter, that's just a stream you just scroll down and auto refresh.
[2251.62 --> 2253.08]  I can build that in a weekend, right?
[2255.38 --> 2258.88]  You know, every time you hear that, you look at them, you know, with a side eye.
[2258.98 --> 2260.60]  You're like, uh-huh, sure.
[2260.86 --> 2261.00]  Right?
[2261.12 --> 2265.50]  So it's, for some reason, I think maybe it's programmer culture, coder culture.
[2265.56 --> 2266.46]  I don't know what it is.
[2266.94 --> 2269.94]  And usually from dudes, I think you were alluding to that earlier.
[2270.32 --> 2274.10]  We have this sort of this ego about us, about, you know, the ability to create.
[2274.10 --> 2280.14]  We call ourselves makers and builders because we think just the act of creating something makes it valuable.
[2280.72 --> 2281.80]  That's only the beginning.
[2282.58 --> 2284.94]  Yeah, and that's my unpopular opinion, by the way.
[2285.06 --> 2286.58]  I'll share that when it comes time.
[2287.42 --> 2287.76]  Okay.
[2287.92 --> 2290.28]  That's true also even down at the code level.
[2290.52 --> 2295.20]  I had a friend who was looking at Go and they started to learn it.
[2295.28 --> 2298.82]  And they sort of dropped it because they were confused about arrays and slices.
[2298.82 --> 2310.40]  And I was kind of heartbroken because actually you don't need to really know everything about how arrays and slices work in Go to be able to use them, to be useful.
[2310.78 --> 2314.96]  And so this sometimes sounds a little bit anti-intellectualist or something, and it's not that.
[2315.08 --> 2317.52]  I think the more you learn, the better, of course.
[2317.84 --> 2323.84]  But there is something about getting useful and solving real problems for people.
[2323.84 --> 2329.18]  If that's your focus, not nothing else matters, but almost nothing else matters.
[2329.76 --> 2339.72]  I feel like that's a way to give yourself a best chance of doing something that's going to stand the test of time or be useful or be used or be successful, whatever it is you're doing.
[2340.56 --> 2341.36]  Oh, yeah, definitely.
[2341.72 --> 2343.04]  No, you're exactly right.
[2343.26 --> 2347.78]  I think I have definitely indoctrinated you into my church of haters.
[2347.78 --> 2351.54]  I was called a killjoy.
[2352.04 --> 2354.72]  No, I'm a professional joy stealer or killer.
[2355.44 --> 2356.52]  And it's not that.
[2356.60 --> 2357.96]  It's just how I get through today.
[2358.16 --> 2361.32]  I realize that the world is not friendly.
[2361.94 --> 2366.92]  And our goal is to make it better for people that come behind us.
[2367.22 --> 2369.26]  And that's really all we can do.
[2369.44 --> 2372.00]  But we realize that you can't change the whole world.
[2372.88 --> 2375.90]  I tried boiling an ocean once, and guess what happened?
[2376.28 --> 2376.64]  Nothing.
[2376.64 --> 2379.86]  Was it a digital ocean or analog?
[2381.90 --> 2382.80]  That was good.
[2383.26 --> 2383.56]  I know.
[2384.22 --> 2385.56]  Was it a digital ocean?
[2385.74 --> 2387.08]  Were you making a pun or not?
[2387.48 --> 2388.44]  No, I wasn't.
[2389.24 --> 2391.30]  I mean, I definitely boiled things while I was there.
[2392.38 --> 2396.08]  I am definitely not one of those seen and not heard people.
[2397.32 --> 2398.64]  You're going to feel me if I'm here.
[2400.46 --> 2401.10]  Well, good.
[2406.64 --> 2410.10]  What up, nerds?
[2410.10 --> 2411.82]  I've got some pretty awesome news to share with you.
[2412.18 --> 2415.96]  Pluralsight is totally free for the entire month of April.
[2416.34 --> 2416.84]  I'm not kidding.
[2417.10 --> 2417.42]  Seriously.
[2417.64 --> 2420.82]  Head to Pluralsight.com slash changelog and skill up while you stay at home.
[2421.14 --> 2428.50]  For the entire month of April, you'll get access to over 7,000 courses from experts in software development, security, cloud, and data.
[2428.50 --> 2430.44]  There's never been a better time to skill up.
[2430.66 --> 2432.36]  Head to Pluralsight.com slash changelog.
[2432.50 --> 2435.14]  Again, Pluralsight.com slash changelog.
[2435.14 --> 2456.06]  I'm curious if you've witnessed situations where Go didn't take, right, in an enterprise organization.
[2456.78 --> 2458.82]  You know, I have not seen that yet.
[2458.82 --> 2460.86]  I've seen places where Go didn't take over.
[2460.86 --> 2471.50]  You know, VMware, I will guarantee that our ESXi, so that's our hypervisor that runs your virtual machines on bare metal.
[2471.68 --> 2473.04]  That's never going to be written in Go.
[2473.62 --> 2483.06]  But I think in places where it has been applied at a higher level where we are building APIs and doing distributed computing, I've never seen it loose.
[2483.54 --> 2488.10]  But, I mean, I've been hearing more rumbles about Rust lately, and I've been learning it.
[2488.10 --> 2489.50]  And I look at it like this.
[2490.18 --> 2493.04]  A programming language is a programming language is a programming language.
[2493.74 --> 2495.40]  And it's not who you say.
[2495.48 --> 2496.52]  It's how many people are listening.
[2497.30 --> 2498.84]  Or what you say is how many people are listening.
[2499.64 --> 2504.92]  And, I mean, I like, in my professional career, I've touched over 20 languages.
[2505.50 --> 2506.98]  And we're doing Go now.
[2507.36 --> 2508.60]  Might not be doing it in the future.
[2508.78 --> 2509.26]  And guess what?
[2509.32 --> 2509.80]  That's fine.
[2510.56 --> 2510.82]  Mm-hmm.
[2511.18 --> 2513.26]  Yeah, that's like, this is a Go podcast, though.
[2513.30 --> 2518.28]  That's like going on the Great British Baking Show and going, yeah, and ovens and ovens and ovens.
[2519.36 --> 2520.30]  Food's all food.
[2520.86 --> 2524.16]  I'm just going to make a casserole today.
[2525.02 --> 2530.20]  But the best part about this being a podcast is that the majority of people listening to this are not live.
[2530.20 --> 2535.28]  So, if they have ill feelings about this, I'll just be like, I don't know what you're talking about.
[2536.70 --> 2539.16]  Or, even better yet, that wasn't me.
[2539.94 --> 2540.08]  Oh.
[2540.78 --> 2541.32]  Yes.
[2541.50 --> 2545.86]  There's a different Brian Liles floating about, you know, who's behind things like Octant.
[2546.32 --> 2548.80]  Speaking of which, let's talk about Octant.
[2549.02 --> 2552.68]  So, that is arguably an enterprise project, right?
[2552.72 --> 2555.44]  Because it's solving problems that the enterprise have.
[2555.72 --> 2556.66]  No, I disagree.
[2557.20 --> 2557.72]  You disagree?
[2558.12 --> 2558.20]  100%.
[2558.72 --> 2559.00]  Yes.
[2559.00 --> 2559.88]  Tell me about that.
[2559.88 --> 2561.08]  It doesn't solve problems?
[2561.40 --> 2561.66]  No.
[2562.00 --> 2563.32]  First of all, shout out to Johnny.
[2564.08 --> 2569.16]  I launched Octant to the world at Johnny's meetup in Baltimore last August.
[2569.52 --> 2573.28]  He was the first person who had seen that outside of folks at VMware.
[2573.50 --> 2578.14]  But, to go back even further, we started Octant at Heptio.
[2578.32 --> 2582.52]  We were way less than 100 people at that time, or maybe we were around 100 people.
[2583.54 --> 2585.62]  And it's not an enterprise.
[2585.78 --> 2586.86]  It wasn't enterprise software.
[2586.86 --> 2591.96]  The problem I have with software, just in general, or just tech in general, is all too hard.
[2592.52 --> 2597.26]  Yeah, I can code in over 20 languages, and I have code in the Linux source.
[2597.72 --> 2598.58]  Well, probably not anymore.
[2598.70 --> 2599.82]  That's probably been dropped off.
[2599.82 --> 2602.04]  And I've done all these crazy things.
[2602.24 --> 2603.18]  But guess what?
[2603.28 --> 2604.50]  My kid hasn't.
[2605.00 --> 2610.04]  Or, and I hate to say my mom, but I do say my mom because she's particularly tech adverse.
[2610.04 --> 2620.46]  And we need to realize that if we are trying to bring up technologies, and in my case, Kubernetes, we can't just say, oh, go use the command line.
[2621.58 --> 2622.66]  That doesn't work.
[2623.32 --> 2624.92]  But you're not saying that to your mom.
[2625.20 --> 2626.64]  You're not saying that to your mother, are you?
[2627.04 --> 2628.22]  Oh, no.
[2628.28 --> 2630.92]  My mom doesn't know what Kubernetes is, nor does she care.
[2631.16 --> 2633.04]  And she shouldn't care because it's not in her sphere.
[2633.72 --> 2634.76]  I don't even care.
[2635.16 --> 2636.54]  I don't even care about it.
[2636.92 --> 2637.60]  And you shouldn't.
[2637.80 --> 2639.76]  If it's not in your sphere, you shouldn't care.
[2639.86 --> 2642.04]  And actually, we should get to the point where it doesn't really matter.
[2642.64 --> 2648.50]  But it came down to, it was like, how do I know what's going on with my workloads in Kubernetes?
[2649.18 --> 2650.44]  And that was the first premise.
[2650.64 --> 2652.62]  And then it kind of evolved into a dashboard.
[2653.04 --> 2654.12]  And people are like, it's a dashboard.
[2654.32 --> 2656.82]  I'm like, well, no, it's not a dashboard.
[2657.14 --> 2658.28]  It has a dashboard in it.
[2658.56 --> 2662.76]  And now we're evolving it in a couple of different directions, where for a long time,
[2662.76 --> 2663.66]  I was really resistant.
[2664.12 --> 2668.60]  So Octant runs as a Go app and Angular and TypeScript.
[2669.02 --> 2673.46]  But it's a Go app that runs on Windows, Mac, and Linux just fine.
[2674.20 --> 2676.50]  We're moving it to two different directions.
[2676.68 --> 2682.32]  We're moving it to the cluster, running in the cluster as a website, because come to find
[2682.32 --> 2686.54]  out, and here's a lesson for everyone out there, you have to build software people need
[2686.54 --> 2688.62]  to want to use, and you have to meet them where they are.
[2689.00 --> 2692.64]  So we find with our enterprise customer, and this is the enterprise feature, we want to
[2692.64 --> 2693.36]  run it in cluster.
[2693.60 --> 2694.06]  That's cool.
[2694.18 --> 2695.02]  We'll make that happen.
[2695.58 --> 2701.46]  But for our other users and for our small office, home office people, or people like
[2701.46 --> 2706.48]  me who just want a tool that can talk to different clusters, we're also moving it to an Electron
[2706.48 --> 2707.08]  app as well.
[2707.28 --> 2711.42]  I know people hate Electron, but go look at what else is out there, and then come back
[2711.42 --> 2712.84]  to me and say that you hate Electron.
[2713.20 --> 2717.00]  Electron is the best thing if you look at everything else out there.
[2717.00 --> 2719.90]  And go look at what VS Code has done with them.
[2720.04 --> 2721.54]  It is possible to make a good app.
[2721.84 --> 2723.66]  If it's not great, guess what?
[2723.94 --> 2724.94]  That's someone else's fault.
[2725.08 --> 2727.62]  It's not Electron's fault every piece of the time.
[2728.06 --> 2729.22]  So we're moving this app.
[2729.46 --> 2730.42]  But we use Go.
[2730.60 --> 2734.84]  And the reason we use Go is, first of all, because the best driver, the first client we
[2734.84 --> 2736.54]  could find for Kubernetes wasn't Go.
[2736.90 --> 2740.50]  But when you write an app that's small, writing whatever you want.
[2740.58 --> 2743.22]  But when the app gets bigger, so Okten is super complex.
[2743.22 --> 2747.66]  It probably has about 12 or 13 different domains of different things that it does.
[2748.32 --> 2752.54]  And we find that having a strongly typed language in this case makes it easier for people to
[2752.54 --> 2753.18]  come step in.
[2753.64 --> 2754.94]  We have no weird duct typing.
[2755.52 --> 2758.72]  There's only three lines of reflect in the whole entire app.
[2758.80 --> 2760.24]  And I figured out a way to get rid of those.
[2760.82 --> 2767.02]  And it's easy for people to be able to hook up to something like IntelliJ or no, or like
[2767.02 --> 2767.44]  Goland.
[2767.76 --> 2770.68]  And now they can actually view this thing and they can navigate through it.
[2771.02 --> 2772.52]  There's lots of benefits there.
[2772.52 --> 2774.40]  But here's the crazy part.
[2774.62 --> 2776.94]  Ever try writing a web app in Go?
[2777.36 --> 2778.82]  God, no, don't do that.
[2779.00 --> 2779.30]  It's painful.
[2779.64 --> 2780.32]  Don't do that.
[2780.68 --> 2785.68]  So Go just serves a website that actually is an Angular type of app.
[2785.92 --> 2786.84]  And we do it that way.
[2786.94 --> 2789.82]  So really, it's go find the best tool for your problem.
[2790.30 --> 2795.34]  If you run around with a Go hammer for everything, you're just going to make Go-sized holes
[2795.34 --> 2795.82]  everywhere.
[2795.94 --> 2796.82]  And that's not going to work.
[2798.68 --> 2799.36]  That's brilliant.
[2799.46 --> 2800.72]  Now I want to buy a Go hammer.
[2800.72 --> 2805.62]  But I actually remember the launch of Octon.
[2805.82 --> 2811.78]  I was following the Twitter storm on when you announced it in the Baltimore meetup, right?
[2812.28 --> 2812.58]  Mm-hmm.
[2812.90 --> 2814.10]  I mean, I say storm.
[2814.38 --> 2816.08]  It had likes in the high ones.
[2816.70 --> 2818.14]  But that was still...
[2818.14 --> 2818.78]  Hey, you know what?
[2818.78 --> 2820.34]  But no, I mean...
[2820.34 --> 2822.04]  Well, it was...
[2822.04 --> 2822.66]  Go what?
[2822.92 --> 2823.68]  Here's the thing.
[2824.30 --> 2826.20]  You say that, but I look at it like this.
[2826.42 --> 2827.68]  It's success to me.
[2828.18 --> 2834.42]  At VMware, I have a team of people writing, working full-time on software that I made.
[2834.88 --> 2835.30]  I won.
[2836.58 --> 2837.02]  Yeah.
[2837.02 --> 2840.90]  Well, actually, what I love about it is it just solves a real problem.
[2841.14 --> 2846.56]  And the thing is, that is a fundamental thing that a lot of projects miss, I think.
[2846.90 --> 2850.54]  You know, especially, like, we like to write packages.
[2850.76 --> 2853.44]  I love making packages and open sourcing them.
[2853.46 --> 2854.46]  I really love doing that.
[2854.46 --> 2856.46]  And I used to do it all the time.
[2857.10 --> 2861.80]  And the only reason I don't do it as often now is because that process can involve a lot
[2861.80 --> 2867.72]  of sort of imagining things and building kind of hypothetical software, solving hypothetical
[2867.72 --> 2868.38]  problems.
[2869.00 --> 2875.00]  When you solve an actual real problem that you have, it's a whole different ballgame.
[2875.00 --> 2881.06]  And it's almost, I think we should, everyone who's working on software should kind of understand
[2881.06 --> 2885.38]  the why, really make sure that you are solving a real problem for somebody.
[2885.50 --> 2888.96]  And it isn't just, hasn't just been imagined, I think.
[2889.38 --> 2890.58]  Yeah, that's a real thing.
[2890.82 --> 2891.60]  Now, don't get me wrong.
[2891.90 --> 2894.40]  If you go look at my GitHub right now, I think I looked at it this morning.
[2894.60 --> 2898.30]  I have 255 projects that I've created over the life of GitHub.
[2898.72 --> 2901.76]  And that's not even everything I've created because I think I have some GitLab stuff too.
[2901.96 --> 2903.44]  I enjoy writing software.
[2904.38 --> 2910.48]  But you need to write every once in a while, you have to write software that is usable, either
[2910.48 --> 2912.56]  solves your problem or solves someone else's problem.
[2912.92 --> 2918.64]  You can't just go out there and be like, I'm writing software all the time, unless you're
[2918.64 --> 2920.72]  like independently wealthy or you just don't care.
[2921.60 --> 2925.80]  But if you want to like progress in this world, you need to actually write software that helps
[2925.80 --> 2926.14]  people.
[2927.00 --> 2927.14]  Yeah.
[2927.44 --> 2930.28]  I mean, that's what we all want to do really anyway.
[2930.28 --> 2935.24]  I think it's just easy to kind of forget that or often it gets deferred as well.
[2935.30 --> 2938.80]  It's like, well, that's the product, that's that team's responsibility.
[2938.80 --> 2941.50]  So I just take instructions or something.
[2941.66 --> 2947.14]  And I just think it's never as good as when you understand the problem you're really solving
[2947.14 --> 2947.62]  yourself.
[2947.88 --> 2950.00]  Well, that's another problem that we have.
[2950.26 --> 2952.60]  You know, we're way over the, we're all over the map on this conversation.
[2952.60 --> 2956.16]  But that attitude, well, that's someone else's problem.
[2956.52 --> 2959.36]  No, no, no, no.
[2959.48 --> 2963.38]  I mean, it might be someone else's job to solve it.
[2963.38 --> 2965.94]  But if it's blocking you, it's your problem too.
[2967.04 --> 2972.30]  And we, we're really easy, I guess today, especially, you know, people I work with that
[2972.30 --> 2974.08]  I see, and this is like no complaints.
[2974.08 --> 2975.40]  It's actually great where I work.
[2975.76 --> 2976.82]  But I see this now.
[2976.82 --> 2982.64]  And I see it on social media, where people are like, oh, it's not perfect for me.
[2983.08 --> 2986.68]  Throw the hands up, you know, throw the whole, throw the whole baby out.
[2987.04 --> 2988.72]  And you really, we can't do that.
[2989.34 --> 2994.08]  We have to be, you know, villages are full of people.
[2994.52 --> 2997.50]  And if someone doesn't do their job, you know, the village could fail.
[2997.62 --> 3000.86]  Or we have to kill that person and find someone else.
[3001.48 --> 3002.06]  But we can't kill.
[3002.46 --> 3004.82]  That's quite a strong policy.
[3004.82 --> 3007.04]  It is, but we can't kill people anymore.
[3007.18 --> 3009.20]  And we don't want to kill people at all because that's wrong.
[3009.76 --> 3012.88]  So we need to realize that no one's perfect.
[3013.42 --> 3016.24]  And we have to work with everyone around us to make that world.
[3016.40 --> 3016.72]  We want it to be.
[3016.72 --> 3018.42]  Why did that sound so forced, Brian?
[3018.60 --> 3023.04]  I feel like you've had a lawyer tell you before that you have to say, no, no, no.
[3023.20 --> 3024.88]  Remember, killing people is wrong.
[3025.28 --> 3029.46]  No, I mean, if you sat down with me, I am anti a whole bunch of bad things.
[3029.54 --> 3030.82]  Like, I don't like any of that stuff.
[3030.98 --> 3033.54]  So this is all metaphorical.
[3033.54 --> 3034.86]  The village doesn't even exist.
[3035.00 --> 3036.54]  Oh, you don't actually do any murders or anything?
[3037.10 --> 3037.76]  Oh, gosh, no.
[3038.16 --> 3038.72]  Okay, right.
[3038.78 --> 3038.92]  Good.
[3038.98 --> 3039.10]  Yeah.
[3039.18 --> 3039.66]  Okay, good.
[3039.78 --> 3040.30]  No, that's great.
[3040.34 --> 3041.62]  Yeah, this would be a different podcast.
[3042.02 --> 3042.18]  Yeah.
[3042.38 --> 3044.84]  Or at least save it for the unpopular opinion bit.
[3045.80 --> 3048.48]  Speaking of which, we're at time for unpopular opinions.
[3048.60 --> 3051.44]  This episode has absolutely flown, I think.
[3051.82 --> 3052.44]  I know, right?
[3052.60 --> 3052.82]  Yeah.
[3052.90 --> 3053.08]  Yeah.
[3053.60 --> 3056.10]  Welcome to my world of random Brian thoughts.
[3056.98 --> 3058.54]  And now you see what my Twitter's like.
[3060.02 --> 3061.22]  All right, drop it like it's hot.
[3061.22 --> 3061.72]  Oh.
[3061.72 --> 3062.16]  Oh.
[3062.16 --> 3062.30]  Oh.
[3062.30 --> 3062.34]  Oh.
[3062.34 --> 3062.36]  Oh.
[3062.36 --> 3062.42]  Oh.
[3062.42 --> 3062.94]  Oh.
[3062.94 --> 3063.26]  Oh.
[3063.26 --> 3063.30]  Oh.
[3063.30 --> 3063.52]  Oh.
[3063.52 --> 3063.72]  Oh.
[3064.98 --> 3066.34]  Unpopular opinion.
[3067.06 --> 3069.04]  I actually think you should probably leave.
[3069.64 --> 3070.02]  Oh.
[3072.22 --> 3072.56]  Oh.
[3072.56 --> 3074.12]  Unpopular opinion.
[3080.06 --> 3080.62]  All right.
[3080.68 --> 3081.68]  My unpopular opinion.
[3082.12 --> 3082.36]  All right.
[3082.40 --> 3083.06]  Here it comes.
[3083.28 --> 3085.22]  In my mind, the world owes you nothing.
[3085.94 --> 3092.24]  So whenever you, if you go to a job and you're a beginning developer and you say, well, I've
[3092.24 --> 3092.92]  worked four years.
[3092.92 --> 3093.52]  I should be a senior.
[3093.52 --> 3093.76]  I should be a senior.
[3093.76 --> 3093.78]  I should be a senior.
[3093.78 --> 3094.26]  Nope.
[3094.26 --> 3094.30]  Nope.
[3094.30 --> 3094.86]  Nope.
[3094.86 --> 3095.94]  You should not be a senior.
[3095.94 --> 3100.50]  What the world owes you though, is not blocking you from moving forward.
[3100.50 --> 3101.70]  And that's the difference.
[3101.70 --> 3105.16]  So my unpopular opinion is that you don't deserve anything.
[3105.16 --> 3109.52]  You should have to go get and work and earn everything you have.
[3109.52 --> 3110.74]  And it should be fair.
[3110.74 --> 3114.10]  So whenever I see people out there saying, well, we deserve this.
[3114.10 --> 3114.62]  No, you don't.
[3114.62 --> 3116.60]  And people hate when I say that to them.
[3116.60 --> 3117.80]  But guess what?
[3118.76 --> 3119.94]  Your life is great.
[3120.14 --> 3120.86]  You know why it is?
[3120.86 --> 3122.16]  Because you can see my tweets.
[3123.98 --> 3125.38]  And you're like, what does that mean?
[3125.38 --> 3130.70]  Well, there's a whole part of this world that either can't because they're sick, can't because
[3130.70 --> 3134.34]  they can't afford the tech to get here, or can't because they're just looking in other
[3134.34 --> 3138.78]  directions because they're so busy trying to actually get through life and think you're
[3138.78 --> 3139.68]  not one of those people.
[3139.68 --> 3144.04]  And I'm not saying, this is not basically saying that there's someone worse than us.
[3144.36 --> 3145.12]  But here's the thing.
[3145.26 --> 3145.96]  Think about this.
[3146.60 --> 3148.52]  You don't deserve anything.
[3148.86 --> 3150.94]  Everything you have is you earned it.
[3151.12 --> 3153.10]  And this is how you get rid of imposter syndrome.
[3153.46 --> 3154.64]  You know how you're here right now?
[3154.68 --> 3155.54]  Because you earned it.
[3155.70 --> 3156.94]  There is no imposter syndrome.
[3157.54 --> 3160.30]  What it is, you're here because you're supposed to be here.
[3160.92 --> 3161.82]  And that's it.
[3162.08 --> 3162.88]  Don't question it.
[3163.80 --> 3164.82]  I can live with that.
[3164.94 --> 3166.22]  Oh, hold on one second though.
[3166.58 --> 3167.28]  Oh, another one?
[3167.58 --> 3167.88]  No.
[3167.88 --> 3171.54]  So in the peanut gallery, somebody said that's not unpopular.
[3172.34 --> 3172.76]  All right.
[3173.04 --> 3174.24]  So one more quick one.
[3174.76 --> 3175.78]  Here's what it is.
[3176.22 --> 3180.28]  Twitter fame, work fame, it's all crap.
[3180.54 --> 3181.94]  Maybe this is not unpopular either.
[3182.36 --> 3183.06]  But here's the thing.
[3183.14 --> 3187.72]  That famous person you know is only famous because they impressed another famous person.
[3188.42 --> 3192.30]  And people who are seeking that, trying to be famous and try to do this, basically,
[3192.30 --> 3195.16]  you're not even measuring up to your own levels if that's what you're seeking.
[3195.16 --> 3199.62]  What you're actually seeking is someone who probably doesn't really care about you, acceptance.
[3200.24 --> 3201.66]  And you really have to stop that.
[3202.14 --> 3205.12]  So that is my unpopular opinions.
[3205.30 --> 3207.16]  And actually, here's the most unpopular opinion.
[3207.34 --> 3208.34]  And this will leave it.
[3208.34 --> 3213.44]  I hate to say this, but most likely, I am smarter than you.
[3213.56 --> 3214.94]  And you might want to debate it.
[3215.00 --> 3216.20]  And you might think, oh, no, Brian's wrong.
[3216.30 --> 3218.34]  No, literally, I am probably smarter than you.
[3218.70 --> 3220.68]  So we can debate that.
[3220.74 --> 3221.88]  But you will be wrong.
[3222.44 --> 3224.28]  And I will leave it at that, definitely.
[3224.28 --> 3229.04]  That is a great ending.
[3232.04 --> 3233.00]  There's no rebuttals.
[3233.16 --> 3234.66]  They can't come debate you on the show.
[3235.82 --> 3238.24]  It's like a mic drop right there.
[3238.40 --> 3239.56]  Because I'm smarter than them.
[3243.12 --> 3244.10]  Oh, my goodness.
[3244.30 --> 3244.66]  Awesome.
[3244.84 --> 3245.12]  Awesome.
[3245.38 --> 3250.76]  Well, Brian, this has been both an educational and entertaining show.
[3250.96 --> 3252.48]  Thank you so much for coming on the show.
[3252.70 --> 3253.84]  It's been a pleasure having you.
[3254.82 --> 3255.26]  Yeah.
[3255.42 --> 3257.68]  Any parting gifts, parting words?
[3258.36 --> 3260.00]  Yes, I do have a parting word.
[3261.50 --> 3263.42]  Leave the world better than you found it.
[3264.22 --> 3266.06]  There's always someone doing worse than you.
[3266.48 --> 3268.00]  You don't have to help everyone doing.
[3268.16 --> 3269.72]  But turn around and help that next person.
[3270.12 --> 3274.20]  And tell them the only way that you can continue doing this is if they turn around and help that next person.
[3275.06 --> 3279.68]  So realize that the world gets better when we all work together to make it better.
[3280.08 --> 3281.10]  It ain't about politics.
[3281.20 --> 3282.22]  It ain't about anything else.
[3282.22 --> 3284.98]  It's about people helping people be better people.
[3285.42 --> 3285.88]  That's it.
[3285.88 --> 3291.30]  I love that you don't have to help everybody, but just help the next person in the line.
[3291.42 --> 3293.96]  It's like some kind of kindness blockchain.
[3294.78 --> 3297.20]  And I think, yeah, I like it.
[3297.48 --> 3298.06]  I like that one.
[3298.06 --> 3298.54]  Awesome.
[3298.54 --> 3298.62]  Awesome.
[3300.86 --> 3303.70]  Well, listener, we hope you've enjoyed the show.
[3304.30 --> 3307.14]  And please tune in next time on the next Go Time.
[3307.14 --> 3313.26]  Thank you for listening to this episode of Go Time.
[3313.60 --> 3316.72]  More like this at changelog.com slash go time.
[3316.82 --> 3321.92]  There you'll find our latest as well as the lists of our most popular episodes and the ones we recommend.
[3321.92 --> 3325.08]  I personally recommend episode 110, the fireside chat.
[3325.40 --> 3326.12]  It's a great listen.
[3326.12 --> 3330.78]  Thanks again to Brian Lyles for inviting us into his world of random thoughts.
[3331.28 --> 3332.20]  Follow him on Twitter.
[3332.36 --> 3333.60]  He's at Brian L.
[3333.76 --> 3335.92]  That's B-R-Y-A-N-L.
[3336.58 --> 3339.58]  This episode was hosted by Johnny Borsico and Matt Reier.
[3340.06 --> 3349.22]  If you got a chuckle out of Matt's kindness blockchain joke, hop in the Go Time FM channel of Gopher Slack and ask about the follow-on joke that we had to cut to keep the show family friendly.
[3349.98 --> 3354.48]  Our music is produced by the mysterious Breakmaster Cylinder and we're brought to you by awesome sponsors.
[3354.92 --> 3357.26]  Special thanks to Fastly, Linode, and Rollbar.
[3357.78 --> 3358.70]  That's all for now.
[3359.02 --> 3360.04]  We'll talk to you next week.
[3360.04 --> 3361.04]  Bye.
[3369.58 --> 3370.58]  Bye.
[3399.58 --> 3420.94]  Okay, yeah.
[3421.40 --> 3429.10]  I was thinking actually earlier, do you prefer to edit, to like change code when you're refactoring something?
[3429.10 --> 3430.16]  To just change it?
[3430.22 --> 3433.52]  Or do you prefer to kind of rewrite it wholesale, that piece?
[3434.56 --> 3435.62]  Does anyone have any preferences?
[3436.62 --> 3437.58]  It depends.
[3437.78 --> 3442.06]  That's a really weird question, but it really depends.
[3442.20 --> 3447.10]  It depends on really how bad Past Brian was.
[3447.44 --> 3449.16]  I was looking at this code earlier.
[3449.78 --> 3451.14]  It was yesterday or the day before.
[3451.92 --> 3457.74]  And I was trying to figure out how to refactor it because I was like, we need to change this because I need to add new features.
[3457.74 --> 3461.82]  And I was going through the call tree and I usually just write it down.
[3461.98 --> 3463.88]  I don't even use the debug print stack trace.
[3463.96 --> 3466.68]  I just went through and went through all the method calls to see what it was doing.
[3467.10 --> 3470.06]  And it was pretty much eight more calls than it needed to be.
[3470.50 --> 3473.44]  In that case, I am actually going to rewrite it.
[3473.44 --> 3476.78]  And just wholesale, I actually said, nope, this is done.
[3476.92 --> 3478.36]  I'm going to rewrite the whole thing.
[3478.68 --> 3485.18]  But generally, if it's just a small piece and I'm either one, confident I have test coverage or two, don't really care.
[3485.44 --> 3488.68]  I might just go in and say, we're going to live once.
[3488.68 --> 3491.20]  Just tweak it, hack it.
[3491.66 --> 3494.06]  Testing, test coverage does enable that, doesn't it?
[3494.12 --> 3497.88]  You can, with quite a lot of confidence, you can sort of be quite bold.
[3498.40 --> 3506.18]  But I always find still just like if I have to change something that already exists, it depends if you're right.
[3506.24 --> 3509.46]  If the design's changing a lot, it's different.
[3509.56 --> 3512.48]  But I like to just, I think, always just sort of rewrite it.
[3512.48 --> 3516.14]  It's just like now I know what it's meant to be, I can do it again.
[3516.26 --> 3523.82]  But I wondered if that was just a preference thing or if others do have different thoughts.
[3523.82 --> 3528.96]  But I think it's a testament to, one, how well your tests are written.
[3529.22 --> 3533.66]  And two, how well your abstraction is around what you're trying to do.
[3534.18 --> 3540.94]  And I guess I'm not going to sound like old guy, but really when it comes down to it, if it's hard to change, you messed up.
[3541.46 --> 3542.34]  And that's fine.
[3542.48 --> 3543.36]  I mean, we're developers.
[3544.50 --> 3549.76]  They wouldn't give us backspaces and get history if we were going to get it right the first time.
[3550.10 --> 3551.14]  Wait, there's a backspace?
[3552.32 --> 3554.94]  I've just been, oh, I could have really used that.
[3555.28 --> 3558.28]  I've been just starting again when I make a mistake.
[3559.62 --> 3560.86]  Yeah, backspace.
[3562.16 --> 3564.28]  I like that it's called backspace as well.
[3564.28 --> 3567.76]  It's like, properly comes from old typewriters probably, doesn't it?
[3567.82 --> 3569.80]  Like underscore, right?
[3570.16 --> 3572.30]  Backspace literally is just moving it back a space.
[3572.30 --> 3572.70]  I suppose.
[3573.98 --> 3575.02]  Yeah, we could have.
[3575.14 --> 3579.66]  We definitely dropped a good chance to give it a much better name.
[3580.14 --> 3580.46]  Yeah.
[3580.62 --> 3582.56]  And then delete, of course.
[3582.94 --> 3583.30]  Does it?
[3583.60 --> 3585.72]  It's this strange deleting the other way.
[3585.72 --> 3588.14]  On Windows it was that anyway, wasn't it?
[3589.20 --> 3590.62]  Yeah, I don't know how it works.
[3590.80 --> 3593.08]  I have a delete key on my keyboard.
[3593.64 --> 3595.02]  I don't think I ever use it.
[3595.48 --> 3596.26]  No, I do.
[3596.60 --> 3599.24]  I use it because my keyboard can control Spotify.
[3599.24 --> 3603.86]  And I think that's the stop command if I use it with the function key.
[3604.20 --> 3604.86]  So that's what I do.
[3604.86 --> 3608.44]  I thought you were going to say you could delete songs or something on Spotify.
[3608.44 --> 3608.90]  No, I never.
[3610.30 --> 3612.18]  Anything that you just don't like, gone.
[3612.86 --> 3613.74]  That'd be good, wouldn't it?
[3613.74 --> 3615.88]  All right.
[3615.92 --> 3617.28]  I'm ready if you are.
[3618.36 --> 3619.66]  Yes, I believe so.
[3619.72 --> 3620.80]  Yeah, this is just the pre-show.
[3621.20 --> 3626.36]  So if the pre-show is that good, how are we in the rest of it?
[3626.76 --> 3627.98]  It's going to be, you know.
[3628.30 --> 3629.10]  It's going to be great.
[3629.62 --> 3630.64]  Unless we've peaked.
[3630.64 --> 3632.86]  No, not yet.
[3633.10 --> 3634.68]  We haven't peaked yet.
[3635.00 --> 3635.58]  I hope not.
[3635.82 --> 3637.24]  We haven't jumped a shark, as they say.
[3637.98 --> 3641.48]  I mean, this is my second time on go time.
[3642.86 --> 3645.64]  So, yeah, maybe it has jumped the shark.
[3645.84 --> 3649.66]  If you're back to me, my gosh, there's so many interesting people out there.
[3650.28 --> 3651.34]  Yep, maybe we're done.
[3651.76 --> 3652.28]  This is it, people.
[3652.28 --> 3654.20]  This is the last episode we didn't know about.
[3654.64 --> 3655.58]  Yeah, last one.
[3658.34 --> 3658.90]  All right.
[3658.90 --> 3659.92]  Let me get in character here.
[3659.92 --> 3662.10]  Let me get my voice.
[3663.02 --> 3664.86]  I should have drank some tea before this.
[3665.02 --> 3666.08]  You're not wearing your wig.
[3668.14 --> 3670.00]  Normally wears a podcasting wig.
[3671.06 --> 3674.16]  Yeah, my podcast wig and socks.
[3674.46 --> 3674.56]  Yeah.
[3674.64 --> 3674.86]  Yeah.
[3674.86 --> 3675.48]  That's it.
