[0.00 → 5.14] We're at Rodeon.com, and you're listening to the Changelog Podcast.
[18.46 → 25.00] Welcome to the Changelog episode 0.3.3. I'm Adam Stachowiak.
[25.54 → 27.60] And I'm Won Edelman. This is the Changelog.
[27.60 → 29.48] We cover what's fresh and new in the world of open source.
[30.00 → 32.84] If you caught us on iTunes, we're also on the web at thechangelog.com.
[33.02 → 33.92] We're also up in GitHub.
[34.44 → 36.50] Yep, head to GitHub.com forward slash explore.
[36.60 → 41.92] You'll find some training repos, some feature repos from the blog, as well as the audio podcasts.
[42.28 → 47.12] And if you're on Twitter, follow ChangeLog Show, not the Changelog, for all you crazy people out there.
[47.34 → 49.04] And if you want to follow me, I'm Adam Stack.
[49.60 → 52.12] And I'm Penguin, P-E-N-G-W-I-N-N.
[52.24 → 53.52] Hey, Adam, did you hear they caught that man?
[54.38 → 54.98] What man?
[55.46 → 56.50] The man that stole your microphone.
[56.50 → 61.38] Ah, I took my mic to LSRC and somebody took it.
[61.44 → 61.92] I think it was you.
[62.34 → 63.06] Somebody took it.
[63.12 → 65.78] I have now stolen both of Adam's mics.
[66.36 → 73.04] Speaking of Mike, Mike Par ham from Austin, who I had to fight hard not to call Mark Par ham
[73.04 → 76.22] in the Dolly story that I posted this morning.
[76.64 → 78.58] But I used the wrong Twitter handle.
[79.02 → 80.48] He's not at Mike Par ham.
[80.48 → 89.34] He's Markham, so I am Markham-ed when it comes to following Mike's Ruby projects.
[89.68 → 93.68] Well, you messed up there, but I hear you did some awesome work doing the training at Lone Star Ruby Con.
[93.76 → 94.24] How'd that go?
[94.58 → 95.36] That was fun.
[95.50 → 97.68] We were both there doing design eye for the dev guy.
[98.24 → 98.64] Yeah.
[98.64 → 102.34] Also did a talk on Saturday about Ruby API wrappers.
[102.44 → 103.20] Such a fun conference.
[103.28 → 104.40] I love these regional conferences.
[104.74 → 104.94] Yeah.
[105.06 → 106.50] You know, I had such good conversations there.
[106.54 → 109.32] I always enjoy just sometimes just the hallway chatter, really.
[109.42 → 113.40] I mean, I enjoy the presentations, but the hallway chatter is always nice to enjoy as well.
[113.80 → 114.18] Absolutely.
[114.84 → 117.74] Speaking of fun, Node Knockout was this weekend.
[117.74 → 119.54] How many teams competed?
[119.66 → 120.26] Like 200-something?
[120.94 → 121.56] Over 200.
[121.70 → 125.54] I think the guy said 100 or so finished.
[126.50 → 128.48] And we've done these types of contests before.
[128.64 → 129.74] They're just exhausting.
[130.08 → 130.30] Right.
[130.40 → 132.44] So this is like the Rails Rumble then.
[132.52 → 133.74] Still went to Rails Rumble, but for Node?
[134.06 → 134.64] That's right.
[134.84 → 138.94] So we talked to Gerard and Vishnu from Node Knockout.
[139.04 → 141.20] They have a consulting firm called Fortnite.
[142.16 → 145.48] And Michael and I sat down with them and talked about all the entries
[145.48 → 147.68] and kind of the background of the competition.
[148.00 → 150.16] And you've got two days left to vote.
[150.84 → 154.86] Voting ends, if you're listening to this live, voting ends on Thursday.
[156.34 → 157.42] Thursday the 2nd.
[157.76 → 159.40] Wednesday, September 2nd.
[159.68 → 163.14] And if you want to go vote, go to NodeKnockout.com and do it.
[163.80 → 165.36] Listen to the episode and go vote for your winners.
[165.72 → 166.08] Awesome.
[166.20 → 167.28] So we've got an awesome episode here.
[167.80 → 168.12] We do.
[168.18 → 168.74] Let's get to it.
[168.74 → 169.36] Let's do it.
[177.74 → 178.62] All right.
[178.66 → 184.12] We're joined today by the organizers of the Node Knockout competition, Jared and Vishnu.
[184.66 → 188.94] You guys introduced yourself and a little bit about who you are and how you got into Node.
[188.94 → 192.08] So I'm Jared.
[193.14 → 196.88] And I am Jared of Jared and Vishnu.
[198.00 → 202.66] And I, we really actually, Vishnu and I got into Node.
[202.66 → 206.74] We kind of fell into it, head over heels, if you will.
[208.68 → 213.76] We've done a lot of client-side JavaScript, and we love the idea of Node, which I think resonates with a lot of people.
[213.76 → 217.50] And so we wanted to try it out.
[218.00 → 223.72] And we'd kind of been people who've primarily been in the Ruby world on the server side.
[225.16 → 230.24] And as part of that, we've done kind of a bunch of programming competitions called the Rails Rumble.
[230.76 → 235.38] And we really loved kind of using that weekend, the Rails Rumble weekend, for trying out new technologies.
[235.38 → 246.54] And so we really hadn't done any Node at all until we kind of, and we were waiting for kind of competition like Rails Rumble to exist to try it out.
[247.08 → 252.22] And so I'm kind of hinting at where the idea for Node Knockout came from, is we were hoping somebody else would put it on.
[253.34 → 258.60] But that's kind of, I guess, both of our background.
[261.46 → 262.04] Well, yeah.
[262.10 → 262.90] So I'm Vishnu.
[262.90 → 267.52] Yeah, Jared and I, we both are Fortnite Labs, I guess.
[267.64 → 268.16] We're the only two.
[270.18 → 275.44] And I guess I'm probably more developer-heavy, although, and maybe kind of designer-y.
[277.06 → 281.72] Jared is kind of probably more data-y and product-y, I guess.
[282.64 → 285.64] But there's a reasonable amount of overlap between the two of us.
[285.92 → 290.38] So certainly Vishnu is a heck of a lot better at design and also at development than me.
[290.38 → 298.96] With Fortnite Labs, was that the company where you were releasing every two weeks or just a cool name?
[299.40 → 300.08] Kind of both.
[300.40 → 305.42] So normally whenever we estimate things, it somehow ends up being around two weeks for the projects that we want to do.
[306.28 → 311.62] And so then we realized, of course, that Fortnite would be a good name because it means two weeks.
[311.62 → 317.10] It was a little bit of a reaction to our previous company had been kind of a we'd been running it.
[317.18 → 319.12] And it was a big kind of product.
[319.64 → 321.56] Big, long-term, multi-year product.
[322.04 → 326.44] And we'd kind of always been more successful and had more fun with the smaller stuff.
[326.44 → 336.86] So we figured, you know, when we were going to go do our own thing, we should do things we enjoy, which ends up being the shorter stuff, the stuff that takes about two weeks to get done.
[337.62 → 339.42] And so we've done a fair amount of things in two weeks.
[339.52 → 341.36] We did a dashboard.
[341.96 → 343.18] It took about two weeks.
[343.28 → 346.14] We've done a mobile app.
[346.26 → 347.20] It took about two weeks.
[348.02 → 349.76] Yeah, a number of little consulting projects.
[349.76 → 352.36] So we're kind of falling into some bigger projects now.
[353.32 → 356.50] So Node Knockout was a lot more than two weeks' worth of work.
[356.92 → 357.10] Yeah.
[357.56 → 359.38] So you guys put the Node Knockout together.
[359.54 → 367.78] So for the folks that may not be familiar with the Rails Rumble or the Django Dash, why don't you give an overview of the rules for the Node Knockout?
[369.48 → 373.50] So Node Knockout or Rails Rumble are similar format contests.
[374.10 → 379.60] Our programming contests, they're very like hackathons that are 48 hours, normally on the weekend.
[379.76 → 382.36] We've concentrated roughly on a specific technology.
[382.62 → 385.34] So Rails is Rails, the Django Dash is the Django.
[385.54 → 387.66] So we wanted one for Node.js.
[388.58 → 391.80] And it's build whatever from scratch in 48 hours.
[392.30 → 395.26] And that's pretty much the one rule, I think.
[395.78 → 395.98] Yeah.
[396.16 → 402.22] I mean, I think what makes the contest unique is that really you start from nothing.
[402.36 → 404.20] You can't have any digital assets.
[404.20 → 407.04] So no designs, no code.
[407.04 → 410.10] You can rely on open source libraries and things like that.
[410.50 → 416.02] But you really have to start and build basically everything from scratch over the weekend.
[416.02 → 423.68] And so, you know, we just got through it, which is why we're both a little bit wired out of it.
[424.16 → 430.36] But, you know, literally we went from people deploying Hello World apps on Friday at, you know, 10 p.m.
[430.58 → 435.16] to fully functioning, amazing services and products.
[435.72 → 439.48] You know, essentially, you know, more than just an app, a whole business oftentimes.
[439.48 → 443.74] You know, 48 hours later on Sunday at 5 p.m. our time.
[444.40 → 444.50] Okay.
[444.60 → 449.04] So how many businesses have actually started to appear out of Node Knockout?
[449.24 → 450.58] Any ideas and numbers?
[451.08 → 452.26] How many businesses have appeared?
[452.42 → 456.68] Well, 98 teams got to reasonable products.
[457.14 → 459.60] We'll see if any actual businesses come out of that.
[459.76 → 463.68] I know a number, or not a number, but a handful of businesses have come out of Rails Rumble.
[463.68 → 466.32] And we have a number of VCs judging.
[466.94 → 474.18] So it's possible that if something seems appealing, you know, there's gasoline to pour on that match or that spark.
[474.90 → 479.54] I know we haven't judged yet, but do you have any favourite entries just yet?
[481.48 → 482.32] You know, we have.
[482.82 → 488.22] So to be honest, we haven't really had a ton of time to peruse things because we've been so busy putting on the competition.
[488.44 → 491.40] We're actually working on getting scoring together.
[491.40 → 493.42] I like Swarm Nation.
[493.86 → 495.46] I like, what else was there?
[495.52 → 499.00] We had some friends in the competition who we like.
[499.66 → 502.28] They did something called the Watchmaker.
[502.44 → 503.06] The Watchmaker.
[503.38 → 505.06] So that's 734M.
[505.12 → 505.96] Team 734M.
[506.38 → 509.02] Which is the same team name we've used in the past for Rails Rumble.
[509.64 → 512.22] So it holds a special place in our heart.
[512.32 → 512.54] Yeah.
[512.68 → 516.28] It's like a weird, pixel-y, retro, weird world.
[516.28 → 523.36] And then Map Reduce is also pretty mind-blowing to me, at least.
[525.02 → 532.30] It's roughly like SETI at Map Reduce or SETI at JavaScript website, I guess.
[532.46 → 533.12] It's hard to explain.
[533.58 → 534.34] What else was there?
[535.12 → 536.54] Can you think of anything off the top of your head?
[537.08 → 537.30] Yeah.
[537.42 → 541.18] I mean, it's just like Medium did a great job with their math.
[541.18 → 547.28] There's just, I mean, there's so much variance in kind of what's been done.
[547.38 → 548.02] It's just amazing.
[548.20 → 553.48] Like, there was a great app done by a team called Hack and Slash that lets you play kind
[553.48 → 559.34] of as a two-person or as a multiplayer two-dimensional platform game.
[559.50 → 560.92] But the platform is a webpage.
[561.28 → 565.18] You can kind of jump up and down on DIVS in the webpage, which is just like totally amazing.
[566.96 → 568.46] A lot of cool games.
[568.46 → 574.34] There's a great one that's kind of a multiplayer tower defence slash offence game.
[575.30 → 578.14] You know, it's just really pretty awesome what people have done.
[578.50 → 582.20] And I think what's particularly cool about the apps that people have submitted is that
[582.20 → 585.02] they don't really necessarily look like traditional web apps.
[585.18 → 587.70] You know, they're almost all entirely one-pagers.
[588.14 → 592.50] They're almost all real-time communication apps.
[592.82 → 595.30] You know, so it's like everything's happening kind of all at once.
[595.92 → 597.52] And so that's kind of exciting.
[597.52 → 599.02] Oh, and there was one that...
[599.02 → 599.82] Bladder block.
[600.30 → 601.02] Also, it was fun.
[601.28 → 602.20] Like, online Dictionary.
[602.40 → 602.76] Online Dictionary.
[602.88 → 606.02] And that one that does BitTorrent is pretty cool.
[606.20 → 606.72] Oh, right.
[606.98 → 607.52] There's one that...
[608.26 → 609.40] I did play Bladder block.
[609.70 → 612.90] That's totally not what I was expecting with that domain name.
[612.96 → 615.16] I did see the translation when you get through.
[615.30 → 620.40] I was expecting some sort of, you know, first-person shooter where you had to get to the loo.
[620.88 → 621.36] But...
[621.36 → 623.90] So, gaming.
[624.00 → 625.06] Is that a theme for this year?
[625.06 → 627.20] Or do you think it's just a place where Node shines?
[628.82 → 632.10] I think gaming caters to Node's strengths.
[632.80 → 634.60] Node is very, very strong.
[635.32 → 637.62] And not just that it caters to Node's strengths.
[637.76 → 640.58] It really shows off other platforms' weaknesses.
[641.34 → 647.56] Like, we actually did an online Massive Multiplayer Laser Roads game for Rails 1 Rumble last year.
[647.76 → 648.24] Asteroids.
[648.24 → 651.50] And it was really, really hard.
[651.82 → 653.58] And we were the only people to do a game.
[653.72 → 655.28] And it was considered insanely innovative.
[655.52 → 656.08] Or one of two.
[656.14 → 657.18] Or one of two teams to do a game.
[657.24 → 658.66] And it was considered insanely innovative.
[660.52 → 662.24] And it's just because it's not...
[662.78 → 664.02] Rails isn't designed for that.
[664.60 → 668.06] And whereas Node is totally...
[668.06 → 669.70] It's flexible enough that you can do that.
[670.04 → 671.76] And since, you know, you take away the constraint.
[672.02 → 673.38] You know, people love making games.
[673.38 → 676.64] And that's, I think, one of the reasons you've seen so many of them.
[678.98 → 681.72] Drop Node was another one that was actually more of a utility.
[681.90 → 683.10] It's just easy file sharing.
[683.56 → 685.38] So you just drag and drop onto the thing.
[685.48 → 690.04] And it actually uses WebSockets between two clients, I believe, to transfer the file.
[690.80 → 691.04] Okay.
[691.14 → 695.82] So you've already mentioned that a lot of the apps were using real-time technologies.
[696.86 → 701.08] And there's an absolute plethora of Node modules.
[701.08 → 704.34] Any ideas on which were the most used modules?
[706.70 → 711.02] So I think that Express and Connect got used a lot.
[712.88 → 721.96] I think, unfortunately for you, Michael, I think Socket.io was kind of more of the winner on the WebSocket side of things.
[722.10 → 724.32] Just because it gracefully degraded.
[725.02 → 726.72] So I heard a lot of people using that.
[726.72 → 733.54] A lot of people actually used the NoSQL databases.
[734.36 → 737.92] So there was a lot of people using things like Congo, Couch, and Regis.
[739.08 → 740.68] So those seemed to be winners.
[741.72 → 748.82] Aside from that, you know, I'm trying to remember what we were getting support issues for in the chat rooms, actually, mostly.
[749.26 → 750.32] I think those were the big ones.
[750.32 → 753.76] You know, the website's got a really nice design.
[754.02 → 756.08] I've been watching the sponsors list grow.
[756.18 → 759.02] It's almost up to NASCAR proportions now.
[760.12 → 764.06] How did you get such a list of really top-notch sponsors?
[764.44 → 766.42] And how did that list come about?
[766.42 → 772.10] So we came up with the idea for the site.
[772.28 → 773.40] We came up with a name.
[773.98 → 776.66] And then we pinged a couple of people about it.
[777.88 → 780.62] And then everybody just kind of came to us.
[781.62 → 783.76] And we figured it out.
[784.18 → 786.24] Occasionally we reached out to some sponsors on our own,
[786.32 → 789.02] but you don't tend to see those on the side of the website.
[789.02 → 795.12] Like, Google's sponsoring with some prizes, but they're not listed.
[796.68 → 801.58] For the most part, almost everybody reached out to us except for, you know,
[801.62 → 804.02] the very few people we contacted at the beginning just to say,
[804.10 → 804.76] hey, we have this idea.
[804.86 → 809.68] We think you might be kind of a good person to help us either provide infrastructure
[809.68 → 810.84] or write some blog posts.
[811.44 → 812.98] And everybody else just kind of found us.
[812.98 → 815.86] So getting sponsors has been not difficult at all.
[816.58 → 816.60] Okay.
[816.60 → 820.04] So you've mentioned the name of the competition,
[820.44 → 824.12] but I hear that it has a bit of an interesting story as to how it came about.
[824.66 → 826.80] Well, I mean, I guess I did it in my intro.
[827.20 → 832.06] But so basically we wanted to compete in a competition like this.
[832.58 → 834.62] And so we were waiting for somebody to put it on,
[834.68 → 835.76] waiting for somebody to put it on.
[835.98 → 839.06] And then we kind of got tired of waiting.
[839.18 → 841.32] And we were talking like brainstorming names for it.
[841.50 → 843.92] And I think my wife actually came up with a great name,
[844.00 → 845.00] which was Node Knockout.
[845.00 → 848.46] You know, kind of keeping with the alliteration that Rails does,
[849.16 → 849.82] Rails Rumble does.
[850.56 → 852.38] And so we said, like, we have a name for it.
[852.78 → 855.84] We had time because we had kind of just switched from being full-time employees
[855.84 → 857.28] to doing our own consulting business.
[857.72 → 859.72] And so we were like, we have time to put it on.
[860.52 → 863.48] We have a pretty good set of contexts.
[863.72 → 865.16] And, you know, we live in Silicon Valley.
[865.16 → 868.60] And so we, especially as consultants, we meet a lot of people.
[869.04 → 871.94] So we knew we could get the infrastructure and the judges.
[872.16 → 876.98] And there probably wouldn't be a lot better people to do it than us in terms of just connections.
[876.98 → 879.50] So we figured, hey, why not?
[879.56 → 880.26] How hard could it be?
[880.84 → 884.10] And we subsequently learned that it could be a lot of work.
[885.08 → 887.42] But it's gone really, really well.
[887.48 → 888.62] It's been very exciting.
[888.84 → 891.66] We've got to meet some great, great, dedicated people.
[892.56 → 894.48] And it's just been a total blast.
[894.56 → 895.46] Very, very fulfilling.
[895.46 → 897.40] Any plans to make this an annual event?
[898.30 → 898.58] Yeah.
[899.06 → 900.24] I mean, right now we're all...
[900.24 → 901.48] You guys sound tired.
[902.04 → 902.32] Yeah.
[902.60 → 903.46] Yeah, I'm tired.
[903.70 → 909.42] It's hard to think about doing it next year when you're, like, already exhausted
[909.42 → 912.50] and thinking about all of that, repeating all the work.
[914.16 → 915.14] But, yeah, definitely.
[915.64 → 921.34] I think the one thing that makes us question it the most is that we really want to compete in it
[921.34 → 922.40] more than anything else.
[922.40 → 927.26] And so to organize at the same time of competing is, of course, not really cool.
[927.94 → 932.74] So I think we're looking for a scapegoat on trying to get somebody else to run most of it next year
[932.74 → 933.70] so that we can actually compete.
[934.62 → 939.14] But I think we'll try to do it with a little bit bigger team than next year.
[939.48 → 943.42] This year we've been fortunate to have kind of the support of a number of people,
[943.72 → 946.00] including Ryan Dahl, that joined.
[946.22 → 948.96] And, Michael, you've been helping us, too, which has been totally great.
[948.96 → 954.96] But at the same time, it's really been, you know, we haven't been...
[955.52 → 956.84] We weren't perfect enough.
[956.92 → 958.86] We didn't really know enough to be able to hand off a lot of it.
[959.70 → 965.84] And so I think one of the learning experiences we have for next year is that it's good to be able to know
[965.84 → 968.12] what you need to do so you can hand off as much as possible
[968.12 → 971.66] because there's just a lot of coordination and communication work that has to happen.
[972.66 → 974.44] You've constantly mentioned the judges.
[975.02 → 976.86] How many judges are there, actually?
[976.86 → 984.26] There are 64 judges, expert judges, in addition to the public,
[984.72 → 989.16] who I think we have like 1,000 people who have voted so far from the public.
[990.52 → 995.46] These judges are people who we've reached out to in our network or have come to us
[995.46 → 999.40] or who other people who have come to us have suggested.
[999.66 → 1004.06] We've been really, really fortunate to get to some just amazing judges.
[1004.06 → 1007.70] And I'm really excited to look forward to, you know, what they're going to write.
[1007.90 → 1012.32] But we've gotten, you know, Ryan Dahl as a judge, the creator of Node.
[1012.56 → 1013.76] We've gotten...
[1013.76 → 1014.44] Brendan Eich.
[1014.98 → 1016.64] The creator of JavaScript as a judge.
[1016.78 → 1018.56] We've gotten John Remix as a judge.
[1019.04 → 1021.46] You know, we couldn't get Douglas Crockford as a judge.
[1021.64 → 1024.08] We tried to reach out to him a number of times.
[1024.08 → 1031.06] And then Tim Caswell, who's a judge, the creator of Connect, actually saw him on Friday night
[1031.06 → 1033.08] and reached out to him and said, hey...
[1033.78 → 1035.96] And apparently, actually, finally did talk to him.
[1036.36 → 1039.08] And we found that he did not...
[1040.08 → 1041.24] He hadn't heard of it at all.
[1041.34 → 1042.60] So it's just like one of those things.
[1042.76 → 1046.14] Like, for example, Deanna Alter of Arabian.
[1046.82 → 1049.88] I think 10 or 12 people pinged him about being a judge.
[1050.06 → 1051.24] So he's a judge now, too.
[1051.24 → 1059.60] So we tried the mechanism of approaching judges by full-court press, if you will.
[1060.02 → 1065.30] Okay, the other thing that is often looked at when people look at deploying a Node app
[1065.30 → 1069.14] is how to actually get Node onto our server,
[1069.38 → 1072.36] but also what sort of stacks exists out there already.
[1072.50 → 1075.66] I mean, Rails has Heroku and Rails machine.
[1076.88 → 1079.38] And then what's Node got?
[1079.38 → 1083.16] I know that in the competition you used Joint and Heroku.
[1083.38 → 1087.40] Could you explain sort of how well that went and also introduce them?
[1087.80 → 1088.46] Sure, absolutely.
[1088.70 → 1092.82] We've been really, really fortunate to have some great sponsors in joining Heroku for the competition.
[1093.00 → 1094.38] They provided all the hosting for free.
[1094.54 → 1100.20] Joint provided Knockout HQ, which is amazingly generous and very, very well organized.
[1100.20 → 1110.92] The kind of actually a lot of what kicked off the competition was that Heroku had just provided Node.
[1111.88 → 1112.78] A Node beta.
[1113.12 → 1114.04] A Node beta, yeah.
[1114.18 → 1116.64] So you could use Heroku dynes with Node.
[1117.16 → 1120.88] And so that was kind of, we figured, oh, well, you know, now Hosting Proviso rare providing it,
[1120.94 → 1122.84] so we could probably get this competition kicked off.
[1122.84 → 1128.44] And then actually immediately after we kind of announced the competition,
[1128.68 → 1133.14] we pinged Ryan before doing anything because we wanted to respect him.
[1134.60 → 1138.50] And so then Joint reached out to us and said, hey, look, you know, we do Hosting 2,
[1138.58 → 1141.78] and we're thinking about releasing smart machines maybe even for the competition.
[1141.78 → 1149.52] And so about two days before the competition, Wednesday, before the competition started Friday,
[1149.66 → 1157.60] about three in the morning, Joint released Node smart machines, which they are very, very beta.
[1159.36 → 1160.90] They have an awesome domain name.
[1160.98 → 1162.92] They have an awesome domain name, no.de.
[1163.16 → 1167.14] They have a lot of great functionality for the competition.
[1167.34 → 1168.26] You've got a static IP.
[1168.54 → 1170.10] You've got a lot of great stuff.
[1170.10 → 1172.66] You've got full access to a box.
[1172.80 → 1173.84] You've got SSH access.
[1176.02 → 1181.32] And so we were very fortunate to have that as an option in addition to Heroku as an option,
[1181.58 → 1184.16] which is, you know, very easy to deploy, very time-tested.
[1184.56 → 1187.84] It's been running a great Rails environment for years now.
[1189.16 → 1193.92] And so both providers did a great job.
[1194.02 → 1195.30] There were not a ton of issues.
[1195.58 → 1197.72] All the issues were addressed very, very quickly.
[1197.72 → 1202.68] For a service that was two days old, the joint service was just unbelievable.
[1202.92 → 1209.18] The support was really great because people were trying to figure out how the joint stack worked a little bit because it's on Polaris,
[1209.24 → 1210.62] which not a lot of people are familiar with.
[1211.48 → 1214.86] But the joint support made everything really super smooth.
[1214.86 → 1219.78] And the deployment process itself for both of these instances was very simple.
[1220.34 → 1222.40] It was just a simple Git-based deploy.
[1222.54 → 1224.70] So all you did was Git pushed to a remote repository.
[1225.10 → 1230.86] And with both services, it would take your code, upgrade it, and restart your server.
[1230.86 → 1237.62] So basically give you a great, you know, really, really simple, really, really easy to use, you know, deploy.
[1237.82 → 1244.30] And actually, one of the stories we heard from somebody was I'd never deployed to a server at all except by using STP.
[1244.38 → 1245.48] I'd never used Git or anything.
[1245.72 → 1250.46] And I was able to get, you know, my code up in Git and deployed before the end of the competition.
[1250.60 → 1253.10] I had a really great time so much that I want to keep working on it afterwards.
[1253.10 → 1257.30] So, you know, that's a huge success story for getting people to use these tools,
[1257.44 → 1260.96] which are ultimately going to make them better developers and make the web a better place.
[1261.04 → 1261.66] And we're really happy.
[1262.86 → 1267.70] Well, if you call it any episodes of the show, you know, this is where we usually put our guests on the spot
[1267.70 → 1269.70] and ask what's on your open source radar.
[1269.90 → 1275.58] So what out there, node-related or not node-related, that is open source that's got you excited
[1275.58 → 1276.84] and you can't wait to play with it?
[1276.84 → 1286.56] For me, I'm actually excited about where Accentra or, yeah, where Accentra's taking kind of connect and express.
[1287.44 → 1290.08] I mean, we started using it before, like, a huge refactor.
[1290.94 → 1295.98] And so I'm kind of excited to check out this that's kind of slimmed down
[1295.98 → 1298.32] and it seems a lot more pleasurable to use.
[1299.00 → 1303.16] NPM also, when we first started putting the website together, which is written in node,
[1303.16 → 1306.78] there were, like, three different package managers,
[1307.08 → 1310.30] and NPM seems to kind of have one out in all of those now.
[1310.44 → 1315.72] And so I'm pretty excited about using that since we're not right now.
[1315.88 → 1316.06] Yeah.
[1316.60 → 1319.56] And then another one, we actually had a lot of things we're excited about using
[1319.56 → 1322.36] because of the core technology website.
[1322.70 → 1325.38] But we actually also wrote our own ODM on top of Congo
[1325.38 → 1329.26] because we really overlooked that Congo's existed.
[1329.26 → 1332.06] So I want to kind of play with that and check that out.
[1332.06 → 1336.98] And Guillermo has, the author has kind of some API changes he's talked about.
[1337.98 → 1341.26] And then the other thing I mentioned that node technology that we can't really,
[1341.54 → 1345.16] I can't personally sell enough is I really, really enjoy using Node Inspector,
[1345.58 → 1349.94] which basically brings a web inspector to Node.
[1351.44 → 1354.58] And, you know, I don't know how much I'm at liberty to say
[1354.58 → 1358.74] because Danny, the writer, was showing off some stuff to me
[1358.74 → 1360.42] and kind of, I think, made me more private.
[1360.42 → 1363.58] But I think there's some really cool stuff going up with that.
[1363.70 → 1365.64] So that's something to keep your eyes open for.
[1366.06 → 1366.18] Yeah.
[1366.26 → 1367.10] That's a great project.
[1367.50 → 1367.66] Yeah.
[1369.16 → 1369.52] Cool.
[1369.62 → 1371.86] Well, thanks for joining us today to talk about the Node Knockout.
[1371.98 → 1375.50] I can't wait to look forward to seeing if you guys rest up a group rate
[1375.50 → 1376.56] and do this again next year.
[1376.72 → 1379.78] And hopefully Michael and I will get to participate.
[1380.78 → 1381.38] Oh, absolutely.
[1381.38 → 1385.10] And, by the way, I don't know when this podcast is going out,
[1385.16 → 1391.40] but the voting is going on now until Thursday at 5 p.m. Pacific, 0000 UTC.
[1392.74 → 1396.16] So, you know, if you're listening to this, and you haven't yet done it,
[1396.22 → 1398.14] go ahead and check out nonockout.com
[1398.14 → 1402.44] and, you know, leave some votes on these great, great apps that people have created.
[1402.96 → 1403.28] Absolutely.
[1403.44 → 1405.02] We'll be sure and put those links in the show notes.
[1405.24 → 1405.68] Thanks, guys.
[1405.68 → 1405.74] Thanks, guys.
[1405.74 → 1405.78] Thanks, guys.
[1405.78 → 1406.68] Thanks, guys.
[1406.68 → 1407.68] Thanks, guys.
[1407.68 → 1407.74] Thanks, guys.
[1407.74 → 1409.74] Thanks, guys.
[1409.74 → 1410.74] Thanks, guys.
[1410.74 → 1411.36] Thanks, guys.
[1411.36 → 1441.34] Thanks, guys.
[1441.36 → 1471.34] Thanks, guys.
