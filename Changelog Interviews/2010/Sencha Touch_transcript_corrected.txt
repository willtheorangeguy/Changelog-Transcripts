[0.00 → 18.66] Welcome to the Changelog episode 0.3.0.
[18.82 → 19.86] I'm Adam Stachowiak.
[20.06 → 20.88] And I'm Wend Sutherland.
[21.08 → 21.98] This is the Changelog.
[22.04 → 23.92] We cover what's fresh and new in the world of open source.
[24.32 → 27.36] If you found us on iTunes, we're also on the web at thechangelog.com.
[27.36 → 30.28] And we're also on GitHub.com forward slash explore.
[30.52 → 35.34] You'll find some training repos, some feature repos from our blog, as well as the audio podcasts.
[35.74 → 38.68] If you're on Twitter, follow ChangeLog Show, not the Changelog.
[39.08 → 39.96] And I'm Adam Stack.
[40.24 → 42.78] And I'm Penguin, P-E-N-G-W-Y-N-N.
[43.10 → 44.72] Set down this week with David Canada.
[45.10 → 47.04] Yeah, he's got quite the resume I see here.
[47.20 → 51.80] Yeah, Centra Mobile, WebKit Bits, which I find myself reading all the time.
[51.92 → 54.46] And before that, JR Touch, which I think you've played with.
[55.02 → 56.18] That's a popular one there.
[56.42 → 57.24] Yeah, it is.
[57.36 → 63.40] It's probably the bleeding edge of web development with the WebKit browsers on the mobile devices.
[63.72 → 63.92] Yeah.
[64.22 → 67.60] I was pretty excited to hear that they were playing with SaaS in this.
[67.94 → 69.70] Yeah, we're big Compass and SaaS fans.
[69.80 → 76.90] If you've caught any episodes of the Changelog, you know, we're users and fans of Compass and SaaS.
[76.98 → 83.62] And they're using it in kind of unique way to do their theming with all of their buttons and controls and pickers and things of that sort.
[83.62 → 87.60] They're using a lot of variables and mix-ins and things like that.
[87.60 → 87.64] Yeah.
[87.96 → 89.70] So what's cool about Centra Touch?
[90.14 → 93.40] Centra Touch lets you build web interfaces for mobile devices.
[93.76 → 96.12] You know, HTML5's all the buzz right now.
[96.20 → 100.90] But it's a way to do it without having to learn the native platforms, either Android or iOS.
[100.90 → 100.98] Yes.
[101.38 → 101.86] Very cool.
[101.98 → 103.66] And I guess this is what episode 30, right?
[103.68 → 105.82] So that's 30 episodes for the Changelog.
[106.00 → 108.88] 30 episodes and all roads lead to SaaS, right?
[109.58 → 110.22] Yeah, right.
[110.26 → 111.82] Episode 1 and episode 30.
[112.14 → 117.88] And we're going to have those guys on soon to talk about a lot of the developments that have happened with Compass and SaaS since we last talked to them.
[117.88 → 120.24] That world is moving so quickly.
[120.50 → 121.24] I can't even take it.
[121.32 → 122.44] It's hard to keep up with.
[122.82 → 124.00] Yeah, but open source moves fast.
[124.40 → 124.94] Keep up.
[125.40 → 125.72] All right.
[125.78 → 126.62] Let's get to this episode.
[126.84 → 127.46] Let's do it.
[136.42 → 136.88] All right.
[136.90 → 138.96] We're joined today by David Canada from Cynthia.
[139.32 → 142.70] We're going to talk about Cynthia Mobile and some of the open source projects they have over there.
[142.78 → 145.82] David, why don't you introduce yourself and just let the folks know who you are and kind of what you do.
[146.40 → 146.76] Sure.
[146.76 → 147.96] My name is David Canada.
[149.10 → 153.62] Before coming to Cynthia, I ran a few open source projects including JR Touch.
[154.34 → 158.00] I also run a blog called WebKit Bits, which is about WebKit.
[159.84 → 164.46] And before that, I've sort of always worked within the design development industry.
[165.34 → 167.92] So JR Touch, popular iPhone project.
[168.06 → 169.66] Tell me a little bit about how that came about.
[170.14 → 170.62] Sure.
[170.78 → 176.30] So I did my first iPhone app about a year and a half, two years ago.
[176.30 → 177.60] That was called Outpost.
[177.70 → 178.80] It was for Basecamp.
[179.94 → 184.16] That was a fully native app, which I did with a developer friend, Jim W.
[184.16 → 194.04] And so as we put that out, I started to want to look into doing another app, probably for Backpack at the time.
[194.04 → 201.08] But really wanted a little more hands-on experience with the development of it.
[201.08 → 218.46] And so after trying to learn Objective-C for a couple of days and just not being too interested in the language and then sort of at the same time, I just coincidentally was looking into the capabilities of WebKit and Safari on the iPhone.
[218.46 → 221.46] And I started to see what was possible there.
[221.46 → 229.96] And there wasn't much in that arena that really covered that sort of native-feeling web app.
[231.06 → 239.82] For those that don't know, JR Touch is, I guess, a fair comparison might be a more polished, jQuery-centric GUI.
[239.82 → 245.22] Yeah, I don't want to compare too directly to GUI.
[245.34 → 246.68] I think, you know, those guys were great.
[246.92 → 252.08] And especially, you know, Joe kicking that project off was a great idea.
[252.42 → 262.46] I think the big thing that JR Touch sort of brought to the table when we came out was, you know, the use of hardware accelerated animations was a big deal.
[262.68 → 266.66] Adding a lot more animations in terms of 3D and flips and things.
[266.66 → 280.76] And then we also just, by using jQuery, made it a lot more extendable by using sort of jQuery's event syntax and adding a lot of custom callbacks that GUI didn't really have at the time.
[281.02 → 283.70] So now you're part of the Cents team.
[284.04 → 289.58] Give a little background about Cents and its roots in XJS and what it aims to solve.
[290.52 → 291.04] Absolutely.
[291.72 → 296.40] So I came into XJS, which is now Cents, in December.
[296.66 → 301.46] Before that, I had heard about XJS sort of in passing.
[301.66 → 309.02] I haven't done a ton of work in sort of rich Internet apps like XJS does for the desktop.
[309.02 → 321.26] So their goal back then was basically to create the richest, most powerful JavaScript framework for mobile, as they've done for the desktop.
[321.26 → 334.76] And JR Touch certainly had some elements of that, but was not the, you know, sort of application programming structure that some developers needed.
[334.76 → 339.22] So when I came in, I came in as creative director.
[339.22 → 351.50] And my role in the company has pretty much been split between the development side and sort of taking everything I've learned in JR Touch and help bring it to Cents Touch.
[351.76 → 355.26] And I definitely can't take credit for Cents Touch alone.
[355.42 → 361.30] We've had, particularly Tommy Minds has been sort of the JavaScript mastermind behind it.
[361.30 → 363.56] And we've had a lot of developers helping out with it.
[363.68 → 365.52] And I really think it shows.
[365.52 → 375.82] But my time has pretty much been split between that and then also doing the sort of marketing and branding side of Cents, which, you know, including the rename and redesign.
[376.30 → 379.70] And some upcoming design projects will be launching soon.
[380.84 → 382.00] Looks fantastic.
[382.18 → 386.84] Now, Cents targets not only iPhone and iOS, but also Android as well?
[387.56 → 388.48] Yep, absolutely.
[388.48 → 395.72] And so what are the what are some of the challenges of hitting both of those platforms in one framework?
[397.36 → 406.40] Okay, so for those who don't know, both the iPhone and Android are based on WebKit, which is a browsing engine that's also in Safari and Chrome.
[407.20 → 411.62] As PPK has noted in the past, there are a million different versions of WebKit.
[411.62 → 421.34] And so it was, to make it work on both platforms was actually a good deal harder than we thought it might be initially.
[422.02 → 429.62] There's a fair amount of operating system sort of interference with some of the elements on pages.
[429.62 → 440.58] For example, form inputs like text input and text areas are basically always controlled by the operating system when implementing WebKit.
[440.90 → 445.32] And so they can respond very differently to events or things like that.
[445.96 → 453.60] And then just general challenges in terms of screen resolution, especially with the number of devices that Android is on.
[453.60 → 457.90] And, you know, some minor differences in their WebKit versions.
[458.90 → 460.30] You know, talk about that for a moment.
[460.54 → 466.72] You know, I guess the main difference right now between Android development and iPhone development,
[466.72 → 470.88] I think a lot of folks are making the comparison between Mac and Windows back in the day,
[470.96 → 474.84] where on the Windows side it was, you know, they didn't control the hardware.
[475.02 → 477.00] They only provided the software.
[477.16 → 478.18] It's much the same model.
[478.18 → 481.02] Now, on Android, you've got multiple flavours out there.
[481.52 → 483.56] And it seems like they're reproducing all the time.
[484.00 → 485.80] What challenges have you seen in supporting?
[486.22 → 489.36] And I guess how far back do you support in that stack?
[490.24 → 490.44] Yeah.
[490.74 → 494.24] So publicly we're saying basically 2.0.
[495.48 → 499.66] Internally we obviously highly prefer a 2.2 or a Promo.
[501.16 → 506.36] It just has done wonders for them in terms of their JavaScript processing.
[506.36 → 516.74] I think the iPhone has always had a small advantage in regard to animations from having core animation built into the OS.
[517.26 → 523.50] So even in Safari, when it's doing a hardware accelerated animation,
[524.22 → 530.06] it's using the operating system level frameworks to accomplish it.
[530.22 → 533.00] And I think it shows in the smoothness of the animations.
[533.00 → 541.74] So in that way, I think Android still – I love Android, and every time Android releases a new version,
[541.88 → 543.86] I want to think, like, this is the one.
[544.00 → 545.44] This is going to be it.
[545.44 → 551.60] But just personally, I've always found iOS has offered a far superior experience.
[552.26 → 560.80] You know, one of the things that attracted me to India when I first saw it was the fact that it was intuitive yet not native.
[560.80 → 566.36] And by that I mean it's an interface that is very intuitive if you've used either platform,
[566.58 → 571.62] but it doesn't try to go that last 5% to really emulate the operating system,
[571.76 → 577.08] which seems like always leaves the user just wanting a little bit more because web apps are web apps.
[577.18 → 578.04] They're not native apps.
[578.04 → 585.22] Yeah, I mean, we've done, I think, a fair amount so far in terms of replicating a lot of native stuff.
[585.42 → 593.92] So, you know, the biggest thing and biggest talking point a couple of months ago was just sort of emulated scrolling,
[594.08 → 599.96] momentum scrolling, and the ability to fix, you know, elements to a certain position on the page and keep them there.
[599.96 → 603.52] This has always been like a challenge in mobile web kit.
[603.60 → 607.66] They've just never built it in because of some OS-type restrictions.
[608.04 → 609.24] It just hasn't been possible.
[609.78 → 614.36] So we have to sort of fake it with JavaScript and CSS.
[615.58 → 621.48] So, you know, once that was out of the way, we sort of moved on to a whole range of different native-feeling components
[621.48 → 625.02] like carousels, pickers, things like that.
[625.02 → 635.88] I think the biggest thing that we miss and that we're just not able to do is some of the hardware APIs that we're unable to reach.
[636.34 → 643.84] So, you know, in terms of open source projects, you have Phone Gap, which has been a great MIT project from Novi
[643.84 → 651.66] that opens up those APIs, lets people access the camera or access the contact list or, you know,
[651.66 → 658.88] even just easier audio and video, even though it's part of HTML5, you can actually get a more polished experience with them,
[659.82 → 662.06] you know, using some built-in native APIs.
[663.20 → 664.54] You know, you've got a blog post.
[664.82 → 665.98] This is actually your blog post.
[666.06 → 667.94] I didn't realize the byline the first time I read it.
[668.02 → 668.98] Getting sassy with CSS.
[669.24 → 671.64] We're big fans of both Compass and Sass here.
[671.74 → 675.88] Episode one of the change log was about Compass and Sass.
[676.02 → 676.64] Oh, was it?
[676.76 → 678.10] I didn't realize that.
[678.10 → 687.02] And we're going to have Nathan and Chris on very soon to talk about the latest and greatest Sass 3.0 and Compass 1.0 items that are out there.
[687.10 → 692.04] But talk a bit about the architecture of the themes in Sen cha and where Sass plays into that.
[693.40 → 693.84] Definitely.
[694.44 → 700.60] So that, the theming has been sort of my brainchild in the project in regard to development.
[700.74 → 702.28] That's been my major contribution.
[702.28 → 709.40] And I just think it's the most flexible sort of framework theming I've seen yet.
[709.86 → 713.76] And I'm just super excited about it.
[713.96 → 723.28] Like, so basically, Sass and Compass at a very core level provide you some tools in CSS that you've never had.
[723.38 → 728.82] They abstract CSS to the point where you can use functions, variables, things like that.
[728.82 → 744.48] But in regard to creating a framework, a framework that includes a UI layer, especially like Sass and Touch, having flexibility and sort of making those style sheets as compact as possible is a huge goal.
[744.70 → 749.02] You know, because customizing one's app is probably one of the highest priorities.
[749.02 → 759.40] And so we've done a lot with Sass and Compass in regard to making colour variables, sort of overriding variables.
[759.40 → 765.40] And so you can, at this point, take sort of a Sass theme file.
[765.96 → 769.92] All you have to do is include our theme file, our Sass file.
[770.22 → 780.72] And then you can basically overwrite variables like base colour or highlight colour or active to change the entire look and feel of the application.
[781.38 → 787.08] Do you have a preference between the indented old school Sass style and the new SCSS?
[787.08 → 797.76] Yeah, I used to hate the old style because I was so used to CSS, and it just felt unnatural.
[798.40 → 802.54] And its dependence on white space formatting was extremely strict.
[802.66 → 806.18] So if you had an extra space somewhere, it would throw off the whole compiler.
[806.18 → 810.84] Then we made the switch to Sassy CSS, the SCSS.
[811.64 → 816.68] And then I missed the old one because it was so much more compact.
[817.60 → 824.82] But now I've sort of gotten over it and I like it being a little more verbose with all the punctuation and everything.
[825.02 → 825.80] I think it's better.
[826.08 → 827.38] You know, I'm an old school guy myself.
[827.38 → 835.80] I started a new project in the SCSS, the curly brace syntax, just to get up to speed on the differences and the nuances.
[836.16 → 838.74] And I gave it a couple of weeks and I just had to switch it back.
[839.24 → 843.14] At first, it's annoying because, you know, you have so many more brackets and things.
[843.32 → 847.98] But the fact that you don't have these white space errors is a huge plus for me.
[847.98 → 853.14] And I also actually very much like the fact that it validates as CSS.
[854.22 → 861.16] Even though it has no actual implications in the compilation process, it just feels better.
[861.64 → 862.54] That's a big plus.
[863.08 → 865.56] Let's talk about UI programming for a moment.
[865.76 → 869.96] So what is the programming model to build a Cinching Mobile application?
[869.96 → 873.96] Most of the examples I've seen are purely programmatic.
[873.96 → 878.94] Is there any declarative markup style options available?
[879.60 → 880.62] There are not.
[880.76 → 886.76] So that is definitely the biggest differentiation point between JR Touch and Cinching Touch.
[886.86 → 890.28] And we are keeping both active and running, by the way.
[890.40 → 898.86] So JR Touch has become part of Cinching Labs, which is sort of our new foundation set up specifically for MIT fully open source projects.
[898.86 → 904.88] So Cinching Touch is definitely programmatic.
[905.08 → 907.32] It's API-driven in JavaScript.
[908.26 → 914.98] We are investigating the possibility of doing some sort of progressive enhancement solution.
[914.98 → 929.58] But at the same time, that's sort of a lower priority on our list as sort of creating the most robust, functional, and optimized framework.
[929.58 → 931.68] It's sort of number one priority at the moment.
[932.10 → 938.48] I can see that sort of thing playing in as sort of like a plug-in that you could throw in on top of Cinching Touch at some point.
[938.48 → 954.98] But in terms of creating sort of actual, if you were to think about most sort of well-done iPhone apps, if you were to think about Twitter as an iPhone app, it's not something where you would want the bulk of your content really residing in the HTML page to begin with.
[954.98 → 964.62] It's more about sort of functional process and having some sort of application structure like MVC or something behind it.
[964.62 → 973.58] Well, I guess the upside of a programmatic approach like that is you could build tools on top of that to build those interfaces at some point, right?
[974.14 → 974.88] Yeah, absolutely.
[974.88 → 985.84] And so we've done that on the desktop so far with X Designer, which allows you to sort of drag and drop components to generate the UI classes for your app.
[985.88 → 990.88] And then you can just kind of drop those UI classes into the app and write your functional code around it.
[990.88 → 996.80] And I think doing something like that for touch wouldn't be too big a hassle, though.
[997.42 → 1000.10] Again, you know, we are still in beta with something to touch.
[1000.24 → 1007.18] So we have a little bit more to go on the framework before we start investigating tools and some extra plug-ins and things.
[1007.26 → 1011.48] But they are all sort of on the plate as it stands.
[1011.48 → 1021.54] Well, we've hit on iPhone and Android, but we should mention that you've got really robust support for the iPad with the split window UI metaphors.
[1021.70 → 1022.54] Talk about that for a moment.
[1023.70 → 1024.06] Sure.
[1024.44 → 1033.02] I think the iPad, you know, in terms of traffic and market share, it's not the most exciting thing in the world.
[1033.16 → 1035.66] You know, there's still plenty of room for growth there.
[1035.66 → 1041.38] But in terms of what Sens ha Touch can do for the iPad, I do think it's sort of unprecedented.
[1041.60 → 1044.90] It's definitely something you can't accomplish with JR Touch.
[1046.32 → 1060.08] You can make very native-feeling iPad web apps with Sens ha Touch because of all the sort of layout and data options that we've brought over from XJS.
[1060.08 → 1065.22] It's really just, at its core, Sens ha Touch is really just an app framework.
[1066.32 → 1077.72] And so sort of the more resolution we can give it and still having it be a touch-based API, you know, a touch-based UI, the better, the more impressive I think it becomes.
[1078.26 → 1080.56] We've got some impressive demos up on the website.
[1080.68 → 1083.58] One of those is the Open Congress application.
[1083.74 → 1088.30] It looks like you guys are using APIs from Sunlight Labs, which were on episode 013.
[1088.30 → 1090.38] Did you have a hand in building that one?
[1090.46 → 1092.38] I guess the Geo Congress app is what I'm talking about.
[1093.20 → 1093.28] Yeah.
[1093.50 → 1100.90] So I helped design that app, and I helped style that app, and I helped a little bit within the structure.
[1101.10 → 1102.96] But really, that was mostly coworkers.
[1104.28 → 1105.56] I spent the majority of my time.
[1105.74 → 1108.98] So my demo was sort of the Diva one in terms of programming.
[1110.34 → 1113.34] I did the majority of the programming on that one.
[1113.44 → 1115.44] And that was more of a lesson for myself.
[1115.44 → 1119.30] I just wanted to make sure I put an app out there before I started marketing the thing.
[1121.40 → 1129.18] Well, since we are an open-source podcast, let's talk about licensing models for a moment around not only the mobile platform but the other projects that you guys have.
[1130.32 → 1130.72] Sure.
[1130.72 → 1137.74] So, as I mentioned, just real quick, so we just recently launched Central Labs.
[1138.94 → 1140.18] JR Touch is in there.
[1141.00 → 1144.46] Rafael.js is in there, who I understand was on a few weeks ago as well.
[1144.46 → 1159.82] And then we also have a variety of sort of Node-related projects, which we're putting on there, including Connect and Express, which are some great sort of server-side JavaScript projects.
[1159.82 → 1166.30] I think that's one of the most exciting things happening in tech right now is stuff happening in Node.
[1167.46 → 1172.00] And I know we hope to look a little more into it as we develop our framework further.
[1172.34 → 1176.26] But so that's all under Central Labs at the moment.
[1176.44 → 1181.08] And we will be getting a site up to better highlight those projects soon.
[1181.08 → 1196.00] And then there are the projects which we offer commercial licenses for, including XJS, XGWT, which is a native port of XJS to GWT, and Central Touch.
[1197.06 → 1201.26] So what are your plans for world domination around, I guess, JavaScript on the server side?
[1201.32 → 1204.36] It sounds like you're attracting some really sharp talent.
[1204.50 → 1205.56] Tim Caswell is a buddy of ours.
[1205.66 → 1209.48] He was on Episode 017, and we know TJ and those guys are out there.
[1209.48 → 1216.06] So what are you guys doing on the server with Node that's intersecting all of this mobile and client-side magic?
[1216.50 → 1216.68] Yeah.
[1217.08 → 1221.38] Tim and TJ are super awesome, super talented developers.
[1223.00 → 1227.38] Unfortunately, I can't really disclose everything we're looking at right now.
[1227.90 → 1229.80] But you're going to give us a scoop when you get close.
[1230.32 → 1233.26] Yes, I will definitely call back in with the scoop.
[1233.26 → 1248.68] But I know a variety of things that we're looking at as far as inclusion with the framework and some of the possibilities that it's opening up are just incredibly innovative.
[1248.84 → 1251.44] I mean, I just haven't seen stuff like it before.
[1251.44 → 1259.44] But I don't want to bound the company to a certain direction, especially because that's not really my field.
[1260.62 → 1260.72] Sure.
[1261.20 → 1267.98] Well, we come to the part of the show where we ask, kind of turn the episode upside down and ask our guests what's got them excited in the world of open source.
[1268.08 → 1268.78] So what's on your radar?
[1269.00 → 1270.54] What are you anxious to play with?
[1271.44 → 1273.66] Yeah, I mean, we've already covered most of them.
[1273.66 → 1277.94] So I'll be honest and admit, I haven't tried Node at all yet.
[1278.30 → 1285.00] And some of the things I've heard in terms of performance and optimization, I just think are sort of amazing.
[1285.30 → 1289.48] So, I mean, that's a big thing I want to get into is learning Node.
[1290.70 → 1296.66] As we mentioned, SAS and Compass are probably my favourite two new technologies this year I've found.
[1296.66 → 1303.18] I just sort of can't get over how much easier they've made style sheet authoring.
[1303.36 → 1311.66] And, like, I can't even think of, like, doing a one-page site now without using SAS and Compass because it just makes it that much easier.
[1313.70 → 1318.72] And then I don't think this qualifies as an open source technology.
[1318.88 → 1320.06] I mean, no, it's open.
[1320.06 → 1333.12] So Yahoo's SQL has also been just a new thing I've just sort of got onto this year, which is incredibly cool.
[1333.30 → 1345.78] I mean, it's – so for those who don't know, SQL is a sort of developer tool from Yahoo that allows you to sort of query the web in a SQL-like format.
[1345.78 → 1358.62] And this can be sort of anything in regard to a query, a REST-based XML API, or it could query a JSON API, or it could even just screen scrape pages.
[1359.18 → 1361.76] It can do all of this with SSL authentication.
[1363.14 → 1370.48] I mean, the power behind it is just kind of immeasurable in that, especially when I was putting together that Diva demo,
[1370.48 → 1382.12] I think one of the coolest things you realize when you're working with SQL is the second you join two data sources as if you were joining two tables in MySQL.
[1383.48 → 1391.76] And it's really just sort of these data sources on the Internet of these API endpoints, and it's actually combining data from the server side.
[1391.76 → 1397.20] And no matter what you use, it'll spit back the data it gets in JSON format.
[1397.62 → 1412.70] So for web app developers, you know, cross-domain issues have always been a huge sort of burden because you can't really request certain types of APIs over – from different servers as a security precaution.
[1413.34 → 1416.12] But SQL actually removes a ton of those issues.
[1416.12 → 1421.38] So for web app developers, I think it's just one of the coolest technologies I've seen.
[1422.36 → 1424.52] Fun time to be a mashup developer for sure.
[1425.20 → 1426.02] Yeah, definitely.
[1426.52 → 1427.46] Well, thanks for joining us today.
[1427.54 → 1437.00] I can't wait to continue to play with India and see where the project's headed, especially as you close in on 1.0 and what great things the listeners are going to build with it.
[1437.72 → 1438.12] Definitely.
[1438.34 → 1439.12] Thanks for having me.
[1439.12 → 1446.34] I think we have a ton of good stuff coming, so there are plenty more secrets before 1.0 actually drops.
[1446.64 → 1461.44] But yeah, and I should also mention real quick, we are going to offer commercial licensing on India Touch, just like we do with XJS and GWT, which are split between GPL and commercial.
[1462.18 → 1464.96] And we will be announcing that within a week.
[1465.12 → 1466.58] So that's coming very soon.
[1466.58 → 1468.44] I know there are a lot of people waiting to hear that.
[1469.12 → 1470.02] Great. Looking forward to it.
[1470.24 → 1470.72] Thanks, David.
[1471.16 → 1472.12] All right. Thanks for having me.
[1472.12 → 1473.28] The dip.
[1473.36 → 1490.68] The dip
[1490.68 → 1499.80] So how could I forget where I found myself for the first time?
[1500.80 → 1503.52] Safe in your arms.
