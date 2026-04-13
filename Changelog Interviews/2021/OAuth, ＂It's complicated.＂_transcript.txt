[0.46 --> 4.78]  What's up, welcome back, I'm Adam Stachowiak and you are listening to The Change Log.
[5.08 --> 10.72]  On this show, Jared and I talk with the hackers, leaders, and the innovators from all areas of the software world.
[11.12 --> 13.94]  We face our imposter syndrome, so you don't have to.
[14.24 --> 23.90]  Today we're joined by Aaron Parecki, co-founder of IndieWebCamp and maintainer of OAuth for a deep dive on the state of OAuth 2.0 and what's next in OAuth 2.1.
[23.90 --> 37.22]  We cover the complications of OAuth, RFCs like ProofKey for CodeExchange, also known as Pixie, OAuth for browser-based apps, and next-generation specs like the Grant Negotiation and Authorization Protocol, also known as GNAB.
[37.46 --> 42.72]  But the conversation begins with how Aaron experiments with the IndieWeb as a showcase of what's possible.
[43.18 --> 46.26]  Big thanks to our partners Linode Fastly and LaunchDarkly.
[46.66 --> 49.08]  We love Linode, they keep it fast and simple.
[49.38 --> 52.26]  Get $100 in credit at linode.com slash changelog.
[52.26 --> 54.80]  Our bandwidth is provided by Fastly.
[54.92 --> 56.70]  Learn more at Fastly.com.
[57.00 --> 59.20]  And get your feature flags powered by LaunchDarkly.
[59.34 --> 61.44]  Get a demo at LaunchDarkly.com.
[66.46 --> 69.14]  This episode is brought to you by Gitpod.
[69.24 --> 73.44]  Gitpod lets you spin up fresh, ephemeral, automated dev environments in the cloud in seconds.
[73.90 --> 76.38]  And I'm here with Johannes Landgraf, co-founder of Gitpod.
[76.38 --> 82.56]  Johannes, you recently opened up your free tier to every developer with a GitLab, GitHub, or Bitbucket account.
[82.84 --> 83.56]  What are your goals with that?
[83.82 --> 84.54]  Thanks, Adam.
[84.70 --> 90.28]  As you know, everything we do at Gitpod centers around eliminating friction from the workflow of developers.
[90.74 --> 96.58]  We work towards a future where ephemeral, cloud-based development environments are the standard and modern engineering teams.
[96.78 --> 97.78]  Just think about it.
[97.92 --> 100.68]  It's 2021 and we use automation everywhere.
[100.68 --> 104.58]  We automate infrastructure, CICD build pipelines, and even write in code.
[104.88 --> 107.72]  The only thing we have not automated are developer environments.
[108.12 --> 113.94]  They are still brittle, tied to local machines and a constant source of friction during onboarding and ongoing development.
[114.32 --> 115.72]  With Gitpod, this stops.
[116.08 --> 121.02]  Our free plan gives devs access to cloud-based developer environments for 50 hours per month.
[121.36 --> 128.72]  Companies such as Google, Facebook, and most recently GitHub have internally built solutions and moved software development to the cloud.
[128.72 --> 131.14]  I know I'm biased, but I can fully relate.
[131.42 --> 136.86]  Once you experience the productivity boost and peace of mind that automation offers, you never want to go back.
[137.14 --> 142.20]  Gitpod is open source and with our free tier, we want to make cloud-based development available for everyone.
[142.56 --> 143.12]  Very cool.
[143.36 --> 147.44]  Alright, if this gets you excited, learn more and get started for free at gitpod.io.
[147.72 --> 149.52]  Again, gitpod.io.
[158.72 --> 169.86]  So, Aaron, we have you here to talk about a few different things.
[170.28 --> 175.94]  OAuth, IndieWeb, tracking yourself since 2008, as it says on your website.
[176.10 --> 177.94]  You're like super into tracking your location.
[178.46 --> 180.06]  I thought we'd start there, kind of interesting.
[180.72 --> 184.54]  I mean, we're all being tracked at this point, but you're doing it to yourself on purpose.
[184.68 --> 185.46]  You want to tell us about that?
[185.46 --> 187.72]  I've been doing it for a long time.
[187.88 --> 189.48]  2008 was quite a while ago now.
[189.66 --> 189.86]  Totally.
[190.16 --> 195.16]  I've just always been fascinated with data collection and personal data collection about myself.
[196.06 --> 207.92]  And I actually, technically, I started tracking myself at least 10 years before that when I dug up some logbooks that I had found from my early childhood.
[207.92 --> 213.58]  Of having written down when we left for school and when we got there and like the times.
[213.90 --> 219.78]  And it was about two years of this collection of notebooks that I found with that.
[219.84 --> 221.24]  And I was like, oh yeah, that explains a lot.
[221.38 --> 222.10]  That explains a lot.
[223.26 --> 226.90]  So, you've been doing it on purpose, but via GPS for a long time.
[227.12 --> 228.44]  Have you learned anything about yourself?
[228.80 --> 229.16]  Habits?
[229.16 --> 236.82]  I mean, has that data tracking, I enjoy data tracking, but I always think like, why am I, I stopped doing it.
[236.86 --> 237.72]  I'm like, why am I doing this?
[237.80 --> 240.18]  Because I'm not, there's nothing actionable.
[240.34 --> 241.22]  There's nothing to learn.
[241.30 --> 242.80]  But it seems like you're getting something out of it.
[242.86 --> 246.58]  So, have you like revealed things about yourself to yourself or what?
[246.58 --> 252.70]  I know that's really the glamour idea of like learning insights about yourself and things like that.
[252.86 --> 259.74]  And there's definitely some ways where that's possible, but I would not say that's my primary motivation at this point for doing it.
[260.18 --> 274.06]  But what I have done with that data is used it to remind myself of things or used it to be able to geotag or remember where I was on a certain date or tag other things with my location.
[274.06 --> 284.38]  So, if I have a, well, I guess cameras do this automatically now, but if I have a photo from a not smartphone camera with just a date on it and I want to be like, where was that from?
[284.52 --> 286.06]  Where was I when I took that photo?
[286.30 --> 287.64]  I have that data now.
[287.66 --> 292.06]  So, I can go back and dig it up and correlate it with the location because it has a timestamp.
[293.00 --> 295.54]  Were you a big Goala user by any chance?
[295.84 --> 296.24]  Oh, yeah.
[296.30 --> 297.12]  And I still use Foursquare.
[297.12 --> 297.70]  Foursquare or Goala?
[297.86 --> 298.54]  Which one's for you?
[299.40 --> 301.64]  Well, Foursquare now because Goala's gone.
[301.64 --> 301.92]  Right.
[301.92 --> 308.12]  But I did use Goala briefly and then switched to Foursquare and I've been using it since then also.
[308.24 --> 308.38]  Still use it.
[308.90 --> 309.14]  Yeah.
[309.54 --> 310.10]  That's interesting.
[310.78 --> 311.50]  Logbooks even.
[311.78 --> 313.68]  Like, before GPS, you're logging yourself.
[314.46 --> 315.04]  Yeah, totally.
[315.18 --> 317.98]  Like, writing down, I got home at 3.28 p.m.
[318.04 --> 318.70]  Like, that kind of thing?
[319.04 --> 319.28]  Yeah.
[319.34 --> 323.26]  Made a little spreadsheet on a little notebook and filled in the dates and times.
[323.42 --> 325.22]  I filled out who drove the car that day.
[325.78 --> 326.42]  That's kind of cool.
[326.68 --> 327.94]  What do you think made you do that?
[327.94 --> 331.42]  Like, what were some of the early thoughts around doing it?
[331.42 --> 334.22]  Did you do it intentionally or was it just sort of like for fun?
[334.54 --> 335.66]  I have no idea.
[335.88 --> 336.18]  No idea.
[336.18 --> 337.80]  I mean, it was definitely intentional.
[338.08 --> 339.78]  I have no idea why I did that.
[340.18 --> 343.34]  Well, one thing you said is you're kind of obsessed with maps.
[344.16 --> 344.42]  Mm-hmm.
[344.42 --> 347.76]  And I think, actually, Jack Dorsey once said that about himself.
[347.90 --> 352.30]  You know, the idea for Twitter was more like, when it started, was like, what's your status?
[352.38 --> 353.80]  Or kind of like, what are you doing right now?
[353.96 --> 358.92]  And that came out of his interest in, like, where people are and what they're doing.
[358.92 --> 364.72]  And he kind of thought of it like in a train sense or in like a, there was a mapping part
[364.72 --> 366.10]  of what his thought process was there.
[366.16 --> 368.82]  Now, obviously, he stumbled upon something quite different from that.
[368.96 --> 373.50]  But was your interest with maps tied into the interest of like where I am, when I am?
[374.10 --> 374.86]  Yeah, definitely.
[375.12 --> 381.52]  And I also remember doing this as a child on long road trips between like Portland and California.
[381.80 --> 387.56]  I remember taking the giant fold-out maps and the highlighter and then tracing the route on the map,
[387.84 --> 388.96]  but in real time.
[389.18 --> 393.08]  So like, oh, now we made it to this off-ramp.
[393.20 --> 394.80]  Let's go fill in that little trace.
[394.88 --> 395.84]  Oh, we made another mile.
[395.98 --> 396.92]  I can see this mile marker.
[396.92 --> 403.20]  So trace that, doing that in real time because GPS tracking hadn't really existed at that point.
[403.20 --> 403.42]  Right.
[403.94 --> 404.80]  That is kind of cool.
[404.98 --> 407.14]  Do you also find yourself a completionist?
[408.00 --> 408.28]  Yeah.
[408.38 --> 408.56]  Yeah.
[408.94 --> 409.30]  Well.
[409.80 --> 413.00]  You're starting to hit on some things that resonate with me and I'm a completionist.
[413.08 --> 413.92]  So I'm starting to think, ah.
[415.60 --> 423.64]  I would say I would probably describe myself as, the problem I have is that if I start something,
[423.64 --> 426.48]  I need to be able to continue to do it indefinitely.
[427.06 --> 430.26]  So there are some tracking projects I've started that I have stopped.
[430.26 --> 435.94]  And I will tend to not bother starting something unless I know I can continue it.
[436.48 --> 441.64]  So one of the ones that I have, for example, not been able to do, even though I've tried a couple of times,
[441.70 --> 442.68]  is tracking my mood.
[443.06 --> 444.58]  So I think that'd be very fascinating data.
[445.04 --> 448.44]  But I've had two problems trying to collect that data.
[448.44 --> 454.86]  One, the amount of effort it takes is slightly too much to be able to plan on doing it indefinitely.
[455.60 --> 462.74]  Whereas the amount of work it takes for me to track my location indefinitely has now reduced to almost zero because I've automated so much of it.
[462.74 --> 473.80]  And the other problem with tracking my mood is I have not been able to find a good rating system that I can rely on to be consistent over time.
[474.46 --> 479.36]  So I've tried three-point scales, five-point scales, ten-point scales.
[479.36 --> 484.42]  And they all have various problems and inconsistencies.
[485.00 --> 499.76]  And the last problem is that as I try to track my mood, I am either influencing it negatively, as in if I'm thinking to myself, I'm not in a very good mood, it'll put me in a worse mood.
[499.96 --> 500.02]  Right.
[500.02 --> 501.74]  Having just thought about that.
[501.90 --> 509.96]  So it doesn't even seem like all of these problems with it, even though I love that data, it just caused me to completely fail to collect that.
[510.08 --> 510.24]  Yeah.
[510.34 --> 511.58]  Even though I've tried several times.
[511.72 --> 516.76]  It's like you're a faulty measuring stick, you know, because your mood affects the mood and you're trying to observe the mood.
[516.84 --> 522.20]  Kind of the Heisenberg principle of observability or something like that, where you end up changing the thing that you're trying to observe.
[522.62 --> 528.06]  And that was actually one of the big conscious decisions I made when I started tracking my location,
[528.06 --> 532.56]  which was I didn't want the fact that I was tracking my location to change where I was going.
[533.18 --> 537.54]  So at the beginning, like think back to 2008, smartphones were brand new.
[537.60 --> 538.96]  The iPhone was only a couple of years old.
[539.42 --> 544.36]  So that was not really like a normal thing that most people had access to at that point.
[545.52 --> 555.80]  So the big worry was like, oh, well, if you're tracking where you're going, aren't you going to be like concerned about somebody finding out or concerned about whatever?
[555.98 --> 556.12]  Right.
[556.12 --> 562.40]  So I just tried to make sure that the act of tracking my location was not changing where I was going as in.
[562.42 --> 569.44]  I wasn't avoiding places or I wasn't even like going down other streets in order to complete a city grid or things like that.
[569.44 --> 577.64]  I want because I wanted it to be passive collection just about what I do, not trying to treat it as a as a challenge to visit every street or something.
[578.02 --> 579.40]  What do you do to go back to it?
[579.40 --> 583.88]  You said before you could map it back to places or whatever.
[584.00 --> 588.00]  How do you go back to this data and enjoy it or make sense of it or analyze it?
[588.00 --> 599.58]  So everything that I've I've collected, I've now normalized all the different ways that I have been collecting into my current sort of database, which is actually just a collection of JSON files on a hard drive.
[599.72 --> 605.58]  And they're sorted into year, month, day folders and or rather year, month folders with a file per day.
[605.58 --> 610.00]  Then it's a line of JSON per file within the file.
[610.34 --> 614.04]  So what that basically means is that none of these folders are very large.
[614.80 --> 619.68]  At most, I have eighty six thousand four hundred lines in a file, one per second.
[619.84 --> 622.58]  That's the max resolution I can track with mine.
[622.58 --> 625.86]  And it becomes it's a very manageable data set.
[625.98 --> 627.46]  It's not anything fancy.
[627.66 --> 631.64]  It's easy to back up, easy to sync between multiple computers.
[632.46 --> 636.80]  And that is where everything is stored now.
[636.80 --> 643.44]  So my my current GPS tracking app that I wrote writes I have a thing that writes into that storage format on the server.
[643.68 --> 648.84]  And then over the past years of using different kinds of apps, I've converted all that data into that format.
[648.84 --> 658.92]  And then I've got some simple tools on top of that, which will load it in a web interface, for example, where I can just pull up a day and then see the path, the whole path for the day on a map.
[659.30 --> 663.38]  And then the other way that a lot of this data gets used is on my website.
[663.92 --> 672.32]  When I post a photo or post a note on my website, which these all get this is this is getting into the indie web thing.
[672.48 --> 674.34]  But like I don't actually post on Twitter.
[674.52 --> 675.90]  My bot posts on Twitter.
[675.90 --> 684.02]  So I post on my website, my website posts up to Twitter for me and anything I create on any social media ends up coming back to my website in some form.
[684.10 --> 690.70]  So my website is the canonical version of my online presence across whatever platforms I happen to be using this year.
[691.14 --> 696.92]  When my website, when I create a post on my website, then that also has a hook into my location database.
[697.04 --> 705.20]  So I can tag every post on my website with where I was at the time it was posted, even if the thing I'm using to post doesn't know about my location.
[705.20 --> 706.10]  Mm hmm.
[706.56 --> 707.44]  Very interesting.
[707.88 --> 709.34]  And your website's a wealth of things.
[709.44 --> 711.48]  I looked at the copyright, I think goes back to 1999.
[711.94 --> 713.58]  So like, I like this.
[714.12 --> 721.38]  You have your hub and everything else is just distribution or, you know, broadcasting into other spaces.
[721.38 --> 725.04]  But like Aaron Parecki dot com, that's yours.
[725.18 --> 725.72]  You own it.
[726.30 --> 728.00]  You can do whatever you want with it.
[728.10 --> 730.30]  You have you've built over time.
[730.30 --> 733.80]  A lot of us replace our website, but it seems like you've been adding new portions.
[734.76 --> 742.00]  And so you can tie into this like lifelong database of GPS's positioning and use it however you like.
[742.06 --> 743.24]  It's it's pretty cool.
[743.70 --> 748.50]  Over the top, is this accurate to the to the time of day for you, the battery life of your phone or something?
[748.98 --> 752.20]  And then your cloud, like what's the partly cloudy where you're at?
[752.26 --> 752.96]  68 degrees?
[753.02 --> 755.08]  Is that is that based on your phone or what?
[755.08 --> 756.10]  It's current.
[756.20 --> 758.08]  That's again tapped into that same location database.
[758.08 --> 762.68]  So my website always knows where I currently am and whether I'm on a bike or on a plane.
[763.18 --> 766.88]  And because it knows where I am, it knows my local time and it knows the weather.
[767.60 --> 771.20]  So what that means is that so I used to travel a lot, obviously not anymore.
[771.20 --> 777.80]  But I was previously traveling a lot for work and hopping between countries and cities and doing all these workshops and conference talks.
[778.38 --> 784.70]  And it meant that basically at any given moment, nobody would know what time it was if they were trying to contact me because I could be anywhere.
[785.08 --> 794.98]  So I put that on my website as a way to be like, oh, if you're trying to get in touch with me, you can just, you know, you go to my contact page and it says, oh, it's 3 a.m. because Aaron's in Sydney.
[795.66 --> 798.20]  And then, you know, it's probably not a good time to expect a response.
[799.30 --> 801.62]  You've made life really easy on a potential stalker.
[801.78 --> 807.74]  I mean, they would just be hooked up with all the tools they need just to know exactly what I have thought of that.
[807.74 --> 815.72]  And I also definitely recognize that I am extremely privileged and that I am not likely to have a stalker because I am not a woman on the Internet.
[815.82 --> 816.06]  Right.
[816.24 --> 819.60]  So that is something I've been aware of.
[819.62 --> 821.20]  And I realize not everybody can do this.
[821.20 --> 844.36]  And I like to think of it as I'm able to use this privilege of being a straight white male on the Internet to be able to demonstrate some of the more things that are a little bit farther fetched about self-tracking and publicizing that information because I'm not likely to become a target.
[844.36 --> 844.64]  Yeah.
[845.00 --> 850.66]  Well, one thing all people can do is the IndieWeb thing, which you're promoting and practicing yourself.
[850.80 --> 850.98]  Right.
[851.06 --> 861.56]  So this idea of IndieWeb, which you've been a part of for a while, is something that everybody, you know, can opt into that way of going about engaging with the Internet.
[861.70 --> 863.46]  Do you want to just touch on that briefly?
[863.52 --> 867.64]  I know we're going to get to OAuth and there's so much to talk about there that we do want to save time for it.
[867.66 --> 869.96]  But I think IndieWeb is important and interesting.
[870.20 --> 871.52]  So you obviously do, too.
[871.52 --> 874.96]  You've been a co-founder of IndieWebCamp and have been a part of it for a while.
[875.60 --> 875.70]  Yeah.
[875.78 --> 884.20]  I like to think of my website as demonstrating all of the things that are possible to do with your own personal website and expressing yourself online.
[884.40 --> 889.22]  And I fully realize that not everybody will do all of the things that my website is doing, nor should they.
[889.62 --> 895.16]  But I would like to have as much of that public as I can in order to demonstrate what's possible.
[895.64 --> 898.84]  And then people can choose which of those things they like.
[898.84 --> 904.82]  Maybe you like the idea of having just the time of day it is where you are, but not anything about where you are.
[905.10 --> 912.26]  Or maybe you like the idea of having all of your photos on your own website, treating Instagram as just a copy of your account.
[912.54 --> 917.40]  So, you know, you can pick and choose from all of the things that all of us in the IndieWeb community are doing.
[917.40 --> 923.40]  And I've just chosen to use my website as a way to demonstrate a lot of what is possible.
[924.32 --> 931.10]  What are the touch points for somebody who's like, okay, IndieWeb sounds cool, but maybe intimidating or I'm not sure.
[931.20 --> 938.98]  How do I, is there a list of lists of like, these are IndieWeb people who are doing IndieWeb things and you can steal some of their ideas?
[939.14 --> 941.28]  Or are there implementations of these things?
[941.28 --> 948.38]  I know there were some open source projects for a while that were trying to promote this lifestyle of posting online and syndication.
[949.14 --> 953.16]  Some have fallen by the wayside, but where do you send people who are interested in IndieWeb?
[953.48 --> 956.78]  The main home of the IndieWeb online is IndieWeb.org.
[957.24 --> 963.98]  And that is the, it's a wiki where it's a collection of, it's documentation of what everybody is doing with their websites.
[963.98 --> 967.90]  And both in the past and what could be done in the future.
[968.42 --> 973.72]  And the community is organized mainly in an online chat.
[973.72 --> 985.84]  So that's available through, in IndieWeb fashion, the website, chat.indieweb.org, as well as IRC, as well as Matrix, as well as Slack, and as well as possibly Discord.
[986.00 --> 987.50]  We're experimenting with a Discord bridge as well.
[987.54 --> 988.28]  And they're all connected.
[988.28 --> 990.88]  So you can join via any of them and you're talking to everybody all at once.
[991.34 --> 993.72]  So you don't, you're not tied to one of these platforms.
[993.98 --> 995.08]  Trying to make it accessible.
[995.80 --> 998.16]  Come in using whatever is the easiest for you.
[998.70 --> 1002.12]  And the community also is organized around events.
[1002.30 --> 1006.34]  So heavy, heavy event-based, meetup-based community.
[1006.66 --> 1008.60]  Again, it was a lot of in-person events.
[1008.78 --> 1011.50]  Every year I have been hosting a conference in Portland.
[1011.76 --> 1012.92]  It was the IndieWeb Summit.
[1013.36 --> 1015.68]  And we've obviously been on pause the last two years.
[1015.76 --> 1016.82]  Now it was always in the summer.
[1017.24 --> 1019.78]  But we're still doing a lot of online meetups in the meantime.
[1019.78 --> 1023.68]  So these are over Zoom, usually sometimes Jitsi.
[1023.98 --> 1028.92]  And you can join any of these meetups and just come and chat and learn what other people are doing.
[1029.32 --> 1035.76]  The main idea of the IndieWeb community is to get people to have their own presence online.
[1036.02 --> 1037.60]  Just have your own website.
[1038.08 --> 1042.10]  And that can mean a lot of different things to a lot of different people.
[1042.24 --> 1043.56]  And that's great that it can.
[1043.56 --> 1051.02]  So if you want your website to be just a one-page thing about you and what you're doing and links to find you elsewhere, that's great.
[1051.32 --> 1052.00]  That is your website.
[1052.20 --> 1053.52]  You control that and you can do that.
[1053.66 --> 1059.76]  If you want your website to be a full-on log of everything you've done online and offline, that's also great.
[1059.86 --> 1060.48]  You can do that.
[1060.48 --> 1065.88]  So there's obviously a lot of range in between those two extremes.
[1066.36 --> 1072.02]  And we do see a lot of people fall into various levels of that.
[1072.16 --> 1082.06]  So you could have a WordPress blog, which is a great, easy way to get a website that you can post things to and collect your online life on that site.
[1082.06 --> 1095.20]  I like that pragmatic approach because a lot of the IndieWeb blog posts or content that I've seen historically, some of it's very purist and idealistic to the point where it's all or nothing.
[1096.46 --> 1102.22]  And I like that the way you're presenting it and maybe the way that the community's moved or whatever.
[1102.70 --> 1109.68]  It's a little bit more opt-in-able to different aspects of IndieWeb because I resonate with a lot of what you're saying.
[1109.68 --> 1118.72]  And there's also bumping up against either technical limitations or time limitations or content that I don't care about quite as much.
[1119.12 --> 1120.02]  I don't really care.
[1120.64 --> 1128.76]  I guess historically with my tweets, I have posted them on Twitter and then I had a thing that would suck in those into my website.
[1129.42 --> 1132.24]  They're like an open source thing, like a tweet archive kind of a thing.
[1132.98 --> 1133.96]  Twitter now offers that.
[1134.08 --> 1137.56]  You can log in and click down a zip file every once in a while if you wanted to.
[1137.56 --> 1141.86]  But it's not the purist, you know, publish there and then syndicate.
[1142.46 --> 1150.38]  It's publish over here on your platform but then make sure that I can, I ultimately have those things so that Twitter couldn't remove them.
[1150.46 --> 1160.42]  And so it's like kind of not full Indie but at the same time, I very much believe in the power of owning your own domain, publishing your own content on your own website,
[1160.42 --> 1163.78]  especially content that matters to you and you want to last for a while.
[1164.10 --> 1172.32]  And then using the different social networks for what they're good at as opposed to writing for free on Twitter.com.
[1172.54 --> 1173.78]  All my thoughts, for example.
[1173.78 --> 1175.58]  Exactly, yeah.
[1175.76 --> 1186.88]  And I think it's actually even more of a problem of when you're writing these longer form things that are, you know, tutorials or things that you want to use to build your own brand or build your presence online.
[1186.88 --> 1193.60]  And then you go and put that on Medium where it's like 100% somebody else's platform and you're just giving content to somebody else's domain.
[1193.60 --> 1204.54]  So for those, it's like especially important, put that on your website and then use those platforms like you're saying to promote the thing that you wrote on your website and drive people to your own place online.
[1205.38 --> 1219.92]  It's really great for a source of truth too because if you use your personal domain as the hub and you broadcast that to Twitter or somewhere else and somehow in the middle there it changes, well, this is actually the source of truth.
[1219.92 --> 1226.74]  Like, you know, reminds me of the very last episode of Silicon Valley when he sent the message.
[1226.90 --> 1232.02]  Stop me if you heard this before, but he sent the message and perfectly put four dots in and not three, which is a common ellipses.
[1232.32 --> 1239.22]  And somehow the AI in the middle there decided to compress it, which taught them how they subjected security and all these fun things, whatever.
[1239.78 --> 1242.26]  Turn that four dot ellipses into a three dot ellipses.
[1242.76 --> 1244.70]  So long story short, somewhere in the middle there can change.
[1244.78 --> 1248.48]  And by you having your hub, you can confirm truth essentially.
[1249.22 --> 1249.30]  Yep.
[1249.92 --> 1277.66]  This episode is brought to you by Retool.
[1277.66 --> 1283.60]  Retool is the low-code platform for developers to build internal tools super fast and super easy.
[1284.02 --> 1286.60]  They have a ton of integrations and templates to start with.
[1286.86 --> 1291.26]  With a click of a button in seconds, you can start with a new Postgres admin panel application.
[1291.70 --> 1295.86]  Kick off an admin panel for reading from and writing to your database built on Postgres.
[1296.38 --> 1300.06]  This app lets you look through, edit, and add users, orders, and products.
[1300.38 --> 1301.90]  It's too easy to get started with Retool.
[1301.90 --> 1305.50]  Head to retool.com slash changelog to learn more and try it for free.
[1305.82 --> 1308.44]  Again, that's retool.com slash changelog.
[1308.44 --> 1325.54]  So Aaron, back in December of 2019, in a post title, It's Time for OAuth 2.1, you wrote,
[1325.54 --> 1336.16]  Trying to understand OAuth often feels like being trapped inside a maze of specs, trying to find your way out before you can finally do what you actually set out to do, build your application.
[1336.16 --> 1338.84]  That resonated with me.
[1339.38 --> 1346.70]  And you go on, of course, to speak in depth about that and about OAuth 2 and 2.1 and where we've been and where we're headed.
[1346.86 --> 1348.02]  But how did we get there?
[1348.30 --> 1349.32]  How did we get to that point?
[1349.68 --> 1352.96]  Because it's been a long and windy road with OAuth and a lot of people involved.
[1353.92 --> 1355.24]  Why does it feel like that?
[1355.32 --> 1357.80]  Or at least why did it feel like that in December of 2019?
[1358.64 --> 1359.42]  That's a good question.
[1359.56 --> 1359.74]  Yeah.
[1359.74 --> 1362.12]  I still stand by that statement.
[1362.50 --> 1367.16]  And here we are a year and a half later and still working on 2.1.
[1367.28 --> 1373.62]  But obviously that was in no small part due to the events of 2020 slowing that work down.
[1374.46 --> 1375.64]  But how did we get there?
[1375.86 --> 1381.34]  I think, honestly, I think it's a natural evolution of the space.
[1381.42 --> 1384.82]  And I don't even think it's necessarily bad that it happened that way.
[1384.82 --> 1390.88]  It started out in 2012 with the OAuth 2 draft being published.
[1391.68 --> 1398.90]  And that draft, the core draft, was, you know, I had been going through a pretty rough time in the spec world.
[1399.08 --> 1401.90]  And there were several arguments involved in creating that.
[1402.04 --> 1411.16]  And there were several people who quit in a fit of rage to go and do other things because they were just done with the spec world, which I totally understand.
[1411.16 --> 1420.58]  And what was left in that core draft was a relatively small amount of information, a small amount, a small spec.
[1420.70 --> 1422.62]  It was a core, right?
[1422.64 --> 1427.36]  It was a framework, actually, not even a spec, which means you can use it to build things.
[1427.48 --> 1428.56]  You can use it to build specs.
[1428.90 --> 1432.44]  But by itself, it didn't necessarily describe a complete interoperable system.
[1432.44 --> 1439.06]  So there are a lot of good parts in it, but you need more in order to actually finish building out a system.
[1439.32 --> 1441.46]  You need more pieces.
[1441.92 --> 1444.52]  So there's that aspect of it.
[1444.64 --> 1455.32]  And then the other aspect is that over the years, there were things discovered about the core spec that were maybe security problems or there were better ways to do things.
[1455.32 --> 1465.00]  And a lot of that stuff ended up being expressed by new specs and new extensions, one of them being Pixie, PKCE, proof key for code exchange.
[1465.22 --> 1474.50]  That was an extension developed originally because mobile apps couldn't do the flow the sort of normal OAuth way, and they needed a solution for that.
[1474.60 --> 1483.46]  And then it turns out it's been discovered that that extension actually solves a number of different attacks that weren't even really thought of when Pixie was originally developed.
[1483.46 --> 1500.00]  So this is stuff that just sort of happens over the years of people building things with the specs and deploying these systems and getting experience with how these things work and how they evolve and then documenting it.
[1500.24 --> 1503.14]  And that's really what specs are, the documentation of a system.
[1503.58 --> 1508.86]  And yes, there's a lot of them because we've learned a lot over the last nearly 10 years.
[1509.36 --> 1511.00]  And I think that's okay.
[1511.00 --> 1514.80]  It's okay to have that evolve slowly like that.
[1514.88 --> 1524.86]  It doesn't need to be something that you create perfectly in the first try because realistically, that's actually not possible to go and set out to design a spec and make it perfect on the first try.
[1525.32 --> 1526.40]  That is how we got there.
[1526.52 --> 1531.72]  It was a lot of filling in the gaps in the original OAuth 2.
[1531.82 --> 1533.98]  It was a lot of patching of security features.
[1533.98 --> 1540.88]  And also there's the whole section of things that were intentionally not described by the spec.
[1541.06 --> 1551.24]  For example, how an API can validate access tokens, which was at the beginning sort of considered internal implementation detail of a system.
[1551.24 --> 1557.84]  But it turns out, as we've seen, people create companies around the idea of providing OAuth as a service.
[1557.84 --> 1565.36]  Then it makes sense to provide a standard way to validate access tokens so that you can interoperate with different companies' services.
[1566.08 --> 1569.16]  So it's just a lot of evolution, slow evolution of the space.
[1569.44 --> 1574.32]  And that's how we got to December 2019 of, yes, there's a lot going on.
[1574.44 --> 1576.24]  There are a lot of different pieces, a lot of moving parts.
[1576.24 --> 1591.18]  And if you actually take a look at those moving parts and all the different building blocks and all the different pieces, there is a much simpler picture that's sort of coming out the other end, which is what we're trying to capture in OAuth 2.1.
[1591.38 --> 1596.86]  Is that there are a lot of things that are known to be not good practices anymore.
[1597.14 --> 1598.36]  So let's take those out.
[1598.44 --> 1604.00]  There's security features that we should just always be doing, like Pixie, because it solves many different attacks.
[1604.00 --> 1609.68]  And if we can consolidate all those, then that's just less stuff for people to read.
[1609.94 --> 1617.80]  Because I don't want you to have to read 10 specs in order to get to the point of what the industry considers the best practice right now.
[1618.14 --> 1625.02]  So OAuth 2.1, which sounds like it's still in the works, is not new things.
[1625.02 --> 1634.24]  It's a distillation of things that were how OAuth 2.0 evolved and said, here were the good ideas.
[1634.54 --> 1636.00]  Let's get rid of those bad ideas.
[1636.54 --> 1637.96]  This is how you should do it now.
[1638.64 --> 1638.80]  Yep.
[1639.02 --> 1644.12]  It's trying to modernize OAuth 2.0 without actually changing any, without adding new things.
[1644.24 --> 1645.88]  So we're not trying to invent a new spec.
[1646.24 --> 1649.76]  We're not trying to say everything about OAuth 2.0 was terrible.
[1649.92 --> 1650.52]  Let's start over.
[1650.52 --> 1657.76]  It's really just, it's trying to encapsulate what is currently regarded as the best practice of OAuth 2.0.
[1657.84 --> 1664.52]  And the problem with OAuth 2.0 is that if you say OAuth 2.0, it actually doesn't really mean anything because it's so many different specs in reality.
[1664.76 --> 1670.22]  OAuth 2.0 is a collection of several different specs and you kind of have to know which ones are relevant.
[1671.00 --> 1676.94]  So the idea with calling it OAuth 2.1, giving it a name and a new RFC is that that just sets a new baseline.
[1676.94 --> 1685.58]  So that's giving a name to what is the best practice and what we, we do consider to be OAuth 2.0 today.
[1685.58 --> 1688.52]  So are those guide rails there?
[1688.66 --> 1701.56]  I know the 2.1 isn't ratified or finished or whatever, but if you were to say 2021 and onward, if you're doing OAuth 2, here's the flow or maybe, maybe it's three flows or whatever it is.
[1701.58 --> 1705.72]  Like here's the simplified version now and here's how it would work.
[1706.00 --> 1710.14]  Could you explain that to us in words or is that like a half hour dissertation?
[1710.56 --> 1710.68]  Okay.
[1710.68 --> 1713.34]  I mean, I can give you a short version.
[1713.40 --> 1714.38]  Give us the simplified.
[1714.38 --> 1715.24]  I can also give you a long version.
[1715.82 --> 1716.66]  Let's start with the short.
[1716.90 --> 1717.62]  Give us a medium version.
[1718.94 --> 1724.18]  The short version is disregard password and implicit grants.
[1724.68 --> 1725.70]  Those don't exist anymore.
[1726.18 --> 1733.96]  So the main flow in OAuth 2 and OAuth 2.1 is the authorization code flow with the mechanism described by Pixie.
[1734.50 --> 1739.02]  So Pixie describes a, it's a neat little trick that's been added into the authorization code flow.
[1739.02 --> 1744.78]  It turns out there's several reasons why that's a good idea, which are way too detailed to go into right now.
[1744.94 --> 1745.04]  Okay.
[1745.36 --> 1748.66]  But it is always a good idea for every kind of app to use Pixie.
[1749.12 --> 1757.60]  I do get a lot of people confused about, because of the origins of Pixie, whether you should use Pixie if you have a client secret, for example.
[1757.88 --> 1760.94]  And it turns out the answer is yes, use Pixie, even if you have a client secret.
[1761.04 --> 1765.08]  Because a client secret is not solving some of the attacks that Pixie does solve.
[1765.34 --> 1767.26]  So it's not a replacement for a client secret.
[1767.26 --> 1767.98]  It's not an alternative.
[1767.98 --> 1771.04]  It is just how the authorization code flow should work.
[1771.56 --> 1777.26]  Now, the client secret issue is, how do you authenticate a public client, like a mobile app or a single page app?
[1777.42 --> 1779.02]  And the answer there is you can't.
[1779.26 --> 1783.96]  There is no way to do that, whether or not you're using any OAuth flow or OAuth at all.
[1783.96 --> 1785.60]  So you just don't.
[1785.88 --> 1796.02]  And you rely on the redirect URL and the registration of that and the fact that domain names are the other foundation of our security online.
[1796.14 --> 1799.26]  And that's enough protection of those kinds of apps.
[1799.26 --> 1806.70]  The main OAuth flow today is authorization code flow with Pixie and use that for everything unless you have a very specific reason.
[1806.98 --> 1810.88]  Otherwise, the other flow to be using would be the device flow, which is an extension.
[1810.88 --> 1816.98]  And that's what you'll be using when you're on like an Apple TV or other devices that don't have a browser or don't have a keyboard.
[1817.76 --> 1830.38]  And then the third sort of, I don't want to call it a main flow, but the third flow that will be commonly used is the client credentials flow, where it is a client, an OAuth client that's not acting on behalf of a user.
[1830.54 --> 1832.70]  It's just the client acting on behalf of itself.
[1832.70 --> 1834.62]  So there's no user involved in the flow.
[1834.78 --> 1836.86]  It's just the client shows up and says, I want an access token.
[1837.00 --> 1837.74]  And then it gets one.
[1838.44 --> 1846.70]  Which happens a lot with administrative apps or backend tooling, where you're just trying to remotely manage a service, which we do a lot of that stuff around here.
[1847.44 --> 1849.72]  And you just don't need, and there's no client being represented.
[1849.86 --> 1852.24]  You're just like, no, it's just us.
[1852.68 --> 1856.56]  It's just changelog trying to update a DNS record.
[1856.56 --> 1861.86]  Yeah, and it's kind of like using a API key to go make a request somewhere.
[1861.86 --> 1869.18]  But by including it in the OAuth world, it means you can use it alongside of your OAuth flows that do have users.
[1869.52 --> 1874.72]  So it uses the same, you end up with the same access tokens, and you end up with the same sort of ways of validating things.
[1874.72 --> 1878.08]  And you don't have to hard code as much stuff in every different place it's being used.
[1878.08 --> 1878.40]  Right.
[1878.58 --> 1890.06]  So there's no advantage as a provider or as a service provider to doing the OAuth style, except for the fact that you're probably doing it for your client style anyways.
[1890.06 --> 1898.56]  And so it's just one path of authentication for your API, regardless of which style you're doing.
[1898.62 --> 1903.12]  Versus it, like you said, if you're like, well, we also have this API token thing we do for service accounts.
[1903.30 --> 1906.78]  And that would just be like a whole other code path for the provider.
[1906.88 --> 1907.34]  Is that what you're saying?
[1908.18 --> 1908.46]  Yeah.
[1908.58 --> 1910.48]  So let me rephrase that, I guess.
[1910.48 --> 1920.50]  So using client credentials has the advantage of using the same access token format that you'd be using for flows that do have users involved.
[1920.72 --> 1925.40]  So if you're building out a system and you expect a user to be logging in, you should be using OAuth.
[1925.78 --> 1928.96]  You'll end up with access tokens and your APIs can validate those access tokens.
[1928.96 --> 1942.48]  If you also have a situation where you're expecting clients to not have users log in because they are just service level things, then if you fit them into the same framework, you can have your clients go get access tokens from the same place, your OAuth server.
[1943.04 --> 1947.82]  And your APIs can validate access tokens in the same way as they're validating the access tokens for users.
[1947.82 --> 1956.32]  Now, the alternative would be you would have like a special API key thing that your APIs know how to validate those API keys.
[1956.62 --> 1962.28]  But now you've got a whole separate thing to manage of like issuing those, provisioning those, getting your API to validate those.
[1962.68 --> 1966.92]  Whereas using the OAuth client credentials flow means you've consolidated that logic.
[1967.76 --> 1967.78]  Okay.
[1968.14 --> 1970.56]  I think I understood you, but I regurgitated poorly.
[1971.24 --> 1974.20]  So you did a good job the first time and a better job the second time.
[1974.26 --> 1974.92]  Thank you for that.
[1974.92 --> 1977.80]  The device thing is interesting.
[1978.10 --> 1982.92]  So because back in 2012, we didn't have these devices really, or did we?
[1983.04 --> 1991.24]  I mean, where you have like an Apple TV or a Chromecast thing that you're trying to sign into with, and there's no keyboard there.
[1991.42 --> 1992.32]  There's no there there.
[1992.52 --> 1998.38]  It's like, well, you know, it's going to pull up this thing onto the screen that you're going to go like letter by letter.
[1998.94 --> 2000.74]  There's no browser usually, right?
[2000.74 --> 2000.78]  Right.
[2001.04 --> 2006.38]  There's usually no browser in those, which means you can't open a web page and send these off to the to the OAuth server.
[2006.62 --> 2006.72]  Right.
[2007.02 --> 2011.68]  So what we have seen is people build password dialogues into those devices.
[2011.94 --> 2016.18]  And then, yeah, you've got the onscreen keyboard that you're scrolling letter by letter, switching to the symbol.
[2016.42 --> 2016.78]  Oh, yeah.
[2016.84 --> 2017.80]  Long password.
[2018.20 --> 2018.94]  Long password.
[2018.94 --> 2021.60]  And you're entering it very slowly in front of anybody else in the room.
[2021.86 --> 2023.10]  So it's painful.
[2023.20 --> 2024.06]  That's great.
[2024.22 --> 2026.38]  And that's not a good solution.
[2026.54 --> 2032.74]  So the the fix for that is the OAuth device flow, which kind of separates the application.
[2032.86 --> 2036.14]  It's going to be getting the access token from the device you're using to log in.
[2036.14 --> 2038.96]  So you will start the flow on the TV.
[2039.62 --> 2040.44]  There is no keyboard.
[2040.60 --> 2041.66]  There is no browser.
[2042.36 --> 2048.20]  And instead, it says, hey, go over to your computer or go pull up your phone, go enter this link and then enter these six letters.
[2048.82 --> 2052.16]  And that establishes the connection between the TV and your phone.
[2052.30 --> 2057.52]  And then you can finish logging in on your phone where you do have a keyboard and a browser and your password manager and things like that.
[2057.52 --> 2065.68]  And potentially even more hardened security for the person's true identity because face ID and touch ID and whatever ID.
[2065.68 --> 2066.08]  Right.
[2066.30 --> 2067.86]  You can tap into multi-factor auth.
[2067.86 --> 2071.04]  You can tap into single sign-on to other systems that the TV doesn't even have to be aware of.
[2071.98 --> 2073.22]  Lots of lots of benefits.
[2074.56 --> 2076.08]  So OAuth can handle that now.
[2076.20 --> 2084.18]  Another thing you mentioned in that post, which I thought was interesting, it's kind of an aside, is that there's Justin Richer, perhaps, has this whole other idea.
[2084.70 --> 2086.46]  Transactional authorization.
[2086.46 --> 2088.06]  I don't know if that's still a thing.
[2088.12 --> 2090.26]  You say maybe eventually that'll be OAuth 3.
[2091.04 --> 2094.84]  Has that advanced or is that still a thing or what's the situation with that?
[2094.84 --> 2095.10]  Yeah.
[2095.64 --> 2099.00]  There's been quite a lot of movement on that front since 2019.
[2099.48 --> 2104.84]  So it was called transactional authorization in 2019 when Justin had originally proposed it.
[2105.14 --> 2111.44]  And since then, there actually is a new working group formed at the IETF to take on that work.
[2111.84 --> 2113.32]  And it's been renamed since then.
[2113.32 --> 2116.04]  So now it's called Gnap, G-N-A-P.
[2116.46 --> 2116.68]  Okay.
[2117.00 --> 2119.56]  And don't even get me started on the naming.
[2120.30 --> 2121.12]  What's the stand for?
[2121.12 --> 2122.18]  That was a whole thing.
[2122.62 --> 2130.42]  It was a very long discussion on the mailing list and pages of Google Docs of suggestions and voting.
[2130.68 --> 2132.30]  It was a whole process.
[2132.94 --> 2134.60]  But that was when the group was formed.
[2135.30 --> 2136.60]  Had to decide on the name for it.
[2136.82 --> 2138.74]  And anyway, whole thing.
[2138.74 --> 2142.82]  So Gnap, Grant Negotiation and Authorization Protocol is what that stands for.
[2143.04 --> 2143.18]  Okay.
[2143.18 --> 2148.06]  And that was the least bad suggestion out of all of them.
[2148.06 --> 2154.88]  So that is a new IETF group, meaning it's not happening within the OAuth working group.
[2155.32 --> 2162.24]  However, there are a lot of people who participate in both still, just like OAuth and OpenID Connect, where OpenID Connect is actually not even in the IETF.
[2162.36 --> 2163.30]  It's in its own foundation.
[2163.72 --> 2165.94]  But there are a lot of people who participate in both.
[2165.94 --> 2169.92]  Gnap, on the other hand, is so it's a new IETF group and it's a new document.
[2170.24 --> 2173.12]  And that work has continued on since then.
[2173.20 --> 2186.24]  It has gone through a pretty extensive amount of changes and iterations and redefining the scope of the document and pulling some of it out into a new document.
[2186.24 --> 2195.54]  The whole idea with that one is explicitly to not assume any compatibility with OAuth, but solve similar problems.
[2196.08 --> 2201.70]  So I know a lot of people's frustrations with OAuth beyond just the fact that it's in a bunch of documents.
[2201.90 --> 2211.14]  There are some things about how OAuth works that you can't really change at this point without breaking a lot of assumptions of a lot of software.
[2212.26 --> 2217.18]  So those are things that we kind of have to just deal with and live with now in the OAuth world.
[2217.90 --> 2220.18]  And they're not, it's not broken.
[2220.66 --> 2222.58]  It's fine, but it's not ideal.
[2222.80 --> 2224.92]  And there isn't a good way around that one.
[2224.92 --> 2226.90]  We're trying to clean up OAuth with OAuth 2.1.
[2227.28 --> 2231.80]  I would think of that as like housekeeping, you know, clean up your house before a guest comes over kind of thing.
[2232.32 --> 2235.14]  But Gnap is more like rebuild the house.
[2235.50 --> 2236.88]  We're going to start from a new foundation.
[2237.52 --> 2242.70]  Do you have any for instances on things in OAuth 2 that you just described in general?
[2242.80 --> 2244.58]  But are there any examples of what you're talking about?
[2244.58 --> 2245.06]  Yeah.
[2245.84 --> 2252.90]  One of the examples of something that is pretty deeply baked into the model of OAuth is the idea of a client.
[2253.38 --> 2259.22]  This is where you would go to the developer website of a company and you would say, I'm going to build an OAuth app against your API.
[2259.74 --> 2260.76]  I'm going to register a client.
[2260.90 --> 2262.46]  And you go in there and you type in the client name.
[2262.46 --> 2265.94]  You upload an icon and then you get back a client ID and a client secret.
[2266.44 --> 2269.28]  Or you may only get back a client ID if you told that you're building a mobile app.
[2269.86 --> 2273.76]  And then you put that, you use that client ID and your client secret in your applications.
[2273.94 --> 2278.92]  You configure your applications with those client ID, with a client ID, with a client secret, if you have the secret.
[2278.92 --> 2280.76]  And you do an OAuth flow.
[2281.50 --> 2291.76]  The reason this is potentially a problem is that there isn't really a distinction between the concept of I'm building this app, like it has a name and it's in the app store.
[2292.06 --> 2296.32]  And the difference between a particular instance of that app running somewhere.
[2296.68 --> 2298.20]  So this is most obvious with mobile apps.
[2298.38 --> 2305.66]  I publish an app into the app store and it's identified by the client ID and it has a name and it has an icon and all that.
[2305.66 --> 2310.92]  But when it runs on somebody's phone, it is a unique piece of software on one person's phone.
[2311.32 --> 2315.00]  And somebody else running that same app, it's the same software, but it's a different instance.
[2315.28 --> 2324.36]  And because it's a different instance, we actually have an opportunity to do a lot of things around the security of it that just don't really mesh well with OAuth.
[2324.60 --> 2327.40]  And yeah, you can shoehorn a bunch of the stuff in it.
[2327.40 --> 2340.72]  Like one of the security features that would be really useful is to be able to say, OK, the access tokens issued to this person's phone cannot be used by anybody else's instance of that app.
[2340.72 --> 2353.64]  So if an access token is somehow shared with another device, you wouldn't be able to kind of swap it out and have it be put into the other person's phone because the access token is tied to that one device.
[2354.18 --> 2367.48]  And this is something that we are trying to do, solve in many different ways right now in the OAuth community of this idea of authenticating individual instances of the software with specific keys on each specific instance of an app.
[2367.48 --> 2370.78]  Again, it's not that it's impossible to solve it within the OAuth framework.
[2370.92 --> 2374.74]  It's that it's fighting the OAuth framework, trying to add that concept into it.
[2375.20 --> 2380.56]  So it ends up being harder to describe like I am struggling to describe right now.
[2380.74 --> 2389.22]  It ends up being harder to describe that because of the assumptions of OAuth being you have an OAuth client, it has an identifier, and that's just kind of the client.
[2389.54 --> 2394.48]  That is the client, but it's not really because there's an instance of the client that isn't really talked about in OAuth.
[2394.48 --> 2394.70]  Yeah.
[2395.24 --> 2401.66]  So with Gnap, it's flipping that completely on its head where there isn't really the concept of one group of software.
[2401.86 --> 2406.76]  Every client is an instance by default and has its own keys by default.
[2407.06 --> 2416.54]  And that is permeating the entire part of Gnap where you start the flow with your own keys that are assumed to not be shared with any other piece of software.
[2416.54 --> 2422.32]  And then you can take advantage of the fact that there are unique keys baked in from the beginning for each instance.
[2423.08 --> 2426.80]  So, yeah, it's not impossible to do these things in OAuth.
[2426.84 --> 2431.12]  And we do see people adding in those security features and bringing in those properties into OAuth clients.
[2431.60 --> 2434.64]  And you can definitely do it, but it is not how you would.
[2434.70 --> 2436.50]  It's not the easy way to do it.
[2436.54 --> 2439.10]  It's not the default way, and it's a lot harder to describe.
[2439.10 --> 2442.54]  You said Gnap was essentially starting over, right?
[2443.12 --> 2443.36]  Mm-hmm.
[2444.16 --> 2445.40]  Do you feel that's the best way?
[2445.48 --> 2447.02]  What are your thoughts on the direction?
[2447.16 --> 2452.26]  Obviously, you seem to be pro OAuth 2.1 or current 2.0.
[2452.84 --> 2454.22]  Where do you land on that?
[2454.30 --> 2455.18]  Are you for Gnap?
[2455.34 --> 2457.08]  What do you think is good or bad about it?
[2457.94 --> 2458.76]  Yeah, that's a good question.
[2458.96 --> 2464.26]  So I should also clarify, I am one of the editors of OAuth 2.1,
[2464.26 --> 2470.88]  meaning I'm participating in the development of that draft, which is progressing on standards track.
[2471.24 --> 2474.42]  I am also an editor on the Gnap spec.
[2474.70 --> 2480.58]  So I am involved in that work, and I do work with Justin and Fabian, the other editor, on that draft as well.
[2481.10 --> 2486.80]  So I do think that within the OAuth world, the OAuth 2.1 work is extremely important,
[2487.32 --> 2493.14]  and I do think it's worth doing that work, regardless of anything else that happens elsewhere.
[2493.14 --> 2498.64]  So I think that there's obviously a huge amount of software that's deployed with OAuth today,
[2498.84 --> 2503.02]  and it bakes in these assumptions, and it's fine, and it works,
[2503.38 --> 2507.06]  and it needs to be continued to be supported for a very long time.
[2507.46 --> 2514.30]  And I think that all of that stuff does benefit greatly from having a simpler definition of OAuth,
[2514.40 --> 2515.42]  which is OAuth 2.1.
[2515.88 --> 2517.44]  Now, totally separate from that,
[2517.44 --> 2529.18]  I think there's a lot of interesting opportunity with Gnap to make this work in ways that are easier to deploy in situations that we haven't necessarily thought of yet.
[2529.46 --> 2533.66]  So, for example, the device flow was not thought of at the beginning of OAuth,
[2533.70 --> 2536.16]  when OAuth was first created, and it's been added into it.
[2536.16 --> 2546.70]  And it fits into that world in a way that is definitely not the sort of natural way of doing it,
[2546.72 --> 2550.36]  because it has to rely on these assumptions that maybe don't apply in the device world.
[2550.84 --> 2555.88]  And I think we're going to see more of that happening in the future as more kinds of devices appear,
[2556.08 --> 2558.40]  and technology keeps evolving.
[2558.40 --> 2562.62]  One of the aspects of that is this whole idea of self-sovereign identity,
[2562.76 --> 2566.40]  which we're seeing as a huge community right now,
[2566.88 --> 2570.88]  using digital wallets for identities and things like that.
[2571.26 --> 2574.52]  None of that is very mature at the moment.
[2574.88 --> 2576.46]  It still feels very experimental.
[2576.98 --> 2582.92]  And a lot of it completely does not work with the assumptions of an OAuth world.
[2582.92 --> 2588.10]  So, you'll see people either completely not understanding OAuth from that world,
[2588.18 --> 2591.90]  because it doesn't match the underlying assumptions of how they're thinking about the world.
[2592.52 --> 2596.26]  And some people will try to sort of shoehorn OAuth into that model.
[2596.74 --> 2598.44]  So, what we're hoping is that with Gnap,
[2599.28 --> 2606.80]  it can be a better fit for a lot of the future developments of things that are maybe not even thought of yet.
[2607.20 --> 2609.58]  So, you think that work for 2.1 needs to happen no matter what,
[2609.66 --> 2611.08]  because OAuth is going to be around.
[2611.24 --> 2612.04]  It's not going to go away.
[2612.04 --> 2614.68]  So, we need to continue the work to stabilize things.
[2614.82 --> 2617.48]  But Gnap might be a better future.
[2618.24 --> 2619.18]  I think there's potential for that.
[2619.36 --> 2627.20]  And at the very least, I think there is potential for Gnap to point out some of the assumptions that OAuth is making
[2627.20 --> 2630.24]  that maybe we don't need to rely on anymore.
[2630.34 --> 2634.28]  Maybe there's ways to sort of backport some of that work into the OAuth world,
[2634.40 --> 2640.20]  if it can be demonstrated that those assumptions were holding back progress in other ways.
[2640.20 --> 2646.56]  And that kind of stuff is hard to do within a single working group because of how much legacy there is,
[2646.64 --> 2648.78]  of how much deployed and running code there is.
[2648.84 --> 2650.64]  Which, again, it's not that that's bad.
[2650.68 --> 2651.54]  I'm not saying that's bad at all.
[2651.58 --> 2654.78]  It's great that there's a lot of running code because that's what actually matters at the end of the day.
[2654.78 --> 2664.02]  What I don't like seeing is people not realizing what assumptions exist in a system and not being willing to challenge those assumptions.
[2664.32 --> 2670.02]  That is kind of why this has to end up happening in a new group because it's a lot easier to just say,
[2670.02 --> 2675.50]  well, we're just going to forget about all of those assumptions and start with a greenfield and then come up with something
[2675.50 --> 2680.78]  that hopefully does result in running code and useful in some deployed systems.
[2680.92 --> 2688.98]  But if not, maybe we can use that to point out some of the assumptions in OAuth that don't need to be there and should change in OAuth.
[2688.98 --> 2694.48]  What about the progression of using OAuth, moving from different spec to spec?
[2694.70 --> 2704.26]  So if OAuth 2 to OAuth 2.1, what is it like to be a developer to have to deal with that change or enable my application to be within that spec?
[2704.36 --> 2708.20]  Is it a challenge for a lot of developers to go from version to version?
[2708.76 --> 2709.12]  Yeah.
[2709.74 --> 2713.58]  Well, so OAuth 1 to OAuth 2 was a huge breaking change.
[2713.88 --> 2717.42]  Again, OAuth 1 had a bunch of assumptions that didn't make sense anymore.
[2717.42 --> 2720.58]  Like, mobile apps weren't really a thing when OAuth 1 was created.
[2720.88 --> 2723.48]  And it turns out OAuth 1 doesn't really work at all with mobile apps.
[2723.66 --> 2728.00]  So that was a huge breaking change and basically completely incompatible.
[2728.10 --> 2729.94]  And there's no way to, like, migrate.
[2730.20 --> 2731.58]  You have to just, it's from scratch.
[2731.64 --> 2732.60]  You write the code from scratch.
[2732.84 --> 2736.14]  And that's why Twitter, for example, still hasn't really switched over to OAuth 2.
[2736.22 --> 2737.22]  They're still on OAuth 1.
[2737.64 --> 2745.40]  And what we're hoping with OAuth 2 and what we've seen over the last now 10 years is that it's a lot of incremental changes,
[2745.40 --> 2747.00]  a lot of smaller incremental changes.
[2747.42 --> 2752.92]  So you don't need to support the device flow, for example, unless you need to support those devices.
[2753.04 --> 2755.98]  So you don't even need to worry about that spec unless you are building apps for a TV.
[2756.22 --> 2761.66]  But also things like Pixie, which it's not a new spec, but we are now hearing about it a lot recently
[2761.66 --> 2768.60]  because it is now recently being recommended for every kind of application, even web server-based applications.
[2768.60 --> 2775.94]  So adding Pixie in is not a ton of work by itself, and it is something you can add incrementally to a system.
[2776.56 --> 2782.12]  That's all just to say that OAuth 2.1 is not supposed to be something like, oh, you're going to have to go tear everything out and replace it.
[2782.36 --> 2792.78]  It's really supposed to be, well, it's very possible that the code you are running right now already is compliant with OAuth 2.1 if you've followed all of the recent guidance in OAuth 2.1.
[2792.78 --> 2801.74]  That's the goal is that hopefully there will be a set of people who don't have to make any changes and they will already be compliant with OAuth 2.1.
[2801.74 --> 2819.50]  This episode is brought to you by our friends at Square.
[2819.72 --> 2824.94]  For our listeners out there building applications with Square, if you haven't yet, you need to check out their API Explorer.
[2824.94 --> 2831.14]  It's an interactive interface you can use to build, view, and send HTTP requests that call Square APIs.
[2831.14 --> 2839.24]  API Explorer lets you test your requests using actual sandbox or production resources inside your account such as customers, orders, and catalog objects.
[2839.24 --> 2844.14]  You can use the API Explorer to quickly populate sandbox or production resources in your account.
[2844.52 --> 2847.74]  Then you can interact with those new resources inside the seller dashboard.
[2848.18 --> 2856.40]  For example, if you use API Explorer to create a customer in your production or sandbox environment, the customer is displayed in the production or sandbox seller dashboard.
[2856.40 --> 2864.20]  This tool is so powerful and will likely become your best friend when interacting with, testing, or playing with your applications inside Square.
[2864.44 --> 2873.28]  Check the show notes for links to the docs, the API Explorer, and the developer account sign-up page, or head to developer.squareup.com slash explore slash square to jump right in.
[2873.54 --> 2879.54]  Again, check for links in the show notes or head to developer.squareup.com slash explore slash square to play right now.
[2879.54 --> 2895.78]  So OAuth 2.1 says don't use the implicit flow.
[2896.64 --> 2897.12]  Why?
[2897.46 --> 2898.30]  What is it?
[2898.52 --> 2899.70]  Why avoid it?
[2900.70 --> 2902.04]  I already implemented it.
[2902.14 --> 2903.18]  Are you not supposed to use it now?
[2903.18 --> 2910.40]  Help us out with the implicit flow and then explain Pixie exactly what it solves and maybe how it works.
[2910.90 --> 2911.02]  Yeah.
[2911.12 --> 2917.80]  So the implicit flow is one of those things that I probably would recommend replacing, if at all possible, with the more secure flow.
[2918.70 --> 2921.72]  The implicit flow was always a hack.
[2921.84 --> 2926.22]  It was created as a workaround for limitations in browsers.
[2926.68 --> 2929.70]  Keep in mind, these are limitations in browsers from 2010.
[2930.26 --> 2932.10]  So the world is quite a bit different now.
[2932.10 --> 2933.52]  Browsers can do a lot more things.
[2934.04 --> 2937.68]  So the way the implicit flow works is the user clicks the link to log in.
[2938.10 --> 2941.66]  They're taken from the application over to the OAuth server.
[2941.90 --> 2943.44]  They log in there like normal.
[2943.60 --> 2944.76]  This is all the same in both flows.
[2945.08 --> 2955.58]  But when the OAuth server is ready to go and give the application an access token, it sends the access token in the address bar, in the URL, in the redirect back to the application.
[2955.82 --> 2959.70]  And the application will pull out of the URL and then start using it.
[2959.70 --> 2962.60]  So at first glance, you're like, cool, that seems very easy.
[2962.74 --> 2963.58]  It saves a step.
[2963.66 --> 2965.70]  I don't have to worry about this weird authorization code thing.
[2965.78 --> 2966.78]  I don't need a token endpoint.
[2967.22 --> 2970.48]  It's just one redirect there and one redirect back.
[2970.62 --> 2970.72]  Right.
[2970.72 --> 2973.28]  So why is that a problem?
[2973.28 --> 2981.18]  Well, in OAuth, we use these terms front channel and back channel.
[2981.74 --> 2989.10]  So the idea with a back channel is it's the sort of normal or default way that you're used to making requests on the Internet.
[2989.10 --> 2991.66]  It's an HTTP client to an HTTP server.
[2992.66 --> 2998.10]  And if you're using HTTPS, which you should be for almost everything these days, then that connection is encrypted.
[2998.48 --> 3005.84]  You know that when you send data and what you receive, it's all secure and encrypted in transit and you can trust the response that comes back.
[3005.84 --> 3010.78]  I like to think of that as hand delivering a message to somebody.
[3011.12 --> 3020.98]  So you can walk up to somebody, you can see them, they can see you, you can give them something, you can see they took it, and you know that nobody else came in and stole it because you can see they have it now.
[3021.72 --> 3022.60]  That's the back channel.
[3022.78 --> 3023.28]  That's great.
[3023.52 --> 3025.70]  We should use that as much as possible.
[3025.70 --> 3036.82]  The front channel is the idea of instead of an HTTP request from a client to a server, we're going to have two pieces of software exchange data through the user's browser.
[3038.18 --> 3042.60]  So that means we're actually going to use the address bar as a way to move data from one thing to another.
[3043.30 --> 3053.44]  So both OAuth flows, the authorization code flow and the implicit flow, start out in the front channel with the first request that the client makes is saying, here's what I'm trying to do.
[3053.44 --> 3055.92]  Here's who I am, here's what I'm trying to access.
[3056.46 --> 3059.62]  I would like you to send the user back to this redirect URL when they're done.
[3059.96 --> 3066.82]  That is a front channel message, meaning the application does not make that request directly to the OAuth server.
[3066.98 --> 3070.84]  It actually makes the request to the browser and tells the browser to go visit the OAuth server.
[3071.58 --> 3072.24]  That's fine.
[3072.40 --> 3072.64]  Great.
[3072.88 --> 3078.04]  Although I can explain some issues with that as well, which there is also solutions for.
[3078.04 --> 3083.64]  But the important one is on the way back where the OAuth server is trying to deliver the access token back to the application.
[3084.16 --> 3086.26]  Now, the secure way to do that would be in a back channel.
[3086.46 --> 3090.42]  But the OAuth server doesn't have a way to talk to the application in a back channel.
[3090.62 --> 3093.54]  The app might be running on a mobile phone or might be a single page app in a browser.
[3093.70 --> 3095.68]  And those are not an HTTP server.
[3096.02 --> 3098.00]  So they can't accept a back channel request.
[3098.46 --> 3105.54]  So instead, the OAuth server uses the front channel, putting the access token into the address bar, having the browser delivered to the application.
[3105.54 --> 3110.94]  I like to think of this as sending a letter in the mail where I'm trying to send you a message.
[3111.24 --> 3113.72]  I don't have a way to go and walk up to you to give it to you.
[3113.78 --> 3120.28]  So I instead put the message in an envelope and I put it in the mail and I trust that the mail carrier is going to deliver it to you.
[3120.66 --> 3122.18]  And there's a lot of trust there.
[3122.26 --> 3124.62]  There's a lot of inherent trust in the mail service.
[3125.26 --> 3126.28]  It'll probably work.
[3126.50 --> 3127.52]  It'll probably be fine.
[3127.76 --> 3131.12]  But I have no way to prove or guarantee that the message made it there.
[3131.12 --> 3138.24]  I also can't ensure that it wasn't copied in transit or stolen or tampered with, modified.
[3138.68 --> 3143.58]  I have no guarantee once the mail has left my hand and it's in the post office.
[3143.98 --> 3146.62]  So anytime we're using the front channel, it's that same situation.
[3147.16 --> 3149.68]  The OAuth server wants to give an access token to the client.
[3150.12 --> 3156.26]  Instead, it gives it to the browser to deliver to the client, which means now the OAuth server doesn't actually ever know if it really made it there.
[3156.26 --> 3160.68]  And think about if you get a letter in the mail, you have a similar problem on the receiving end.
[3160.94 --> 3164.96]  You don't actually have any guarantee that that letter is from who it says it's from.
[3165.58 --> 3168.26]  A return address isn't any proof at all.
[3168.48 --> 3175.40]  So if you ever get anything in the front channel, you can't be sure that it's actually from who you think it's from.
[3175.56 --> 3185.22]  Meaning if you get an access token in the front channel, you don't know if it's the access token you were expecting or if it's somebody trying to trick the application into accepting a different access token.
[3185.22 --> 3196.84]  So this is the problem with the implicit flow is that it actually sends the access token in the mail and there is no guarantee on the sending side that it's secure and no guarantee on the receiving side that it's actually the right access token.
[3197.30 --> 3199.32]  And there's not really a way around that.
[3199.82 --> 3206.94]  There's various patches you can do to solve one half of those problems, but not the other half.
[3207.26 --> 3210.12]  That's just inherently the problem with using the front channel.
[3210.12 --> 3219.24]  The implicit flow was created because of old limits in browsers, primarily the lack of ability to do cross origin requests.
[3219.94 --> 3222.68]  So back in the day, cross origin resource sharing wasn't a thing.
[3223.06 --> 3227.06]  So we use the implicit flow to avoid any sort of HTTP request.
[3227.20 --> 3229.72]  Instead, it's just using redirects, using the front channel.
[3230.08 --> 3230.86]  So clever hack.
[3231.24 --> 3231.98]  But hey, guess what?
[3232.06 --> 3236.34]  Browser's caught up and now we have cross origin resource sharing and it's not really a thing anymore.
[3236.34 --> 3239.38]  And it's no problem to make cross origin requests.
[3240.16 --> 3242.70]  So we don't need the implicit flow anymore.
[3243.10 --> 3246.14]  And we can't even solve all the security problems with the implicit flow.
[3246.34 --> 3248.00]  So it really just doesn't have a place anymore.
[3248.34 --> 3251.66]  That's the reason we're taking it out of the OAuth spec.
[3252.50 --> 3255.26]  So then I tracked all that.
[3255.32 --> 3257.44]  I don't know about you, Adam, but that was a good explainer.
[3257.70 --> 3258.74]  I think I'm with you.
[3258.94 --> 3259.58]  Yeah, it was awesome.
[3260.10 --> 3264.74]  Now go into what it's replaced with and why it fixes those problems.
[3264.74 --> 3268.52]  So this is definitely a challenge to do without diagrams.
[3269.30 --> 3272.06]  But this is hard mode podcast.
[3272.06 --> 3273.48]  Yeah, yeah, yeah.
[3273.96 --> 3279.26]  So the better solution is the authorization code flow, in particular with Pixie.
[3279.44 --> 3281.84]  So the way that works is it starts off the same.
[3282.08 --> 3285.88]  The app makes a front channel request to the OAuth server to start the flow.
[3286.40 --> 3290.50]  The user logs in like before, does two-factor auth, whatever they need to do.
[3290.50 --> 3297.16]  And instead of the OAuth server sending the access token back in the front channel, it still has to send something back in the front channel.
[3297.32 --> 3298.66]  Because it doesn't have a back channel connection.
[3299.26 --> 3304.40]  What it sends is a temporary one-time use short-lived code.
[3304.72 --> 3306.14]  And that's called the authorization code.
[3306.60 --> 3307.98]  This is why it's the authorization code flow.
[3308.28 --> 3308.30]  Okay.
[3308.30 --> 3310.90]  So that's what it sends in the mail.
[3311.40 --> 3314.64]  You can use this mail analogy to think about how this works.
[3315.04 --> 3322.18]  If you want to send somebody your house key and you put it in the mail, how good are you going to feel about that?
[3322.36 --> 3323.84]  Probably not very, right?
[3324.48 --> 3329.94]  Instead, it would be a lot better to put something in the mail where it doesn't matter if it's stolen because you can protect it in other ways.
[3329.94 --> 3340.68]  So instead of putting your actual house key in the mail, you can put a coupon, a temporary one-time use, go to this desk to redeem it kind of thing.
[3340.82 --> 3346.90]  And if somebody steals it, well, we can do other things in order to prevent it from being used by somebody who stole it.
[3347.80 --> 3353.74]  So an authorization code by itself is solving some of these problems, right?
[3353.74 --> 3357.58]  Where now at least the application gets this authorization code in the front channel.
[3358.02 --> 3359.84]  So it doesn't know where it's really from.
[3360.10 --> 3365.22]  And that isn't the access token yet, but it can go redeem it for an access token at the token endpoint.
[3365.66 --> 3367.26]  And it can do that in the back channel.
[3367.70 --> 3373.76]  So it can go and take that authorization code, make a back channel request over HTTPS to the OAuth server.
[3374.08 --> 3377.20]  And now it knows where it's talking to and it knows who it's talking to.
[3377.40 --> 3382.46]  And it can get the access token in the response from that HTTP request, meaning it's in the back channel where it is secure.
[3382.46 --> 3383.98]  That's great.
[3384.12 --> 3385.30]  That's the authorization code flow.
[3385.64 --> 3400.92]  The problem is that if we can't authenticate the client, then if someone steals that authorization code, because it was in the front channel where it's possible to be stolen, how do we know that it's actually their client that we thought we were sending it to?
[3401.36 --> 3401.72]  Right?
[3401.76 --> 3410.92]  If you send a coupon in the mail and someone steals it and they go to the desk to redeem it for your house key, how do you know that you aren't giving the house key to the wrong person?
[3410.92 --> 3412.62]  And that's where Pixie comes in.
[3413.16 --> 3420.80]  So Pixie attempts to solve this problem of not really knowing who is going to end up coming back with this authorization code.
[3421.02 --> 3429.32]  If you imagine you've just sent this coupon in the mail, you want to know that the person who received it is the same person that requested it.
[3429.66 --> 3430.20]  That's the key.
[3430.42 --> 3437.84]  The problem is that that request came in the front channel, which means you can't even actually really know who that request is from originally.
[3437.84 --> 3441.46]  So this is the sort of brilliant part about Pixie.
[3441.80 --> 3448.40]  Pixie uses a hash mechanism to work around this limitation of not being able to like have pre-registered secrets.
[3448.66 --> 3452.36]  So a hash, the idea with a hash, of course, is it's a one-way operation.
[3452.94 --> 3458.74]  So if I told you to think of 10 random numbers, write them all down on a piece of paper, and then add them up and tell me the sum.
[3459.00 --> 3461.00]  That is an example of a hashing algorithm.
[3461.22 --> 3462.02]  It's not a very good one.
[3462.28 --> 3463.22]  Please don't use it in production.
[3463.50 --> 3464.72]  But it is a hashing algorithm.
[3464.72 --> 3470.14]  Knowing just the sum, I would not be able to tell you which 10 numbers you chose.
[3470.36 --> 3473.92]  But if you tell me the 10 numbers, I can verify they add up to the same number.
[3474.46 --> 3484.36]  So it's a one-way operation, meaning you can take the hash and share that in a front channel where it may be observed or stolen because there's no way to reverse engineer it.
[3484.78 --> 3490.10]  So if we take that mechanism of a hash, we can add that into the flow.
[3490.10 --> 3497.22]  When the app first starts out, instead of just sending the user over to the OAuth server, it first creates a random string.
[3497.84 --> 3499.44]  And then it calculates a hash of that string.
[3499.90 --> 3501.78]  We actually use SHA-256 for this.
[3502.22 --> 3506.38]  So it calculates the hash, and it puts that hash in the front channel request to the OAuth server.
[3506.98 --> 3510.50]  So someone could observe that hash, but it's fine because they can't reverse engineer it.
[3510.96 --> 3512.66]  The OAuth server can remember the hash.
[3512.66 --> 3518.18]  And when it issues the authorization code, it knows what hash it saw when it issued that code.
[3518.44 --> 3527.34]  So now that coupon that it's sending in the mail, it knows a sum or the hash that it created when it issued that code.
[3527.78 --> 3536.16]  So now when someone is coming back with that authorization code, which it hadn't previously had a way to link up with the original request,
[3536.16 --> 3544.40]  in order to actually use the authorization code, whoever is using that code has to be able to prove that they control the hash that was used to request the code.
[3545.02 --> 3551.92]  And they can do that by providing the original secret, which the OAuth server can calculate the hash of and compare the two hashes.
[3552.22 --> 3555.20]  And the secret doesn't matter anymore because it's one-time use.
[3555.84 --> 3558.32]  It's one-time use, and that is over the back channel as well.
[3558.40 --> 3559.30]  Okay, fair.
[3559.30 --> 3559.70]  Yeah.
[3560.28 --> 3560.52]  Yeah.
[3561.16 --> 3573.96]  So what this means is that the OAuth server now knows that the thing that made the request with the authorization code is, in fact, the same thing that it sent the authorization code to in the front channel.
[3574.72 --> 3575.18]  Nice.
[3575.18 --> 3584.12]  So if we think back to our house key analogy, if you sent this coupon in the mail, you don't really know who it went to.
[3584.12 --> 3589.84]  But instead of just sending it off to somebody in the mail, it had to be requested by somebody.
[3589.94 --> 3593.26]  So the request that came in would include a number.
[3593.36 --> 3594.20]  It would include that sum.
[3594.66 --> 3598.12]  You could write that down, create this coupon, send that in the mail.
[3598.42 --> 3600.12]  You've still got this number you're holding on to.
[3600.50 --> 3606.30]  And now when someone comes back with that coupon to redeem it, they have to be able to prove they know that secret number.
[3606.54 --> 3607.78]  But it's not just a secret number.
[3607.86 --> 3613.34]  It's a hash, which means they have to actually know the actual 10 numbers that they chose to add up to that number.
[3613.34 --> 3620.50]  And then you know the person walking up to you at the desk is the person that actually made that first request on the phone, for example.
[3620.82 --> 3620.92]  Right.
[3622.52 --> 3624.62]  That's a pretty nice move.
[3624.64 --> 3626.44]  It's a clever little trick.
[3626.96 --> 3636.06]  Yeah, because you're making the front channel, which is inherently, I guess, insecure, secured because you're able to share the hash, which is publicly available fine.
[3636.06 --> 3641.20]  And then when you get to the back channel, as well as it just being a one-time use thing.
[3641.26 --> 3645.62]  But the back channel is necessary because you could have intercepted that on the way or something.
[3645.96 --> 3646.70]  So, yeah.
[3646.90 --> 3649.64]  We can use the back channel to provide the secret.
[3649.88 --> 3659.32]  Now, in most public key, private key, or where you have like a hash and a source operations, providing the secret is not something that you necessarily want to do.
[3659.32 --> 3664.34]  But because it is one time and you're proving who you were, all you're proving is that you made this request in the first place.
[3664.46 --> 3664.60]  Right.
[3665.26 --> 3667.38]  Then you can secure it that way.
[3668.34 --> 3668.38]  Exactly.
[3668.54 --> 3671.26]  This is not the same as actual public key authentication.
[3671.48 --> 3671.60]  No.
[3671.82 --> 3672.94]  And it's not intended to be.
[3673.00 --> 3685.94]  It is a much simpler mechanism because it's doing just one particular thing, which is tying the initial front channel request for a particular login to the particular request in the back channel for the access token.
[3685.94 --> 3686.30]  Right.
[3686.46 --> 3690.34]  It's not a, so every time the app starts this flow, it makes up a new secret.
[3690.54 --> 3692.16]  It's not part of the app's identity at all.
[3692.16 --> 3692.34]  Totally.
[3692.34 --> 3695.16]  It's just unique to this one instance of this one flow.
[3695.74 --> 3696.38]  So, yeah.
[3696.44 --> 3699.34]  Normally in public private key stuff, you don't share your private key at all.
[3699.58 --> 3700.58]  You assign things.
[3700.66 --> 3702.24]  But this is not that same thing.
[3702.28 --> 3705.34]  It just happens to be using a hash that is also often used in.
[3705.94 --> 3706.30]  Right.
[3706.42 --> 3707.92]  And you're generating a new one every time.
[3707.96 --> 3710.34]  Because all you're trying to say is, I was the original requester.
[3710.50 --> 3713.54]  But next time you do the request, it doesn't matter what those combos are.
[3713.54 --> 3713.84]  Right.
[3713.84 --> 3721.06]  Whereas if you had a singular private key and you give the public key out, you wouldn't send the private key, even if it was a back channel later.
[3721.64 --> 3721.84]  Yep.
[3722.00 --> 3727.84]  And this is actually kind of getting back to that, what we were talking about earlier, about client instances and the identity of clients.
[3728.28 --> 3728.30]  Totally.
[3728.30 --> 3728.32]  Yeah.
[3728.32 --> 3728.58]  Good point.
[3728.98 --> 3733.06]  Where in this model, the client authentication doesn't really matter.
[3733.22 --> 3734.16]  And that's not the point here.
[3734.22 --> 3740.58]  And that's why I was saying at the beginning that Pixie is not a replacement for a client secret and has nothing to do with whether or not you have a client secret.
[3740.58 --> 3748.24]  Pixie is useful to make sure that the thing that's requesting the authorization code is the same thing that's going to be using that authorization code later.
[3748.24 --> 3754.06]  If you have the ability to authenticate the client, then you absolutely should, even if you're doing Pixie.
[3754.74 --> 3757.14]  So that request for a token is over the back channel.
[3757.46 --> 3764.88]  So that request for the token over the back channel, that can be authenticated for clients that have credentials, meaning web server based apps.
[3764.88 --> 3770.50]  Or if you are doing per instance authentication of mobile apps, you can do it there as well.
[3770.58 --> 3773.44]  It would just be a per instance authentication of some sort.
[3774.52 --> 3780.10]  And that, again, it just has nothing to do with whether the Pixie is being used at all.
[3780.24 --> 3782.24]  It's a completely separate question.
[3782.88 --> 3785.44]  What's interesting, too, is how it seems to be pretty transparent to a user.
[3785.44 --> 3801.86]  So you mentioned before Apple TV, it gives you a code, you go to somewhere.com slash activate, you go to that browser to that on your phone, you log in, so you authenticate via, say, you know, your typical username and password, maybe, I don't know.
[3802.26 --> 3803.04]  Is that the scenario?
[3803.10 --> 3805.48]  That's the kind of scenario where Pixie is playing a role.
[3805.48 --> 3816.82]  So it's pretty transparent to that end user where all I'm doing is typing in that six character string that the Apple TV told me, went to my browser in the phone, and it's pretty transparent from a user perspective.
[3817.46 --> 3818.68]  Well, Pixie isn't even visible.
[3818.94 --> 3820.70]  Pixie isn't even visible to the end user, right?
[3820.70 --> 3821.20]  Right, exactly.
[3821.46 --> 3823.82]  It's all just behind the scenes stuff.
[3824.08 --> 3834.14]  The point I'm trying to make, too, is that that's good because the more trouble you put in front of a user to be, I suppose, secure or to use authentication, the more they're going to write their password down.
[3834.14 --> 3839.96]  You know, on their monitor or, you know, circumvent the system or just not use it and be insecure anyway.
[3840.12 --> 3849.76]  So the cool thing is that this protocol, this spec, allows developers to make these things where users don't get fatigued by the process of authentication.
[3850.24 --> 3852.34]  You can still do it, and it's not a challenge.
[3852.64 --> 3856.44]  Kind of a pain to open my phone, go to slash activate, you know, throw in that code.
[3856.44 --> 3864.44]  But I prefer that over, say, swiping my finger back and forth on the Apple TV, you know, as an example, to use that example.
[3864.74 --> 3870.70]  It's very fatiguing as a user to make my friends wait or make my wife wait or whatever while I log in.
[3870.70 --> 3880.48]  It can be done sort of quickly because I have a lot more identity and presence on my phone that secures me to it to know that I can give that code back to the site.
[3880.48 --> 3882.14]  So you did it.
[3882.20 --> 3883.74]  You explained to us without diagrams.
[3883.94 --> 3885.70]  I think you have diagrams somewhere.
[3885.96 --> 3889.52]  So let's not make this the only resource for people.
[3890.24 --> 3892.22]  Do you want to learn the new OAuth 2?
[3892.48 --> 3894.38]  Not the new, but the preferred OAuth 2 things.
[3894.42 --> 3897.36]  You have to listen to the third part of this one episode of the changelog.
[3897.80 --> 3898.96]  No, there's other resources.
[3899.58 --> 3901.04]  Aaron, point us towards them.
[3901.12 --> 3904.48]  I know you have, I think you have a book on OAuth 2 Simplified.
[3904.66 --> 3905.86]  There's guides.
[3906.06 --> 3907.38]  There's cheat sheets.
[3907.38 --> 3912.56]  How can people visualize this and learn it, you know, on their own time?
[3913.18 --> 3914.86]  Yeah, I've got a lot of resources available.
[3915.12 --> 3920.08]  So the book that I wrote, OAuth 2 Simplified, it is at OAuth2simplified.com.
[3920.20 --> 3921.64]  You can find links to purchase it there.
[3922.12 --> 3925.82]  It is actually also, the contents of the book are on OAuth.com.
[3925.94 --> 3928.30]  That is the sort of web-based version of the book.
[3928.60 --> 3930.86]  That website is sponsored by Okta.
[3931.28 --> 3934.02]  And I also have a video course about OAuth.
[3934.02 --> 3936.98]  And that's where we walk through step-by-step all the flows.
[3937.48 --> 3941.20]  There's a whole bunch of exercises in there to actually try this stuff out yourself as well.
[3941.66 --> 3945.02]  You can find the link to that one also at OAuth2simplified.com.
[3945.52 --> 3948.78]  The OAuth course is called The Nuts and Bolts of OAuth.
[3949.00 --> 3949.54]  Very good.
[3949.82 --> 3952.62]  We have Developer Day coming up from Okta, which is kind of cool.
[3952.92 --> 3953.96]  We'll be doing some talks there.
[3954.02 --> 3954.70]  What else has happened there?
[3954.72 --> 3956.56]  I think you mentioned labs and the pre-call.
[3956.92 --> 3957.66]  What other fun things?
[3957.70 --> 3960.28]  We haven't even mentioned that on this podcast yet, but...
[3960.28 --> 3961.34]  Developer Day will be a lot of fun.
[3961.34 --> 3963.32]  That is on August 24th.
[3963.40 --> 3966.42]  And the first day is going to be a bunch of really interesting talks.
[3966.42 --> 3971.26]  Not just about OAuth, about all sorts of web stuff and API and authentication.
[3971.94 --> 3974.78]  And I'll be doing a talk there with Vittorio from Auth0.
[3975.04 --> 3975.84]  So that'll be fun.
[3976.18 --> 3978.22]  Always a good time chatting with him.
[3978.22 --> 3982.62]  And then the day after the sessions are the labs.
[3983.08 --> 3985.46]  And that is a full day of hands-on activities.
[3985.76 --> 3986.84]  It is entirely free.
[3987.50 --> 3990.10]  And actually, they'll be streamed to YouTube as well.
[3990.18 --> 3991.44]  So you don't even need to register for those.
[3991.52 --> 3992.18]  You can just show up.
[3992.84 --> 3996.12]  And that's going to be starting at 8 a.m. Pacific, ending at 5.30 p.m. Pacific.
[3996.26 --> 3997.68]  Every 90 minutes will be a different topic.
[3998.22 --> 4001.74]  I will be kicking things off with a walkthrough of OAuth.
[4001.82 --> 4005.68]  We'll do exactly what we just talked about here of walking through Pixie step-by-step
[4005.68 --> 4007.80]  against a real OAuth server.
[4007.80 --> 4011.40]  You'll be spinning up a little OAuth server and trying to get an access token.
[4012.54 --> 4015.26]  And I'll be there live and helping you through it.
[4015.78 --> 4019.26]  And then the rest of the day, we've got all sorts of fun events as well.
[4019.54 --> 4021.04]  There'll be a session from Auth0.
[4021.38 --> 4025.70]  We'll be doing stuff with Terraform and Kong and JFrog.
[4026.28 --> 4028.04]  So a lot of good sessions there.
[4029.02 --> 4030.48]  Sounds cool to me.
[4030.58 --> 4032.34]  Well, we do want to give a shout-out to Barat.
[4032.42 --> 4033.46]  They call him All Business.
[4033.72 --> 4037.34]  All Business Barat over there for introducing us to you, Aaron.
[4037.34 --> 4039.62]  And this has been an absolute joy.
[4040.02 --> 4041.84]  You do a great job explaining these things.
[4042.16 --> 4043.38]  I mean, it's hairy.
[4044.80 --> 4046.36]  It's hairy technical details.
[4047.00 --> 4048.94]  And that's kind of the onus of this conversation.
[4049.10 --> 4051.94]  It's like, hey, OAuth is complicated.
[4052.60 --> 4053.68]  Why is it complicated?
[4053.84 --> 4055.10]  There's reasons for that.
[4055.10 --> 4064.40]  I think you did a good job explaining a little bit of the history and how things have changed over time and how you're not going to land on the perfect API or spec the first time anyways.
[4064.96 --> 4068.74]  So you have to learn as you advance.
[4068.92 --> 4071.62]  And that means that things got a little bit complicated.
[4071.62 --> 4073.28]  But now they're becoming a little more simplified.
[4073.84 --> 4076.70]  And there's a bright future ahead for authentication on the web.
[4077.26 --> 4080.54]  Anything else that we didn't ask you or you wanted to touch on before we called a show?
[4081.02 --> 4081.70]  That sounds great.
[4081.94 --> 4082.86]  Developer Day will be fun.
[4083.04 --> 4088.22]  Oh, I do have a show that I do with Vittorio on YouTube, the OAuth Happy Hour.
[4088.22 --> 4091.28]  And it is approximately monthly.
[4091.80 --> 4099.88]  And we just chat for an hour about OAuth and talk about what's new in the OAuth world, what's been happening with the specs.
[4100.10 --> 4104.94]  We get into some of the details of some of the extensions that are brand new and still being worked on.
[4105.68 --> 4107.18]  And it's a lot of fun.
[4107.24 --> 4108.16]  This is a live stream on YouTube.
[4108.68 --> 4112.66]  You can check out the schedule for that at octadev.events.
[4113.30 --> 4115.84]  There are links to the upcoming episodes there.
[4115.84 --> 4117.74]  And we schedule them usually a few months ahead of time.
[4118.22 --> 4118.54]  Cool.
[4118.66 --> 4120.00]  And yeah, a lot of fun.
[4120.34 --> 4121.26]  Come bring your questions too.
[4121.34 --> 4123.66]  We'll answer questions from the chat if you show up.
[4124.22 --> 4124.42]  Yeah.
[4124.58 --> 4124.98]  There you go.
[4125.08 --> 4126.02]  Show up and ask questions.
[4126.64 --> 4127.08]  That's cool.
[4127.24 --> 4129.94]  Is drinks required or the optional?
[4130.78 --> 4131.46]  Drinks are optional.
[4131.88 --> 4132.86]  Bring whatever you want to drink.
[4133.62 --> 4136.74]  We may even be able to hook you up with some drinks soon.
[4136.82 --> 4138.02]  I'm working on making that happen.
[4138.68 --> 4138.96]  Nice.
[4139.14 --> 4139.30]  Cool.
[4139.82 --> 4140.36]  It's been fun.
[4140.60 --> 4141.70]  Aaron, thank you so much for your time, man.
[4142.00 --> 4142.68]  Thanks for having me.
[4142.76 --> 4143.62]  It's been really fun.
[4146.02 --> 4146.70]  All right.
[4146.70 --> 4148.42]  That's it for this episode of the ChangeLog.
[4148.48 --> 4149.60]  Thank you for tuning in.
[4149.60 --> 4153.64]  We have a bunch of podcasts for you at changelog.com.
[4153.68 --> 4154.32]  You should check out.
[4154.54 --> 4155.56]  Subscribe to the Master Feed.
[4155.68 --> 4158.22]  Get them all at changelog.com slash master.
[4158.34 --> 4160.70]  Get everything we ship in a single feed.
[4161.06 --> 4165.04]  And I want to personally invite you to join the community at changelog.com slash community.
[4165.30 --> 4166.20]  It's free to join.
[4166.44 --> 4167.54]  Come hang with us in Slack.
[4167.78 --> 4169.92]  There are no imposters and everyone is welcome.
[4170.34 --> 4173.38]  Huge thanks again to our partners, Linode, Fastly, and Launched Darkly.
[4173.38 --> 4177.22]  Also, thanks to Brake Master Cylinder for making all of our awesome beats.
[4177.62 --> 4178.74]  That's it for this week.
[4178.94 --> 4179.88]  We'll see you next week.
[4179.88 --> 4209.86]  We'll see you next week.
[4209.88 --> 4210.88]  Game on.
[4210.88 --> 4222.88]  Game on.
