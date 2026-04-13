[0.00 → 2.80] I'm Matt Mullen wake, and you're listening to The Change Log.
[11.40 → 15.78] Welcome back everyone. This is The Change Log, and I'm your host Adam Stachowiak.
[15.94 → 25.88] This is episode 197. Big show today. We got Matt Mullen wake online to talk about the past, present, and future of WordPress.
[25.88 → 32.50] We talked about the role of JavaScript for WordPress, their new REST API. We asked Matt to predict the future.
[33.00 → 38.92] Matt went all the way to 2025 and tried to decrypt what might happen for WordPress as well as the web.
[39.30 → 42.26] Calypso, we talked about that and so much more.
[42.76 → 49.22] We had three awesome sponsors, DigitalOcean, Rollbar, and BMC's True Sight Pulse.
[49.84 → 53.52] If you haven't subscribed to our emails yet, you should do it now.
[53.52 → 58.82] Go to changelaw.com slash weekly and changelaw.com slash nightly.
[58.94 → 62.50] Those are our two awesome emails everyone loves.
[62.68 → 64.50] Every week we send out Change Log Weekly.
[64.64 → 69.64] It's our editorialized take on what happened this week in open source software development.
[69.78 → 74.12] We share tons of articles and resources that hit our radar every single week,
[74.18 → 80.64] as well as repositories, videos, and even some contributed projects on our ping repo.
[80.64 → 84.04] So, change all nightly happens to be our own radar.
[84.46 → 90.22] Very often we're pulling out projects or talking to people from that email.
[90.38 → 97.66] Every single night people get that email at 10 o'clock Central Standard Time and love change all nightly
[97.66 → 103.56] because it keeps them up to date on what's happening every single day on GitHub in open source.
[103.56 → 107.98] Once again, changelaw.com slash weekly, changelaw.com slash nightly.
[108.42 → 108.86] Subscribe.
[109.54 → 111.00] And now, on to the show.
[118.18 → 123.38] Alright, we're joined today by Matt Holloway to talk about the past, the present, and the future of WordPress.
[123.68 → 126.06] This thing called Calypso, which we heard about this year.
[126.54 → 128.90] His thoughts on open source and so much more.
[128.90 → 132.34] We also have Jared Antoni call, so Jared, say what's up, my friend.
[132.96 → 133.48] What's up?
[133.54 → 133.94] What's up?
[134.22 → 138.84] Adam, I was going to ask you, is this, can we get some of the praise out of the way right up front for Matt?
[139.04 → 139.72] Is that cool with you?
[140.34 → 140.94] What do you mean?
[141.22 → 142.30] I have some praise for him.
[142.32 → 144.34] I just like to get it out of the way so we can have a...
[144.34 → 144.76] Do it.
[145.14 → 148.86] Okay, so Matt, you probably hear this a lot, but that's not going to stop me.
[150.56 → 155.70] WordPress was actually kind of how I got into the web development game back in, gosh, 2005, 2006.
[155.70 → 156.92] Oh man, me too.
[157.34 → 159.64] And so I wanted to thank you and say it's awesome.
[160.24 → 172.40] My initial web dev was like me basically pimping my blog, which was a WordPress blog, and I learned all sorts of things about how to change plugins and, you know, just kind of got my start on WordPress.
[172.62 → 173.50] So thanks much for that.
[173.66 → 175.20] Oh man, I'm saying the same thing, Matt.
[175.22 → 176.78] That's my story too, what Jared said.
[178.06 → 179.06] How's that make you feel?
[179.86 → 180.56] Perfect.
[180.76 → 182.76] That's a fantastic way to kick things off.
[182.76 → 186.24] My story is a little bit different from Jared.
[186.30 → 193.60] I was more on the front end than, I guess, the PHP plugins, which was still there, of course, but less when I got into it, which was 2004.
[194.64 → 198.56] And what really drew me to WordPress even deeper was Kubrick.
[198.94 → 201.52] And then like a year later, you made Kubrick the official theme.
[201.60 → 202.46] So that was a big deal.
[202.62 → 204.72] And it's kind of crazy to go back in time.
[204.72 → 206.66] I didn't expect that at the beginning of the show.
[206.74 → 208.66] And you just, you blew my mind, man.
[208.66 → 216.02] It's funny to look back at that theme too, because now it seems so dated, but it was very, very innovative at its time.
[216.44 → 216.66] Yeah.
[217.92 → 218.68] Who was it?
[219.74 → 220.50] Christian Hillman.
[220.74 → 221.40] Is that how you say his name?
[221.62 → 221.92] Hillman?
[222.28 → 222.94] Michael Hillman.
[223.28 → 223.46] Yeah.
[224.00 → 227.28] He, I think, is he still at Squarespace now?
[227.44 → 228.64] I don't know, but he was an awesome designer.
[228.84 → 229.62] I liked his stuff.
[229.90 → 230.78] That's a good question.
[230.90 → 232.64] I haven't caught up with him lately.
[232.64 → 240.56] But actually, when he was working on his visa, I wrote him a letter to help him be able to work in the U.S. at Squarespace.
[241.12 → 241.52] Very cool.
[241.76 → 242.16] Very cool.
[242.58 → 245.30] Well, it's certainly great to finally get you on the show, Matt.
[245.34 → 251.56] It's literally been, as you can tell, years in the making, even beyond the show as it has come out.
[251.70 → 252.66] But welcome to the show.
[252.76 → 257.98] This is, it's been so long since we've been actually waiting to get you on the show, because the show's been around for a while.
[257.98 → 262.98] And we've obviously covered open source for a while, but it just never came to the point where we can actually get you on the show.
[263.04 → 264.22] But this is a good time.
[264.26 → 264.78] What do you think?
[265.80 → 266.56] Never been better.
[266.78 → 267.38] Never been better.
[267.84 → 270.70] So there's a little history, I guess, for you as well as the listeners.
[270.82 → 275.26] We relaunched our blog on WordPress from Tumblr a while ago.
[275.32 → 276.96] So we've obviously been invested on WordPress.
[277.18 → 277.74] We love WordPress.
[278.02 → 280.52] Jared and I both just told you our roots are on WordPress.
[280.52 → 282.56] But even before that, we wanted to get you on the show.
[282.56 → 295.96] And now with Calypso and you're shaking things up a bit, we thought this would be a great time to really have a conversation I think our listeners love to hear about, which is like not just a project and what you're doing, but kind of behind the scenes.
[296.06 → 302.42] Who you are, where you come from, a bit of history on Matt Mullenweg, where WordPress came from, all that good stuff.
[302.42 → 309.78] But before we dive deep into that deep subject, maybe you can kind of just catch folks up with the recent announcement of Calypso.
[309.78 → 313.32] It's a very exciting time to be in the WordPress world.
[314.10 → 324.20] There's a lot happening around APIs and everything, but there was this project that was about 20 months in the making before the first release, which was in generally the automatic.
[324.20 → 334.14] We saw that the technical foundation that WordPress was based on wasn't the one I could imagine us building the next 10 years of a great user experience on.
[334.14 → 342.48] And so we took a look at the landscape, what the best and worst technologies were, what we liked and didn't about our current technology stack.
[343.08 → 348.36] And if there's anything about WordPress developers and the type of automatic, I would say is that we're very, very pragmatic.
[348.36 → 357.10] So we look at technology for tech as a means to an end, not necessarily as something for its own sake.
[357.72 → 372.18] And what we came to was that if we were able to basically have a version of the WordPress interface that worked purely over HTTP APIs and was written in JavaScript 100% top to bottom,
[372.18 → 380.44] we could create a really, perfect user experience that was, you know, not just a few bits above, but actually 10x what we have today.
[381.02 → 383.04] So that's what we did.
[383.08 → 385.36] And we released it November 2015.
[385.44 → 387.52] And the adoption has been very exciting so far.
[387.70 → 388.10] Wow.
[388.36 → 391.86] Well, that certainly tees up quite the conversation we're going to have.
[392.28 → 400.54] So listeners, rest assured, we're going to dive deep into JavaScript specifically, Calypso, what that means, Node.js, a lot of the stuff you just mentioned there, Matt.
[400.54 → 407.30] So I thought it'd be good to start off with at least some sort of notion of what recently happened, in your own words, around Calypso.
[407.64 → 414.94] But, you know, another thing is to give the popularity and duration of WordPress, we couldn't start the show-off proper without digging into the history of things.
[415.12 → 422.94] And so, Jared, correct me if I'm wrong, but one of the things we've been doing a lot lately has been, especially with folks like Matt who come on the show,
[422.96 → 429.82] rather than just jump into the tech and some of the details around that, we kind of go a little deeper and figure out what the origin story is of someone.
[429.82 → 440.18] So I don't know how often, Matt, you get a chance to share this kind of information, but we're really curious where things begin for you, not just with WordPress, but like in software development.
[440.32 → 445.50] Like what was the earliest thing you can kind of take us to that got you into tech, got you into software development?
[446.54 → 446.80] Huh.
[446.80 → 451.10] Well, my father's always been in computers.
[451.62 → 461.78] So, you know, from a very young age, there was always a computer around the house, and he would program mostly for oil companies like Brown and Root, places like that.
[462.50 → 465.28] And so, yeah, just having technology around the house.
[465.28 → 473.66] The earliest things I remember was really just video games, but I think that was a good introduction because it was a lot of fun.
[473.76 → 475.74] So it got me interested into how to tweak things.
[475.98 → 485.62] And a lot of early video games you could tweak, like you could create maps for them or modify it or open the code and see how it works and tweak it a little bit.
[485.70 → 486.88] So all that was pretty fun.
[486.88 → 489.34] Was it a game or something like that that got you originally?
[489.48 → 491.56] What was the first piece of code you think you touched?
[493.20 → 498.16] It might have been one of the Ultima games or something like that.
[498.64 → 499.66] But I don't remember exactly.
[500.30 → 509.88] The first code I remember writing like a full program from scratch was actually in my middle school had a bunch of the old Macintoshes.
[510.38 → 512.10] And I was very into music at the time.
[512.10 → 517.56] And the teacher, I kind of gone through a lot of the early lessons.
[517.86 → 520.48] And actually a lot of what we did in class was just play Oregon Trail.
[521.74 → 530.50] But so I got kind of into programming and made a little program, you know, probably using HyperCard or something that I figured out.
[530.78 → 532.66] All it had was like a little tone generator.
[532.66 → 545.34] But if you could tell at like 44,000 hertz and a duration, you could essentially program in music to come out of this little, not even MIDI, like, you know, very much a tone generator type thing.
[545.86 → 551.04] So I started, made a little program and programmed in like for Elise and a few other classical songs.
[551.30 → 553.54] And so you press a button, and we play the song.
[554.08 → 559.30] Well, that's kind of where you and I differ, Matt, because I was right there with you with the Oregon Trail.
[559.30 → 562.76] But my problem is that's all I accomplished was Oregon Trail.
[563.76 → 571.74] Well, it was very cool to learn about music, especially the relationship between frequencies and notes, you know, because music is very mathematical.
[572.54 → 575.12] And obviously programming is so mathematical as well, right?
[575.50 → 577.90] You know, I don't use very much math.
[578.90 → 580.52] I generally want to program.
[580.52 → 593.34] So I also have here in our notes, Matt, which is maybe pretty well known since there's usually a Texas silhouette behind the WordPress logo sometimes out there.
[593.40 → 597.76] I've seen a couple of stickers out there flying around that have the WordPress logo in Texas.
[597.76 → 599.86] But you're Texan originally, right?
[600.54 → 600.66] Yeah.
[600.70 → 601.92] Born and raised in Houston, Texas.
[601.92 → 607.46] And that was where, you know, where I worked on the early versions of WordPress from.
[607.46 → 611.22] And I'm assuming you went to the University of Houston right here in Houston.
[611.86 → 612.48] I did.
[612.68 → 612.86] Yeah.
[613.36 → 615.46] And what did you study when you were in college?
[616.36 → 617.78] Political science, actually.
[618.36 → 620.22] So way different from what you're doing now.
[620.28 → 621.52] I guess kind of not really.
[621.64 → 623.46] It's somewhat similar.
[624.36 → 625.32] You're in politics in a way.
[625.76 → 625.92] Yeah.
[625.92 → 628.62] Open source has way more to do with people than it does with code.
[628.80 → 629.24] That's true.
[629.50 → 630.00] That's true.
[630.00 → 638.86] So I guess when you were back in those days, could you imagine the journey to where you're at now?
[638.96 → 647.44] I mean, does what you've done, not just you alone, but obviously with a huge amount of people who love WordPress and love what's come from the work you've started.
[647.90 → 652.56] Could you imagine the, you know, everything that's kind of transpired since then?
[652.56 → 660.06] I would definitely say from the early days, there was really no conception of it being even a tenth of what it is today.
[660.72 → 664.18] But very much the next steps were always obvious.
[664.92 → 670.96] And the entire team was unified by a desire to take something that was difficult and make it easier.
[670.96 → 675.42] To take things that were inaccessible and make them accessible to a wider audience.
[675.88 → 684.52] Operating under the assumption that the more people publishing, the more people who felt this power over their web presence, the better place the world would be.
[686.12 → 690.60] So take us back to those first few steps that weren't quite so intentional.
[691.68 → 695.20] Looks like it was maybe 2002, early 2003.
[695.20 → 703.12] WordPress started out as a fork of another open source project, I believe, called B2 slash Café Log.
[703.56 → 704.28] Can you tell us about that?
[705.44 → 705.84] Yeah, totally.
[705.98 → 709.52] And it's something, you know, the audience of this podcast will probably appreciate a lot better.
[710.74 → 716.88] Yeah, originally, so I started blogging by reading blogs, like many people.
[717.02 → 718.82] And blogs were pretty popular around this time.
[718.82 → 726.50] And all the blogs that I read used software called Movable Type, which wasn't open source, but it included the source code.
[726.70 → 727.88] It was a Perl script, essentially.
[728.50 → 735.26] So even though it wasn't open source licensed, it was kind of open enough for most people.
[735.42 → 742.30] And it actually had a pretty good ecosystem around it of people writing tutorials and making plugins and doing things like that.
[742.30 → 749.60] But the Perl approach of Movable Type, particularly how it would statically rebuild the site.
[749.76 → 756.08] So when you made a new post, it would generate a bunch of HTML files, like a new one for your homepage, for your archives pages, for everything.
[756.62 → 761.98] And it's kind of cool that it automated this, you know, because it was doing, it literally was almost like a faster horse.
[762.12 → 768.40] Like it took what people used to do manually around blogging, just updating a bunch of pages on their site, and just made it faster.
[768.96 → 770.76] But it seemed still a little bit clunky.
[770.76 → 772.70] I wanted a car, not just a faster horse.
[773.44 → 781.82] And so I came across B2, which was a lot simpler and certainly had a much, much smaller user base than Movable Type.
[782.68 → 787.58] But, you know, to me, the code was very easy to understand and grasp.
[787.90 → 789.32] It wasn't very complicated.
[789.64 → 790.82] It wasn't very nested.
[792.08 → 794.96] And it just kind of did one thing, which is blogging, and it did it well.
[795.70 → 797.08] And I really took to that.
[797.08 → 799.94] And so it converted my site to be B2 powered.
[799.94 → 804.92] And then got active just with the not even with the project as much as the forums.
[805.52 → 807.22] I was really into forums at the time.
[807.34 → 811.32] I'd run a few different forums and participated on some web design forums and things.
[812.00 → 814.68] And so when I came across the B2 forums, I was like, oh, cool.
[814.68 → 817.58] So I both can, I asked a ton of questions.
[817.80 → 820.44] And I just started helping other people where I could.
[821.26 → 822.64] I'm kind of curious about the name.
[823.28 → 825.68] You know, B2, WordPress.
[826.56 → 827.96] And that's what his fork was.
[828.02 → 829.84] But, you know, where did this word come from?
[829.90 → 831.04] How did you come up with that?
[831.04 → 831.48] Yeah.
[832.02 → 835.02] So B2 is interesting because it had kind of a dual name.
[835.12 → 839.52] So B2 was, I think, a reference to it being like a better version of Blogger.
[840.28 → 843.42] So Blogger being B1 and this being B2.
[843.76 → 844.04] Nice.
[844.44 → 847.86] It also had a secondary name, which was Cafe Log.
[847.86 → 850.92] So the domain was CafeLog.com.
[851.40 → 854.44] The SourceForge, you know, username was Cafe Log.
[854.52 → 858.22] That was because the username and domain B2 was not available.
[858.22 → 861.44] So a lot of people referred to it like with a slash.
[861.58 → 863.08] It was B2 slash Cafe Log.
[863.50 → 866.80] And in fact, most people weren't sure exactly what to call it.
[866.90 → 870.82] So I knew that when naming this new thing, I wanted it to only have one name.
[872.28 → 874.04] So where did the name come from then?
[874.14 → 875.96] Like, how did you get there?
[877.00 → 879.38] You know, it was actually a lot of thinking.
[880.20 → 884.54] So there was, at the time, like I said, I was into blogging.
[884.54 → 891.76] And there was like a Houston blogger group that would get together kind of like once a month, usually for drinks.
[891.76 → 896.84] So I would have to go to the bar like four or five hours early before they started checking IDs.
[897.16 → 899.64] A place like Flying Saucer or something like that.
[899.64 → 900.20] Oh, Flying Saucer.
[900.28 → 900.98] That's a good place.
[901.44 → 901.74] Yeah.
[901.74 → 904.98] But these people are super cool.
[905.22 → 908.30] And it was exciting for me to connect with other bloggers.
[909.02 → 910.72] Because that was primarily what I was doing at the time.
[910.80 → 911.84] I was just blogging.
[912.18 → 913.88] You know, I blog like a couple of times per day.
[914.06 → 915.16] Way more than I do now even.
[916.56 → 921.04] And one of the folks was Christine Slick, now Trimble.
[922.02 → 927.12] And, you know, of course I was telling everyone in the group like this thing I was working on and why they should switch it to it.
[927.22 → 928.76] No one used B2 or WordPress.
[928.96 → 930.74] They all used Movable Type or Blogger.
[931.16 → 932.54] But, you know, I talk about it constantly.
[933.44 → 935.76] And, you know, they were really nice to me and stuff.
[936.12 → 938.24] And Christine just called up one day, and she's like, ah.
[938.66 → 941.32] She knew I was kind of waiting for a name or trying to find a name.
[941.38 → 942.20] She's like, I have it.
[942.68 → 944.42] And I even checked the domains available.
[944.94 → 945.98] And it was WordPress.
[946.28 → 946.52] Wow.
[946.52 → 948.24] And the .org was available.
[948.78 → 951.60] And so I just registered it right there on the phone.
[952.10 → 953.32] Probably GoDaddy or something.
[954.06 → 956.66] And that was kind of off to the races.
[957.14 → 957.34] Wow.
[957.46 → 960.18] So you registered the .org first, not .com?
[960.70 → 962.02] Yeah, the .com was taken.
[962.50 → 962.78] Wow.
[962.94 → 963.22] Okay.
[963.60 → 966.60] So I think I got the .org and the .net.
[967.28 → 967.64] Nice.
[968.02 → 975.36] So one thing that you did keep going in, and maybe you can touch on exactly how long it took to get to this moment, but is that you got traction.
[975.36 → 979.36] And so we, you know, our audience is software developers, open sourcers, of course.
[979.98 → 991.40] And one thing that we find very interesting in general, I mean, I think a lot of people do, even in the startup community, is like the idea of getting traction for something that you are doing or something that you believe in.
[991.40 → 998.72] And you mentioned that you're, you know, going to these meetups and talking to people about WordPress or even pre-name or naming it.
[1000.30 → 1001.64] But what happened?
[1001.76 → 1006.00] Like, where did, how did it snowball, and how did WordPress get the traction that it got?
[1007.02 → 1013.92] Well, I think part of what the story illustrates is from, from the very, you know, even before day one, WordPress was a community project.
[1013.92 → 1019.06] You know, the name came from other folks, the ideas, everything.
[1019.88 → 1026.46] And a lot of what we've done through history is not doing something the first, but trying to do it the best.
[1027.12 → 1033.10] Where it started to tip off actually goes back a little bit to, you know, what I was talking about earlier with movable type.
[1033.10 → 1039.50] So movable type, like I said, it was open but not open source.
[1040.18 → 1045.58] They decided to release a new version of the software that didn't really add a ton of features.
[1045.74 → 1050.70] It was a little bit of a rewrite version and, but had an expensive upgrade path.
[1051.42 → 1058.82] So it's kind of a double whammy where they didn't add a lot, and they didn't, you know, they wanted to charge people for it.
[1058.82 → 1063.96] And of course having a customer base, which is, it's almost like you sell megaphones, right?
[1064.00 → 1067.94] When you make blogging software, all of your customers are publishers.
[1068.54 → 1068.62] Right.
[1068.76 → 1072.02] So all of their customers published how unhappy they were.
[1074.62 → 1075.34] That's so funny.
[1075.44 → 1076.18] I never thought about that.
[1076.28 → 1080.88] Like it, you obviously, if you upset the blogger sphere as it was called back in those days.
[1080.88 → 1083.10] And I don't know, I don't think it's still referred to as that anymore.
[1083.28 → 1085.32] It's just more like the people who blog.
[1085.54 → 1085.86] I don't know.
[1086.16 → 1086.94] Now it's just the web.
[1087.10 → 1087.58] The web.
[1087.58 → 1088.02] Yeah.
[1088.02 → 1088.14] Yeah.
[1088.42 → 1089.20] It's expected.
[1089.30 → 1093.92] It's the de facto, but you don't want to make those people mad because they have a lot of voice.
[1094.82 → 1095.22] Yeah.
[1095.64 → 1096.82] You don't want to mess with those people.
[1096.98 → 1101.10] Those people you want to treat well and not make the upgrade path painful.
[1101.54 → 1101.70] Yeah.
[1101.74 → 1102.54] The influencers.
[1102.78 → 1103.00] Right.
[1103.42 → 1105.36] But yeah, that was everyone that they pissed off.
[1105.60 → 1110.30] At the time also, WordPress had some better technology around.
[1110.44 → 1115.00] Well, when the PHP approach being fully dynamic, we were kind of betting on Moore's law.
[1115.00 → 1125.02] You know, that the sort of it would get faster and faster to serve dynamic pages and that those dynamic pages would be more compelling because you could customize them per user if you wanted.
[1125.02 → 1131.28] Then statically generate things, which of course is, you know, very, very cheap to serve.
[1131.28 → 1134.56] We had some pretty good anti-spam technology.
[1135.12 → 1136.62] And so that was a good differentiator.
[1136.62 → 1141.62] And then second or finally that, you know, we were actually open source.
[1142.04 → 1150.54] So rather than being open enough or OpenSSH, something like what they did where the license changed and the upgrade to the new version would cost a lot of money.
[1150.54 → 1154.48] Wouldn't happen with WordPress or any open source software.
[1154.90 → 1167.34] So they, a lot of people sort of, I think, you know, one of the challenges with open source is that where philosophically, you know, folks who get into it can understand it.
[1167.88 → 1170.94] Everyday consumers aren't affected by the issues very often.
[1170.94 → 1176.64] So they might not think about, you know, all that opens or all the freedoms that open source provides.
[1177.30 → 1185.68] But this was like a very real wake-up call for folks where it had sort of been good enough, and they had traded freedom for convenience.
[1186.12 → 1192.98] And then one day they woke up, and that freedom had been taken away, the bit of freedom they did have, which of course is the risk with proprietary software.
[1192.98 → 1199.58] And so there was a real sort of renaissance in the blogosphere of an appreciation for open source.
[1200.34 → 1202.26] And WordPress was just perfectly situated.
[1202.72 → 1203.92] You know, we had a great importer.
[1204.30 → 1205.50] People were starting to use it.
[1205.56 → 1214.30] We had some influencers switch already to really capture this tipping point of people looking for software that was both better and open.
[1215.40 → 1222.96] What do you think made people, I guess when I look at WordPress and I see it maybe from the same lens that Jared asked that question,
[1222.98 → 1227.26] from I think of it like the ability to extend it.
[1227.36 → 1236.24] And maybe it wasn't that way right from the get-go, but it was the plug-in system, the plug-in architecture that really let someone do more and more with it.
[1236.38 → 1239.72] And obviously with each version, that system got better and better and better.
[1240.40 → 1241.92] So, Jared, you mentioned Snowball.
[1242.00 → 1243.62] I kind of feel like that snowballed over time.
[1243.88 → 1251.88] How do you feel about the plug-in architecture and that system being something that was a catalyst for that traction that Jared asked about?
[1251.88 → 1258.30] If you can believe it, at the time, version 1.0 of WordPress had no plug-ins and no themes.
[1261.16 → 1263.84] So, lots of ways to improve still.
[1264.60 → 1264.86] Yeah.
[1265.38 → 1267.16] So, when did the plug-ins come into place?
[1268.28 → 1272.36] Plug-ins were in version 1.2 and then themes were in version 1.5.
[1272.90 → 1275.28] So, when did the traction actually begin then?
[1275.40 → 1276.92] Did it begin at 1.0 or 1.2?
[1277.16 → 1278.54] It really became at 1.0.
[1278.54 → 1278.98] Okay.
[1280.02 → 1286.82] Because that was the release that both was a pretty good release and around the time that movable type made their big misstep.
[1287.78 → 1294.14] So, what we had at the time was, you know, B2 had this brilliant system of filters.
[1294.52 → 1302.66] So, you could register a function that would take, you know, the output of something like the content of your post, run it through a function, and then return it.
[1302.66 → 1305.88] So, with WordPress, we had sent it out to add actions.
[1306.52 → 1313.34] So, you know, when you get to this point in the execution of the program, you know, run whatever is registered on this hook.
[1313.56 → 1315.34] So, that's filters and hooks that are on WordPress.
[1316.22 → 1318.60] That was either around 1.0 or 1.2.
[1318.60 → 1323.50] But at the time, we had, there were no plugins for any software, really.
[1323.94 → 1334.86] So, what you would do is for like PHP BB or B2 or anything else, the modifications people would publish like, open this file, go to line 33, paste in this code.
[1335.58 → 1339.18] Open this file, go to line 242, and paste in this code.
[1339.58 → 1342.40] And so, there'd be this sort of manual instructions for where to put in the code.
[1342.60 → 1343.94] And that's just what folks would do.
[1344.00 → 1344.80] They would hack the core.
[1344.80 → 1346.42] I can remember doing that.
[1346.60 → 1352.74] Actually, I can remember hacking the core, and that became, you know, non-existent because of other ways now.
[1353.30 → 1356.78] Well, it was very practical, though, because we'd released a new version.
[1357.12 → 1363.04] And I used to, for, this was kind of more post-moving to San Francisco, but I did it in Houston, too.
[1363.40 → 1367.54] So, when a new version of WordPress came out, I would just invite everyone over to my house to upgrade.
[1368.52 → 1370.36] Because it was kind of hard to upgrade.
[1370.62 → 1373.18] So, yeah, I just put out an open call, even on the blog.
[1373.18 → 1377.00] And I said, hey, if you want to upgrade, come on over, and I'll walk you through it.
[1377.10 → 1381.76] And so, because we'd have to bring over their hacks and their modifications to the core software.
[1382.96 → 1390.76] So, doing that, helping probably hundreds of people with that, it became obvious that we needed a way, something that could be persistent through versions.
[1390.76 → 1395.22] And that was a lot of the early inspiration behind the filters and hook system.
[1396.54 → 1396.72] Very cool.
[1396.78 → 1399.86] One thing you mentioned is, you know, kind of the timing was right there.
[1399.86 → 1401.66] And you had people mad at movable type.
[1402.14 → 1409.12] And you had WordPress, which was, both had some technology improvements and was open source and free as well.
[1409.12 → 1414.68] And that was a huge, you know, potential aspect of the traction that you got.
[1414.90 → 1419.84] I'm curious about your introduction to open source and kind of what got the hooks into you.
[1419.98 → 1422.26] Was it, you know, being able to fork B2?
[1422.46 → 1424.26] Was it WordPress or did it predate that?
[1426.26 → 1426.74] Hmm.
[1427.06 → 1428.52] It definitely predated that.
[1428.52 → 1433.90] So, probably my first exposure was to things that weren't open source, but were OpenSSH.
[1434.32 → 1438.08] So, like a bulletin or Envision BB.
[1438.42 → 1438.90] Yeah, results.
[1439.56 → 1439.64] Yeah.
[1440.80 → 1446.08] And they weren't open source, but you could see the code, you could modify it, that sort of thing.
[1447.96 → 1451.02] First open source, I also, at the time, I'd play with Linux.
[1451.20 → 1454.46] Like, I would go to the Houston Linux users group.
[1455.26 → 1456.28] My friend ran that.
[1456.28 → 1458.10] I ran the Houston Palm Pilots user group.
[1458.84 → 1463.42] I would go to the wireless user group because 802.11b was like a very new technology at the time.
[1463.68 → 1466.52] So, and you had to like, it wasn't built into anything.
[1466.62 → 1469.44] So, you'd have like cars and stuff you'd have to buy to plug it in.
[1470.44 → 1474.82] So, all of that, you know, there was just kind of, the community wasn't huge at the time in Houston.
[1475.04 → 1476.84] But I was kind of around all those folks.
[1477.88 → 1481.94] And because that was the people that were most passionate about technology.
[1482.54 → 1483.92] And we would all get together.
[1483.92 → 1487.80] There was a nonprofit that's now defunct, but it was called the Houston Area League of PC Users.
[1488.42 → 1490.64] And that's kind of where we would all meet up and get together.
[1491.38 → 1493.46] So, that was kind of early exposure.
[1493.82 → 1497.80] And, you know, I ran a little bit of Linux, a little bit of stuff at the time.
[1497.80 → 1501.38] And then for the web, it was really forum software.
[1502.22 → 1506.44] And maybe actually gallery was something I used a little bit before B2 even.
[1507.12 → 1509.32] It was just a PHP script called gallery.
[1510.60 → 1511.40] Good naming.
[1511.68 → 1512.54] It was very descriptive.
[1513.14 → 1514.04] But really awesome.
[1514.66 → 1516.84] And so, it allowed you to have photo galleries online.
[1516.84 → 1519.84] So, a lot of my early publishing was actually just photos.
[1520.88 → 1524.38] And I modified gallery extremely heavily.
[1524.56 → 1527.64] I hacked the core ton to make the outputs web standards compliant.
[1528.94 → 1533.24] And so, that was one of the first programs I got really, really into.
[1533.50 → 1535.42] The developer there actually worked for Google.
[1535.92 → 1537.34] And so, he was a great developer.
[1537.48 → 1540.32] So, it was perfect to read his code and learn from it.
[1540.32 → 1544.80] We have a ton of other questions to ask you later on in the show about open source.
[1545.14 → 1547.66] So, listening, it won't end there.
[1547.74 → 1549.16] We'll ask Matt more later on.
[1550.52 → 1555.56] We do want to dive, now that we've been through some of your history and also some of the WordPress history,
[1555.58 → 1559.44] we want to go further into the present because that's where we're kind of at now.
[1559.44 → 1561.18] But before we do that, let's take a break real quick.
[1561.26 → 1567.46] And when we come back, we're going to dive deep into Calypso, JavaScript, the future, or sorry, the present,
[1567.78 → 1569.22] and kind of take it from there.
[1569.32 → 1570.20] So, we'll be right back.
[1570.32 → 1575.76] DigitalOcean is simple cloud hosting built for developers.
[1576.38 → 1585.12] If you have not tried DigitalOcean yet, in 55 seconds, you can have a blazing fast SSD cloud server up and running
[1585.12 → 1592.34] with your choice of Linux distro, CPU, RAM, and even create new droplets based on backups or snapshots in time,
[1592.40 → 1593.32] which is a cool feature.
[1593.70 → 1599.94] For those that operate in Teams, you can invite multiple users to access and manage your account's infrastructure resources.
[1600.32 → 1603.52] While keeping all of your sensitive information totally private.
[1603.52 → 1610.34] Head to DigitalOcean.com and make sure you use our code CHANGELOG to get a $10 credit when you create a new account.
[1610.34 → 1615.06] All right, we're back from the break.
[1615.06 → 1627.22] And, you know, we've been talking to Matt about this history, this beautiful history of his step into programming and then open source and then WordPress and the history there, how it started at 1.0, like all software does.
[1627.22 → 1635.70] And now WordPress, I just looked in the WordPress admin for changelog.com, 442 is the current version.
[1635.82 → 1638.06] So, we're definitely come a very, very far away.
[1639.08 → 1647.64] WordPress now powers, at least based on the link you have on WordPress.com, at least 25% of the web, Matt.
[1647.64 → 1650.08] So, I mean, I don't know.
[1650.16 → 1657.12] Does this history, does this where you're at now, the present, does this astound you of like what's been accomplished by you and the team?
[1658.46 → 1672.86] I think if anything, it shows how much is left to do because there are still 75% of the web, but more importantly, billions of people who only have access to publish online through essentially proprietary networks.
[1672.86 → 1675.76] You know, be that Twitter or Facebook or something like that.
[1675.98 → 1677.82] And they deserve their own home on the web.
[1678.16 → 1685.28] You know, they deserve a little slice of it, which is just theirs, which isn't necessarily tracked or has advertising or anything that they don't want.
[1686.32 → 1687.24] Just like their home.
[1688.38 → 1693.72] Adam, I think that might actually lead into a question that I had stored for later, but I might just ask it now because it's on topic.
[1694.76 → 1699.32] You know, the web has changed quite a bit since 2003, 2004 when WordPress began.
[1699.80 → 1702.44] WordPress, as Adam stated, has changed quite a bit.
[1702.44 → 1707.58] You know, it was originally all about blogging, and it does quite a bit more than that nowadays.
[1707.86 → 1709.42] It can do some amazing things, really.
[1709.98 → 1710.90] But the web has changed.
[1711.00 → 1712.82] WordPress has changed alongside it.
[1713.54 → 1714.98] Blogging has changed as well.
[1715.46 → 1717.56] And you just mentioned, you know, proprietary systems.
[1718.64 → 1722.18] You know, blogging has gone in and out and sometimes back into style.
[1723.16 → 1726.00] You're a guy who still writes regularly on your own domain.
[1726.68 → 1731.82] Curious about your thoughts on blogging as a medium in today's and maybe tomorrow's web,
[1731.82 → 1736.90] especially with websites like Medium and other things where a lot of people are writing these days.
[1737.32 → 1737.40] Right.
[1738.00 → 1740.34] I think it's probably still one of the best.
[1740.34 → 1749.70] So for specialized media content, podcasting, you know, you have iTunes and other like Overcast and things like that.
[1749.94 → 1751.96] For photos, you know, Instagram, etc.
[1752.20 → 1760.30] So for specialized media content, there's specialized networks that are probably provided better features and distribution.
[1760.30 → 1765.32] But for a place to bring everything together and a place to write, nothing matches blogging still.
[1765.32 → 1770.68] Since Jared mentioned it, I guess we're veering slightly off the outline here.
[1770.78 → 1775.66] But since he mentioned Medium, obviously WordPress is still part of the game out there now.
[1775.84 → 1781.78] Maybe we're a little different, but we have a weekly email called Change Law Weekly, which basically is an email filled with links.
[1781.78 → 1786.42] Everything from new projects, reposts could be project homepages.
[1786.62 → 1798.34] And then also deep articles that talk about the experience of being a software developer, whether it's how to do something, a tutorial or, you know, talking about their best practices or whatever.
[1799.30 → 1807.46] More and more often, I would say that we're linking to Medium rather than not so much a WordPress site or somebody like you had mentioned, their private site.
[1807.46 → 1815.86] How do you feel about something like not so much Medium specifically, but like Medium-like things where they're hosted rather than self-hosted?
[1815.96 → 1818.02] I guess it's probably the argument rather than just saying Medium.
[1818.40 → 1821.42] How do you feel about that chasm of hosted versus self-hosted?
[1822.40 → 1824.70] Yeah, I've been through this cycle a few times now.
[1825.08 → 1834.82] And every once in a while, you know, a network of some sort comes along that either promises or actually provides, you know, some sort of utility.
[1834.98 → 1837.00] With Medium, they have a fantastic editor.
[1837.00 → 1838.96] And they have a promise of distribution.
[1839.96 → 1844.22] Now, that said, I think there's a lot of tradeoffs people make to be on Medium.
[1844.68 → 1848.56] So, for example, you're sort of trapped in their design of how things are.
[1849.84 → 1851.64] You know, you're on their domain.
[1852.36 → 1857.82] And the branding of it is very much you're like a guest in Medium's house.
[1858.54 → 1861.68] So if people are fine with that tradeoff, they should totally make it.
[1861.92 → 1864.18] All in all, I'm happy that people are publishing.
[1864.18 → 1882.30] But what I imagine is that especially at the point when Medium is forced to become a business, which probably is going to mean advertising, people might regret having invested so much of their writing and personality and online presence into something that's ultimately out of their control.
[1882.30 → 1887.86] Although, you know, EV is a really cool guy, obviously a billionaire from Twitter.
[1888.82 → 1892.54] Medium has investors and employees and at some point needs to become sustainable.
[1893.04 → 1896.10] And we haven't yet seen what that model is going to be.
[1896.10 → 1902.78] And a business before their business model exists is a very shaky foundation, which to build anything on.
[1903.62 → 1907.84] I guess while we're on the topic of business models, this also wasn't in the outline either.
[1908.36 → 1910.18] We're kind of veering way off-topic here.
[1910.26 → 1919.94] But since we're pulling from the end here, just for the listener's sake, since obviously we're going to talk about sustainability to a degree during this call, that wasn't mostly part of the plan.
[1919.94 → 1929.20] But since you mentioned sustaining oneself, you know, growing up to become a business or being a business, not a deep version of it, just a quick version of it.
[1929.24 → 1932.16] What's the business model of automatic, and what's the business model of WordPress?
[1933.16 → 1936.32] The beautiful thing about WordPress is it doesn't need a business model.
[1936.64 → 1939.44] It's an open source project staffed with volunteers.
[1939.74 → 1941.52] Some people who volunteer on their own time.
[1941.60 → 1946.54] Some people who are sponsored by media companies or automatic or development firms, whatever.
[1946.54 → 1953.00] WordPress doesn't really have any costs, so it doesn't really need any revenue, which is really nice.
[1954.00 → 1957.30] Automatic is a different can of beans, I guess.
[1957.52 → 1965.52] It's a for-profit company with investors, over 430 employees all over the world in 46 countries, I think.
[1965.52 → 1977.34] And so what we tried to figure out there was a model where is making money and doing well would benefit the community and vice versa.
[1978.40 → 1984.10] So a big initial decision from that, since you all like going in the historical stuff, was not forking the software.
[1984.10 → 1993.90] So what runs WordPress.com is the same code that you download from WordPress.org, the website, the same code that you run on your site.
[1994.48 → 2003.24] Basically, we're able to figure out a way, both improving the core software, which I think benefits lots of folks, and in creating a number of plugins and infrastructure around it,
[2003.64 → 2012.46] that we can run WordPress the same that anyone can download at truly web scale, serving billions and billions and billions of pages every single month.
[2012.46 → 2013.96] So that's pretty cool.
[2014.12 → 2017.48] So that means when we improve WordPress.com, it improves WordPress and vice versa.
[2018.16 → 2026.86] With the business model, what we've tried to stay away from is monetizing things that should be free.
[2026.98 → 2028.26] That's probably a good way to put it.
[2028.64 → 2035.66] So what we try to do is create services around hosting or things that are hard to do and charge a subscription for that.
[2035.66 → 2046.10] So whether you run Jetpack or whether you host your site on WordPress.com, there's a subscription that's somewhere around $100 or $300 per year that gets you lots of extra goodies.
[2046.96 → 2056.18] And our hope is whether it's for people who just want to support us or whether they find a lot of utility from what we're selling, they do that upgrade.
[2056.18 → 2062.38] And of course, a small percentage of people do, far, far less than 5%.
[2062.38 → 2068.04] But the folks who do allow us to invest and support everyone who's free.
[2068.48 → 2077.46] So even though 99% of people never pay us a dollar, the 1% that do support the business and support the whole thing.
[2077.78 → 2079.62] So it allows us to invest.
[2080.40 → 2084.72] We've invested at this point probably $150, $200 million into WordPress.
[2084.72 → 2087.98] And so the community gets the benefit of all that investment.
[2089.08 → 2091.40] I guess that's a good thing to mention.
[2091.48 → 2102.70] The reason why I think that's important to mention before Jared takes us into some of the tech pieces here is that, you know, just the mention of when I asked you about the hosted versus, you know, self-hosted versus a hosted model.
[2102.76 → 2104.90] And you mentioned Medium and growing up into a real business.
[2105.26 → 2108.20] Just to put more trust and faith back into this conversation.
[2108.20 → 2118.02] Obviously, you have it on your own, but just to make it clear to the listening audience, like what your business motives are from a revenue perspective and how that plays back into the greater WordPress community.
[2118.96 → 2122.32] And I think a key there is also the trust we built up over the past decade.
[2122.32 → 2129.86] And two, WordPress.com is unique among, you know, all real business services I can think of in the top 100.
[2130.32 → 2136.30] And that's not only can you get your data out, which is actually surprisingly still not that common.
[2136.66 → 2138.26] But of course, you can get all of your data out.
[2138.72 → 2141.96] But you can take the data and run the same software someplace else.
[2143.20 → 2143.60] That's a good point.
[2144.02 → 2147.54] There's not really very, you can't, you can download a file from Facebook.
[2147.54 → 2149.22] But what do you do with it?
[2149.84 → 2161.84] You know, and so by giving you both the data and the software to run it, I think that we provide a degree of freedom for our users that is, you know, a strong foundation of trust.
[2162.14 → 2162.20] Yeah.
[2162.44 → 2162.58] Yeah.
[2163.08 → 2171.18] Do you think the WordPress.org and the WordPress.com model that is working so well for the community and for Automatic as a company,
[2171.58 → 2177.40] is this a unique perspective or a unique position that WordPress is in to be successful in this way?
[2177.54 → 2187.26] Or do you think this is a model that people can, can clone or can follow in order to also have success as a business supporting an open source project?
[2188.20 → 2188.62] I totally.
[2188.80 → 2194.02] And in fact, you know, part of the idea with Automatic was to provide a template for other people to follow,
[2194.12 → 2198.02] to provide something where I want more businesses to be built in this way.
[2198.02 → 2211.02] Because I think businesses only for the enrichment of their shareholders are fine, but it's not where I personally want to spend my time or my energy.
[2211.68 → 2217.28] And I think more and more people young and old are wanting to have not just a profit, but an impact.
[2217.28 → 2224.24] And so if you can align sort of a community and a nonprofit with a for-profit in this way, they're very, very complimentary.
[2224.78 → 2227.22] I believe they can accomplish things that neither could on its own.
[2227.94 → 2231.88] So, you know, especially in the WordPress world, if you look at the bigger businesses around it,
[2232.42 → 2238.22] a lot of them look a lot like Automatic down to being distributed and using P2 to communicate with each other and things like that.
[2238.22 → 2240.94] So that's always making me very, very happy.
[2241.76 → 2248.16] And, you know, if folks are interested in this, there's a fellow who actually wrote a book about Automatic called A Year Without Pants.
[2249.06 → 2254.64] And it provides a lot of insight because he worked at the company for kind of about a year, year and a half,
[2254.84 → 2256.44] and just wrote about his experience.
[2256.76 → 2261.24] And I've started to see more and more entrepreneurs who've read that book, and then they model their business after it.
[2261.26 → 2262.22] And that makes me super happy.
[2262.96 → 2264.06] A year without pants, huh?
[2264.14 → 2265.88] Did he not wear pants?
[2265.88 → 2270.24] Well, the joke is that when you work from home, you don't need to.
[2271.86 → 2272.90] I didn't even get that.
[2273.30 → 2276.20] I can't say that I am wearing pants right now, and I do actually every day.
[2276.94 → 2278.28] Yeah, I'm wearing pants right now.
[2278.46 → 2279.46] Well, shorts, but.
[2279.66 → 2281.46] I just checked, and yes, I am wearing pants as well.
[2281.74 → 2282.72] I love the cover, Scott.
[2282.96 → 2285.08] I'm sure the listeners are very excited to know this.
[2286.16 → 2287.62] We are all wearing pants.
[2287.88 → 2288.50] The big topics.
[2288.88 → 2290.56] Scott Bur khan, yeah, I haven't read this guy.
[2290.56 → 2295.14] He was, it's so funny how you see names on the web.
[2295.88 → 2302.76] Maybe you never meet him, or you don't really cross paths quite so deeply as maybe Jared and I have with this podcast and open source and stuff.
[2302.86 → 2303.38] But I remember him.
[2303.44 → 2310.76] He was huge into speaking at O'Reilly's Ignite, and he did really well with blogs and a bunch of other stuff.
[2310.84 → 2314.54] But I remember him doing like this really, the most notable that I can think of.
[2314.62 → 2317.34] I think it was actually a how to do an Ignite talk.
[2317.34 → 2319.02] And Matt, you may be familiar with that.
[2319.90 → 2320.58] Yeah, he did.
[2320.90 → 2325.56] Actually, one of the books he's written, I knew him as an author before he joined, and that's why I wanted him to join.
[2325.84 → 2328.70] Because he had written a great book on product management that I really loved.
[2329.20 → 2332.34] And I think at that point, he had also done Confessions of a Public Speaker.
[2332.56 → 2332.90] Yes.
[2333.02 → 2334.26] Which is a book on public speaking.
[2334.26 → 2342.04] And so, yeah, my pitch to him was basically, you know, you've written a ton about your experience at Microsoft.
[2342.64 → 2347.58] And he was at Microsoft when Microsoft was probably the most interesting software company in the world.
[2347.80 → 2349.74] Not the most moral, but the most interesting.
[2351.10 → 2352.82] I was like, you know, that's the past of work.
[2352.92 → 2354.46] Come see what the future of work is like.
[2355.06 → 2356.54] And, you know, do it for a couple of years.
[2356.64 → 2357.16] Help us out.
[2357.16 → 2360.58] And worst case, you'll have something, a good story to write about.
[2361.70 → 2364.00] Since we're off-topic, we might as well stay off-topic.
[2364.16 → 2366.58] And then we'll get really on topic after the break.
[2366.68 → 2367.36] I promise.
[2367.56 → 2370.82] We're going to talk all about Calypso and what that means for the future of WordPress.
[2371.52 → 2381.72] But while we're here and off-topic, I want to ask you about open source kind of writ large in the sense of a project that's run for all these years, all these contributors.
[2381.72 → 2388.64] Has a company kind of behind it in certain ways, has a community behind it, has a cottage industry around it.
[2388.86 → 2390.72] And yet here it is, open source project.
[2390.84 → 2396.42] Can you tell us what it's like to manage something of this size and influence in terms of open source?
[2397.42 → 2397.96] Oh, wow.
[2398.76 → 2410.04] It was actually, you know, managing the volunteer side of both WordPress, but also things like the Houston Palm Pilot Users Group and other places that volunteer.
[2410.04 → 2413.68] It was fantastic practice, actually, for running a company.
[2414.26 → 2417.24] And I think when they go well, they actually look very, very similar.
[2419.06 → 2424.08] You know, when you're managing volunteers, people are working on things because they want to, not because they have to.
[2424.50 → 2426.18] You don't really have a carrot or a stick.
[2427.60 → 2430.84] So you think a lot about the environment and the motivations and recognition.
[2430.84 → 2440.50] And the truth is, in modern day business, especially a technology business like automatics, people are there because they want to be there.
[2441.28 → 2444.42] You know, every company in the world is hiring every engineer they can find.
[2445.80 → 2447.58] No one is forced to work at automatic.
[2447.86 → 2448.96] They're there because they want to be there.
[2448.96 → 2455.92] So I think a lot about motivation and work environment and recognition and all the same sort of things and vice versa.
[2456.24 → 2463.96] Like over time, learning how better to, for example, delegate more responsibility, be better about accountability, how to run a meeting.
[2464.22 → 2467.14] All of that, that I sort of learned through the automatic experience.
[2467.32 → 2471.70] We've tried to apply to the WordPress open source project to great success.
[2471.70 → 2473.80] I don't really think about that.
[2473.90 → 2482.96] What you said with the running a user group or a WordPress or not a WordPress project, but an open source project, how that's good training for running a business.
[2483.20 → 2487.24] I mean, that's, that's really insightful, but I never really thought of it like that.
[2487.72 → 2489.14] Like I said, it works both ways.
[2489.50 → 2496.20] You know, early days of WordPress, we were very bad about communicating releases and those releases being on time.
[2496.20 → 2504.18] And of course, in the business, when you're working with partners and all sorts of things, accountability becomes so, so important, probably the most important thing in a business.
[2504.92 → 2510.76] So we began to think a lot about, well, what does it mean to be accountable on the open source side of things?
[2511.14 → 2514.90] Well, first is if we say we're going to release on this date, let's release on that date.
[2515.28 → 2523.78] And then you start to realize, well, it's not perfect enough to pick a date because that's like a depending on which time zone you're in, it could be like a 24-hour window.
[2523.78 → 2524.22] Right.
[2525.30 → 2532.14] And, you know, we had it before where, you know, it's kind of like, well, I guess it's still, it's still Tuesday in Hawaii.
[2532.44 → 2535.78] So let's stay up to six in the morning and do this release.
[2536.00 → 2536.28] That's true.
[2536.72 → 2537.96] Yeah, that's, that's funny.
[2538.14 → 2542.24] And so even things just like saying, Hey, let's pick a date and let's pick a time.
[2542.38 → 2547.24] It's going to be 10 a.m. Eastern on, you know, December 6th.
[2547.24 → 2548.56] And we're going to do the release then.
[2549.44 → 2552.98] And then starting to look at what needs to happen to make that happen.
[2553.78 → 2556.52] Uh, when the release date can slip, it's not a big deal.
[2556.52 → 2560.12] Like if, or lots of small things can build up.
[2560.20 → 2566.06] So it was like the day before the release scene, you realize, oh, we haven't made the about page yet, or we haven't written the blog post, or we don't have a video.
[2566.24 → 2568.92] So let's just wait an extra day, and then we'll do a video and that'll be better.
[2568.92 → 2576.08] But when your, your date is firm, and you have an actual deadline, you start to back up and say, okay, that's four weeks away.
[2576.20 → 2580.54] What needs to happen in week one, week two, week three, and week four to hit that date?
[2581.42 → 2586.88] And, um, release leads, you know, we, nowadays, um, the release lead.
[2586.88 → 2592.14] So the person who is sort of the grand poo bah in charge of a release for WordPress rotates for every release.
[2592.62 → 2597.24] So the person who led 4.3 is different from 4.4 and who will lead 4.5, 4.6.
[2597.78 → 2604.28] So that gives a lot of different people experience on sort of managing deadlines and managing people and things like that.
[2604.28 → 2617.04] And I think once you've done that, you also become a better contributor, but I've been very, very impressed at the past, past couple of years, actually, we have gotten infinitely better at hitting our deadlines and doing the work ahead of time to do it.
[2617.38 → 2620.46] If you know two months out that you're going to be a week late, that's not bad, right?
[2620.88 → 2621.58] You can change it.
[2622.12 → 2626.36] If you know a week before that you're going to be a week late, that's really, really, terrible.
[2626.46 → 2631.90] It means that you really screwed something up probably a month or two ago that you should have accounted for.
[2631.90 → 2651.40] I think that's fascinating how you're, if it's not your decision to do so, but whomever's decision to rotate people out, because I've been in product development, not only as a software person, like either as a designer or actually building something, but also as from a PM standpoint for a nonprofit.
[2651.96 → 2653.80] And I never really thought about it.
[2653.80 → 2660.86] It would have been a lot better if you were actually rotating people out because that position can be very stressful and fatiguing.
[2660.86 → 2666.56] And it's also good cross-training to let other people do the role too, because, or just lead, you know, in general.
[2666.68 → 2669.58] And I think it's kind of interesting to rotate that role around.
[2670.00 → 2680.80] And that way it's also not, you know, someone's never the boss or the bully or the, you know, it just seems like more of a communal shared role.
[2681.10 → 2682.34] And I like that idea a lot.
[2683.54 → 2683.98] You nailed it.
[2684.00 → 2685.88] And you should put what you just said in the podcast.
[2686.56 → 2687.10] All right.
[2687.48 → 2688.40] We'll find a way.
[2688.54 → 2689.18] We'll find a way.
[2689.18 → 2691.12] I think that's a natural stopping point.
[2691.26 → 2692.68] So we'll take our next break.
[2692.98 → 2696.06] And as promised on the other side of the break, we will talk about Calypso.
[2696.32 → 2699.50] So stay tuned, and we'll talk about Calypso after this break.
[2702.82 → 2705.24] There's a saying I once heard, you may have heard it too.
[2705.50 → 2707.36] It's all bugs have software.
[2707.88 → 2709.76] I don't know where I heard it, but it just stuck with me.
[2710.30 → 2715.16] And one of the most frustrating things about being a software developer is dealing with errors, dealing with bugs.
[2715.16 → 2718.60] They happen and relying on your users to report your errors sucks.
[2719.04 → 2723.00] Digging through log files, trying to debug issues is not cool.
[2723.34 → 2726.82] Or having a million alerts flood your inbox every single day.
[2727.26 → 2728.74] It's the worst.
[2728.74 → 2738.44] With Rollbar's full stack error monitoring, you get the context, the insights, and the control you need to find and fix bugs faster with a lot less noise.
[2739.02 → 2740.32] It's easy to install.
[2740.44 → 2743.92] You start tracking production errors and deployments in eight minutes or less.
[2744.46 → 2754.06] Rollbar works with all major languages and frameworks, including Ruby, Python, JavaScript, PHP, Node.js, iOS, Android, and more.
[2754.06 → 2764.66] You can integrate Rollbar into your existing workflow, send error alerts to Slack or Hip Chat, or automatically create new issues in GitHub, Jira, Asana, Pivotal Tracker.
[2765.12 → 2767.38] And we have a special offer for changelog listeners.
[2767.94 → 2770.34] Go to rollbar.com slash changelog.
[2770.56 → 2771.16] Sign up.
[2771.24 → 2773.58] Get the bootstrap plan for free for 90 days.
[2773.86 → 2776.98] That's basically 300,000 errors tracked totally free.
[2777.32 → 2778.66] Give Rollbar a try today.
[2778.78 → 2781.50] Head over to rollbar.com slash changelog.
[2784.06 → 2788.70] All right, we are back talking with Matt Mullenweg about all things open source.
[2789.08 → 2794.44] Specifically, Matt, now we want to talk about Calypso, which you mentioned at the top of the show.
[2795.72 → 2800.84] But for the listeners, could you reiterate what's been going on with Calypso?
[2800.84 → 2804.78] You mentioned you launched it, or you announced it November 23rd of 2015.
[2805.54 → 2807.02] The 1.0 is out there.
[2807.10 → 2808.54] It's part of WordPress.com.
[2808.54 → 2814.00] But take us back to what it is and then how long you've been working on it and that kind of stuff.
[2815.06 → 2822.02] Calypso is basically the base of which I expect us to build the next decade of WordPress interfaces on.
[2822.44 → 2823.70] It's 100% JavaScript.
[2824.18 → 2825.48] It uses React.
[2825.66 → 2830.44] And we're starting to integrate a lot of Redux for hackers who are familiar with that sort of stuff.
[2830.44 → 2837.44] Talks purely over APIs and starting to incorporate.
[2837.64 → 2839.20] It's a very, very cool code base.
[2839.44 → 2841.42] It's totally – oh, I should also say it's totally open source.
[2841.86 → 2844.60] So it's both what runs WordPress.com.
[2845.02 → 2846.90] When you visit WordPress.com, it's the interface.
[2847.30 → 2848.04] It's the signup.
[2848.12 → 2848.80] It's the store.
[2849.36 → 2852.08] Any A-B test we run are all open sourcing in there.
[2852.08 → 2855.44] So what you see on WordPress.com is actually just what's in our GitHub.
[2856.50 → 2861.26] And so it's a degree of radical transparency as well that was a little uncomfortable for people at first.
[2861.34 → 2863.18] But we're starting to get into it.
[2863.90 → 2864.56] Cool code base.
[2864.72 → 2870.24] Like everything, every bit of code has usually been peer-reviewed by a few folks.
[2871.08 → 2879.62] The way we approach React components, you know, even if you aren't going to use WordPress at all, check out the component library because there are lots of components there that people could reuse for other projects.
[2879.62 → 2884.30] And it's really transformed how fast we're able to move and iterate.
[2884.64 → 2887.98] Oh, and the most important thing I suppose I should say is the user experience.
[2888.52 → 2895.58] It is so much faster than the sort of like PHP generating an HTML page and delivering it to you.
[2897.32 → 2898.62] And there's more coming.
[2898.90 → 2900.58] So you can look at the code base.
[2900.94 → 2903.42] We're not announcing yet, but obviously you all can read the code.
[2904.60 → 2906.86] You can see that we're starting to add offline support.
[2906.86 → 2917.58] So by moving the data store to Redux and doing some pretty cool stuff around caching and even things whereas you move your mouse towards a button, we'll start to preload what's behind that button.
[2918.78 → 2921.70] We can just make the user experience basically instantaneous.
[2923.00 → 2927.06] One of the things you said on your announcement post, which is on Matt's blog.
[2927.06 → 2931.80] In case you don't know, it's ma.TT, which is one of the best domain hacks probably of all time.
[2932.44 → 2939.72] We'll link this up is the announcement post that he posted on his own site is how this was a huge risk, this move.
[2940.08 → 2946.74] And you said that most open source projects will fade away rather than make evolutionary jumps.
[2946.74 → 2952.64] But to a large degree, you're kind of eating your own lunch, or I don't know what the term is.
[2952.90 → 2957.86] But this was a risky move saying, you know what, WP admin, it served us well.
[2958.34 → 2963.28] You know, many people would just keep on keeping on and keep slowly improving WP admin.
[2963.64 → 2968.10] But you guys decided to start fresh and make a big risk.
[2968.24 → 2970.60] Can you speak to that decision-making process?
[2970.60 → 2980.60] We always, you know, at the same time that we've been obsessed with backwards compatibility, and I think that served WordPress very well.
[2983.38 → 2990.36] We think a ton about the future because I have always treated WordPress and my work at Automatic as a multi-decade endeavour.
[2990.36 → 3008.24] And so when I think about the year 2025, you know, the technology stack that we needed to really create an experience that competes with not just Medium, but also with Facebook and mobile apps and everything was radically different.
[3008.98 → 3019.68] And things like offline support, which are, you know, going to be just a few months after we launched Calypso, are almost inconceivable to do in the old model of how WP admin and WordPress is written.
[3019.68 → 3025.10] So it was very much just a shared decision.
[3025.42 → 3027.20] And it's definitely uncomfortable, definitely.
[3027.44 → 3037.30] Like at the time when we started Calypso, there were probably just two JavaScript developers in the company out of more than 100 that were like gurus of JavaScript.
[3037.72 → 3042.96] And so there was a learning curve for the entire company to basically learn a new language.
[3043.86 → 3045.32] And that sucks in the beginning.
[3045.32 → 3047.08] Like once you do it, it's fine.
[3047.16 → 3050.14] But like while you're in it, like, man, why is it so frustrating?
[3050.28 → 3051.50] Why do variables work this way?
[3051.58 → 3052.82] Why does inheritance like whatever?
[3053.46 → 3054.54] You're just grumpy, right?
[3054.72 → 3057.70] Because you're going through that sort of learning curve.
[3057.90 → 3062.62] But once we went through it, the other side was definitely worth it.
[3062.62 → 3069.56] You mentioned the I guess, the PHP stack, if I'm trying to play back your words in my brain.
[3069.56 → 3082.78] But since we're talking about the present and the future kind of in this in the same vein here, while we're on the subject of stack and thinking about 2025, right now the stack is a lamp stack.
[3082.78 → 3085.18] You know, it's what everybody knows WordPress as.
[3085.30 → 3087.78] And now with Calypso, it's obviously shaking things up a bit.
[3087.90 → 3090.50] And it's, you know, JavaScript front heavy, API driven.
[3091.38 → 3093.84] What's the role of PHP in the future of WordPress?
[3093.98 → 3095.14] What's the future stack?
[3095.18 → 3098.64] As you think of 2025, obviously you probably can't get that far ahead.
[3098.72 → 3102.66] But if you were that far ahead, and you were looking back, what would you be talking about?
[3103.78 → 3105.44] You know, PHP is kind of cooler than ever.
[3105.44 → 3116.38] With both PHP 7 and the hip hop virtual machine, HHVM from Facebook, the performance gains that PHP getting are really exciting.
[3118.82 → 3124.72] So how I think of the stack in 2025, you know, I'm not going to, I wouldn't bet a million dollars on this.
[3124.72 → 3134.44] But if I had a guest today, I would say that the interface, so what users use every day for WordPress is 100% JavaScript.
[3134.44 → 3138.68] And it talks over HTTP to a PHP backend.
[3139.10 → 3143.82] So kind of the WordPress core or kernel or server side is PHP powered.
[3145.56 → 3149.96] And still speaking to a MySQL database, has that been changed at all?
[3150.02 → 3153.08] Are you still bullish on MySQL as a backend?
[3153.66 → 3155.00] MySQL is something compatible.
[3155.20 → 3155.82] Maybe it's Maria.
[3156.22 → 3158.72] Maybe it's, you know, the Persona fork or something like that.
[3158.72 → 3165.66] MySQL has definitely, I think, had a crisis of leadership since it's been under Oracle's wing.
[3166.04 → 3168.58] But something MySQL like, I think definitely.
[3169.24 → 3170.94] What about the server part of it?
[3171.54 → 3172.60] Oh, like the web server?
[3173.06 → 3173.22] Right.
[3173.36 → 3177.70] Well, if it's going to be, you know, if it's a LAMP stack, is it going to be Apache?
[3177.88 → 3179.24] Is it going to be Nginx?
[3179.24 → 3186.42] I know there's, like, for example, Changelog runs on Apache, even though Jared's part of the team, and he'd rather be Nginx.
[3186.52 → 3187.22] It's not Nginx.
[3187.48 → 3187.92] It's...
[3187.92 → 3190.86] If I had to pick one, I'd bet on Nginx.
[3191.26 → 3194.56] And we do, Nginx runs everything we do.
[3194.76 → 3197.64] And we also support its development a lot.
[3197.64 → 3199.22] So that would be the one I would pick.
[3199.98 → 3202.04] So 2025, Nginx is still a thing.
[3204.32 → 3207.16] It's silly to try to project 10 years in the future.
[3207.70 → 3212.52] But if I had to pick one, if you were like, Matt, you have to pick something today that you have to use for the next 10 years?
[3212.66 → 3213.46] Yeah, that's what I would use.
[3213.86 → 3213.98] Yeah.
[3214.06 → 3217.54] The reality, though, is that you should constantly be evaluating new things.
[3218.20 → 3218.38] Right.
[3218.38 → 3224.64] And that's part of, I think, really what you have to do in technology is disrupt yourself.
[3224.98 → 3231.52] You have to look at all your assumptions and say, does the reason I chose this back then, do those reasons still apply?
[3232.44 → 3237.18] And if not, if starting from first principles, if I were starting from scratch today, what would I do?
[3237.86 → 3241.94] So I guess since that's the question, then, why JavaScript?
[3243.08 → 3243.96] Why now?
[3244.24 → 3246.34] Why React?
[3246.52 → 3247.32] Why Redux?
[3247.32 → 3249.72] And why 100% JavaScript now?
[3250.00 → 3251.70] Like, what changed your mind?
[3251.78 → 3255.44] What's been happening over the past couple of years that's gotten you and the rest of the team to this point?
[3256.38 → 3257.20] Two things.
[3257.58 → 3262.84] I think that, you know, the browser war is reigniting with Chrome, WebKit, etc.
[3263.80 → 3276.38] Basically, executing JavaScript as a VM has had more development into it than probably any other language, probably more than Java now, but any other language other than Java in the history.
[3276.38 → 3280.02] So JavaScript just has some of the best VMs in the world, you know?
[3280.02 → 3285.12] And that's a testament to the amazing engineering talent, especially Google that's kind of into it.
[3285.82 → 3288.28] Things like Node made it accessible on the server side.
[3289.02 → 3292.10] And, you know, Facebook's investment and innovation around React.
[3292.10 → 3295.26] Now, is React what we're using a few years from now?
[3295.44 → 3295.90] Who knows?
[3296.36 → 3298.90] Why we use React is because it's so minimalist.
[3299.16 → 3307.02] It allows us to take our own approach and isn't too opinionated about forcing us to do things very firmly in one way or another.
[3307.02 → 3310.18] So it allows us to create our own framework in a lot of ways.
[3311.16 → 3314.72] But JavaScript, yeah, I'm happily betting on that.
[3314.88 → 3321.18] It's hard to imagine a world because browsers evolved to be from about documents to be about applications.
[3321.92 → 3324.96] And JavaScript is the lingua franca of those applications.
[3324.96 → 3329.30] It's an interesting, I mean, I agree with you.
[3329.38 → 3340.08] It's interesting that a product like WordPress, which is about, you know, publishing content online, which is very much documents based, right?
[3340.12 → 3340.70] And it's core.
[3340.70 → 3340.74] It's core.
[3341.84 → 3348.40] Still fits into the application mould that more and more websites are built around.
[3350.02 → 3351.92] As you say right now, it's the admin, right?
[3351.96 → 3355.14] It's everything that you do interacting and managing that content.
[3356.42 → 3363.92] But did you say, did I hear you say earlier that down the road, even the front end publishing, right?
[3363.96 → 3367.26] The rendering of all your content will also be JavaScript driven?
[3367.26 → 3370.80] Now, that I'm not 100% sure on.
[3372.18 → 3376.54] I think that'll actually become, WordPress will become more agnostic that way.
[3376.70 → 3387.06] Because as we start to have better APIs, some people will write a Ruby front end or a Go front end or a JavaScript front end talking to the PHP powered WordPress.
[3387.70 → 3390.56] But I think that PHP is also fantastic for that.
[3390.56 → 3398.12] And there's not as much need for the theming side of things to make it that much different right now.
[3398.52 → 3399.92] Because PHP is a emulating language.
[3400.08 → 3401.12] And that's what WordPress themes are.
[3401.18 → 3402.78] They're essentially fancy templates.
[3403.40 → 3403.42] Yeah.
[3404.24 → 3404.50] Right.
[3404.94 → 3408.98] Going back to another thing you said about the incredible risk.
[3409.04 → 3410.12] I'm going to quote it back to you.
[3410.20 → 3413.94] You wrote that this was a huge bet, incredibly risky and difficult to execute.
[3413.94 → 3416.14] But it paid off like any disruption.
[3416.30 → 3417.02] It is uncomfortable.
[3417.72 → 3420.46] And I'm sure it will be controversial in some circles.
[3421.36 → 3422.30] So this was in November.
[3422.30 → 3423.96] We're a few months past that now.
[3424.64 → 3427.30] We know that this announcement did make a big splash.
[3427.30 → 3429.20] And people were wondering, what's the future of WordPress?
[3429.40 → 3430.12] What does this mean?
[3431.08 → 3436.90] What controversies have arisen since you published that in light of the announcement and the launch of Calypso?
[3436.90 → 3440.78] And then how would you like to address any of them, if you would?
[3442.26 → 3445.50] You know, it's actually been a bit less controversial than I thought.
[3445.86 → 3446.06] Really?
[3446.80 → 3453.88] I think that it's still going to be difficult for a Calypso approach development for WordPress to be adopted.
[3453.88 → 3466.14] It'll take a few years because it's a big learning curve for people, developers like myself a year or two ago that have really only done PHP, HTML, etc. type development.
[3466.90 → 3471.16] But the benefits on the other side are just totally worth it.
[3471.88 → 3479.08] The controversy, I mean, some of it, it was a private project inside Automatic.
[3479.78 → 3482.16] So that was secret, you know, for a long time.
[3482.28 → 3484.30] So maybe a little bit of pushback around there.
[3484.62 → 3485.90] But now it's all out in the open.
[3487.00 → 3489.64] It's all, you know, people are starting to adopt it and fork it.
[3489.82 → 3495.52] We're getting contributions to the repository from people who don't work for Automatic, which is kind of interesting.
[3495.52 → 3500.80] And it's brought in an entirely new class of developer that maybe never would have considered WordPress before.
[3501.58 → 3511.44] Because, you know, although I'm very pragmatic around technology, a lot of folks, you know, think like JavaScript is cool and PHP is not cool.
[3511.58 → 3514.16] Or, you know, there's sort of a fashion element to it as well.
[3514.16 → 3525.06] So a lot of folks who may have thought of WordPress as being an older technology have given it a second look and, you know, dived into the code at Calypso and found it to be really cutting edge and modern.
[3525.06 → 3535.60] Do you have any fears that, so while you may be bullish on it, and I don't doubt that what you see is the truth.
[3537.08 → 3540.02] I guess when I look at WordPress, I see several types of users.
[3540.02 → 3543.96] You have some that are developers that are building on it to enrich the ecosystem.
[3543.96 → 3551.46] Some that are building on it because they have had to learn enough to run their own website.
[3551.74 → 3556.88] And so they've been willing to go down that road and actually become a geek, so to speak, or a nerd.
[3558.14 → 3560.16] Or even a hacker if they go that far.
[3560.56 → 3562.88] And you have some people who simply just want to publish.
[3562.88 → 3575.28] And correct me if I'm wrong, but I'm hearing what I think seemed like a simpler WordPress before to a more complex WordPress in the future.
[3575.40 → 3581.32] Albeit for those who are into tech and into software development, they see a brighter future for it.
[3581.72 → 3583.78] But maybe not everyone shares that same dream.
[3583.78 → 3591.24] Do you think that's going to fracture or concern your 25% number any bit because the road is harder to go down?
[3591.24 → 3591.64] Hmm.
[3593.40 → 3599.02] So of those three groups you talked about, for users, it's kind of a no-brainer because the user experience is so much better.
[3600.60 → 3608.76] For people developing sites, there also shouldn't be a huge, huge change because, again, WP admin is still there.
[3609.30 → 3612.00] So if they want to use that old way of doing things, it's still there.
[3614.24 → 3619.06] But for people who want to be on the bleeding edge of development, there's a lot to learn.
[3619.06 → 3620.80] And that is kind of scary.
[3621.04 → 3622.24] Change is always scary, right?
[3623.06 → 3625.54] But I wouldn't say it's necessarily more complex.
[3625.78 → 3627.56] It actually allows us to simplify a ton.
[3628.04 → 3633.32] By having a really robust API and everything go through that API, API-driven development essentially,
[3633.86 → 3642.04] it makes it way easier to integrate with other systems, to maintain backwards compatibility, to change interfaces, to customize things.
[3642.04 → 3647.58] And if you look at what WP admin is, it already has a ton of JavaScript.
[3648.92 → 3650.40] It's just mixed with PHP.
[3650.40 → 3660.98] So by making it pure JavaScript, it sounds more complicated, but in practice, it feels much simpler.
[3661.70 → 3670.88] And that's why people are able to do things faster in this new environment than we were able to when trying to hack together, clutch together,
[3671.06 → 3677.18] like AJAX requests with PHP-generated things and HTML on the page and all that.
[3677.18 → 3680.64] But you have to jump through a lot of hoops to do very simple stuff.
[3680.80 → 3689.80] Like, for example, in Calypso, if I'm looking at the comments and you from across the world moderate one of the comments to approve it,
[3690.10 → 3692.46] that immediately shows up as approved on my screen too.
[3694.94 → 3696.94] And it's a data-driven model.
[3696.94 → 3700.52] So things can happen not just, you know, I talked about offline.
[3700.68 → 3701.76] Things can happen in real time.
[3703.24 → 3708.60] Writing the code to do that, I mean, we have kind of a version of that in WP admin, is such a hack.
[3710.14 → 3710.54] Yeah.
[3710.70 → 3714.34] Because you're not just dealing with the data and the interface isn't reacting to the data.
[3714.88 → 3719.40] You're trying to build out the HTML and update sort of arbitrary HTML.
[3719.60 → 3720.54] And it's very, very fragile.
[3720.54 → 3728.30] Yeah, that's probably one of my biggest gripes about the WP admin as it is now is how hard it's been to customize it.
[3729.24 → 3732.68] We even have some more in our notes, but I'm not sure if we will actually get to that particular topic,
[3732.80 → 3736.66] which is WordPress sort of started out as this, you know, obviously as a blog,
[3736.72 → 3740.32] and now it's kind of evolved into a, you know, roll your own CMS to a degree.
[3740.50 → 3745.26] It's, you know, this linear content flow that's just built around this engine, basically.
[3745.26 → 3749.68] And, yeah, it's kind of crazy how things have played out.
[3750.64 → 3757.72] Matt, you mentioned that WP admin still ships, you know, with WordPress, or it's still there, is what you said.
[3758.40 → 3760.40] What about Calypso and timing?
[3760.82 → 3766.22] It's live on WordPress.com, so it's obviously getting that stress testing that any, you know, production app gets,
[3766.36 → 3770.06] especially on a site that gives as much traffic as you guys get at WordPress.com.
[3770.06 → 3778.34] But when is it going to be like a de facto part of WordPress.org, like the open source projects release when you download that bundle?
[3778.96 → 3780.34] When's Calypso going to be a part of it?
[3781.04 → 3781.52] I don't know.
[3781.62 → 3782.68] That's really up to the community.
[3783.36 → 3789.06] So I think right now it's nice to have it separate because it's very experimental, very, very experimental.
[3789.06 → 3799.18] And so it can kind of fail, or it can succeed or fail on its own.
[3799.82 → 3802.92] And we can be, we can try crazy stuff with it.
[3804.66 → 3812.92] At the point when it comes into the WordPress core, that's when we have to really think about, we have to change the way that it's developed a little bit.
[3812.92 → 3818.30] So I think that for now we should take advantage of it being a separate thing and try to iterate as quickly as possible.
[3818.56 → 3826.06] And it gets to something that is measurably so much better than WP admin, that we can want to user test against one, user test against the other and say,
[3826.56 → 3832.66] okay, only 50% of people can figure out this thing and 90% of people figure out this other thing.
[3833.28 → 3838.66] So I would say that if and when it comes in, it'll be community driven.
[3838.90 → 3840.34] And I also want it to be data driven.
[3840.34 → 3849.62] You know, it's something that is often too rare in open source projects because it's difficult or impossible to collect the type of data that can drive decisions.
[3850.02 → 3861.10] But you would never run a business or web service without having very, very, very detailed cohort analysis and feedback and A-B test, multivariant test and everything.
[3861.10 → 3870.66] So whatever we can do to figure out and improve the project when we have this kind of perfect data, we can apply.
[3871.66 → 3874.26] So what about WP admin in the meantime?
[3874.68 → 3886.94] Is it in bug fix mode, security patch mode, or is it still actively being worked on in conjunction in case Calypso doesn't get the adoption or the data doesn't tell you what everybody's hoping that it will tell you?
[3886.94 → 3889.42] It is actively being worked on.
[3889.64 → 3895.02] So that's what's kind of nice is at Automatic, we've been focused really 100% on Calypso.
[3895.02 → 3900.64] But the core open source community, you know, the last release had 150, 160 contributors.
[3901.48 → 3902.76] Everything happens in WP admin.
[3903.10 → 3905.18] So they've been developing in parallel.
[3905.74 → 3915.48] And I think we'll continue to, which is pretty exciting because not only are we able to really, you know, get over our skis and like do something really wild and experimental,
[3915.48 → 3920.84] but we have the safety nets of the existing thing that's still actively being developed.
[3921.28 → 3929.10] So there's no, we haven't had to trade off the traditional tradeoffs that a business might make to do something like this.
[3929.30 → 3935.04] And that's really a good example of the open source and the nonprofit and the for-profit working in concert.
[3935.04 → 3944.32] So we had a question here, whether people who were working on themes or things, I guess, that it would be WP admin focused, whether they're wasting their time.
[3944.32 → 3951.96] And I got to imagine there's people out there that either through Word Camp, any keynote you've given or any other podcast you've been on,
[3952.00 → 3960.54] have been waiting to hear whether, you know, their anxiety will be subsided by some sort of response that says they're not wasting their time.
[3960.54 → 3970.52] But, you know, in light of, I guess you kind of answered it to a degree, but in light of Calypso being sort of, it's still an experiment, and it's still not proven yet.
[3970.52 → 3981.60] And the fact that WP admin is still being worked on by the open source community, maybe subside any anxiety you think might be out there for those who are working on plugins, themes, what have you.
[3981.60 → 3990.86] Those developers who have like poured their lives, and you know them better than I do, Matt, poured their lives, their businesses, their extra time, their open source time into WordPress.
[3991.72 → 3995.58] You know, are they wasting their time or, you know, what's the future for those kinds of people?
[3997.00 → 4002.70] I try my best to lay out the future at the state of the word speech I gave in December at the Word Camp US.
[4002.70 → 4012.98] And so if you're building a plugin today, what I absolutely believe you should do is start to turn your interface into JavaScript, embedded in WP admin, right?
[4013.06 → 4017.14] So to a user, it might not change, but move it to be JavaScript and API driven.
[4017.86 → 4022.68] And the last release, version 4.4, we brought in a scaffolding for a REST API.
[4023.82 → 4029.18] It basically allows plugins to register endpoints on this really beautiful REST API.
[4029.18 → 4035.90] So what you can start to do is create endpoints for everything your plugin does and then have the interface interact with those endpoints.
[4036.32 → 4042.70] By the way, that also makes it easier for other apps, for mobile apps, for tons of things to integrate with your plugin as well.
[4043.20 → 4051.44] So if you can take that sort of API driven development, you can get a lot of the benefits of Calypso while still fully in WP admin.
[4052.36 → 4052.66] Well said.
[4052.66 → 4063.74] I know that was one of my anxieties for I guess the community was just thinking like, Geez, you know, with this experiment, is it going to like totally disrupt things or is there a path?
[4063.84 → 4065.04] And that makes a lot of sense.
[4066.70 → 4068.24] So we're going to take one more break.
[4068.28 → 4069.40] This is our final break for the show.
[4069.46 → 4074.36] When we come back, got a pretty interesting question for you, Matt.
[4074.40 → 4075.32] I hope you're ready for it.
[4075.44 → 4076.42] You'll like it, I promise.
[4076.58 → 4078.02] But it's going to be awesome.
[4078.14 → 4079.26] So we'll be right back.
[4079.26 → 4089.40] We're excited to be working with BMC to spread the word about Thrust Pulse, their infrastructure monitoring service with one second resolution.
[4089.86 → 4097.34] I talked to Mike Warren, the senior architect, about the importance of alarming, but more importantly, the importance of more accurate alarming.
[4097.34 → 4104.92] We also talked about integrations and how that plays into communicating internally across your teams as well as outside your organization.
[4105.24 → 4105.70] Take a listen.
[4105.70 → 4112.22] So alarming comes in really handy when you have one-second data because we actually collect at different resolutions.
[4112.64 → 4118.08] And we aggregate that data into one second, 15 seconds, 60 seconds, five minutes.
[4118.30 → 4124.08] And what that allows us to do is we can actually pull out some of the noise and give you more accurate alarms.
[4124.38 → 4126.58] Now the question is, what do you do for me?
[4126.72 → 4127.48] Email me?
[4127.62 → 4128.82] Well, that's not going to be very helpful.
[4128.82 → 4137.64] Really what I want is I want to find a way to push that towards my team so we're all knowing what's happening with the services, what's up, what's down, what's fixed, what's not.
[4137.90 → 4139.30] And that's where the integrations come in.
[4139.48 → 4142.06] So integrating in with things like your chat.
[4142.18 → 4146.20] How do I integrate into my other tools like PagerDuty or Opt genie?
[4146.52 → 4149.76] So how do I take advantage of hooking up who's on call and who's not?
[4149.76 → 4151.66] And then potentially how do I do automation?
[4151.98 → 4158.92] So fire off a web hook or potentially if you have another setup, you can set off an email and maybe that triggers something for you.
[4159.08 → 4163.70] But essentially you end up with that full round trip with everybody involved in that process.
[4163.90 → 4168.78] And that's your developers and your operations team because both of them have to be involved and know what's happening.
[4168.78 → 4173.14] So kind of with that end to end level, we can pull the different stats from everywhere.
[4173.64 → 4177.60] We can share those dashboards between anybody in your team at a certain point in time.
[4177.60 → 4183.40] And we can embed those dashboards into any of your existing dashboards or monitoring tools or things you may have.
[4183.56 → 4187.12] And that gives you the ability to share that information outside your organization.
[4187.12 → 4193.94] So that way you kind of have that one single piece that you can talk about, share about and see those metrics everywhere.
[4194.48 → 4197.82] I have the ability to have that communication with my team.
[4197.82 → 4203.72] And I, B, have the ability to have that same visualization across my team and external to our team.
[4204.26 → 4208.22] That was Mike Morin, the senior architect of BMC's True Sight Pulse.
[4208.42 → 4215.40] Head to bmc.com slash True Sight Pulse all in word to learn more and tell them Adam from the change log sent you.
[4218.98 → 4219.96] All right, we're back.
[4220.30 → 4223.68] And Matt, before the break, I teed up a question, which I did not ask.
[4223.68 → 4229.08] But I did go a little tiny crazy in the break there, which I, you know, fully admit.
[4229.46 → 4231.16] Nobody heard that, but I'm admitting it on the air.
[4232.06 → 4232.56] What's that?
[4232.98 → 4234.36] The breaks are the best part of this podcast.
[4234.80 → 4237.82] Yeah, I mean, nobody gets to hear the breaks, Matt.
[4237.86 → 4239.60] It's a shame because Jared and I say that all the time.
[4239.64 → 4242.40] We're like, man, I really wish we could air the breaks.
[4242.46 → 4243.78] And maybe we will do that sometime.
[4243.90 → 4245.84] But it's just the breaks are fun.
[4245.92 → 4246.68] We take breaks.
[4247.32 → 4248.36] We still have a chat.
[4248.36 → 4249.30] It just doesn't hit the air.
[4249.42 → 4250.24] And there you go.
[4250.24 → 4256.84] But the question I have for you is since you are a futurist, you think about the year 2025.
[4257.26 → 4258.76] You care deeply about this community.
[4259.48 → 4271.50] So you're obviously the kind of person that looks towards the future or has a list of dreams they hope to accomplish at some point in time, whether it's next year or 20 years from now.
[4272.10 → 4274.68] You know, I'm curious what stone is left unturned.
[4274.68 → 4283.10] What have you or Automatic or the community, whether it's you specifically driving that motion, what is left unturned?
[4283.18 → 4284.68] What accomplishment is left unturned?
[4285.56 → 4291.46] And what do you hope to accomplish with WordPress in the near future, whether it's 10, 20, 30 years, whatever?
[4294.68 → 4300.36] It's funny because even in our core mission, which is democratized publishing, we still have so far to go.
[4300.36 → 4305.26] I said it earlier, there's still 6.9 billion people who haven't used WordPress yet.
[4305.66 → 4308.24] And that number grows every day.
[4309.28 → 4310.62] Lots of people are being born.
[4311.18 → 4318.74] When I think of things that I would love to get to, it actually necessarily isn't something on WordPress, but the things related to WordPress.
[4318.74 → 4325.70] One of which we actually started to get into last year, which was, I've always thought that e-commerce was way too complicated.
[4326.44 → 4328.38] And I have friends who try to sell things online.
[4329.02 → 4329.80] It was such a pain.
[4330.84 → 4334.98] And last year, Automatic bought a plugin for WordPress actually called WooCommerce.
[4335.86 → 4339.38] W-O-O-Commerce, which makes it easy to sell things online.
[4339.94 → 4342.58] But it's kind of, it's early days.
[4343.02 → 4346.74] WooCommerce is kind of where WordPress was in like 2008, 2009.
[4346.74 → 4352.28] So there's so much growth and so much potential for it that it's been very exciting to work on.
[4352.60 → 4357.82] And I've also been learning a ton from the team just because they've lived and breathed e-commerce for so long.
[4358.56 → 4362.16] And it's not an area that I prior was an expert in.
[4362.62 → 4366.84] The other thing that I really love, and it's just kind of fun to hack on.
[4366.94 → 4367.22] I don't know.
[4367.32 → 4368.44] Have you always used Simple Notes?
[4369.64 → 4370.04] No.
[4370.44 → 4370.64] Yeah.
[4370.70 → 4372.38] So it's the S icon.
[4372.38 → 4372.86] Yeah.
[4373.76 → 4376.32] So we release it for desktop.
[4377.08 → 4378.00] There's a web version.
[4378.14 → 4379.88] There's mobile apps for Android and iOS.
[4380.92 → 4382.60] Simple Note is a Simple Notes app.
[4383.68 → 4385.68] And I'm a little bit obsessed with it.
[4385.72 → 4386.02] Okay.
[4386.56 → 4386.98] It's simple.
[4387.92 → 4388.36] Go ahead.
[4388.56 → 4389.12] It's simple.
[4390.30 → 4391.18] Don't make a joke.
[4391.40 → 4392.90] And the latency ruined it.
[4393.56 → 4394.70] My bad at you, latency.
[4394.70 → 4397.84] I think of it like a beautiful Zing garden.
[4398.36 → 4402.10] So where we can go and sort of rake the rocks on Simple Note.
[4402.86 → 4404.56] And it's incredibly powerful.
[4405.72 → 4412.80] You know, the simplest interface in the world, when you think about it, is also the one with the most complexity behind it, which is the Google search box.
[4412.80 → 4428.34] How many hundreds of thousands of servers and, you know, not even terabytes, but petabytes and petabytes of work have happened behind the scenes to serve you an answer to whatever you type into Google in, you know, 50 or 100 milliseconds.
[4428.68 → 4429.52] It is incredible.
[4429.82 → 4431.10] But it's behind the simplest interface.
[4431.86 → 4435.88] And that's, I think, part of what we can do with Simple Note is it has an incredibly simple interface.
[4436.14 → 4438.48] But behind the scenes, there's some really cool stuff going on.
[4438.48 → 4441.46] So, for example, it saves every version of every note.
[4441.72 → 4445.82] So you can rewind in history and see how a note has evolved over time.
[4446.00 → 4448.40] Or if you accidentally mess something up, like revert.
[4448.90 → 4451.12] So you think of it as having built-in version control.
[4451.76 → 4454.14] Now, that feature, a lot of people don't even know it's there.
[4454.38 → 4455.12] And that's kind of the beauty.
[4455.74 → 4457.74] So I love working on that.
[4458.02 → 4460.68] And it's not something that we're able to work as a priority.
[4460.92 → 4462.06] It doesn't make any money.
[4462.22 → 4463.26] It's a labour of love.
[4463.40 → 4464.56] But we really love it.
[4464.56 → 4468.70] And there will actually be some cool stuff for Simple Note coming out in the next month or two.
[4469.06 → 4471.20] So if you haven't tried it out yet, try it out.
[4472.02 → 4476.00] Is that part of, I guess, then your stones unturned?
[4476.94 → 4477.30] Yeah.
[4477.56 → 4478.64] How does that relate back to that?
[4479.06 → 4482.06] Man, I would love to work for like six months on just Simple Note.
[4483.24 → 4485.40] And hopefully we could still call it simple at the end.
[4486.44 → 4488.80] Have you always owned it then?
[4489.64 → 4491.26] No, it was actually an acquisition we did.
[4491.66 → 4493.46] I thought so because I used this a while ago.
[4493.46 → 4494.44] And I didn't know that.
[4494.52 → 4498.42] That's why when you started seeing it as yours, I was like, I didn't know that was Matt's thing.
[4499.44 → 4506.10] Well, we actually bought the company for, it wasn't Simple Note, but the synchronization technology behind it called Symposium,
[4506.58 → 4514.70] which is essentially, imagine it like a synchronized database, JSON sort of database that you can write to.
[4514.70 → 4519.46] And then opportunistically resolves that on the network.
[4520.28 → 4526.86] We use Symposium technology for things like notifications on WordPress.com and in the mobile ops.
[4527.30 → 4528.78] And it's pretty cool tech.
[4529.32 → 4531.08] I hope to open source that someday too.
[4531.08 → 4534.18] So a couple of related questions, Matt.
[4534.72 → 4537.98] How much software do you get to personally write nowadays?
[4538.64 → 4544.58] And then as a follow-up to that, what would it take to get you six months to just work on Simple Note yourself?
[4544.58 → 4550.98] Not very much, although I did have a couple of commits this year already.
[4551.60 → 4556.12] So I still maintain my sandbox and dev environment and everything.
[4557.28 → 4570.50] But I think that software is a craft, you know, and I'm continually impressed and humbled by the dedication and care and thought that the engineers at Automatic put into that craft.
[4570.50 → 4573.50] And I also have, you know, huge respect for it.
[4573.80 → 4580.18] So me just dropping in, yes, I can make a change to the homepage pretty easily if I wanted to.
[4580.26 → 4582.48] But then am I doing the proper test?
[4582.88 → 4585.48] Am I getting the PR, you know, the pull request reviewed?
[4585.70 → 4587.52] Am I, you know, localizing properly?
[4587.60 → 4592.18] Am I doing all the things that are the best practices that help us, what we produce be ultra-high quality?
[4592.78 → 4598.70] And that is more than just the time that I have available for my fun coding things.
[4598.70 → 4611.36] So when I code, it's typically for an internal system, like something in the only automation scene or for something kind of finance or HR related, where I'm one of the people who works in those areas who can code.
[4612.06 → 4615.96] And it has access to all the bank accounts and all the HR systems and all the.
[4616.28 → 4622.38] So it tends to be more in that scene, which is a little sad because I love getting feedback on my code.
[4622.46 → 4624.60] And a lot of this code no one in the world will ever see.
[4625.82 → 4626.08] Right.
[4626.86 → 4628.04] What about that second part?
[4628.04 → 4630.52] So you said you wanted to do six months on Simple Note.
[4630.76 → 4632.26] What would it take to get you there?
[4633.16 → 4634.44] Oh, six months on Simple Note.
[4635.34 → 4637.64] Well, that's a good question.
[4640.04 → 4642.64] I'd probably have to take a sabbatical or something.
[4642.64 → 4648.70] You know, the duties of CEO are very expansive and also very rewarding.
[4648.70 → 4658.52] You know, I, although I miss sort of the satisfaction of just like building something that you can see in touch with your hands, like of coding every day.
[4659.06 → 4665.82] Now I get to work with people who are brilliant engineers, brilliant designers, brilliant managers, brilliant leaders, brilliant business people.
[4665.82 → 4668.20] And the impact is so much larger.
[4668.20 → 4684.80] And so my product has moved from being something, you know, like WordPress to actually the entirety of the organization of automatic and how that runs and the culture and the funding and the business and every aspect of it is incredibly challenging and super rewarding.
[4684.80 → 4692.28] So, yeah, it's I don't know if I would choose to go back right now because there's just so much to do in the CEO role.
[4692.28 → 4694.66] So let's hop back to open source for a moment.
[4695.38 → 4700.28] As we've said, you've been pretty bullish on open source for a while now, long time.
[4700.64 → 4711.78] And since you've been in the open source game for so long, what are some of the biggest changes that you've seen over the last few years as open source has become more and more the de facto way of doing things?
[4711.78 → 4715.14] We see more big companies doing open source than we used to.
[4715.74 → 4721.38] And then as a follow-up to that, do you want to make any predictions on what's to come with the open source community?
[4723.18 → 4724.38] Those are both tough.
[4727.54 → 4728.62] Two big shifts.
[4729.18 → 4731.84] The first was the shift from web services.
[4732.38 → 4738.96] I mean, the GPL was written in the early 90s and anticipated a world more where software is downloaded and run on devices.
[4739.78 → 4745.84] And although we do open source and share all the code for WordPress.com, technically the GPL were not required to.
[4745.84 → 4757.20] And so the license didn't anticipate software delivery through a browser as being, you know, today the dominant method for which most people interact with software.
[4757.20 → 4765.88] The other thing that has super surprised me was the how close the mobile ecosystems are.
[4766.54 → 4772.40] You know, even originally things like the Apple app store for iOS not allowing open source.
[4772.40 → 4778.08] And we actually went out on a limb and open sourcing the WordPress app for iOS.
[4778.74 → 4782.48] And at the time it was expressly disallowed by the Apple terms of service.
[4783.16 → 4786.18] But we were like, well, we believe in this.
[4786.90 → 4791.66] We think, you know, there's at the time there was basically no open source apps for iOS.
[4791.66 → 4793.50] And we're like, well, this is bad for the community, right?
[4793.56 → 4798.66] Because people can't see Objective-C, full apps and code, anything beyond demo apps.
[4799.54 → 4802.62] And then finally I was like, well, worst case, Apple kicks us out.
[4803.04 → 4805.10] I would love to make a lot of noise about that.
[4806.74 → 4810.24] You know, because so much of Apple's success is built on open source.
[4810.36 → 4814.62] Really every technology company today, Facebook, Google, Twitter, Apple, et cetera.
[4814.92 → 4821.08] We're all built on, you know, not just hundreds, but sometimes thousands of open source projects.
[4822.52 → 4824.54] And so I think it would be very hypocritical.
[4824.78 → 4828.70] I also had some indications that some people inside of Apple disagreed with this stance.
[4829.08 → 4830.46] So we went ahead and did it.
[4831.02 → 4832.66] And first nothing happened.
[4833.08 → 4835.58] Then we got kind of a behind the scenes nod.
[4836.22 → 4842.26] So at the WWDC, the Apple Developers Conference, they actually used WordPress code in some of the presentations.
[4844.30 → 4847.44] Partially because there weren't any other apps that were open source that they could show.
[4848.10 → 4849.20] And so that was kind of a nod.
[4849.20 → 4854.90] And then later they updated the terms of service to sort of allow for what we do.
[4855.92 → 4858.64] But it's also a good example of where we try to be pragmatic.
[4859.56 → 4868.30] So if we were philosophically pure, I have a huge admiration for someone like a Richard Stallman, who literally won't use a cell phone because it doesn't have an open source BIOS.
[4868.30 → 4886.32] But where I try to orient my sort of balance between the moral aspects of open source, which I believe in hugely, more than anything else in my life actually, is with a pragmatism, which is trying to improve the world as much as possible for as many people as possible.
[4886.32 → 4894.34] And so sometimes that means making short-term trade-offs where you might not have a perfect stack that's 100% open source.
[4894.78 → 4897.72] Or you might trade some of that.
[4898.34 → 4902.06] But I'm okay doing that as long as it's going in the right direction.
[4903.02 → 4906.32] As long as either we can create...
[4906.32 → 4911.04] So for example, I think in the App Store, it's under some Apple license.
[4911.62 → 4915.34] But the exact same code is available under the GPL and publicly available.
[4915.76 → 4920.44] So technically, even using the Apple device, like you're not in a free software environment.
[4921.10 → 4923.44] But that means a lot of people can reach and use WordPress.
[4924.32 → 4929.88] And in practicality, it doesn't matter that in the App Store it's under this whatever they do.
[4929.88 → 4931.70] Because you can see the code.
[4931.82 → 4932.22] You can run it.
[4932.28 → 4932.94] You can modify it.
[4932.94 → 4933.68] You can build it yourself.
[4933.78 → 4934.48] You can run it yourself.
[4935.08 → 4936.50] So, I mean, that's...
[4936.50 → 4940.86] I think a lot about sort of the end user experience of what open source really enables.
[4941.14 → 4945.08] Than necessarily always being 100% pure in the stack.
[4946.42 → 4951.78] Well, since we've had a chance to go down memory lane, talk about the present, talk about the future,
[4951.78 → 4957.72] and hear your thoughts on open source as it's changed and also some predictions for the future of it.
[4957.72 → 4961.88] But let's turn that back on the WordPress community at large.
[4963.34 → 4968.08] Speak for automatic, speak for WordPress as best you can, which I'm sure you can do.
[4968.74 → 4975.88] But what are the needs to move the open source portion of, or just, I guess, WordPress in general forward?
[4976.40 → 4977.40] So we talked about Calypso.
[4977.48 → 4978.34] We talked about the future.
[4978.34 → 4983.86] We talked about 2025 and the stack that might or might not be a reality then.
[4983.86 → 4990.02] But what are the needs that are in place now that the listening audience can go and take action on?
[4990.12 → 4990.88] Is there issues?
[4991.10 → 4992.32] Is there a repo of places?
[4992.52 → 4996.24] Is there just ideas sitting out that people can go and build and start to dream about?
[4996.64 → 4998.02] How can people step in and help out?
[4998.64 → 5000.68] I'll try to address that on a few different levels.
[5001.50 → 5003.62] Also because I wear a lot of different hats, as you said.
[5003.76 → 5006.08] Like the CEO of Automatic, lead of WordPress, et cetera.
[5006.08 → 5013.26] If you're a developer for WordPress, and I said this on stage at Word Camp, learn JavaScript.
[5013.90 → 5015.02] Like really dive into it.
[5015.56 → 5016.86] I believe it is the future.
[5017.46 → 5022.56] It's already for the past four or five years been where all the interesting features and improvements to WordPress have come.
[5022.70 → 5024.18] They've been primarily JavaScript features.
[5025.14 → 5030.46] And so the writing is very much on the wall that that is the future, I think, not just of WordPress, but of web development.
[5030.46 → 5036.24] So if you don't know it, learn it sooner rather than later.
[5036.56 → 5038.52] You will thank me years from now.
[5039.46 → 5048.38] If you're a plugin developer, start to do what I did earlier, which is moved your plugin to be API-driven and using the framework and the scaffolding that we put in WordPress 4.4.
[5049.58 → 5051.04] You also kind of slipped in there.
[5051.16 → 5054.48] Like what is most important for WordPress to succeed in the future?
[5055.10 → 5056.58] And that's a bit more abstract.
[5056.58 → 5060.50] You know, I wish I could say, you know, read this book or learn this language and we'll be fine.
[5061.02 → 5066.66] But I think it has a lot more to do with the fuzzier side or the more people side of the community.
[5067.86 → 5074.96] One thing I'm incredibly proud of the WordPress community for, but we have so much more to do here, is it's a very friendly community.
[5076.74 → 5081.92] Whether that's me growing up in the South and learning Southern charms or politeness or etiquette or things like that.
[5081.92 → 5096.70] But I've always been proud that people, no matter what your background, male or female, what your primary language is, whether English is your first language or your fifth language or your zeroth language, you know, whatever it is.
[5097.22 → 5101.36] That in the WordPress community, we try to act with empathy.
[5101.52 → 5102.88] We try to be understanding.
[5103.36 → 5105.96] We shut down when people are jerks right away.
[5105.96 → 5109.64] If someone's making someone uncomfortable, we deal with it right away.
[5109.76 → 5112.70] Like we try to, you know, be a good host.
[5113.20 → 5119.10] Just like if someone was in your house at a dinner party and like yelling at a guest, you would say, hey, you know, like cool it.
[5119.32 → 5121.38] And if they kept doing it, you would ask them to leave your house.
[5122.06 → 5124.10] So we try to treat the project in that way.
[5124.22 → 5132.96] And I think that's really important because if you look at the numbers, software in general and open source in particular has a representation problem.
[5132.96 → 5136.64] You know, we're not representative of the people that are using it.
[5137.20 → 5139.20] Gender is the obvious one, right?
[5139.24 → 5142.12] Because in the world, we're about half men, half women.
[5142.74 → 5145.12] And open source projects are not that.
[5146.12 → 5151.30] But also language participation and, you know, racial backgrounds and things like that.
[5151.36 → 5153.44] We need to be better about this.
[5153.44 → 5168.36] And first and foremost, if there's one thing everyone can do with a project they're involved in, it's making sure that the tone and how you interact with folks, how people interact with each other is friendly and understanding.
[5169.04 → 5174.60] And this is, you know, there's so much in open source that a shorthand, which can be very off-putting.
[5174.60 → 5180.38] You know, the idea of a plus one or a minus one on a ticket or even the way we close tickets.
[5180.50 → 5182.30] And this is still a problem on the WordPress repository.
[5182.82 → 5184.48] WON'T FIX in all caps.
[5185.72 → 5186.94] Wow, that's kind of mean.
[5187.24 → 5187.60] Rude.
[5187.64 → 5188.68] I have this idea.
[5188.88 → 5190.00] Like I think I should WON'T FIX.
[5190.24 → 5198.08] You know, it's very – we don't think about it because once you understand the context of it, you know it's not a big deal.
[5198.08 → 5198.52] Yeah.
[5198.68 → 5207.52] That's maybe your first ticket that you contributed to a process, which you were already maybe a little nervous about, a little scared, and you put that out there and someone closes it as WON'T BE FIXED.
[5207.66 → 5209.98] Even the terminology in the frame of closing something.
[5210.96 → 5216.60] It's – we really need to question these assumptions of how we interact with each other, especially because it's online.
[5217.02 → 5220.78] Now, that said, I think that open source can lead the software world in this.
[5220.78 → 5233.24] Because I've seen, and I have experienced that, you know, open source is very much – people can look at the ideas without looking at the people.
[5234.04 → 5246.90] And it provides an abstraction of the being in person to allow folks from wherever they are on the world, you know, with internet connection and some basic tools to contribute and to learn and to read and to talk about things.
[5247.22 → 5249.14] So we need to think about that accessibility.
[5249.14 → 5257.96] So that's – I mean that was a little bit of a soapbox, but it's something that I think that – I think we do pretty well on WordPress.
[5258.28 → 5259.54] We can do much, much, much better.
[5260.10 → 5264.72] And in the open source world in generally, we need to really, really give some thought to it.
[5265.48 → 5271.06] And that goes into – you know, you can think of accessibility as a very universal term.
[5271.20 → 5271.96] And I think you should.
[5271.96 → 5279.46] It's not just – it is helping people who are maybe blind or hard of hearing or mobility or things like that.
[5279.78 → 5287.42] But it's also thinking about accessibility to the four or five billion people who will be coming online in the next few years.
[5287.60 → 5290.42] It's thinking about accessibility for what devices people actually use.
[5290.42 → 5296.18] It's great that your system runs on, like, the latest version of Node and Nginx and Linux.
[5296.36 → 5301.76] But, like, are you really reaching the most people that you could with that?
[5302.22 → 5304.78] And I believe that as developers, we have a moral imperative.
[5305.18 → 5309.22] Like, you know, if you're able to write code right now, you have an incredible gift.
[5309.22 → 5317.02] It's one, that you were – won the ovarian lottery, and you were able to have a life that led you to learn this thing, which wasn't basic survival.
[5317.14 → 5318.26] It goes so far beyond that.
[5318.58 → 5327.74] But two, that you have this skill, which now a single person can write things and affect things that touch hundreds of millions or billions of people.
[5328.44 → 5330.90] And so I think we all have limited time on this planet.
[5330.90 → 5342.10] And so we have a responsibility to try to use that skill, you know, whether you consider it God-given or fortune-given or whatever it is, for the good that will affect the most people.
[5343.64 → 5346.56] Well, Sam, I can definitely see that's from many different hats, too.
[5346.56 → 5358.68] So we certainly subscribe to the idea of obviously being loving, giving, you know, making things accessible, things like that.
[5358.68 → 5372.34] And just – I think just being a good citizen to those out there and not always being the won'tt-fix person, you know, being short, tactful, you know, Twitter-forced maybe expression like won'tt-fix.
[5372.42 → 5383.76] That's just kind of a, you know, a quick way to say something where you should take some time to actually explain yourself, especially if it's somebody new or newer that you're influencing still yet on the community, so to speak.
[5383.76 → 5393.72] Well, Matt, one question to close with, and we gave you these questions in email, so we gave you a few, but we're only going to ask you one today.
[5394.46 → 5404.00] And we're curious of your hero, someone, somebody that's influenced you, somebody that made Matt who he is today, leading what he does, doing what you do.
[5404.12 → 5407.68] Who's someone that's inspired you to do what you've done?
[5408.12 → 5408.70] Who's your hero?
[5408.70 → 5414.54] I really wanted to give you a single answer for this, but I couldn't narrow it down.
[5414.72 → 5417.96] It was actually worse that you asked me ahead of time because I gave it a lot of thought.
[5420.10 → 5421.68] I'll just try to list it quickly.
[5421.90 → 5422.02] Sure.
[5423.10 → 5424.36] And it'll be a lot of books.
[5424.54 → 5425.90] So there's a book, Beautiful Code.
[5426.08 → 5426.92] It's an O'Reilly book.
[5427.54 → 5432.24] It's, you know, great information from a number of – a collection of essays and things.
[5432.24 → 5436.06] The Pragmatic Programmer is, of course, a classic.
[5437.22 → 5442.46] Books like Don't Make Me Think by Steve Drug or The Design of Everyday Things, which I think is Don Norman.
[5443.26 → 5444.64] You know, I think it's important.
[5444.88 → 5448.92] A lot of innovation in the world comes from bridging disciplines.
[5449.64 → 5452.72] And so if you're a programmer, read books on design.
[5452.80 → 5454.34] If you're a designer, learn about programming.
[5454.34 → 5462.30] You know, try to look at the – because that intersection of fields is where you'll be able to create the most interesting work.
[5463.68 → 5465.76] And then, you know, a lot of it comes down to bloggers.
[5466.52 → 5470.26] You know, I thought a lot about Dave Weiner and his writing on software.
[5471.48 → 5475.58] Joel Sapolsky and his amazing essays on, like, rewriting things.
[5475.84 → 5477.18] Scott Bergen, who we talked about.
[5477.70 → 5480.86] There are great wikis, especially around agile stuff, like the C2 wiki.
[5480.86 → 5487.94] Yeah, and then the final thing I was thinking about was just, you know, programming is just a form of writing.
[5488.82 → 5492.48] And a lot of my inspiration comes from the great writers in history and reading about writing.
[5493.12 → 5501.02] And so if people listening to this were to read one thing, it would actually be an essay by Orson Welles called Politics and the English Language.
[5501.76 → 5503.18] It's written in, like, 1946.
[5503.94 → 5507.20] And it's a long read, but you can read it in, like, 15 or 20 minutes.
[5507.20 → 5513.38] And if you read only one thing, if you took only one thing from this entire podcast, I would say to check out that essay.
[5514.28 → 5518.28] And, you know, it talks about the English language, and it's written in the context of the 40s.
[5518.40 → 5524.12] But, you know, you can apply that to code and the elegance and the succinctness and the clarity.
[5525.58 → 5531.52] Works just as well for code as it does for design, as it does for speaking, as it does for writing.
[5531.52 → 5534.74] Well, we'll definitely take good notes on that.
[5534.84 → 5537.68] So for those that listen to the show, you know, we have show notes.
[5537.94 → 5539.58] This is episode 197.
[5540.06 → 5543.90] So if you're on the web or web browser, go to changelog.com slash 197.
[5544.18 → 5545.02] You'll find the notes there.
[5545.22 → 5554.68] All the books, people, and essays that Matt mentioned will be there waiting for you to go and devour them and enjoy them and take your time reading them.
[5555.06 → 5556.92] I'm sorry for causing you all so much work.
[5557.56 → 5559.94] You gave them some homework, that's for sure.
[5559.94 → 5566.42] We've got at least seven tabs open right there real quick to put in there in the notes.
[5566.64 → 5568.40] But we'll have them there for you no matter what.
[5568.46 → 5568.94] We'll get them there.
[5569.68 → 5571.82] Matt, it was such a pleasure to have you on the show.
[5572.10 → 5573.56] Honestly, I know we took a lot of your time off.
[5573.66 → 5576.20] We have been waiting years for you to get you on the show.
[5576.40 → 5580.22] So sorry for the timing, I guess, to get you an invitation on here.
[5580.30 → 5587.58] But also thanks to you for keep pushing forward and actually getting a chance to come on and agreeing and all that good stuff.
[5587.58 → 5591.38] But we do have some great shows in the schedule.
[5591.50 → 5595.06] Coming up soon, we have a different Matt's.
[5595.60 → 5599.68] It's Matt's himself joining us to discuss 20 years of Ruby.
[5599.68 → 5606.92] We're also planning a cool call with Sarah J. Chips and George Stocker to talk about the open source behind Jewel Bot.
[5607.02 → 5610.42] So if you've seen Jewel Bot out there, and you thought it was super awesome, guess what?
[5610.44 → 5615.38] It's powered by open source and some fascinating people who care about women and girls getting into programming.
[5615.60 → 5621.38] If you want to find out about the open source behind that and also what it means for getting more women and more girls into programming.
[5621.38 → 5629.00] And Matt, again, thank you so much for joining us today to come on and talk about WordPress and the history and your history and all that cool stuff.
[5629.10 → 5635.24] We couldn't have had this show without you because Jared and I were both influenced by WordPress.
[5635.56 → 5637.08] And that's obviously how we got here today.
[5637.16 → 5639.18] So it's sort of like a big old circle of life, my friend.
[5639.36 → 5642.12] So kind of interesting that it works out like that.
[5642.60 → 5645.02] Anything else you want to mention before we close out the show?
[5646.02 → 5646.70] No, sounds great.
[5646.78 → 5648.08] I really appreciate you guys chatting.
[5648.34 → 5648.70] Awesome.
[5648.70 → 5651.78] To the listeners out there, we thank you so much for listening.
[5652.12 → 5653.00] Couldn't do the show without you.
[5653.12 → 5665.50] And if you want to support what we're doing, and you want to get a backstage pass to everything we do, including our Slack room, as well as our special discounts we have from offers or from special discounts and offers from our partners.
[5665.82 → 5668.72] Join the community and become a member for 20 bucks a year.
[5669.16 → 5673.00] Head to changelog.com slash membership to learn more about that.
[5673.54 → 5675.08] That's it, fellas, for this week.
[5675.16 → 5676.02] So let's say goodbye.
[5676.70 → 5676.94] Goodbye.
[5677.12 → 5677.72] Thanks again, Matt.
[5677.72 → 5678.78] Bye-bye.
[5702.90 → 5703.26] Love it.
[5703.28 → 5704.74] Love it.
[5705.58 → 5705.88] Bye-bye.
[5706.10 → 5706.70] Bye-bye.
[5706.70 → 5736.68] We'll be right back.
