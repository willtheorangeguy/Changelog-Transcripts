[0.08 → 8.56] The Change Log was brought to you by Pusher, a hosted API that lets you quickly, easily, and securely add scalable real-time functionality to web and mobile apps.
[9.10 → 18.50] Check out Pusher's real-time showcase at pusher.com slash showcase to learn how Gauges, Cloud App, Buffer, and many others are using the awesomeness that is Pusher.
[19.12 → 24.06] Join the real-time web and get your free API account at pusher.com.
[30.00 → 43.14] Welcome to The Change Log, episode 0.7.4.
[43.36 → 44.40] I'm Adam Stachowiak.
[44.70 → 45.56] And I'm Won Netherlands.
[45.76 → 46.74] This is The Change Log.
[46.80 → 48.32] We cover what's fresh and new in open source.
[48.54 → 51.28] If you found us on iTunes, we're also on the web at thechangelog.com.
[51.72 → 54.72] And we're also on GitHub, so head to GitHub.com slash explore.
[54.80 → 58.96] You'll find some training repos, some feature repos from our blog as Wealthy Audio Podcast.
[58.96 → 61.44] And if you're on Twitter, we've said it before.
[61.62 → 62.92] Stop following Change Log Show.
[63.10 → 64.78] Follow The Change Log, because that's who we are.
[65.42 → 66.50] And I am Adam Stack.
[66.98 → 69.20] And I'm Penguin, P-E-N-G-W-Y-N-N.
[69.64 → 70.98] Fun, fun episode this week.
[71.06 → 75.64] Talked about some open source typography with Micah Rich from the League of Movable Type.
[76.54 → 77.38] We're both fanboys.
[77.88 → 79.02] Yeah, big, big fanboys.
[79.16 → 85.22] I was really encouraged by his passion for typography, for one, but also open source and how that kind of bleeds into
[85.22 → 91.04] how he learns some of the technologies he knows about just by being able to play with open source technologies.
[91.46 → 98.24] I was impressed with his dev shops using Sinatra and Warden and some open source projects to build Letter case,
[98.32 → 99.32] which we get into in the show.
[99.54 → 99.80] Yeah.
[100.64 → 103.82] Well-rounded, well-talented individual, that Micah.
[104.20 → 104.68] He is.
[104.68 → 108.08] I hate to say it in a bad way, but I was surprised as well.
[108.08 → 115.04] I just expected him to be more of the designer side of open source, considering the League and all that.
[115.80 → 120.68] I want to send out another special thank you to Pusher App for backing this podcast.
[120.96 → 125.20] If you're not using Pusher to power your real-time internet, you should check it out.
[125.80 → 128.94] Power's such interfaces as Gauges and others.
[129.10 → 132.00] It's a really cool tool, and you'll have a lot of fun playing with Pusher.
[132.68 → 134.26] Join the real-time web.
[134.98 → 136.04] What episode should we get to it?
[136.44 → 136.92] Let's do it.
[138.08 → 149.62] We're chatting today with Micah Rich from League of Movable Types.
[149.70 → 151.58] Micah, why don't you introduce yourself for our listeners?
[152.64 → 153.96] Hey, I'm Micah.
[153.96 → 158.28] I am one of the founders of the League and of a good company.
[159.10 → 160.32] But what's the name of the company?
[161.04 → 161.66] A Good Company.
[162.36 → 163.04] No, seriously.
[163.32 → 164.24] Dude, what's mine say?
[164.46 → 164.76] Sweet.
[164.76 → 169.34] Tell us how League of Movable Type came about.
[171.60 → 176.08] It was right after my old business partner, Caroline, and I.
[176.48 → 177.68] Caroline had a Lozano.
[177.68 → 189.28] We started a good company, and it was sort of in the days before people were using interesting fonts on the Internet, which honestly was not that long ago.
[189.34 → 190.78] It was, I don't know, three years ago.
[190.78 → 198.12] And we were starting to do client work, and we're looking to find some cool fonts to use.
[198.28 → 204.64] And it was just so difficult to find one that we were allowed to actually embed on a site with Font face.
[204.64 → 212.82] And so we were looking around, and I found this thread on typophile.com, if you guys know that one.
[212.82 → 212.92] Yeah.
[213.76 → 217.48] A lot of insider chat there with the typography folk.
[218.36 → 219.16] Yeah, yeah.
[220.10 → 223.70] A lot of very talented people on that posting their opinions.
[223.70 → 235.84] So someone had gone on and started a thread just sort of asking if anybody knew of any open source fonts that somebody could use for, like, a student project or something.
[236.38 → 244.32] And there was this incredible, like, 10-page backlash from all the professional typographers being like, how dare you?
[244.64 → 250.86] Like, that's totally ruining our professional business, and how could you even ask something like that?
[250.86 → 270.28] And I was just completely astounded just from, I don't know, my background, I guess, being from, like, I had worked at Thought Bot at the time in Boston, who, you know, every programmer there is amazing and professional and has awesome open source projects.
[270.28 → 280.34] And the fact that the typographers were, like, so disgusted at the idea of sharing something, it, you know, kind of brought about the rebel in me.
[280.42 → 283.04] And I was like, man, we got to do something about that.
[283.66 → 295.96] So, you know, we started with a font that Caroline had made in college just to say, hey, if we're going to do it, we might as well start with us and contribute something.
[295.96 → 300.60] And, I don't know, it kind of just has been exploding ever since, I guess.
[300.80 → 301.66] And which font was that?
[302.86 → 303.76] That was Junction.
[304.02 → 305.12] Junction was the first one.
[305.16 → 306.68] I thought for sure you were going to say League Gothic.
[307.84 → 310.76] No, no, no, that actually didn't come out until much later.
[311.98 → 318.46] So, speaking of Revolution, that's actually part of the tagline on the homepage, which is, no more BS, join the Revolution.
[318.46 → 326.08] So, it was, I didn't even know you were part of Thought Bot, and truth be told, just this past episode, was it Joshua Clayton, Wynn?
[326.88 → 327.30] That's right.
[327.46 → 331.72] He's at Thought Bot, and they chatted about Tmux and CLI goodness.
[332.84 → 334.92] What was that conversation about, Wynn?
[335.02 → 336.02] I missed that one.
[336.58 → 338.18] A lot of command line seeker.
[338.32 → 338.68] There you go.
[338.94 → 340.64] And that's cool that you guys kind of overlap there.
[341.10 → 342.94] And Thought Bot is big in open source.
[342.94 → 348.58] They're big about sharing and just knowledge share and open source sharing and stuff, so that's awesome.
[349.54 → 349.64] Yeah.
[349.78 → 354.74] I mean, I honestly was not there very long, but I loved it.
[354.98 → 359.44] They are amazing people, and they totally opened my eyes to a million different things.
[359.50 → 363.50] And I think that was a lot of it, too, the open source contributions that they've done.
[363.62 → 367.80] So, you think that's where you kind of got the bug of open source, or just was it before that?
[367.80 → 378.96] I had definitely paid attention to it before, because, I mean, I, in college, had taught myself, for our senior thesis, how to use Rails.
[379.08 → 381.20] We built, like, a social network as our senior thesis.
[382.76 → 389.66] And I would not have had anything built had it not been for all the people that had shared their gems and libraries and whatnot.
[389.66 → 398.20] And so, I kind of knew about it, and then going into Thought Bot, they were so into it that I think that just solidified my perception of how it should be.
[399.90 → 404.34] So, when you started the league, how much education on Font Face did you have to do?
[407.08 → 407.82] Quite a bit.
[407.92 → 413.16] I mean, there wasn't really a lot going on with it at the time, honestly.
[413.30 → 417.58] It was sort of browsers had just started experimenting with allowing it.
[419.66 → 426.30] And so, they're definitely, everybody was still learning how to use it, I think, at the time.
[427.62 → 430.92] And since then, you know, people are experts now.
[431.84 → 434.24] But at the time, we were all kind of just making it up as we went along.
[436.34 → 440.98] So, League Gothic is, I think, by far my favourite in your catalogue.
[441.90 → 444.26] Are all of your fonts included in Type kit?
[445.90 → 446.26] No.
[446.26 → 456.56] Yeah, well, Type kit had contacted us at one point saying, you know, we want to get your stuff in there.
[456.72 → 458.44] And I thought that it was a really cool idea.
[459.84 → 466.22] And we kind of just agreed that as long as it was available for free on the free plan, then it was cool.
[466.22 → 471.18] But, I mean, I haven't looked recently.
[471.80 → 474.26] I think not all of them are on there.
[474.48 → 479.00] And I know there's at least one that we had to take off.
[480.16 → 486.46] Which, you know, it was, I think, Ostrich Sands had been on there.
[486.46 → 492.82] And then Tyler Fink was the guy who made it.
[493.12 → 499.48] And he kind of had some moral obligations to that, which I think were reasonable.
[499.74 → 501.66] And so they worked with us to take that one-off.
[502.96 → 506.30] So with Type kit, they have a slightly different embedding mechanism.
[506.42 → 507.82] It depends on JavaScript.
[507.82 → 517.54] So I guess part of the DRM process, even if the font's free, they split up the font in a couple of different files to keep you from embedding and stealing the font in one shot.
[517.60 → 517.98] Is that right?
[518.34 → 518.92] Right, yeah.
[519.02 → 523.58] And I think they worked with Google to make that with their Google Web Fonts project.
[523.78 → 526.26] I think they collaborated to make that JavaScript library.
[526.26 → 532.24] Right, and it can pull fonts from Google's library as well, which is growing, by the way.
[533.44 → 540.86] How much do you view, I guess, that library or that collection as competition or just furthering the cause?
[543.66 → 545.02] Yes and no.
[545.98 → 549.68] I mean, they have a ton of open source stuff on there, which I think is awesome.
[549.68 → 558.94] And the guy in charge of that pretty much is a guy named Dave Cross land, who we've talked a bunch of times about all kinds of stuff.
[559.16 → 562.02] And he's a really intelligent dude who totally knows what he's doing.
[563.04 → 577.32] At the same time, I sort of have some personal reservations about the way that they go about doing stuff, which I think applies more to Google than Dave or the Web Fonts project specifically.
[577.32 → 600.00] One of the things I love about your presentation on your catalogue, like so many type foundries, you show real-life working examples of the font in the wild with print layouts and designed layouts around them instead of just showing them in a gallery view.
[600.50 → 600.94] Yeah.
[601.16 → 606.20] Is that part of just the design aesthetic that you guys want to embrace, or how did that come about?
[607.32 → 612.20] It was sort of a natural thing that I'm not sure was ever a conscious decision.
[612.44 → 623.24] But when we were designing it the first time, we had just been used to, in design school, having spec posters that we would make.
[623.80 → 629.52] It's just something that a lot of typographers do, I guess, to show off, hey, how awesome is this font?
[629.58 → 630.80] Let's look at it being used.
[630.80 → 634.38] And we just wanted to do that for our own stuff.
[634.48 → 636.58] And we kind of had some of that already, too.
[636.70 → 638.48] So we were like, hey, this looks gorgeous.
[638.96 → 640.06] You know, we should do that.
[640.30 → 643.24] And it turned out to be a really great thing.
[643.30 → 645.78] Like, I can't imagine not doing that at this point.
[646.28 → 647.18] I think it would look horrible.
[647.18 → 655.14] So part of, I guess, embracing open source with typography, part of that is actually accepting pull requests.
[655.44 → 660.58] You know, that was kind of glorified by GitHub to fork and send a pull request of some changes.
[660.72 → 669.02] What are some of the fonts that you've got or types that are on GitHub that have been forked and have been changed?
[669.16 → 673.28] And can you describe some changes that have happened that you just absolutely loved?
[673.28 → 675.28] Yeah.
[676.00 → 679.40] Honestly, that hasn't happened as much as I want yet.
[679.64 → 684.38] And that's kind of a crusade that I need to bring up more, I think, to people.
[685.22 → 693.04] But there have been, like, our two most popular, I think, have been Chunk and League Gothic.
[693.04 → 707.26] And for both of those, we got, I guess, pull requests from random people that we had never met that we had no affiliation with that had gone in and been like, hey, it was missing a bunch of extra characters.
[707.46 → 708.42] I threw those in.
[708.68 → 710.14] I fixed some of the kerning.
[711.84 → 716.86] Somebody once made an italic version of League Gothic, which I think is awesome.
[717.06 → 719.08] And I totally want to promote doing that more.
[719.08 → 725.90] I think that's most of what it's been so far.
[726.40 → 730.46] And I would love to, I don't know, try to...
[730.46 → 742.74] I think my goals for the future with the League are, like, to try to educate people on how to do stuff so that they can experiment and do crazier things than adding an italic version.
[742.74 → 749.50] Like, that's cool, but you can do so much crazier stuff by forking a font and playing with it.
[749.72 → 759.06] So imagine you were on a podcast, and you had a chance to tell a bunch of people how to better fork and change and commit things back to the League.
[759.22 → 760.12] What would you say to them?
[760.12 → 768.34] I mean, I'm hoping at some point to help educate typographers on how Git works.
[768.44 → 769.60] I feel like that's its own thing.
[769.60 → 787.48] But, you know, I think the main idea is that it's really not that hard to open up the source for these fonts and use them to see how they were made so that you can understand how kerning classes work.
[787.48 → 794.90] And, you know, why someone has this many points in an N versus an O and that kind of stuff.
[795.14 → 803.90] And as for how to do it, I mean, research, you know, how GitHub does pull requests and go do that.
[803.94 → 804.68] It's really not hard.
[804.88 → 810.94] You, like, go to our GitHub page, hit fork, and pull it to your computer.
[811.18 → 813.32] And then you can do whatever the heck you want with it.
[813.32 → 823.06] So when you, I guess this is probably getting into more typography than it is actual open source, but what are some of the tools that you use to manage the source of the fonts?
[825.24 → 828.80] There are only a couple tools, honestly.
[829.18 → 830.36] There's probably a handful.
[832.08 → 836.10] Font Forge is the only open source one, and it's awful.
[836.60 → 840.34] I mean, much respect to the people who made it, but it's ancient at this point.
[840.34 → 845.00] And I think on a Mac, you still need, like, X11 to open it.
[847.88 → 853.56] If it were me trying to recommend somebody right now doing it, I would say go look up Glyph's app.
[854.46 → 856.32] I think it's glyphsapp.com.
[856.52 → 860.88] It's a super expensive program, which, like, professional typographers think, oh, it's nothing.
[860.96 → 862.60] It's super cheap because it's, like, $300.
[862.60 → 868.98] But, I mean, professional typography is a crazy field, you know.
[872.00 → 875.96] But you can get a demo and play with it.
[877.08 → 883.64] And that is the best newest app that I have found by far is Glyph's app.
[883.84 → 884.68] Super cool.
[884.68 → 887.40] And you have a number of members.
[887.92 → 891.22] I guess you're calling them contributors, and you also have some supporting members.
[891.34 → 896.86] So I guess supporting members are people who have donated money, or what are they on this?
[897.10 → 903.82] I'm looking at the League of MovableType.com slash members, and I'm wondering what the people down at the bottom are about, the supporting members.
[903.82 → 913.98] Yeah, so contributors have always been what we called people who contributed a font, or helped contribute to a font.
[915.42 → 924.90] And just a couple of months ago when I was redesigning the site and integrating it with GitHub and all kinds of back-end technology stuff that I was excited about at the time,
[924.90 → 938.44] I figured I, like, I've been playing with a million different ideas for years on how to make money with the League without ruining the idealism and the purity of it.
[939.68 → 946.26] And I finally was just like, man, when I'm building all this back-end stuff, I should just let people donate if they want to.
[947.38 → 950.16] You know, like, it can be a completely voluntary thing.
[950.16 → 960.12] So I've decided to call them supporting members because I feel like they don't have a font that they can contribute, but they can still support us financially.
[960.42 → 962.72] So it's totally voluntary.
[963.70 → 974.68] At the moment, I would like in the future to be able to offer things that only supporting members can get, but at the moment, it's sort of just the benefit of knowing that you're helping.
[974.68 → 984.88] And so you sign up for an account, and you decide how much you want to donate, and we're using Stripe on the back-end to take credit cards.
[985.16 → 989.00] And it just kind of takes however much you want to donate every month.
[990.14 → 990.38] Pretty neat.
[990.74 → 991.34] Stripe is awesome.
[992.00 → 992.18] Yeah.
[993.02 → 993.92] Yeah, they're super cool.
[994.02 → 1000.50] I went and visited them once in Palo Alto, and they're super cool guys, and their service is unbelievable.
[1000.50 → 1004.08] You mentioned Chung 5 being one of your most popular ones.
[1004.90 → 1008.98] Do you get a thrill seeing that just spread across the web when you land on a new site?
[1009.42 → 1010.06] Yeah, totally.
[1010.48 → 1011.72] Oh, and all of them.
[1011.72 → 1027.74] Like, just the other day, Tyler, who's contributed a bunch of fonts at this point, tweeted me a link that the new swimsuit issue for Sports Illustrated,
[1027.74 → 1032.00] I'm not sure if it's in the print issue, but it's definitely in the behind-the-scenes videos.
[1032.12 → 1034.02] They used Blackout, one of the other fonts.
[1034.72 → 1035.04] Nice.
[1035.42 → 1042.00] And seeing that, like, you know, I mean, say what you will about the swimsuit issue, but it's still Sports Illustrated using one of our fonts.
[1042.06 → 1043.04] That's super flippin' cool.
[1043.04 → 1048.48] Yeah, I love just the fact that, you know, these fonts being out there and available, freely available,
[1048.60 → 1053.72] it just stepped up the design of a lot of open-source activities as well.
[1053.80 → 1059.82] I was speaking at a conference just last week, and I don't know if it speaks to how ineffective my talk was,
[1059.84 → 1063.66] but the first question I feel when I got done was, hey, what's your presentation font stack?
[1064.18 → 1064.62] Really?
[1065.10 → 1069.06] You know, League Gothic is the base font in that deck, and, you know, I shared that.
[1069.06 → 1071.00] And the other one is Hand of Sean.
[1071.96 → 1075.86] It's a handwriting font that I'm now seeing everywhere, you know, and there's just certain,
[1076.30 → 1080.44] even as a consumer of these fonts, there's a thrill there of seeing something that, you know,
[1081.38 → 1089.08] you've used and used for a while, and you've been helping to spread to see, you know, other larger outfits use that.
[1089.08 → 1092.10] I saw Hand of Sean on the side of a Hertz bus at the airport.
[1092.54 → 1092.90] Oh, really?
[1093.22 → 1093.52] You know.
[1094.40 → 1095.30] That's awesome.
[1095.66 → 1095.96] You're right.
[1096.06 → 1097.08] That's totally a thrill.
[1097.08 → 1103.98] But, like, seeing people that you respect that you don't know using it, like, you know, I don't know,
[1104.04 → 1108.68] famous designers that you follow on Twitter that would otherwise have no idea you exist,
[1109.34 → 1112.90] seeing them use a League font, I'm like, oh, that's awesome.
[1114.80 → 1116.16] What's your favourite ampersand?
[1117.20 → 1118.26] Oh, gosh.
[1118.58 → 1119.44] Oh, I don't know.
[1122.50 → 1123.74] Ditto, I think.
[1125.62 → 1126.26] Anyone's Ditto.
[1127.08 → 1128.20] I always love that font.
[1128.46 → 1129.18] Good contrast.
[1130.62 → 1135.02] Seems like Baskerville is one of the go-to in the web font stack.
[1135.12 → 1147.20] So when you're not embedding your own League fonts, what's your default font stack on the web for Serif, Sans Serif?
[1147.20 → 1150.62] Um, I don't know.
[1150.74 → 1160.92] I, I, I, for, for interface stuff, I often go with, for Dana, for, for a long time, Helvetica was, like, my branding, uh, for myself.
[1161.12 → 1162.52] And I still use that a lot.
[1163.08 → 1168.70] For, for Serif, uh, I feel like Georgia is the most readable body copy.
[1168.70 → 1172.76] Um, but I, you're right, I always love Baskerville.
[1173.32 → 1176.56] And there is an open source version of Baskerville that I love, too.
[1176.88 → 1178.12] It's called Open Baskerville.
[1178.94 → 1179.90] I've seen that out there.
[1179.90 → 1179.94] Yeah.
[1181.18 → 1182.38] So that's good stuff, too.
[1184.76 → 1192.92] So one of the projects, I don't think we've, we featured this on the blog, I haven't talked about it online, that I like, is, um, lettering JS.
[1192.92 → 1195.54] And it allows you to tweak the, the kerning.
[1195.94 → 1196.34] Yeah.
[1196.46 → 1197.38] In your headlines.
[1197.74 → 1206.48] You know what other holes do you see in, in web design technologies that, uh, we have in the print world, but we just don't have online that would help typography?
[1208.20 → 1209.22] That's a good question.
[1209.48 → 1220.80] Um, I don't, I'm, I mean, at this point, I feel like I'm, I'm so focused on web that it's, it's honestly been a long time since I even did print stuff.
[1220.80 → 1236.80] But, I mean, I mean, that kind of tight control over kerning and, uh, you know, even just like the only, the only spacing you can do between letters is like a pixel at a time with CSS.
[1237.30 → 1239.90] And sometimes that's, that looks ugly.
[1239.90 → 1244.20] Whereas you go into InDesign and, you know, you, you have such tight control.
[1244.58 → 1251.62] It, it seems ridiculous that you don't have that kind of artistic ability on the web still.
[1252.20 → 1254.80] But at the same time, it's, it's an entirely different medium.
[1254.80 → 1262.60] Like there's so many things you can do with the web that you can't do with print that, you know, I, I think it goes in both directions.
[1262.60 → 1270.60] But I think that's a great example is, is like lettering JS is sort of a hack for giving you fine control over typography.
[1271.14 → 1275.02] And I think in general, that is something that the web doesn't have is fine control.
[1276.38 → 1277.02] That's true.
[1277.02 → 1286.24] Who's got the best and the worst rendering engines as far as the browsers that you've seen and seeing the same font and how they are rendered in different operating systems and browsers.
[1286.24 → 1291.44] Yeah, that, that totally kicked my butt actually with the League of Movable Type redesign.
[1291.86 → 1297.92] Because I was trying to use some really beautiful embedded typography for the body copy.
[1298.58 → 1307.32] And I had to scrap it because, uh, Internet Explorer kicked my butt and it just, it looked awful on Internet Explorer and Windows.
[1307.76 → 1309.88] I had to change it back to Georgia.
[1309.88 → 1317.00] Um, I think if it were up to me, I, I would be WebKit all the way.
[1318.12 → 1330.02] So usually when you start a movement like this, uh, like you see on your homepage, again, we'll go back to that where you see you're joining the revolution and people are using open source technologies in so many different ways.
[1330.02 → 1341.78] I mean, everybody from Netflix to Twitter to Facebook has something in the open source world, and you've got this manifesto that kind of declares what you're standing for, but then you've also got this group of members.
[1341.90 → 1350.18] I'm just kind of curious on where the manifesto came, came from and where the members, the people that have actually contributed fonts came from.
[1350.18 → 1363.42] Well, the manifesto was, you know, like my, my first reaction to that outrage against the idea of open source typography.
[1363.42 → 1365.82] I, I, I don't know.
[1365.86 → 1373.44] I felt really passionate about Lee about that and was like, this is, this is my reasoning behind why this needs to happen.
[1374.44 → 1378.96] Um, and I haven't really changed the copy since I wrote it three years ago.
[1378.96 → 1385.36] Um, and it's, it's interesting.
[1385.46 → 1396.84] It's an interesting dichotomy because I feel like the catalogue for the league of movable type needs to be selective in order to showcase how great it could be.
[1398.02 → 1404.50] While at the same time, I want to be supportive of everyone participating.
[1404.98 → 1405.96] You know what I'm saying?
[1405.96 → 1409.88] It's a tough, uh, it's a tough line to, to trail around too.
[1409.96 → 1424.12] I mean, to be selective, but then also to be open is, uh, but then again, you, you did say that, um, that you were having trouble getting people to actually fork and contribute things back.
[1424.12 → 1438.14] Um, so maybe part of the movement forward is like you had said, doing a better job of educating on how to use GitHub or even use get technology to pull that down your computer fork and change and submit those patches.
[1438.14 → 1446.56] I think that's a that's definitely a world where topography developers and designers don't really play much.
[1446.56 → 1448.70] Yeah, absolutely.
[1448.96 → 1457.50] Like nobody, I don't know any professional photographers that even consider a collaborative font feasible.
[1457.78 → 1457.98] Yeah.
[1458.06 → 1459.08] And I think that's ridiculous.
[1459.08 → 1461.22] And I think it honestly goes on both sides.
[1461.36 → 1475.08] Like I want the future of the league to be education for the people who are already great typographers or, I mean, I don't, I don't care if you're great type, if your focus is typography, I want to educate you on how to use the technology.
[1475.08 → 1476.54] So that's not a barrier for you.
[1476.64 → 1486.44] And on the other side, I want, you know, regular developers, people who use GitHub all the time to feel confident enough to start messing around with designing fonts.
[1486.56 → 1487.12] They could.
[1487.40 → 1490.80] And I totally believe that anybody could go either way.
[1490.88 → 1493.70] And so I kind of want to educate both sides of that.
[1494.40 → 1497.92] So the contributors that are a part of the league now, how do they come about?
[1500.36 → 1503.10] A couple of them were people that we knew.
[1503.10 → 1506.90] I mean, we started with Caroline's font that she did in college.
[1507.30 → 1530.78] And then after that, I think the next one was someone named Haley that we, Haley Fig that we did not know had seen it and had already been giving away one of her fonts for free, Singlet, which is still one of my favourite ones in our catalogue.
[1533.10 → 1537.44] She had already been giving it away for free and was like, hey, I really like what you guys are talking about.
[1537.88 → 1540.28] How about I contribute this font?
[1541.02 → 1542.10] And so we put it on there.
[1542.66 → 1547.08] And from there, we, the next one, you know, so that was a stranger.
[1547.08 → 1551.24] That was someone who had contacted us saying, I totally like what you guys are doing.
[1551.24 → 1556.54] The next one was someone that Caroline and I had gone to school with in Los Angeles.
[1558.30 → 1562.00] A bunch of people that we went to school with took a type design class.
[1562.22 → 1567.20] So there were a handful of fonts in our graduating class that were not being used.
[1567.20 → 1569.62] And we contacted a bunch of those people.
[1569.94 → 1575.34] And one of the people who came back was Meredith Mandel, who made Chunk.
[1576.46 → 1579.86] And she was kind of just like, yeah, sure, why not?
[1579.88 → 1580.98] I think that's cool, I guess.
[1581.70 → 1587.16] And I think to this day, she has no idea how famous she is because she's not really in the web world.
[1587.16 → 1589.02] She's sort of a regular designer.
[1589.02 → 1594.94] And I think she has no idea how much people love and use her font.
[1595.26 → 1599.82] What's the motivation, I guess, for like you said, you know, she's a regular designer, for lack of better terms,
[1599.92 → 1602.78] to say that maybe she doesn't really have a presence on the web.
[1602.92 → 1608.68] But what is the motivation for a designer, a type designer, to get involved with the League of the Mobile Type?
[1608.68 → 1614.06] Is it just because they care about just the movement of the craft?
[1614.20 → 1617.38] I mean, what's some of the reasons why you would think that they would join the League?
[1617.38 → 1620.48] Ideally, exactly that.
[1620.56 → 1622.04] And originally, I think that's what it was.
[1622.14 → 1628.38] I think Haley and Meredith and the next one that we had was Tyler.
[1628.84 → 1631.60] Actually, honestly, I feel like everybody that has contributed.
[1632.88 → 1634.52] The next one was Barry Schwartz.
[1635.30 → 1644.84] I think all of them do really believe that, hey, I want to do some good and like contribute this thing for the good of the design community and give back.
[1644.84 → 1650.36] And I love that all the people that we have involved, you know, have that in their heart to be mushy.
[1652.26 → 1656.90] But at this point, there are other benefits, too, because we have tons of people who know about the League.
[1657.00 → 1659.10] We get tons of people visiting every month.
[1659.10 → 1663.70] And there's a certain exposure that comes from that.
[1663.70 → 1674.58] I think at this point, any new font that we launch and give away will immediately become, I don't know, viewed.
[1674.92 → 1676.56] Like lots of eyes will be on that.
[1676.88 → 1680.82] And that is some incentive at this point to do that, I think.
[1680.82 → 1683.24] So let's spin the focus more towards you.
[1683.32 → 1684.20] We've talked about Caroline.
[1684.32 → 1686.58] We've talked about Meredith and their contribution to the League.
[1687.58 → 1691.48] And as one had mentioned earlier, his brand is built around League Gothic.
[1691.64 → 1694.24] And you are the author, the contributor of League Gothic.
[1694.42 → 1699.38] So when we look at your role and who you are to the League, you're the founder.
[1699.60 → 1702.28] But what other roles do you play for the League?
[1702.28 → 1717.48] I have always been the I don't know, with the League, with a good company, you know, the actual business that I run, I feel like I've always sort of played the part of stage manager.
[1718.44 → 1724.76] Like, I contributed to League Gothic, but I certainly didn't make the thing.
[1724.90 → 1728.12] Caroline did almost, you know, like so much of the work on that.
[1728.12 → 1734.80] And I, for that particularly, I came up with the idea.
[1734.96 → 1743.76] I was like, hey, we should, you know, revive an old font that, you know, people have kind of forgotten about that we could contribute to the open.
[1743.88 → 1744.86] We should revive it.
[1744.86 → 1759.02] And I went through, and I picked out, I got this giant, like hefty specimen, type specimen book of fonts that were allowed to be, you know, redone.
[1759.48 → 1761.72] I mean, that's sort of a complicated issue.
[1761.88 → 1765.32] You can kind of make any font your own.
[1765.60 → 1771.08] You know, you could print off someone's font and redraw it yourself and call that your own.
[1771.08 → 1775.66] But these at least were sort of public domain at this point.
[1776.26 → 1778.78] Yeah, it says on the page there, the company went bankrupt.
[1779.12 → 1783.26] And since it was older than, what, 1923, it was in the public domain?
[1784.44 → 1784.80] Right.
[1784.96 → 1786.04] I forget the actual year.
[1786.16 → 1787.70] If it says it, I believe you.
[1788.70 → 1789.52] I won't lie.
[1791.30 → 1793.66] No, but that was it.
[1793.66 → 1798.18] I think it was a company called ATF that had drawn a bunch of fonts and then went bankrupt.
[1798.78 → 1804.16] And you, anybody right now could go look up a font specimen.
[1804.44 → 1808.30] A lot of people have scanned really high quality versions on the Internet.
[1808.84 → 1811.60] And you could trace that and make a font.
[1812.24 → 1814.26] And you could sell it if you want to.
[1814.72 → 1816.94] I mean, I'm here to promote, hey, you should make it open source.
[1816.94 → 1825.78] But that's perfectly legal just because of the weirdness of copyrights with fonts, which is probably a whole other tangent.
[1826.76 → 1831.28] But in terms of what I do, I feel like I've always been a stage manager.
[1831.54 → 1833.98] Like, I knew how to use the technology.
[1835.42 → 1842.04] You know, I knew how to build the sites and the services that we want to do because I'm sort of half programmer for all of these things.
[1842.04 → 1849.04] And I was an evangelist, like, going out trying to talk to people and get them excited.
[1849.84 → 1858.30] And, you know, use my unending charm to try to convince them that this is a good cause.
[1859.18 → 1866.34] And so I was always sort of playing a bunch of different roles of actually building stuff and being a programmer.
[1866.34 → 1873.20] And then going out and, you know, doing interviews to try to get people up and, like, writing.
[1873.28 → 1881.06] I wrote an article for .NET Magazine at one point sort of saying, this is the cause and this is why you guys should stand up and be with us here.
[1882.52 → 1888.42] So in that way, I'm, you know, like, I'm definitely not a typographer.
[1889.16 → 1890.10] And I can help.
[1890.10 → 1894.18] I can contribute to people, you know, like League Gothic.
[1894.40 → 1896.34] I contributed some of the drawing to that.
[1897.14 → 1901.20] But for the most part, I do all the behind-the-scenes stuff like that.
[1901.48 → 1910.58] You had mentioned going back and being able to redraw, you know, a high-scaled specimen and being able to resell it.
[1910.62 → 1913.70] But you had said, you know, you would encourage them to do it open source.
[1913.70 → 1920.80] Is there a way that someone could be a contributor to the League but also still be able to make money from their work?
[1920.94 → 1926.40] Or is there a way that the League is able to find other ways to make money besides just saying, hey, it's open source.
[1926.48 → 1927.38] You can't make money from it.
[1927.44 → 1940.22] Because on this show, we've seen lots of technologies come by that have been open source but have found ways through GPL licensing or certain licensing to still be able to spend their work another way with certain restrictions.
[1940.22 → 1946.38] But still be able to make money from it but at the same time push the movement of open source, you know?
[1947.58 → 1947.98] Yeah.
[1948.22 → 1952.50] And that's – well, that's something I've always been really fascinated with and tried to research more.
[1954.44 → 1956.92] Because I, you know, I hate money.
[1957.04 → 1958.02] I'm not perfect with money.
[1959.32 → 1960.86] I make it because I have to.
[1961.04 → 1964.48] But, like, other than that, I don't – you know, I'm not perfect with it.
[1964.48 → 1973.58] So the answer to that, I think, is that there are other interesting ways that we're sort of experimenting with here.
[1973.58 → 1986.78] So the Open Font License, which is – you know, it's an open license specifically designed for fonts, similar to all the other open licenses that people use.
[1986.78 → 2000.98] It actually describes in there that the author of the font – my understanding, at least, is that the author of the font can both give it away and sell it if they want to.
[2001.42 → 2002.98] Because they made it.
[2002.98 → 2023.56] And one of the things at the moment that I'm working with sort of confidentially, privately with some people is taking the open source version and helping the author expand it to something that is specific for what a company would need.
[2023.56 → 2035.06] So it's sort of like in between making a custom font and giving the open source font away for free so that the open font is sort of a basis.
[2035.46 → 2044.36] And then there's custom work on top of it that is more in line with what professional typographers do as their day job.
[2044.64 → 2045.06] You know what I mean?
[2046.28 → 2052.98] Which I think is really awesome and an interesting path that I'm kind of just starting to explore.
[2053.56 → 2056.98] Any plans to include any glyph fonts on the league?
[2058.30 → 2059.56] Not at the moment, though.
[2059.74 → 2061.40] You know, I'd totally be open to it.
[2062.84 → 2070.90] There's an interesting debate going around at the moment on whether that's semantically acceptable to use glyph fonts on the web.
[2072.32 → 2075.16] And, you know, I'm not even sure that I have an opinion about that.
[2075.24 → 2076.08] I'm not sure if it matters.
[2076.08 → 2081.60] But, you know, the answer is that I would totally be open to it.
[2081.68 → 2084.40] But nothing is on the horizon at the moment.
[2085.68 → 2090.08] And in fact, honestly, the only thing that I think is on the horizon is something that...
[2090.08 → 2093.52] It's similar to League Gothic.
[2093.72 → 2097.46] Caroline and I started a font a while ago.
[2097.46 → 2099.48] Probably the beginning of last summer.
[2100.60 → 2104.70] That has kind of been slowly evolving.
[2104.98 → 2110.64] Of sort of reviving an old font that people kind of forgot existed.
[2110.64 → 2117.44] And other than that, you know, I know Tyler is kind of always working on stuff.
[2119.92 → 2121.48] And the rest I'm not really sure about.
[2122.48 → 2133.10] Not to have you give anything away that you're not ready to disclose yet, but any classical faces that you'd like to see freely available that aren't yet?
[2133.10 → 2136.40] Man, I can't wait until we can do Future.
[2137.02 → 2138.10] A version of Future.
[2138.30 → 2139.46] I think that would be fantastic.
[2139.74 → 2141.02] I think people would eat that up.
[2141.64 → 2144.96] But at the moment, we can't really do that.
[2145.10 → 2146.44] It's still copyrighted.
[2146.74 → 2148.32] I'm actually a huge fan of Future.
[2148.38 → 2150.32] I love the many ways they have.
[2150.40 → 2151.24] The thick to the thin.
[2151.44 → 2158.98] It's one of those fonts that just work across the board for pretty much any kind of work you're trying to do, too.
[2160.12 → 2160.50] Yeah.
[2160.50 → 2167.88] And that actually brings up another interesting point in that, you know, we get criticism sometimes.
[2168.22 → 2179.16] I think people forget that it's an open source font foundry sometimes and just consider it a regular font foundry and say, man, so many of the fonts have, like, one weight.
[2180.10 → 2182.40] And I have to be like, yeah, I know it sucks.
[2183.14 → 2185.92] But, hey, why don't you help?
[2185.92 → 2192.72] Like, you know, you could make another weight and contribute back on GitHub, and we could totally have that be the official version.
[2192.72 → 2208.38] And that's something that I would love to do soon in the future is, like, unveil, you know, a family that has, that is a family that has, you know, everything that you would need.
[2208.40 → 2212.26] You know, the different weights and obliques and that would be nice.
[2212.26 → 2227.66] So I guess one way you could probably do that, though, is just anybody who's out there that's, you know, more on the design side of a font face or typography could just reach out to you and kind of, you said you're the kind of the guider, right?
[2227.66 → 2237.82] You guide them into what some of the technology is, maybe a couple blog posts on how to easily work with Git or even using the Mac app, I guess, would be one way to do it, too.
[2237.82 → 2239.62] Yeah, yeah, absolutely.
[2240.04 → 2250.54] And I would love to, you know, if there's somebody out there right now that's listening that, you know, has kind of been like, man, I would love to, but I don't know all the tech behind it.
[2252.22 → 2254.62] I'm an excellent teacher and would love to do that kind of stuff.
[2254.62 → 2267.70] And what you're talking about is exactly a plan that I have for this year, hopefully, to, I don't know, like make an online manual that describes how you could use Git, like in the most basic way so that it's not overwhelming.
[2268.48 → 2281.70] And maybe how you could use one or two of the available font editors and combine it all into sort of manual on from start to finish, this is how you would draw a font.
[2281.70 → 2287.54] And GitHub does have the Git for designers series out there, don't they?
[2288.24 → 2298.34] I remember seeing that at some point and I thought that was sort of a good, you know, inspiration, I guess, like similar kind of thing that I would like to do.
[2299.80 → 2301.08] Except it's a little more specific.
[2301.08 → 2305.98] There's a whole other world of talent out there that's just not in our circles.
[2306.10 → 2308.24] We would love to assimilate those folks.
[2309.04 → 2309.24] Yeah.
[2309.66 → 2325.34] Like all the people I know of that are not even hardcore programmers, just, you know, half-core programmers that know of things like Git or, you know, even just the command line, just not being afraid of the command line.
[2325.34 → 2329.70] And all of those people would be like, man, I wish all these designers could use this.
[2329.78 → 2330.72] And I know that they can.
[2330.72 → 2337.38] It's just some, you know, mental blocking that designers seem to think, ah, that's too complicated.
[2337.52 → 2339.02] I don't want to figure that out.
[2339.08 → 2339.82] When really it's not.
[2340.76 → 2346.30] What's the degree of difficulty between a good headline font and a good body font?
[2346.30 → 2354.86] Because I'm thinking with body, you need, like you mentioned, multiple faces for emphasis and also, you know, multiple styles for obliques.
[2355.02 → 2361.26] So what's, how hard is it to execute a good headline font versus just a durable body font?
[2363.28 → 2365.24] Well, I'm not sure.
[2365.32 → 2372.56] I mean, I think a lot of people would say that headline fonts are easier because they're less subtle, I guess.
[2372.60 → 2374.64] Like you can be crazy with a headline font.
[2374.64 → 2381.86] You can make some, you know, super insane looking thing that you would never be able to read if it were body copy.
[2383.68 → 2390.34] But at the same time, there's, there's sort of more guidelines that you can use for body copy.
[2390.46 → 2392.04] So it's really not that much more difficult.
[2392.48 → 2400.24] And, and honestly, you don't, I mean, it's nice to have all of those styles, but you don't always need them.
[2400.24 → 2405.24] And that should not be a barrier, I think, to someone who's interested in making a body font.
[2406.18 → 2413.66] Don't get overwhelmed by the idea that you need, you know, four or six or eight different styles and weights.
[2413.90 → 2417.78] You don't, you can just start with regular and build it up over time.
[2417.78 → 2418.20] You know?
[2418.20 → 2425.12] Do you kind of wince when you see a font without a heavier face having the faux bold in the browser?
[2426.40 → 2427.06] Faux bold.
[2427.22 → 2427.36] Yeah.
[2427.36 → 2438.24] Faux sometimes bothers me a little bit, especially like I did a client project recently with, with a good company where, uh, they didn't, they, they didn't really have a logo.
[2438.38 → 2438.86] Exactly.
[2438.86 → 2442.14] It was sort of based on something that another designer had done with CSS.
[2442.14 → 2447.02] And it was already a bold face that that designer didn't know what they were doing.
[2447.02 → 2450.90] And they had done faux bold with CSS and I kind of had to mimic it.
[2451.00 → 2452.66] And it was painful.
[2453.80 → 2458.32] How much effort do you put into vertical rhythm when you're doing web layouts?
[2459.54 → 2460.82] That is a good question.
[2460.82 → 2467.60] Um, I pay a lot of attention to it, but I'm also not very strict.
[2467.60 → 2479.26] I feel like a lot of the design, the way that I do it is sort of go with the flow design where there are a couple rules and guidelines that you follow, and the rest is sort of make it up as you go along.
[2479.60 → 2481.42] But I think it's absolutely important.
[2481.42 → 2493.58] Like there's, there are not many things that will as drastically improve a design as having the right vertical rhythm.
[2493.58 → 2505.44] Any type treatments that you want to do on the web that currently can't with CSS that you find yourself breaking down and creating images?
[2507.12 → 2507.60] Huh.
[2508.04 → 2514.20] Um, shadow treatments and multiple shadow treatments and things that where you just couldn't get the effect with pure CSS.
[2515.50 → 2516.24] I don't know.
[2516.30 → 2519.96] I mean, that's honestly been getting so much better over just even the last couple of months.
[2519.96 → 2528.92] It's like, I feel like now it's, it's much more acceptable to use like multiple, uh, box shadows and tech shadows and stuff like that.
[2529.04 → 2535.24] And you can get some pretty awesome looking, looking stuff with just CSS.
[2535.24 → 2543.62] Like actually around the time that I was redesigning the league, I was, I was working on a side project for myself called Iconic.
[2543.62 → 2547.54] Um, which, you know, went nowhere.
[2547.70 → 2554.76] It's, it, it doesn't even matter what it was, but like I had designed this, uh, really detailed text treatment.
[2554.76 → 2560.00] It was like really dark and, and sort of cosmic and, and really cool looking in Photoshop.
[2560.36 → 2564.50] And I was about to splice it up and use it on, on the site.
[2564.50 → 2566.32] And I was like, wait a minute, you know what?
[2566.34 → 2568.00] I, I think I could actually do this.
[2568.00 → 2578.18] And it, it ended up with like all of these extra little box shadows and like highlights and stuff that I ended up being able to do with all the new CSS three shadow stuff.
[2579.04 → 2584.46] And, uh, you know, it's, it's kind of amazing how far it's come in just like the last year.
[2585.80 → 2586.76] It's kind of awesome.
[2586.76 → 2594.34] And speaking of, uh, what's happening in the future and stuff like that, I happen to be one of your followers on Dribbble.
[2594.62 → 2600.30] And I see recently you've been dribbling some stuff on this thing called Letter case.
[2600.30 → 2612.72] And if you've, uh, if you've been listening, and you've been following along, and you've gone to the league's website and have been kind of poking around, you'll see, uh, I think it's add this to, yeah, add to Letter case.
[2612.72 → 2616.44] And it just takes you right to lettercaseapp.com.
[2616.52 → 2618.84] I guess unless you're logged in, it probably does something a little different.
[2619.06 → 2620.22] So what's, what's the play here?
[2620.30 → 2626.90] This is something outside this open source project, but it's kind of together.
[2627.10 → 2627.94] What is Letter case?
[2629.08 → 2629.94] Well, all right.
[2629.94 → 2640.56] So Letter case originally came about as a way to try to make money without ruining what the league's ideals were.
[2640.56 → 2649.64] Um, you know, there was a big audience of, of designers who were really into the typography that came along with the league.
[2649.64 → 2659.28] And I was like, I don't have an idea at the moment of how to make money other than like advertising or something, which originally I really didn't want to do.
[2659.86 → 2668.02] Um, and I was trying to find something kind of where the same audience would find something useful, uh, that they'd be willing to pay for.
[2668.02 → 2675.54] And one of the thorns in everyone's side is font management.
[2676.54 → 2686.64] You know, for, for every hundred designers, there are 80 different ways that people manage their fonts because nobody's made tools that are good.
[2686.64 → 2690.20] Um, well, I mean, that's a little harsh.
[2690.20 → 2702.72] Like there's a couple of really decent tools, uh, that, that to me just are not where we should be with that because I think nobody wants to work on it.
[2703.00 → 2704.96] It's just not something that's on people's radar.
[2704.96 → 2705.56] You know?
[2705.68 → 2710.34] Well, it's a shame though, because, you know, if I'm going to mention a name, I spent a hundred bucks on an app.
[2710.34 → 2715.10] It's called font Explorer X pro, and it does it's, yeah, I actually bought that.
[2715.24 → 2715.52] Interesting.
[2715.92 → 2717.50] It does its job.
[2717.74 → 2726.48] I only bought it because everything else sucked, and I wanted to at least buy something that was worthwhile that if I bought it, and it had some support, then it'd be okay.
[2726.48 → 2738.74] So to this day, I still have yet to get any support from them, and I've not had any issues with it, but at the same time, it doesn't really help me use my type any better than just selecting it myself.
[2738.84 → 2745.18] Like there's nothing that helps me examine specimens of different families and look at different kerning and all these different things.
[2745.22 → 2752.42] So is this like the, the path that letter cases is heading down or is it just going to be the, the tagline that it says it's a bit more minimalist and font management?
[2752.42 → 2757.48] It's definitely going to be minimalist, but that's, that's me.
[2757.60 → 2759.46] That's, that's how I make stuff.
[2759.62 → 2766.90] And that's, I have sort of a unique idea for a way that people can find fonts that, that nobody's really tried yet.
[2767.06 → 2773.76] But I think the reason that I feel like it'll actually work is because I want it to be a whole service.
[2773.76 → 2787.96] Like I, like more like a platform where like the way that it works is that there's a little Dropbox style application that runs in your menu bar that sort of syncs your folder with letter cases database online.
[2787.96 → 2808.14] And once I get my version of the tool built, you know, there's going to be an API so that someone else can do other crazy stuff differently, which I think will all of a sudden make any kind of font management tool that you can imagine.
[2808.14 → 2828.94] But the, you know, the, the way that I think mine will be different, I've been very inspired by Dribbble, you know, it's, they kind of came out of nowhere, but I often use Dribbble as a way to gather inspiration when I don't know how I want something to look.
[2829.04 → 2829.30] Right.
[2829.34 → 2830.52] I think a lot of people do that.
[2832.48 → 2837.84] I wish I was a bit more like Pinterest, I guess for designers, but there's some Pinterest like qualities.
[2837.84 → 2843.34] You didn't mention that, but it made me think of just like organizing different thoughts and seeing things side by side and stuff like that.
[2843.40 → 2845.96] You kind of get a chance to do that with something like Pinterest.
[2846.14 → 2851.20] I think that's kind of something that Dribbble has allowed you to do by cavorting or whatnot.
[2851.64 → 2853.48] And it's, it's kind of neat.
[2854.16 → 2854.28] Right.
[2854.42 → 2855.00] I agree.
[2855.08 → 2861.78] Like it's, it's interesting how you can take that simple idea and kind of mould it into a bunch of different tools.
[2861.78 → 2872.50] And I, I kind of think one of the ways that you, we sort of mentioned this earlier with the league that, uh, one of the reasons that, uh, I don't know.
[2872.56 → 2880.52] Well, not one of the reasons, but one of the defining factors are those, those type specimens of the fonts actually being used somehow.
[2880.52 → 2881.12] Right.
[2881.32 → 2893.06] When mentioned that he liked how you guys actually use real world cases of your, your type actually out there in the wild versus just specimens that, you know, are just black and white and common, I guess.
[2893.26 → 2893.58] Right.
[2893.64 → 2897.04] And that's kind of where my brain is at with, with letter case.
[2897.04 → 2914.18] I think the most interesting part of what I'm building with letter case right now is that I, I want to attach images of, of stuff that you were actually using the fonts with so that, and, and sort of like you, let's say you have, uh, Gotham, right.
[2914.20 → 2920.26] And I have Gotham and you know, we don't really know each other, whatever you build some site.
[2920.26 → 2931.42] Well, you can't build a site with Gotham, but you know, you, you design something with Gotham and you upload an image of what you are designing with Gotham and attach it to the Gotham family that you have in your letter case.
[2932.04 → 2949.98] And, um, when I have Gotham and I go on my letter case, um, it'll show me other people like you, what, what you have done with Gotham so that I can kind of look through this visual database of what other good designers have done with the same stuff.
[2949.98 → 2954.90] I have to try to inspire me to use what I have differently, you know?
[2955.86 → 2956.22] Right.
[2957.40 → 2963.22] So when you talk about a letter case, then I guess, since we're talking about open source, that's what the change law is about.
[2963.84 → 2967.82] Um, you know, what kind of open source technologies are you using to actually make letter case?
[2968.48 → 2972.98] Oh, pretty much, pretty much all, uh, open source technologies.
[2973.92 → 2976.50] I mean, it's running on Sinatra, which I love.
[2977.26 → 2979.92] Um, it's got,
[2979.98 → 2998.14] there's, there's, there's sort of an old, well, there's two open source libraries that I'm using to extract information from the fonts themselves, which is a surprisingly, uh, I don't know, unexplored, uh,
[2998.56 → 3000.34] a thing.
[3000.34 → 3008.74] I don't know that, that there hasn't been a lot of technology around extracting information from fonts because fonts are actually really complicated on the inside.
[3008.74 → 3015.90] Um, but there are two libraries that have been helping me to extract that information.
[3016.28 → 3019.66] There's actually to build the API, I'm using something called grape.
[3019.74 → 3020.94] If you guys are familiar with grape.
[3021.34 → 3021.78] Yeah.
[3022.44 → 3022.88] Right.
[3023.02 → 3023.26] Yeah.
[3023.60 → 3024.28] Grape is awesome.
[3024.44 → 3025.04] I love grape.
[3025.04 → 3033.00] Um, and warden for, you know, just basic user stuff.
[3033.00 → 3050.96] Like it's, it's basically more a collection of other open source stuff doing what I wanted to do than it is me inventing stuff, which is, I, you know, that's, that's exactly why I feel like open source is amazing is because it, it lets somebody who, you know, I started out not knowing how to program.
[3050.96 → 3057.32] And by using stuff that people had given away for free and shown me how they made it, I learned how to do it too.
[3057.50 → 3064.34] And that's exactly why I think, uh, typography should have the same, I don't know, channel.
[3065.92 → 3074.28] So we normally close out the show by asking you your programming hero, but, uh, given your background, I'll ask you either programming or design hero.
[3074.28 → 3076.38] Oh, goodness.
[3077.98 → 3082.14] Um, that one's, that one's tough to answer.
[3082.62 → 3086.10] Uh, does that have to be open source related?
[3086.58 → 3087.34] No, not at all.
[3087.76 → 3088.20] All right.
[3088.26 → 3093.42] Well, if we're talking about just design and not a perspective or mentality.
[3093.42 → 3101.82] So take that with a grain of salt, I would have to say that, uh, Löffler and Fur Jones make some amazing, beautiful typography.
[3104.02 → 3107.92] That's about it, but they do, they are very good at that.
[3109.84 → 3112.36] Certainly been fun for us to chat with you.
[3112.42 → 3120.56] We've been using fonts from the league for some time now, and hopefully we've turned some other folks on to how to spruce up their web typography.
[3120.56 → 3122.34] So thanks, Micah, for joining us.
[3122.70 → 3123.50] Hey, thanks for having me.
[3123.54 → 3124.02] This was fun.
[3124.38 → 3125.00] It was a lot of fun.
[3125.10 → 3125.78] Thanks for coming on the show.
[3126.10 → 3126.32] Yeah.
[3126.32 → 3126.38] Yeah.
[3126.38 → 3144.76] See it in my eyes.
[3144.76 → 3154.18] So how could I forget when I found myself for the first time?
[3154.18 → 3157.88] Safe in your arms.
[3157.88 → 3160.02] As a dark fashion.
[3160.02 → 3165.58] This is a dark fashion.
[3165.58 → 3168.58] Do not bring more mad.
[3186.70 → 3187.44] I thought this is not funny.
