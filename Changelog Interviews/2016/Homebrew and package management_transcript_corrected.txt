[0.00 → 3.02] I'm Mike McQuaid, and you're listening to The Change Log.
[11.76 → 16.24] Welcome back, everyone. This is The Change Log, and I'm your host, Adam Stachowiak. This is
[16.24 → 21.48] episode 223, and today, Jared and I are joined by Mike McQuaid, the maintainer of Homebrew.
[21.86 → 27.04] We talked about Homebrew's 1.0 release recently. We talked about a lot of the changes happening.
[27.04 → 33.10] There's no more user local. Homebrew now lives at user local Homebrew to keep user local cleaner.
[33.54 → 39.54] Homebrew also auto-updates now, and in the seven years of Homebrew, the community has grown to nearly
[39.54 → 46.68] 6,000 unique contributors. There's also talks of Linux Brew, which is a fork of Homebrew joining,
[46.88 → 51.96] and lots of fun stuff happening in this package manager space for the operating systems.
[51.96 → 58.96] We have three sponsors on today's show, Rollbar, Top Tile, and Linde. First sponsor of the show
[58.96 → 65.38] is our friends at Rollbar. Rollbar puts errors in their place. Head to rollbar.com slash changelog,
[65.44 → 69.84] get the bootstrap plan for free for 90 days. And today, I'm sharing a conversation with you that
[69.84 → 75.18] I had with Paul Bigger, the founder of CircleCI, and he talked deeply about how they use Rollbar
[75.18 → 80.48] and how important that tool is to their developers. Take a listen.
[80.98 → 85.06] One of the key parts about doing continuous delivery, you don't just have to test your
[85.06 → 89.48] software, but you have to constantly keep track of it. You're going to be doing deploys 10 times a day
[89.48 → 94.10] or 20 times a day, and you have to know that each deploy works. And the way to do that is to have
[94.10 → 101.16] perfect monitoring. And Rollbar is literally the thing that you need to do that monitoring.
[101.16 → 106.26] You need to make sure that every time you deploy, you're going to get an alert if something goes
[106.26 → 109.48] wrong. And that's exactly what Rollbar does for CircleCI.
[109.88 → 114.28] Well, that's awesome. Thanks, Paul. I appreciate your time. So listeners, we have a special offer
[114.28 → 121.80] for you. Go to rollbar.com slash changelog, sign up, get the bootstrap plan for free for 90 days.
[122.16 → 129.12] That's 300,000 errors tracked, totally for free. Get Rollbar trying today. Head over to rollbar.com
[129.12 → 130.46] slash changelog.
[131.16 → 145.62] We're back. We got a fun show lined up. Got Mike Le quay here from Homebrew, Homebrew fame.
[146.20 → 148.92] Obviously, Homebrew 1-0. Jerry, what do you think about that, man?
[149.50 → 156.38] I was excited. I think our whole community was excited. It's a big announcement from a big project
[156.38 → 161.06] that many of us have relied upon for years and years. And it's awesome to see anything
[161.06 → 166.32] hit that 1.0 milestone. So Mike, congratulations on the big release and welcome to the changelog.
[166.64 → 171.48] Thank you very much. Thanks for having me, guys. Yeah, no, it's an exciting time, I think,
[171.48 → 178.42] for most of the Homebrew team as well. Because we've been sort of a bit haphazard with the version
[178.42 → 183.40] numbers. If you look at, I went through and actually took the time before the release to go and tag all
[183.40 → 188.48] the old versions through there. And some of them are, you know, multiple versions in the space of a
[188.48 → 192.50] week. And then you have years, I think, between some versions, and they're all a little bit arbitrary.
[192.50 → 198.28] And now it's kind of giving us this chance to sort of become a more real software project and start
[198.28 → 202.82] doing like semantic versioning and start kind of thinking about how we're doing our release process
[202.82 → 205.50] and try and have that stable base for people to be able to rely on.
[206.28 → 212.06] Now, Adam, you had a Homebrew show back before I was a co-host of the changelog, all the way back in 2010,
[212.30 → 215.62] episode 35. You want to give us a little bit of background on that?
[215.94 → 218.14] I wish I could, man. I wish I could remember six years back.
[218.14 → 223.42] I could barely remember last week or last month. But just based on our own show notes,
[223.54 → 227.62] me and Wynn, when Wynn was part of the show. And it's kind of funny because now Wynn works with
[227.62 → 233.28] Mike as manager, manager of somebody's manager or something like that at GitHub. But, you know,
[233.36 → 237.62] we caught up with Max Howell, talked about Homebrew. I think the show was a lot more loose then.
[237.78 → 241.86] I don't think we were quite as standardized as we are now, where we kind of go into the history and
[241.86 → 246.22] kind of go deep like this. It was a bit just more, a bit more of a wing it kind of show, I guess,
[246.22 → 250.18] then. But fun talking to Max. I can't remember a single thing we talked about. I know we talked
[250.18 → 256.64] about at least Mac, beer and scrabbling because that's what the notes say. So there you go. But
[256.64 → 263.18] you can check that out at changelog.com slash 35 or scroll all the way back or pretty far back in the
[263.18 → 267.08] list of podcasts that you have there in your listener.
[268.02 → 272.18] Yeah. So it's been a long time and definitely kind of catch-up show, but a new show,
[272.18 → 278.80] an introduction to Mike. Mike, we like to get backgrounds, origin stories, kind of the roots
[278.80 → 284.46] of where you began in the programming trades. So can you tell us how you got started, and what got you
[284.46 → 285.06] to where you are now?
[285.86 → 292.46] Sure thing. So I guess I first got sort of interested in computers and computer things being
[292.46 → 298.94] young and when my parents brought our PC home. And it was always like, I guess my parents learned
[298.94 → 303.26] that they could pretty much get me to do any chore, including like mind-numbing spreadsheet
[303.26 → 308.50] entry if it was on the computer. And I was just, I don't know, I was always fascinated with the
[308.50 → 313.78] things. So when the time came to go off to college, I went and studied computer science
[313.78 → 319.22] and yeah, and basically just got more into, I guess, open source while I was doing that.
[319.36 → 324.92] There was our curriculum was quite kind of Unix focused. So I ended up kind of using Linux on my
[324.92 → 332.60] desktop and all the fun that, that that produced back in 2007 using Gen 2 to compile everything
[332.60 → 336.68] from source. So it would take like days to get my system ready in 24 hours.
[336.94 → 336.98] You were hardcore.
[337.60 → 343.08] Well, I mean, I don't know if it was so much hardcore as just masochistic, but it was certainly,
[343.34 → 348.98] I certainly learned a wee bit along the way about, you know, how, how software gets put together
[348.98 → 354.34] and how things kind of build and how they fail and stuff like that. So yeah, I kind of dabbled
[354.34 → 358.08] with that through Unix started doing little bits of open source programming kind of by
[358.08 → 362.90] myself, like publishing stuff on my website or whatever, but not really collaborating
[362.90 → 369.42] with anyone and beyond kind of university group projects. And until after, I guess I
[369.42 → 372.46] was sort of got a bit involved with the Gen 2 kind of bug tracker and stuff like that.
[372.56 → 379.02] And then my summer after graduating, I did Google Summer of Code on the KDE project, which
[379.02 → 384.90] was the Linux, like, I guess a desktop environment or like the kind of GUI and stuff like that.
[385.22 → 389.30] And, and yeah, and I kind of worked on that for a few years and that, that was great fun.
[389.90 → 397.90] And then in the end, I remember the very, so I had a job where I was doing like Qt, the kind of
[397.90 → 402.70] toolkit it's based on, which everyone thinks is Qt, but it's actually Qt, which is always interesting
[402.70 → 407.12] when you refer to someone who doesn't know this as, oh, they are also a Qt developer.
[407.12 → 415.30] And then, yeah, so there you go. But yeah, so I was doing that. So part of the job, a lot
[415.30 → 420.08] of clients back then, at least were wanting stuff that would run on at least two out of
[420.08 → 424.80] three platforms, Windows, Mac and Linux. So I would, I had like an environment for each
[424.80 → 428.86] of those platforms. And so I had kind of a Mac that I kind of had picked up because
[428.86 → 433.86] of that. And I didn't really use it for much. And then I remember one day I had some friends
[433.86 → 437.00] around, and we were trying to watch, I had dual monitor set up, and I was trying to watch a
[437.00 → 442.76] DVD without tearing on my new NVIDIA card or whatever. And I couldn't get a DVD to play.
[442.86 → 449.46] And this was in 2008, I think, you know, 2008, 2009. And I couldn't get a DVD to play properly.
[449.86 → 454.62] And I was just like, that was the day I realized that my, my days with desktop Linux were done.
[454.96 → 460.24] And so I pulled out the Mac, plugged it in, and then that all worked perfectly. And then sort of
[460.24 → 465.62] slightly moved my approach over to the Mac was doing some KDE on Mac stuff before I kind of gave
[465.62 → 471.58] up. And then kind of used Mac ports a bit. And then I ended up creating this while working on
[471.58 → 476.12] this thing called Mac ports dummies, which kind of sort of led me a little bit into homebrew.
[476.22 → 480.32] Mac ports dummies was a way of like sort of pretending that a bunch of stuff was installed
[480.32 → 485.34] that was provided by OSX. And then I kind of knew Max, he was a friend of a friend.
[486.02 → 488.88] And we ended up kind of meeting up and going for a beer and stuff like that. And he was like,
[488.90 → 491.84] oh yeah, you know, there's this homebrew thing I've kind of made, you should check it out. It
[491.84 → 496.50] sounds like it's sort of in keeping with your interest. So I guess that was about 2009,
[496.50 → 502.02] I started working on homebrew. And I guess since then I've been kind of working as a maintainer and
[502.02 → 503.76] yeah, just never really stopped.
[504.72 → 510.18] So that's an interesting way to go to the Mac. I guess my story was a little different. I was on
[510.18 → 516.02] Windows, and it just was a better machine. So I just kind of went to the Mac and didn't look back,
[516.16 → 520.78] but you know, moving to the Mac is that's kind of interesting story to kind of get to the Mac
[520.78 → 521.40] basically.
[522.10 → 527.40] Yeah. It's, it's weird, I guess, because when I talk to a lot of people who, I guess being involved
[527.40 → 532.38] with a project like homebrew, and I'm also kind of really obsessive about like OSX styling,
[532.38 → 537.62] like I still use text mate as my main editor, just because I mean, as much as I love things like
[537.62 → 542.38] Atom and Sublime, they don't look like quite right. Right. And so everyone assumes I'd be one
[542.38 → 547.90] of those people who's been on a Mac since I was, you know, like, purist. Yeah, exactly. Like since,
[548.02 → 550.18] you know what year was that? Because I mean, you might be a purist.
[550.74 → 557.26] Well, so I guess that was 2000 and yeah, 2008 or nine, I kind of, yeah. So the first Mac I had was
[557.26 → 564.56] on Leopard on 10.5, also the first version of OSX that homebrew supported. So yeah, I've been on a
[564.56 → 569.76] wee while at this time, but like, yeah, I feel like I've, you know, the really hardcore folks are
[569.76 → 572.38] the people who had the OS9 machine at home.
[572.58 → 577.64] Right. A little bit, a little bit sooner to the party than you, but not much. In fact, my path is
[577.64 → 582.18] very similar. Only I was on Ubuntu in college, started off on Windows in high school, Ubuntu in
[582.18 → 588.38] college and just got sick of, of having to deal with mostly device drivers and Wi-Fi back then.
[589.52 → 595.06] And the Mac was tantalizing, I think it was probably 2007 and Leopard was also my first version.
[595.48 → 598.96] That being said, man, I'm far moved away from TextMate at this point. Are you at least on
[598.96 → 603.96] TextMate 2 or are you like real old school? Yeah, I'm on TextMate 2, and I'm, I'm kind of
[603.96 → 608.90] scratching my own itches quite a bit more. Like, you know, I've, I've made a few bundles for it and
[608.90 → 614.62] all this type of thing, but it just fits pretty well with, with my workflow. So as I say, I try
[614.62 → 619.38] other things, but then I just, there's tiny little things that annoy me and I might just be too old
[619.38 → 624.98] and far gone at this point to stuck in my ways. So give us a little bit of the context around,
[624.98 → 630.28] uh, you gave us how you met Max and you started contributing to Homebrew and using it a lot. Um,
[630.86 → 636.88] give us the, the timeframe around Max's kind of transition out. You're now lead maintainer. Of course,
[636.88 → 642.88] it's a huge project with thousands of contributors. And, um, many of that is because of the way that
[642.88 → 646.46] you can use to contribute formula, which has recently changed. We'll talk about that soon,
[646.46 → 651.50] but help us out with the transition where you, you became the man when it comes to the
[651.50 → 656.94] homebrew community and project. Well, I mean, I guess, so the lead maintainer thing is quite recent.
[656.94 → 663.16] Like the that title at least is literally just something we sort of decided shortly before
[663.16 → 671.30] homebrew 1.0. Um, so Max, I guess like, like any open source project, and we try and build this into
[671.30 → 676.08] the way we kind of run homebrew, there's the expectation that people will kind of come in
[676.08 → 681.54] and come out and stuff like that. And I think Max just ended up having a different job and was
[681.54 → 684.56] spending less time on homebrew and some other people stepped up and were spending more time
[684.56 → 690.92] on homebrew. And, you know, in the end, I think he just ended up sort of drifting out and other
[690.92 → 695.56] people ended up drifting in. And when Max left, so he, he was the kind of, you know, the lead at that
[695.56 → 703.60] point. And when he left, we kind of agreed that we'd sort of have a sort of democratic situation where,
[703.60 → 710.20] you know, we would decide things more or less by committee and stuff like that. And I think that,
[710.20 → 713.70] and there are definitely a lot of open source projects where that, that goes pretty far.
[713.70 → 718.72] I think where we struggled and where we felt the kind of pain of that coming up recently was
[718.72 → 725.38] when, well, I was kind of contributing a lot more than other people were. And when you have
[725.38 → 730.18] the idea that almost it's a democracy and everyone gets a vote, like it doesn't,
[731.10 → 736.80] with the way, I guess I read a thing about the governance models and the best one, you know,
[736.80 → 742.56] that meritocratic is a really loaded term, and it's not, I don't think it applies in open source,
[742.68 → 747.16] but that what people have described as the meritocratic governance model is almost like
[747.16 → 753.50] you have more decision-making power based on doing more work basically. So, you know,
[753.68 → 757.96] and that's not commit counts or lines of code changed or whatever, but basically if you're more
[757.96 → 762.52] involved, if you're spending more time in the project, and you're kind of leading the direction
[762.52 → 767.26] a bit more than you probably have a bit more say. So I think the lead maintainer thing came about
[767.26 → 773.84] because I was essentially kind of filling that role and, you know, to validate some other kind
[773.84 → 779.22] of complaints, I think that were made, like I was maybe sort of overruling or pushing through
[779.22 → 784.26] some things and not really operating by the committee side of things. And, and my,
[784.40 → 788.74] my understanding was that people were annoyed that I was doing that. Whereas I think actually,
[788.74 → 793.24] like having talked about it more and come to the lead maintainer thing, what was annoying people
[793.24 → 800.40] more was actually this, this disconnect between the, the reality of like me kind of basically leading
[800.40 → 807.64] and other, other people feeling like they couldn't overrule me on things. And, and yeah, and I guess,
[808.06 → 812.98] you know, I'm sure you've all read and heard about, you know, all this stuff about implicit and
[812.98 → 818.14] explicit power structures and, and GitHub's as a company has had its movement through there as well.
[818.14 → 823.20] And I think that's basically what the move has been is that it's moved from being an implicit
[823.20 → 828.44] to an explicit thing. And it is just, as a result, it's made a few little things a little bit easier.
[829.12 → 832.18] So there was an explicit transition then from Max to you or?
[832.94 → 839.70] Well, no, I guess so. The transition was from Max to, I guess, every, to all the maintainers,
[839.96 → 846.56] I think it was five or six of us at that point. And then that we grew up to, I think, 13 maintainers.
[846.56 → 852.64] And then the transition from that model to being me with, with the kind of majority agreeing that
[852.64 → 853.76] that was a good move.
[854.46 → 858.52] I'm sitting here on the contributors tab, man. It's funny you say that too, that it wasn't just,
[858.62 → 863.78] you know, contributors in terms of code, but contributors in terms of effort across the
[863.78 → 868.58] project, whether it's thought, leadership, governance, whatever. I think that that's something
[868.58 → 873.32] that the contributors tab doesn't really reflect very well. But one thing that I was thinking about
[873.32 → 877.60] on the contributors tab is I'm looking at Jack Nagel. I'm looking at you. I'm looking at Adam V.
[877.94 → 882.28] I'm looking at Max. And so for others that kind of line up there, I kind of wish we can overlap,
[883.14 → 889.48] you know, see Mike and you and Max and Adam, see all of your graphs kind of in the same timeline,
[889.48 → 894.84] because just kind of like looking at them, I can see where Max was having fits and starts during a
[894.84 → 901.24] couple during 2012. And you seem to like start to get more involved in terms of contributions.
[901.24 → 906.38] And then it seems like when Max dipped away and stepped off to do his own thing or go to Apple
[906.38 → 911.32] or wherever his path has taken him is when you got more involved in the same thing with Jack and
[911.32 → 915.32] a little bit the same thing with Adam as well. So it's kind of interesting to look at the
[915.32 → 916.30] contributor graph that way.
[916.82 → 922.30] Yeah. And it's interesting as well, because as I think you are, I suspected you were going to mention
[922.30 → 927.84] later on anyway, there's the we've split into two repositories now. So you've got the homebrew brew,
[927.84 → 934.38] which is the package manager and homebrew core, which is the formulae. And we kind of split the
[934.38 → 940.30] history between them as well. So you can kind of see the kind of this quiet difference in
[940.30 → 944.46] contribution patterns between the two. And there's the same sort of faces in there, but you know,
[944.52 → 950.12] there's someone who, um, people who are very, very active in one and not really in the other.
[950.12 → 956.60] And I think that was the big thing where like Max particularly was kind of always most active
[956.60 → 961.76] in the package manager itself. And I guess lately I've been sort of similar. I've kind of, you know,
[961.76 → 965.96] had a reasonable number of contributions to the packages, but like not nearly as much as some
[965.96 → 972.18] other people. And in the last, the 1.0 release has been more of a thing around the package manager
[972.18 → 977.86] rather than the packages itself. And so that's where my focus has been the last, I guess, few months,
[977.86 → 984.32] certainly. So when you went into this, uh, meritocracy or voting based things and you,
[984.46 → 990.86] you all found that it wasn't moving forward at the pace or the, you know, the desired, uh,
[991.06 → 996.10] pace that you, you guys wanted it to. And then because you were already kind of implicitly acting
[996.10 → 1001.00] as a leader or as you thought, perhaps overstepping your bounds, but people actually appreciated it.
[1001.44 → 1006.00] Um, did you end up just kind of like with this flat structure where it's, you know, Mike McQuaid
[1006.00 → 1012.46] and then everybody else, or is there underneath that structure, is there a group of core
[1012.46 → 1016.22] maintainers and then everybody else? How exactly does it structure it now?
[1016.66 → 1022.16] So, I mean, we have what our kind of lingo is, and I realize it varies from project to project is
[1022.16 → 1028.04] what we call a maintainer is basically anyone who has commit access. And historically that's always
[1028.04 → 1032.34] been based on you get commit access to both repositories. You don't just get it to one.
[1032.34 → 1035.98] That, that may be something that changes in the future. We have people who are very interested
[1035.98 → 1040.96] in just the package manager and not the packages or vice versa. And then we have contributors,
[1041.20 → 1047.12] which are anyone who's ever submitted a single commit, um, to any project basically within the
[1047.12 → 1053.68] homebrew umbrella. And then we have users obviously, which goes without saying. Um, so we've, yeah,
[1053.74 → 1057.90] so we've moved from a model of being all the maintainers are like, at least on paper, kind of
[1057.90 → 1064.58] on an equal footing to being, I'm, I guess, technically in charge, but then it, the way I've
[1064.58 → 1070.32] had a good manager in a workplace deal with this stuff in the past is that they basically
[1070.32 → 1076.10] only invoke their manager status when they have to, when, so they will always try and like
[1076.10 → 1082.24] have a discussion and win the discussion on an equal footing. Well, not win, but, you know,
[1082.30 → 1087.60] convince other people of their point. And I feel like it's the same thing with us now that
[1087.60 → 1093.56] the lead position is mainly just there to be able to have me be able to say sometimes like,
[1093.64 → 1098.04] okay, well, we need someone to make a decision here. We have two sides who are kind of equal
[1098.04 → 1102.92] or equally, like there's some stuff that is important in the direction of the project.
[1103.14 → 1107.80] And this is a feature that other people may not feel passionately about, but I feel that
[1107.80 → 1111.98] this has to go in, and it's important for us to have this feature, even if the bulk of other
[1111.98 → 1117.56] maintainers might disagree on that front. Um, and maybe part of that is because
[1117.56 → 1122.10] you know, we, we do, we started gathering analytics, which I don't want to get too much
[1122.10 → 1127.12] into, but you know, before that a big part of it would be, I mean, I, I was the person
[1127.12 → 1131.26] who did the most, I guess, talks at conferences about homebrew and stuff like that. And I've
[1131.26 → 1135.02] kind of travelled around and met a lot of users and there's a certain amount of stuff that
[1135.02 → 1138.48] it doesn't, it doesn't turn into mailing list posts. It doesn't turn into issue tracker,
[1138.48 → 1142.46] but you, you speak to the same sort of power users again and again, and you hear the same
[1142.46 → 1147.46] complaints again and again, like in person. And then some of that has sort of driven the
[1148.06 → 1152.32] kind of, I guess, product direction of homebrew maybe a bit more because you just realize like,
[1152.40 → 1156.28] okay, this isn't, people are not filing issues because they're confused about this. This is
[1156.28 → 1161.00] just something that they find annoying and people generally don't find like file issues about just
[1161.00 → 1165.78] things that are like annoyances. They file them about things that are actively broken or whatever.
[1165.78 → 1171.54] So let's touch real quick on GitHub's relationship with homebrew with regard to, you know, employing
[1171.54 → 1175.68] you, and you're the lead maintainer. And is this officially sanctioned work or is it, are you
[1175.68 → 1179.64] still doing it like completely on the side? And then we'll take our first break. And on the other
[1179.64 → 1183.86] side, we'll talk about the new stuff in homebrew specifically. I will probably start with the
[1183.86 → 1186.70] split repositories, but how does GitHub play into the mix?
[1187.58 → 1193.50] So I guess I've been at GitHub coming up to three years. So certainly the majority of my time working
[1193.50 → 1199.38] on homebrew has not been at GitHub. And GitHub, similarly with my previous employees, really, like
[1199.38 → 1206.60] they, they have, I guess, paid me to work on homebrew on occasion in the when I have had Google
[1206.60 → 1210.86] Summer of Code students through GitHub and stuff like that, or Homebrew Google Summer of Code students,
[1210.88 → 1216.36] which have been blessed with GitHub. I've spent work time on that in terms of like day-to-day work.
[1216.76 → 1222.92] Like I, I don't, in theory, at least work on it on GitHub's time. If I'm blocked waiting for
[1222.92 → 1227.24] something for like five minutes, I'm waiting for a test run to finish. I'll go and fire through my
[1227.24 → 1232.02] homebrew emails, triage, give a little reply, whatever. And then equal, there's something that
[1232.02 → 1237.48] is going to, or is currently blowing up and will affect GitHub employees because we use
[1237.48 → 1243.00] homebrew fairly heavily internally. And then I'll fix that. But I don't generally do kind of
[1243.00 → 1248.62] the day-to-day kind of homebrew work during GitHub time. So that's mainly my kind of evenings,
[1248.76 → 1249.92] weekends, spare time, et cetera.
[1249.92 → 1254.16] Very good. Well, I think that sets us up. Let's take a break. And on the other side,
[1254.20 → 1258.92] we'll talk about what is new with Homebrew 1.0.0. We'll be right back.
[1260.92 → 1265.42] I talked to Daniel Reed, head of design at Top Tow, about their new expansion into
[1265.42 → 1270.66] Top Tow designers, doing for designers what they've done for developers. We talked about why
[1270.66 → 1273.50] Top Tow works for designers, and this is what she had to say.
[1273.50 → 1279.70] As a designer, the big, or as any kind of creative person, the big overarching question is always
[1279.70 → 1285.44] like, how can you find inspiration? And for me personally, and for a lot of creatives that
[1285.44 → 1290.28] I've spoken to, it's really about travelling, exploring, and being accountable for your own
[1290.28 → 1296.72] career. And I think as a Top Tow designer or a remote designer in general, the ability to be able to switch
[1296.72 → 1303.62] up your lifestyle, change contexts, meet new people, have new ideas sort of infiltrated into
[1303.62 → 1308.28] your life by having that freedom and flexibility is something that's absolutely fundamental to doing
[1308.28 → 1314.60] great work. For any designer that is wanting to pursue their skills, to be accountable for their
[1314.60 → 1319.80] life, to have new challenges, that's the real power of Top Tow, I feel. You're not just stuck with
[1319.80 → 1327.82] one product, one company, or even one agency, but you can choose to work on multiple occasionally, or a range
[1327.82 → 1333.12] of different clients. And I think that that keeps you fresh, it gets you involved in new technologies,
[1333.32 → 1338.38] different people, and is really fundamental for being sort of switched on as a designer.
[1338.94 → 1342.86] All right, that was Daniel Reid, head of design for Top Tow. To learn more, go to
[1342.86 → 1349.48] TopTow.com slash designers, that's T-O-P-T-A-L dot com slash designers, tell them Adam from the
[1349.48 → 1351.84] changelog sent you, and now back to the show.
[1357.86 → 1364.38] All right, we are back celebrating, cheering even, on Homebrew 1.0 with Lee Bain Tate or Mike McQuaid.
[1364.56 → 1369.56] See what I did there? I like that. And Mike, we like to hear all that's fresh and new. We haven't
[1369.56 → 1374.58] covered Homebrew for many years. You don't have to go through the entire history of the source code,
[1374.72 → 1381.38] but kind of just want to camp out on what's new with the official 1.0 release. And there's a lot
[1381.38 → 1388.40] of highlights. We have the separate repos, we have the community site, we have the move out of user
[1388.40 → 1395.44] local, user local Homebrew, we have the software conservancy, software freedom conservancy thing.
[1395.64 → 1399.36] So we'll kind of work our way down through the list, but let's start with where we left off,
[1399.36 → 1406.36] which was that you guys split the repositories up. And one thing about the original Homebrew
[1406.36 → 1410.90] repository, which by the way, it's still out there, you guys have it under brew,
[1411.36 → 1419.32] under legacy dash Homebrew, is it was always one of the most forked and starred and watched and
[1419.32 → 1425.84] contributed to, probably has the most PRs perhaps, of almost any repository on GitHub,
[1425.84 → 1431.08] because of the reason that not just like you said, not just the package manager itself,
[1431.18 → 1436.54] the source code that makes up Homebrew is in there, but also all the different formulae,
[1436.90 → 1441.60] which is how you know, the descriptions of how packages get installed and uninstalled.
[1442.08 → 1445.70] So when I first saw that you guys split up into different repos, I thought, oh, no,
[1445.70 → 1449.38] they had this great star count. They had this great fork count, you know, this kind of this
[1449.38 → 1457.60] statistical legacy there that now is going to be broken. But that being said, you all have set up
[1457.60 → 1463.32] analytics over the last year or so that gives you better stats than just the stars and the forks
[1463.32 → 1469.72] for actual usage. So start off with telling us the onus behind splitting the repositories,
[1469.72 → 1473.12] and then perhaps give us some insight into the analytics that you guys have been tracking.
[1473.12 → 1481.14] Sure thing. So I guess the main onus is the problem with Homebrew before was if you wanted to get,
[1481.48 → 1485.68] say you wanted to get a new version of some package, you run brew update to kind of update
[1485.68 → 1490.72] Homebrew's kind of definitions. And that also updates the package manager. The problem with that is,
[1491.12 → 1495.90] if you want the new update of something, and we have made some change on master,
[1496.40 → 1502.38] which breaks something for you, then there's no way you can get the new version of OpenSSL or whatever.
[1502.38 → 1507.96] And not get the broken thing as well. So we've kind of had that goal for a long time to be able to
[1507.96 → 1512.44] separate the package manager from the packages. And I mean, that's what every other package manager
[1512.44 → 1517.58] does. And to separate those two things out, so we can provide some degree of stability.
[1518.24 → 1523.12] So that was the first step in the process, which again, is kind of noted in the release notes that
[1523.12 → 1528.86] now we kind of jump between tags. And so you can, if you're kind of a Homebrew maintainer,
[1528.92 → 1532.26] then you continue to track the master branch, but everyone else kind of jumps between,
[1532.26 → 1538.44] 1.00, 1.01, et cetera. And that gives us time to be able to do more QA on the package manager
[1538.44 → 1544.06] itself while still having that rolling release approach for the formulae. And in terms of stars
[1544.06 → 1547.96] and all that type of stuff, like, yeah, that still breaks my heart a little bit. I still
[1547.96 → 1555.04] weep for the star count, but you know, it's slowly getting its way up on the new repository and stuff
[1555.04 → 1559.84] like that. And it is useful to be able to see stuff like GitHub's kind of contributor graph and see how
[1559.84 → 1563.70] that varies on the package manager compared to the packages. Cause that's interesting.
[1563.70 → 1569.54] And another thing on there, which is a wee while off probably still is we're trying to get the
[1569.54 → 1573.12] package manager. There's another thing called Linux brew, which is like running Homebrew on Linux
[1573.12 → 1579.28] and stuff like that. And having the package manager be separate means that we can, we can separate out
[1579.28 → 1585.34] our package definitions for, but still have the package manager itself be cross-platform support
[1585.34 → 1590.84] platforms, stuff like that. And it generally just provides it as a nice tool. Who knows? Maybe one
[1590.84 → 1597.16] day it might even be bundles of Ruby gem you can use to kind of access your, your stuff. And, but yeah,
[1597.16 → 1603.42] nowadays we have, as you mentioned, the analytics that was introduced, I think it was March or so.
[1603.42 → 1610.10] And that basically provides us with the ability to see, we can't see any stuff about individual users.
[1610.10 → 1614.36] If I wanted to see, okay, this particular user, what have they done? But that's not available to us
[1614.36 → 1620.70] because we kind of just use a random UUID that people can reset at any time. And so we track users
[1620.70 → 1625.92] just so we can get kind of user counts. And so I've got kind of the analytics dashboard open right now.
[1626.00 → 1630.94] It's, you know, it's kind of a slightly weird mapping from what it's normally used for, but it basically
[1630.94 → 1635.66] lets us see what commands people run like in proportion to each other, what packages people
[1635.66 → 1640.96] are running, what versions people are running. And the really useful stuff for us is what is like
[1640.96 → 1646.24] the percentage breakdown on stuff like OSX versions. So then we can prioritize the support on different
[1646.24 → 1651.06] things. And also what are the most popular packages that people install, and what options
[1651.06 → 1654.58] are they installing with? So again, we can kind of prioritize options and things like that.
[1655.12 → 1660.58] So as a whole, it basically just provides what analytics tends to do for, for any, um,
[1660.94 → 1666.16] piece of software, which is, it lets us inform our future design and inform kind of what things we
[1666.16 → 1671.28] focus on based on the stuff our users actually use rather than our speculation on what the users use,
[1671.40 → 1673.00] which is something we didn't have before.
[1673.76 → 1678.90] We get hub stars and watchers are indicators, but they're not exactly, I don't think, uh,
[1678.90 → 1683.52] those things are for maintainers. I think they're more for the public to show some,
[1683.52 → 1688.02] I mean, because I can't give you that deep of insight, like knowing watchers and stars,
[1688.02 → 1692.18] those are important, but it's not giving you deep enough insights that you need as a maintainer
[1692.18 → 1692.68] these days.
[1693.36 → 1698.34] Yeah, I agree. Like it's not, you know, you certainly can't have like, Oh, well we did this,
[1698.44 → 1702.58] we ship this new feature, and we got, you know, 5% more stars. That doesn't really,
[1703.08 → 1706.74] that doesn't really help us. Whereas when we see, we ship this new feature and our error
[1706.74 → 1712.52] counts gone up from, you know, 0.01% to 0.05 or whatever and stuff like that. Like that's
[1712.52 → 1717.32] more of the type of things we're concerned about. And it's particularly useful when,
[1717.50 → 1722.40] you know, when we can go and see if something breaks, like we, we periodically go through and,
[1722.44 → 1726.90] you know, do some porting or when a new version of OS X is out or whatever.
[1727.08 → 1730.46] And it's useful to be able to go through all of our packages and be like, okay, well,
[1731.18 → 1735.04] this thing's broken on the new version of OS X, but no one has actually installed this since March.
[1735.10 → 1739.22] So let's not go and spend like three hours trying to fix this piece of software that
[1739.22 → 1742.94] no one is actually using. We can just remove it instead. We call it,
[1742.98 → 1747.86] sending it to the boneyard, which means the definition is still there. If someone wants
[1747.86 → 1752.14] to pick that up at a later point and pull that through, then they can do that. That's,
[1752.24 → 1756.16] it's a little bit easier than kind of navigating through the Git history if you're not a Git whiz.
[1756.84 → 1762.94] And it lets us kind of push away the kind of maintenance burden of that for a wee while at least.
[1763.42 → 1768.38] Well, you wouldn't think twice when delivering an application that you do for work or whatever
[1768.38 → 1771.74] about installing error tracking or installing monitoring or something like that. So
[1771.74 → 1776.74] it's almost the same case for, you know, homebrew is that you need something to track
[1776.74 → 1781.46] what's happening so that you can make good decisions for the future, right? You wouldn't
[1781.46 → 1782.06] think twice.
[1782.78 → 1787.24] Yeah, exactly. And I think that's, that's what it comes down to for me is I have used a lot of
[1787.24 → 1792.24] these tools. Well, I mean, across, I think every workplace I've been at, I've used some sort of
[1792.24 → 1797.74] kind of metrics tracking. And again, people, I guess people sometimes think that metrics tracking is just
[1797.74 → 1802.20] Google Analytics and like, oh, well, they don't have Google Analytics installed. So they're not
[1802.20 → 1806.02] tracking metrics. And so, well, actually they're probably tracking metrics in the backend and
[1806.02 → 1809.72] they're not doing this because they're selling your personal information. Well, I mean, some
[1809.72 → 1813.58] companies are doing that because they are selling your personal information. But in homebrew's case,
[1813.82 → 1819.48] it was kind of disappointing to see where exactly we're not. I mean, we've specifically designed it
[1819.48 → 1824.42] so that we couldn't, even if we wanted to kind of get anything that would be commercially viable out of
[1824.42 → 1829.42] this. So the thing is, is that it's kind of disappointing when you release some stuff like
[1829.42 → 1834.28] the analytics, because you get some people who go and express kind of obviously some sort of
[1834.28 → 1838.52] solidarity with like, well, okay, I understand why you're using this. And most homebrew's users are
[1838.52 → 1845.36] developers. So there is that, but then there's this very vocal minority who, you know, who escalates
[1845.36 → 1851.16] beyond that. And it becomes, how dare you have this? How dare it is opt out rather than opt in?
[1851.16 → 1855.90] My reasoning, obviously for it being opt out is because you can gather better data if you're
[1855.90 → 1860.94] tracking the majority of people and not just the subset of people who decide to opt in. They may
[1860.94 → 1865.60] well have different behaviour and stuff like that, which means that you're not able to make as sound
[1865.60 → 1871.00] decisions. But yeah, so, and that vocal minority, you know, that they got very upset on some of them on
[1871.00 → 1876.62] hacker news and Reddit and stuff like that, and then start sending me personal emails telling me to,
[1876.62 → 1883.08] you know, do all sorts of things. And it's not, yeah, it's, it's not unpleasant. And it is with
[1883.08 → 1888.44] hindsight, it's funny. And I'm lucky enough to have a thick enough skin that it, it didn't bother me
[1888.44 → 1895.02] too much. But I mean, it, it is depressing that we still are in 2016 have to deal with stuff like
[1895.02 → 1899.86] this, because I mean, if there's any of those people who, and I did say this to someone who,
[1899.86 → 1904.60] and who emailed me, I mean, that that's what kills open source. That's what drives open source
[1904.60 → 1911.72] maintainers away, and kills successful open source projects like me and, well, I had moments, but
[1911.72 → 1916.20] certainly some of our other kind of major maintainers had to be talked into staying in the project at
[1916.20 → 1920.90] all, because they were, you know, and several of my, we talk about diversity problems, sometimes in
[1920.90 → 1926.20] open source as well, you know, several of my co-workers who aren't just, you know, young white men,
[1926.20 → 1930.38] who I talked to about the homebrew thing is they just said, that sounds awful, like, I would never
[1930.38 → 1936.82] want to be involved with a project where I would have that abuse, or something I do in my spare time
[1936.82 → 1941.70] to try and help out other people. And I think it is, you know, it does seem to be getting better. And
[1941.70 → 1946.44] we do seem to be as a community recognizing that, like, this behaviour is not acceptable. And this
[1946.44 → 1954.36] behaviour is not what we, how we build software. And, but, you know, we don't necessarily have
[1954.36 → 1959.00] all the kind of tooling and institutions and everything quite figured out how to kind of
[1959.00 → 1964.08] stop stuff like that when, as you say, it's, you're an email or a Twitter message away from someone
[1964.08 → 1965.40] starting to be mean.
[1966.26 → 1971.06] Well, sorry that you had to go through all that, Mike. In light of the change, and the fact that you
[1971.06 → 1974.70] guys have had it running for a while, could you, would you mind sharing some stats with us, like
[1974.70 → 1979.56] users or popular packages, or what, what fruit have come from these analytics?
[1979.56 → 1985.18] Yeah, sure. So, I mean, I can see the kind of active users, which I guess is someone whose run a
[1985.18 → 1991.22] homebrew. Like, so there's, I think, 2000 people who've run a homebrew command in the last 30 seconds or so.
[1991.98 → 1992.30] Nice.
[1992.80 → 1997.22] There may be more than that. And then I can see kind of the version breakdown. Interestingly, there's still
[1997.22 → 2004.24] a lot more people running on pre 1.0. And the kind of active users right now, there's like over 1000 on
[2004.24 → 2014.96] 0.99. And then 637 on 1.05, 209 on like the kind of master, the last kind of master commit, and stuff like
[2014.96 → 2021.48] that. And then I jumped through to kind of the most popular packages. And somewhat unsurprisingly, open SSL is the
[2021.48 → 2028.26] most popular package by far, then followed by package config, which is used, like, it's one of those things where no one
[2028.26 → 2033.46] probably intentionally installs it, but it's a dependency for a lot of things. Then living,
[2033.80 → 2039.06] SQLite, great piece of software, Node.js, free type, again, probably something that not a lot of people
[2039.06 → 2045.14] are installing intentionally, and then git. And so, yeah, it's kind of, it is valuable being able to see
[2045.14 → 2051.28] these things. And the dropdown is kind of quite impressive. So, I mean, open SSL, we have in
[2051.28 → 2056.22] Homebrew itself, and this tracks Homebrew and our kind of third-party repositories. So, you know, maybe
[2056.22 → 2063.94] 4,000 different packages. So, of that, open SSL itself has like 3.5% of all installs of all software.
[2064.74 → 2072.06] And so, it's quite interesting to see how quickly it drops off, and you get below kind of 0.1%
[2072.06 → 2076.16] within the first, you know, 170 packages.
[2077.04 → 2081.84] Curious, in light of transparency and open source, kind of the spirit of the community,
[2081.92 → 2084.90] have you considered making the I don't know if you can even do that with Google Analytics,
[2084.90 → 2088.70] but like an open dashboard where anybody can come and just see the usages?
[2089.50 → 2095.86] Yeah, you can't, unfortunately. I mean, what I have been considering is doing a database dump
[2095.86 → 2103.40] every so often of like the stuff that I'm kind of most interested in. But yeah, I mean, it's, again,
[2103.50 → 2108.80] it doesn't seem to be a trivial way of automating that. So, it needs to be me manually going in and
[2108.80 → 2113.64] like clicking through every time. So, yeah, I'm still, that's still kind of on my list of things
[2113.64 → 2118.42] to try and do, to try and improve the transparency of this. And then hopefully people can see that
[2118.42 → 2121.78] this is not, you know, there's nothing nefarious happening here.
[2122.34 → 2126.36] Yeah, because I mean, they can see the source code, at least, of where the calls to track are
[2126.36 → 2130.28] happening in Google Analytics or calls off to Google Analytics. But it'd be really cool to have,
[2130.44 → 2135.30] you know, publicly available the results of that data, because then you can have people draw other
[2135.30 → 2141.20] insights or just enjoy it. But even, yeah, remove that fear of what you all are tracking.
[2141.84 → 2146.88] Well, and the thing that some people have asked already, actually, about that is people who are
[2146.88 → 2151.58] scientists who've been asking, you know, if it would be really useful for me, as I've, you know,
[2151.58 → 2155.96] worked on some piece of software as part of my PhD, to be able to put in a paper, well,
[2156.32 → 2159.90] this has actually been used this many times or installed this many times or whatever,
[2159.90 → 2163.72] because that gives some, I don't know, I'm not a scientist, but that gives, I think,
[2163.72 → 2169.74] some sort of weighting or a sense of importance to the kind of work they've been doing, which I can
[2169.74 → 2170.00] understand.
[2170.54 → 2175.88] Or people who are putting the work in to maintain specific formulas or formulae, as you guys
[2175.88 → 2176.76] say to call them.
[2177.16 → 2177.30] Yeah.
[2177.50 → 2181.14] To know, like, is this worth my effort? Like, oh, me and six other people are using it.
[2181.68 → 2185.72] And I got six complaints, you know, that's, that's just the total, that's all the users,
[2185.72 → 2189.14] as opposed to, oh, this has, you know, a lot of people are really drawing value from this,
[2189.18 → 2190.30] I'm going to continue to maintain it.
[2190.62 → 2191.52] Yeah, yeah, exactly.
[2191.52 → 2196.20] Well, one thing you mentioned is updating. In light of those stats, you know, not everybody's
[2196.20 → 2201.48] on 1.0, but just moving on to the some of the other new features is you guys now have
[2201.48 → 2203.60] auto updating built in. Is that correct?
[2204.10 → 2208.84] Yeah, we do. So now if you run through install, it will check for updates in the backgrounds,
[2208.96 → 2213.66] I think by default, once a minute. And when I say in the background, I don't actually mean
[2213.66 → 2218.18] in the background. I mean, before you run the command, it will check for updates. And that was
[2218.18 → 2222.06] actually, that's one of my favourite features in there, because it was a really fun exercise
[2222.06 → 2228.32] for me in kind of performance benchmarking, like on kind of the full stack. Because I,
[2228.74 → 2232.92] this is something I had a while ago is I was like, okay, well, I want to be able to run auto
[2232.92 → 2238.66] updates, because a lot of the time when things break, we tend to get a fairly long tail of
[2238.66 → 2243.14] people who haven't run the update who file the issue for something which is fixed, you know,
[2243.14 → 2248.08] a day, a week, sometimes even a month, a month earlier. And I've always kind of wanted to have
[2248.08 → 2254.18] that. But then the updater at that time took probably about 15 to 30 seconds, depending on
[2254.18 → 2259.78] where you are in the world and stuff like that sort of minimum to do that. And that was kind of
[2259.78 → 2266.10] frustrated me. So in the end, I kind of poured some time into that and tried to make it worked on a few
[2266.10 → 2271.72] things that made that really fast. And one thing was kind of more reliable, I guess. So one thing was
[2271.72 → 2279.14] kind of moving some of the auto update stuff from Ruby into bash, more just because Ruby gets more
[2279.14 → 2284.00] upset when you modify its own code underneath it than bash does, or at least it's easier to work
[2284.00 → 2290.00] around that in bash. The other thing that was a kind of fun, but completely overkill thing was
[2290.00 → 2296.66] with me being lucky enough to work GitHub, I noticed that the slowest thing by far was doing a git fetch
[2296.66 → 2301.04] on like a massive repository like Homebrew that's had huge numbers of pull requests and stuff like that.
[2301.04 → 2307.12] So that git fetch, just like a no op git fetch when there's nothing to fetch was actually pretty
[2307.12 → 2317.00] slow. And so I was at that time on the GitHub API team. So in my kind of weekend, I figured I'd go and
[2317.00 → 2322.22] see if I could play around and figure out a way to make that faster. And because we have like a
[2322.22 → 2329.30] cache API layer, and there's like an API call you can use to get the kind of latest state of a branch.
[2329.30 → 2335.30] So I kind of tweaked that a little bit, I made it so you can pass in the SHA one from git as the
[2335.30 → 2340.34] e-tag to that. So you get three or four unmodified if nothing has changed, and therefore not use up your
[2340.34 → 2345.86] rate limit and allow us at GitHub to kind of deliver that from the cache. And basically, yeah, as a result,
[2346.58 → 2355.16] like flip that git fetch operation to just being an HTTP call. And that's like way, way, way faster. And for both GitHub
[2355.16 → 2360.16] to process and for homebrew to process. So as a result, I was able to kind of play around with that
[2360.16 → 2367.16] and do some parallelization and stuff like that. And now it's generally kind of under a second, or around
[2367.16 → 2373.16] about a second, and down from kind of 30 when you are kind of doing an auto update. So that seemed like a
[2373.16 → 2379.40] reasonable amount of time for people to kind of spend on every call, considering, you know, if you
[2379.40 → 2383.72] do a brew install, the compilation and extraction time are going to be significantly longer than that
[2383.72 → 2384.16] anyway.
[2384.16 → 2388.16] Life is good when you control both sides of the API, right?
[2388.16 → 2394.88] Yeah, no, it's much, it's much, much easier. And when you have that, like, it's, it's nice to be
[2394.88 → 2399.92] able to kind of jump in there and play around. But I think even if I didn't control that side of things,
[2399.92 → 2403.68] there, there might have been ways I could have played around and made it a little bit faster.
[2403.68 → 2407.68] But no, it's certainly easier, as you say, when you have that. And when you have very smart coworkers who
[2408.32 → 2413.12] I can kind of bump it off, you kind of actually work on git itself as their, their day job,
[2413.12 → 2417.36] and then be like, okay, am I, I being stupid here? Like why this is slow and all this type of thing.
[2417.36 → 2421.20] And then, and then discussing an approach with them, that was kind of pretty fun.
[2421.20 → 2428.08] So just one aspect of user experience, I think focusing on the speed is, is key there. And in
[2428.08 → 2433.52] fact, Adam and I were kind of lamenting a little bit before the call about certain bits of software
[2433.52 → 2439.12] that do auto update, but you don't run them enough for them to ever be updated. So my example,
[2439.12 → 2445.04] for me at least is Firefox, which I don't use on a regular basis, but I do use if I'm doing browser
[2445.04 → 2449.36] testing or for one-off purposes. And it seems like, I think they may do it in the background
[2449.36 → 2452.88] now, but it used to be every time I launched Firefox, it would say, Hey, we have an update,
[2452.88 → 2457.92] update. And it seems like brew is for me, at least I use it all, all the time. So I don't have
[2457.92 → 2461.52] that issue, but it could be the kind of thing where you don't launch it very often. And then it feels
[2461.52 → 2467.84] like every time you're running the brew command is updating. Sometimes, sometimes like, I just
[2467.84 → 2471.84] got to get this thing installed. I need this command so I can fix something that's on fire.
[2473.04 → 2480.08] So speed, I think is important to fix that is if it happens real fast, no big deal. But in light of
[2480.08 → 2484.08] there is a new update, does it automatically run that for you? Or does it prompt you where you can
[2484.08 → 2488.96] say not right now? Have you thought through those kinds of things? Well, so it, so we have,
[2488.96 → 2493.44] in terms of our commands, we have a separation between update and upgrade. So update is basically
[2493.44 → 2498.72] get all the definitions in the package manager, have the latest version, and then upgrade is like,
[2498.72 → 2502.88] you know, install open SSL 1.1 instead of 1.0. Right.
[2502.88 → 2509.60] And so, yeah, so we don't auto upgrade. And sure, but I'm referring to like, say I run brew install
[2509.60 → 2514.72] JR, because I need to parse some, some JSON on like man line real fast. Yeah. And you don't want to wait
[2514.72 → 2518.64] the couple of seconds for the update. Yeah. I mean, that, that's one of those things that
[2518.64 → 2525.20] we, like we kind of considered, but in the end, the kind of support burden for that is,
[2525.76 → 2532.16] it's worth it for us. Like you would not believe how many, like annoying, because again, I don't
[2532.16 → 2537.28] think we mind that much about the, the issue count or whatever, or the number of issues people are
[2537.28 → 2542.40] filing. But what's the worst thing is when you get the same issue again and again and again, and the
[2542.40 → 2547.36] response to fix it is the same thing again and again and again. And like my attitude is always
[2547.36 → 2553.28] try and automate myself out of the job. So like if it's the same command, we're having to tell people
[2553.28 → 2557.60] to run like every single time. And if people are still not running that command, then it's like,
[2557.60 → 2559.52] well, we're going to just run that command for you.
[2559.52 → 2565.76] I think it's definitely the I think the pain is alleviated because of the small payload size of
[2565.76 → 2570.80] right. Updating homebrew. Whereas in the like, for example, with my Firefox example,
[2570.80 → 2576.56] you got to download like a 60 megabyte file or whatever it is. Um, so it's more of like, okay,
[2576.56 → 2582.68] I'm going to sit and wait. But in this case, even when you do have, I run brew installed JR, and I'm,
[2582.80 → 2587.34] you know, I'm a dot release behind, we're talking like seconds to get that thing upgraded. Is that right?
[2587.34 → 2591.34] So that's the point where it's doing the, the auto updating is like when you're doing a brew install,
[2591.34 → 2592.62] not just brew update.
[2593.18 → 2599.34] Yeah. Yeah. So, uh, we have, so basically a brew install now does a brew update in the background.
[2599.66 → 2603.74] Okay. I'm, I'm tracking now. I heard you said before, but I wasn't sure what,
[2603.74 → 2606.98] under which command it was doing in the background. You said once per minute,
[2607.58 → 2609.22] something like, well, if you do brew update.
[2609.66 → 2614.06] Yeah. So if you do brew update, then it will basically skip them or the next skip,
[2614.18 → 2616.78] even looking for the next minute. And then I, as I say,
[2616.78 → 2621.12] yeah, it's optimized for the no op case where if you don't actually have anything to update there,
[2621.12 → 2623.58] then it will just ignore it.
[2623.58 → 2626.40] And she said, it's just definitions, right? So it's just pulling back,
[2626.48 → 2628.68] like the latest things are available to brew install.
[2629.22 → 2632.58] Yep. Yep, exactly. And invariably that's,
[2633.06 → 2637.02] I think the other thing that's kind of tricky from a package manager perspective is that
[2637.02 → 2643.70] you have this conflict between what people want and, uh, what people need where,
[2643.70 → 2648.88] you know, humans myself included are lazy. And if you can avoid upgrading something now,
[2648.88 → 2651.72] and if you can kind of put it off until tomorrow, like most people will,
[2652.18 → 2657.00] but then there's some of this stuff that it's like, well, actually that's a huge deal with
[2657.00 → 2662.30] security. So you need to update this now. And if you don't want to update this now,
[2662.50 → 2665.98] then we've got to sort of like nudge you in the right direction so that you do that
[2665.98 → 2670.50] so that your machine doesn't get owned. And then it's, we're at least partly responsible.
[2670.50 → 2676.06] And as I say, it's that kind of weird conflict that you have where sometimes you've got to just
[2676.06 → 2681.70] force people to do things or not implement things that they want you to. Like a recent thing that
[2681.70 → 2686.66] could have made the 1.0 release notes, but actually I kind of pruned it from there is we don't,
[2686.74 → 2692.66] we used to let you run homebrew as root. Um, and like, you know, you would have to completely
[2692.66 → 2696.78] change all the ownership. So it was root and everything like that to almost emphasize that,
[2696.78 → 2701.54] look, I'm really sure. But in the end, we're just like, you know what, there's a use case for this,
[2701.62 → 2707.60] but it's just a terrible idea because if you run homebrew as root, like we don't,
[2707.72 → 2711.30] like other package managers that run as root, they drop privileges because that's what they're
[2711.30 → 2715.48] designed. So they will run as root. And then when it actually comes to doing installation or whatever,
[2715.56 → 2720.00] they'll go and just be like, okay, I'm a user now with no privileges, so I can't do stuff.
[2720.14 → 2724.12] Whereas in homebrew, because the vast majority of our users are not running as root,
[2724.12 → 2728.24] we haven't implemented that, and we don't have the motivation to implement that. So if you run
[2728.24 → 2733.34] homebrew as root, like a make file can now literally change any file on your entire system.
[2734.22 → 2741.52] And so like, that's bad. And we added a sandbox that means that obviously you're running as the
[2741.52 → 2746.64] same user. And then we stopped the build process from being able to write to arbitrary locations
[2746.64 → 2750.94] in your system. But again, to make it even worse, sandbox broke when you were the root user.
[2750.94 → 2755.30] So we had to disable the sandbox for the root user. And at that point, we were like, okay,
[2755.34 → 2761.90] this is just way too dangerous. And unfortunately, we need to make the call that we know better than
[2761.90 → 2767.36] other people do by assessing the risk in this situation. Because we've seen what happens when
[2767.36 → 2771.66] there's a make bar log that starts trying to just delete random files of your system. And users maybe
[2771.66 → 2776.60] haven't seen that. And when that happens, and they destroy everything, and they don't have any backups,
[2776.60 → 2781.94] they may not hold us responsible, but they kind of should if we have seen that coming,
[2781.94 → 2786.10] and we've not addressed it properly. So yeah, sometimes.
[2786.90 → 2791.16] Well, while we're talking about technical changes, well, let's hit on one more, and then we'll take
[2791.16 → 2797.86] our next break, which are you've changed the default location of the homebrew repository. In fact,
[2797.90 → 2804.92] I believe as you upgrade it, we'll move it for you from user local to subdirectory user local homebrew.
[2804.92 → 2809.46] Can you speak to that change? And then the implications of what all entails?
[2810.26 → 2813.80] So there's always been a bit of people have had a bit of a love hate relationship with homebrew
[2813.80 → 2819.98] being installed in user local. And the main reason homebrew is there is that originally,
[2820.12 → 2825.42] at least was because that's in your compiler and a bunch of other Unity tools, they look there by
[2825.42 → 2829.62] default. So that basically means with Ruby gems and various other things, if you have a library in
[2829.62 → 2834.56] there and user local lib, user local bin, then they will look in there. And you don't need to
[2834.56 → 2840.18] manually specify your location. So that works quite nicely for most people. And again, when
[2840.18 → 2845.04] homebrew got started, that's something that helped is, again, adding to this sort of zero
[2845.04 → 2850.08] configuration approach that homebrew is taking on things. So the problem with this is time goes on
[2850.08 → 2854.68] and we say in our repo, like, oh, yeah, we want to add a README, we want to add a code of conduct,
[2854.68 → 2862.56] we want to, you know, add a bunch of stuff in our repository. The problem with that is all that
[2862.56 → 2868.14] stuff ends up then getting dumped in user local. And then people like, okay, well, user local bin get,
[2868.40 → 2875.22] okay, I'm fine with that. User local, like, readme.md, that feels kind of weird to me when there's other
[2875.22 → 2879.72] stuff in user local. And people, people were getting annoyed with that. And I kind of understand that.
[2879.72 → 2885.94] So it was actually one of our users came out with something which was kind of, I mean, frankly,
[2886.04 → 2892.88] a hack that had never really been patched, which was that homebrews, by default, homebrews,
[2893.14 → 2897.84] what we call the prefix, which is user local. And that's where all your files get sim linked into,
[2897.94 → 2903.96] like user local bin, etc, as I was saying before. And that has actually remained unchanged. And that was
[2903.96 → 2907.84] the same as where we had the repository previously. But there was a hack you could do,
[2907.84 → 2912.38] where you could install the repository in a different case, in a different place and sim link
[2912.38 → 2917.36] it funnily. And then it would put the repositories files or the README file, code of conduct,
[2917.64 → 2923.20] documentation, whatever, in a different path that you specify of your choosing. And then user local
[2923.20 → 2928.22] would contain just the kind of sim links and the installation packages. And the nice thing about that
[2928.22 → 2934.26] is that user local, you may have seen the user local seller directory. Now that's where all the
[2934.26 → 2937.62] binaries are actually stored. And then there's sim linked into various different locations.
[2937.84 → 2942.38] The problem is, if we decided to move that, we would have to rebuild all our binary packages
[2942.38 → 2948.64] for all of our OSX versions. And that's basically a massive pain that we don't want to kind of have
[2948.64 → 2954.72] to go through. And so this kind of was this hack that, like this person suggested, I kind of tried
[2954.72 → 2958.24] out on my own machine for a few weeks, and it was completely flawless. Everything just worked
[2958.24 → 2965.32] absolutely perfectly. And that allows us now after the move, to have all our binary packages be the
[2965.32 → 2969.20] same, still have all the kind of the compiler search paths and stuff like that be fine.
[2969.20 → 2974.80] But now we can move stuff around in our repository on GitHub. You know, if we want to put a readme.md
[2974.80 → 2979.88] file or contributing.md file or change those file names or whatever, they can all now live
[2979.88 → 2986.32] inside user local homebrew instead. And we don't need to worry about kind of junking up people's user
[2986.32 → 2993.58] local. Another final benefit from that is, so we always, we would tell people to take ownership of user
[2993.58 → 3000.12] local and just recursively CHO on that. So you can always write anywhere in there. The problem is,
[3000.12 → 3008.48] is Apple's OSX installers, various other tools would reset that. Yeah, every time. So every time
[3008.48 → 3013.62] there's a new version of OSX that comes out, it would be that kind of reset process. And it was a
[3013.62 → 3017.92] massive pain for a lot of people. So now what we do instead is we create the root level directories
[3017.92 → 3022.60] and user local, get people to CHO on them instead, which our installer does by default.
[3022.88 → 3026.24] And then you just have those root level directories, which kind of stick there.
[3026.96 → 3031.14] And anything else can dump files and user local can change the ownership of user local and,
[3031.18 → 3036.78] and all that good stuff. And that doesn't affect us anymore. So again, that's another example of
[3036.78 → 3042.06] somewhere where it's massively cut down on a bunch of these issues. We would just see again,
[3042.06 → 3046.14] again, on every arrow search release. So yeah, it's been great. Or macOS.
[3046.54 → 3048.54] You've actually been bitten by that book once before.
[3049.02 → 3053.52] Yeah. Yeah. I've been bitten by that one several times before. I forget that it happens and then
[3053.52 → 3055.16] it happens and then everything explodes.
[3055.68 → 3060.60] I just upgraded at 1.0 yesterday. And as part of the upgrade, because I, I upgraded to Sierra
[3060.60 → 3066.56] last week and I just did the upgrade to homebrew 1.0 yesterday. And I had to change ownership
[3066.56 → 3071.06] on user local because homebrew had set it back to, was it root and wheel or something like that?
[3071.06 → 3073.02] So yeah, I can see that happening to everybody.
[3073.36 → 3077.76] Yeah, exactly. And then nicely now we, after the migration, we then tell people, okay,
[3077.76 → 3081.38] you can actually now change this back. And then that's now the last time. So when
[3081.38 → 3088.16] Sierra plus one, I'm still hoping for macOS sea lion to come out, but when that comes out or
[3088.16 → 3092.86] whatever, then yeah, hopefully these permission issues will just be gone for good at that point,
[3093.04 → 3094.30] which will be lovely.
[3094.64 → 3100.46] That's funny. As we're talking through all this, the details, I'm, I'm just reflecting on
[3100.46 → 3105.34] earlier in the show when you said that you, uh, that you do this homebrew stuff, as you said,
[3105.34 → 3109.18] in the times whenever like you're running a test suite, and it takes five minutes or something like
[3109.18 → 3113.34] that. Like I'm just reflecting on all this detail and all this complexity and all this community and
[3113.34 → 3118.00] all this, you know, how important homebrew is to so many developers out there, how you and others
[3118.00 → 3120.66] do this in your spare time. And that's just crazy to me. I mean,
[3120.66 → 3125.18] yeah. So, I mean, I'd say kind of here and there time, but yeah, I mean, in the run up to 1.0,
[3125.18 → 3131.04] I'd sort of decided I want to ship it all in a roundabout, the Sierra release. Um, so yeah. So
[3131.04 → 3137.50] in the two weeks before that, like I was just like doing pretty much every, every evening and weekend,
[3137.50 → 3142.54] like pretty much all evening and weekend. Like I, I think there was, you know, we were getting to
[3142.54 → 3148.26] the point where my, uh, my dog and wife would have like not tolerated any further.
[3148.90 → 3152.72] As we know, you're a dog lover too. We can hear your pups in the background there for a second or
[3152.72 → 3157.36] two. So you got a little cameo on the show. Yeah. Yeah. No, I do love my dog. She's pretty
[3157.36 → 3161.82] great. And she's in my GitHub profile picture as well. So. Well, cool. Let's, uh, let's pause there.
[3161.82 → 3165.98] Then when we come back, we got lots of, lots of other things to talk about. Software Freedom Conservancy,
[3166.26 → 3170.72] the new community sites, some other things happening, uh, more community growth and maybe even
[3170.72 → 3175.64] more ways that the community can step in and support homebrew and, uh, ship their own formula
[3175.64 → 3180.12] or formulae as they, as you might say, or have changed the way you say it. So let's pause here.
[3180.36 → 3180.84] We'll be right back.
[3183.72 → 3188.68] Linde is our cloud server of choice. Get up and running in seconds with your choice of Linux
[3188.68 → 3196.18] distro resources and no location, SSD storage, 40 gigabit network, Intel E5 processors. Use the
[3196.18 → 3200.68] promo code change log 20 for a $20 credit, two months free. One of the
[3200.68 → 3206.72] fastest, most efficient SSD cloud servers is what we're building our new CMS on. We love Linde.
[3206.72 → 3211.54] We think you love them too. Again, use the code change log 20 for $20 credit. Head to
[3211.54 → 3213.78] linode.com slash change law to get started.
[3219.72 → 3224.14] We're back with Mike McQuaid talking about homebrew and, and Mike around homebrew, there's
[3224.14 → 3230.24] several, uh, terminologies. You got cast, you got tap, you got brew, you've got several things.
[3230.24 → 3233.72] You got formula or formulae. I think that's changed if I'm correct.
[3234.08 → 3234.98] It's plural form.
[3235.36 → 3240.02] It's plural form. Okay. Um, walk us through some of the terminology, you know, do you tap
[3240.02 → 3242.90] a cast? Do you tap a keg? What is it? How does this work?
[3243.34 → 3250.00] Yeah. So I think the terminology is a bit sometimes tenuous in places, and it's not quite, um, all
[3250.00 → 3256.46] adding up, but a tap is effectively what we call a third party repository basically. So
[3256.46 → 3260.74] that, that was initially created. That was one of kind of Max's last big features he worked
[3260.74 → 3267.66] on. And a tap basically allows anyone to be able to have a Git repository, which, well,
[3267.68 → 3271.52] it doesn't actually have to be a Git repository anymore, but a directory with a collection of
[3271.52 → 3277.34] formulae or homebrew extension commands that they can go and say to anyone, okay, like here's
[3277.34 → 3282.66] this one command you can use to install a tap on your machine and then brew update will
[3282.66 → 3286.52] then keep that up to date and brew install will then let you install from any of those
[3286.52 → 3293.36] taps as well. So actually as part, a fun little fact is as when we split our homebrew into the
[3293.36 → 3298.88] two repositories, the formulae became their own tap. So previously you had all the kind
[3298.88 → 3303.92] of central formulae, and then you had taps, but then now actually everywhere that contains
[3303.92 → 3309.32] formulae is always in some sort of tap. Seems like that's a promotion of the tap idea because
[3309.32 → 3315.74] back when I first started using homebrew, like using a third party, uh, repository for formulae was
[3315.74 → 3320.74] kind of like sketch, and you were like, well, if you really have to do this, but now it seems like
[3320.74 → 3324.20] that's very commonplace. Is that a fair characterization?
[3324.96 → 3329.80] Yeah, definitely. I think there's a recognition in that, that a that people are going to want to do
[3329.80 → 3335.14] stuff that we, you know, we don't have the, you know, if you work at a company, you may well want
[3335.14 → 3339.94] to have internal tools, which are installed, um, by homebrew through a tap, but also there's,
[3340.40 → 3344.16] it's helped us with some of the really long tail stuff because now we can say to people,
[3344.16 → 3349.20] if, you know, if you're the only person interested in this, then you can just create your own tap and
[3349.20 → 3353.34] you can keep that up to date. And then if more and more people, particularly now we have analytics
[3353.34 → 3357.94] for some of this stuff. Um, if more and more people use that, then we can consider kind of bring that
[3357.94 → 3363.68] into homebrew itself. And before that we couldn't, not those kinds of private taps are revealed by
[3363.68 → 3367.82] analytics. We're careful to not do that. But within, within the homebrew organization, we have
[3367.82 → 3373.40] several kind of taps, um, for different things. And it lets us as well, kind of subdivide maintainers
[3373.40 → 3377.82] based on things that are interested in. So we have a science tap, a PHP tap, a Python tap.
[3378.14 → 3384.42] And those are not, you know, to install Python, you don't have to tap Python tap, but it provides some
[3384.42 → 3388.76] sort of stuff, which is deeper into that ecosystem and stuff, which we wouldn't include in our main
[3388.76 → 3394.28] repository and can kind of find a home in some of these taps instead. And these taps can be run
[3394.28 → 3398.82] independently and a little bit looser on some of the restrictions that we kind of have to
[3398.82 → 3400.64] kind of keep the core working effectively.
[3401.40 → 3403.50] Tell us about cask. What's cask?
[3403.94 → 3409.04] So, yeah, so that was quite exciting. So brew cask was originally a thing made, I can't remember what year
[3409.04 → 3414.22] it was originally, but someone basically really liked homebrew, but they hated the fact that
[3414.42 → 3417.96] you know, when you install Mac applications, you know, you have to download the zip or the package
[3417.96 → 3423.30] file, the EMG or whatever, and move the file there. And it's, you know, it's almost always the
[3423.30 → 3428.28] same process every time. Uh, and it's like, and I think they were just like, well, why do I have
[3428.28 → 3432.56] to, why can I install my command line software beautifully? But then I had to like physically
[3432.56 → 3438.04] drag and drop a thing with my mouse. And to, that's the that's the sound I make when I do it.
[3438.42 → 3443.60] Exactly. I actually quite like drag control. I kind of missed that a little bit in some ways,
[3443.60 → 3447.62] like the little dragging the icon into the applications folder, and it's all nice and
[3447.62 → 3450.88] pretty. And you can still do it, Mike. No one's stopping you, man. You can still do it.
[3451.38 → 3455.76] Yeah. My, my obsessive desire to script everything is stopping me, unfortunately.
[3457.04 → 3463.14] But yeah, so like they made this brew cask command so that you could do that. You could do brew
[3463.14 → 3469.84] cask install and, you know, Google Chrome, whatever. Um, and we had a summer code student this
[3469.84 → 3477.84] summer, Anastasia, who is a very, very smart Russian student who worked on basically trying
[3477.84 → 3483.20] to unify the two projects. So homebrew cask, they originally were kind of almost extension,
[3483.32 → 3489.64] I think, in just a tap. And we kept, because we didn't provide any sort of official API for them,
[3490.22 → 3494.66] they kept, and they're being broken by our changes. So at the end, they ended up rendering
[3494.66 → 3498.52] a lot of homebrew code, homebrew's code. So in Google's summer of code this summer,
[3499.04 → 3504.56] the student worked on basically re-rendering all this stuff so that they could kind of,
[3504.62 → 3508.72] we could share a lot more code between the two projects and deduplicating between the two
[3508.72 → 3513.26] projects. So we kind of stuff which didn't make sense to have in both, wasn't in both,
[3513.76 → 3518.78] and both in terms of like source codes, but also in terms of things that are installed when they
[3518.78 → 3523.96] both installed identical software that there wasn't a need to have them both. And then finally,
[3524.12 → 3528.90] actually moving all homebrew cask's kind of package manager code into the homebrew package
[3528.90 → 3535.52] manager itself. And so now we have homebrew cask living within homebrew itself. So when you run
[3535.52 → 3540.76] brew cask, now that's part of the homebrew package manager and part of the homebrew's release process
[3540.76 → 3545.42] and stuff like that. And we're able to do stuff like share a lot more code, share maintainers,
[3545.42 → 3549.08] share testing. And that kind of provides some guarantee as well, that we're never going to
[3549.08 → 3554.52] break homebrew cask stuff because our package manager tests are now running all the homebrew
[3554.52 → 3559.36] cask's tests as well. I just did a brew cask list on my machine, and it turns out,
[3559.48 → 3564.38] even though I don't know what cask is, I have used it to install Screen Hero. So I believe someone
[3564.38 → 3569.10] said, yeah, just type this. And I thought, oh, that's really cool. You just type brew cask install
[3569.10 → 3573.56] Screen Hero or whatever the application is and magic happens. And then you forget that you did it and
[3573.56 → 3580.42] all as well. So, and the cool thing that comes on top of a brew tap and brew cask as well is,
[3580.64 → 3584.56] which not many people know about. And I think partly because I've not done a good job at
[3584.56 → 3589.56] describing it is the thing brew bundle. So that lets you have a brew file, kind of like a gem file
[3589.56 → 3597.52] or whatever, in which you specify a list of homebrew packages, cask packages, and actually like taps and
[3597.52 → 3602.94] eventually even like Mac App Store packages as well. And then it will automatically, you can run
[3602.94 → 3606.56] brew bundle, and it will go through that list and install any of the ones that aren't installed.
[3606.92 → 3613.36] And you can also do the reverse where you can kind of dump to a file and then have that as kind of
[3613.36 → 3616.50] almost like a backup of everything you've got installed and all the options they're installed
[3616.50 → 3621.08] with and stuff like that. So that's been really useful for letting people kind of almost import and
[3621.08 → 3627.20] export their configuration, but also for having like a system-wide like installation. So you can have
[3627.20 → 3631.46] one script, which then installs all of your software. But then we've been leaning on that heavily
[3631.46 → 3637.90] started GitHub as well to have that per project. So you can specify a definition of this project
[3637.90 → 3643.44] requires MySQL and Nginx and stuff like that. And there hasn't really been a good way before that
[3643.44 → 3648.52] of kind of defining that. Like often that's just in the documentation, but we can actually have now
[3648.52 → 3654.12] in the brew file. So it will install the correct version of MySQL and then start up a daemon in the
[3654.12 → 3658.46] background on the system if it's not already running. And then that'd be a no-op if that stuff is
[3658.46 → 3662.40] already installed and the daemon's already running. That brew file is really handy for
[3662.40 → 3669.30] descriptors. I've seen that actually, I think in maybe earlier versions of Thought Bot's laptop
[3669.30 → 3673.80] project where they're doing lots of interesting things around. They actually used to support Linux
[3673.80 → 3678.40] and Mac, and now it's just Mac, but it's kind of like their way of setting up a development machine.
[3679.90 → 3684.62] And I'm pretty sure I recall seeing a brew file in that. And that's kind of where I actually
[3684.62 → 3688.94] stumbled upon that and thought that's kind of interesting to see. Like here's a way you can
[3688.94 → 3694.44] just run a lot of brew commands basically. Yeah, yeah, exactly. So it's pretty neat for that.
[3694.60 → 3699.68] And again, being able to standardize on these things, I as self-plug have like a little project
[3699.68 → 3706.64] called Strap that we again use inside of GitHub that is kind of a system bootstrap type thing.
[3707.22 → 3711.78] And that rather than, it's a different approach to Thought Bot laptop because it's not opinionated
[3711.78 → 3716.36] at all about what stuff should be installed. So if you have a brew file in your.files directory,
[3716.54 → 3721.38] it will check out your.files directory and run the brew file in there. So every person can have
[3721.38 → 3727.78] their own almost custom system bootstrap script from that perspective and still yet have like a
[3727.78 → 3732.32] sort of centralized way of running that for everyone. So it's been quite neat. But yeah,
[3732.38 → 3736.54] my long-term dream, if I ever get around to it, which I probably never will, is to try and
[3736.54 → 3741.84] work with a few other people and see if we can get some sort of brew file definition format,
[3742.12 → 3748.18] which a bunch of package managers support so that we can have a way of, you can declare in a project
[3748.18 → 3754.96] that, okay, I want to install my, this project needs my SQL installed, LibXML2, whatever,
[3755.44 → 3760.98] like the kind of native package manager dependencies. And that file can then be read by, you know,
[3760.98 → 3766.62] whether you're on Fedora or NuGet on Windows, maybe even, or Homebrew or Mac ports and have
[3766.62 → 3771.18] a single file, which could be used to kind of shared metadata across all these package managers.
[3771.44 → 3774.46] That's kind of a little dream of mine that may or may not happen one day.
[3775.14 → 3780.38] That'll be cool. I think RVM had a similar dream. Isn't that right, Adam? For RVM3,
[3780.50 → 3783.92] I'm not sure if you ever got there, but it was kind of like beyond Ruby versioning. It was like
[3783.92 → 3789.52] versioning for everything. You could just list all your, you know, this requires Postgres,
[3789.52 → 3795.96] this requires Regis, for instance, but definitely a dream to get everybody involved because that's
[3795.96 → 3800.72] a lot of different software projects that would need to come on board. And if I couldn't call it
[3800.72 → 3805.82] brew file, it'd have to be like package file or. Yeah, obviously. Yeah. I'll submit the term,
[3806.02 → 3812.62] you should call it dependencies. Yeah. Yeah. That seems fine. People tend to like that one.
[3813.06 → 3817.42] Might have to have some slight pun on the name just because I'm British and that's,
[3817.42 → 3822.28] you know, that's what happens to us. So tell us about keg.
[3822.86 → 3830.52] So kegs are when, so that's one of the hardest metaphors in that even the homebrew maintainers
[3830.52 → 3838.08] probably disagree on what a keg actually is. But a keg is technically, that's the directory when you
[3838.08 → 3845.92] install homebrew a package in it, the directories that uses the prefix. So this is going to get a bit
[3845.92 → 3851.10] package manager, naval gaze. But the way most package managers work is they have a unified
[3851.10 → 3856.94] prefix. And what I mean by that is when you run configure or make install or whatever, say
[3856.94 → 3864.38] on two pieces of software, the prefix you set is say user local. And then what it does is it
[3864.38 → 3868.56] chucks binaries and user local bin, it chucks libraries and user local lib, et cetera. And that's
[3868.56 → 3870.76] the general way most package managers work.
[3870.76 → 3876.80] So what homebrew does, which was actually aped off by Max's own admission off another package
[3876.80 → 3881.68] manager whose name escapes me off the top of my head at the moment. But basically having every
[3881.68 → 3888.00] single package be in its own prefix by package and by version. So if you go into user local seller,
[3888.38 → 3892.56] you'll see you have user local seller and then the names of all your packages. So user local seller
[3892.56 → 3897.60] and then a subdirectory called get and then a subdirectory of whatever version of get is installed.
[3897.60 → 3902.80] And then within that, then you have been, lib, all these other directories. And then what homebrew
[3902.80 → 3908.96] does is we then sim link the contents of those subdirectories back into user local bin. So in user
[3908.96 → 3916.64] local bin get, that's not actually the get binary. That's a sim link to user local seller get version
[3916.64 → 3925.32] bin get. And basically the benefit for that is it lets you stop software from stomping on each other.
[3925.32 → 3931.18] So you can have software installed side by side, which installs conflicting things. And, but they both,
[3931.24 → 3937.10] they just both can't be linked at the same time rather than being like, Oh, okay. We actually just
[3937.10 → 3939.80] can't install these two things in the package manager at the same time.
[3940.12 → 3945.02] I might actually suggest after this that, uh, that there actually be some sort of like glossary for
[3945.02 → 3950.66] homebrew because you'll have so many terms and I'd forgotten about seller. And we actually asked
[3950.66 → 3954.82] about keg as a joke because I, I didn't think it was a real thing. I was hoping you'd laugh, but
[3954.82 → 3961.08] it's actually real. And so our next one is like, tell us about pints, but yeah, pints are not real.
[3961.26 → 3963.30] Well, I mean, they are real, but not in home.
[3963.30 → 3963.84] They're real to me.
[3964.46 → 3969.78] Yeah. Yeah. Um, so yeah, no, I mean, we definitely could do with having a glossary. I mean, why?
[3970.04 → 3975.16] I mean, if anything, it could be an attractor to contributors because it's funny. It's just a new way to like,
[3975.16 → 3979.62] talk about your project and just have fun with what it is, you know?
[3980.26 → 3986.14] Yeah, exactly. I mean, so my, the reason why I, I, I didn't do that originally is my whole thing
[3986.14 → 3991.66] was I wanted to rename everything. So we wouldn't call X kegs anymore. We wouldn't be careful now.
[3992.16 → 3996.30] Why? Exactly. Exactly. And, and that was, you were concerned about the, uh, you know,
[3996.30 → 3997.80] the analytics people getting, yeah.
[3998.38 → 4001.88] This is the real reason he wanted to be lead maintainer. So he could rename all of the
[4001.88 → 4006.42] would you just, would you come up with a brand-new analogy or would you just remove all analogies?
[4006.42 → 4011.08] I mean, I think, yeah, we just call things packages. If there's an established name already,
[4011.24 → 4016.68] call them that packages, prefix, whatever. But I mean, I think the argument, which I,
[4016.72 → 4020.88] I probably mostly agree with at this point that pretty much every other person in the world said
[4020.88 → 4024.66] is that, okay, you might make things slightly easier for new users, but at this point,
[4024.70 → 4028.38] homebrew is at the point where you're probably going to confuse a lot of people who've learned
[4028.38 → 4034.26] the existing terminology more than you're going to help, you know, a new user, a code economy or
[4034.26 → 4038.70] whatever, understand this stuff. And yeah. And as you say, probably the best middle ground is just
[4038.70 → 4040.72] have a glossary and just define these things.
[4041.24 → 4046.24] I guess it depends though on this change stuff. Now, you know, the, the Asia RME says don't do
[4046.24 → 4054.88] that, but I think if, uh, if the plan was wider adoption and, uh, a greater invitation and if the
[4054.88 → 4060.86] normalizing of the puns, while we all love puns and just the play on words kind of gets played out,
[4060.88 → 4066.64] so to speak, if it was, if reducing that helped invite people and actually contributed to a greater
[4066.64 → 4071.30] project, that might be for it, but it would hurt along the way. I'd cry a little bit.
[4071.90 → 4078.30] Yeah. Yeah. No, I do agree. And I mean, it's, it's maybe whether we can change some of these things
[4078.30 → 4083.68] whilst maintaining other things or whatever, like, you know, we can certainly maintain the kind of beer
[4083.68 → 4088.66] theme and the little nice cute emojis we have and stuff like that whilst maybe renaming some of
[4088.66 → 4095.38] these things. So yeah, it's, it's, it's still a source of debate and torment for us all.
[4096.52 → 4100.56] Adam sounds like he's for it. I'm against it. So there you go. You split us down the middle.
[4100.98 → 4102.52] I'm not exactly for it.
[4102.88 → 4109.58] Embrace the analogy and just it's, it gives, Homebrew has a personality. It has a theme. It's,
[4109.58 → 4116.40] it's actually worked out better than most names in terms of like, they have kegs and casks and taps.
[4116.62 → 4120.68] And I mean, those are things that actually have make some sense. Now, once you get outside of it,
[4120.70 → 4124.74] like, would you say boneyard or graveyard or something, but some things just don't match.
[4124.88 → 4130.80] Then you get mad because you're like, Oh, we can't think of a beer themed boneyard. But along the way,
[4130.80 → 4134.86] I think it's helped massively. And I think it makes it kind of joy in certain ways.
[4134.86 → 4140.42] Yeah. Yeah. And I think that's, you know, I redesigned the website for, with the help from
[4140.42 → 4147.26] an Australian designer, Danielle, whose full name is actually on the website. But yeah, so I think
[4147.26 → 4150.48] that was part of what I was going for a little bit with the redesign as well. Because she came up with
[4150.48 → 4156.48] these great new icons you may have seen, which is just, they feel a lot more playful and kind of fun.
[4156.48 → 4164.60] And like, it's, I feel like that, I love them when I set upon them at first, because it, it just feels
[4164.60 → 4169.74] like that's the vibe of our project is we're trying to have that sort of fun, slightly kind of jovial,
[4169.90 → 4175.16] slightly silly, like, you know, part of that is the fact that, you know, we have prose guidelines and
[4175.16 → 4180.64] in our prose guidelines, we favour British English just because, you know, Max was British. I was,
[4180.76 → 4184.84] and partly just because, I mean, a little part of me, and I think this is more Scottish thing than a
[4184.84 → 4188.28] British thing is I kind of just like being difficult. You know, I'm one of those people
[4188.28 → 4195.20] when I worked with a cute back then as well, uh, when you define colours, that was a cute colour.
[4195.20 → 4202.78] And I would regularly name my cute colours, variables colour with a C O L O U R. And just,
[4202.98 → 4208.20] you know, because I'm a crotchety British person and I, I found it funny to do those type of things.
[4208.20 → 4213.66] So I think part of that kind of groups into homebrew, and we do try and we kind of have to remind
[4213.66 → 4217.62] people sometimes that like, we know some of this stuff's a little bit silly, but that's,
[4218.10 → 4222.76] that's the project. We're not a company. We're not a serious business, and can afford to be a
[4222.76 → 4226.72] little bit more silly, even when maybe sometimes it's a little bit self-destructive because
[4226.72 → 4230.50] that fun is what keeps us working on it, I guess.
[4231.10 → 4235.48] Right. Well, now that you're getting kind of beyond yourself and talking about the community and the
[4235.48 → 4239.74] group of people that are all involved with it, let's, let's change focus. We're getting a little bit
[4239.74 → 4243.28] low on time here, but let's talk about the social side of things in 1.0. And you have
[4243.28 → 4247.18] two, what I would call kind of social announcements or things that have happened at least in light of
[4247.18 → 4252.42] 1.0. And one is the joining of the software freedom conservancy. And the other is a setting
[4252.42 → 4257.60] up of the community discourse. I'm not sure exactly when those things happen, but let's start with
[4257.60 → 4263.08] the software freedom conservancy. Homebrew has joined that. What does that mean for the project?
[4263.62 → 4268.18] Sure. It's one of those things that for open source that you don't really understand until you run
[4268.18 → 4275.60] a big project for a while, but when your project has like no possession effectively, then there's
[4275.60 → 4280.30] not really a need as much for a thing like software freedom conservancy. The problem is when you have,
[4280.38 → 4284.50] we had a Kickstarter a few years ago, which was really great. Let us buy some Mac minis, which
[4284.50 → 4290.70] we use for our CI. And as I get older, thankfully not that old, and I'm a bit of a paranoid person
[4290.70 → 4296.38] anyway. Part of me is like, okay, well, these CI's are in a data centre, like a friend of mine
[4296.38 → 4302.88] runs an ISP in the UK. And we have a bunch of money in a bank account, which again, I have access
[4302.88 → 4306.80] to, but I've given other people the credentials too and stuff like that. What happens if I get hit
[4306.80 → 4312.32] by a car to those servers? What happens when they go down? What happens to the money in that bank
[4312.32 → 4319.18] account? And I just, you know, that stuff gets a little bit more worrying. And it becomes one of
[4319.18 → 4323.38] these things where you think, well, it's actually not very responsible for me just assuming that
[4323.38 → 4329.82] this project will survive my health. And it also means that if I ever did want to, or have to step
[4329.82 → 4335.74] away from the project, then the unwrangling of me from the project would be a lot more difficult.
[4335.74 → 4341.70] And what the software freedom conservancy provides is a legal entity to own these things. And a legal
[4341.70 → 4347.90] entity to, if whoever ever got sued for whatever reason, then the software freedom conservancy would
[4347.90 → 4358.12] defend us. And also on top of that as well, they are a 501c3 or for non-Americans, a nonprofit in the US,
[4358.30 → 4363.78] which makes it a lot easier to accept donations, basically, which are tax-deductible for individuals
[4363.78 → 4370.24] and corporations to provide. So that is not something we've not managed to do a massive amount
[4370.24 → 4374.66] of fundraising yet. That's probably my next big project to try and like lean in on that a bit more.
[4374.66 → 4380.58] And because our recurring monthly revenue is zero, but basically just all those things that kind of
[4380.58 → 4387.18] help provide some more kind of infrastructure and architecture around the kind of the governance
[4387.18 → 4389.50] and running of the project.
[4390.54 → 4395.78] I'm surprised to see or to hear that, uh, that it's zero, like there are no contributions,
[4395.78 → 4400.94] there are no donations. I mean, I mean, that's, we're running low on time. So this is harder to,
[4400.94 → 4407.44] to kind of like tap into, to keep using our terms, but, uh, um, it just surprises me that it's,
[4407.56 → 4412.06] that homebrew is used by so many and depended upon by so many. I mean, I don't know a developer,
[4412.20 → 4417.96] that many developers out there that aren't developing at least on a Mac, uh, more often Linux,
[4418.06 → 4424.34] but, uh, not as often on Windows, although it's becoming more and more popular with Ubuntu's
[4424.34 → 4428.78] announcement of bash and Microsoft and all that good stuff, but I'm just surprised. Wow.
[4428.78 → 4434.58] Yeah. Yeah. So, I mean, part of that, you know, we're coming to personal beliefs and stuff, but,
[4434.88 → 4441.10] you know, my whole thing is I, I don't feel happy spending money on a recurring basis until I have
[4441.10 → 4445.90] money coming in on a recurring basis in both my personal life and with homebrew. So it restricts
[4445.90 → 4448.96] the stuff we can do. There are certain things that it's like, you know, I would love to just be able
[4448.96 → 4454.46] to spin up an AWS instance to run that, but we don't have the money, so we can't afford to do that.
[4454.46 → 4461.62] And yeah, it is a bit of a pain. Um, and it's not hit us that adversely yet, but as I say,
[4461.66 → 4466.74] on the flip side, we've not ever really beyond the Kickstarter tried to do decent fundraising for
[4466.74 → 4470.72] that. And that's something I do want to, you know, personally do in future.
[4471.50 → 4475.62] Well, that's somewhere we can help you play a role a little bit. I mean, I know that Jared and I,
[4475.74 → 4481.40] we both, uh, have some passions around that and, you know, we can always talk to you outside of this,
[4481.40 → 4486.58] the context of the show to, to help you on that front, to give us, you know, collaborate in that
[4486.58 → 4490.94] front a little bit. And that's something I think we have some future ideas around nothing that's
[4490.94 → 4496.34] exactly solid, but definitely some passion. And anytime we hear of something like homebrew,
[4496.86 → 4501.48] having zero recurring revenue to do even stickers, you know, anything that's like community outreach,
[4501.52 → 4506.14] not so much like just have money, you know, that to have money, but you know, to have money to do
[4506.14 → 4511.82] things that are, you know, community related or growth related or, you know, outreach or anything,
[4511.94 → 4517.40] anything whatsoever. You can't sponsor one of the maintainers going to a talk because you just have,
[4517.54 → 4522.12] you know, you have no funds to doing that stuff. It's, it's very limiting. And I think that there's
[4522.12 → 4526.34] so many people out there using it. There's got to be some way you can bring in at least a buck a user
[4526.34 → 4527.94] and that'd be a lot. And I mean,
[4528.06 → 4532.48] Yep. Well, let's cover real quick, even though we're real short on time. So give us the, uh,
[4532.48 → 4537.44] the information on the community discourse site and the purpose and the site for that.
[4537.88 → 4543.22] Yeah. So that's something we shipped that I think on the same day as 1.0. And it's basically just
[4543.22 → 4547.98] another way of communicating on homebrew is something that the mailing list, we've got a
[4547.98 → 4552.28] mailing list, we've got an IRC channel, we've got the issue tracker and like, none of them are quite,
[4552.28 → 4558.78] you know, they all feel slightly formal in their own ways. And I think that the discourse has been
[4558.78 → 4563.70] kind of great since it started actually of just allowing people a little bit more of a kind of
[4563.70 → 4568.90] free form place to talk, to kind of post about issues in a little bit of a looser way and people
[4568.90 → 4572.74] to be able to help each other as well. That's the nice, it seems to be building an expectation there,
[4572.76 → 4576.88] which is nice, which is that it's not just the maintainers who are kind of jumping in and kind
[4576.88 → 4581.58] of helping people there and a bit more of a kind of discussion and stuff like that. And yeah,
[4581.58 → 4582.28] it's been good.
[4582.28 → 4587.10] One more thing I heard you mention earlier, but I'm just curious what the tie-in is together.
[4587.10 → 4591.80] Because I see in the footer, its Linux Brew is maintained by Linux Brew, but earlier you
[4591.80 → 4596.80] mentioned Linux Brew. It also says as the homebrew package manager for Linux, is there an affiliation
[4596.80 → 4601.34] there? Is there, I know one of the maintainers crosses over at least it was, what's the relationship
[4601.34 → 4603.08] there? Just curious in closing.
[4603.76 → 4610.76] So I think originally Linux Brew was like just a fork. And then we kind of created that and they,
[4610.76 → 4618.12] they just kind of had a bunch of patches on top of homebrew. But then with 1.0, like we have a kind
[4618.12 → 4625.28] of what I call a generic backend, which is a backend that doesn't assume anything OSX or Linux centric
[4625.28 → 4632.44] and kind of, kind of run the tests and run and install on, on Linux and Mac. And so now that we have
[4632.44 → 4640.20] that backend, we're trying to do more porting to try and get things into, from Linux Brew's brew kind of
[4640.20 → 4645.58] package manager fork into homebrew itself. And then hopefully maybe a 1.1 or whatever, we'll have a
[4645.58 → 4652.82] point where Linux Brew can go away entirely. And we can run that entirely off homebrew's brew and we
[4652.82 → 4657.52] can have a unified package manager that works on, on OSX and on Linux.
[4657.52 → 4662.64] Nice. Good stuff. Is there anything we missed in this condo? Jared and I had a quite of a list to
[4662.64 → 4666.00] talk through pretty much just based around your 1.0 announcement, but is there anything we missed
[4666.00 → 4670.12] that you wanted to make sure we talked about? I don't think so. I think that that was kind of
[4670.12 → 4675.62] everything I wanted to talk about. And I looked at your little notes about the common questions at
[4675.62 → 4679.32] the end of the show. I'm not sure if we were doing them or not, but I think we've touched on all of,
[4679.56 → 4684.36] almost all of them anyway. So. Well, there's one we want to camp out on, which is essentially a
[4684.36 → 4689.46] great invitation from you and the other maintainers of homebrew to the community, you know, so it,
[4689.72 → 4694.56] and there are lots of listeners of this show from all walks of open source, all walks of developer life.
[4694.56 → 4700.28] So if you were putting out a widespread invitation to those who could step into homebrew and help out
[4700.28 → 4705.36] in various ways, what would those ways be? Yeah, that's a great question. I think basically
[4705.36 → 4711.00] just getting involved at all is great. We have a thing in our homebrew brew README about the easiest
[4711.00 → 4716.60] ways to get involved, which is basically we have a an audit tool for kind of running through things
[4716.60 → 4721.44] and seeing if there's any little violations and of our kind of style. And that's a great way to get
[4721.44 → 4726.18] started and get kind of familiar with our workflow. But I think the main thing I would just say is
[4726.18 → 4731.16] anyone who's sort of in the wider homebrew community is just be nice to each other. I think open source,
[4731.42 → 4736.96] as I kind of touched upon a little bit earlier, has a problem with retaining and welcoming people,
[4737.12 → 4742.26] particularly people from more diverse backgrounds than it's historically been. And that's something I
[4742.26 → 4747.60] feel like everyone can do, whether it's on homebrew or on any project to kind of make the open source
[4747.60 → 4753.82] ecosystem a better place, is tried and just be nice, be friendly, be helpful, be kind to people
[4753.82 → 4758.82] in homebrew and on any open source project, because that's the way we're going to grow this
[4758.82 → 4762.98] community. And that's the way we're all going to make better software together. Because when you
[4762.98 → 4767.08] don't have those things, people stop working on things like homebrew. When you don't have those
[4767.08 → 4770.48] things, people don't want to work on open source. And that hurts us all really.
[4770.48 → 4776.88] I need kind of like a universal mini so or mini so. What is it, Jared? For Matt's is nice. We are
[4776.88 → 4781.46] nice. Can almost be like to maintain our maintainers are nice. We are a nice kind of thing. You know,
[4781.48 → 4786.44] it's just universal mini swan. That's what it is. Yeah. No, I like that. That's nice.
[4786.88 → 4792.94] No, I mean, I think that every, you know, sure, everyone says they're nice. And it's a variation of
[4792.94 → 4797.34] nice. But, you know, maybe they're not nice. I don't know. Maybe there's a project out there
[4797.34 → 4801.84] that's just like led by somebody who's a complete jerk or not a very nice person. And so,
[4801.84 → 4807.94] their community is not very nice. But I think when you look at the leadership of homebrew over
[4807.94 → 4812.10] the years, you know, starting out with Max and the leadership that stepped up over these years,
[4812.60 → 4816.22] you've all been very nice. And there's no reason not to be nice back.
[4816.78 → 4822.26] Yeah, well, we do try to be. And I think that the thing I think that's important to remember is
[4822.26 → 4827.28] people, again, when you're saying everyone kind of thinks they're nice, is you're as nice
[4827.28 → 4833.28] as the way you treat the person you're angriest with, the person you're most disgusted with,
[4833.36 → 4837.68] whatever. Like it's not when it's dealing your day to day. It's when you're furious or
[4837.68 → 4843.86] frustrated or disappointed or confused or whatever like that. Your behaviour in that situation is what
[4843.86 → 4851.28] like we're asking you as like open source people and equally myself as well. I've got as much to learn
[4851.28 → 4855.34] from this as anyone does. Like that's the stuff we need to kind of work on because it's very easy to be
[4855.34 → 4859.52] kind of nice in the times when you think things are great, but it's harder in the times when
[4859.52 → 4861.46] everything is broken, and your house is on fire.
[4861.46 → 4867.26] That is true. That's a it's actually a good example of when people are actually nice is when
[4867.26 → 4873.06] they're angry or should be angry or could be angry or whatever. That's totally true. So,
[4873.06 → 4877.30] Mike, you know, one thing I want to mention to the listeners before we close out is that we have
[4877.30 → 4880.64] this email called Change Law Weekly. I don't know, Mike, if you subscribe to it or not, but
[4880.64 → 4886.00] every week on Saturday and Jared, now it seems like Sundays because Sundays have kind of been a better
[4886.00 → 4890.96] day for us. We've just had such business going on between the news site going out three shows,
[4890.96 → 4895.82] lots of stuff happening around the business. I've been changing our verbiage to every weekend,
[4896.08 → 4901.08] every weekend. Yeah. I mean, I think Saturday has been a great day traditionally for us, but
[4901.08 → 4905.42] Sunday has turned out to be the day we actually ended up shipping this email. But in that email,
[4905.50 → 4912.78] the most recent one, uh, issue one 24, we mentioned Hebrew 1.0.0 and many other awesome things. So if
[4912.78 → 4918.62] you're not subscribed to that, go to changelog.com slash weekly subscribe, all we ask for is your
[4918.62 → 4922.96] email. But if you put your name in there, we greet you nicely in the email. So the name is optional.
[4922.96 → 4927.62] So don't feel like you have to, but a lot of people listen to that or sorry, a lot of people
[4927.62 → 4933.32] read that email, include our latest episodes, uh, everything that hits the, you know, our radar in
[4933.32 → 4937.86] terms of open source, software development, encouragement, uh, things like Mike's talking
[4937.86 → 4941.92] about here with being nice and stuff like that. So a lot of stuff around software development.
[4941.92 → 4947.38] So if you don't subscribe to that, you know, Jerry, what have we got? Sad faces or happy faces?
[4948.10 → 4952.32] Emoji, sad face. Emoji, sad face. And Mike, so do you subscribe to this? Just curious.
[4953.18 → 4958.22] Yeah, I do. As of three seconds ago, three seconds ago. What's your favourite issue?
[4958.40 → 4960.04] That's all we ask. That's all we ask.
[4960.12 → 4961.44] Just cause you just subscribed.
[4962.02 → 4963.36] My favourite issue is the next one.
[4963.90 → 4965.14] 125. Nice.
[4965.34 → 4965.86] You're going to love it.
[4966.18 → 4969.06] You're going to love it. You're going to love it. Now we got a lot of pressure on us to please
[4969.06 → 4971.20] Mike, which is, which is hard.
[4971.76 → 4975.92] I don't want to see an unsubscribed on Sunday. I'm going to be, I'm going to email you. I'm
[4975.92 → 4976.98] going to email you nasty things.
[4977.34 → 4981.96] That's right. Yes. That's the way we do it. But, uh, that's what I want to mention in closing,
[4981.96 → 4986.16] just because we mentioned, uh, homebrews 1.0 announcement recently in that email, a great
[4986.16 → 4989.60] place to, to mention that. And if you listen to the show, and you don't subscribe to that email,
[4989.60 → 4994.36] it's just, you're just missing out. That's all I can say. So do that now, take our direction.
[4994.36 → 5000.72] And, uh, that's it for the show fellas. So let's say goodbye. Bye everyone. Bye.
[5024.36 → 5025.36] Bye.
