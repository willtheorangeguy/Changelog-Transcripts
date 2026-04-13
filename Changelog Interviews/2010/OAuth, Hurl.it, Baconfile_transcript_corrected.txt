[0.00 → 18.54] Welcome to The Change Log, episode 0.1.5.
[18.60 → 19.50] I'm Adam Stachowiak.
[19.84 → 20.64] And I am Wend Mechelen.
[21.14 → 23.56] We follow what's fresh and new in the world of open source.
[23.80 → 27.84] If you found us on iTunes, we're actually on their internet at thechangelog.com.
[27.84 → 31.88] Or for real-time view, check out tail.thechangelog.com.
[32.38 → 35.42] We're also on GitHub.com forward slash explore.
[35.58 → 41.16] We'll find some trending repos, some feature repos from our blog, and all the episodes of our podcast.
[41.34 → 41.76] So check it out.
[42.16 → 44.64] If you want to follow us on Twitter, you can do so as well.
[44.78 → 47.84] Follow changelog show, not the changelog, sorry.
[48.44 → 50.46] And if you want to follow me, I'm Adam, S-T-A-C.
[50.54 → 51.58] That's Adam Stack.
[52.10 → 54.90] And I'm Penguin, P-E-N-G-W-Y-N-N.
[55.50 → 56.66] Well, you're just back from FOA.
[57.84 → 58.86] Yeah, FOA, man.
[58.88 → 60.16] It was an awesome time in Miami.
[60.44 → 62.24] It's like not quite Vegas.
[62.62 → 64.44] It's not Sin City, but it's close enough.
[65.20 → 68.44] And a lot of fun there, a lot of good people at the conference.
[68.76 → 73.08] And Ryan always knows how to do a good job, and not just himself, but his team as well.
[73.12 → 76.86] He's got an awesome team he's built, and they definitely know how to do conferences as well.
[77.18 → 78.36] Ryan Carson you're talking about?
[78.58 → 79.66] Yeah, Ryan Carson, yeah.
[80.76 → 81.48] Personified, yeah.
[81.66 → 85.60] I'm excited about heading out to the Twitter conference, Chirp, in April.
[85.60 → 86.62] It's a Carson joint.
[86.62 → 89.76] That's just before Scoff, isn't it?
[90.40 → 92.14] Yeah, little birdie says we may be out there.
[92.26 → 92.94] Yeah, that's what I heard.
[93.14 → 93.58] We'll see.
[93.98 → 94.44] We'll see.
[94.90 → 101.54] But, yeah, one person we did catch up with, well, actually two people, one specifically from Facebook.
[101.78 → 103.30] We hope to catch up with David Recording.
[103.80 → 108.14] He had a few minutes of chat with Ryan on stage about what Facebook is doing at open source,
[108.22 → 109.96] and I think he's got a lot of cool stuff to talk about.
[109.96 → 115.10] So hopefully he makes some time to show his face or his voice on this ditty.
[115.60 → 116.44] I look forward to it.
[116.80 → 122.96] We've got a great interview this week with Leah Culver, recently of Six Apart, most recently of Plan cast.
[123.06 → 124.76] It's a development since we recorded the episode.
[124.76 → 124.84] What?
[125.84 → 128.62] It's kind of funny how she didn't tell us about that.
[128.68 → 130.10] It was the day after she announced it.
[130.72 → 132.14] Yeah, we could have scooped it.
[132.58 → 134.36] I feel like we've been wronged, Leah.
[135.42 → 135.98] Oh, well.
[136.48 → 137.84] It's a good interview, nonetheless.
[138.18 → 139.06] Yeah, no, she's awesome.
[139.06 → 145.46] I think what she's done with OAuth and especially what you guys were talking about with the whole API junkie stuff.
[145.54 → 146.28] Man, you guys are crazy.
[147.16 → 149.16] Yeah, I've got a sickness, and it's called APIs.
[150.04 → 152.78] So good stuff, good stuff.
[153.02 → 153.62] It's a great interview.
[153.70 → 154.22] You want to get to it?
[154.36 → 154.72] Yeah, sure.
[154.82 → 155.12] Let's go.
[160.18 → 167.32] All right, we're joined today by Leah Culver, and we're with Adam.
[167.32 → 173.16] I should mention that Adam's with us because he makes this strange appearance about 30 minutes into every episode.
[173.30 → 174.82] So Adam's here, wedding and earrings.
[175.36 → 177.46] And we're talking today with Leah Culver from Six Apart.
[177.66 → 183.72] Leah, why don't you introduce yourself to the audience, the guys that might not know you, and what you do at Six Apart.
[184.64 → 185.48] Hi, everyone.
[185.98 → 186.92] I'm Leah Culver.
[187.18 → 191.72] I work at Six Apart currently as a product manager but formerly as a software engineer.
[191.72 → 201.82] And prior to that, I had my own company, Pounds, where I was the primary engineer, and that was acquired by Six Apart sometime last December.
[202.50 → 207.98] So I do a lot of work with Django and a little bit with some other technologies.
[208.14 → 209.40] So I'm very excited to be on the show.
[209.54 → 210.04] Thanks, you guys.
[210.50 → 212.04] Yeah, thanks for joining us.
[212.04 → 218.36] So I have some curiosity to how you transitioned from having Pounds and then going into Six Apart.
[218.48 → 222.20] What was that like to be kind of approached by them and then get consumed by them?
[223.24 → 225.62] It's an interesting process for sure.
[225.98 → 230.04] I mean, I've always been a big fan of the company, Six Apart.
[230.76 → 232.46] I really like the products that they make.
[232.52 → 239.32] They've been very active in open source communities, and I feel like they sort of have similar values to myself.
[239.68 → 241.38] It's someplace I always wanted to work.
[241.38 → 242.66] So it was actually pretty easy.
[244.52 → 245.94] How did Pounds come about?
[246.58 → 253.80] Everybody that I talk to about Pounds compared it to Twitter, and I'm not sure if that comparison is 100% fair.
[253.92 → 258.56] But what's the background on how Pounds came about and what you guys were trying to do over there?
[260.00 → 267.64] Well, I wanted to do a social site, and I wanted it to do with messaging and sharing content online.
[267.64 → 275.64] We had a couple of specific use cases, specifically when you found something online that you thought was funny or clever.
[275.82 → 277.80] How would you share that with the people you knew?
[277.80 → 284.32] And I'd end up getting these IMs that were just links to stuff or links to funny videos.
[285.04 → 287.06] And we thought there could be a better way.
[287.06 → 296.62] And I met Kevin Rose, one of the co-founders, at an event in the fall of, I want to say 2006.
[296.62 → 303.38] And at the same time, I met Daniel Berea, the other Pounds co-founder.
[303.50 → 305.58] So there were three of us, three Pounds co-founders.
[306.06 → 311.20] And we all got along very well, and we really wanted to work on this idea.
[311.20 → 318.92] And Daniel's a designer, and Kevin's a business person and an entrepreneur, and I'm a developer.
[320.14 → 324.96] And so it all sort of worked out, and we had similar ideas and got together and just discussed them
[324.96 → 330.72] and came up with this thing that was inspired by a lot of different sites that were around at the time.
[330.78 → 335.60] Because this was kind of a very popular idea to make something that was like blogging,
[335.66 → 337.48] but more conversational and more social.
[337.48 → 341.66] So what's it like to work with Kevin and Daniel Berea, then?
[341.76 → 346.24] I guess Daniel was the co-founder that had the design skills, and you were the co-founder.
[346.24 → 349.78] Yeah, he's a super talented designer, so that was really nice.
[350.42 → 355.28] And Kevin's pretty business savvy and has really great connections, so that was nice.
[355.34 → 356.18] It was very convenient.
[357.08 → 360.86] Yeah, it's kind of rare that you get such a good team to come together in that way.
[361.14 → 363.46] So if you find it, hold on to it.
[363.82 → 364.38] Yeah, absolutely.
[364.38 → 370.40] So OAuth and Embed, you're the I guess, co-writer for both of those specs.
[370.52 → 371.84] Did those both come out of Pounce?
[373.04 → 374.52] Well, yes and no.
[374.72 → 376.48] So Embed more than OAuth.
[376.62 → 378.50] OAuth sort of came actually from Twitter.
[379.60 → 384.50] And Blaine Cook's desire to do, well, Twitter and Magnolia both,
[384.50 → 391.18] they had this issue where Magnolia allowed OpenID for login.
[392.08 → 398.36] And at the time, APIs were mostly HTTP basic auth, which depends on a username and password.
[398.48 → 403.42] And of course, when you have OpenID, you don't have a username and password for that particular site.
[403.42 → 413.62] So they were looking around at other solutions, and folks like Google and Yahoo and especially Flickr had done some token-based auth that was fascinating,
[413.80 → 414.64] but it was all different.
[415.22 → 417.36] And they wanted to make sort of a standard.
[417.86 → 423.44] And Pounce got on board later because I was interested in the work, and I thought it was a really great project.
[423.44 → 426.20] Talk about OAuth for a moment.
[426.42 → 430.98] I've done some OAuth development myself on the Twitter gem most recently.
[431.40 → 439.24] And I think the vibe is that it's well-suited for web applications and not so suited for desktop applications.
[439.36 → 440.20] Would you share that point of view?
[442.84 → 443.96] Yes and no.
[444.04 → 450.14] I've seen it done well on desktop and web applications, though it doesn't have quite the same benefit.
[450.14 → 456.12] But it's difficult to come up with a scheme that sort of works for all three.
[456.30 → 462.16] And every single case of logins, there's like – I mean, it's not even just like desktop and mobile.
[462.32 → 468.70] It's like a mobile app accessing a desktop app that accesses the original API and things like that.
[468.84 → 470.72] So it gets pretty complicated.
[472.12 → 475.42] It is a deceptively simple problem.
[475.42 → 481.82] I think at first glance you think that authentication is just something that isn't that difficult.
[482.02 → 485.26] But when you kind of peel the onion, it starts to stink after a while.
[486.28 → 486.72] Right.
[487.06 → 489.28] I mean, it's just – it's security issues.
[489.42 → 495.70] It's things that you never think about that, you know, someone trying to hack your site is always one step ahead thinking of these things.
[495.90 → 501.28] And it seems unnecessarily complex, but there really are reasons for all the decisions that were made.
[501.82 → 502.48] You know, that's right.
[502.48 → 504.72] As we speak, there's an issue on Twitter.
[504.84 → 505.80] I don't know if you've seen it today.
[506.08 → 514.40] The site Twitter grader evidently was hacked and sending out tweets on behalf of hundreds of – I guess tens of thousands of users.
[515.20 → 521.34] But the cool thing about OAuth, since they implemented OAuth, you can just go into your connections on Twitter and turn that off,
[521.38 → 523.70] which is something you can't do with basic authentication.
[523.90 → 526.28] I think that's the main selling point.
[526.28 → 530.22] A lot of developers push back at wanting to implement it, but it does have its perks.
[530.22 → 530.66] Right.
[531.24 → 532.82] And it's not like they've stolen your password.
[532.96 → 535.66] And a lot of people reuse passwords over and over.
[535.84 → 539.58] Like my Twitter password might be the same as my Flickr password per se.
[539.78 → 542.86] And if your passwords are stolen, people can hack all sorts of your sites, right?
[542.88 → 544.66] And you have to go in and change it in a bunch of places.
[545.20 → 549.42] It's pretty easy to actually revoke your OAuth token for a particular site.
[550.46 → 554.64] Actually, it's a little bit hard to find in your settings on Twitter, but you can do it.
[554.76 → 555.10] Sure.
[555.10 → 557.54] And it sort of just kills the problem right there.
[557.78 → 558.42] It's pretty nice.
[558.64 → 562.64] One of the questions that keeps popping back up on the Twitter list around OAuth is,
[563.34 → 572.68] for open source desktop applications instead of web applications, what should be the protocol, I guess, around generating those keys?
[573.68 → 574.98] The consumer keys?
[575.14 → 576.04] The consumer keys.
[576.38 → 584.04] So basically, I guess everybody that clones a desktop open source app really has to generate their own set of consumer keys, right?
[584.04 → 585.46] Right, right.
[585.54 → 596.46] And that's an issue for a lot of web applications, too, that are open source is they publish whatever their keys to different services may be.
[597.70 → 598.12] Yeah.
[598.36 → 603.72] I mean, I'm not sure that I'm the best person to know really great solutions for that.
[605.30 → 605.82] Yeah.
[605.90 → 606.86] It's always tricky.
[606.86 → 612.04] When I created the LinkedIn gem, when they released their API, they implemented OAuth.
[612.24 → 622.04] And I ended up checking in my keys into the gem source, I must admit, and had someone update my LinkedIn status from my own library.
[622.14 → 622.92] So it's kind of embarrassing.
[623.34 → 628.28] But you have to be careful with those because it's just like someone that has your username and password.
[628.54 → 629.22] It's pretty funny.
[629.22 → 638.14] I think I've made the mistake of publishing like my root password for a server one time in some of my code in like a fabric file or something.
[638.26 → 639.38] And I was just so embarrassed.
[639.88 → 641.02] I changed it, of course.
[641.14 → 643.94] But, you know, this sort of things live on in your commit history.
[646.16 → 648.68] Talk about Embed for a moment, if you would.
[648.78 → 651.40] How did that come about and what problem is it trying to solve?
[651.40 → 658.78] So Embed was – that was actually pretty much pounce-driven at first.
[659.42 → 669.06] We had this feature where you could enter a URL for a photo or a video, and we'd automatically sort of change that link into an embed of that actual photo or video.
[669.18 → 671.58] So you'd see like a photo appear instead of just a link.
[671.58 → 684.06] But one of the issues we had was that we had added like YouTube and Vimeo, but then we'd have smaller video sites or video sites that maybe, you know, we didn't know about come and ask us how do we get this feature.
[684.16 → 688.96] And so I was adding a bunch of JavaScript and specialized code for every single site.
[689.16 → 692.60] And I was like, okay, this is taking up too much time.
[693.12 → 699.30] We want to be nice to everyone, and we want everyone to be able to have their links appear as videos or photos.
[699.30 → 709.32] So why don't we sort of make a standard format that they can provide for us and an API that we can use to sort of treat all these embeds similarly?
[710.68 → 714.26] You know, one of the selling points for Embed is especially around video.
[714.62 → 717.16] How do you see HTML5 affecting that at all?
[718.06 → 719.58] You know, I'm not actually sure.
[719.70 → 722.06] I haven't been following the debate too closely.
[722.06 → 732.04] But it should, I mean, pretty much anything you include in Embed in between your tags can be any, it can actually be any HTML.
[732.38 → 738.20] So it doesn't really matter what type of video player it is, which I guess could be a benefit.
[738.38 → 743.46] There's actually a type for Embed called Rich where you can put in any HTML you like.
[743.46 → 755.48] And it's up to the consumers of Embed to verify, like, the security, or, like, to make sure that it's a trusted transaction and that you're getting sort of what you expect.
[755.68 → 766.76] So really, if you switched from a Flash video to the new HTML5 video format, as a consumer, you probably wouldn't even need to know that.
[766.76 → 771.68] The provider could change at will as long as they respected, like, the size constraints of the video.
[773.46 → 778.40] I'm curious about, not in a bad way, but why did you choose Python?
[778.52 → 779.98] Why did you choose to stay with Python?
[780.64 → 782.04] And kind of what got you into development?
[783.02 → 785.90] So I was actually a Java developer in school.
[786.18 → 786.50] No.
[787.58 → 789.00] That's what you do in school.
[789.26 → 789.54] Right.
[790.24 → 790.62] Right.
[790.76 → 794.64] And I had interned as a Java intern.
[795.16 → 797.44] And I got my first job out of school doing Java.
[797.58 → 798.70] My first two jobs, actually.
[799.88 → 802.10] So I've been a Java developer for a long time.
[802.10 → 806.28] And when it came to making Pounce and making my own site, I was like, no more Java.
[807.18 → 808.66] I want to see what else was out there.
[810.52 → 812.94] And I looked into a couple different things.
[813.16 → 822.96] I looked into Perl a little bit, PHP a little bit, but not very much because I really wanted to use web frameworks, which were kind of like the new hot things.
[822.96 → 824.70] So I took a look at Ruby on Rails.
[824.70 → 827.70] And I had just a horrible time installing everything.
[828.54 → 829.70] This was 2006.
[831.62 → 837.66] And one of my friends suggested taking a look at Django, which was like a totally new framework as well.
[837.66 → 839.88] And I tried it out.
[839.88 → 845.48] And I got everything installed a lot quicker, which is totally the wrong reason to choose a framework.
[846.02 → 848.88] But at the time, I just wanted something that would work.
[848.96 → 850.18] And I understood the documentation.
[850.94 → 852.66] And so that was really it.
[853.06 → 857.90] So that's why I've been doing Python for so long, is it was Django that got me into it.
[857.90 → 859.32] So serendipity then.
[859.52 → 860.34] It just clicked.
[861.34 → 861.60] Yeah.
[861.90 → 862.12] Yeah.
[862.18 → 868.40] I really felt like, I mean, I think people feel that different concepts in programming really vibe with them.
[868.46 → 871.30] And I felt like some of the stuff in Python really vibed with me.
[872.54 → 873.26] Very cool.
[873.78 → 874.56] What was your internship?
[874.76 → 876.88] Out on the West Coast or in Minnesota where you're from?
[876.90 → 877.54] Oh, in Minnesota.
[877.74 → 879.56] I interned at IBM in Minnesota.
[880.56 → 883.88] So talk a bit about geography for a second.
[883.88 → 887.58] So have opportunities opened up for you since moving out to the West Coast?
[888.62 → 889.80] It's definitely different.
[890.60 → 897.50] I think my feeling was when I lived in Minnesota that programming was a job, you know, very much like being a dentist or a doctor.
[897.68 → 900.54] You just you are a programmer, and you went to work at a big company.
[901.26 → 902.40] And that's what you did.
[902.48 → 904.20] And you work nine to five and that was it.
[904.26 → 910.22] And then moving out to the Bay Area, there's very different attitude in general.
[910.22 → 913.82] I mean, I've met people who do all sorts of crazy stuff all over the world.
[913.82 → 921.04] But in the Bay Area, there's definitely more of a culture for not working the nine to five.
[921.32 → 923.34] It's kind of like the 90210 story.
[923.46 → 926.98] You go from Minnesota to California and things open up.
[928.50 → 929.18] Oh, what was that?
[929.28 → 929.48] Sorry.
[929.88 → 931.18] Like 90210, right?
[931.28 → 931.66] 90210.
[931.84 → 933.52] Didn't they live in Minnesota or something like that?
[933.54 → 935.86] And they went from Minnesota to California.
[936.20 → 938.86] I think you think of like the Beverly Hillbillies or something.
[938.86 → 941.06] No, it wasn't.
[941.16 → 942.06] They were from Minnesota.
[942.44 → 943.12] Was it 90210?
[943.12 → 945.48] You know, I think that was before my time.
[946.40 → 946.68] How old are you?
[946.68 → 949.60] You're going to have to introduce our audience to 90210, buddy.
[950.00 → 950.48] Oh, boy.
[951.00 → 955.84] Well, I guess I was a fan when I was younger, but I was probably like 11.
[956.66 → 957.52] How old are you, by the way?
[957.64 → 958.18] Just curious.
[958.82 → 959.10] Me?
[959.26 → 959.66] 27.
[960.28 → 962.32] So you're not young.
[962.44 → 962.96] You're not old.
[964.00 → 964.28] No.
[964.60 → 967.30] When is just over 30, and I'm just 30?
[967.30 → 972.04] The TV reference is from the guy that doesn't watch or doesn't have network television.
[972.74 → 973.22] That's great.
[974.76 → 977.12] I don't watch too much TV either, sadly.
[977.60 → 979.82] Well, not on TV, TV.
[980.76 → 984.60] Well, speaking of open source and open source TV, do you use Boxer?
[984.60 → 988.22] You know, I hate to say this and admit this.
[988.30 → 1000.16] I've never used Boxer, but I've used – Chris just installed Plex on our Mac Mini, and I've
[1000.16 → 1003.44] been sort of having a little love-hate relationship with it.
[1003.44 → 1008.76] Well, that does open the door for our first question from our Twitter fan base.
[1009.50 → 1013.16] Jay Noisemaker wants to know what Chris Two-stroke is like in person.
[1015.96 → 1018.40] The same.
[1020.96 → 1023.46] He's very much the same online as in person.
[1025.32 → 1025.58] Yeah.
[1025.58 → 1028.92] So he only speaks 140 characters then?
[1031.88 → 1033.26] No, only on Gists.
[1034.14 → 1038.82] If you missed it, we had a great interview with Chris in episode 0.1.0, I believe.
[1039.04 → 1040.30] Yeah, it was our first point release.
[1041.22 → 1042.48] It's an excellent episode.
[1042.84 → 1043.72] About three weeks ago.
[1044.26 → 1046.20] Let's talk about some of the apps you've created.
[1046.68 → 1048.86] So Hurl It.
[1049.04 → 1053.72] I don't know that there's a day that goes by in the last couple of weeks that I haven't
[1053.72 → 1055.12] used this application.
[1055.12 → 1059.76] So how does a Python girl get mixed up in a Rails rumble?
[1061.04 → 1064.10] So Chris and I did Hurl It together.
[1064.26 → 1068.10] We also did the Django Dash together previously, a few months before.
[1069.42 → 1070.68] So it was kind of a deal.
[1070.86 → 1073.76] He did the Django Dash, and I did the Rails rumble.
[1074.32 → 1075.36] So it was fun.
[1075.52 → 1076.32] I really liked it.
[1076.36 → 1080.48] It was kind of crazy to say, you know, I didn't really know Ruby very much at all,
[1080.58 → 1081.70] and to jump in.
[1081.70 → 1087.20] And I actually did most – I mostly did design, so that was pretty fun.
[1087.20 → 1092.54] If you don't know, Hurl is – I guess Hurl It, Hurl IT, Hurl.IT.
[1093.04 → 1100.28] It's a great API harness to put in endpoints for APIs and test them and replay those requests
[1100.28 → 1100.78] and responses.
[1100.92 → 1104.20] I use it quite a lot because Adam knows that I have an addiction to writing wrappers for
[1104.20 → 1104.68] APIs.
[1105.06 → 1105.74] He does.
[1105.74 → 1106.22] Yeah, I do.
[1107.48 → 1113.08] Yeah, I'm kind of an API junkie myself in that I'm, like, obsessed with every sort of
[1113.08 → 1114.42] detail about APIs.
[1114.98 → 1121.30] And it's really like the programmer's design, the programmer's interface.
[1121.50 → 1122.04] It's very fun.
[1122.42 → 1124.38] Have you come across an app called Charles Proxy?
[1125.18 → 1126.88] Yes, I've used Charles before.
[1127.28 → 1129.82] In fact, I'd use it a lot before I used Hurl.
[1131.70 → 1133.08] It's actually really nice.
[1133.08 → 1134.04] Yeah, I love Charles.
[1134.28 → 1135.54] It's just – it's too cool.
[1135.66 → 1140.62] You know, last week, the Goal guys, we've been begging them for an API for weeks, and
[1140.62 → 1141.44] they finally released it.
[1141.52 → 1146.96] But I got tired of waiting, so I was able to hook up Charles and set it up as a proxy
[1146.96 → 1148.32] on my MacBook.
[1149.24 → 1155.90] And I used that proxy server connection on my iPhone and then used the iPhone native app
[1155.90 → 1159.86] to Goal and then sniff out their hidden API that their iPhone app uses.
[1159.98 → 1160.72] It's just too cool.
[1161.16 → 1161.84] Oh, wow.
[1161.94 → 1162.76] That's crazy.
[1162.76 → 1167.16] Yeah, it's – I mean, I love, like, getting views into sort of, you know, having, like,
[1167.18 → 1172.50] these nice graphical views into what's going on when you're making requests and getting
[1172.50 → 1172.96] responses.
[1173.08 → 1173.70] That's super cool.
[1174.34 → 1175.56] So that's funny.
[1176.14 → 1176.84] Wow, that's crazy.
[1176.92 → 1178.22] So now they have a public API.
[1178.64 → 1183.88] They do have a public API, although it's much slimmed down from what I was actually able
[1183.88 → 1184.78] to find underneath the hood.
[1184.88 → 1189.74] So on the public API, it's mostly read-only, but there are some methods there if you know
[1189.74 → 1193.02] where to look to actually create spots and things.
[1193.12 → 1195.20] But I think they're worried about people gaming the system.
[1195.32 → 1199.02] You know, the whole deal with Goal is you have to be where you say you're checking in,
[1199.20 → 1201.58] which if you have API access, you could be anywhere.
[1202.32 → 1202.94] You know, is it?
[1202.94 → 1208.06] I haven't used Goal that much, but I did look at their API browser, which people were
[1208.06 → 1209.20] saying looked a lot like Hurl.
[1209.34 → 1215.12] But Hurl was inspired by other API browsers, so it's not really a fair comparison.
[1215.76 → 1223.62] You know what I use Hurl for mostly is if I'm writing a wrapper to an API, I will use
[1223.62 → 1228.24] Hurl to test the API endpoint and then save the response as a fixture file.
[1228.24 → 1233.20] And then start writing tests that will parse that fixture file and then implement the code
[1233.20 → 1234.46] that makes the test pass.
[1234.50 → 1235.64] It's kind of the workflow that I have.
[1236.26 → 1236.68] Oh, that's great.
[1236.76 → 1244.06] Do you use, like, the little view where it renders it outside the actual, like, page UI?
[1244.36 → 1245.88] It'll just give you the plain text?
[1246.06 → 1246.48] Yeah, I do.
[1246.62 → 1250.24] I'll pop that open and then just copy that to the clipboard and then paste it in a new file.
[1250.24 → 1257.52] And I use TextMate as my editor, so a lot of times I'll use the format JavaScript function
[1257.52 → 1260.12] that's built in there to format nice and neat and tidy.
[1260.92 → 1263.26] Most recently, I used it for another product.
[1263.68 → 1266.48] I guess you and Chris also partner on Bacon File.
[1267.38 → 1267.68] Yeah.
[1268.02 → 1271.72] Well, actually, Bacon File I made long before I knew Chris.
[1272.40 → 1272.88] Okay.
[1272.88 → 1280.10] Yeah, but he wrote a desktop app for Bacon File where you could drag files.
[1280.60 → 1282.06] So tell the folks what Bacon File is.
[1283.30 → 1288.86] So Bacon File is sort of my inspiration for it was I have a friend who has, like,
[1289.04 → 1295.82] just like an Apache server that displays files, you know, like it just shows a directory of files.
[1295.94 → 1296.64] You can browse it.
[1296.68 → 1297.44] And I thought, that's great.
[1297.54 → 1298.12] I want that.
[1298.12 → 1302.40] I want a way that I can just, you know, put my files up online and just be like, here you go.
[1302.62 → 1306.12] Get this thing from here sort of feel.
[1306.32 → 1311.56] And I found that there's not really any sites that sort of just allow me to throw random files at them.
[1313.32 → 1319.90] So the original intent for Bacon File was to be for anybody to just be able to upload any file they want.
[1319.98 → 1322.68] It showed, like, a nice directory, and you could, like, browse the tree.
[1322.68 → 1330.02] But it ended up being, I had second thoughts because that sounded kind of costly, storing people's random files.
[1332.10 → 1341.86] So instead I used Amazon S3 and said if you have your own S3 account, which you pay for your own bandwidth and your own storage,
[1342.24 → 1345.48] then you can use this as a nice web interface to Amazon S3.
[1345.48 → 1347.64] It's really neat.
[1348.48 → 1351.94] Recently I wrote a wrapper for it, Chunky Bacon File.
[1352.50 → 1353.48] Oh, I saw that.
[1353.58 → 1354.18] That was great.
[1354.88 → 1359.82] Basically it's a tutorial for writing your first gem or API wrapper in Ruby,
[1359.96 → 1360.60] and I couldn't resist.
[1360.90 → 1367.38] I was looking for a test case when I came across Bacon File and why the lucky stiff is big in the Ruby community.
[1367.50 → 1369.44] I couldn't resist the name Chunky Bacon File.
[1370.02 → 1371.16] Oh, that's so cute.
[1371.16 → 1375.26] Yeah, you know, I don't know how useful the app is for a lot of people,
[1375.46 → 1380.34] but I worked really hard on the API, so it's very exciting to see people use it.
[1380.44 → 1380.80] Thanks.
[1381.20 → 1382.96] I really don't know if it's not more popular.
[1383.80 → 1388.26] It's incredibly useful to just be able to add a file and tweet it to somebody and say,
[1388.34 → 1388.90] here, grab this.
[1389.68 → 1392.66] I think it's mostly the Amazon S3 component of it.
[1392.98 → 1397.62] Like, I think in the original concept, you know, where you just can log in and upload as many files as you want,
[1397.66 → 1398.86] I think it would be a lot more popular.
[1398.86 → 1405.18] But the fact is you have to pay for your own files, and you have to sort of manage your S3 account, which is a pain.
[1405.90 → 1405.96] Right.
[1406.92 → 1410.16] Finding those credentials is difficult, even if you do have an S3 account,
[1410.22 → 1415.76] even to find those in the Amazon website of where my crews to even put in here.
[1416.22 → 1416.56] I know.
[1416.66 → 1418.98] I wrote up a whole, like, step-by-step thing for Bacon File.
[1419.10 → 1422.08] It's like, here's how you find your Amazon S3 credentials.
[1423.16 → 1425.00] You know, and so it's kind of a pain.
[1425.00 → 1430.18] But so one of the things I was thinking about doing this next year was open sourcing all of Bacon File,
[1430.32 → 1435.08] since it doesn't make me any money, and it doesn't cause anybody any harm.
[1435.32 → 1437.50] I thought it would be kind of fun to open that up.
[1437.96 → 1440.88] Well, you've already done that with Hurl It, right?
[1440.92 → 1443.46] Because I was surprised to actually see the source, and I don't know why it didn't dawn on me,
[1443.56 → 1446.64] being in the Rails Rumble, that it would be available out there.
[1446.72 → 1448.86] But that's already out there, right?
[1449.52 → 1449.80] Yep.
[1449.86 → 1450.10] Yep.
[1450.10 → 1450.74] Hurl's available.
[1450.86 → 1451.58] You can download it.
[1451.58 → 1455.18] What I was hoping to do with it, or I think what Chris and I were both hoping would happen,
[1455.32 → 1463.34] would be that people that had APIs would sort of adopt it for API browsing on their own site.
[1463.90 → 1467.60] But it's not really packaged very well for that, but I was hoping that maybe it could be.
[1467.60 → 1468.16] Oh, that's interesting.
[1468.42 → 1472.22] So to be able to run it, I guess, as a subcomponent of your API site,
[1472.30 → 1475.84] to say kind of like what Gala did with here's our methods,
[1475.84 → 1479.22] and here's how you can kind of test it out in your browser, right?
[1479.22 → 1480.66] Yeah, exactly.
[1480.96 → 1483.66] And the inspiration, I think maybe I mentioned this, it came from Netflix,
[1483.84 → 1487.18] where they have that sort of browser already.
[1488.22 → 1491.04] Yeah, so let's talk about that for a second, because Adam,
[1491.16 → 1493.24] you can just hang out with two API junkies who are talking here.
[1494.66 → 1495.60] I'm taking notes.
[1496.06 → 1496.52] There you go.
[1496.86 → 1501.62] So basic authentication is built into Hurl It, right?
[1501.62 → 1508.64] Yeah, the ability to just enter a username and password instead of having to do the hashing.
[1508.94 → 1509.24] Sure.
[1509.34 → 1511.48] What would it take to get OAuth integration?
[1511.58 → 1514.46] Because that tends to be a much harder problem to solve.
[1514.54 → 1515.98] I remember when I was writing the LinkedIn gem,
[1516.20 → 1520.18] I had to write my own stubs just to dump fixtures to test calls,
[1520.24 → 1521.82] because OAuth does add some complexity.
[1522.60 → 1523.16] Oh, definitely.
[1523.60 → 1527.00] We thought about doing OAuth in time for the Rails Rumble.
[1527.00 → 1531.60] On Sunday afternoon, the last day of the Rumble, we talked about adding it in,
[1531.68 → 1534.72] and I played around with a bunch of different, well,
[1534.78 → 1539.08] I found a nice OAuth gem that I liked and wanted to use,
[1539.36 → 1541.24] and played around with it a bit.
[1541.32 → 1543.58] But what it came down to was the UI was complicated.
[1543.88 → 1548.76] It's actually very complicated to set up all those steps in a way that's simple
[1548.76 → 1552.02] and easy enough for anybody to use.
[1552.02 → 1558.60] And I think I've seen there's a tool, there are a couple tools for OAuth that are pretty nice.
[1558.70 → 1562.58] I think Google has one that's pretty good,
[1562.66 → 1569.10] but I haven't really seen any that I thought were simple enough to be a perfect web application.
[1570.12 → 1572.76] So a UI design, I think, is the answer.
[1573.86 → 1576.38] So let's talk about Six Apart.
[1576.66 → 1577.94] How long have you been at Six Apart now?
[1579.00 → 1580.94] Since December of last year.
[1580.94 → 1585.64] So what kind of endeavours is Six Apart doing in terms of open source?
[1585.74 → 1586.16] It's really cool.
[1587.54 → 1593.52] So the really cool thing that they've done in the past year is actually a Django project called Motion,
[1593.92 → 1600.50] and it's on Six Apart's GitHub site, GitHub.com slash six apart.
[1602.12 → 1604.08] And it's actually called Typepad Motion.
[1604.08 → 1604.42] Yeah, okay.
[1604.58 → 1605.58] Yeah, Typepad Motion.
[1605.58 → 1619.02] And what it is it's a community site mostly aimed at sort of celebrities and, you know, groups, online groups.
[1619.22 → 1621.08] And you can go there, and you can discuss things.
[1621.18 → 1624.38] You can post content and comment on that content.
[1624.38 → 1632.52] And it powers sites such as Paris Hilton's community site and Zachary Quito from Star Trek.
[1633.18 → 1634.26] So it's pretty fun.
[1634.48 → 1635.36] It's interesting.
[1638.24 → 1639.46] It's a fun Django project.
[1639.58 → 1640.32] And it's all open source.
[1640.32 → 1645.80] And so if you wanted to use that, how would you go and get started with using it?
[1645.86 → 1654.26] Just pick it up and just – you have to be a Django user or is there something that Six Apart does behind the scenes that help them out?
[1654.26 → 1662.24] So if you go to developer.typepad.com – I can't believe I'm messing up my URLs today.
[1664.34 → 1669.92] But there are step-by-step instructions on how you can get it installed and how you can get it running and how all the components work.
[1671.00 → 1672.46] And it's pretty nice.
[1673.76 → 1673.90] I'm not sure –
[1673.90 → 1675.46] Oh, it's running up on the App Engine.
[1676.82 → 1682.62] Yeah, they actually have it working on App Engine now, which was kind of their task for – or people have been working on that for a little while.
[1682.62 → 1683.82] A couple of people I know at Six Apart.
[1684.88 → 1685.68] That's pretty cool.
[1686.00 → 1691.62] It's pretty nice that they can strip it down, or it can be stripped down to work on App Engine and –
[1691.62 → 1696.06] You mentioned earlier that you're no longer a developer at Six Apart.
[1696.16 → 1698.16] You're more of a product manager, right?
[1698.50 → 1707.68] What was the transition like going from more of behind the scenes making things work to sort of going to the different direction to being product manager?
[1708.22 → 1710.18] Well, I've always really loved making –
[1710.18 → 1710.72] Product manager, sorry.
[1711.28 → 1711.86] I bet.
[1711.86 → 1712.30] Project.
[1712.36 → 1713.84] I mess them up all the time.
[1716.88 → 1721.12] And in my mind, you do a little bit of both for everything anyway.
[1721.56 → 1732.42] But I'd always been interested in making projects from the ground up and making them from scratch, which is one of the reasons that I love competitions like the Rails Rumble,
[1732.72 → 1737.20] is that you have this opportunity to sort of come up with an idea and see that from start to finish.
[1737.26 → 1738.46] And that's what I really love doing.
[1738.46 → 1742.08] I'm not so much just a developer as I am.
[1742.18 → 1743.64] I like to make whole projects.
[1744.28 → 1756.06] And so once I realized this, and I realized I was at a large company where, you know, you are a developer, or you're a product manager, I wanted to have that be my more official title.
[1756.06 → 1760.34] While I still did a little bit of development, not very much.
[1760.34 → 1764.98] I really like sort of coming up with new concepts and new projects.
[1764.98 → 1766.88] So it's different.
[1767.54 → 1769.48] What projects are you leading right now?
[1769.48 → 1772.90] So let me see.
[1773.02 → 1779.80] None of my – oh, one of the projects I worked on has been released, Type kit integration with Typepad.
[1780.46 → 1785.20] So you can set up – so Type kit is a provider of fonts.
[1785.20 → 1786.98] So –
[1786.98 → 1789.44] That's the fonts under subscription, right?
[1789.92 → 1790.42] Yes.
[1790.48 → 1794.40] You subscribe, and can get fonts from renowned type designers.
[1794.62 → 1796.14] So actual real type designers.
[1796.80 → 1798.32] And you can put them on your website.
[1798.60 → 1803.28] So I'm kind of hoping to see the death of Helvetica and Ariel and Times New Roman.
[1803.82 → 1804.26] All right.
[1804.26 → 1806.66] I'm excited to see new fonts on the web, right?
[1808.42 → 1810.62] It's kind of nice to see a little bit more variety.
[1810.70 → 1818.00] Every time I see a blog or, you know, a website, and they use just a crazy typeface, I'm just – I'm super impressed.
[1818.00 → 1830.18] So what happened was there was a hack made by Ben Trout, the founder of Six Apart, to add these custom fonts to Typepad blogs.
[1830.40 → 1834.08] So I helped sort of get that released, which was fun.
[1835.20 → 1837.32] Were you involved with Typepad Micro?
[1837.54 → 1839.22] I know that was a recent release.
[1840.50 → 1841.02] Yeah.
[1841.26 → 1844.10] I started doing product management on Typepad.
[1845.16 → 1854.24] Well, formerly I had worked on Motion, the Django open source project, and then switched to doing product management in part because I wanted to work on Micro.
[1855.12 → 1857.24] I think it's a really cool project.
[1857.96 → 1863.24] I really like the idea that you can sign up for Typepad for free, which is awesome.
[1863.24 → 1866.00] And it's really nice and simple and fun.
[1866.66 → 1868.04] Are you getting attacked by school children?
[1869.18 → 1875.78] There's a school near my apartment, and my windows face the street.
[1875.78 → 1885.12] So I guess one thing you mentioned before was you realized that you have this big company to just sort of play in.
[1885.46 → 1892.84] What is it like to go from back in school, playing with Java, dabbling in Python to build Pounce?
[1892.84 → 1896.46] And then you mentioned being acquired and what that process was like.
[1896.64 → 1902.78] But now you're this product manager who can just decide on anything and play in this big company.
[1902.94 → 1903.70] What's that like now?
[1904.04 → 1905.00] What kind of freedom do you have there?
[1905.00 → 1907.80] It's all different.
[1908.12 → 1909.36] It's all a different process.
[1910.00 → 1913.34] I always love change and doing different things.
[1913.74 → 1924.40] And part of the fun of working at Sixth Part is getting to sort of play around with bigger projects, big sites like Typepad.
[1924.40 → 1928.62] But at the same time, that also comes with a little bit of restriction.
[1929.64 → 1934.84] It's not like Pounce, where I'd come up with something, and it would be out the door the next day.
[1935.68 → 1936.74] It takes a little bit more.
[1937.34 → 1941.74] You have to spend a little more time thinking about your decisions because they impact a bigger audience.
[1941.74 → 1946.56] Do you get an opportunity to go and speak a lot at different conferences?
[1948.18 → 1950.32] I used to more than I do now.
[1951.54 → 1953.32] I used to more than I do now.
[1954.60 → 1958.86] But yeah, still occasionally on a wide variety of stuff.
[1959.42 → 1965.00] It's kind of fun to have done everything from a startup to open specifications.
[1965.00 → 1972.14] So, you know, one conference I'll be talking about OAuth and another one I'll be talking about being a female entrepreneur.
[1972.58 → 1974.58] It's like two totally different things.
[1975.46 → 1979.00] I have a sort of maybe a controversial topic to ask you about.
[1979.12 → 1983.06] Would you consider being a female in this industry an asset or a liability?
[1984.22 → 1985.18] Oh, that's a good question.
[1985.28 → 1985.98] And it's both.
[1986.36 → 1987.88] It definitely is both.
[1988.96 → 1991.76] It's an asset because you're kind of a curiosity.
[1991.98 → 1993.84] People want to know who you are and what you're doing.
[1993.84 → 2005.48] And if you can play that in the right way to sort of get attention to, you can promote worthwhile causes or, you know, sort of get to know a lot of people that you might not have gotten to know otherwise.
[2006.16 → 2017.82] But it also is a liability in that you really have to sort of go the extra mile to prove yourself in things that I think other people would consider men competent at right away.
[2017.96 → 2020.66] It's kind of it's a little bit like a little bit of a prejudice.
[2020.66 → 2025.34] And, you know, it's something I think we all have, myself included.
[2026.56 → 2031.50] Well, you've got to admit that it's got to be great not having to stand in line for the restroom at conferences, right?
[2032.86 → 2033.82] Yes and no.
[2034.06 → 2038.12] I go to these women in tech conferences, and it's like twice as bad.
[2039.54 → 2047.96] But, yeah, no, that's actually my secret was in college I would always use the restroom in the computer science building whether I had a class there or not at that time of day.
[2047.96 → 2050.20] Just because they were always clean and always empty.
[2051.34 → 2052.54] Well, how did you get into computers?
[2052.68 → 2057.64] Because I hear the argument a lot that we need to get more young ladies into computer science.
[2057.88 → 2060.16] So, you know, how did you get involved with programming?
[2060.92 → 2066.20] Well, we always had a computer in our home, and I was always kind of the ruler of the computer.
[2066.90 → 2071.54] I don't know if you guys were as well, but sort of the person that owned the family computer.
[2071.54 → 2075.42] And I only have sisters, so it was pretty easy.
[2075.62 → 2076.36] And I'm the oldest.
[2076.40 → 2084.54] I was the oldest of three girls, so it was easy to sort of keep my sisters away from the computer when I wanted to use it selfishly.
[2085.78 → 2092.18] So, and I ended up making websites when I was in my teens because I thought it was fun.
[2092.28 → 2095.48] And I made like an Angel Fire site and a GeoCity site.
[2097.72 → 2098.58] That's awesome.
[2098.58 → 2100.78] Yeah, like HTML sites.
[2101.00 → 2105.36] And I thought it was so cool because I'd have my own website, and I'd show my friends.
[2105.46 → 2106.92] And then my friends had their own websites.
[2107.20 → 2108.66] And then they'd make their own websites.
[2109.00 → 2113.44] And then, you know, it was like when you get bored with AIM, you'd start making websites.
[2114.64 → 2119.32] Which I'm kind of sad that I don't know how that exists in any form today.
[2119.48 → 2125.58] Like if you wanted to make your own HTML CSS, I guess you maybe like stiff up your MySpace page.
[2125.58 → 2126.98] I don't know what the...
[2126.98 → 2128.30] Maybe Google Sites.
[2128.58 → 2131.38] It's probably the closest thing we have nowadays because GeoCity is gone.
[2132.20 → 2132.84] Kids today.
[2133.14 → 2133.88] That's true, yeah.
[2134.18 → 2134.96] MySpace pages.
[2135.20 → 2136.76] As a father of two...
[2136.76 → 2137.46] Oh, what was that?
[2137.52 → 2137.70] Sorry.
[2138.00 → 2143.10] As a father of two, you know, hopefully I've got two girls that might fall in your footsteps.
[2143.10 → 2148.96] We'll see if my four-year-old, my oldest, has an old hand-me-down MacBook that I was so proud the other day.
[2149.00 → 2151.60] She came in and asked me, did we just lose internet?
[2154.60 → 2156.32] Did you lose your Wi-Fi connection?
[2157.40 → 2157.76] Exactly.
[2157.76 → 2159.26] Oh, funny.
[2159.26 → 2160.14] It's awesome.
[2160.14 → 2160.46] Yeah.
[2161.06 → 2167.32] You know, I think part of it is just encouraging creativity and exploration.
[2167.76 → 2171.22] You know, we poke around at computers all day and aren't afraid they're going to break.
[2171.56 → 2174.02] And I think that's a really valuable concept.
[2174.48 → 2180.20] You know, the idea that you can play around with something and really sort of push its limits.
[2180.20 → 2185.20] So we're at the point in the call where we ask what's on your open source radar.
[2185.42 → 2191.90] So we want to know what's cool in open source out there for you that you're just dying to play with.
[2194.44 → 2195.22] Open source.
[2195.40 → 2201.00] I recently played with Node.js, building some sites, server-side JavaScript.
[2201.32 → 2202.06] It's kind of interesting.
[2202.22 → 2207.90] Both the concept of server-side JavaScript and event-driven programming, which I hadn't really done a lot of before.
[2207.90 → 2210.48] You don't know it, but you just kept the streak alive.
[2210.62 → 2215.12] I think that's 10 or 11 straight episodes that we mentioned Node.js.
[2215.30 → 2216.60] I think it's since episode four.
[2218.10 → 2218.50] Awesome.
[2218.96 → 2223.00] Well, it's sort of been like the most recent big project to sort of come out.
[2223.18 → 2225.18] So it doesn't surprise me too much.
[2227.30 → 2228.80] I'm trying to think of anything else.
[2228.80 → 2230.42] There's a lot of stuff going on out there, too, with that.
[2230.50 → 2234.44] We just got introduced to howtonode.org.
[2234.94 → 2235.86] If you want to check that out.
[2236.28 → 2236.68] Okay.
[2236.68 → 2238.52] Two fellow listeners of the changelog.
[2238.94 → 2241.64] I can never pronounce their name right, but if you've got it.
[2241.92 → 2242.50] Is it Mikkel?
[2243.24 → 2244.52] Yes, and Tim Caswell?
[2244.96 → 2245.50] Tim Caswell.
[2245.66 → 2248.58] So they actually run this open blog.
[2248.82 → 2253.44] And what I mean by open blogging, and if you can read this other blog post, we'll probably send you a link to.
[2253.44 → 2258.52] But they essentially just wrote this blogging engine in Node.
[2258.96 → 2260.06] And they put it on GitHub.
[2260.26 → 2260.84] It's open source.
[2260.84 → 2265.78] So if you want to write an article, you just fork it, write your article, and send them a pull request.
[2267.40 → 2267.80] Interesting.
[2268.08 → 2269.30] That's kind of crazy.
[2269.30 → 2279.50] And then a good friend of ours and fellow listener of the changelog and, I guess, fellow designer, he's more of a SaaS and front-end kind of guy and works a lot in Compass.
[2279.50 → 2284.74] If you plan those words, I'm not sure if you touch that much in your projects.
[2284.74 → 2300.48] But he wrote a recent article about kind of open blogging in general, just taking the concept of a blog as source code, like Octopuses or Jekyll or Statistic or something like that, and sort of opening up the doors to anyone.
[2301.16 → 2304.58] Just fork it, write an article, and send them a request.
[2304.58 → 2307.28] I'm not a lover of Static blogs.
[2308.78 → 2326.32] So, I mean, I like the idea of guest authors and contributing posts, but I sort of feel like database-based blog posts were sort of – this is going to get me in so much trouble, but I'm kind of a sucker for databases despite the new trend.
[2326.32 → 2329.26] What's your favourite CMS?
[2329.52 → 2334.80] Because Adam and I are kicking around some ideas, and we'd love to hear your thoughts on the subject.
[2335.68 → 2337.04] You know, that's tough.
[2337.18 → 2339.60] It sort of depends on what you're looking to do with it.
[2339.86 → 2343.40] Well, I guess it sticks apart, you have to say, that Typepad.
[2343.40 → 2344.08] Google Type?
[2344.30 → 2346.78] I haven't looked at Google Type much at all.
[2347.06 → 2351.32] But Typepad actually is great for blogging, and I would recommend it.
[2351.32 → 2357.18] I mean, I switched my blog over to Typepad about six months after I started working at Six Apart.
[2357.70 → 2368.86] But part of the reason I did was I had been working on it for a while, and I had been using it to test things for – I wasn't actually working on Typepad at the time, but I had been playing around with it.
[2368.86 → 2371.48] And what I realized is, like, why am I hosting my own blog?
[2371.84 → 2373.74] Like, I have so many other projects that I work on.
[2373.80 → 2377.78] The last thing I want to do – and I was using WordPress at the time – the last thing I want to do is upgrade WordPress.
[2377.78 → 2381.18] That was, like, the last way that I want to spend my weekend.
[2381.74 → 2387.16] So I was like, I'm just going to switch to a hosted blog, and Typepad's there, and it was great.
[2387.70 → 2399.96] So I know that makes me not the best engineer, but sometimes you have to pick and choose which things you really want to spend your time hacking on in your weekends.
[2401.12 → 2402.42] So what is it with the database?
[2402.56 → 2404.08] What do you miss if you go static?
[2404.22 → 2406.42] What is it that ties you back to the database?
[2407.78 → 2412.38] The ability to easily edit posts, I guess, from, like, a UI.
[2412.64 → 2416.10] Like, I'm someone who just wants to – when I'm coding, I'm coding.
[2416.20 → 2417.46] When I'm blogging, I'm blogging.
[2417.56 → 2424.74] I don't want to, like, go into my own blogging application and notice a bug and then want to fix that when really I should be writing a blog post, you know?
[2425.62 → 2425.90] So.
[2426.60 → 2427.34] Ah, I see.
[2427.52 → 2427.80] Okay.
[2428.60 → 2429.00] Yeah.
[2429.00 → 2439.52] So the thing with us, the reason why we were looking at the concept was because I use WordPress to publish this website for the Web 2.0 show, which is another podcast I run.
[2440.42 → 2442.42] And so I use WordPress.
[2442.60 → 2447.06] So I tend to just write all my posts in TextMate and save the file locally.
[2447.06 → 2450.30] And it might be in HTML or whatever I'm writing it in.
[2450.50 → 2452.16] Then I copy, and I paste into WordPress.
[2452.28 → 2455.10] So I don't actually do a lot of drafting inside the UI itself.
[2455.10 → 2456.16] Do you write them in HTML?
[2456.94 → 2458.40] Do you write your blog post in HTML?
[2458.66 → 2459.24] Or do you use, like, Markup?
[2459.24 → 2464.46] Well, I think WordPress actually uses – out of the box WordPress, I'm pretty sure, just supports HTML in there.
[2464.58 → 2466.58] So that's the only real option you have.
[2467.34 → 2468.16] I love Markdown.
[2468.40 → 2469.42] Markdown's probably my favourite.
[2469.42 → 2472.48] I like Markdown, too, but I think that it requires a plug-in.
[2472.60 → 2473.42] I have just been lazy.
[2473.66 → 2474.50] I just didn't put a plug-in.
[2475.58 → 2480.46] You know, I write HTML so fast that I almost prefer to just do everything in HTML.
[2480.92 → 2483.82] Speaking of HTML, have you played much with Hamill at all?
[2484.74 → 2486.44] No, actually, I have not.
[2486.80 → 2489.02] And so I prefer to stay out of that argument.
[2492.58 → 2493.66] Anything else on your radar?
[2494.46 → 2495.70] Oh, anything else.
[2495.82 → 2496.36] Oh, Geez.
[2496.44 → 2497.54] You guys caught me unprepared.
[2497.54 → 2498.76] I would have prepared a list of stuff.
[2499.00 → 2500.88] Anything in the NoSQL space got you excited?
[2501.06 → 2503.64] And JavaScript in the server is big, so is NoSQL right now.
[2503.68 → 2507.48] You know, I've tried almost every NoSQL option out there.
[2507.86 → 2512.76] And I can't say every one, but I've used Couch DB, Congo, and Regis.
[2513.94 → 2517.36] And every time, I'm just crying to get back to SQL.
[2520.54 → 2522.66] I'm one of these people that I like the niceties.
[2523.42 → 2524.92] I like the stuff that's been added on.
[2524.92 → 2533.88] And I feel like it's such a new space that the tools really aren't quite there yet for everything that you want to do.
[2536.34 → 2537.36] Anyway, that's horrible.
[2537.48 → 2538.70] It's going to get me in so much trouble.
[2539.70 → 2542.00] A lot of people are entitled to their own opinion, of course, right?
[2542.52 → 2544.16] Yeah, definitely, definitely.
[2544.38 → 2547.94] It's the first time I've really shared my horrible opinions on NoSQL.
[2547.94 → 2550.10] But, I mean, it's an exciting space.
[2550.20 → 2558.02] I mean, for Bacon File, Bacon File uses Couch DB as the main storage engine, which is good and bad.
[2558.48 → 2569.08] It's great because it works really well for Bacon File, the concept of documents, because it literally is documents that you're storing, even though it's not quite the same type of document.
[2569.16 → 2571.78] But you're storing a bunch of metadata about one object.
[2571.78 → 2574.56] So you really are – it sort of fits the paradigm well.
[2575.72 → 2586.50] And with Hurl, we used Regis, which sort of worked well because we had a very small amount of information to store and very specific.
[2586.92 → 2588.12] So I don't know.
[2588.42 → 2593.70] They have their place, and I'll keep trying them out, but I'm not quite – maybe I'm just not in love with one yet.
[2593.70 → 2597.04] What was that we talked about last night when it was React?
[2597.46 → 2597.86] React.
[2598.24 → 2598.64] React.
[2598.88 → 2599.34] There you go.
[2599.52 → 2601.12] I pronounce it incorrectly every time.
[2601.20 → 2602.68] It's spelled R-I-A-K, right?
[2603.60 → 2604.62] R-I-A-K.
[2604.92 → 2605.12] Yeah.
[2605.62 → 2611.48] And so that's like an open source and a commercial version of like a NoSQL type of solution.
[2612.62 → 2613.36] Have you played with that one?
[2613.92 → 2614.96] No, I have not.
[2615.42 → 2615.82] Wow.
[2616.68 → 2617.36] I'm surprised.
[2617.36 → 2618.64] There's lots of –
[2618.64 → 2619.54] Yeah.
[2619.98 → 2621.22] Yeah, no, it looks pretty cool.
[2621.22 → 2622.88] Well, you just have to be a better listener of the changelog.
[2622.88 → 2625.52] You'd be on the up and up if you'd like to be on open source.
[2625.62 → 2626.46] I mean, it moves fast.
[2626.52 → 2627.24] We hope you keep up.
[2628.04 → 2628.82] Yeah, you're right.
[2628.92 → 2629.68] You're totally right.
[2629.80 → 2631.14] I should keep up a little bit better.
[2632.96 → 2637.30] Vince, Vince, Chuck, at my plug, my shameless plug of our tagline.
[2637.36 → 2639.48] Our tagline is open source moves fast.
[2639.58 → 2640.46] Keep up.
[2641.32 → 2647.54] It is very true, and I hate to admit that I fall behind a little bit sometimes.
[2648.52 → 2651.72] But what I sort of like to do is I'm very much like a product person.
[2651.72 → 2655.22] I can't really just play around with the latest technology without building something.
[2655.58 → 2660.02] So that's my horrible vice is I love to build projects.
[2660.48 → 2671.16] And in that process, I end up using new technologies, but I'm not one to go seek them out and play with them necessarily without strong reason.
[2671.16 → 2676.42] Well, Lee, it was actually quite a pleasure to sit down and chat with you.
[2676.56 → 2678.64] You have such a deep past.
[2678.88 → 2686.14] And like you said, you've gone from the startup space to working at Six Apart and doing all the cool stuff you guys are doing there.
[2686.40 → 2687.78] So you've kind of run the full gamut.
[2687.86 → 2688.84] You've worked with Kevin Rose.
[2688.94 → 2690.34] You've worked with Daniel Berger.
[2690.82 → 2694.38] You've been to the hot parties, and you've been behind the scenes too.
[2694.38 → 2699.04] So it's really cool to have the chance to have this chat with you.
[2699.18 → 2700.26] We appreciate you coming on the show.
[2701.26 → 2703.14] Yeah, thanks so much for having me, you guys.
[2703.22 → 2711.48] I know I'm not the typical open source project developer, but I really love some of the new projects that are coming out.
[2711.56 → 2714.98] And I'm excited to find out more, so I guess I'll have to keep up with you guys a little better.
[2715.46 → 2715.90] Yeah, for sure.
[2716.72 → 2717.60] Yeah, thanks.
[2717.88 → 2718.22] No problem.
[2718.22 → 2718.46] Thanks.
[2724.34 → 2727.28] Thank you for listening to this edition of The Changelog.
[2728.38 → 2735.04] Point your browser to tail.thechangelog.com to find out what's going on right now in open source.
[2736.28 → 2744.82] Also, be sure to head to GitHub.com forward slash explore to catch up on trending and feature repos, as well as the latest episodes of The Changelog.
[2748.22 → 2778.20] The Changelog.
[2778.22 → 2780.68] I hope you guys enjoyed.
[2780.68 → 2782.32] Bring it back.
