[0.00 --> 19.14]  Welcome to the Change Log episode 0.2.5.
[19.26 --> 20.30]  I'm Adam Stachowiak.
[20.46 --> 21.08]  And I'm Wendell.
[21.32 --> 23.46]  We cover what's fresh and new in the world of open source.
[23.72 --> 26.66]  If you found us on iTunes, we're also on the web at thechangelog.com.
[27.08 --> 27.90]  We're also up on GitHub.
[27.90 --> 32.48]  You can check out some training repos, some feature repos from our blog, as well as our audio podcasts.
[32.78 --> 35.82]  If you're on Twitter, you can check us out at changelogshow.
[36.04 --> 36.86]  Not the changelog.
[36.98 --> 37.88]  And I'm Adam Stach.
[38.02 --> 38.62]  And I'm Penguin.
[38.76 --> 40.42]  P-E-N-G-W-I-N-N.
[40.90 --> 44.54]  I had fun talking to Dmitry Baranovsky from RaphaelJS this week.
[44.96 --> 45.84]  That's quite the name, huh?
[46.00 --> 46.52]  It is.
[46.60 --> 50.74]  You know your name's long when Twitter truncates your name and you try to choose it as a screen name.
[51.08 --> 51.74]  Oh, man.
[51.74 --> 58.24]  Cool project from Dmitry, Raphael and its counterpart, Grafael, which I didn't get at first.
[58.38 --> 59.56]  I kept calling it G.
[59.64 --> 60.08]  Raphael.
[60.20 --> 62.24]  And he finally said, you know, Grafael.
[62.66 --> 63.32]  It's like, oh, yeah.
[63.76 --> 68.74]  Because when Raphael does, it's a cool graphics library for JavaScript.
[68.92 --> 70.98]  And Grafael does graphs based on that.
[71.50 --> 71.98]  Oh, wow.
[72.20 --> 72.80]  It's pretty cool.
[72.90 --> 78.46]  Some nice looking graphs that uses SVG under the hood instead of Canvas, which is kind of old school.
[78.46 --> 81.38]  But it's got some advantages, as Dmitry gets into.
[83.70 --> 87.82]  Speaking of JavaScript, we'll be at Texas JavaScript June 5th.
[87.94 --> 88.34]  That's right.
[88.38 --> 88.86]  Over in Austin.
[89.26 --> 90.04]  Yeah, I'm looking forward to that one.
[90.08 --> 90.92]  It's got quite the lineup.
[91.42 --> 92.94]  I mean, it's in our backyard we have to go, right?
[93.02 --> 94.34]  It's going to be a lot of fun.
[94.60 --> 97.48]  It's not quite JSConf, but hey, everything's bigger in Texas, right?
[97.88 --> 98.48]  That's true.
[98.60 --> 99.06]  That's true.
[100.16 --> 100.50]  Cool.
[100.66 --> 102.96]  Well, I bet you're ready to see what we talked about.
[103.42 --> 104.94]  Let's get to the episode, yes.
[105.74 --> 106.40]  Let's do it.
[108.46 --> 117.52]  All right.
[117.54 --> 120.40]  We're joined by Dmitry Baranovsky from Raphael.js.
[120.62 --> 123.86]  Dmitry, why don't you tell the folks who you are and a little bit about Raphael.
[124.04 --> 124.28]  Okay.
[125.30 --> 128.62]  I work as a software architect at AXTGS.
[129.48 --> 132.76]  And Raphael started my side project about two years ago.
[132.76 --> 139.14]  So it's pretty much an adapter for vector graphics on the web.
[139.80 --> 144.28]  So it's a JavaScript library to draw some extra stuff.
[144.28 --> 150.40]  So what sort of project were you creating when you created Raphael to solve the problem?
[151.60 --> 153.56]  There were no any projects.
[153.64 --> 157.04]  I just created as a side, you know.
[158.12 --> 158.86]  Just for fun?
[159.60 --> 160.64]  Yeah, just an experiment.
[161.14 --> 161.98]  I was playing around.
[161.98 --> 167.20]  I was creating, like, drawing stuff.
[167.38 --> 169.78]  It would be fun, you know, to draw something cross-browser.
[170.54 --> 178.66]  So, like, and I, you know, have been playing with SVG a long time ago, I don't know, in the year 2002 or something like that.
[178.66 --> 182.30]  And I was like, oh, I could use SVG now here, here, and there.
[183.08 --> 189.86]  And, you know, Explorer has VML, so maybe I could create function circle, which will draw a circle for me cross-browser.
[190.00 --> 190.44]  So I did.
[190.64 --> 193.48]  And, oh, now I could do this, now I could do that.
[194.10 --> 200.82]  And then I show it to my colleagues, especially to Lachlan Hardy, who heavily supported me.
[200.90 --> 202.20]  They're like, oh, dude, it's awesome.
[202.56 --> 204.22]  You should create a library from it.
[204.22 --> 209.92]  And I'm like, oh, sure, okay, well, you know, it still has lots of bugs and lots of things not covered.
[210.94 --> 219.12]  But because it has such a great support, I decided to actually release it after probably about two months working on it.
[219.94 --> 221.98]  I think it's ready to show it off.
[222.76 --> 230.94]  So that's a lot of work for a side project, especially to manage the, you know, cross-platform nature between SVG and VML.
[230.94 --> 238.32]  So did you set out to support VML for Internet Explorer out of the box, or did that come later?
[239.18 --> 251.02]  No, it was in the beginning because, you know, as a web developer, I feel like if I can't do this, whatever I'm doing cross-browser, then it's just a toy.
[251.26 --> 251.84]  It's not real.
[251.84 --> 262.84]  And if I will do something, okay, I can do, you know, draw these amazing things in Canvas, but it only works in Chrome, for example, then it's just a toy.
[263.10 --> 263.96]  Yeah, yeah, okay, good.
[264.30 --> 265.50]  Can you use it really somewhere?
[266.32 --> 266.64]  No.
[267.86 --> 268.30]  So.
[268.94 --> 279.92]  For the folks that might not, you know, understand, haven't dealt with graphics and JavaScript that much, explain the difference between Canvas and SVG and the different approaches.
[279.92 --> 280.56]  Right.
[281.90 --> 291.06]  So that's basically why I choose SVG instead of Canvas, because I had a choice of Canvas and SVG, and I could pick up anything.
[292.02 --> 305.76]  And I choose SVG because it's closer to VML, because in difference to Canvas, SVG allows you to create elements, just like any DOM elements, like you could create div and span, the same way you could create circle and rectangle.
[305.76 --> 309.88]  And then, you know, change the attributes.
[310.84 --> 313.70]  So in Canvas, you just separate with pixels.
[314.56 --> 320.38]  You create a model of circle, then you say paint this circle on Canvas, and you have just a bunch of pixels.
[320.52 --> 323.08]  You can't really take it back and update.
[323.54 --> 328.68]  You have to keep your model and basically redraw a circle if you want to make it, I don't know, red.
[328.68 --> 333.10]  You have to clean the canvas, draw it again with new shapes.
[333.68 --> 336.60]  And in the SVG, you actually operate with DOM elements.
[337.02 --> 345.38]  As a result, you could attach on click events to circles, on mouse hover to curves, or whatever else you could think about.
[346.32 --> 348.16]  And the VML is basically the same.
[348.26 --> 351.32]  The VML is historically a grandfather of SVG.
[351.32 --> 356.62]  So they share the same concept, it's only that VML has a terrible API.
[358.32 --> 359.34]  Just a terrible API.
[360.02 --> 366.32]  So recently, you released 1.4 of Rafael, and it includes touch event support.
[366.50 --> 372.04]  Was this just for fun, or did you have a need to take this project to the mobile platform?
[373.36 --> 380.04]  This already was not basically for fun, because I was doing another project for AXT.
[381.32 --> 387.14]  And it was like a small side project, but I need to have drag and drop in iPad.
[388.98 --> 397.42]  And, you know, I was writing just a code for this, because you could just write everything straight in JavaScript.
[398.20 --> 402.62]  And then I decided, well, it would be nice to have it actually as a part of the library, as soon as I'm writing it anyway.
[403.14 --> 406.74]  So I just included it into the library, make it more generic, make it nicer.
[407.88 --> 409.82]  And, yeah, and then just decided to release it.
[409.82 --> 415.96]  You've got one of the better demo pages for a lot of JavaScript plugins, or any plugins for that matter.
[416.50 --> 421.42]  Do you have any sort of design background, or how did you create such sexy charts?
[422.54 --> 428.90]  Well, I was a senior designer once in my career, but I quit this job because I hate to be a designer.
[429.00 --> 435.30]  It's very unthankful, because everybody has their opinion on everything, if it's about design.
[435.30 --> 438.96]  When it's about code, it's people less opinionated.
[440.26 --> 441.82]  You could create perfect code.
[442.62 --> 445.76]  I mean, imagine you wouldn't like to create a function which adds two numbers.
[446.22 --> 448.56]  I'm pretty sure you could write a code which is perfect.
[449.44 --> 449.70]  Right?
[449.70 --> 455.10]  When you need to draw a circle, then everybody thinks, oh, it's too big, it's too small.
[455.36 --> 456.44]  What color it should be?
[456.50 --> 457.54]  It should be black, it should be red.
[457.58 --> 458.30]  I like green.
[458.70 --> 460.72]  And it's such a nightmare.
[460.98 --> 462.78]  So I quit the design job.
[462.78 --> 468.34]  Because I like to code as well, so I just start more coding, less designing.
[469.28 --> 475.20]  And I obviously have lack of experience in design because of that, but that's okay.
[475.32 --> 483.76]  I have enough design knowledge to just roll up a site, which looks not ugly, and that's enough.
[483.76 --> 492.50]  So you were telling me earlier that the project, I guess, is a little over two years old now that the first release was on 808 of 8.
[493.84 --> 499.38]  When did the graphing component of G. Raphael begin?
[499.38 --> 516.76]  The graphing component began when I was doing some, well, I was working for Atlassian, and I was doing some charting solutions for the Fisher and Crucible product.
[517.54 --> 521.94]  I was, like a second man on this team, and I was doing the charting stuff.
[522.04 --> 526.10]  And I was about to do charting plugins for a long time, and I did some preparation.
[526.10 --> 531.28]  And this kind of kick off for me to actually do some real coding.
[532.14 --> 537.96]  So as a part of my work, I also was coding this charting solution, and I released it.
[539.04 --> 545.82]  I think it didn't end up to be in Crucible at the end, but now we have this charting thing.
[546.44 --> 553.74]  I hope to come back straight and actually work on it, because I really like it, and I didn't have time to write a presentation.
[553.74 --> 558.58]  I hope to the moment when this will be online, I will write something.
[559.14 --> 566.94]  But I try not to promise anything, because I'm just one guy with a family and day job.
[568.94 --> 570.78]  This is all side things.
[571.74 --> 573.40]  We should mention that you're in Australia.
[574.52 --> 582.50]  So what's it like running an open source project from the other side of the globe and listing users via Twitter and social media?
[582.50 --> 591.10]  Well, you know, it's like if you never experienced anything else, it's pretty much okay.
[591.60 --> 596.68]  So I wake up in the morning, I read the tweets, and then during the day nothing happening, I could just work.
[597.56 --> 601.24]  And then next day I have another tweet.
[601.24 --> 608.06]  I can't reply to people straight away, but, you know, it's not that bad.
[608.64 --> 611.10]  Not much difference to being in Australia.
[612.38 --> 613.46]  It's actually kind of annoying.
[613.82 --> 618.26]  You kind of have to be in Silicon Valley to do something.
[619.06 --> 620.64]  It's not much happening outside.
[622.00 --> 622.98]  And why not?
[623.02 --> 624.02]  It's just Internet, right?
[624.02 --> 624.62]  Sure.
[624.72 --> 627.64]  So it should be, like, possible to do it anyway.
[627.86 --> 634.36]  It's just for some reason everything is concentrated geographically in the U.S. and Silicon Valley in particular.
[636.60 --> 637.04]  Absolutely.
[637.64 --> 644.32]  You know, it seems like there's been a pattern of really sharp Rubyists that I've met in New South Wales even.
[644.68 --> 645.76]  And that's where you're located, right?
[645.76 --> 655.08]  Yeah, I know a couple of people from Ruby development, and they're pretty smart, and they're doing great things.
[655.42 --> 656.70]  And I don't know.
[657.38 --> 661.58]  It's like living in Australia is better than in the U.S., I'm pretty sure about that.
[662.14 --> 664.70]  Otherwise, I will move.
[665.38 --> 668.16]  But it's much better to live here.
[668.76 --> 675.66]  And I'm working currently for XTGS, and this is a company based in Silicon Valley, but I work remotely.
[676.76 --> 678.42]  Yeah, it works pretty good so far.
[678.80 --> 683.20]  Is JavaScript your primary language, or are you in other server platforms?
[684.02 --> 689.42]  No, JavaScript is my only language, which I name when people ask me what languages I know.
[689.42 --> 701.50]  Because, well, I know a bit of PHP, a bit of Ruby, a bit of XSL, but obviously HTML, CSS, but I never mentioned that.
[701.72 --> 702.90]  And just, yeah, I know JavaScript.
[702.90 --> 703.30]  That's it.
[703.52 --> 706.84]  Because JavaScript I know, the rest, I just have a quintess of language.
[707.54 --> 711.22]  I'm not really happy to be a PHP developer, for example.
[712.22 --> 713.36]  What about Node.js?
[713.62 --> 714.28]  Played with that, anything?
[715.18 --> 716.34]  Well, yeah, I played a bit.
[716.34 --> 720.76]  And I had a nice chat with Ryan on JSConf recently.
[721.72 --> 727.04]  It's a bit low level for me at the moment.
[728.42 --> 731.00]  Not in terms of language, but in terms of what you can do.
[731.00 --> 739.70]  Because I'm front-end with design exposure, not a front-end developer with back-end exposure as much.
[740.50 --> 745.88]  So Node.js looked for me just like, you know, it's great that I could write in a language I know.
[746.98 --> 748.16]  And that's pretty much it.
[748.96 --> 749.22]  Sure.
[750.22 --> 750.94]  You're kind of talking.
[751.58 --> 751.90]  I'm sorry.
[751.90 --> 758.72]  Yeah, I'm pretty sure there will be lots of things emerging in the Node.js, like lots of frameworks on top of it.
[759.10 --> 768.40]  And later or soon, I'm holding my hand on the pulse, and I'm pretty sure that I will encounter it again in my career anytime soon.
[768.40 --> 784.14]  Coming back to the client side for a moment, you're really pushing the envelope with both of these projects from an interactive standpoint of, you know, kind of what traditionally is a Flash or even Java space, right?
[784.18 --> 788.12]  But you're doing this in straight-up JavaScript and SVG.
[788.28 --> 792.94]  So what are the limits as you see them in doing this sort of thing in the browser?
[792.94 --> 798.88]  What sort of applications are still not quite available to the front-end JavaScript developer?
[800.52 --> 805.54]  Well, the limits are in the browser itself, so the performance is an issue.
[807.56 --> 814.60]  The SVG is not – I don't think there's a lot of work done by browser vendors on optimizing SVG at the moment.
[814.60 --> 824.28]  So, like, making it render faster, do things faster, because it obviously lags when you put a lot of objects in SVG.
[825.52 --> 833.26]  Because the page – like, in general, the page will, you know, run slowly if you put, like, 10,000 DOM elements on it.
[833.32 --> 835.16]  It will try to animate them at once.
[835.98 --> 839.94]  But it's not something which happens when you're building the web pages.
[839.94 --> 843.82]  But in case of SVG, in case of graphics, there's something which could happen.
[844.38 --> 846.12]  You could animate a lot of objects at once.
[846.34 --> 849.60]  But there's not much optimization done on the browser side.
[850.76 --> 851.74]  I heard about IE9.
[851.84 --> 854.48]  We're going to use some hardware acceleration for your rendering.
[854.72 --> 855.44]  That would be awesome.
[856.26 --> 858.04]  But that's, like, a future.
[860.92 --> 862.02]  That's pretty much it.
[862.02 --> 873.82]  Apart from that, as soon as HTML5 became a reality with video tag, with audio tag, with SVG full support, and ability to, you know, embed video inside SVG.
[874.16 --> 878.86]  Like, Opera does pretty good at this point in supporting the page standards.
[878.86 --> 889.92]  But, again, if all this became reality, if performance will have as a big hit as a JavaScript performance, for example.
[890.08 --> 895.98]  Like, recently, as you know, we have this whole – lots of big, fast JavaScript engines coming out.
[896.64 --> 897.98]  So – but that's not enough.
[899.50 --> 902.46]  JavaScript is fast, but DOM rendering is still quite slow.
[903.24 --> 905.32]  As soon as it will be faster, I don't know.
[905.42 --> 907.50]  There are, like, not much limits left.
[907.50 --> 916.96]  What's your favorite browser to work with from both a development standpoint and from a performance standpoint?
[917.90 --> 919.42]  Well, I work with Safari.
[919.76 --> 921.00]  That's my default browser.
[922.54 --> 925.40]  But that's, like, unusual choice, you know.
[926.76 --> 934.18]  I'm developing in Firefox most of the time because of Firebug, obviously.
[934.18 --> 942.44]  And basically I'm developing Safari and Firebug because Firebug has issues and Web Inspector has issues.
[942.58 --> 944.82]  But fortunately they have usually different issues.
[945.64 --> 948.62]  So you could kind of cover things with both.
[950.04 --> 952.64]  And, well, yeah, I'm testing other browsers.
[953.46 --> 956.00]  But I'm not really a fan of Chrome.
[956.96 --> 958.06]  I don't like it.
[958.66 --> 959.40]  It's personal.
[959.40 --> 964.42]  From a rendering aspect or from just a usability aspect?
[965.38 --> 966.72]  No, the rendering aspect is good.
[967.50 --> 970.16]  It just – I just don't like UI of it.
[970.78 --> 973.10]  But, you know, it's just me.
[973.42 --> 974.86]  I know everybody likes Chrome.
[975.26 --> 976.92]  Everybody I know likes Chrome.
[977.68 --> 979.28]  But me, I don't like Chrome.
[979.28 --> 989.16]  What level of debug support is available in both Firebug and the development inspector inside of the WebKit browsers for SVG?
[990.46 --> 992.86]  Well, the latest Firefox is pretty good.
[992.96 --> 995.38]  You could click on the circle to inspect element.
[995.56 --> 997.32]  It will give you the circle thing.
[998.02 --> 1001.50]  It doesn't – I think Firebug doesn't highlight it properly at the moment.
[1001.50 --> 1011.84]  While Safari highlights it, but it has bugs with a, you know, figure out where the bonding box of an element in case of SVG.
[1013.88 --> 1016.68]  But in general, yeah, it works pretty well.
[1016.84 --> 1017.78]  I mean, it's just a DOM.
[1017.92 --> 1019.06]  So you could open it up.
[1019.12 --> 1021.50]  You could change its coordinates and stuff.
[1021.74 --> 1023.70]  It's right in Firebug or Web Inspector.
[1023.70 --> 1030.92]  So regarding generic JavaScript debugging, it's, well, it's well-known things.
[1031.16 --> 1034.68]  It's pretty much average everywhere at the moment.
[1036.30 --> 1037.62]  So, yeah.
[1038.04 --> 1039.76]  Do you have a favorite JavaScript framework?
[1041.98 --> 1042.54]  Raphael?
[1044.22 --> 1045.90]  Outside of the graphics area.
[1046.80 --> 1050.76]  Yeah, well, I use jQuery if I need to do something quickly.
[1050.76 --> 1057.04]  But, well, I'm not a big fan of jQuery.
[1057.84 --> 1060.90]  I think it has some issues somewhere.
[1061.80 --> 1067.02]  Well, but, you know, I'm JavaScript developer and I know that this is a – everything has issues.
[1067.16 --> 1068.36]  And Raphael has lots of issues.
[1070.36 --> 1073.06]  I haven't seen perfect framework so far.
[1074.00 --> 1077.38]  So the thing about jQuery, it has very nice API.
[1077.38 --> 1084.38]  And if you use Raphael, you will notice I will just take this API and use it in Raphael.
[1085.26 --> 1087.04]  It's trying to make it as funky.
[1088.86 --> 1093.62]  In terms of possibilities if I need to develop web app, well, of course, I like XT.js.
[1093.86 --> 1095.38]  But, you know, I'm a bit based point.
[1099.44 --> 1100.98]  Yeah, that's pretty much it.
[1101.10 --> 1105.00]  I don't really look into other frameworks outside of it.
[1105.00 --> 1110.80]  You said you mentioned that this was created as a side project early on.
[1110.88 --> 1115.76]  Is it still just a side project or you got some items in production with this framework?
[1117.50 --> 1119.02]  It's still a side project.
[1119.44 --> 1122.90]  It's still just me working on it.
[1123.76 --> 1127.16]  So as soon as it's just one developer, you can't call it a serious project.
[1127.88 --> 1129.06]  It's still a side thing.
[1129.06 --> 1133.64]  But, you know, it's like my hobby.
[1134.22 --> 1135.12]  I'm patient about it.
[1135.24 --> 1141.66]  So, you know, when you're patient about something, it changes everything.
[1142.12 --> 1144.52]  It doesn't matter how many people go on it if you like it.
[1145.52 --> 1148.80]  Closing in on a thousand watchers on GitHub,
[1148.80 --> 1155.46]  how has the community for Rafael grown since you moved your code over to GitHub?
[1156.68 --> 1158.18]  Well, not much, I should say.
[1158.38 --> 1159.64]  Not as much as I expected.
[1159.88 --> 1162.14]  I know there are some people who like it.
[1163.02 --> 1165.54]  I know there are people who love it even.
[1166.76 --> 1170.76]  But I can't really see much contributions to the project.
[1170.76 --> 1176.12]  So I was hoping that, you know, I will release it on GitHub and people will say,
[1176.24 --> 1178.44]  like, hey, I found a bug and here's a patch for it.
[1178.78 --> 1181.56]  And it will happen, like, each week, at least once.
[1182.14 --> 1186.14]  I will lie if I will say nobody will ever submit any useful patch.
[1186.80 --> 1191.40]  But if there was, like, five, it's a good number.
[1192.20 --> 1193.42]  I think it was less than that.
[1194.08 --> 1198.76]  So lots of patches coming which are totally useless and people just...
[1198.76 --> 1202.64]  I could see some people just submitting the patch for sake of submitting a patch.
[1203.56 --> 1205.94]  And, you know, like, oh, I submit the patch to Rafael, yeah.
[1208.16 --> 1212.42]  But most of the time I reject them because they're useless.
[1213.06 --> 1216.84]  And if I like them, usually I rewrite them and not really a patch,
[1216.92 --> 1219.84]  but actually just fixing the bugs are my way
[1219.84 --> 1224.70]  because I'm quite picky about the code, especially in Rafael,
[1224.90 --> 1227.74]  because I want it to be perfect in my vision.
[1228.76 --> 1230.84]  Because it's the only place where I can do that.
[1232.92 --> 1237.02]  Everywhere you work, you have, you know, work-related standards
[1237.02 --> 1240.04]  and you could, you know, you should be able to write the code
[1240.04 --> 1242.66]  so the other developers in the team will understand it.
[1243.00 --> 1246.46]  In case of Rafael, I don't care much about understanding this by other developers
[1246.46 --> 1247.98]  as soon as I can understand it.
[1248.44 --> 1250.78]  So I'm pretty sure that in a year I could open it up
[1250.78 --> 1251.76]  and I could understand everything.
[1252.46 --> 1253.88]  So that's enough for me.
[1253.88 --> 1259.00]  Somebody else could not understand it, but that's not my problem really.
[1259.88 --> 1264.08]  And it also serves like, you know, a saving from, you know,
[1264.12 --> 1265.66]  having even more stupid patches.
[1266.52 --> 1269.58]  So most of, most of, well, I'm pretty sure a lot of people
[1269.58 --> 1272.14]  who just open code say, like, I don't even know how it works
[1272.14 --> 1272.82]  and close it up.
[1273.22 --> 1273.72]  And that's good.
[1273.72 --> 1277.86]  So they don't deserve to, you know, to be decent.
[1279.54 --> 1282.86]  Sort of a benevolent dictator there for your own project.
[1283.12 --> 1283.62]  That's a good thing.
[1283.98 --> 1285.18]  You should be a dictator.
[1285.28 --> 1287.30]  Otherwise, your project will die in vain.
[1287.30 --> 1291.26]  I'm, like, I'm very, very strong on it.
[1291.34 --> 1294.00]  And I have, like, run into some conflict with the guys
[1294.00 --> 1295.50]  who are telling me, hey, it's open source.
[1295.58 --> 1297.52]  Why I can't add this feature to it?
[1298.04 --> 1299.90]  And while it's open source means you can read it
[1299.90 --> 1303.98]  and doesn't mean you should, you're able to write anything you wish
[1303.98 --> 1305.88]  because otherwise it would be a mess and chaos
[1305.88 --> 1307.86]  because everybody has their opinion.
[1308.80 --> 1311.74]  And, you know, Rafael is an opinionated project
[1311.74 --> 1313.54]  as well as Graphael.
[1313.54 --> 1316.84]  I receive people complaining that Graphael,
[1317.10 --> 1318.42]  when you're creating a pie chart,
[1319.36 --> 1322.32]  you can't put more than 10 segments on a pie.
[1323.34 --> 1327.02]  And I say yes because I don't want you to create ugly charts
[1327.02 --> 1328.02]  with my library.
[1329.46 --> 1330.36]  I love it.
[1330.46 --> 1331.04]  I love it.
[1332.04 --> 1335.06]  Can't create ugly charts with my graphing library.
[1335.22 --> 1335.44]  Nice.
[1336.20 --> 1339.26]  Because people will create ugly things with Raphael.
[1339.34 --> 1340.42]  I'm pretty sure about that.
[1340.50 --> 1341.14]  I saw a couple.
[1341.14 --> 1343.94]  You can't prevent this from happening,
[1344.04 --> 1346.42]  but I can do as much as I can to prevent this from happening.
[1346.64 --> 1347.88]  Well, have you added that to your license
[1347.88 --> 1350.84]  that you can use this code as long as you don't create ugly pie charts?
[1351.60 --> 1353.06]  I should probably, yes.
[1353.28 --> 1355.88]  Well, I see about 10 plugins for Raphael.
[1356.22 --> 1358.52]  Do you have, like, an official plugin API
[1358.52 --> 1360.96]  or are these just extractions that you built along the way?
[1361.68 --> 1365.30]  Well, there is a plugin API for Raphael as well as jQuery has,
[1365.30 --> 1370.00]  so you could write Raphael.fm.methodname and put the function,
[1371.00 --> 1374.48]  or Raphael.el.methodname, put function on elements.
[1375.54 --> 1377.54]  So it's all documented.
[1378.00 --> 1378.52]  It's all official.
[1379.88 --> 1385.20]  I have a plan to create a plugin page in Raphael.js.com,
[1385.20 --> 1389.12]  so people could search for plugins and submit some plugins
[1389.12 --> 1391.46]  to some centralized location.
[1393.26 --> 1394.94]  Just a question of time.
[1396.18 --> 1396.94]  Because I have this plan.
[1397.04 --> 1399.10]  I know something which would be awesome to have.
[1399.84 --> 1402.82]  Just, you know, I have it on my to-do list,
[1403.16 --> 1404.78]  but not the next point.
[1404.78 --> 1408.82]  So I will do it eventually.
[1411.02 --> 1413.18]  I'm taking a peek inside of your test folder here
[1413.18 --> 1415.44]  to see if I could see a favorite testing framework,
[1415.54 --> 1417.60]  because testing JavaScript is always a challenge.
[1417.80 --> 1418.38]  Do you have one?
[1419.20 --> 1419.50]  No.
[1420.38 --> 1421.90]  I don't look at test folder.
[1421.98 --> 1422.66]  I should delete it.
[1424.62 --> 1426.48]  It's legacy folder.
[1426.90 --> 1430.28]  I created once, but it really I'm not using.
[1430.74 --> 1432.08]  Well, the thing is about Raphael,
[1432.08 --> 1435.50]  I still can't find a good solution to test the framework
[1435.50 --> 1436.84]  because it's so visual.
[1437.76 --> 1440.60]  And if you create a circle, for example,
[1440.60 --> 1443.18]  and you ask Dom, is circle there?
[1443.90 --> 1444.80]  Dom will say yes.
[1445.26 --> 1446.68]  But is circle actually looking good?
[1447.44 --> 1450.48]  Is it actually visible on the screen?
[1450.58 --> 1452.02]  Is it actually circle?
[1452.28 --> 1453.24]  Is it anti-alized?
[1453.40 --> 1454.76]  Is it like all these things?
[1454.88 --> 1458.70]  You can't really ask the code from this.
[1458.74 --> 1459.58]  You have to look at it.
[1460.04 --> 1460.84]  You make an animation.
[1460.96 --> 1462.04]  Is animation smooth?
[1462.08 --> 1467.18]  Is it really going the right path when you're doing the animation?
[1467.70 --> 1470.22]  Is it like there's so many things?
[1470.72 --> 1475.60]  Basically, I use like the demos on the page is pretty much my test.
[1476.64 --> 1480.32]  So I run the demos across all the browsers before each release,
[1480.88 --> 1485.92]  and they should work because they're kind of covering the whole aspects of Raphael
[1485.92 --> 1489.14]  because they were emerging as soon as I was adding new features.
[1489.30 --> 1490.72]  You could, you know, look at the demos.
[1490.84 --> 1492.64]  You could see how they're coming up.
[1493.04 --> 1494.88]  So as soon as I add new feature, I create a new demo,
[1494.96 --> 1496.22]  and I put the demo on the page.
[1497.50 --> 1501.08]  So each demo kind of tests for the new feature of the library.
[1501.08 --> 1504.94]  And running all the demos together will, you know,
[1504.94 --> 1507.04]  pretty much cover all the features library have.
[1508.46 --> 1512.10]  What's the variance between each browser out there?
[1512.18 --> 1516.76]  I know that, you know, there's subtleties in even the way that each browser renders fonts and things,
[1516.80 --> 1519.16]  and as a designer, that bugs me to no end.
[1519.16 --> 1520.82]  What about for SVG?
[1521.02 --> 1523.52]  Are there subtleties in a way a circle is drawn?
[1524.88 --> 1531.22]  Well, if you talk about SVG, then SVG-supported browser does things pretty good.
[1531.46 --> 1533.44]  I can't really spot the difference much.
[1534.16 --> 1538.64]  The VML has obviously its own way of drawing stuff.
[1538.64 --> 1545.34]  And, like, the biggest thing you will notice if you start using Raphael is
[1545.34 --> 1550.24]  if you draw a rectangle and stroke it with one pixel line,
[1551.10 --> 1553.52]  the line will be between two pixels.
[1553.72 --> 1555.88]  It wouldn't match to pixel grid in SVG
[1555.88 --> 1559.98]  because the middle of the line is laying between pixels.
[1560.30 --> 1564.00]  And when you make one pixel width of the line,
[1564.16 --> 1566.68]  you're trying to kind of draw it between pixels,
[1566.68 --> 1569.18]  so it actually looks like two-pixel line.
[1570.66 --> 1573.36]  You know, but grayed a bit because of anti-alizing.
[1574.06 --> 1579.22]  And the VML will try to match pixel grid to actually make it one pixel.
[1580.70 --> 1582.72]  And this is a small inconsistence.
[1582.84 --> 1585.18]  I don't really know how to fight.
[1586.28 --> 1588.76]  I was trying to do it before,
[1589.34 --> 1592.58]  and I just rolled it back, my changes, because it didn't work.
[1592.64 --> 1593.34]  People start complaining,
[1593.34 --> 1596.80]  hey, why are all my drawings shifted to half a pixel?
[1598.00 --> 1601.18]  Because I'm trying to emulate VML, but it's not always worked as well,
[1601.28 --> 1602.80]  so it's much more complicated,
[1603.02 --> 1605.96]  and maybe I will find a solution one day.
[1607.16 --> 1610.34]  But in case of VML, yeah, the rendering is quite different.
[1611.10 --> 1615.98]  The SVG-based browsers are pretty much rendering these things the same way.
[1615.98 --> 1621.34]  There are lots of inconsistency in support of features of SVG,
[1622.22 --> 1624.28]  like filters, for example,
[1624.74 --> 1627.14]  are not really well supported at the moment,
[1628.18 --> 1630.72]  like some other things.
[1630.92 --> 1633.80]  But generally, if you draw a circle or square,
[1634.72 --> 1640.12]  you wouldn't spot the difference between Safari and Firefox, for example.
[1640.12 --> 1644.76]  Well, to keep this episode commute-friendly for those folks
[1644.76 --> 1646.44]  that are listening on the way to the office,
[1647.08 --> 1648.84]  we'll need to wrap it up.
[1649.08 --> 1651.42]  And we do that at the end of each episode
[1651.42 --> 1654.32]  by asking our guests what's on their open-source radar.
[1654.48 --> 1656.04]  So are there any open-source projects
[1656.04 --> 1659.10]  that have you excited that you really want to play with
[1659.10 --> 1659.94]  that you haven't yet?
[1661.50 --> 1662.26]  All of them.
[1664.48 --> 1667.00]  And especially the ones I didn't find yet.
[1667.00 --> 1670.56]  Do you play mostly with just JavaScript?
[1671.60 --> 1673.56]  Well, mostly with JavaScript, yes.
[1675.44 --> 1679.56]  But I like to pick up something open-source
[1679.56 --> 1682.24]  and usually approach any open-source project.
[1683.62 --> 1684.96]  And then I dig into code,
[1685.08 --> 1686.34]  and then I sometimes say,
[1686.42 --> 1687.88]  oh, it's not actually as bad.
[1689.56 --> 1690.56]  What about templating?
[1690.72 --> 1691.78]  Something like Mustache.js
[1691.78 --> 1694.42]  or any of those templating frameworks?
[1694.42 --> 1698.52]  I have a discussion just yesterday about templating.
[1699.08 --> 1703.78]  And basically, for three years,
[1703.86 --> 1705.12]  I've worked as XSLT developer,
[1705.34 --> 1707.20]  which is basically templating Kai.
[1707.78 --> 1710.42]  And I have my very strong opinion
[1710.42 --> 1713.42]  that templates shouldn't have a logic inside.
[1715.32 --> 1715.98]  And that's like,
[1716.34 --> 1718.12]  we could discuss another 30 minutes on that.
[1718.40 --> 1719.78]  But just to be short,
[1720.54 --> 1722.60]  I'm pretty sure this is a disaster.
[1722.60 --> 1724.78]  So it's like a hole
[1724.78 --> 1726.70]  which is going to be bigger and bigger and bigger.
[1727.04 --> 1728.36]  As soon as you have some logic,
[1728.82 --> 1729.82]  it's like bad.
[1730.04 --> 1732.30]  And I suggested recently
[1732.30 --> 1733.86]  the templating mechanism,
[1734.54 --> 1737.20]  which is a very small framework,
[1737.54 --> 1739.24]  about 100 lines of code,
[1739.66 --> 1742.46]  which just used strings as a template,
[1742.68 --> 1744.88]  and all logics belong in JavaScript.
[1744.88 --> 1748.88]  which makes sense,
[1749.36 --> 1750.40]  because logic should be written
[1750.40 --> 1750.86]  in the language
[1750.86 --> 1752.62]  which was designed to write logic.
[1753.14 --> 1753.98]  And you don't need to know
[1753.98 --> 1755.48]  yet another language to do this.
[1756.12 --> 1757.68]  And there are lots and lots of things.
[1757.84 --> 1758.22]  And it's like,
[1758.58 --> 1759.26]  I know it's like,
[1759.66 --> 1761.42]  if I will blog about it,
[1761.46 --> 1762.80]  I will have like 10,000 comments
[1762.80 --> 1763.42]  that I'm an idiot.
[1763.98 --> 1766.22]  But I don't care.
[1766.22 --> 1769.14]  I know that I'm right.
[1769.46 --> 1771.12]  Because I was working with templates
[1771.12 --> 1774.20]  and I know that having logic
[1774.20 --> 1775.28]  is always a problem
[1775.28 --> 1776.74]  because people are trying to put there
[1776.74 --> 1777.60]  a lot of things,
[1777.86 --> 1779.42]  much more than templates should handle.
[1779.90 --> 1780.52]  And then you have,
[1781.16 --> 1781.58]  to read it,
[1781.64 --> 1783.52]  you have to have double parsing in your head.
[1783.78 --> 1785.72]  So you have to parse template
[1785.72 --> 1788.12]  into whatever HTML it generates,
[1788.20 --> 1788.66]  for example.
[1789.02 --> 1790.80]  And then you actually need to parse HTML
[1790.80 --> 1791.88]  to understand what it does.
[1791.88 --> 1793.36]  And that's like,
[1793.42 --> 1794.80]  double parsing is not really something
[1794.80 --> 1796.26]  we humans are doing well.
[1797.12 --> 1799.60]  So I am big, big, big,
[1800.02 --> 1800.52]  you know,
[1801.60 --> 1802.52]  on the point that
[1802.52 --> 1804.38]  templates shouldn't have logic inside.
[1804.70 --> 1806.12]  So should we look for a new
[1806.12 --> 1808.32]  tippling framework from Dimitri soon
[1808.32 --> 1809.66]  that has no logic built in?
[1810.36 --> 1812.00]  I wouldn't release this framework
[1812.00 --> 1813.74]  if I didn't expect
[1813.74 --> 1815.10]  that people will hate me for that
[1815.10 --> 1817.26]  and it wouldn't be ever popular at all.
[1817.50 --> 1818.54]  So I probably wouldn't.
[1819.98 --> 1820.74]  I could release it.
[1820.82 --> 1821.04]  It's like,
[1821.08 --> 1821.66]  it's already written.
[1821.66 --> 1822.32]  Like, I don't know.
[1823.02 --> 1823.52]  All together,
[1823.66 --> 1825.32]  it's 200 lines of code probably
[1825.32 --> 1826.00]  with examples.
[1826.82 --> 1826.96]  So,
[1827.64 --> 1829.40]  but I don't think it's something
[1829.40 --> 1829.72]  which,
[1830.06 --> 1830.38]  you know,
[1830.40 --> 1831.30]  people will appreciate.
[1832.36 --> 1832.80]  Well,
[1832.86 --> 1833.64]  throw it out there
[1833.64 --> 1835.20]  and then when people fork it,
[1835.26 --> 1836.34]  then you don't have to accept
[1836.34 --> 1837.06]  the patches, right?
[1838.68 --> 1839.08]  Yeah.
[1841.60 --> 1842.28]  We'll see.
[1842.48 --> 1843.38]  It's not a project
[1843.38 --> 1844.78]  that you need to support then.
[1844.90 --> 1845.36]  And, you know,
[1845.40 --> 1847.74]  I have problems with Graphel.
[1848.06 --> 1849.12]  I was trying to find
[1849.12 --> 1850.64]  somebody who will,
[1850.64 --> 1850.92]  you know,
[1850.92 --> 1851.38]  support,
[1851.58 --> 1852.06]  just, you know,
[1852.10 --> 1852.98]  hold the Graphel.
[1853.16 --> 1854.20]  I was tweeting like,
[1854.28 --> 1854.40]  hey,
[1854.46 --> 1855.88]  who want to own Graphel?
[1855.98 --> 1857.08]  I gave it to you for free.
[1857.76 --> 1858.00]  And nobody,
[1859.36 --> 1859.66]  you know,
[1859.72 --> 1860.44]  and people replied,
[1860.56 --> 1860.70]  yeah,
[1860.76 --> 1861.16]  I can.
[1861.32 --> 1861.66]  Okay,
[1861.90 --> 1863.34]  could you write documentation for it?
[1863.34 --> 1864.20]  And,
[1864.28 --> 1864.80]  yeah,
[1864.92 --> 1866.08]  maybe next year.
[1866.28 --> 1866.44]  Yeah,
[1866.64 --> 1866.84]  so,
[1867.02 --> 1868.40]  nobody did.
[1869.10 --> 1869.28]  So,
[1869.42 --> 1870.20]  okay,
[1870.74 --> 1871.90]  I have to do things myself
[1871.90 --> 1873.06]  if I want to do this proper.
[1874.16 --> 1874.38]  So,
[1874.48 --> 1875.86]  I will work on documentation.
[1878.48 --> 1880.54]  Free framework to good home
[1880.54 --> 1881.32]  and documentation.
[1881.74 --> 1882.50]  Thanks for joining us,
[1882.54 --> 1882.84]  Dimitri.
[1882.96 --> 1884.08]  Thanks for taking time out of
[1884.08 --> 1885.18]  your lunch hour over there
[1885.18 --> 1886.84]  and sitting down with us.
[1887.80 --> 1888.28]  Thank you.
[1894.42 --> 1895.60]  Thank you for listening
[1895.60 --> 1897.34]  to this edition of the Change Log.
[1898.48 --> 1899.82]  Point your browser to
[1899.82 --> 1902.02]  tail.thechangelog.com
[1902.02 --> 1903.16]  to find out what's going on
[1903.16 --> 1903.90]  right now
[1903.90 --> 1905.14]  in open source.
[1906.48 --> 1906.82]  Also,
[1906.90 --> 1907.56]  be sure to head to
[1907.56 --> 1908.52]  github.com
[1908.52 --> 1909.60]  forward slash explore
[1909.60 --> 1910.70]  to catch up on trending
[1910.70 --> 1911.84]  and feature repos
[1911.84 --> 1913.48]  as well as the latest episodes
[1913.48 --> 1914.88]  of the Change Log.
[1914.88 --> 1919.68]  Safe in your arms
[1919.68 --> 1923.34]  As a dark passion show
[1923.34 --> 1927.78]  Was mine alone
[1927.78 --> 1930.30]  Open,
[1931.64 --> 1933.46]  Open
[1933.46 --> 1937.76]  For us to try
[1937.76 --> 1939.40]  Bring it back,
[1939.58 --> 1941.26]  bring it back to
[1941.26 --> 1943.26]  Open
[1943.26 --> 1945.74]  Freedom
[1945.74 --> 1952.22] aries
[1952.72 --> 1953.10] んで
[1953.10 --> 1953.74] 日本 Chief
[1953.74 --> 1955.40]  heure
[1955.40 --> 1957.86] 下
[1957.86 --> 1961.78] 하�
