[0.00 --> 3.60]  Hi, I'm Jan Leonard from Berlin. I work on Couch TV, and you should listen to The Changelog.
[19.48 --> 24.50]  Welcome to The Changelog, episode 0.2.8. I'm Adam Stachowiak.
[24.86 --> 29.08]  And I'm Wynne Netherland. This is The Changelog. We cover what's fresh and new in the world of open source.
[29.08 --> 32.68]  If you found us on iTunes, we're also on the web at thechangelog.com.
[32.86 --> 33.64]  And we're also on GitHub.
[34.30 --> 41.20]  Yep, if you go to github.com forward slash explore, you'll find some training repos, some feature repos from our blog, as well as our audio podcasts.
[41.36 --> 45.88]  If you're on Twitter, follow ChangeLogShow, not The Changelog. And I'm Adam Stach.
[46.40 --> 51.02]  And I'm Penguin, P-E-N-G-W-Y-N-N, episode 28. Can you believe it?
[51.12 --> 53.16]  Wow, man. On location, too.
[53.16 --> 58.26]  On location at Texas JavaScript. Another interview that we did while we were down in Austin.
[58.46 --> 60.80]  Talked to John Resig from jQuery.
[61.38 --> 63.76]  Yeah, mobile, well, Mozilla, yeah.
[64.32 --> 69.42]  Mozilla Labs. Talked about the state of mobile web development. What did he say would be fun in about three years?
[69.66 --> 74.78]  Well, he said in three years it would be finally fun to develop for the web on the mobile devices.
[75.32 --> 78.18]  What's three years in tech years? That's like a decade, right?
[78.26 --> 79.54]  Yeah, it's 30 years, right?
[79.54 --> 91.12]  At least. So he's got a project called Test Swarm from Mozilla Labs that allows you to do continuous integration testing for your JavaScripts across a wide range of browsers and simulators.
[92.14 --> 100.98]  Talked a bit about what it's entailed to support all these browsers that are beyond iPhone and Android, especially on BlackBerry and Simeon and Nokia.
[101.44 --> 107.92]  And he's also got the devices to battle, the platforms and the software, the browsers to battle. That's a mess.
[107.92 --> 112.16]  Sounds like a recipe for insanity personally, but he's pretty excited about it.
[112.38 --> 115.16]  Well, if there's one man who could do it, maybe it's John and his team.
[115.78 --> 116.84]  Agreed. Should we get to it?
[116.92 --> 117.82]  Let's do it.
[117.82 --> 132.40]  We're joined today by John Rezig, creator of jQuery, worker at Mozilla Labs.
[133.06 --> 135.62]  Talk to us today about Test Swarm, some other projects you've got.
[135.92 --> 139.04]  For the four or five people out there that may not know who you are, John, why don't you introduce yourself?
[139.52 --> 139.76]  Sure.
[139.76 --> 141.96]  Sure. So thanks for having me.
[142.08 --> 150.24]  But I'm the creator of the jQuery JavaScript library and a number of other JavaScript-y projects.
[151.22 --> 158.24]  I'm also the author of the book Pro JavaScript Techniques and the author of the upcoming Secrets of the JavaScript Ninja.
[159.30 --> 161.14]  Cool. So we're at Texas JavaScript.
[161.14 --> 171.38]  JavaScript's really had kind of a renaissance in the last couple of years, thanks mainly to client-side frameworks like your own and then Node.js on the server side.
[171.78 --> 173.90]  What's the state of JavaScript as you see it?
[175.50 --> 177.44]  I think it's very favorable.
[177.44 --> 185.98]  I just, I do not, like I frequently sit down and I think, you know, where, you know, the web is going and how languages are evolving.
[186.36 --> 194.84]  And I just can't envision a world in which JavaScript is not still relevant, you know, five, ten years, 15 years down the line.
[195.20 --> 198.64]  It's, you know, it's part of every browser.
[198.92 --> 200.42]  It's the language everyone's using.
[200.42 --> 212.32]  And, yeah, so I think, you know, in a lot of ways I think now, you know, if you're still on the edge or trying to decide if you want to get into JavaScript, it's a phenomenal language to get into.
[212.78 --> 213.84]  There's oodles of jobs.
[213.96 --> 218.22]  Like everyone hires for JavaScript since everyone does web apps.
[218.60 --> 222.06]  So it's just, I don't know, I think it's the tops.
[222.38 --> 225.42]  But, of course, I'm seeing this as a guy who does JavaScript all the time.
[225.42 --> 231.64]  So to suppress my inner fanboy, we'll postpone a couple of the jQuery questions here for a minute.
[231.98 --> 236.34]  Give you a chance to talk about TestWarm and this project from Mozilla Labs.
[236.48 --> 237.70]  What is it and what's it trying to do?
[238.20 --> 238.44]  Sure.
[238.56 --> 242.98]  So this is a project that I developed last year, 2009.
[243.76 --> 254.84]  And it was trying to solve a definite problem I was encountering, which is that when you're testing, trying to do automated testing in browsers,
[255.42 --> 265.10]  specifically for JavaScript code, you have to open up a large number of browsers, you have to run the code, you have to collect the results, display the results, et cetera, et cetera.
[265.36 --> 266.70]  It gets very time-consuming.
[267.74 --> 280.36]  And so sort of the premise behind getting TestWarm up and running was that people could contribute their machines and their browsers and hook them into the swarm, as it's called.
[280.36 --> 289.62]  And then projects like us, like jQuery, could just submit tests and they would run in the client machines and we would collect results back.
[289.82 --> 293.74]  So it would remove the burden of running those machines from us.
[293.94 --> 298.96]  And we could just take all the advantage of running and having nice and easy test runs.
[298.96 --> 314.26]  So what that sort of led up to, though, and what I've been working on lately is that when you start doing testing on mobile devices and testing on phones, it's really hard to automate that.
[315.28 --> 319.56]  And whereas typically on the desktop, there is some way you can automate it.
[319.56 --> 325.32]  There's toolkits like Selenium, for example, and those can automate browser execution.
[325.74 --> 327.30]  But in phones, it's just a wild west.
[327.44 --> 329.42]  There's nothing there to automate that.
[329.98 --> 338.00]  So this is where TestForm is really helping us because we're able to automate the execution of tests on mobile devices and we're able to get results back.
[338.28 --> 342.02]  And we're able to develop very similarly to how we would on the desktop.
[342.02 --> 349.60]  So it helps to just smooth things over and make our development process work that much better.
[350.10 --> 354.98]  So dealing with such a wide array of simulators and all these different platforms, all unicorn and rainbows?
[355.72 --> 356.74]  Not really, no.
[357.50 --> 360.26]  I mean, it's a lot better than what it used to be.
[361.60 --> 370.66]  And in a lot of ways, I think that we're sort of on the cusp of mobile web development becoming really, really good.
[370.66 --> 375.66]  I think probably in a couple years here, it's going to be phenomenal.
[376.36 --> 382.14]  Because right now what we have are we have a good number of WebKit-based browsers, which is fantastic.
[382.50 --> 389.16]  But we also have a lot of really just weird and old browsers, like the BlackBerry browsers or the older Windows Mobile browsers.
[389.82 --> 394.96]  And that's just a lot of legacy that's hanging around and making it frustrating for us.
[394.96 --> 407.36]  So, yeah, it's definitely a challenging process, especially since there has been no good information published on how to do mobile web development.
[407.80 --> 417.66]  Like when you're doing desktop web development, you know you just have to download Firefox, download Safari, download Opera, and you just open it up and you test.
[417.66 --> 422.66]  But you know that because it's like common knowledge at this point.
[423.14 --> 429.40]  Whereas with mobile development, no one knows what the popular browsers are or how to download them or how to test them.
[429.96 --> 431.98]  And so this is something I've been trying to figure out.
[432.90 --> 436.64]  And this is what I talked about today.
[436.64 --> 442.42]  But it's something I'm going to be publishing here within the next couple weeks on the jQuery mobile website.
[443.46 --> 443.70]  Very cool.
[444.24 --> 448.98]  In your talk, you mentioned that in three years from now it's going to get real fun to develop applications.
[449.62 --> 451.46]  Are we going towards web browser?
[451.58 --> 452.24]  Are we going towards native?
[452.36 --> 454.98]  What is the best way to go towards the mobile web?
[455.66 --> 461.36]  So the way I think about it is that you could develop mobile applications.
[461.36 --> 466.46]  When I say mobile applications, I mean like something you buy off an app store and you install.
[467.10 --> 469.20]  You can do this using HTML, CSS, JavaScript.
[469.54 --> 471.48]  And there are a bunch of people that are really interested in that.
[471.92 --> 474.46]  There's a phone gap that makes that possible.
[475.20 --> 475.98]  That's all well and good.
[476.24 --> 479.50]  As far as I'm concerned, though, that's really, really easy.
[479.86 --> 481.72]  You know, you're using a latest web kit.
[482.02 --> 482.54]  It's a dream.
[483.66 --> 490.54]  But the reality is that that's a very small subset of the total number of devices that you could be targeting.
[491.36 --> 501.20]  The best way to get your application or your website, for that matter, in front of the most number of people is to make it a website.
[501.80 --> 505.12]  You know, and just treat it like you would anything else.
[506.70 --> 514.84]  So that way your users can just open up a URL, interact with your web application, what have you.
[515.26 --> 518.46]  But just using your traditional web technologies.
[518.46 --> 524.70]  And in a lot of ways here, you can just, you know, it's the, what, write once, use everywhere.
[525.96 --> 530.98]  And so it simply means, even from a logistical standpoint, it makes more sense.
[531.38 --> 533.94]  You just have to write one web application.
[534.26 --> 534.82]  It works.
[535.36 --> 536.78]  And you get more users.
[536.78 --> 544.54]  Whereas if you're targeting strictly application installs, you know, you're severely limited.
[545.34 --> 557.16]  So at least, and at least from a technological perspective, I find that it's just, it's much, it's a much more challenging problem to try and target those multiple platforms.
[557.16 --> 562.64]  Whereas simply targeting like iPhone, for example, it's, it's rather trivial.
[562.78 --> 564.14]  It's a subset of the larger issue.
[564.62 --> 564.70]  Right.
[565.14 --> 568.68]  So when we look at the mobile web, how many browsers do we really have to support?
[568.84 --> 570.54]  There's Symbian, there's, there's Windows.
[570.86 --> 571.76]  How many are there?
[572.42 --> 573.70]  There's, there's, there's a lot.
[573.70 --> 588.82]  But it's, at least in counting all the different operating system versions and devices, what it boils down is, it boils down to about a dozen devices, physical devices you have to own.
[589.26 --> 593.18]  And then on those, there's a varying number of browsers you have to support.
[593.92 --> 600.56]  It depends because like, like for example, Opera runs on most mobile phones, Opera Mobile and Opera Mini.
[600.56 --> 608.12]  And then Fennec, the Firefox for mobile, runs on Android and Memo.
[609.10 --> 614.76]  And so it's, the total number of browsers is a little bit larger than the 12.
[616.00 --> 624.00]  So, but in, in total, it's definitely more browsers than we, than what we currently support on a jQuery desktop.
[624.62 --> 628.06]  You know, it is, because, you know, right now we support, I think it's 11 browsers.
[628.06 --> 631.60]  And so this is more than double our browser coverage.
[632.30 --> 635.46]  Talk about Fennec for a moment and, and Firefox on mobile.
[635.66 --> 636.74]  Is this a code name?
[636.84 --> 639.14]  Is this the, the marketing name for this particular platform?
[639.14 --> 643.66]  And how are, what were we at in the lifespan of, of Firefox on mobile?
[644.74 --> 647.00]  I think it was a code name.
[647.14 --> 648.58]  I think it's the actual name now.
[648.76 --> 649.74]  Don't quote me on that.
[650.54 --> 654.06]  Um, because I mean, they have like the logo and everything.
[654.16 --> 656.00]  It's little Fennec Fox and it looks really cute.
[656.00 --> 667.66]  Um, and so, I mean, the big push or so traditionally it's been running on Memo, which is, um, a Linux based operating system that was on a Nokia tablet devices.
[668.20 --> 669.78]  Um, doesn't have a lot of market share.
[670.42 --> 676.42]  Um, they started work on a Windows mobile version, which was probably a good idea.
[676.42 --> 682.44]  But the problem was that they weren't able to get tools for Windows mobile that allowed them to build a good enough Firefox.
[683.32 --> 688.86]  So they canceled that project and, uh, they're focusing almost entirely on Android now.
[689.12 --> 691.88]  Shipping a really good Firefox browser for Android.
[692.12 --> 695.02]  And I've played around with it some and it's, it's just, it's fantastic.
[695.30 --> 700.32]  It, in, in some ways it's even faster than the built in WebKit based browser.
[700.32 --> 702.40]  Um, which I think is pretty cool.
[702.72 --> 711.48]  And so I think there's a lot of potential here for, you know, additional competition to really bring new browsers in, uh, into this market.
[711.88 --> 713.78]  Especially so on, um, on Android.
[713.98 --> 717.06]  Because Android is, is growing, you know, gangbusters here.
[717.60 --> 722.18]  And, um, so, you know, both Opera and Android, I think, have a lot of potential to grow here.
[722.18 --> 729.22]  When we look at the, the space of the mobile browser like you just mentioned, how does that trickle down in comparison to, say, the, the desktop browsers?
[729.40 --> 737.38]  Like, the standards, do we have the same troubles, the same different issues with supporting standards and certain types of standards being supported on web browsers for mobile?
[738.24 --> 739.52]  So, the problems do exist.
[739.72 --> 743.70]  They're, they're tending, generally speaking, they're tending towards a better state.
[744.12 --> 748.68]  Um, so, like, for example, BlackBerry has their own custom browser that they wrote.
[748.68 --> 753.34]  Um, and it's not quite as good as what the other browsers have.
[753.68 --> 758.48]  Um, they are, they just did a rewrite, and the next version of the BlackBerry browser is going to be WebKit based.
[759.10 --> 769.68]  Um, but generally speaking, the browsers that we're supporting are, on mobile, are generally equivalent to the browsers you see on, uh, desktop.
[771.06 --> 778.52]  Roughly speaking, what you end up supporting in, in mobile is, like, Safari 2 and newer, um, Firefox 3.5 and newer, i.e. 6 and,
[778.68 --> 782.26]  uh, 7 and, uh, Opera 9.5 and newer.
[782.50 --> 784.56]  That's roughly what the versions correlate to.
[785.30 --> 790.58]  Um, so, yeah, so it's, it's, it's a pretty manageable problem.
[791.02 --> 794.94]  The, the difficulty is, it's just, it's just those little quirks that get you.
[795.06 --> 799.82]  And the, the simulators and the, you know, all the knowledge that has to go into making sure everything runs smoothly.
[800.26 --> 807.34]  I, I'd say probably most of the issues you're going to encounter in doing mobile web development aren't going to be logistical JavaScript-y issues.
[807.44 --> 809.52]  Are there going to be more interaction issues?
[809.84 --> 814.08]  You know, developing good UIs, developing things that work with touch interfaces.
[814.50 --> 817.84]  Like, I've got a feeling that this probably where most of the work's going to go.
[817.84 --> 821.44]  You know, a lot of web development is using tools like Firebug.
[821.86 --> 825.74]  And since you're developing for the platform, you're also consuming as a developer.
[826.22 --> 830.18]  You get to kind of inspect the markup and, and interact with your application in a live environment.
[830.70 --> 836.48]  Um, you mentioned in your talk that the simulators are often kind of, it's difficult to simulate the actions that you're performing.
[836.90 --> 839.84]  How much more important are tests in this brave new world?
[839.84 --> 842.38]  I mean, it's, it's, it's critical.
[842.92 --> 848.28]  Um, and so it's, there, there, there, there's two things.
[848.36 --> 849.76]  There, there's the testing and there's the debugging.
[850.36 --> 855.66]  Um, and unfortunately debugging is really not solved yet.
[855.78 --> 867.48]  So there's, there's tools like Dragonfly for, uh, Opera, which do, does that a little bit, it gives you like a developer console that you can use, uh, and have a hook into, uh, mobile devices.
[867.48 --> 869.40]  So that's something.
[870.34 --> 878.38]  Um, but in general, there aren't really tools, you know, like Windows Mobile or Blackberry or Fennec for that matter.
[878.54 --> 880.14]  Like they don't have those debug consoles.
[880.56 --> 883.26]  Um, so it's, it's, it's definitely tricky.
[883.36 --> 893.04]  And, and, and this is one case where, so testing will get you part of the way there and that it'll, it'll make sure you have good coverage and stop you from getting regressions or at least help lead you on the right track.
[893.04 --> 899.02]  Um, but it's not going to help you to actually fix the bugs and that's still hard.
[899.56 --> 903.68]  So you didn't jump into this new mobile world because you were bored and needed a, a weekend hobby.
[903.80 --> 908.90]  You really are trying to push forward to get jQuery, uh, in a more mobile friendly state.
[909.00 --> 910.44]  Talk about progress around that.
[911.14 --> 919.48]  So when looking at the, um, the mobile system, you know, I wanted to make sure that jQuery was going to be a capable mobile, uh, library.
[919.48 --> 934.70]  And one of the things that I thought originally was maybe a good way to distribute jQuery would have like be like have a stripped down build of just things were only like web kit devices.
[935.86 --> 940.68]  That could work, but I don't think that's as interesting of a problem.
[940.68 --> 945.96]  Um, what I think is more interesting is being able to ship one copy of jQuery, have it be the copy of jQuery.
[946.06 --> 955.08]  It's the same one you download on the website and have it work for both all the desktop browsers and all the mobile browsers and just, just have it just work.
[955.16 --> 962.10]  So that way you can publish your website using jQuery and it's going to work on desktop and mobile and we can make that guarantee.
[962.46 --> 966.92]  I think that's a far more interesting problem and something that no one else is really tackling right now.
[966.92 --> 978.86]  So, so at least going forward, most of our effort isn't going to be that interesting or at least not, uh, it's not going to be like flashy and, you know, uh, you know, gestures and stuff.
[978.90 --> 983.96]  It's going to be, it's going to be very straightforward in that we're just going to make sure we work and we can guarantee that we work and we're testing.
[984.54 --> 988.84]  Um, which is, it's a lot of work and that's something that we really want to push forward towards.
[988.84 --> 993.02]  How much has, uh, projects like JQ Touch influenced your work at all?
[993.82 --> 1006.54]  I mean, yeah, the JQ Touch and IUI, I mean, they're both fantastic projects and they, um, they're predominantly focusing on the user interface, making sure that users have a, an easy way to produce an interface to interact with.
[1007.12 --> 1016.04]  Um, the, the thing is that both of them tend to emphasize creating a, replicating an iPhone-like experience.
[1016.04 --> 1022.18]  And that's something, but it, it, it doesn't really work outside of an iPhone.
[1022.54 --> 1026.00]  You know, it doesn't really work on Android, it doesn't work on a Palm, it doesn't work on Windows Mobile.
[1026.30 --> 1034.48]  Like, you, you really need to have something that's much more generic and something that is producing a good user experience more universally.
[1034.72 --> 1041.34]  So this is something that I'm very interested in and something I'll be pushing forward, uh, on, uh, after the jQuery core bits are done.
[1041.34 --> 1051.42]  So that we can provide users with the tools they need to have a good, uh, mobile application that isn't iPhone-specific.
[1052.18 --> 1058.48]  You know, continuing that thread, uh, the health of a, of an open-source project can really be judged by the ecosystem it supports as well.
[1058.86 --> 1066.34]  Two projects that we featured on the show that I'd like to get your feedback on, uh, first is SammyJS and the second, uh, underscore JS.
[1066.34 --> 1067.18]  Mm-hmm.
[1067.72 --> 1071.22]  Oh, I mean, I played around with both of those, um, a little bit.
[1071.42 --> 1074.94]  And, uh, I wish I had more time to play with fun JavaScript projects.
[1075.46 --> 1084.22]  Um, but yeah, I mean, um, underscore, I'm trying to remember, I played around with it because it provides all the different, um, utilities and such.
[1084.36 --> 1084.66]  That's right.
[1084.74 --> 1087.52]  And, um, yeah, I like, I like that one.
[1087.62 --> 1089.26]  It certainly had an interesting API.
[1089.80 --> 1091.72]  Uh, it was, it was nice to use.
[1091.92 --> 1094.94]  Um, and then Sammy was the, the script loader, um, right?
[1094.94 --> 1100.58]  So, Sammy is the one that, uh, mimics Sinatra in the browser, so he gives you routes and state, hash-based state.
[1100.74 --> 1100.86]  Yeah.
[1101.38 --> 1106.24]  And, um, and, uh, yeah, I mean, they're cool.
[1106.46 --> 1109.64]  And, and, I, like I said, I wish I had more time to, like, really dig into it.
[1109.66 --> 1110.94]  Same thing with, like, Node.js, for example.
[1111.30 --> 1112.60]  Like, like, like, that's hot stuff.
[1112.66 --> 1116.40]  And, like, I just have, like, no time to, like, actually sit down and, like, build a Node.js application.
[1116.62 --> 1118.80]  Which is funny because, like, you know, like, all I do all day is JavaScript.
[1118.98 --> 1121.04]  But, like, I'd have no time to, like, play with other JavaScript.
[1121.04 --> 1125.40]  So what, and this is usually the part of the show we ask what is on your open source radar.
[1125.60 --> 1127.16]  So it doesn't have to be JavaScript related.
[1127.38 --> 1136.98]  Things, rocks you've uncovered in this new mobile world where you're, you know, uncovering all these little-known simulators that we're now being, you know, forced to deal with.
[1137.34 --> 1138.60]  What projects have you excited?
[1138.74 --> 1142.12]  What, what is pushing the envelope and has you excited to, to play with?
[1142.12 --> 1146.80]  I wish there were more projects relating to mobile, mobile web.
[1147.48 --> 1148.64]  There really aren't that many.
[1148.96 --> 1157.80]  The one that I was playing around recently was Touchscroll, which helps to simulate scrolling gestures on iPhone devices.
[1158.56 --> 1162.86]  And because that's, because one of the problems with the iPhone is that you can't have position fixed elements.
[1163.80 --> 1167.00]  And so that's something that it helps to work around.
[1167.46 --> 1169.40]  So that was a pretty interesting piece of code there.
[1169.44 --> 1170.68]  And I've been playing around with that a little bit.
[1170.68 --> 1179.90]  Another one, the name is escaping me at the moment, but it is written by Yehuda Katz, WY Katz on GitHub.
[1180.54 --> 1184.06]  And he was working on doing state management.
[1184.60 --> 1192.36]  So being able to manage, like, loading in remote JSON resources and having them hit the cache wherever possible.
[1192.86 --> 1194.68]  So, I mean, that's been a challenge in and of itself.
[1194.74 --> 1198.70]  But it helps to allow you to build offline applications easier.
[1198.70 --> 1210.30]  When you say you wish there were more projects in the mobile web space for the JavaScript guys out there who either want to impress you or just get into a cool project,
[1210.38 --> 1213.10]  what kind of projects do you want to see happen in the mobile web?
[1213.90 --> 1216.42]  More projects that aren't just for the iPhone.
[1216.42 --> 1225.70]  Like, if you look at this, almost all the iPhone specific, or almost all the JavaScript projects that are for mobile are just for iPhone.
[1226.36 --> 1227.88]  They're, you know, JQ Touch, IUI.
[1228.10 --> 1230.18]  Like, all those, they're just, that's all they target.
[1230.58 --> 1232.70]  And if it happens to work on Android, then they're like, okay.
[1232.96 --> 1234.42]  But, like, they don't even go beyond that.
[1234.42 --> 1239.50]  So something that would impress me would be things that work on more platforms.
[1240.10 --> 1243.22]  You know, things that take Blackberry into account, take Windows Mobile into account.
[1243.78 --> 1245.50]  And then you'll have my attention, for sure.
[1245.94 --> 1253.68]  You know, I'm seeing another parallel to, you know, when the web came out, we did a lot of work to try to emulate desktop interfaces in the web.
[1253.98 --> 1255.22]  And it seems like they always fall short.
[1255.30 --> 1260.60]  And as powerful as HTML5 and, you know, these new JavaScript frameworks, we have a lot more tools at our disposal now.
[1260.60 --> 1266.24]  And it seems like a lot of times when we're building web interfaces in the mobile web, we tend to want to emulate native widgets,
[1266.36 --> 1268.36]  where it seems like we're always just a bit lacking.
[1268.80 --> 1274.58]  Should we just be changing our focus and coming up with new interfaces that are just web-based and we're proud of it?
[1275.10 --> 1275.92]  Yeah, I suspect so.
[1276.16 --> 1285.14]  I mean, I think a lot of what we've learned building, because a lot of what we've been building historically on desktop web apps
[1285.14 --> 1287.46]  has been mimicking desktop applications.
[1287.46 --> 1292.12]  You know, modal dialogues and grids and, you know, stuff like that.
[1292.18 --> 1295.46]  It doesn't make sense at all on a mobile device.
[1296.28 --> 1300.46]  Like, no one would ever use a grid on a mobile device.
[1300.54 --> 1301.02]  It's insane.
[1301.58 --> 1310.60]  So you kind of have to, like, sort of, you definitely have to rethink how you interact with information and how you display it.
[1312.74 --> 1314.62]  This is something I'm very excited about.
[1314.62 --> 1326.02]  I definitely want people to tackle this and release, you know, frameworks that try to think of, you know, new ways of interacting with this information
[1326.02 --> 1329.02]  and hopefully ways that aren't just copying what the iPhone is doing.
[1329.62 --> 1330.60]  One more question.
[1330.60 --> 1341.00]  There seems to be a lot of heat around templating in JavaScript these days with Mustache.js and you've got your own, you know, templating thoughts that you've put on your blog.
[1341.72 --> 1348.88]  What's your thoughts on templating and is it an idea that's here to stay now that we have JSON and we're passing data back and forth?
[1348.96 --> 1350.24]  Is it a new way of building web applications?
[1350.40 --> 1350.80]  What's your take?
[1350.80 --> 1352.74]  I definitely think there's a lot of potential.
[1352.94 --> 1361.02]  I mean, we just recently worked on a new templating module for jQuery core.
[1361.74 --> 1364.20]  And that's been good.
[1364.28 --> 1365.40]  People have really enjoyed that.
[1365.40 --> 1375.20]  And it sort of took some of the existing templating work that I had done, combined in some of the techniques from Mustache.js,
[1375.46 --> 1381.18]  and kind of come up with this new set of functionality that's really, I think, good and very usable.
[1382.22 --> 1383.50]  And people seem to like it.
[1383.64 --> 1383.78]  So, yeah.
[1384.00 --> 1384.32]  Cool.
[1384.38 --> 1385.02]  Thanks for joining us.
[1385.20 --> 1385.36]  Yeah.
[1385.40 --> 1385.90]  Thanks for having me.
[1385.90 --> 1395.28]  Thank you for listening to this edition of The Changelog.
[1396.34 --> 1403.06]  Point your browser to tale.thechangelog.com to find out what's going on right now in open source.
[1404.24 --> 1409.76]  Also, be sure to head to github.com forward slash explore to catch up on trending and feature repos,
[1409.86 --> 1412.82]  as well as the latest episodes of The Changelog.
[1415.90 --> 1445.88]  The Changelog.
[1445.90 --> 1448.80]  Before I lift your eyes.
[1448.90 --> 1450.34]  Bring it down.
