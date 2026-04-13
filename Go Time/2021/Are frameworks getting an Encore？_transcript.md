[0.00 --> 8.54]  What you as a developer have to do is just focus on building your product instead of spending a lot of time on things surrounding your product.
[8.72 --> 13.90]  Infrastructure and operations and boilerplate and configuration and all of this stuff.
[14.14 --> 14.30]  Okay.
[14.52 --> 17.16]  We're basically automating Johnny out of his job.
[17.64 --> 21.82]  Oh, Natalie came to fight today.
[22.40 --> 25.26]  No, no, I'm asking to summarize this in a very clear way.
[25.26 --> 30.48]  I think it's important to remember that operations and SRE in particular will never go away.
[30.64 --> 32.30]  A tool cannot replace that.
[32.74 --> 33.70]  True diplomat.
[33.88 --> 34.98]  Three of them there, Johnny.
[36.64 --> 37.06]  I'll see you.
[37.08 --> 38.38]  I expect to check in the mail.
[40.90 --> 47.76]  No, but it's more about when you have SREs, unless they're very, very nice, they're not going to sit and do your work for you.
[47.76 --> 55.42]  They can handle a lot of the operations aspect, but somebody still needs to do all the work to get the code into production.
[57.24 --> 59.88]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[60.10 --> 60.82]  We love Linode.
[60.90 --> 62.32]  They keep it fast and simple.
[62.46 --> 64.80]  Check them out at linode.com slash changelog.
[65.04 --> 67.12]  Our bandwidth is provided by Fastly.
[67.46 --> 71.00]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[71.28 --> 73.00]  Get a demo at LaunchDarkly.com.
[73.78 --> 74.66]  What's up, Gophers?
[74.66 --> 84.40]  Our friends over Gravitational made a big transition at the end of 2020 to rebrand as Teleport and shared a new product announcement to showcase the direction they're taking.
[84.76 --> 93.80]  Teleport is operating from a vision of being able to run and access software anywhere in a secure and compliant manner, something they call environment-free computing.
[93.80 --> 107.56]  With Teleport, engineering teams can quickly access any resource anywhere using a unified access plane that consolidates access controls and auditing across all environments, infrastructure, applications, as well as data.
[107.90 --> 114.58]  Teleport server access lets you SSH securely into Linux servers and smart devices with a complete audit trail.
[114.94 --> 120.84]  Teleport Kubernetes access lets you access Kubernetes clusters securely with complete visibility to access and behavior.
[120.84 --> 127.80]  And finally, Teleport application access lets you access web apps running behind NAT and firewalls with security and compliance.
[128.16 --> 131.70]  Try Teleport today in the cloud, self-hosted, or open source.
[132.04 --> 134.64]  Head to goteleport.com to learn more and get started.
[135.00 --> 136.98]  Again, goteleport.com.
[136.98 --> 158.44]  Let's do it.
[159.02 --> 160.08]  It's go time.
[160.80 --> 165.50]  Welcome to Go Time, your source for diverse discussions from around the Go community.
[165.50 --> 172.46]  We record the show live on YouTube each and every Tuesday at 3 p.m. U.S. Eastern, 7 p.m. UTC.
[173.02 --> 177.80]  Subscribe at youtube.com slash changelog to be notified when we go live.
[178.08 --> 183.78]  And don't forget to follow Go Time FM on Twitter and vote on our unpopular opinion polls.
[184.10 --> 185.52]  This is very important stuff.
[185.84 --> 186.90]  Okay, let's do this.
[187.06 --> 187.38]  Here we go.
[187.38 --> 195.60]  Hello and welcome to Go Time.
[195.90 --> 197.84]  Yes, your ears do not deceive you.
[198.02 --> 199.50]  It's me, Johnny, and I'm back.
[199.90 --> 202.18]  I'm a short hiatus and feeling a bit refreshed.
[202.72 --> 206.08]  Although, I just came off of a long uncalled stint.
[206.18 --> 208.10]  So, let's hold off on the refresh.
[208.44 --> 209.46]  Yeah, we'll get back to that.
[209.46 --> 213.66]  Anyways, I bring with me my charming co-host, Natalie Pistonovich.
[213.86 --> 214.18]  Hello.
[214.56 --> 216.04]  And Jared Sento.
[216.28 --> 216.58]  Hello.
[217.20 --> 219.02]  You might be wondering, who are we hosting today?
[219.28 --> 222.76]  Well, before I tell you, you need to understand what we're going to be talking about today.
[222.92 --> 228.12]  The show's topic is developer productivity and their trade-offs.
[228.34 --> 229.92]  There are always trade-offs.
[229.92 --> 236.34]  And our guest today, Mr. Andre Erickson, has no doubt had to make some as the creator of Encore,
[236.60 --> 242.28]  a seemingly kitchen sink included back-end framework that is currently making the rounds in the Go community.
[242.60 --> 243.20]  So, welcome, Andre.
[243.38 --> 244.10]  Thank you very much.
[244.22 --> 246.08]  So, I have to sort of forewarn you.
[246.92 --> 249.30]  This is not going to be an episode about Encore.
[249.76 --> 253.54]  What we want to know are some of the lessons you've learned, right?
[253.60 --> 257.76]  And indeed, some of the trade-offs you've had to make over the course of building such a framework.
[257.76 --> 261.00]  So, I checked it out and there's a lot going on in there.
[261.12 --> 263.80]  And I'm sure we'll be touching on some of these things as we go, right?
[264.06 --> 267.28]  But first, I want us to sort of frame the discussion a little bit.
[267.56 --> 271.26]  What do you understand by developer productivity?
[271.66 --> 274.48]  I think there are two very different perspectives on this question.
[274.94 --> 281.36]  And I think, on the one hand, you can take a very rational approach and you can talk about it in terms of mathematics, right?
[281.36 --> 291.24]  And when you think about it that way, developer productivity is essentially about how do we spend as little time as possible on things that don't matter?
[291.90 --> 295.66]  Like, you know, things that aren't really bringing your product forward.
[295.88 --> 297.98]  What I call undifferentiated work.
[298.52 --> 306.34]  And the second part is when you actually are working on things that bring your product forward, you want to do that as quickly as possible.
[306.34 --> 308.04]  So, how can we speed that part up?
[308.36 --> 314.40]  But I think a different perspective is how do we make development as enjoyable as possible?
[314.70 --> 318.98]  How can we make it so that we're spending time working on the things that we enjoy?
[319.58 --> 322.30]  And, of course, that's a much more personal question.
[322.54 --> 325.58]  And exactly what that means will vary from person to person.
[325.92 --> 331.72]  Some people spend, really enjoy working on infrastructure and DevOps and build systems and this sort of thing.
[331.72 --> 337.20]  And for me, I really love working on creating things for the end user.
[337.82 --> 342.42]  So, finding ways to make the end user's lives just a little bit better.
[342.92 --> 345.98]  But it all depends on what you're enjoying as a person.
[346.48 --> 350.68]  But those are the two main perspectives that I think about when it comes to developer productivity.
[351.00 --> 351.10]  Okay.
[351.46 --> 360.52]  This coming from someone who has a very, very specific definition of that in their minds, given that you're a framework and tool author, right?
[360.52 --> 371.50]  Now, what I want to understand and know, especially from my co-hosts, Natalie and Jared, as far as I know, neither of you has authored a framework or tool or anything like that.
[371.56 --> 374.08]  At least not at the scale that Andre has, right?
[374.12 --> 378.06]  So, you and I tend to be users of these kinds of tools.
[378.64 --> 386.32]  So, I'm going to ask Natalie to go first to tell me, what do you seek, right, as productivity, right, from your developer tooling?
[386.40 --> 387.20]  What does that mean to you?
[387.20 --> 387.68]  Yeah.
[389.04 --> 394.60]  I was just thinking that this answer changed a lot through the years that I was a developer.
[394.76 --> 400.74]  Because in the beginning, I would probably, like, if there was more, it would might be overwhelming for me, right?
[400.76 --> 403.54]  Like, all those features and, like, shortcuts and whatnot.
[403.86 --> 407.22]  And even arguments of which one, which IDE is better.
[407.32 --> 408.02]  Things like this.
[408.02 --> 416.98]  And I do think that now that I've been doing the same thing for a while, I know better kind of what works for me specifically.
[417.26 --> 421.62]  And I know to be careful when I answer because for others, it might be different.
[422.18 --> 425.82]  For others who are in a different place, it might be a bit different.
[425.82 --> 430.38]  And it might be even, like, how do I ever get to have a search to a place where I have such an opinion?
[430.74 --> 434.08]  It's also a thought that you can have hearing such a question and such a discussion.
[434.32 --> 436.66]  And how do I learn that when I learn the language and everything?
[436.80 --> 439.10]  So, lots of meta instead of answering.
[439.24 --> 443.72]  And all that is immediately going through the mind when we talk about developer productivity.
[443.72 --> 451.02]  And it would be also interesting to have different parts of our conversation today focus on what is it like for beginners?
[451.22 --> 453.40]  What is it like for people who are very advanced?
[453.50 --> 459.10]  What is it like for the people who are beyond all of us and actually build the tool and can say why and when what?
[459.74 --> 469.28]  I use for my IDE VS code and things that I find super useful is that when pulling all sorts of libraries, it shows me the signature code, for example.
[469.28 --> 473.40]  That's, like, something maybe a little bit basic, but I find it super useful.
[473.72 --> 477.84]  I know that in core it has way advanced things like tracing.
[478.20 --> 481.56]  This is something that I find always useful, always interesting.
[481.94 --> 489.12]  And I only got to introduce this into a code base as a recommendation, kind of, in a previous job that I had as an engineering manager.
[489.24 --> 494.32]  So, I never had to do this on my own just to convince other people to do this because I think it's useful.
[494.72 --> 497.22]  Like, I still think this is something that could be super useful.
[497.22 --> 504.86]  And I am looking forward to try this in my projects and see how can this make life easier even without the extra work.
[505.10 --> 508.50]  Those are the two main things that come to my mind when we talk about productivity.
[509.04 --> 509.48]  Jared, hit me.
[509.70 --> 511.42]  Yeah, I think Natalie's point is well taken.
[511.60 --> 515.02]  To define developer productivity, please define developer, you know?
[515.02 --> 520.76]  And it's like, well, it's hard to do that because we're all shapes and sizes and backgrounds and experiences.
[521.12 --> 523.04]  And we all, there's a subjective side to that.
[523.08 --> 524.66]  So, I'll answer it subjectively.
[525.02 --> 527.98]  I'm not a math guy, so I can't do the math side that Andre brought.
[528.22 --> 536.32]  Well, I'll say that generally speaking, I look at how can I quickly and, to a certain degree, enjoyably, get my ideas into the world.
[536.32 --> 545.48]  From the point where I've conceived a notion or my customer has conceived a notion and we've decided this is something worth doing, how quickly can I take that to fruition?
[545.74 --> 546.58]  That's productive.
[547.06 --> 550.22]  Sometimes that means getting into the flow and staying in the flow.
[550.56 --> 554.42]  And so, my productivity is affected by my surroundings, right?
[554.72 --> 560.02]  Externalities, things that aren't even in the computer but they're around me or in Slack or in these other places.
[560.02 --> 567.24]  Other times, it's actually in my editor with my programming language, with my tool set or my framework.
[567.86 --> 571.96]  And I'm trying to harness those tools, you know, to get that idea out.
[572.38 --> 580.90]  And so, when I think about those specific aspects, we're talking about frameworks, libraries, tools, then I really appreciate things that take the minutiae away.
[581.38 --> 584.28]  Don't make me think about things that I don't care about.
[584.60 --> 589.08]  Help me to focus on the differentiated aspects of what I'm trying to do, right?
[589.08 --> 594.50]  My particular view and me trying to accomplish that aspect.
[595.14 --> 597.98]  Everything else is minutiae.
[598.44 --> 601.32]  And it really kind of makes you feel unproductive.
[602.30 --> 605.38]  Configurations, picking this, picking that, customizations.
[606.54 --> 609.70]  Sometimes data structures can be that if they're common things.
[609.86 --> 612.06]  Other times, data structures are your application, right?
[612.58 --> 616.46]  So, that's all subjective, or not subjective, but kind of an it depends place.
[616.46 --> 618.92]  So, there's lots of things that you can define that, of what that is.
[619.08 --> 625.18]  But if I'm not focusing on the uniqueness of the problem I'm trying to solve, then I'm not feeling productive.
[625.18 --> 636.54]  I think you touched on a really important aspect, which is, I think a lot of people intuitively think about developer productivity and developer tools as being about things that happen when you're writing code.
[636.86 --> 644.36]  But what you highlighted is that the end-to-end process of getting something in front of users is so much more than that, right?
[644.36 --> 648.04]  It's about, first of all, having an idea that you want to try.
[648.56 --> 650.92]  And then there's usually some coding involved.
[651.62 --> 652.80]  Sometimes there isn't.
[652.96 --> 655.08]  But then there's collaboration with other people.
[655.74 --> 660.16]  There is some sort of, usually, review process and verification.
[660.64 --> 662.14]  Are we making the right change?
[662.14 --> 669.38]  And then there's some sort of, talking specifically about backend, but I think there are analogies to other areas.
[669.94 --> 673.96]  Some sort of deployment, or like, how do you actually get it in front of users?
[674.66 --> 678.54]  And after that, how do you make sure that everything works?
[678.88 --> 681.42]  How can you address any issues that pop up?
[681.66 --> 685.72]  All of this is like the end-to-end feedback loop of building things.
[685.72 --> 695.94]  And I think often you just focus on a very small part of the whole, when you think, like, how do we get people to write 10 characters less in their editor or whatever?
[696.24 --> 699.06]  But the whole cycle is so much bigger than that.
[700.14 --> 700.94]  I hear all of that.
[701.00 --> 706.80]  And I'm thinking, just like Natalie says, when you say productivity, it depends on sort of your approach, right?
[706.82 --> 708.34]  What context are you working in, right?
[708.62 --> 710.14]  Jared asked, like, developer productivity.
[710.32 --> 711.56]  Well, define developer, right?
[711.56 --> 715.64]  So the idea then becomes, what layer are we talking about?
[715.72 --> 716.68]  Of developer productivity.
[717.04 --> 720.68]  Because I can think of just three off the top of my head.
[721.68 --> 725.18]  So there's developer time productivity, which is Natalie touched on.
[725.26 --> 727.46]  When I'm coding, I'm getting that IntelliSense.
[727.66 --> 729.42]  It's helping me get my job done faster.
[729.58 --> 732.44]  I don't have to work hard to write the code itself, right?
[732.88 --> 734.32]  There's deploy time productivity.
[734.98 --> 743.36]  How easy is it for me to ship that thing from an idea in my head or when I sit down with a customer or prospect and then translate that into working software?
[743.36 --> 750.50]  For me, as an operations sort of focused engineer, there's the operational sort of aspect of productivity.
[750.92 --> 753.06]  If I can't operate this piece of code, right?
[753.10 --> 759.32]  If I can't monitor it, if I can't trace things, requests coming in to see where a problem exists, I can't collect metrics.
[759.32 --> 766.54]  You know, metrics, if I can't observe it, to use the more sort of a trendy term these days, beyond just monitoring, you can't just say monitoring anymore.
[766.58 --> 767.84]  You have to be observable, right?
[768.32 --> 771.28]  If you want to stretch it beyond sort of the technical aspects of things, right?
[771.66 --> 772.88]  There's the business.
[772.98 --> 777.16]  How easy is it for the intended audience to derive value of the solution that you put together?
[777.16 --> 781.52]  So there's a lot of sort of layers to this productivity question, right?
[781.76 --> 786.56]  So to me, when you're writing a framework or a tool, you kind of have to pick your battles.
[786.56 --> 789.56]  Like which layer of productivity we're talking about here, right?
[789.58 --> 794.34]  Are you developing a VS Code extension to make my dev time productivity give that a boost?
[794.78 --> 797.32]  Are you making my productivity giving that a boost?
[797.50 --> 799.34]  Like which layer are we talking about here?
[799.48 --> 804.76]  I'm interested in sort of understanding in your work, you've identified several of these areas.
[804.76 --> 807.44]  Some of the stuff you're working on touches on many of these layers.
[807.72 --> 813.38]  What was the most important of these problem sets, right, for you to sort of tackle multiple of them?
[813.66 --> 816.42]  Like in what order did they feel to you like they needed to be solved?
[817.16 --> 818.22]  So I think that's super interesting.
[818.40 --> 822.10]  And I really agree with your characterization of the different layers.
[822.10 --> 832.20]  I guess Encore is in many ways contrarian in that I firmly believe that to really unlock much greater productivity,
[832.20 --> 835.82]  we actually need to look across these layers.
[836.32 --> 842.16]  And nowadays, most tools, as you pointed out, only operate in one layer.
[842.62 --> 849.48]  But when you actually bridge that gap, you end up getting something that is much more powerful.
[850.14 --> 855.96]  And what underpins Encore is really this belief that to really provide a better experience
[855.96 --> 861.96]  in all of these layers, we need to better understand what an application is doing.
[861.96 --> 869.08]  Because when we as developers are building an application, we have a mental picture in our heads of how it works,
[869.14 --> 870.24]  how everything fits together.
[870.50 --> 874.42]  And generally speaking, our tools do not share that understanding.
[874.90 --> 879.36]  They generally just think of it as code and files when you're in an editor.
[879.36 --> 888.26]  And when you're at this operations layer, suddenly we package everything into a container and treat it as a black box,
[888.26 --> 891.34]  where we have no idea how it all fits together.
[891.72 --> 897.84]  We can kind of try to figure it out based on network connections between different parts and so on.
[898.16 --> 902.76]  But we're really lacking this map of how everything fits together.
[902.76 --> 910.82]  And so what Encore is trying to do is really bridge that gap and build up a very detailed mental model
[910.82 --> 916.38]  of how your application fits together and then try to improve on all of these layers.
[916.80 --> 924.36]  So that's why we're combining what is essentially a framework that's just a way to get this sort of understanding.
[924.84 --> 929.86]  And then we use that understanding in the other layers to provide things like tracing and so on.
[929.86 --> 937.14]  Because it turns out that the challenges with developer productivity, they don't firmly fit into one layer or the other.
[937.88 --> 941.78]  And by looking across the whole, we can create a much better experience.
[942.20 --> 946.20]  If I'm a junior developer and I want to use a tool, any tool, Encore included,
[946.48 --> 950.82]  what questions should I be asking myself as a junior developer?
[951.04 --> 954.16]  And we're going to get to the senior developers and the architects and all that stuff.
[954.16 --> 959.60]  Because different people at those layers too are going to be looking at something like Encore and be like,
[959.60 --> 964.10]  hmm, you're doing too much or hmm, you're doing not enough, right?
[964.22 --> 965.90]  So again, perspectives, right?
[966.02 --> 969.50]  So if you're a junior developer, right, and you see something like Encore,
[969.68 --> 971.70]  is there some learning that you have to go do?
[971.78 --> 974.96]  Like all of a sudden, if you were just happy writing code and then, you know,
[974.98 --> 977.38]  you know somebody else is going to deploy it and package it and ship it.
[977.94 --> 983.26]  Now something like Encore comes along and it's talking about all these deployment mechanisms,
[983.62 --> 985.50]  orchestration and tracing, whatever.
[985.80 --> 987.52]  They might not even know what tracing is, right?
[987.52 --> 991.66]  So another way of asking this question, for whom did you build Encore?
[992.02 --> 996.28]  The junior, the senior, the architect, the people who knows what's going on up and down the stack?
[996.40 --> 997.20]  Who's your audience here?
[997.32 --> 1001.28]  And how should each level of competency with the whole life cycle,
[1001.68 --> 1003.30]  like what comfort level should they be at?
[1003.56 --> 1006.20]  So I actually think Encore can be a good fit for all of them.
[1006.40 --> 1011.70]  I think it's less about the experience level and more about what your requirements are on the product side.
[1011.70 --> 1019.08]  Like depending on what you're creating, sometimes your technical requirements are incredibly low level
[1019.08 --> 1024.62]  and you require enormous flexibility and control at the lowest level of the stack.
[1025.32 --> 1031.80]  And then Encore is definitely not the tool for you because it's operating at a higher abstraction level.
[1032.02 --> 1035.36]  At least not today, we don't offer a bunch of these low level knobs.
[1035.36 --> 1042.56]  And on the other hand, if you're building something where you don't need that level of control,
[1043.32 --> 1049.54]  and then Encore can be a great fit just because it takes away and makes reasonable decisions
[1049.54 --> 1053.74]  that usually are very sound, but they are not right for everybody.
[1054.08 --> 1060.04]  And so we've had people using Encore and they really love it across all experience levels.
[1060.04 --> 1065.90]  But it really comes down to what your application has in terms of its requirements.
[1066.48 --> 1070.20]  Encore or not, I think that's something you always need to start with.
[1070.40 --> 1073.92]  Like what is it that you are building and what are the challenges you're having?
[1074.10 --> 1076.10]  And then choose the right tool from that perspective.
[1076.44 --> 1077.88]  I think that's always where you have to start.
[1078.32 --> 1083.88]  Natalie, would you put a framework that does so many things in front of a junior developer?
[1084.26 --> 1087.28]  When you say so many things, I guess you mean Encore.
[1087.52 --> 1088.74]  Encore or something like it.
[1088.74 --> 1090.84]  Actually, the things that it's doing.
[1091.08 --> 1095.46]  We're 20 minutes into the episode and actually realized that probably everybody who's listening
[1095.46 --> 1097.22]  by now has Googled what it does.
[1097.62 --> 1102.78]  But maybe we can mention a few of the things just to organize things in people's heads.
[1103.36 --> 1103.80]  You know what?
[1103.98 --> 1105.02]  You should be hosting this show.
[1105.06 --> 1106.88]  That is a very good point you're making.
[1109.24 --> 1110.00]  Host swap.
[1110.42 --> 1110.66]  All right.
[1110.80 --> 1111.34]  So, okay.
[1111.36 --> 1112.54]  We'll come back to that question then.
[1112.76 --> 1116.44]  Andre, give us a high level of what Encore does.
[1116.44 --> 1120.30]  I like to describe it as a game engine for back-end development.
[1120.86 --> 1128.32]  And what that means is when you're developing a game, you have game engines like Unity and
[1128.32 --> 1135.18]  Unreal Engine that provide like a really integrated experience that is custom made for building
[1135.18 --> 1135.54]  a game.
[1135.54 --> 1141.58]  And when you use those, they provide a lot of value for you.
[1141.76 --> 1151.34]  So you never have to write your own 3D render or multiplayer or AI or pathfinding or physics
[1151.34 --> 1152.46]  and so on.
[1152.64 --> 1155.40]  Because those are things that almost every game needs.
[1155.64 --> 1158.12]  So the game engine provides it for you.
[1158.12 --> 1161.56]  And the end result is a very, very productive experience.
[1161.92 --> 1163.88]  Encore is the same thing for back-end development.
[1164.58 --> 1171.78]  And specifically, you write Go and you do it in a way that Encore understands what it is
[1171.78 --> 1172.24]  you're doing.
[1172.46 --> 1178.26]  So when you're defining an API, when you're making an API call from one back-end service
[1178.26 --> 1186.06]  to another, what request and response schemas for every API endpoint, what infrastructure your
[1186.06 --> 1191.50]  service requires, whether it's a database or something else, where you're interacting with
[1191.50 --> 1194.72]  the database, what secrets you need.
[1195.30 --> 1201.78]  And then Encore takes that code and orchestrates it all together so that you don't have to deal
[1201.78 --> 1208.46]  with setting up infrastructure, marshalling requests to JSON or whatever you use for serializing
[1208.46 --> 1210.32]  and so on and so on and so on.
[1210.32 --> 1216.22]  So that what you as a developer have to do is just focus on building your product instead
[1216.22 --> 1223.20]  of spending a lot of time on things surrounding your product, like infrastructure and operations
[1223.20 --> 1227.12]  and boilerplate and configuration and all of this stuff.
[1227.26 --> 1227.74]  That's the idea.
[1228.08 --> 1228.26]  Okay.
[1228.48 --> 1231.12]  We're basically automating Johnny out of his job.
[1231.68 --> 1232.04]  Oh.
[1233.50 --> 1235.96]  Oh, Natalie came to fight today.
[1236.52 --> 1237.04]  No, no.
[1237.12 --> 1239.38]  I'm asking to summarize this in a very clear way.
[1239.38 --> 1242.96]  Actually, when you were saying that, you also said at some point the engine will provide
[1242.96 --> 1246.68]  and I had to think of Snowpiercer and that was also a little bit entertaining.
[1247.56 --> 1253.10]  Is it some way of saying that this is a little bit automating things that are related to infrastructure,
[1253.10 --> 1257.66]  to SRE ops and only letting you do more backend work?
[1258.10 --> 1263.66]  I think it's important to remember that operations and SRE particular will never go away.
[1263.88 --> 1265.82]  Like a tool cannot replace that.
[1266.24 --> 1267.30]  But true diplomat.
[1267.40 --> 1267.48]  Yeah.
[1267.60 --> 1268.48]  Three of them there, Johnny.
[1269.38 --> 1270.58]  I'll see you.
[1270.58 --> 1271.90]  I'll expect a check in the mail.
[1274.70 --> 1279.44]  No, but it's more about when you have SREs, unless they're very, very nice,
[1279.52 --> 1281.74]  they're not going to sit and do your work for you.
[1281.74 --> 1288.78]  They can handle a lot of the operations aspect, but somebody still needs to do all the work
[1288.78 --> 1290.22]  to get the code into production.
[1290.22 --> 1293.44]  So it's not replacing operations.
[1293.44 --> 1300.20]  It's more like, let's make it easier to get our code out there quickly.
[1300.20 --> 1306.84]  So it's much more about like, let's find all of these annoying parts of backend development
[1306.84 --> 1308.22]  and streamline them.
[1308.66 --> 1315.30]  So the end result is we'll just get your code up and running in a Kubernetes cluster incredibly
[1315.30 --> 1320.54]  simply, and it will all be done according to best practices.
[1320.54 --> 1325.32]  But you still have this level of control where when something is on fire, you still want
[1325.32 --> 1327.90]  to be able to get in there and really dig into things.
[1327.90 --> 1345.96]  This episode is brought to you by our friends at LaunchDarkly, feature management for the
[1345.96 --> 1349.36]  modern enterprise, power testing in production at any scale.
[1349.62 --> 1350.36]  Here's how it works.
[1350.78 --> 1355.30]  LaunchDarkly enables development teams and operation teams to deploy code at any time,
[1355.30 --> 1357.84]  even if a feature isn't ready to release to users.
[1358.20 --> 1362.42]  Wrapping code with feature flags gives you the safety to test new features and infrastructure
[1362.42 --> 1366.10]  in your production environments without impacting the wrong end users.
[1366.54 --> 1370.94]  When you're ready to release more widely, update the flag status and the changes are made instantaneously
[1370.94 --> 1372.88]  by the real-time streaming architecture.
[1373.32 --> 1377.56]  Eliminate risk, deliver value, get started for free today at LaunchDarkly.com.
[1377.90 --> 1379.58]  Again, LaunchDarkly.com.
[1385.30 --> 1385.74]  Cool.
[1396.14 --> 1400.60]  So, Jared, you've bootstrapped applications using frameworks and tools.
[1401.32 --> 1401.44]  Yes.
[1401.44 --> 1411.76]  I'm curious of where you draw the line in your mind, right? Between when those tools sort of do too much or too little. I'm curious how you see that.
[1412.22 --> 1427.48]  Yeah. So I wanted to do as much as possible until it boxes me into a corner and it won't do it the way I want it to. So I just, I'm not unreasonable, Johnny. I just want it to be everything and exactly the way I would write it. I kid a little, but there's some truth in that.
[1427.48 --> 1434.08]  I guess as GoTime's producer, let me just float a stereotype out and maybe have all three of you speak to it. This is on topic, Johnny. It's not completely off topic.
[1434.08 --> 1446.70]  I get the impression that Gophers, and this is a generalization, don't like frameworks. And here's Encore, it's a framework. And I wonder if that's part of the discussion here.
[1446.70 --> 1464.72]  It's like libraries are generally what I see people advocating for or suggesting and frameworks. I don't know any popular Go frameworks. Maybe I do if I had to think real hard. I don't know. All three of you can just speak to that. Is that a generalization that holds or am I misguided in saying that?
[1464.72 --> 1469.46]  I want Andre to answer this question last because I want to hear from Natalie and I have some opinions about that.
[1469.72 --> 1469.86]  Okay.
[1470.08 --> 1471.76]  This is my impression too.
[1471.98 --> 1472.18]  Okay.
[1472.26 --> 1486.52]  Most of the Gophers I know don't use a lot of frameworks or at all. One thing that I liked that I read about Encore that it does is that you write code and it's compiling it to be distributed for you.
[1486.52 --> 1501.38]  I'm really curious about this. Last year, there's a talk, somebody from Cockroach TV about how the error library in Go failed them a little bit in their work because it was not supporting distributed in a good way.
[1501.86 --> 1510.94]  And they had to rewrite that a little bit and then they kind of branched off to have a library or a library for that that is for distributed testing.
[1510.94 --> 1523.02]  So I think this can be an interesting spot. For me, this is a personal focus of curiosity for me. I said, I will not say that I looked at a lot of frameworks, but this is a reason I will look at this one.
[1523.58 --> 1524.56]  Now, here's my take.
[1524.84 --> 1525.00]  Okay.
[1525.12 --> 1525.98]  Jared, you're not wrong.
[1526.10 --> 1526.30]  Okay.
[1526.52 --> 1526.72]  Butt.
[1526.92 --> 1527.18]  Okay.
[1527.44 --> 1527.58]  Butt.
[1528.82 --> 1530.16]  Is this a big butt or a little butt?
[1530.40 --> 1533.54]  Well, I'll let you know. You can take a look at my butt and let me know how big it is.
[1533.62 --> 1534.06]  I'll judge.
[1534.22 --> 1534.72]  Okay, go ahead.
[1534.84 --> 1535.68]  Okay, you can judge me.
[1535.68 --> 1543.80]  So that whole notion of gophers don't like frameworks, we don't like magical things. Yes, there is a lot of truth to that.
[1544.42 --> 1547.66]  But that's where my butt comes. Yeah, I just wanted to call it.
[1547.68 --> 1548.50]  Let's hear it. Let's hear it.
[1550.32 --> 1551.12]  You're stalling.
[1551.12 --> 1561.10]  The developer community, the Go developer community, to be specific, has grown by leaps and bounds, right?
[1561.34 --> 1567.32]  Ever since that whole notion of developers don't like framework, Go developers don't like frameworks and things like that, right?
[1567.54 --> 1569.30]  There is a lot of that that is still true.
[1569.50 --> 1573.72]  We still shy away from a ton of dependencies because more than one of us has been bitten by them.
[1574.10 --> 1577.10]  We still shy away from frameworks that do a lot for us.
[1577.70 --> 1580.82]  Buffalo might be kind of in some circles, might be an exception to that, right?
[1580.82 --> 1583.84]  But yes, there is sort of a tendency to shy away from these things.
[1584.04 --> 1587.86]  But again, the Go developer community has grown so much.
[1587.92 --> 1598.70]  There's a lot of people coming from other language communities that want frameworks, that want scaffolding, that want a Rails-like experience, that want something like Encore that does that and then some, right?
[1599.00 --> 1605.04]  So to say that Go developers in general don't like those things, there's some truth to that.
[1605.06 --> 1608.28]  But I think that's becoming less and less sort of a thing.
[1608.76 --> 1610.32]  And frankly, less and less relevant, right?
[1610.32 --> 1614.00]  So it's becoming more of a, what situation am I in, right?
[1614.00 --> 1627.18]  Because to Natalie's point, if you have a team that's using the language, using the technology, and they're finding that there are some shortcomings in certain areas and they're spinning up their own tool to deal with it, they're solving a particular pain point, right?
[1627.18 --> 1631.10]  So we kind of detach ourselves from this notion that Go for a do thing this way.
[1631.20 --> 1636.80]  It's the same argument we've had on the show before around the idioms of Go and the dangers of sort of a groupthink around that, right?
[1636.86 --> 1637.08]  Yeah.
[1637.08 --> 1643.16]  So we kind of have to really start to move away from, you're a go for a developer, you don't do this, this, and that, right?
[1643.20 --> 1645.20]  To more like, okay, what problem do I need to solve?
[1645.42 --> 1648.94]  So I think there is room, right, in the community for something like Encore.
[1648.94 --> 1663.94]  And then for some situations, like it's doing too much because in more established organizations that have operations team, that have architects, that have people that handle different layers of the stack, maybe Encore does too much.
[1664.52 --> 1665.28]  So it's neither or.
[1665.46 --> 1667.82]  Hopefully that answers your question and you've evaluated the size of my butt.
[1667.82 --> 1668.22]  Yes.
[1668.48 --> 1668.70]  Okay.
[1669.00 --> 1670.14]  I'd say it's medium sized.
[1671.22 --> 1672.04]  Yeah, it's a good point.
[1672.20 --> 1682.32]  I mean, I think that's the thing about generalizations and stereotypes is like sometimes they get formed early on and sometimes it's hard to actually ever escape that stereotype, even if it's no longer true or sometimes it was never true.
[1682.50 --> 1683.88]  And I'll give you some of my background.
[1684.02 --> 1688.16]  I mean, I'm coming from Ruby JavaScript and I do a lot of Elixir and I have Ruby roots.
[1688.60 --> 1690.34]  So I, you know, give me all the magic.
[1690.60 --> 1691.42]  I like the magic.
[1691.70 --> 1693.20]  Y'all make fun of method missing a lot.
[1693.52 --> 1695.08]  I think there's lots of cool uses for method missing.
[1695.08 --> 1696.98]  Of course, yes, you can shoot yourself in the foot.
[1696.98 --> 1710.66]  But I had a very productive career with Ruby on Rails and I made websites and applications way faster, way better, and with more productivity than I ever did prior to Rails.
[1711.64 --> 1720.44]  And so I like frameworks, but I'm also coming from somebody who's had a really good experience really growing up on a framework, outgrowing it at a certain point.
[1720.66 --> 1725.00]  But much of my career was with a framework that served me very, very well.
[1725.00 --> 1729.34]  I also, in the JavaScript community, in JavaScript, we don't like frameworks.
[1729.46 --> 1734.24]  We like tiny little micro libraries, like, you know, pull in all the things, NPM, all the things.
[1734.68 --> 1739.62]  I've seen both worlds and I tend to be somewhat just naturally inclined toward the framework.
[1739.78 --> 1746.74]  I see something like Encore and I think this looks really cool, but I'm also small teams, small customer sizes.
[1746.74 --> 1747.74]  I don't have an SRE.
[1748.04 --> 1750.14]  Well, we kind of have an SRE on hire at ChangeLogGearHard.
[1750.76 --> 1753.54]  But I've done a lot of sysadmin stuff myself over the years.
[1753.60 --> 1755.58]  So, like, I'm operating at a very small scale.
[1756.14 --> 1762.96]  And I think at a small team size or a small business, I want all the things as long as they're well done.
[1762.96 --> 1769.68]  But I totally recognize that large organizations don't need all the things Encore does.
[1769.78 --> 1772.00]  And in that case, it's kind of like it could be a blocker.
[1772.36 --> 1773.92]  Like, well, we need to swap this thing in.
[1773.98 --> 1774.98]  Well, you can't swap it in.
[1775.08 --> 1777.12]  Okay, we can't use a framework.
[1778.06 --> 1778.82]  Yep, those opinions.
[1779.02 --> 1783.24]  And Andre, this is where I sort of ask you to sort of provide some feedback, right,
[1783.24 --> 1789.88]  or some interpretation of the different reasons you've heard here around the whole idea of liking, not liking framework and whatnot.
[1789.88 --> 1792.64]  And also, I want you to sort of think about how to answer the question.
[1793.50 --> 1795.46]  I've sort of been playing devil's advocate during this whole thing.
[1795.80 --> 1801.48]  So I want you to answer the question of basically, who is Encore for?
[1803.10 --> 1804.90]  That's a different question than I expected.
[1805.90 --> 1809.66]  I was going to answer, or I was going to give my opinion on framework.
[1809.94 --> 1811.00]  Oh, do that and then answer.
[1811.12 --> 1811.68]  Go ahead.
[1811.90 --> 1812.02]  Yeah.
[1812.58 --> 1812.78]  Okay.
[1812.78 --> 1825.60]  Well, I actually think that the main thing that Go developers find with frameworks that really rubs them the wrong way is this magic notion, like method missing.
[1826.82 --> 1837.66]  And for those who don't know, that's a Ruby thing where if, correct me if I'm wrong, if a class doesn't have a method, it calls this method instead.
[1837.82 --> 1841.34]  So you can do a lot of like meta programming magic things with it.
[1841.34 --> 1842.26]  That's correct.
[1842.60 --> 1849.68]  And when it comes to Go, a lot of people, myself included, really like with the language is its predictability.
[1850.00 --> 1854.98]  Like we understand when we read something exactly how it works.
[1854.98 --> 1864.74]  And I'd like to think that Encore sticks to that principle and doesn't introduce a lot of magic.
[1865.40 --> 1873.46]  And I believe that at no point when you're writing code with Encore are you confused about what's happening.
[1873.46 --> 1877.58]  And it's all actually very, very straightforward.
[1877.58 --> 1886.08]  And the type of things that we do are considered magical by many.
[1886.08 --> 1899.42]  But I would say that it's more similar to the Go runtime in that sense, where the Go runtime does a lot of things that are very magical compared to what you do as a Go developer.
[1899.42 --> 1909.94]  And similarly, Encore does a lot of things under the hood, but it doesn't change like the predictability of how you're writing code.
[1910.34 --> 1919.12]  And I think that's the critical part that we really need to preserve in Go, whether it's Encore or another framework or library or whatever.
[1919.12 --> 1923.56]  Yeah, I don't think you need to have Encore, I guess, as an example of that.
[1923.66 --> 1926.40]  Magic and framework are not eternal companions.
[1926.72 --> 1934.26]  It's just that one of the most popular web frameworks in human history is Ruby on Rails, which is filled with a lot of magic things.
[1934.70 --> 1937.18]  Just instance variables appear out of nowhere on you.
[1937.42 --> 1941.00]  If you just dream up a method, it's probably there.
[1941.08 --> 1941.72]  Those kind of things.
[1942.16 --> 1943.56]  But there's lots of frameworks that aren't that way.
[1943.56 --> 1947.28]  I mean, in the Python community, they also appreciate explicit over implicit.
[1947.28 --> 1950.94]  And there's frameworks over there that provide explicit calls.
[1951.20 --> 1954.58]  And you can accomplish these things with code gen, with scaffolding, in a lot of the ways.
[1955.22 --> 1960.44]  But again, going back to the persistence of stereotypes, I think a lot of people think framework and they think magic.
[1961.12 --> 1967.30]  And maybe if they don't immediately understand how something works, they think, oh, this must be some tomfoolery going on.
[1967.46 --> 1968.42]  Not always the case.
[1968.42 --> 1975.64]  It's also what's interesting about this specific framework is that it's not only about the code part, right?
[1975.72 --> 1977.20]  It's about deploying things.
[1977.28 --> 1977.96]  Right.
[1978.50 --> 1986.74]  Which is kind of giving complementary part there, which is important to have in mind when you talk about frameworks and magic and so on.
[1986.92 --> 1995.06]  Like it does, leaving this to your SRE colleague or to your release engineer colleague or whoever does deploy stuff is another type of magic.
[1995.32 --> 1996.60]  You also don't understand that.
[1996.66 --> 1998.08]  You just hand this over to somebody else.
[1998.08 --> 1999.30]  That's true.
[1999.30 --> 2010.38]  I must say, when I first look at this framework, I was scratching my head and asking, why would somebody couple that many concerns into one tool?
[2010.38 --> 2013.06]  I'm starting to get that, right?
[2013.06 --> 2014.30]  Based on the conversation we're having.
[2014.70 --> 2017.40]  Thank you for opening my eyes to new possibilities.
[2018.02 --> 2020.64]  To me, I'm used to the most magical.
[2021.02 --> 2026.38]  The most magic I want in any sort of deployment, production ready, sort of push it and it goes kind of thing.
[2026.38 --> 2030.54]  I know I'm biased in saying this, but I've been doing this since before I joined Heroku.
[2030.94 --> 2033.74]  But Heroku is to me is that magical thing, right?
[2033.76 --> 2037.24]  Where I just push my GitHub repository or something like that, right?
[2037.56 --> 2043.56]  And my app is up there and I don't need to know how it got there, what they use under the hood, slugs, build packs, containers.
[2043.56 --> 2044.54]  I don't care, right?
[2044.56 --> 2045.80]  It's just like, it gives me an endpoint.
[2046.22 --> 2046.50]  Great.
[2046.60 --> 2047.92]  I can't even map a domain to that.
[2048.12 --> 2048.42]  Great.
[2048.56 --> 2051.62]  You know, that's the most magic I've ever wanted, right?
[2051.78 --> 2051.92]  Yeah.
[2052.00 --> 2059.82]  So now here comes a tool like this, which is not only helping me be a sort of a developer time productive, right?
[2059.82 --> 2064.64]  Helping with that developer time productivity, but it's going all the way out to deploy time.
[2064.98 --> 2067.94]  So to me, I'm like, okay, this is innovation.
[2068.40 --> 2068.78]  Yes.
[2069.00 --> 2070.72]  But am I ready, right?
[2070.72 --> 2076.14]  As somebody who wants to fiddle with the bits, am I ready to sort of hand over that much control, right?
[2076.16 --> 2080.70]  It's the same dilemma you have every time you choose a piece of technology from a cloud provider, right?
[2081.28 --> 2086.50]  Yes, they might offer a raw tool, the raw sort of deploy this thing on an EC2 instance and you're good to go.
[2086.50 --> 2088.20]  Or you get the managed thing.
[2088.30 --> 2090.68]  You pay a little more, but you get the managed service and it's hands off, right?
[2090.80 --> 2096.22]  So the more control you want, the more you have to sort of shy away from the managed thing.
[2096.30 --> 2100.36]  So to me, this felt like magic, like far edge, right?
[2100.36 --> 2106.36]  And Andre, that's something you are deliberate about, making this as automated as possible.
[2106.64 --> 2107.18]  Who hurt you?
[2107.24 --> 2108.32]  What drove you to that extreme?
[2108.42 --> 2109.22]  Who hurt you?
[2111.54 --> 2112.72]  I love that question.
[2113.06 --> 2116.48]  Actually, that's not really why we're doing it.
[2116.48 --> 2122.46]  And we're actively working on opening up more control in that sense.
[2122.46 --> 2129.48]  The goal with it really, it's not about taking control of everything.
[2129.90 --> 2134.76]  Because I know, like I've done lots and lots of backend development for many years.
[2134.76 --> 2138.86]  And I know that there are many situations where you need more flexibility.
[2138.86 --> 2143.22]  I think the reason we're doing it is because most of the time you don't.
[2143.98 --> 2154.00]  And doing what's sensible is like, it's the right thing, like 90% of the time or 80% of the time.
[2154.74 --> 2159.86]  And we would like to add additional flexibility to support the remaining 20%.
[2159.86 --> 2176.36]  The reason why we started on the very extreme is because we believe that by connecting the whole end-to-end developer process from how you write code in your editor,
[2176.36 --> 2187.56]  which is where the Encore experience starts, if you will, all the way into how you're collaborating with other developers, all the way out to production,
[2188.04 --> 2201.20]  is that by having visibility into where things are running, we can actually help you provide a better experience when you're writing code.
[2201.20 --> 2208.74]  So for example, there are a lot of things when you're writing code, like in my experience, I was at Spotify for many years.
[2209.40 --> 2216.06]  And all the time when you're writing code, you do that with an understanding how things work in production.
[2216.52 --> 2225.02]  So for example, when you're querying a database, you do it with an understanding of the shape of the data in production,
[2225.20 --> 2227.36]  or the shape of your database schema.
[2227.36 --> 2234.10]  When you're deleting an endpoint, you do that because you're sure that it's actually not being called.
[2234.58 --> 2236.26]  Otherwise, you're going to have a bad time.
[2237.30 --> 2241.76]  And when you're checking, like, is this field set?
[2242.34 --> 2248.34]  You do that because you understand that sometimes in production, it's not being set.
[2248.34 --> 2259.52]  And so by actually being part of this whole experience, we want to take some of that insights in production and feed it back into the developer experience.
[2259.80 --> 2267.30]  So that when you're doing a database query, we should be able to give you feedback from the database schema in production.
[2267.62 --> 2269.46]  Like, oh, this is not the right type.
[2269.46 --> 2276.22]  You're querying, you're trying to put a string field into an integer variable or whatever.
[2277.00 --> 2290.26]  And personally sensitive data permitting, it would also be very useful to be able to show you a sample from your database as you're doing, like, database queries in your editor.
[2290.40 --> 2294.86]  Or being able to say, like, hey, did you know that this endpoint is not being called in production?
[2294.86 --> 2297.12]  It last happened three weeks ago.
[2297.48 --> 2298.94]  Maybe you should just delete it right away.
[2299.10 --> 2311.80]  Or when you're making an API, like a change to your API schema to be able to give you feedback, like, hey, your coworker is also working on this endpoint and you're about to collide with each other.
[2311.90 --> 2317.38]  Maybe you should talk right now instead of doing it two days later in a pull request.
[2317.62 --> 2320.76]  Or if you miss it, it's going to break in production, right?
[2320.76 --> 2328.24]  So it's all about using this visibility to feed back into the developer process and reduce the feedback loop.
[2328.42 --> 2329.92]  That's the idea behind all of this.
[2330.20 --> 2334.54]  So it's not about assuming control, even though that's where we started.
[2334.66 --> 2336.12]  We'll gradually pull that back.
[2336.70 --> 2339.58]  It sounds like there is a lot of project-specific content.
[2339.94 --> 2341.44]  And that makes me wonder.
[2341.74 --> 2348.72]  You probably need somebody who is very well familiar with a project that you're working on to set it up initially, right?
[2348.72 --> 2355.96]  But turning to you, the question that Johnny turned to me, would you give a junior person access to this?
[2356.74 --> 2371.62]  And I will focus my question with saying that this can be, given that you can control the amount of exposure to automation versus manual work, sounds like this can be an interesting way of slow onboarding on a platform.
[2372.30 --> 2374.20]  Is this something that you also have in mind?
[2374.20 --> 2383.70]  I actually think for a very long time, I actually struggled with how to communicate it just because the process of using it, it's almost like there's nothing there.
[2384.06 --> 2391.78]  Actually, writing an Encore application ends up being, you're not actually doing much Encore specifics.
[2392.44 --> 2395.32]  You're writing, to define an API, for example.
[2395.32 --> 2399.80]  You are writing a regular Go function at the package level.
[2400.92 --> 2405.26]  And the input to that function is a context, which is Go.
[2405.54 --> 2406.80]  It's a very standard idiom.
[2406.94 --> 2412.12]  As well as a type, which becomes your input to your API.
[2412.34 --> 2416.32]  And the return value is a data structure and an error.
[2416.84 --> 2419.46]  And that becomes your response schema.
[2419.46 --> 2426.36]  That's basically all you need to know to use Encore to write a backend.
[2426.68 --> 2435.14]  And then to make an API call between two backend services, you just import the other service as a Go package.
[2435.42 --> 2439.40]  And then you call the function as if it was a regular function.
[2439.40 --> 2443.82]  When we actually run your application, then we find all of this.
[2444.34 --> 2452.10]  We have a compilation step that finds all of these places and generates the code to replace that with a real API call.
[2452.42 --> 2458.24]  But from a user perspective, it just feels like you're writing regular Go code.
[2459.04 --> 2461.50]  And then we use static analysis.
[2461.84 --> 2463.12]  We figure all of this stuff out.
[2463.12 --> 2467.84]  And then we can do a bunch of stuff like generate API documentation automatically.
[2468.26 --> 2474.74]  Or take all of your API and generate a front-end client for it in different languages and so on.
[2475.14 --> 2481.92]  So there's a very big difference in terms of what do you need to know to write applications with Encore?
[2482.42 --> 2483.60]  And the answer is very little.
[2483.96 --> 2486.40]  And then in terms of what value do I get out of it?
[2487.26 --> 2489.24]  Then there's a variety of things.
[2489.24 --> 2496.08]  But you can very much, as you pointed out, you can very much discover those gradually.
[2496.68 --> 2499.04]  You don't have to learn a bunch of things up front.
[2499.42 --> 2499.98]  That's the idea.
[2500.38 --> 2506.78]  So I'd like to think that it's very, very easy to get started with it, even if you don't know a lot.
[2506.92 --> 2513.40]  And I would even go as far as to say that backend development in general has an incredibly high learning curve.
[2513.40 --> 2520.58]  And so that's another big area that I'm passionate about is how can we actually make that easier for new people to come into?
[2520.86 --> 2526.64]  Because normally you have to learn hundreds of concepts just so you don't break something in production.
[2527.38 --> 2528.88]  And that's incredibly scary.
[2529.20 --> 2535.66]  I remember when I started doing this and the first time I pushed something to production, I was just sitting there almost having a panic attack.
[2535.66 --> 2536.60]  I like that.
[2536.74 --> 2539.18]  All you need to do is import it and call it from another function.
[2539.66 --> 2541.46]  There's no setup and teardown.
[2541.64 --> 2543.78]  There's no how do I hit this API, et cetera.
[2544.32 --> 2550.26]  It seems like that's kind of a microservices thing or backends talking to backends.
[2551.06 --> 2556.02]  Is this the kind of tool that you would mostly use to build backends to be consumed by other backends?
[2556.14 --> 2559.88]  Or would you build Twitter's API with this or Stripe's API?
[2559.88 --> 2565.02]  Or are we talking like smaller, non-public, non-consumer facing backends?
[2565.16 --> 2567.76]  Like would it be a front-end client for this or not?
[2568.46 --> 2570.80]  Yeah, so it's firmly in the backend camp.
[2571.38 --> 2574.92]  So a lot of people get it confused and think that it's a web framework.
[2575.10 --> 2575.88]  And it's really not.
[2576.02 --> 2578.70]  Like if you want to serve HTML, don't use Encore.
[2579.24 --> 2585.88]  It's for APIs that communicate data structures and implement business logic.
[2585.88 --> 2588.20]  So that's where we're aiming.
[2588.68 --> 2595.50]  And doing things like Twitter's API or Stripe, that's very much in the type of things we're targeting.
[2595.78 --> 2596.74]  What about Soap?
[2597.06 --> 2597.94]  Do you support Soap?
[2601.64 --> 2602.32]  Sorry.
[2602.32 --> 2604.32]  Sorry to break it to you.
[2605.00 --> 2605.72]  I'm out.
[2607.14 --> 2608.04]  You lost me.
[2608.04 --> 2617.82]  No, right now, in practice, when you expose a public API, it's only HTTP and JSON.
[2619.12 --> 2627.02]  But again, it's very much about not, I think as developers, that's not something I ever want to spend time on.
[2627.02 --> 2633.94]  I would rather think about my API in terms of data structures and semantics that I want to express.
[2634.62 --> 2639.60]  And then the idea is Encore can expose it in different ways, right?
[2639.68 --> 2643.18]  Whether it's HTTP or JSON, GRPC and Protobuf.
[2643.40 --> 2646.62]  We should be able to expose it in different ways depending on what you need.
[2646.68 --> 2652.56]  Because it's pretty low abstraction level to be dealing with transport protocols in a lot of cases.
[2657.02 --> 2662.30]  This episode is brought to you by our friends at O'Reilly.
[2662.66 --> 2668.78]  Many of you know O'Reilly for their animal tech books and their conferences, but you may not know they have an online learning platform as well.
[2669.14 --> 2673.58]  The platform has all their books, all their videos, and all their conference talks.
[2673.58 --> 2684.72]  Plus, you can learn by doing with live online training courses and virtual conferences, certification practice exams, and interactive sandboxes and scenarios to practice coding alongside what you're learning.
[2684.72 --> 2698.66]  They cover a ton of technology topics, machine learning, AI, programming languages, DevOps, data science, cloud, containers, security, and even soft skills like business management and presentation skills.
[2698.80 --> 2700.56]  You name it, it is all in there.
[2700.88 --> 2706.04]  If you need to keep your team or yourself up to speed on their tech skills, then check out O'Reilly's online learning platform.
[2706.58 --> 2710.14]  Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[2710.26 --> 2712.50]  Again, O'Reilly.com slash changelog.
[2714.72 --> 2729.98]  Three and a half years.
[2730.54 --> 2731.86]  That's how long you've been working on this.
[2732.04 --> 2732.16]  Yep.
[2732.42 --> 2733.44]  Biggest lesson learned.
[2733.72 --> 2740.18]  I really have learned to appreciate the Go backwards compatibility guarantee.
[2740.94 --> 2742.38]  I bet you have.
[2742.38 --> 2753.04]  Well, maybe a different sense than you expected in the sense that it's really, really hard to provide such a guarantee.
[2754.22 --> 2758.82]  And for Encore, we provide a way of writing applications.
[2759.48 --> 2765.62]  I've experienced working in companies where we've had an infrastructure organization that have built internal tools.
[2765.62 --> 2774.40]  And we had to do migrations from one library or one internal tool to another, like every quarter.
[2774.66 --> 2777.52]  And that was incredibly demotivating and incredibly frustrating.
[2777.52 --> 2788.52]  So I've spent so much time thinking about what's the right API for doing things so that you actually can commit to being backwards compatible.
[2789.10 --> 2800.64]  And it just made me respect the Go team and everything they put into the amount of care they put into designing a language and a standard library that is so stable over time.
[2800.64 --> 2807.54]  So someone who uses something like Encore is, one, benefiting from that sort of philosophy.
[2808.18 --> 2813.60]  But is it fair to say that you've sort of incorporated that into the APIs that you're exposing from Encore?
[2813.60 --> 2814.52]  Yeah, absolutely.
[2814.94 --> 2819.66]  I mean, time will tell if there's an incredibly serious issue that needs to be addressed.
[2820.00 --> 2825.98]  I guess the Go team reserves the right to do that in extreme circumstances around security.
[2826.16 --> 2827.60]  But I take it incredibly seriously.
[2828.42 --> 2832.04]  And I've been on the other side of the fence.
[2832.18 --> 2837.54]  And it's just incredibly demotivating that you have plans and you're always busy.
[2837.72 --> 2841.14]  And then somebody comes and tells you like, hey, here's a bunch of work you have to do.
[2841.32 --> 2841.76]  It's awful.
[2841.76 --> 2846.04]  So, yeah, we absolutely want it to be backwards compatible.
[2846.88 --> 2851.28]  And that's a big reason why it's taken so long to get here.
[2851.28 --> 2858.20]  It's just because we're incredibly careful about how we design things to actually enable that.
[2858.68 --> 2861.94]  So Encore is open source and you do have contributors.
[2862.30 --> 2865.66]  Yeah, we open sourced it about two weeks ago.
[2865.78 --> 2867.26]  So it's very, very fresh.
[2867.76 --> 2869.04]  It's all open source.
[2869.04 --> 2873.34]  All the runtime stuff, all the tracing, all the parsing, it's all there.
[2873.34 --> 2876.72]  Was that the plan from the get-go or is that a pivot?
[2876.96 --> 2878.54]  No, it was entirely the plan.
[2878.78 --> 2883.68]  I don't believe, as a developer, you might not realize it when you just import a package.
[2883.68 --> 2890.84]  But we're all building on mountains and mountains of open source from the first line of code we're writing.
[2890.84 --> 2896.82]  And I think not contributing back to that is, I wouldn't say, a mistake.
[2896.96 --> 2898.20]  Like every product is different.
[2898.20 --> 2905.50]  But to me, like being able to contribute back and being able to open source this is incredibly important to me.
[2906.34 --> 2913.16]  And just for developers to have a look at something, even if it's not for you, it's at least different.
[2913.66 --> 2917.70]  And being able to have a look and see how it works under the hood, I think that's super important.
[2917.70 --> 2924.68]  And over the years, I've learned so much from just opening up projects that I like and learning from that.
[2924.80 --> 2926.02]  Like, oh, how did they do this?
[2926.16 --> 2926.30]  Okay.
[2926.40 --> 2930.40]  And then you dig into that and suddenly you've learned something new, right?
[2930.70 --> 2934.20]  So you liked all the open source tools that you had.
[2934.26 --> 2937.60]  And that's why you felt that you want to give back and kind of open source your tool.
[2937.60 --> 2943.10]  Yeah, and I think we talk a lot about developer productivity and how Encore makes it so much better.
[2943.34 --> 2953.54]  But it's also important to remember like how far we've come, both on the coding side and the editors and the languages and the libraries we have.
[2953.86 --> 2954.90]  That's all because of open source.
[2955.24 --> 2961.04]  And then I think a big part of modern productivity for backend development is also due to the cloud.
[2961.54 --> 2962.54]  Thank you, Heroku.
[2962.54 --> 2969.06]  And maybe the story there is not quite as good in terms of open source, but hopefully we'll get there.
[2969.40 --> 2971.52]  Andra, how can the Go community help Encore?
[2971.72 --> 2972.74]  Well, that's a great question.
[2972.84 --> 2973.18]  Thank you.
[2973.74 --> 2974.38]  Thank you.
[2975.30 --> 2984.76]  I'd like to think that, like we talked about this and I talked with a lot of people about, and a lot of people bring this up about frameworks are not the Go way.
[2985.22 --> 2987.48]  And Encore is certainly not for everybody.
[2987.48 --> 2992.26]  I think it very much comes down to your requirements on your product.
[2992.44 --> 2993.84]  Like what is it that you're building?
[2994.40 --> 2999.24]  And do you actually benefit from something taking care of all of these things?
[2999.40 --> 3005.14]  Or does it actually take away too much and it hinders your ability to innovate on your product?
[3005.38 --> 3010.38]  And if it is the right thing for you, then I would love your feedback.
[3010.38 --> 3014.52]  And if it isn't, I would love to hear why not?
[3014.92 --> 3019.66]  And what is it about it that rubs you the wrong way or whatever?
[3020.02 --> 3026.02]  I know it's very, very early days and the things we support right now are limited and so on.
[3026.02 --> 3039.20]  But I very much believe that we can create a much, much better developer experience by eliminating these silos of these different layers that we talked about earlier.
[3039.20 --> 3056.26]  By actually creating an experience that is with you from the first line of code you write into how you're collaborating with other people, into testing and reviewing code and all the way out into production and beyond.
[3056.26 --> 3062.76]  I think it's just, there's so much potential there in terms of creating a really, really good experience.
[3063.30 --> 3073.16]  And anything that like any feedback and any contribution for that matter, if you want to, if you find an issue and you want to fix it or you want to add something, super appreciated.
[3073.50 --> 3075.64]  How do you give feedback on open source projects?
[3075.82 --> 3078.70]  Like you open an issue and say, I don't like this.
[3079.16 --> 3079.96]  Is this how you do this?
[3080.30 --> 3082.28]  There are plenty of examples of that you can look at.
[3082.92 --> 3084.28]  It doesn't work on my machine.
[3084.28 --> 3087.66]  Yeah, that usually goes over well.
[3090.08 --> 3092.12]  Let me tell you the 10 reasons why this is terrible.
[3092.50 --> 3092.72]  One.
[3093.82 --> 3095.70]  Well, at least this is detailed, you know.
[3098.54 --> 3102.86]  Another thing you can do is just open a pull request that deletes the whole project.
[3104.74 --> 3106.30]  That's a serious statement, yeah.
[3106.52 --> 3107.28]  Not unprecedented.
[3107.80 --> 3108.24]  It's happened.
[3109.34 --> 3111.20]  Maybe not on Encore, but it definitely happened.
[3112.86 --> 3113.26]  Awesome.
[3113.26 --> 3115.90]  I think when you do it, it's mindful to be respectful.
[3116.18 --> 3116.68]  Oh, absolutely.
[3116.88 --> 3122.18]  Even if you have to understand where the author is coming from and be respectful of their time.
[3122.80 --> 3125.46]  And maybe they don't share your perspective.
[3126.12 --> 3127.22]  And perhaps no free consulting.
[3127.76 --> 3129.04]  Here's how you should do this.
[3129.52 --> 3134.02]  So I will admit, when I first looked at Encore, I was in a this does too much camp.
[3134.02 --> 3139.76]  I am interested in exploring it a little bit more before I have my final judgment of it.
[3139.98 --> 3146.26]  I am curious, before we start to wrap this up, I am curious if Encore is sort of an all or nothing kind of framework.
[3146.50 --> 3150.02]  Can I have parts of it if I don't like the deployment mechanism?
[3150.12 --> 3151.50]  If I already have a deployment mechanism?
[3151.76 --> 3154.00]  Can I use some of it and not others?
[3154.08 --> 3154.88]  Or is it all or nothing?
[3154.88 --> 3155.48]  Yeah.
[3155.48 --> 3159.02]  So today, the deployment side is pretty all or nothing.
[3159.38 --> 3161.96]  That's the biggest thing that people have asked about.
[3162.52 --> 3171.88]  And it's something that we very much want to open up more just because you should be able to use it in whatever way makes the most sense for you.
[3171.88 --> 3172.36]  Okay.
[3173.10 --> 3173.42]  Okay.
[3173.74 --> 3174.16]  All right.
[3174.50 --> 3177.18]  Yeah, like I said, I'm going to withhold judgment.
[3177.62 --> 3178.36]  I need more data.
[3178.68 --> 3179.16]  More data.
[3179.36 --> 3183.62]  Well, you haven't converted them, but you've got them from hater to like tentatively interested.
[3183.86 --> 3184.90]  So that's a win, Albright.
[3184.96 --> 3185.38]  That's a win.
[3185.98 --> 3187.06]  Yeah, that's it.
[3187.20 --> 3189.58]  You know, I have to give it its due.
[3189.82 --> 3190.22]  Exactly.
[3190.36 --> 3190.70]  Exactly.
[3191.12 --> 3192.46]  So guess what time it is?
[3192.48 --> 3192.80]  Uh-oh.
[3192.80 --> 3194.88]  It's unpopular opinion time.
[3201.88 --> 3215.80]  So who's got some unpop?
[3216.06 --> 3216.74]  I can start.
[3217.10 --> 3222.68]  The question, Johnny, that you asked me if I think this is a good fit for juniors or not was supposed to be my unpopular opinion.
[3222.68 --> 3223.08]  Oh.
[3223.52 --> 3224.44]  No wonder she dodged it.
[3225.00 --> 3226.76]  And yes, I dodged it.
[3226.80 --> 3231.46]  And then when I heard Andres answer, I even backed out of it.
[3231.88 --> 3232.30]  Okay.
[3232.50 --> 3232.78]  Ooh.
[3233.00 --> 3235.04]  I got completely lost throughout this episode.
[3235.48 --> 3240.30]  So I will offer an unrelated, unpopular opinion.
[3240.96 --> 3245.90]  Conferences in online days should have live as a default.
[3247.10 --> 3248.80]  Versus prerecorded sessions.
[3249.00 --> 3249.60]  Why?
[3250.32 --> 3252.88]  And I'm willing to take as a compromise over both.
[3252.96 --> 3253.46]  Oh, right.
[3253.98 --> 3255.70]  I hear that this is indeed unpopular.
[3255.94 --> 3256.16]  Nice.
[3256.60 --> 3257.08]  Why?
[3257.08 --> 3257.52]  Hmm.
[3258.42 --> 3261.98]  Having done both this past one and a half years.
[3262.18 --> 3265.26]  One is the live way is more natural.
[3265.40 --> 3266.80]  I enjoy having small hiccups.
[3267.32 --> 3270.50]  Also because it feels more natural, but also because it's less time consuming.
[3270.66 --> 3273.78]  Because when it's prerecorded, you have no good reason to have small hiccups.
[3274.08 --> 3278.24]  You get to be a little bit more creative with the one and a half people who actually turn on their video.
[3278.24 --> 3289.42]  If there is such type of a feedback in a conference or from the responses and so on, it's not the same energies as in a live event, in-person event, but it's closer to that than completely prerecorded.
[3289.76 --> 3290.20]  Wow.
[3291.22 --> 3292.74]  I don't know what to think.
[3294.10 --> 3296.78]  That I managed to finally get an unpopular opinion.
[3297.04 --> 3297.96]  You should be happy for me.
[3298.88 --> 3300.28]  I'm actually with you, Natalie.
[3300.44 --> 3300.80]  Oh, no.
[3300.92 --> 3301.42]  I'm with you.
[3301.48 --> 3302.32]  Not even a hybrid?
[3302.76 --> 3304.82]  Like maybe like prerecorded talk?
[3304.90 --> 3305.74]  Default, she said.
[3306.00 --> 3308.06]  And, you know, live Q&A or something?
[3308.24 --> 3310.84]  I'm willing to take the compromise of each speaker chooses.
[3311.18 --> 3311.44]  Okay.
[3311.74 --> 3316.94]  Isn't it kind of weird that your talk is going on and you're hanging out in the chat talking to people while your talk is going on?
[3316.96 --> 3318.48]  It just feels kind of like out of body.
[3318.96 --> 3320.36]  No, you can't wait until the end.
[3320.48 --> 3321.22]  Yeah, you can wait.
[3321.52 --> 3322.28]  It's not to be weird.
[3323.88 --> 3325.90]  I really like it as a speaker, too.
[3325.98 --> 3330.40]  It feels just like you want those butterflies in your stomach.
[3330.92 --> 3333.42]  And when you're prerecorded, there's nothing on the line.
[3333.64 --> 3337.28]  You're just like, if something goes wrong, let's just do it again.
[3337.28 --> 3338.42]  And again.
[3338.42 --> 3343.62]  So Chris Hiller, who's a co-host of mine on JS Party, was talking about this.
[3343.76 --> 3344.48]  And he's with Natalie.
[3344.64 --> 3345.08]  And I agree.
[3345.26 --> 3346.40]  He convinced me.
[3346.78 --> 3357.00]  Because as a conference speaker, there's a completely different set of skills and things you have to do versus somebody who's recording a quote-unquote professional video.
[3357.28 --> 3359.12]  Like he doesn't have the setup for video.
[3359.42 --> 3361.12]  He doesn't have like the recording tools.
[3361.12 --> 3364.72]  He had to learn a lot of stuff to prerecord a nice talk.
[3364.98 --> 3367.78]  But he's very good at putting a slide deck together and showing up and talking.
[3368.18 --> 3370.00]  That's like a different skill set that you're asking people.
[3370.10 --> 3373.26]  So he didn't appreciate prerecorded for that reason, which I had never thought about.
[3373.88 --> 3373.94]  Yeah.
[3374.16 --> 3374.58]  I don't know.
[3374.62 --> 3375.78]  I don't know how I feel about this one.
[3376.12 --> 3376.18]  Okay.
[3376.88 --> 3377.84]  We'll put a poll out there.
[3377.92 --> 3379.16]  We'll see what the people say.
[3380.80 --> 3381.58]  Oh, my goodness.
[3381.72 --> 3381.84]  Okay.
[3381.96 --> 3384.98]  Well, Natalie, you stumped me for sure.
[3385.24 --> 3385.62]  I'm sorry.
[3385.92 --> 3386.76]  Here's the thing, though, right?
[3386.92 --> 3387.08]  Yeah.
[3387.16 --> 3388.78]  We'll get to the other unpopular opinions.
[3388.88 --> 3390.92]  But I have to opine on your opinion.
[3391.46 --> 3394.12]  So giving folks a choice, that's awesome.
[3394.38 --> 3396.64]  I think that's sort of the happy medium there.
[3397.02 --> 3397.82]  I've done both.
[3398.04 --> 3408.26]  And I will say one of the things that, and perhaps others will sort of agree with me here, is that because when I have a prerecorded deliverable that I have to give,
[3408.26 --> 3415.98]  I spend a lot more time in preparation and editing and sound fixing.
[3416.98 --> 3419.74]  Because then it's like, okay, this is a video production.
[3420.38 --> 3422.12]  I have to spend the time.
[3422.40 --> 3424.08]  And I don't have the time half the time.
[3424.52 --> 3424.70]  Yeah.
[3424.70 --> 3436.04]  So it's like the level of effort is much higher for prerecorded than it is if I just show up and in the middle of talk, if I'm ums and ums and all these sort of human quirks.
[3436.24 --> 3438.86]  And I'd be okay if somebody said, you know what, you have to do it live.
[3439.10 --> 3440.92]  That way I don't have to agonize about it.
[3440.98 --> 3446.66]  I can just worry about the content rather than worry about the content and the editing that I have to do after I record it.
[3446.68 --> 3446.84]  Right.
[3446.90 --> 3448.72]  So I can definitely see the value in that.
[3448.72 --> 3459.70]  But I think giving folks a choice and maybe a hybrid model where they give the talk and maybe they do live Q&A or rather the prerecorded talk and in the live Q&A afterwards would be also a nice choice to have.
[3460.66 --> 3461.16]  But yeah, man.
[3461.24 --> 3463.48]  Or live talk and prerecorded Q&A.
[3466.84 --> 3467.90]  We found it.
[3468.06 --> 3468.36]  There you go.
[3468.64 --> 3469.00]  Perfect formula.
[3470.60 --> 3475.76]  The only issue with this idea is that some people have internet that is not good enough.
[3476.00 --> 3476.52]  True.
[3476.52 --> 3476.60]  True.
[3477.04 --> 3480.26]  This is, it will not always work, unfortunately.
[3480.62 --> 3481.38]  So many factors.
[3481.70 --> 3482.08]  That's true.
[3482.32 --> 3482.72]  That's true.
[3482.94 --> 3483.80]  All right, Andre, what you got?
[3483.94 --> 3484.66]  So I'm going to pivot.
[3485.28 --> 3488.98]  We never talked about testing, but I have opinions on testing.
[3489.68 --> 3493.20]  I think the testing pyramid is the wrong way up.
[3493.20 --> 3501.92]  I think we should spend as much energy as possible writing system and integration tests and as little as time as possible on unit tests.
[3502.12 --> 3503.66]  Oh, that's going to be a tough one.
[3503.66 --> 3507.84]  Describe to me the testing pyramid because I don't recall the exact order of things.
[3507.92 --> 3510.34]  I remember the food pyramid, but that one was off too, I think.
[3510.62 --> 3511.10]  Exactly.
[3513.12 --> 3514.44]  All pyramids are wrong.
[3516.36 --> 3517.86]  I'm coming out against pyramids.
[3517.86 --> 3523.94]  That's an even bigger take.
[3524.08 --> 3525.02]  Yeah, that's a real risky.
[3525.02 --> 3535.28]  So the testing pyramid is essentially saying that write the most unit tests, write fewer integration tests and the fewest system tests.
[3536.48 --> 3542.22]  And I guess the nuance for me is that, of course, like everything, it depends on what you're doing.
[3542.22 --> 3554.64]  But in my experience, when it comes to backend development and application development, the unit tests ends up being very, very brittle because they test inner workings of your application.
[3554.64 --> 3562.38]  And the things that you're actually trying to keep stable are the interfaces to your users and between parts of the system.
[3562.76 --> 3574.04]  So when you actually test those and you test the behavior of your boundaries, that is when you can actually reason about correctness that matches your users.
[3574.04 --> 3580.16]  And of course, if you're writing a mathematical function or a pure function, then those are the same.
[3580.42 --> 3585.86]  And unit tests make sense because you define correctness in terms of inputs and outputs to that function.
[3586.00 --> 3592.42]  But when you're creating a system, you reason about correctness in terms of the work that that system is performing.
[3592.90 --> 3600.00]  And by writing tests at that level, you end up with tests that they don't break every time you refactor something.
[3600.00 --> 3612.88]  And if you do refactor something and you do it correctly, those tests will just keep on passing in the same way that if you refactor the internals of a mathematical function, the unit tests will keep passing.
[3613.46 --> 3617.74]  So if you're supposed to write few unit tests, what would be an example of a unit test worth writing?
[3618.10 --> 3620.54]  So I think everything you do is different.
[3620.54 --> 3629.36]  But generally, unit tests are great when you're dealing with a function that has a well-defined contract in terms of inputs and outputs.
[3630.00 --> 3639.16]  And I think especially when that function is something that is important to your application in some sense, if it's implementing a core part of your business logic.
[3639.16 --> 3648.16]  There was a company that were building a platform for or an API really for when you're packaging e-commerce orders.
[3648.72 --> 3651.98]  It calculated what's the optimal packing?
[3652.54 --> 3656.36]  How do you pack a box as efficiently as possible?
[3656.54 --> 3659.96]  What's the smallest box that will fit all the stuff that you ordered?
[3660.20 --> 3665.70]  And that's a mathematical problem that is essentially the foundation of their whole business.
[3666.14 --> 3668.04]  And you can probably unit test that.
[3668.32 --> 3672.66]  So in a very extreme case, they can unit test their whole business.
[3673.00 --> 3678.00]  But most of the time, your product is not expressed in terms of a mathematical function.
[3678.34 --> 3679.98]  And then you should be testing at a higher level.
[3680.28 --> 3680.32]  Right.
[3680.44 --> 3681.10]  I can see it.
[3681.20 --> 3681.72]  I'm not going to disagree.
[3681.94 --> 3682.06]  Yeah.
[3682.06 --> 3686.58]  I mean, if you're already convinced, I'm not going to have a shot at it being very unpopular.
[3687.12 --> 3687.24]  Am I?
[3687.90 --> 3688.92]  Just explain it too well.
[3688.98 --> 3691.68]  No, it depends on how Jared sort of phrases it.
[3691.76 --> 3694.08]  So sometimes he makes it a little clickbaity.
[3694.08 --> 3699.26]  Sometimes I misrepresent what you said on accident because I couldn't quite draw it out.
[3699.50 --> 3700.80]  Here's how you do your unpopular opinions.
[3700.88 --> 3703.80]  If you want the best results is you say, here's my unpopular opinion.
[3704.26 --> 3705.36]  And then you say a sentence.
[3705.62 --> 3708.36]  And that sentence needs to represent the unpopular opinion.
[3708.86 --> 3710.44]  And then you can say whatever else after that.
[3710.54 --> 3713.30]  Then I'll, at least, I'll get it right when it comes time to the poll.
[3713.42 --> 3715.32]  A lot of people skip that step and they just start.
[3715.72 --> 3717.52]  You guys have done a great job so far today though.
[3717.52 --> 3719.24]  So we'll find out if these were unpopular.
[3719.72 --> 3721.82]  I had go time FM on Twitter.
[3722.14 --> 3724.56]  Follow along and let your voice be heard.
[3724.90 --> 3725.66]  Vote on the poll.
[3725.96 --> 3727.52]  Let Andre and Natalie know.
[3728.12 --> 3729.30]  Johnny, do you got one for today?
[3729.60 --> 3733.86]  No, my unpopular opinion would be that I don't have to have an unpopular opinion.
[3734.16 --> 3734.94]  Jared Demme.
[3736.08 --> 3737.90]  All right, man.
[3738.34 --> 3739.16]  I'm not going to hold you.
[3739.52 --> 3740.54]  All right.
[3740.66 --> 3743.80]  So listen, this has been a nice show.
[3743.80 --> 3744.80]  I learned a lot.
[3744.80 --> 3748.42]  Had some hard positions softened a bit.
[3748.74 --> 3749.44]  I thank you for that.
[3749.70 --> 3755.24]  It's always good to unlearn some things or really just open your eyes to different possibilities.
[3755.42 --> 3756.60]  So I definitely appreciate it.
[3756.98 --> 3758.00]  Thank you for coming on, Andre.
[3758.20 --> 3760.40]  To my co-hosts, Natalie and Jared.
[3760.54 --> 3763.64]  It's been a pleasure having you here with me to do this.
[3764.08 --> 3771.32]  And yeah, I look forward to see how Encore sort of grows and addresses the kind of needs it's aiming to address.
[3771.32 --> 3775.96]  And yeah, continue to be a great contributor to the Go community.
[3776.34 --> 3781.68]  And if you are listening to this and you are interested in finding out more about Go, Encore.dev is the domain, I believe.
[3782.04 --> 3791.48]  And you can also go on GitHub and see what Encore.dev is the org and then see what the Encore repo has that could use your help as a contributor.
[3792.38 --> 3793.68]  So yeah, definitely.
[3793.96 --> 3795.44]  Thanks again, Andre, for coming on the show.
[3795.56 --> 3796.22]  Thank you very much.
[3796.38 --> 3796.76]  That's a wrap.
[3796.76 --> 3807.10]  If you aren't subscribed to Changelog Weekly, you're missing out on what's moving and shaking in the world of software.
[3807.10 --> 3810.36]  We cover what's new, what's interesting, and why.
[3810.66 --> 3811.58]  It's totally free.
[3812.06 --> 3814.62]  Fight your FOMO at changelog.com slash weekly.
[3815.18 --> 3815.88]  Subscribe today.
[3816.42 --> 3820.10]  And of course, check out the back catalog of awesome episodes at gotime.fm.
[3820.10 --> 3824.52]  Did you know we did an entire episode on your Go application structure?
[3824.88 --> 3828.02]  You can listen to that one at gotime.fm slash 94.
[3829.02 --> 3832.44]  Gotime is produced by Jared Santo with music by Breakmaster Cylinder.
[3832.96 --> 3834.34]  We're brought to you by awesome sponsors.
[3834.94 --> 3837.68]  Thanks again to Fastly, LaunchDarkly, and Linode.
[3838.18 --> 3843.72]  Next time on Gotime, Angelica is talking Ethereum with Raul Jordan and Preston Van Loon.
[3844.04 --> 3845.14]  Stay tuned for that one.
[3845.34 --> 3847.22]  We'll have it ready for you next week.
[3847.22 --> 3877.20]  We'll be right back.
[3877.22 --> 3884.30]  The food pyramid had lots of ways with the Slack channel.
[3885.60 --> 3887.30]  The food pyramid is wrong.
[3888.26 --> 3888.70]  Oh, yeah.
[3888.82 --> 3890.48]  I wasn't in the...
[3890.48 --> 3895.56]  The last thing I saw was Johan was agreeing with your unpopular opinion, Natalie, and then I hopped out.
[3896.50 --> 3898.60]  Yeah, the food pyramid was whack, you know?
[3898.96 --> 3899.48]  Turns out.
[3899.48 --> 3899.60]  Yeah.
[3901.60 --> 3904.06]  People are like, well, anything the government does is whack.
[3904.50 --> 3905.92]  It's just the blanket statement.
[3906.26 --> 3906.48]  Yeah.
[3907.02 --> 3909.04]  It was all lobbied by big cereal, you know?
[3913.04 --> 3913.64]  You know?
[3913.78 --> 3914.00]  Yeah.
[3914.22 --> 3914.54]  Yeah.
[3914.72 --> 3914.92]  Yeah.
[3915.02 --> 3916.66]  So, yeah.
[3916.66 --> 3921.30]  I found kale to be very interesting how it's across countries, completely different.
[3921.48 --> 3927.96]  Like, in the U.S., it's considered health food, but then you also find it in, like, an extremely fried version of that, in, like, the chips variation.
[3927.96 --> 3939.24]  But in Germany, and I think also in the north, in, like, northern Scandinavian countries, it's something like a Christmas food or, like, something you eat in winter, which is part of the comfort food almost.
[3939.94 --> 3940.92]  In stews and so on.
[3940.92 --> 3944.38]  And it's a fundamental part of the food pyramid, you know?
[3946.48 --> 3948.18]  Yeah, I totally believe that.
[3948.28 --> 3949.16]  Just, it fits in all.
[3949.20 --> 3955.16]  I totally believe that if Coca-Cola lobbying enough, a bottle of Coke would be at the bottom of the pyramid, you know?
[3955.68 --> 3957.82]  That's how it works around these parts, you know?
[3958.24 --> 3958.64]  Yeah.
[3958.74 --> 3961.96]  I think big salad is a bit underfunded.
[3966.02 --> 3966.98]  Oh, man.
[3967.64 --> 3968.86]  Ugh, big salad.
[3970.92 --> 3971.92]  Oh, goodness.
[3971.92 --> 3971.96]  Oh, goodness.
