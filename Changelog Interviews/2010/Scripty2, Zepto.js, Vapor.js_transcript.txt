[0.00 --> 18.98]  Welcome to the ChangeLog episode 0.3.9.
[19.14 --> 20.18]  I'm Adam Stachowiak.
[20.50 --> 21.16]  And I'm Wendell.
[21.36 --> 22.56]  This is the ChangeLog.
[22.64 --> 24.64]  We cover what's fresh and new in the world of open source.
[25.00 --> 27.98]  If you found us on iTunes, we're also on the web at thechangelog.com.
[28.26 --> 29.04]  We're also on GitHub.
[29.04 --> 32.44]  Head to github.com slash explore.
[32.58 --> 35.24]  You'll find some training repos, some feature repos from our blog,
[35.28 --> 37.50]  as well as the audio podcast for your listening pleasure.
[37.94 --> 40.44]  If you're on the Twitter, follow ChangeLogShow.
[40.60 --> 41.36]  Not the ChangeLog.
[41.40 --> 42.18]  He's pretty cool, too.
[42.70 --> 43.80]  And I'm Adam Stach.
[44.12 --> 44.72]  And I'm Penguin.
[44.88 --> 46.58]  P-E-N-G-W-Y-N-N.
[47.28 --> 48.32]  Fun episode this week.
[48.40 --> 52.56]  Finally getting to air our conversation with Thomas Fuchs from Scripty2,
[52.72 --> 56.08]  Scriptaculous, Zepto, Vapor.js, all things JavaScript.
[56.08 --> 60.54]  Yeah, this Vapor.js framework is really, really awesome.
[61.14 --> 63.52]  Yeah, it's like the Uber JavaScript framework,
[63.76 --> 67.28]  and it's the lightest weight JavaScript framework that you'll ever find.
[67.54 --> 69.32]  It's been forked how many times now?
[69.98 --> 71.62]  I don't know, upwards of 300, I guess.
[71.96 --> 73.18]  And it's got support for everything?
[74.28 --> 74.72]  Everything.
[74.72 --> 77.42]  And we also have you back from the U.K.
[77.82 --> 81.62]  I am back stateside after seven days over in the U.K.,
[81.62 --> 84.54]  taking my life into my own hands,
[84.64 --> 87.90]  riding with a buddy that was driving on the wrong side of the road the whole time.
[88.40 --> 94.52]  So plenty of flashbacks to European vacation when he goes around the roundabout.
[95.26 --> 97.98]  I saw that video you post on the roundabout, too.
[98.32 --> 101.40]  Yeah, that magic roundabout, you know, that's the five-way roundabout.
[101.40 --> 105.36]  You know it's magic when the actual street sign says,
[105.50 --> 106.44]  the magic roundabout.
[107.94 --> 109.76]  I was pretty lost just watching the video.
[109.94 --> 110.78]  I didn't know where they were going.
[111.40 --> 114.92]  I have no idea how those guys do not have more traffic accidents than they do.
[115.26 --> 116.08]  I was certainly amazed.
[116.20 --> 118.08]  Insurance rates should be so high over there, for sure.
[118.52 --> 118.94]  Oh, I know.
[118.94 --> 119.40]  They probably aren't.
[119.54 --> 121.66]  I guess the only saving grace is the cars are so small
[121.66 --> 123.68]  that it's easier to dodge each other.
[124.04 --> 124.80]  That's probably it.
[124.80 --> 126.00]  That's probably why they get away with it.
[126.00 --> 128.04]  So I love the country.
[128.34 --> 131.70]  Not so much sold on some of the products they sell over there,
[131.84 --> 133.58]  like pourable yogurt.
[133.84 --> 136.90]  This is what, you know, I guess is popular to pour on cereal and stuff.
[137.18 --> 139.78]  So not exactly sold on that one.
[140.10 --> 142.98]  And the internets are quite dodgy for the Wi-Fi.
[143.22 --> 147.14]  But other than that, on my first time in the U.K., I really, really liked it.
[147.14 --> 149.00]  And you got the U.K. badge in Foursquare.
[149.08 --> 150.94]  Or not Foursquare, because you're anti-Foursquare.
[151.04 --> 152.20]  You're a Gowalla fan, right?
[152.24 --> 153.44]  So you got that U.K. badge.
[153.60 --> 154.40]  I'm such a geek.
[154.54 --> 157.16]  I, you know, probably paid out the wazoo on the data plan
[157.16 --> 159.58]  to do a Gowalla check-in at Stonehenge.
[159.92 --> 162.40]  It's a shame how hard I'm laughing inside to know that, too,
[162.44 --> 164.86]  because we've been on road trips and we've had to stop places
[164.86 --> 166.20]  just so you can get a check-in going on.
[166.44 --> 166.86]  I know.
[167.20 --> 168.82]  It's just, it's who I am.
[169.02 --> 169.60]  That's who you are.
[169.64 --> 170.44]  Well, we love you anyways.
[170.86 --> 172.94]  We're happy, extremely happy to have you back.
[172.94 --> 175.44]  So glad you made it back safe, and I'm glad you had fun.
[175.86 --> 176.30]  Had a ball.
[177.02 --> 177.76]  Fun episode this week.
[177.80 --> 178.32]  Should we get to it?
[178.46 --> 179.04]  Let's do it, man.
[188.00 --> 190.92]  Hi, we're joined today by Thomas Fuchs from Scriptaculous fame.
[191.46 --> 192.72]  Thomas, for the folks that don't know,
[193.00 --> 195.24]  why don't you introduce yourself and let them know who you are.
[195.76 --> 197.04]  Hello, I'm Thomas.
[197.30 --> 199.12]  Thomas Fuchs, rhymes with books.
[199.12 --> 205.02]  I am the author of the Scriptaculous JavaScript framework,
[205.02 --> 213.48]  which originated in the Ruby on Rails sphere about five years ago,
[214.00 --> 215.56]  together with Prototype.js.
[216.04 --> 219.94]  And at that time, I also was a core team member of Ruby on Rails.
[220.28 --> 222.76]  And I'm no longer a core team member,
[222.92 --> 224.46]  but I'm still doing a lot of JavaScript.
[225.66 --> 229.18]  And I guess I'm here in the show today to talk about that.
[229.18 --> 232.28]  Yeah, we want to talk about Scripty2.
[232.42 --> 235.24]  Give us the lowdown on the next evolution of Scriptaculous.
[235.74 --> 240.26]  Yeah, so Scripty2, it's the most important thing about it.
[240.32 --> 241.64]  It's very slow in the making,
[241.64 --> 249.26]  but we like to take our time and only implement stuff that we actually use on real-world projects.
[249.62 --> 256.34]  We don't want to implement really big, widget-y frameworks that no one actually uses for code.
[257.06 --> 260.80]  So sometimes it's coming low very slowly.
[261.36 --> 264.24]  But anyway, it's a complete rewrite of Scriptaculous.
[264.24 --> 270.06]  And if you use Scriptaculous, you know that the central part of this is the effects framework.
[270.34 --> 274.04]  And that's been completely rewritten to take advantage of things like prototypes,
[274.86 --> 276.70]  custom events, and stuff like that.
[277.38 --> 282.46]  And it's written for extensibility and easy-to-read code.
[282.64 --> 287.92]  It's a bit more for both than other code I write and other projects I have.
[287.92 --> 293.30]  But it's there for you to take and extend and mess around with.
[293.76 --> 296.82]  And it also has really, really good documentation,
[296.82 --> 300.56]  because this was something that was bugging me from the first version of Scriptaculous,
[301.00 --> 304.54]  where we had a wiki, and then the wiki got shut down,
[304.66 --> 307.82]  and then the wiki, we put it on someone else's service,
[308.18 --> 309.72]  and then the service was abandoned.
[310.06 --> 311.86]  And, you know, it was quite crazy.
[311.86 --> 317.96]  But, yeah, the main focus of Script2 is a completely new effects framework
[317.96 --> 321.96]  with a modern one using modern JavaScript techniques.
[322.60 --> 323.74]  Very extensible.
[325.06 --> 328.16]  It's also usable for things that are not DOM nodes only.
[328.72 --> 331.80]  So not only CSS-based animation, but you can use it for,
[332.42 --> 337.38]  example, you can tie it into Raphael.js and use it for SVG-based animations.
[337.38 --> 342.44]  Or you can do animations on canvas with it if you extend it in the proper way.
[342.90 --> 349.44]  But the basis of it is just a timing and a queuing framework for visual effects.
[350.94 --> 353.46]  So still built on top of Prototype.js, right?
[353.48 --> 356.40]  Yes, it still works on top of Prototype.js.
[357.14 --> 359.54]  So a question from Twitter, Johnson Page asks,
[359.88 --> 362.10]  what's the future of Prototype, in your opinion?
[362.10 --> 368.00]  With Prototype, we have some of the same issues where it's going quite slowly.
[368.22 --> 369.54]  However, it works very well.
[369.66 --> 371.90]  I use it in all of my projects, basically.
[372.30 --> 373.50]  It still works fine.
[374.34 --> 378.88]  We actually just released release candidate 3 of Prototype 1.7,
[380.36 --> 381.34]  or 1.7 and 1.
[382.20 --> 386.16]  And that brings us IE9 compatibility,
[386.16 --> 393.50]  because IE9 now comes with a finally DOM-compatible events framework.
[393.72 --> 397.06]  That's the most important part about it for Prototype.js.
[397.18 --> 398.52]  So it's going along.
[399.00 --> 404.46]  We are still planning to release a Prototype 2.0 at some point.
[404.64 --> 407.60]  Of course, no roadmap or no time on that or date.
[407.60 --> 415.86]  But the main thing about Prototype 2.0 will be that we're moving away from a prototype extension
[415.86 --> 418.10]  for anything that's DOM-related,
[418.34 --> 424.54]  because that has proven to be a bit brittle in the past and very hard to maintain.
[424.74 --> 428.88]  It works, but it comes with a lot of disadvantages.
[428.88 --> 434.50]  So we are moving to something where we will no longer extend DOM nodes.
[434.50 --> 439.48]  But Prototype 2.0, for that reason, will break some compatibility with Prototype 1.0.
[440.10 --> 443.58]  But I think, actually, for Prototype,
[443.86 --> 448.10]  the most important part in Prototype is not so much the DOM stuff,
[448.30 --> 450.06]  but the language stuff.
[450.18 --> 451.62]  This is where Prototype really shines.
[452.02 --> 454.42]  If you have to do any sort of data munching
[454.42 --> 458.72]  or manipulate JavaScript stuff,
[458.96 --> 460.38]  you want a real class system,
[460.50 --> 462.68]  then Prototype is a really good choice.
[462.68 --> 467.10]  It really allows you to write really, really solid JavaScript,
[467.86 --> 469.68]  especially if you come from Ruby,
[469.82 --> 472.84]  because then you feel right at home in Prototype.js.
[473.74 --> 476.30]  You know, I was singing the praises of underscore.js the other day.
[476.38 --> 479.20]  It's the framework that adds a lot of those features
[479.20 --> 482.38]  kind of based on a jQuery model,
[482.60 --> 484.44]  and some guys kind of snickered and said,
[484.50 --> 485.82]  you know, we've had that in Prototype for years.
[485.82 --> 488.06]  Yes. If you go to the underscore website,
[488.16 --> 490.48]  it actually says it's an extraction from Prototype.js.
[491.14 --> 494.48]  So it's, yeah, it's pretty great.
[494.62 --> 496.82]  If you're using something else like jQuery
[496.82 --> 498.72]  or whatever other framework,
[498.78 --> 501.24]  and you want something for, like, data manipulation,
[501.44 --> 505.00]  and especially doing stuff with data in arrays,
[505.00 --> 507.18]  and, you know, you get some JSON data in,
[507.26 --> 509.56]  but you need to reformat it for something else,
[510.16 --> 512.10]  then underscore.js is a really good choice.
[512.30 --> 514.42]  Or, of course, if you're using Prototype.js,
[514.52 --> 516.14]  you get all this sweetness, like,
[516.38 --> 517.62]  built in right into your framework.
[518.16 --> 519.74]  So we've got a pretty young audience,
[519.96 --> 520.92]  and it's hard to believe.
[521.10 --> 523.50]  We have a whole crop of web developers these days
[523.50 --> 527.24]  that have known nothing different than Prototype and jQuery.
[527.24 --> 530.74]  Talk a bit about the world before JavaScript frameworks
[530.74 --> 533.28]  and what it was like building JavaScript in the browser
[533.28 --> 536.56]  with IE and Netscape.
[536.78 --> 538.62]  Yeah, the so-called dark ages.
[538.62 --> 539.62]  Right.
[540.98 --> 545.42]  So before Prototype was really the first,
[545.42 --> 548.40]  like, JavaScript framework
[548.40 --> 550.92]  that actually bundled a lot of functionality
[550.92 --> 552.66]  that before that you would find,
[552.74 --> 556.72]  like, very diverse spots on the Internet.
[556.96 --> 559.14]  You know, of course there were just those sites
[559.14 --> 561.58]  where you could download stupid things
[561.58 --> 563.72]  like mouse trail scripts and stuff like that,
[563.82 --> 567.92]  or the scripts that would run some sort of marquee
[567.92 --> 570.42]  in your status bar and that sort of thing.
[571.62 --> 575.88]  But, like, good quality JavaScript was really hard to find
[575.88 --> 580.36]  because lots of people just thought it was this toy language
[580.36 --> 582.92]  and it's not really widely supported anyway,
[583.08 --> 585.58]  which was probably true at that point.
[585.58 --> 597.62]  So my first real adventures with JavaScript began when Internet Explorer 4 came out.
[597.62 --> 600.78]  And that was the first browser, actually,
[600.78 --> 605.46]  that was, like, JavaScript, like, DOM.
[605.62 --> 606.62]  I wouldn't call it DOM.
[606.74 --> 607.70]  It wasn't really DOM.
[607.82 --> 609.60]  It was, like, IE's version of DOM.
[609.74 --> 611.54]  But that was actually really usable
[611.54 --> 614.90]  to make, like, highly interactive apps and sites.
[615.14 --> 616.04]  And at that point,
[616.58 --> 619.62]  it was certainly the most advanced web browser available.
[619.62 --> 624.90]  Of course, it was very limited from what we have today.
[625.36 --> 627.46]  And it was IE only and so on.
[627.50 --> 630.06]  So it wasn't really usable on the web
[630.06 --> 634.04]  because most people used Netscape at that point.
[635.06 --> 640.00]  But for applications that were, like, used internally or something,
[640.14 --> 641.66]  it was a great choice to use that.
[641.72 --> 644.10]  It was actually, in some ways,
[644.10 --> 649.18]  much more rapid to develop stuff with Internet Explorer
[649.18 --> 652.82]  than to use any, like, sort of desktop-based native applications
[652.82 --> 654.66]  for lots of types of applications.
[655.58 --> 658.42]  So this is, I think, where it all started.
[658.90 --> 662.92]  And JavaScript, at that point,
[663.00 --> 665.72]  wasn't really much different from the JavaScript we use today.
[666.08 --> 670.18]  JavaScript 1.5 has been out for ages.
[670.86 --> 672.58]  And JavaScript 1.3 before that,
[672.58 --> 674.66]  there's not so much difference between those languages.
[674.66 --> 681.90]  So you could have done a framework like jQuery or Prototype
[681.90 --> 685.42]  at that point in time, like, I don't know, 10 years ago.
[686.20 --> 689.66]  Have these frameworks dumbed down the average JavaScript developer?
[690.46 --> 691.70]  That is a really good question.
[691.88 --> 696.16]  I don't think that they dumbed down the existing JavaScript developers,
[696.36 --> 702.52]  but they certainly allowed in people that aren't really developers
[702.52 --> 707.46]  so it's a twofold thing, you know.
[707.66 --> 709.68]  It's good that the language gets more developers,
[710.18 --> 712.72]  but at the other hand, some of the frameworks,
[713.84 --> 715.34]  I think especially jQuery,
[715.84 --> 721.52]  have such a low level of...
[724.52 --> 725.60]  Barrier to entry?
[726.28 --> 727.88]  Yeah, barrier to entry, right?
[727.88 --> 731.48]  That you get people that are not programmers or not developers,
[731.74 --> 733.16]  and they think they can develop.
[733.48 --> 737.00]  And you have to be very careful in that regard.
[737.12 --> 739.52]  You have to teach those people
[739.52 --> 742.34]  that they're actually dealing with a real language there.
[742.60 --> 746.20]  And there's really a complete language there.
[746.28 --> 747.26]  It's not only jQuery.
[747.26 --> 751.18]  You get a complete object-oriented,
[751.54 --> 755.02]  really, really nice scripting language there.
[755.24 --> 758.74]  And I think one thing today that is a problem
[758.74 --> 762.24]  is that no one really reaches those people
[762.24 --> 764.60]  and teaches them how to actually program.
[764.80 --> 767.92]  And that leads to a lot of bad codes in the end, I think.
[767.92 --> 771.92]  You know, one of the things that I found rewarding
[771.92 --> 774.48]  is stepping out of the JavaScript frameworks
[774.48 --> 776.02]  and out of the least common denominator,
[776.24 --> 778.26]  you know, kind of facade we put
[778.26 --> 779.70]  across the browser differences.
[780.08 --> 782.92]  And if you target a certain mobile browser
[782.92 --> 784.52]  like WebKit or something on the iPhone,
[784.64 --> 786.80]  it really frees you to use
[786.80 --> 788.84]  the latest features of JavaScript.
[789.72 --> 790.88]  Yes, indeed.
[791.06 --> 792.04]  It's pretty awesome.
[792.16 --> 794.74]  But I would even step back from that.
[794.74 --> 795.68]  And I would recommend,
[796.02 --> 797.66]  like just sometimes for some projects,
[797.66 --> 799.20]  just use pure JavaScript.
[800.42 --> 802.10]  If you have a little side project or something,
[802.20 --> 802.66]  try that.
[802.98 --> 805.88]  It's actually not that hard to write JavaScript code
[805.88 --> 808.70]  that even works cross-browser in desktop browsers.
[810.74 --> 813.28]  But as I say, WebKit is actually,
[815.06 --> 817.50]  I wouldn't even say WebKit on the iPhone
[817.50 --> 820.50]  is very special as a special browser.
[820.80 --> 825.14]  I would say WebKit is on most mobile browsers, actually,
[825.14 --> 828.48]  except for anything that's named Windows.
[829.48 --> 833.66]  So if you can target a framework for mobile WebKit browsers
[833.66 --> 838.22]  that will allow you to very, very easily replicate
[838.22 --> 840.80]  any like bigger framework on the desktop,
[841.08 --> 842.22]  any bigger frameworks API,
[842.90 --> 845.10]  with very, very few lines of code.
[845.20 --> 847.66]  And I just released something called SEPTO.
[847.66 --> 849.40]  I mean, released.
[849.70 --> 852.64]  It's still in like, it's alpha stages, baby stages.
[853.18 --> 854.22]  But you can still write,
[854.30 --> 857.50]  you can write like jQuery-like code
[857.50 --> 859.58]  that just works on mobile WebKit browsers
[859.58 --> 861.08]  and desktop WebKit browsers.
[861.52 --> 864.36]  And the whole framework is like 2K compressed,
[864.82 --> 867.98]  which is like a tenfold improvement on size
[867.98 --> 869.92]  over jQuery proper.
[870.66 --> 871.86]  It's been well received.
[872.06 --> 874.20]  So I guess the fundamental difference here
[874.20 --> 875.78]  is SEPTO is kind of meant to be inlined
[875.78 --> 877.44]  instead of externally referenced.
[877.96 --> 879.70]  Yes, that's one of the ideas.
[880.10 --> 882.42]  I'm not quite sure if it's actually feasible
[882.42 --> 884.02]  because I think it will end up
[884.02 --> 887.10]  with a little bit more than 2K of code,
[887.26 --> 888.60]  more like 3 to 4K,
[888.78 --> 891.44]  which is like two screenfuls maybe.
[892.84 --> 895.80]  But you can take the core of SEPTO
[895.80 --> 896.80]  and just inline it
[896.80 --> 898.92]  if you have like a one-pager application
[898.92 --> 900.96]  because that will make the loading
[900.96 --> 903.52]  of your application really fast.
[903.52 --> 906.56]  Like say you have like an application
[906.56 --> 909.32]  that kind of mimics a native application
[909.32 --> 910.50]  doing some task,
[910.76 --> 911.94]  specifically some task,
[912.04 --> 913.74]  and it also works offline
[913.74 --> 917.24]  and it uses local storage of some sort.
[918.28 --> 920.32]  Then SEPTO is probably a really good choice
[920.32 --> 925.02]  because the user can practically instantly load it
[925.02 --> 926.96]  because it's so small from the code size.
[927.60 --> 928.90]  And then you go ahead
[928.90 --> 930.16]  and like load in your data
[930.16 --> 931.38]  and whatever, store it locally.
[931.38 --> 934.30]  And from that on, people will be able to use it.
[935.06 --> 938.82]  So the main idea behind it was,
[939.70 --> 941.80]  like it was born
[941.80 --> 945.38]  when we did a site called everytimezone.com
[946.18 --> 950.96]  as like an ad for our time tracking software Freckle.
[951.50 --> 953.16]  We use that quite extensively
[953.16 --> 954.74]  in the changelog to schedule interviews.
[954.94 --> 955.24]  Awesome.
[955.60 --> 956.12]  That's great.
[956.22 --> 956.68]  It's good to hear.
[956.68 --> 961.34]  So that site is a single HTML file.
[961.78 --> 964.14]  It uses, I think, one image,
[964.26 --> 965.24]  which is the ad.
[965.70 --> 967.50]  It doesn't use any other images
[967.50 --> 969.22]  or external CSS files
[969.22 --> 971.16]  or external JavaScript files.
[971.26 --> 972.62]  So if you go to everytimezone.com
[972.62 --> 973.96]  in a desktop browser
[973.96 --> 974.90]  and look at the source,
[975.30 --> 977.22]  everything that's on the site
[977.22 --> 979.34]  is right there in the source.
[979.62 --> 980.68]  The CSS is inlined.
[981.20 --> 982.30]  The JavaScript is inlined.
[982.30 --> 985.20]  And it uses some sort of like early ancestor
[985.20 --> 987.34]  of the idea for SEPTO,
[987.80 --> 991.86]  like my ultra mini Pico tiny framework,
[992.12 --> 993.66]  which was basically five lines of codes,
[993.84 --> 995.16]  like a dollar function,
[995.70 --> 997.22]  a function to set the inner HTML,
[997.42 --> 998.40]  a function to set CSS.
[999.48 --> 1000.72]  That's basically it.
[1001.76 --> 1003.86]  And it was born there
[1003.86 --> 1004.72]  because I could see,
[1005.02 --> 1006.90]  okay, you can make a complete application
[1006.90 --> 1010.54]  with really like only like a few separate functions.
[1010.54 --> 1013.08]  And if you spin the idea further,
[1013.44 --> 1017.38]  if you use all the new and modern API calls
[1017.38 --> 1021.08]  and JavaScript API calls
[1021.08 --> 1022.14]  and DOM API calls
[1022.14 --> 1024.68]  in the mobile WebKit browsers,
[1025.00 --> 1027.96]  then you could really massively save
[1027.96 --> 1028.74]  on lines of code
[1028.74 --> 1031.44]  while still providing a very, very useful API.
[1031.76 --> 1032.74]  And in SEPTO's case,
[1032.82 --> 1035.72]  it's basically the complete core
[1035.72 --> 1037.54]  jQuery API that it provides.
[1037.54 --> 1039.80]  You have a blog post on
[1039.80 --> 1042.54]  when you ported this to the iPad
[1042.54 --> 1044.44]  and some of the considerations for that
[1044.44 --> 1045.20]  I found fascinating.
[1045.32 --> 1047.78]  So talk a bit about considerations for images
[1047.78 --> 1050.60]  and CSS3 and Canvas for a moment.
[1051.34 --> 1051.50]  Yeah.
[1052.12 --> 1055.42]  So CSS3 is pretty interesting
[1055.42 --> 1058.04]  because it allows you to use other things
[1058.04 --> 1060.28]  than image files for backgrounds.
[1061.02 --> 1062.52]  You can use gradients,
[1063.04 --> 1063.98]  CSS gradients.
[1063.98 --> 1067.18]  You could even use canvas elements
[1067.18 --> 1068.94]  as image backgrounds
[1068.94 --> 1070.68]  that you then can script from JavaScript.
[1072.58 --> 1073.76]  And the thing is,
[1074.74 --> 1075.78]  on mobile devices,
[1076.04 --> 1078.48]  specifically the iOS devices,
[1080.42 --> 1082.10]  the web browser is basically,
[1082.50 --> 1083.96]  it doesn't have much to do
[1083.96 --> 1085.64]  with like a traditional web browser
[1085.64 --> 1086.42]  as you think of it.
[1086.78 --> 1090.26]  It's more like a high-performance 3D game engine.
[1090.26 --> 1093.40]  The elements on your page
[1093.40 --> 1095.90]  are actually textures in 3D space.
[1097.06 --> 1098.94]  And in my blog post,
[1099.24 --> 1100.74]  I don't like,
[1101.56 --> 1103.26]  I didn't explain it that way in the blog post,
[1103.34 --> 1105.36]  but it basically works out like this.
[1105.42 --> 1107.06]  The more images you have on your page,
[1107.16 --> 1107.98]  the slower it will get
[1107.98 --> 1109.78]  because the more textures will be involved.
[1110.44 --> 1110.76]  However,
[1110.96 --> 1113.54]  if you have like a sane amount
[1113.54 --> 1114.58]  of images and textures,
[1115.18 --> 1116.40]  you can have very,
[1116.58 --> 1118.92]  very fast screen updates,
[1119.06 --> 1119.82]  rendering updates,
[1119.82 --> 1121.50]  because everything is rendered
[1121.50 --> 1122.28]  by the hardware.
[1123.86 --> 1124.86]  And that comes into play
[1124.86 --> 1127.68]  when you develop for mobile devices.
[1128.24 --> 1129.46]  If you have static images
[1129.46 --> 1132.68]  that are either image files
[1132.68 --> 1135.24]  or made with canvas
[1135.24 --> 1137.46]  or with gradients,
[1137.76 --> 1139.04]  and if you just move them around
[1139.04 --> 1140.72]  with WebKit transform, for example,
[1141.18 --> 1142.94]  then you will probably not experience
[1142.94 --> 1145.50]  any problems with rendering speed.
[1145.88 --> 1146.14]  However,
[1146.40 --> 1147.62]  if you move stuff around
[1147.62 --> 1148.50]  and at the same time
[1148.50 --> 1150.68]  change the DOM contents,
[1150.78 --> 1151.16]  for example,
[1151.30 --> 1152.42]  the inner HTML,
[1152.78 --> 1154.48]  the inner text of a DOM node,
[1155.40 --> 1157.68]  then WebKit has to re-render the element
[1157.68 --> 1159.38]  for each frame
[1159.38 --> 1160.86]  and create a new texture
[1160.86 --> 1163.20]  and load it into the graphics memory chip
[1163.20 --> 1164.28]  and the graphics memory chip
[1164.28 --> 1164.54]  has to,
[1164.90 --> 1165.64]  and so on and so forth.
[1165.72 --> 1167.54]  So if you just move textures around fast,
[1167.66 --> 1169.30]  if you change anything about the elements,
[1169.60 --> 1169.94]  slow.
[1169.94 --> 1173.14]  So we had a particular problem
[1173.14 --> 1174.46]  on every time zone.
[1174.54 --> 1175.18]  There's a slider
[1175.18 --> 1176.72]  which allows you to select
[1176.72 --> 1178.32]  the current time
[1178.32 --> 1179.78]  and then the page updates
[1179.78 --> 1180.36]  based on that.
[1180.84 --> 1181.82]  The slider shows
[1181.82 --> 1183.08]  the current time.
[1183.28 --> 1184.44]  So for each movement
[1184.44 --> 1185.04]  of the slider,
[1185.26 --> 1186.22]  we have to update
[1186.22 --> 1187.54]  the contents of the DOM node
[1187.54 --> 1187.92]  in there,
[1188.24 --> 1189.88]  which causes a bit of slowness.
[1190.68 --> 1192.50]  So because we couldn't change
[1192.50 --> 1193.96]  this particular aspect
[1193.96 --> 1194.60]  of the website
[1194.60 --> 1195.40]  because we wanted
[1195.40 --> 1196.48]  to have the time there,
[1196.48 --> 1198.92]  we decided to look into
[1198.92 --> 1200.96]  what else can we optimize
[1200.96 --> 1202.04]  on the website.
[1202.68 --> 1203.64]  And it turns out
[1203.64 --> 1205.00]  that the biggest way
[1205.00 --> 1206.62]  or the easiest way
[1206.62 --> 1207.90]  to make anything faster
[1207.90 --> 1208.32]  on the web,
[1208.38 --> 1209.14]  and this is even true
[1209.14 --> 1209.96]  for desktop web browsers,
[1210.10 --> 1215.90]  is to have as few nodes
[1215.90 --> 1217.40]  as possible on your page.
[1218.00 --> 1220.66]  We used CSS gradients
[1220.66 --> 1221.48]  and diffs,
[1221.78 --> 1223.08]  absolute deposition diffs
[1223.08 --> 1225.02]  for the bars you can see
[1225.02 --> 1226.64]  on the background of the page
[1226.64 --> 1228.56]  with each bar representing
[1228.56 --> 1230.14]  a day in some time zone.
[1230.66 --> 1231.36]  And I think there are
[1231.36 --> 1233.08]  36 bars on the page.
[1234.16 --> 1235.44]  So 12 time zones
[1235.44 --> 1236.48]  and three bars each.
[1237.72 --> 1239.22]  And for each bar,
[1239.78 --> 1240.54]  each of those bars,
[1240.68 --> 1241.84]  each of those 36 bars
[1241.84 --> 1242.88]  is basically a texture
[1242.88 --> 1243.56]  for the browser
[1243.56 --> 1244.42]  that the browser
[1244.42 --> 1245.06]  has to update
[1245.06 --> 1245.98]  and render and stuff.
[1246.40 --> 1247.20]  We replaced that
[1247.20 --> 1248.82]  with one big canvas element
[1248.82 --> 1250.84]  that we just now update.
[1251.50 --> 1252.78]  And that turns out
[1252.78 --> 1253.50]  to be much faster
[1253.50 --> 1256.38]  because the whole graphics chip
[1256.38 --> 1257.26]  just has to deal
[1257.26 --> 1258.36]  with this one big texture
[1258.36 --> 1258.88]  in the background
[1258.88 --> 1259.76]  instead of 36
[1259.76 --> 1260.72]  individual textures.
[1261.50 --> 1262.42]  And that brought
[1262.42 --> 1263.46]  a big speed boost
[1263.46 --> 1264.40]  into our application.
[1265.34 --> 1266.12]  There's some other
[1266.12 --> 1268.48]  CSS properties
[1268.48 --> 1271.46]  that can cause
[1271.46 --> 1272.66]  performance issues
[1272.66 --> 1274.88]  because of the way
[1274.88 --> 1275.66]  the browser
[1275.66 --> 1277.30]  re-renders elements
[1277.30 --> 1278.66]  and has to re-render textures,
[1279.16 --> 1279.56]  which is,
[1280.04 --> 1281.02]  for example,
[1281.02 --> 1283.22]  box shadow causes
[1283.22 --> 1284.42]  performance problems.
[1285.04 --> 1287.64]  And there's other properties,
[1287.80 --> 1288.42]  but you can read
[1288.42 --> 1289.68]  about that in my blog post.
[1290.38 --> 1290.84]  You know,
[1290.88 --> 1291.28]  I'm convinced
[1291.28 --> 1292.24]  if you want to drive traffic
[1292.24 --> 1292.76]  to your site,
[1292.84 --> 1294.12]  you just mentioned HTML5
[1294.12 --> 1294.60]  and Canvas
[1294.60 --> 1295.56]  in the headline.
[1295.74 --> 1296.90]  We posted an article
[1296.90 --> 1297.32]  this week
[1297.32 --> 1298.22]  about a little framework
[1298.22 --> 1298.54]  called,
[1298.60 --> 1299.18]  a little library
[1299.18 --> 1299.72]  called Jury
[1299.72 --> 1300.58]  that just provides
[1300.58 --> 1301.38]  a chainable wrapper
[1301.38 --> 1302.42]  to the Canvas object.
[1302.98 --> 1304.70]  And it's been highly popular.
[1304.94 --> 1306.60]  So are we at a point
[1306.60 --> 1307.44]  where adoption's
[1307.44 --> 1307.88]  to a point
[1307.88 --> 1308.56]  where we can get
[1308.56 --> 1309.46]  excited about Canvas?
[1309.46 --> 1311.20]  I think so.
[1311.72 --> 1312.48]  It's interesting
[1312.48 --> 1313.24]  that you mentioned it.
[1313.60 --> 1314.78]  The blog post
[1314.78 --> 1315.40]  I wrote about
[1315.40 --> 1316.10]  iPad performance,
[1316.22 --> 1316.88]  I think it has
[1316.88 --> 1318.12]  had like 100,000
[1318.12 --> 1318.96]  page views now.
[1319.90 --> 1321.78]  So it's definitely,
[1321.92 --> 1322.98]  there's a lot of interest
[1322.98 --> 1324.18]  in these technologies.
[1324.50 --> 1325.62]  And if you want to have
[1325.62 --> 1326.82]  really well-performing
[1326.82 --> 1327.40]  applications,
[1329.42 --> 1330.12]  mobile devices
[1330.12 --> 1330.94]  are slower
[1330.94 --> 1331.94]  than desktop browsers.
[1332.12 --> 1333.30]  They have limited resources.
[1333.74 --> 1335.28]  So you have to understand
[1335.28 --> 1336.12]  more about
[1336.12 --> 1336.86]  how they work
[1336.86 --> 1337.84]  to make really
[1337.84 --> 1339.60]  well-performing web pages.
[1340.10 --> 1341.20]  If you just have
[1341.20 --> 1342.70]  a normal web page
[1342.70 --> 1343.56]  with some text
[1343.56 --> 1344.28]  and images on it,
[1344.30 --> 1344.88]  it doesn't matter.
[1345.52 --> 1346.04]  But if you have
[1346.04 --> 1346.72]  an application,
[1347.48 --> 1349.58]  it can start
[1349.58 --> 1350.76]  to matter very quickly
[1350.76 --> 1351.62]  if the user
[1351.62 --> 1352.58]  has like a really smooth
[1352.58 --> 1353.46]  and nice experience
[1353.46 --> 1354.12]  or everything
[1354.12 --> 1354.98]  is kind of slow
[1354.98 --> 1356.84]  and jerky
[1356.84 --> 1357.38]  and lagging.
[1357.58 --> 1360.50]  So if you want
[1360.50 --> 1361.44]  to have the best experience
[1361.44 --> 1361.98]  for your user,
[1362.08 --> 1362.98]  you have to understand
[1362.98 --> 1364.20]  how these devices work
[1364.20 --> 1364.74]  and how these
[1364.74 --> 1366.14]  mobile browsers work
[1366.14 --> 1368.04]  and how you can
[1368.04 --> 1369.14]  use all these
[1369.14 --> 1369.84]  new technologies
[1369.84 --> 1371.20]  like Canvas elements
[1371.20 --> 1374.12]  and CSS-free goodies
[1374.12 --> 1376.50]  and also new DOM
[1376.50 --> 1377.50]  and JavaScript features.
[1378.50 --> 1379.48]  If you understand
[1379.48 --> 1380.02]  all of this,
[1380.08 --> 1381.94]  you can make web applications
[1381.94 --> 1382.88]  for mobile devices
[1382.88 --> 1383.92]  that just work
[1383.92 --> 1384.52]  so much better.
[1385.52 --> 1385.76]  You know,
[1385.82 --> 1386.52]  our industry
[1386.52 --> 1387.56]  tends to find
[1387.56 --> 1388.92]  buzzwords to rally behind.
[1389.02 --> 1389.78]  I remember it was
[1389.78 --> 1392.00]  DHTML back in the day
[1392.00 --> 1392.64]  and then it kind of
[1392.64 --> 1394.32]  merged into AJAX
[1394.32 --> 1395.36]  and now the latest buzzword
[1395.36 --> 1396.70]  is HTML5.
[1396.78 --> 1397.62]  What does HTML5
[1397.62 --> 1398.08]  mean to you?
[1399.18 --> 1400.14]  HTML5 for me,
[1401.06 --> 1402.20]  I do know that
[1402.20 --> 1404.68]  it technically only means
[1404.68 --> 1405.50]  like this upcoming
[1405.50 --> 1406.40]  standard of HTML,
[1406.54 --> 1407.56]  but HTML5 for me
[1407.56 --> 1408.64]  is a technology
[1408.64 --> 1409.28]  of families
[1409.28 --> 1410.54]  which includes
[1410.54 --> 1411.48]  the HTML5
[1411.48 --> 1412.12]  specification
[1412.12 --> 1413.30]  for the next
[1413.30 --> 1414.86]  generation
[1414.86 --> 1416.54]  of the HTML
[1416.54 --> 1418.00]  markup language,
[1418.20 --> 1419.46]  but it also includes
[1419.46 --> 1419.86]  for me
[1419.86 --> 1421.06]  all the improvements
[1421.06 --> 1421.76]  to JavaScript
[1421.76 --> 1422.68]  that are done,
[1422.82 --> 1423.44]  all the improvements
[1423.44 --> 1424.06]  through the DOM
[1424.06 --> 1425.04]  that are done,
[1425.90 --> 1427.36]  and also
[1427.36 --> 1428.42]  all the CSS3
[1428.42 --> 1429.12]  improvements,
[1429.68 --> 1431.32]  and other technologies
[1431.32 --> 1432.94]  that are extending
[1432.94 --> 1433.48]  the DOM
[1433.48 --> 1436.18]  like local storage
[1436.18 --> 1438.20]  and geolocation
[1438.20 --> 1439.90]  and all that sort of stuff.
[1439.98 --> 1440.92]  It's a good word
[1440.92 --> 1442.86]  for defining
[1442.86 --> 1443.48]  the family
[1443.48 --> 1444.50]  of these technologies
[1444.50 --> 1446.10]  that are coming up now,
[1446.26 --> 1446.46]  you know,
[1446.58 --> 1447.40]  Canvas also.
[1448.12 --> 1448.68]  You know,
[1448.72 --> 1449.50]  I probably am
[1449.50 --> 1450.70]  not understating this.
[1450.88 --> 1452.08]  I think a little framework
[1452.08 --> 1452.62]  has come along
[1452.62 --> 1454.50]  to really change
[1454.50 --> 1455.06]  the landscape
[1455.06 --> 1457.24]  and it really
[1457.24 --> 1458.02]  is redefining
[1458.02 --> 1458.68]  everything we thought
[1458.68 --> 1459.52]  we knew about JavaScript
[1459.52 --> 1460.56]  and that's Vapor.js.
[1461.32 --> 1461.78]  Oh yes,
[1461.96 --> 1462.10]  yeah,
[1462.16 --> 1462.56]  Vapor.js
[1462.56 --> 1463.66]  is pretty amazing.
[1465.58 --> 1467.26]  It's the only
[1467.26 --> 1468.42]  JavaScript framework
[1468.42 --> 1469.02]  in existence
[1469.02 --> 1470.44]  that is compatible
[1470.44 --> 1471.64]  with any browser
[1471.64 --> 1473.00]  that has ever been made
[1473.00 --> 1474.12]  and will ever be made.
[1474.64 --> 1475.16]  Even browsers
[1475.16 --> 1475.88]  that don't support
[1475.88 --> 1476.30]  JavaScript
[1476.30 --> 1477.66]  run Vapor.js fine,
[1477.88 --> 1478.36]  which is
[1478.36 --> 1480.92]  a pretty amazing achievement
[1480.92 --> 1481.86]  if you think about it.
[1482.48 --> 1483.28]  We also have
[1483.28 --> 1487.08]  indefinite test coverage,
[1487.76 --> 1488.68]  which is pretty awesome.
[1489.36 --> 1490.12]  That is amazing.
[1490.40 --> 1490.64]  Yeah.
[1491.08 --> 1492.02]  I think no other
[1492.02 --> 1492.74]  software project
[1492.74 --> 1493.78]  in history
[1493.78 --> 1494.94]  has had that.
[1495.04 --> 1495.42]  So that's
[1495.42 --> 1496.36]  quite an achievement,
[1496.78 --> 1498.12]  especially if you think
[1498.12 --> 1498.78]  that Vapor.js
[1498.78 --> 1499.54]  was released
[1499.54 --> 1500.18]  after having
[1500.18 --> 1502.22]  like four or five beers
[1502.22 --> 1503.30]  on like the weekend
[1503.30 --> 1504.30]  of JS Confiu.
[1504.30 --> 1506.88]  I just noticed
[1506.88 --> 1507.62]  you pulled in
[1507.62 --> 1508.78]  a patch
[1508.78 --> 1510.12]  from Kenneth Reeds
[1510.12 --> 1510.56]  here on the
[1510.56 --> 1511.92]  changelog,
[1512.06 --> 1512.60]  so added
[1512.60 --> 1514.16]  X-Core support.
[1514.42 --> 1515.26]  The really amazing
[1515.26 --> 1516.20]  thing about Vapor.js
[1516.20 --> 1517.52]  is that it
[1517.52 --> 1518.40]  came together
[1518.40 --> 1519.36]  in just like
[1519.36 --> 1520.24]  two or three hours
[1520.24 --> 1520.94]  after having
[1520.94 --> 1521.76]  lots of beer
[1521.76 --> 1523.46]  at JS Confiu
[1523.46 --> 1524.60]  last month.
[1524.74 --> 1525.24]  So that was
[1525.24 --> 1526.32]  pretty great,
[1526.56 --> 1527.26]  all these achievements
[1527.26 --> 1528.66]  in that short a time.
[1529.56 --> 1530.58]  We also hold
[1530.58 --> 1532.50]  like 140 forks
[1532.50 --> 1533.52]  on GitHub right now,
[1533.58 --> 1533.94]  I think.
[1534.36 --> 1535.18]  So it's been
[1535.18 --> 1536.00]  pretty popular.
[1537.10 --> 1538.02]  JS Confiu,
[1538.26 --> 1539.02]  give us a recap.
[1540.06 --> 1540.68]  Oh, JS Confiu
[1540.68 --> 1541.32]  is awesome.
[1542.26 --> 1542.96]  First of all,
[1543.58 --> 1544.14]  the organizers
[1544.14 --> 1544.74]  of the conference
[1544.74 --> 1545.98]  are just amazing people.
[1546.26 --> 1546.76]  It's like
[1546.76 --> 1548.04]  what they pull together
[1548.04 --> 1549.72]  in like a completely
[1549.72 --> 1550.58]  non-profit way
[1550.58 --> 1551.22]  is amazing.
[1551.68 --> 1552.86]  So it's really
[1552.86 --> 1554.10]  props to them
[1554.10 --> 1555.00]  for putting
[1555.00 --> 1555.64]  the show together.
[1555.78 --> 1556.68]  It was really great.
[1557.02 --> 1557.80]  Great location,
[1558.58 --> 1560.00]  lots of great people,
[1560.14 --> 1560.90]  very enthusiastic
[1560.90 --> 1561.56]  about JavaScript.
[1561.56 --> 1562.64]  You could really feel
[1562.64 --> 1564.14]  that there's
[1564.14 --> 1565.04]  something going on
[1565.04 --> 1566.12]  in the community
[1566.12 --> 1567.00]  with JavaScript.
[1567.30 --> 1568.42]  Everyone is really excited
[1568.42 --> 1569.20]  and there is
[1569.20 --> 1570.46]  a really good mixture
[1570.46 --> 1572.32]  between server-side
[1572.32 --> 1572.72]  JavaScript
[1572.72 --> 1573.78]  and client-side
[1573.78 --> 1574.70]  JavaScript stuff
[1574.70 --> 1575.92]  which I find
[1575.92 --> 1577.46]  great because
[1577.46 --> 1578.74]  there's a lot of stuff
[1578.74 --> 1579.86]  people can learn
[1579.86 --> 1580.44]  from each other.
[1581.42 --> 1582.26]  As I said earlier,
[1582.52 --> 1583.24]  lots of people
[1583.24 --> 1584.04]  are drawn into
[1584.04 --> 1585.56]  JavaScript by libraries
[1585.56 --> 1586.74]  and they don't really
[1586.74 --> 1587.48]  know what they're doing.
[1587.88 --> 1588.60]  Maybe they're
[1588.60 --> 1589.34]  like designers
[1589.34 --> 1590.12]  and just want to
[1590.12 --> 1590.84]  extend some websites
[1590.84 --> 1591.26]  a little bit.
[1591.56 --> 1592.68]  But the server-side
[1592.68 --> 1593.40]  JavaScript stuff
[1593.40 --> 1594.82]  actually draws in
[1594.82 --> 1595.50]  a lot of really,
[1595.66 --> 1596.52]  really good programmers
[1596.52 --> 1597.20]  to JavaScript
[1597.20 --> 1598.34]  and this will help
[1598.34 --> 1599.32]  the language a lot.
[1599.50 --> 1600.00]  And you could see
[1600.00 --> 1600.92]  that at JS Conf
[1600.92 --> 1601.36]  UF.
[1601.64 --> 1602.28]  I thought there was
[1602.28 --> 1604.32]  a lot of great
[1604.32 --> 1606.34]  talks there
[1606.34 --> 1606.86]  and content.
[1607.60 --> 1608.88]  My favorite talk
[1608.88 --> 1609.56]  was about
[1609.56 --> 1610.76]  FabJS
[1610.76 --> 1611.76]  which was just
[1611.76 --> 1612.92]  a mind-blowing talk.
[1613.04 --> 1613.78]  I hope the video
[1613.78 --> 1614.78]  of that is up soon.
[1615.02 --> 1616.12]  Everyone should see that.
[1616.12 --> 1617.78]  It's a really,
[1617.78 --> 1618.80]  really good example
[1618.80 --> 1621.04]  of how you can
[1621.04 --> 1621.88]  take an existing
[1621.88 --> 1622.82]  language and
[1622.82 --> 1624.24]  completely rethink
[1624.24 --> 1625.90]  the way it can be used.
[1626.40 --> 1626.98]  I'm not saying
[1626.98 --> 1628.06]  I would use it
[1628.06 --> 1628.60]  next week
[1628.60 --> 1631.18]  or at any point,
[1631.34 --> 1632.90]  but it's a really,
[1632.96 --> 1633.88]  really well example
[1633.88 --> 1635.74]  of take something
[1635.74 --> 1637.18]  and just try to
[1637.18 --> 1638.40]  take a step back
[1638.40 --> 1639.38]  and rethink something.
[1639.46 --> 1640.08]  That was really,
[1640.24 --> 1640.58]  really great
[1640.58 --> 1640.98]  and awesome.
[1640.98 --> 1642.70]  And of course,
[1642.80 --> 1643.60]  I just released
[1643.60 --> 1645.04]  was Chris Williams'
[1645.24 --> 1645.84]  talk on
[1645.84 --> 1646.86]  PromoteJS
[1646.86 --> 1648.42]  which was one of
[1648.42 --> 1648.94]  the greatest
[1648.94 --> 1650.26]  talks I've ever
[1650.26 --> 1650.92]  seen in my life,
[1650.98 --> 1651.28]  I think,
[1651.44 --> 1652.90]  on a programming topic.
[1653.66 --> 1654.64]  It's so much
[1654.64 --> 1657.10]  really love
[1657.10 --> 1658.00]  went into this.
[1658.16 --> 1658.70]  You know,
[1658.88 --> 1660.72]  Chris is so
[1660.72 --> 1661.34]  enthusiastic
[1661.34 --> 1663.46]  and excited
[1663.46 --> 1664.52]  about JavaScript
[1664.52 --> 1665.08]  as a language
[1665.08 --> 1665.48]  and I think
[1665.48 --> 1666.00]  we all should
[1666.00 --> 1666.46]  be that.
[1666.82 --> 1667.48]  There's a lot of
[1667.48 --> 1669.54]  bashing
[1669.54 --> 1670.44]  going around.
[1670.44 --> 1671.04]  I do that
[1671.04 --> 1671.84]  a lot of the time.
[1671.96 --> 1672.46]  I really like
[1672.46 --> 1673.44]  to bash sometimes
[1673.44 --> 1674.72]  at things
[1674.72 --> 1675.68]  like IE9.
[1676.22 --> 1677.00]  I don't get
[1677.00 --> 1678.26]  Microsoft at all,
[1678.36 --> 1678.70]  I think.
[1679.40 --> 1679.56]  But
[1679.56 --> 1682.24]  there's also
[1682.24 --> 1683.12]  so much energy
[1683.12 --> 1683.98]  there and if you
[1683.98 --> 1684.50]  take that
[1684.50 --> 1685.10]  and channel that
[1685.10 --> 1685.94]  into something good
[1685.94 --> 1687.22]  instead of
[1687.22 --> 1688.52]  always
[1688.52 --> 1689.94]  lamenting
[1689.94 --> 1691.64]  and crying
[1691.64 --> 1692.26]  about that
[1692.26 --> 1693.24]  JavaScript documentation
[1693.24 --> 1693.78]  is so bad,
[1693.96 --> 1694.72]  instead of sitting
[1694.72 --> 1695.48]  down writing
[1695.48 --> 1696.48]  JavaScript documentation
[1696.48 --> 1697.08]  or linking
[1697.08 --> 1698.16]  to good documentation
[1698.16 --> 1699.30]  so people can
[1699.30 --> 1700.10]  find the stuff
[1700.10 --> 1700.48]  and people
[1700.48 --> 1702.54]  get excited
[1702.54 --> 1703.06]  about JavaScript
[1703.06 --> 1703.58]  as much as
[1703.58 --> 1704.58]  we are excited
[1704.58 --> 1705.26]  about JavaScript
[1705.26 --> 1705.98]  in the JavaScript
[1705.98 --> 1706.54]  community,
[1707.10 --> 1708.50]  everyone wins.
[1709.42 --> 1709.76]  Absolutely.
[1710.10 --> 1710.72]  We're on board
[1710.72 --> 1711.18]  with that effort
[1711.18 --> 1711.58]  so in the
[1711.58 --> 1712.26]  changelog that's
[1712.26 --> 1713.76]  the promote.js
[1713.76 --> 1715.00]  banner in the
[1715.00 --> 1715.80]  sidebar if you've
[1715.80 --> 1716.26]  seen that and
[1716.26 --> 1716.78]  wondered what that
[1716.78 --> 1716.96]  was.
[1716.96 --> 1717.18]  Great.
[1719.12 --> 1719.82]  So server-side
[1719.82 --> 1720.18]  JavaScript,
[1720.44 --> 1721.04]  does this have you
[1721.04 --> 1721.58]  excited at all
[1721.58 --> 1722.00]  or are you still
[1722.00 --> 1722.86]  slinging Ruby
[1722.86 --> 1723.62]  on the server-side?
[1724.24 --> 1725.24]  I'm slinging Ruby
[1725.24 --> 1726.04]  on the server-side.
[1726.04 --> 1728.72]  I do like
[1728.72 --> 1729.58]  JavaScript a lot
[1729.58 --> 1730.56]  but I also
[1730.56 --> 1731.66]  like Ruby a lot
[1731.66 --> 1732.82]  and of course
[1732.82 --> 1733.42]  we have existing
[1733.42 --> 1733.92]  projects,
[1734.06 --> 1734.74]  there's no need
[1734.74 --> 1735.40]  for us to
[1735.40 --> 1736.16]  change it over
[1736.16 --> 1736.66]  to JavaScript
[1736.66 --> 1737.20]  now because
[1737.20 --> 1738.02]  it's cool
[1738.02 --> 1739.98]  but it
[1739.98 --> 1740.56]  definitely
[1740.56 --> 1742.24]  is a good
[1742.24 --> 1744.66]  thing that
[1744.66 --> 1745.26]  happens there
[1745.26 --> 1746.30]  because JavaScript
[1746.30 --> 1747.00]  now as a
[1747.00 --> 1747.80]  language gets
[1747.80 --> 1748.50]  things like
[1748.50 --> 1749.22]  a common
[1749.22 --> 1750.06]  library and
[1750.06 --> 1750.58]  stuff on the
[1750.58 --> 1751.22]  server-side so
[1751.22 --> 1751.86]  that's really
[1751.86 --> 1752.14]  good.
[1752.80 --> 1753.60]  It's actually
[1753.60 --> 1754.22]  been around
[1754.22 --> 1754.84]  for a long
[1754.84 --> 1755.24]  time,
[1755.88 --> 1756.30]  server-side
[1756.30 --> 1756.96]  JavaScript but
[1756.96 --> 1757.92]  it never really
[1757.92 --> 1758.80]  picked up until
[1758.80 --> 1759.72]  Node.js came
[1759.72 --> 1761.58]  along and I
[1761.58 --> 1762.48]  was there when
[1762.48 --> 1765.58]  Ryan Dahl did
[1765.58 --> 1766.42]  his first
[1766.42 --> 1767.56]  Node.js talk
[1767.56 --> 1769.06]  and it was
[1769.06 --> 1769.52]  amazing.
[1772.22 --> 1773.14]  Mind-blowing
[1773.14 --> 1773.60]  again.
[1773.94 --> 1774.58]  It's like someone
[1774.58 --> 1775.54]  sitting down and
[1775.54 --> 1776.38]  rethinking the
[1776.38 --> 1777.16]  way something
[1777.16 --> 1778.00]  works completely.
[1778.50 --> 1779.42]  It's just always
[1779.42 --> 1780.16]  amazing to watch
[1780.16 --> 1780.86]  that process.
[1780.86 --> 1781.76]  even if you
[1781.76 --> 1782.26]  do not have
[1782.26 --> 1783.16]  an immediate
[1783.16 --> 1783.90]  use for it.
[1784.48 --> 1785.14]  We might
[1785.14 --> 1785.86]  actually go
[1785.86 --> 1786.72]  ahead and
[1786.72 --> 1787.72]  use Node.js
[1787.72 --> 1788.04]  for an
[1788.04 --> 1788.98]  upcoming project
[1788.98 --> 1791.02]  where we have
[1791.02 --> 1791.60]  to deal with
[1791.60 --> 1792.02]  a lot of
[1792.02 --> 1792.68]  real-time
[1792.68 --> 1794.10]  stuff like
[1794.10 --> 1794.90]  WebSockets
[1794.90 --> 1795.74]  and that sort
[1795.74 --> 1796.54]  of thing and
[1796.54 --> 1797.34]  for these
[1797.34 --> 1797.96]  things it
[1797.96 --> 1798.76]  really shines.
[1799.78 --> 1801.22]  For things
[1801.22 --> 1801.56]  where you
[1801.56 --> 1802.48]  would now
[1802.48 --> 1803.42]  use Ruby
[1803.42 --> 1803.94]  and Rails
[1803.94 --> 1804.52]  for example,
[1805.08 --> 1805.70]  I think it
[1805.70 --> 1806.60]  might be a
[1806.60 --> 1807.26]  bit premature
[1807.26 --> 1809.24]  to just drop
[1809.24 --> 1809.80]  everything you
[1809.80 --> 1810.56]  have and
[1810.56 --> 1812.86]  adopt Node.js
[1812.86 --> 1813.46]  but for new
[1813.46 --> 1813.84]  projects,
[1813.98 --> 1814.14]  sure.
[1815.04 --> 1815.54]  I noticed you
[1815.54 --> 1816.20]  forked a project
[1816.20 --> 1816.66]  that we covered
[1816.66 --> 1817.12]  last week in
[1817.12 --> 1817.40]  the channel,
[1817.84 --> 1818.84]  eyeballs.js.
[1819.98 --> 1820.80]  Yes, eyeballs
[1820.80 --> 1821.38]  is great.
[1822.08 --> 1822.86]  It's from my
[1822.86 --> 1823.34]  friend Paul
[1823.34 --> 1824.66]  Campbell and
[1824.66 --> 1826.20]  it's basically
[1826.20 --> 1827.80]  a clone of
[1827.80 --> 1828.44]  Ruby and Rails
[1828.44 --> 1829.18]  but running in
[1829.18 --> 1829.60]  the browser
[1829.60 --> 1832.32]  using things
[1832.32 --> 1833.22]  like Web
[1833.22 --> 1834.08]  SQL as
[1834.08 --> 1834.42]  backend.
[1834.42 --> 1835.30]  so that's
[1835.30 --> 1835.74]  pretty good
[1835.74 --> 1837.12]  a pretty
[1837.12 --> 1837.92]  great thing
[1837.92 --> 1838.30]  to have
[1838.30 --> 1838.76]  if you
[1838.76 --> 1839.72]  have a
[1839.72 --> 1840.38]  more data
[1840.38 --> 1840.90]  centric
[1840.90 --> 1841.28]  backend
[1841.28 --> 1842.70]  and send
[1842.70 --> 1843.58]  along JSON
[1843.58 --> 1844.28]  messages and
[1844.28 --> 1845.22]  stuff and
[1845.22 --> 1845.66]  you want to
[1845.66 --> 1846.36]  render more
[1846.36 --> 1846.96]  in a
[1846.96 --> 1847.88]  templated way
[1847.88 --> 1848.64]  on the
[1848.64 --> 1849.22]  front end.
[1849.42 --> 1849.62]  That's
[1849.62 --> 1851.24]  something we
[1851.24 --> 1851.76]  have a use
[1851.76 --> 1852.82]  for in a
[1852.82 --> 1853.32]  current project
[1853.32 --> 1853.66]  so that's
[1853.66 --> 1854.20]  why I forked
[1854.20 --> 1854.32]  it.
[1854.52 --> 1854.94]  I haven't
[1854.94 --> 1855.78]  committed back
[1855.78 --> 1856.26]  any patches
[1856.26 --> 1858.36]  yet but I
[1858.36 --> 1859.68]  might soon.
[1859.80 --> 1860.16]  So what's
[1860.16 --> 1860.80]  your take on
[1860.80 --> 1861.72]  templating choices?
[1861.72 --> 1863.90]  Templating is
[1863.90 --> 1864.28]  interesting.
[1864.58 --> 1865.98]  If a
[1865.98 --> 1866.56]  developer is
[1866.56 --> 1868.56]  bored, the
[1868.56 --> 1869.20]  developer will
[1869.20 --> 1869.88]  develop either
[1869.88 --> 1870.78]  of two things.
[1871.20 --> 1871.84]  One is a
[1871.84 --> 1872.54]  testing framework
[1872.54 --> 1874.52]  or a second
[1874.52 --> 1875.40]  thing is a
[1875.40 --> 1876.36]  templating language.
[1876.90 --> 1877.46]  There's so
[1877.46 --> 1878.20]  many out there.
[1878.52 --> 1879.58]  If you Google
[1879.58 --> 1880.26]  for JavaScript
[1880.26 --> 1881.44]  testing frameworks,
[1881.62 --> 1882.10]  I don't know,
[1882.20 --> 1882.62]  I think there's
[1882.62 --> 1883.32]  like hundreds
[1883.32 --> 1883.88]  of them.
[1884.56 --> 1884.78]  And for
[1884.78 --> 1886.18]  templating language
[1886.18 --> 1886.92]  it's similar.
[1887.84 --> 1889.48]  And it's
[1889.48 --> 1890.26]  quite useful
[1890.26 --> 1890.92]  for a lot of
[1890.92 --> 1891.56]  things but it
[1891.56 --> 1892.02]  won't solve
[1892.02 --> 1892.32]  all your
[1892.32 --> 1892.70]  problems.
[1893.16 --> 1893.62]  You should
[1893.62 --> 1894.22]  never forget
[1894.22 --> 1894.84]  that you
[1894.84 --> 1895.50]  have a
[1895.50 --> 1895.96]  full-blown
[1895.96 --> 1896.66]  language at
[1896.66 --> 1897.30]  your disposal
[1897.30 --> 1898.24]  at all
[1898.24 --> 1899.02]  times if you
[1899.02 --> 1899.58]  do JavaScript.
[1900.34 --> 1900.68]  So you
[1900.68 --> 1901.26]  shouldn't try
[1901.26 --> 1902.52]  to get
[1902.52 --> 1903.16]  too meta,
[1903.54 --> 1903.98]  you know
[1903.98 --> 1904.46]  what I mean?
[1904.64 --> 1905.24]  That you
[1905.24 --> 1906.48]  try to put
[1906.48 --> 1907.02]  everything into
[1907.02 --> 1907.66]  the templating
[1907.66 --> 1908.30]  language and
[1908.30 --> 1908.78]  then you
[1908.78 --> 1909.24]  kind of have
[1909.24 --> 1909.68]  a language
[1909.68 --> 1909.92]  in the
[1909.92 --> 1910.26]  language,
[1910.56 --> 1910.98]  not good.
[1911.08 --> 1911.36]  So it
[1911.36 --> 1911.64]  should be
[1911.64 --> 1912.26]  very basic
[1912.26 --> 1912.86]  if you use
[1912.86 --> 1913.30]  a templating
[1913.30 --> 1913.76]  language in
[1913.76 --> 1914.16]  my opinion.
[1914.30 --> 1914.70]  One of the
[1914.70 --> 1915.26]  approaches is
[1915.26 --> 1915.66]  to start
[1915.66 --> 1916.52]  putting your
[1916.52 --> 1917.42]  templates in
[1917.42 --> 1918.28]  script tags with
[1918.28 --> 1918.60]  just an
[1918.60 --> 1919.40]  alternate language
[1919.40 --> 1920.02]  declaration.
[1920.02 --> 1921.08]  Do you
[1921.08 --> 1921.40]  follow this
[1921.40 --> 1921.76]  approach at
[1921.76 --> 1921.90]  all?
[1923.90 --> 1924.90]  I don't.
[1924.98 --> 1925.38]  I'm aware
[1925.38 --> 1925.76]  of it.
[1926.04 --> 1926.40]  And there's
[1926.40 --> 1926.82]  also things
[1926.82 --> 1927.48]  like CoffeeScript
[1927.48 --> 1928.20]  for example
[1928.20 --> 1929.52]  that kind of
[1929.52 --> 1930.34]  is a new
[1930.34 --> 1931.08]  implementation of
[1931.08 --> 1932.96]  JavaScript in
[1932.96 --> 1933.98]  script tags and
[1933.98 --> 1934.50]  that gets
[1934.50 --> 1935.28]  re-evaluated.
[1937.16 --> 1937.94]  Personally, I
[1937.94 --> 1938.58]  like JavaScript
[1938.58 --> 1939.60]  too much that I'm
[1939.60 --> 1940.26]  a big fan of
[1940.26 --> 1940.66]  those other
[1940.66 --> 1941.06]  approaches.
[1941.22 --> 1941.76]  But I can see
[1941.76 --> 1942.14]  that some
[1942.14 --> 1942.60]  people would
[1942.60 --> 1943.22]  prefer that,
[1943.30 --> 1943.52]  yes.
[1943.52 --> 1945.42]  templating.
[1945.58 --> 1946.12]  I guess a lot
[1946.12 --> 1946.68]  of the projects
[1946.68 --> 1947.28]  that you write,
[1947.34 --> 1948.04]  you write with
[1948.04 --> 1948.68]  Amy.
[1949.40 --> 1949.86]  So who
[1949.86 --> 1950.38]  handles the
[1950.38 --> 1950.66]  templates?
[1952.36 --> 1953.48]  So the way
[1953.48 --> 1954.26]  we work is
[1954.26 --> 1956.00]  basically I'm
[1956.00 --> 1956.30]  the dumb
[1956.30 --> 1956.76]  programmer.
[1957.32 --> 1958.20]  But I'm
[1958.20 --> 1958.52]  pretty good
[1958.52 --> 1958.90]  with coming
[1958.90 --> 1959.38]  up with
[1959.38 --> 1960.48]  strategies to
[1960.48 --> 1960.96]  achieve the
[1960.96 --> 1961.46]  impossible,
[1961.82 --> 1962.32]  if you know
[1962.32 --> 1962.74]  what I mean.
[1963.56 --> 1964.80]  But what Amy
[1964.80 --> 1965.76]  does is she
[1965.76 --> 1966.88]  has the ideas
[1966.88 --> 1967.60]  for the
[1967.60 --> 1968.46]  project and
[1968.46 --> 1969.02]  she does
[1969.02 --> 1970.16]  visual design
[1970.16 --> 1971.46]  and user
[1971.46 --> 1973.40]  interface design
[1973.40 --> 1973.84]  and user
[1973.84 --> 1974.98]  experience design
[1974.98 --> 1976.96]  and concepts,
[1977.12 --> 1977.58]  she says,
[1977.64 --> 1977.88]  from the
[1977.88 --> 1978.28]  other room.
[1979.42 --> 1980.34]  So I'm
[1980.34 --> 1981.16]  really the
[1981.16 --> 1982.38]  dumb person
[1982.38 --> 1982.98]  in this team.
[1983.94 --> 1984.50]  So talk to
[1984.50 --> 1984.84]  us about
[1984.84 --> 1985.62]  Freckle and
[1985.62 --> 1986.44]  some of the
[1986.44 --> 1987.20]  partnerships you
[1987.20 --> 1987.62]  guys have
[1987.62 --> 1987.80]  done.
[1989.12 --> 1989.76]  Yeah, so
[1989.76 --> 1991.00]  Freckle, that
[1991.00 --> 1991.70]  was our first
[1991.70 --> 1992.40]  big application
[1992.40 --> 1992.88]  together.
[1993.32 --> 1995.08]  And Freckle is
[1995.08 --> 1995.64]  a time tracking
[1995.64 --> 1996.48]  software and
[1996.48 --> 1999.14]  the reason we
[1999.14 --> 1999.96]  wrote it is
[1999.96 --> 2000.70]  at that time
[2000.70 --> 2001.54]  we did a lot
[2001.54 --> 2002.06]  of consulting
[2002.06 --> 2003.28]  and that
[2003.28 --> 2004.04]  just was no
[2004.04 --> 2004.76]  good way to
[2004.76 --> 2005.26]  track your
[2005.26 --> 2005.88]  time with
[2005.88 --> 2006.32]  any web
[2006.32 --> 2007.04]  application or
[2007.04 --> 2007.56]  any desktop
[2007.56 --> 2008.22]  application for
[2008.22 --> 2008.62]  that matter.
[2009.06 --> 2009.46]  They were all
[2009.46 --> 2010.04]  just too
[2010.04 --> 2011.14]  complicated and
[2011.14 --> 2011.54]  you know,
[2011.72 --> 2012.54]  like a series
[2012.54 --> 2013.48]  of drop-down
[2013.48 --> 2014.26]  lists and
[2014.26 --> 2015.20]  when you got a
[2015.20 --> 2016.20]  new client you
[2016.20 --> 2016.52]  had to
[2016.52 --> 2017.50]  configure like
[2017.50 --> 2018.32]  half an hour
[2018.32 --> 2019.50]  everything that
[2019.50 --> 2019.84]  you could
[2019.84 --> 2020.78]  actually start
[2020.78 --> 2021.36]  logging time.
[2022.08 --> 2022.80]  With Freckle we
[2022.80 --> 2023.74]  wanted none of
[2023.74 --> 2023.94]  that.
[2024.04 --> 2024.64]  We wanted that
[2024.64 --> 2025.48]  you can launch
[2025.48 --> 2026.02]  the application
[2026.02 --> 2026.80]  and instantly
[2026.80 --> 2027.82]  log time because
[2027.82 --> 2028.50]  that's what the
[2028.50 --> 2028.90]  application is
[2028.90 --> 2029.14]  about.
[2029.56 --> 2030.20]  Everything else,
[2030.20 --> 2030.78]  the configuration
[2030.78 --> 2032.10]  of stuff and
[2032.10 --> 2032.66]  things that can
[2032.66 --> 2033.22]  come later.
[2033.56 --> 2034.00]  When you have
[2034.00 --> 2034.62]  time, when you
[2034.62 --> 2035.30]  sit down and
[2035.30 --> 2035.98]  look at the
[2035.98 --> 2037.06]  hours, then you
[2037.06 --> 2038.56]  can go ahead and
[2038.56 --> 2039.98]  type in a budget
[2039.98 --> 2040.90]  and that sort of
[2040.90 --> 2041.06]  thing.
[2041.16 --> 2041.96]  So it was really
[2041.96 --> 2043.44]  about the most
[2043.44 --> 2044.72]  efficient way for
[2044.72 --> 2045.26]  the user to
[2045.26 --> 2045.92]  enter time.
[2046.44 --> 2047.10]  Nothing should
[2047.10 --> 2047.76]  get into the
[2047.76 --> 2048.30]  user's way.
[2048.92 --> 2049.58]  And this is where
[2049.58 --> 2050.62]  web applications can
[2050.62 --> 2051.44]  be really great.
[2052.64 --> 2053.46]  The browser is
[2053.46 --> 2056.16]  really a blank
[2056.16 --> 2056.70]  canvas.
[2057.26 --> 2058.06]  You can do
[2058.06 --> 2059.02]  basically everything
[2059.02 --> 2059.58]  in the browser.
[2059.76 --> 2060.20]  You are not
[2060.20 --> 2063.00]  subject to
[2063.00 --> 2064.00]  limitations that
[2064.00 --> 2064.48]  you have in
[2064.48 --> 2065.48]  native applications
[2065.48 --> 2066.98]  where widgets are
[2066.98 --> 2068.06]  not configurable and
[2068.06 --> 2068.72]  stuff because you
[2068.72 --> 2069.28]  can just change
[2069.28 --> 2069.94]  everything around
[2069.94 --> 2070.46]  everywhere.
[2071.08 --> 2071.88]  That's the power
[2071.88 --> 2072.70]  of web applications
[2072.70 --> 2073.08]  I think.
[2073.22 --> 2074.30]  You can really
[2074.30 --> 2075.76]  adapt and with
[2075.76 --> 2076.68]  JavaScript you can
[2076.68 --> 2078.06]  do anything you
[2078.06 --> 2079.06]  can think about in
[2079.06 --> 2079.82]  a web application.
[2080.56 --> 2082.02]  The problem that
[2082.02 --> 2082.84]  many web applications
[2082.84 --> 2084.70]  have is that
[2084.70 --> 2086.64]  people try to
[2086.64 --> 2087.64]  stay in some
[2087.64 --> 2088.40]  sort of like
[2088.40 --> 2089.52]  standard compatible
[2089.52 --> 2091.78]  mode or do
[2091.78 --> 2093.06]  not want to be
[2093.06 --> 2095.90]  too bold in
[2095.90 --> 2096.62]  doing applications
[2096.62 --> 2097.44]  but I think that
[2097.44 --> 2098.04]  approach is not
[2098.04 --> 2098.28]  good.
[2098.46 --> 2099.04]  That approach
[2099.04 --> 2101.10]  only leads to
[2101.10 --> 2103.32]  boring applications
[2103.32 --> 2104.36]  that look like
[2104.36 --> 2104.80]  every other
[2104.80 --> 2105.38]  application.
[2106.02 --> 2107.44]  If you sit down
[2107.44 --> 2108.08]  like this and
[2108.08 --> 2109.10]  if you look at
[2109.10 --> 2109.60]  every other
[2109.60 --> 2110.10]  time tracking
[2110.10 --> 2110.60]  application,
[2110.74 --> 2111.48]  if we would
[2111.48 --> 2112.14]  have done that
[2112.14 --> 2113.06]  at the point
[2113.06 --> 2113.50]  when we made
[2113.50 --> 2114.40]  Freckle, we
[2114.40 --> 2115.68]  would have produced
[2115.68 --> 2116.42]  another application
[2116.42 --> 2117.00]  with drop
[2117.00 --> 2117.68]  downs and you
[2117.68 --> 2117.98]  have to
[2117.98 --> 2118.72]  configure it
[2118.72 --> 2119.14]  before you
[2119.14 --> 2119.68]  enter time.
[2120.42 --> 2121.16]  That's not the
[2121.16 --> 2122.60]  way great
[2122.60 --> 2123.26]  applications are
[2123.26 --> 2123.48]  made.
[2123.62 --> 2124.18]  Great applications
[2124.18 --> 2124.92]  are made by
[2124.92 --> 2126.26]  looking at what
[2126.26 --> 2127.10]  the user really
[2127.10 --> 2127.96]  needs and wants
[2127.96 --> 2128.90]  and then you
[2128.90 --> 2129.92]  start everything
[2129.92 --> 2131.08]  from there, not
[2131.08 --> 2131.68]  looking at the
[2131.68 --> 2132.18]  other stuff.
[2132.66 --> 2134.14]  Maybe at some
[2134.14 --> 2134.82]  point in the
[2134.82 --> 2135.64]  development cycle
[2135.64 --> 2136.98]  later you start
[2136.98 --> 2137.60]  looking at the
[2137.60 --> 2138.30]  other stuff and
[2138.30 --> 2138.94]  see what they
[2138.94 --> 2139.88]  do and what you
[2139.88 --> 2140.82]  do and compare
[2140.82 --> 2141.38]  a little bit.
[2141.38 --> 2144.54]  But when you
[2144.54 --> 2145.28]  start something,
[2146.28 --> 2146.92]  don't try to
[2146.92 --> 2147.40]  look at other
[2147.40 --> 2147.74]  stuff.
[2148.04 --> 2148.88]  Just try to do
[2148.88 --> 2149.34]  your thing.
[2149.42 --> 2149.80]  I think that's
[2149.80 --> 2150.12]  important.
[2150.82 --> 2151.62]  And that's the
[2151.62 --> 2152.10]  important thing
[2152.10 --> 2152.48]  we do.
[2152.96 --> 2153.54]  We do not
[2153.54 --> 2154.30]  really listen to
[2154.30 --> 2155.00]  many other
[2155.00 --> 2155.36]  people.
[2155.50 --> 2157.66]  Otherwise, if I
[2157.66 --> 2157.96]  would have
[2157.96 --> 2158.62]  listened to all
[2158.62 --> 2159.62]  the people in
[2159.62 --> 2160.16]  my life that
[2160.16 --> 2161.04]  would tell me
[2161.04 --> 2161.56]  what to do, I
[2161.56 --> 2162.06]  would probably
[2162.06 --> 2162.66]  be still at
[2162.66 --> 2163.66]  university and
[2163.66 --> 2164.80]  then I would
[2164.80 --> 2165.28]  be employed
[2165.28 --> 2166.00]  somewhere until
[2166.00 --> 2166.48]  I'm 80.
[2168.42 --> 2168.88]  You know,
[2169.26 --> 2170.90]  just try to do
[2170.90 --> 2171.20]  your thing.
[2171.20 --> 2171.60]  I think that's
[2171.60 --> 2171.86]  the most
[2171.86 --> 2172.58]  important lesson
[2172.58 --> 2173.16]  that you can
[2173.16 --> 2174.18]  have in life.
[2174.56 --> 2175.04]  So Amy is a
[2175.04 --> 2175.62]  big proponent of
[2175.62 --> 2176.34]  info products.
[2176.44 --> 2176.78]  I know you
[2176.78 --> 2177.62]  have some out
[2177.62 --> 2178.22]  there under
[2178.22 --> 2178.80]  your own name.
[2179.36 --> 2179.96]  You've written
[2179.96 --> 2180.96]  both printed
[2180.96 --> 2182.12]  publications and
[2182.12 --> 2183.74]  I guess e-books
[2183.74 --> 2184.74]  and what we
[2184.74 --> 2185.04]  would call
[2185.04 --> 2185.72]  info products.
[2185.84 --> 2186.18]  What's your
[2186.18 --> 2188.40]  take on doing
[2188.40 --> 2188.84]  this as a
[2188.84 --> 2189.14]  developer?
[2190.48 --> 2191.28]  Yeah, info
[2191.28 --> 2191.90]  products has a
[2191.90 --> 2192.48]  really bad
[2192.48 --> 2194.44]  ring to it.
[2194.76 --> 2196.34]  It sort of
[2196.34 --> 2197.04]  has this
[2197.04 --> 2198.42]  sleazy aura.
[2199.38 --> 2200.10]  But info
[2200.10 --> 2200.66]  products are
[2200.66 --> 2201.14]  really great.
[2201.20 --> 2202.58]  There should be
[2202.58 --> 2203.14]  a better name
[2203.14 --> 2203.50]  for that.
[2203.70 --> 2204.04]  It's like
[2204.04 --> 2205.48]  webinar is one
[2205.48 --> 2206.06]  of those words
[2206.06 --> 2207.40]  or it's just
[2207.40 --> 2208.58]  not a good
[2208.58 --> 2208.78]  word.
[2209.62 --> 2211.76]  But a lot of
[2211.76 --> 2212.56]  developers and a
[2212.56 --> 2213.22]  lot of people we
[2213.22 --> 2214.56]  know actually
[2214.56 --> 2215.54]  make good money
[2215.54 --> 2217.14]  by selling PDFs
[2217.14 --> 2218.12]  or online courses
[2218.12 --> 2218.98]  and stuff like
[2218.98 --> 2219.28]  that.
[2219.60 --> 2220.40]  And it really
[2220.40 --> 2221.16]  helps people.
[2221.92 --> 2222.64]  Because if you
[2222.64 --> 2225.22]  as a developer,
[2225.54 --> 2225.94]  for example,
[2226.10 --> 2226.76]  you're looking for
[2226.76 --> 2227.44]  some information
[2227.44 --> 2228.24]  about, I don't
[2228.24 --> 2229.50]  know, I was
[2229.50 --> 2230.18]  looking for
[2230.18 --> 2231.00]  information about
[2231.00 --> 2232.60]  the Vim
[2232.60 --> 2233.38]  editor, for
[2233.38 --> 2234.22]  example, this
[2234.22 --> 2234.48]  week.
[2235.28 --> 2235.84]  And so I
[2235.84 --> 2236.40]  got to
[2236.40 --> 2237.18]  Joff's site,
[2237.52 --> 2238.26]  Peepcode.com,
[2238.46 --> 2239.74]  and he has a
[2239.74 --> 2240.38]  screencast on it.
[2240.44 --> 2241.18]  So I bought the
[2241.18 --> 2241.66]  screencast.
[2241.80 --> 2242.58]  It's the best way
[2242.58 --> 2243.12]  to learn it.
[2243.50 --> 2244.26]  And if you pay
[2244.26 --> 2244.72]  money for
[2244.72 --> 2245.50]  something, you're
[2245.50 --> 2246.36]  more inclined to
[2246.36 --> 2246.80]  actually pay
[2246.80 --> 2247.60]  attention because
[2247.60 --> 2248.38]  you're kind of,
[2248.96 --> 2250.04]  it's your hard-earned
[2250.04 --> 2250.62]  money that you
[2250.62 --> 2251.80]  invest into, like,
[2252.52 --> 2253.00]  getting more
[2253.00 --> 2253.70]  knowledgeable about
[2253.70 --> 2254.08]  something.
[2254.08 --> 2256.26]  And when
[2256.26 --> 2257.02]  people come to
[2257.02 --> 2258.22]  my info
[2258.22 --> 2259.12]  product, for
[2259.12 --> 2259.56]  example, we
[2259.56 --> 2260.48]  have an info
[2260.48 --> 2261.22]  product called
[2261.22 --> 2262.00]  JavaScript
[2262.00 --> 2262.74]  Performance
[2262.74 --> 2263.22]  Rocks.
[2263.28 --> 2263.98]  It's an e-book
[2263.98 --> 2265.26]  and a little
[2265.26 --> 2266.18]  helper bookmark
[2266.18 --> 2266.68]  application.
[2268.44 --> 2269.20]  People go
[2269.20 --> 2269.62]  there because
[2269.62 --> 2270.54]  they want to
[2270.54 --> 2272.18]  learn about
[2272.18 --> 2274.24]  web performance
[2274.24 --> 2275.18]  specifically.
[2276.02 --> 2277.20]  And they pay
[2277.20 --> 2278.38]  some money and
[2278.38 --> 2279.06]  then they get
[2279.06 --> 2279.66]  really, really
[2279.66 --> 2280.82]  good information
[2280.82 --> 2282.28]  that we took
[2282.28 --> 2282.98]  a long time to
[2282.98 --> 2283.44]  research.
[2283.44 --> 2284.28]  So it's a very
[2284.28 --> 2285.18]  fair exchange.
[2285.54 --> 2286.68]  And I think
[2286.68 --> 2287.60]  the web really
[2287.60 --> 2288.72]  allows you to
[2288.72 --> 2289.88]  self-publish these
[2289.88 --> 2290.48]  things without
[2290.48 --> 2291.06]  going through,
[2291.16 --> 2291.52]  like, a big
[2291.52 --> 2291.92]  publisher.
[2292.04 --> 2293.44]  Because the big
[2293.44 --> 2295.50]  publishers, what
[2295.50 --> 2296.20]  they do is they
[2296.20 --> 2296.88]  fuck you over.
[2297.72 --> 2298.54]  Sorry for my
[2298.54 --> 2299.04]  expletive.
[2299.66 --> 2300.10]  No, that's
[2300.10 --> 2300.38]  right.
[2300.52 --> 2301.10]  You know, I
[2301.10 --> 2302.84]  came to the
[2302.84 --> 2303.26]  Ruby and the
[2303.26 --> 2303.92]  Rails world and
[2303.92 --> 2304.54]  I think Amy's
[2304.54 --> 2305.20]  cheat sheets were
[2305.20 --> 2306.06]  instrumental in
[2306.06 --> 2307.50]  helping me grok
[2307.50 --> 2307.98]  some of the
[2307.98 --> 2309.60]  things, the
[2309.60 --> 2310.06]  terms and the
[2310.06 --> 2310.98]  concepts coming
[2310.98 --> 2311.30]  into that
[2311.30 --> 2311.60]  framework.
[2312.02 --> 2312.54]  And, you
[2312.54 --> 2313.14]  know, I've
[2313.14 --> 2313.88]  shelled out
[2313.88 --> 2314.84]  for a couple
[2314.84 --> 2315.02]  of your
[2315.02 --> 2316.42]  JavaScript e-books.
[2316.64 --> 2317.58]  They're fantastic.
[2317.72 --> 2318.40]  I think it's a
[2318.40 --> 2319.04]  good value
[2319.04 --> 2319.72]  exchange on both
[2319.72 --> 2320.04]  sides.
[2320.54 --> 2321.54]  Yes, definitely.
[2322.16 --> 2323.38]  Anything else in
[2323.38 --> 2324.28]  the stables from
[2324.28 --> 2325.64]  Thomas and Amy?
[2326.26 --> 2327.24]  So, yeah, we are
[2327.24 --> 2328.32]  working on a new
[2328.32 --> 2329.16]  product for
[2329.16 --> 2330.20]  customer support
[2330.20 --> 2331.10]  because all
[2331.10 --> 2331.90]  customer support
[2331.90 --> 2333.32]  software sucks,
[2333.44 --> 2333.80]  basically.
[2334.78 --> 2335.74]  We tried
[2335.74 --> 2336.28]  everything,
[2336.40 --> 2336.88]  believe me.
[2337.68 --> 2338.60]  And it's all
[2338.60 --> 2339.28]  really bad.
[2339.28 --> 2341.12]  and most of
[2341.12 --> 2341.62]  these products,
[2341.98 --> 2342.66]  the most
[2342.66 --> 2343.28]  important problem
[2343.28 --> 2343.84]  they have is
[2343.84 --> 2345.54]  that they do
[2345.54 --> 2346.10]  not build a
[2346.10 --> 2346.92]  bridge between
[2346.92 --> 2348.08]  what the
[2348.08 --> 2348.82]  customers tell
[2348.82 --> 2349.52]  you and then
[2349.52 --> 2350.10]  what you actually
[2350.10 --> 2350.88]  implement in your
[2350.88 --> 2351.22]  software.
[2351.62 --> 2352.82]  So, we are
[2352.82 --> 2353.46]  trying to build
[2353.46 --> 2354.22]  something really,
[2354.36 --> 2354.90]  really great for
[2354.90 --> 2355.10]  that.
[2356.06 --> 2356.86]  It's called
[2356.86 --> 2359.22]  Charmdesk and
[2359.22 --> 2360.86]  you can go to
[2360.86 --> 2363.96]  charmde.sk to
[2363.96 --> 2364.72]  sign up for
[2364.72 --> 2366.54]  our email when
[2366.54 --> 2367.20]  we will announce
[2367.20 --> 2367.38]  it.
[2367.38 --> 2368.26]  It says fall
[2368.26 --> 2368.82]  2010.
[2369.48 --> 2370.16]  Probably we will
[2370.16 --> 2370.66]  get the winter
[2370.66 --> 2371.92]  2010 before we
[2371.92 --> 2372.54]  will announce it.
[2374.16 --> 2374.64]  Yeah.
[2374.98 --> 2375.94]  And we also
[2375.94 --> 2376.36]  have other
[2376.36 --> 2377.00]  products in the
[2377.00 --> 2377.18]  queue.
[2378.34 --> 2379.12]  So, some of my
[2379.12 --> 2379.88]  closing questions
[2379.88 --> 2380.46]  were going to be
[2380.46 --> 2382.60]  Emacs or Vim or
[2382.60 --> 2383.00]  TextMate.
[2383.06 --> 2383.42]  It looks like
[2383.42 --> 2383.94]  you're a Vim
[2383.94 --> 2384.20]  guy.
[2385.54 --> 2386.40]  I'm actually a
[2386.40 --> 2387.04]  TextMate guy.
[2387.14 --> 2387.88]  I just started
[2387.88 --> 2389.46]  using Vim this
[2389.46 --> 2391.20]  week because a
[2391.20 --> 2392.38]  developer we're
[2392.38 --> 2392.98]  working together
[2392.98 --> 2395.04]  very closely is
[2395.04 --> 2395.72]  using it and
[2395.72 --> 2397.24]  he's all about
[2397.24 --> 2397.42]  it.
[2397.52 --> 2398.22]  You know, he's
[2398.22 --> 2399.10]  really excited
[2399.10 --> 2399.58]  about it.
[2399.64 --> 2400.34]  And if someone's
[2400.34 --> 2401.04]  excited about it,
[2401.10 --> 2401.90]  I get interested
[2401.90 --> 2402.82]  because I like
[2402.82 --> 2403.88]  seeing people
[2403.88 --> 2404.50]  that are excited
[2404.50 --> 2405.06]  about something.
[2406.06 --> 2407.60]  And so, I
[2407.60 --> 2408.18]  decided to
[2408.18 --> 2409.36]  check out Vim
[2409.36 --> 2410.70]  and I like it
[2410.70 --> 2411.14]  so far.
[2412.28 --> 2413.08]  I grog the
[2413.08 --> 2413.80]  basics already.
[2415.02 --> 2415.92]  It can only
[2415.92 --> 2417.32]  get better from
[2417.32 --> 2417.56]  there.
[2418.26 --> 2419.16]  Of course, it
[2419.16 --> 2419.96]  has a really
[2419.96 --> 2420.56]  steep learning
[2420.56 --> 2421.98]  curve and it's
[2421.98 --> 2422.68]  certainly not for
[2422.68 --> 2422.96]  everyone.
[2422.96 --> 2424.98]  but it does
[2424.98 --> 2426.02]  some things very
[2426.02 --> 2427.30]  well that I was
[2427.30 --> 2427.90]  looking for in
[2427.90 --> 2428.76]  an editor and
[2428.76 --> 2431.68]  with TextMate 2
[2431.68 --> 2432.60]  being released,
[2433.00 --> 2433.94]  I don't know,
[2434.48 --> 2438.18]  whenever, yeah,
[2438.36 --> 2438.72]  I don't know,
[2438.82 --> 2440.02]  whenever Duke Nukem 4
[2440.02 --> 2440.66]  is released, you
[2440.66 --> 2440.78]  know.
[2442.16 --> 2443.04]  I'm on the same
[2443.04 --> 2443.78]  Vim journey and I
[2443.78 --> 2444.88]  think we're probably
[2444.88 --> 2445.52]  watching the same
[2445.52 --> 2446.36]  peep code from
[2446.36 --> 2448.58]  Jeffrey with
[2448.58 --> 2449.48]  smashing into
[2449.48 --> 2450.10]  Vim with the
[2450.10 --> 2450.80]  soothing voice of
[2450.80 --> 2451.34]  Dan Benjamin.
[2451.34 --> 2453.30]  Yeah, it's a
[2453.30 --> 2453.88]  good one.
[2454.04 --> 2454.54]  It looks like I'm
[2454.54 --> 2455.10]  not the only guy
[2455.10 --> 2456.36]  that's looking for
[2456.36 --> 2457.14]  the perfect terminal
[2457.14 --> 2457.64]  font too.
[2457.82 --> 2458.42]  So, I noticed on
[2458.42 --> 2460.06]  your blog, I
[2460.06 --> 2460.76]  recently got turned
[2460.76 --> 2461.68]  on to Menlo from
[2461.68 --> 2462.50]  David Kaneda from
[2462.50 --> 2463.08]  the Essential
[2463.08 --> 2464.44]  Touch team and
[2464.44 --> 2465.52]  you found a
[2465.52 --> 2466.34]  variant of Menlo
[2466.34 --> 2467.06]  that you're really
[2467.06 --> 2467.36]  liking.
[2468.62 --> 2470.28]  Yes, so Menlo
[2470.28 --> 2471.20]  is a great font.
[2471.36 --> 2472.12]  It's based on
[2472.12 --> 2473.20]  Bitstream,
[2473.36 --> 2473.68]  Vera,
[2474.04 --> 2474.44]  Sans,
[2474.66 --> 2475.36]  Mono, I
[2475.36 --> 2476.74]  think, which is
[2476.74 --> 2477.34]  an open source
[2477.34 --> 2478.78]  font and Apple
[2478.78 --> 2479.94]  adopted that font
[2479.94 --> 2480.64]  as a new
[2480.64 --> 2481.32]  terminal font.
[2481.34 --> 2482.62]  for Snow
[2482.62 --> 2483.94]  Leopard and
[2483.94 --> 2484.28]  it's called
[2484.28 --> 2484.68]  Menlo.
[2485.76 --> 2486.72]  And some other
[2486.72 --> 2487.38]  people picked
[2487.38 --> 2488.44]  Menlo up and
[2488.44 --> 2489.74]  they had little
[2489.74 --> 2490.62]  gripes about it,
[2490.70 --> 2491.12]  you know, like
[2491.12 --> 2492.06]  the shape of the
[2492.06 --> 2492.96]  zero, for example,
[2493.52 --> 2494.76]  in Menlo that
[2494.76 --> 2496.08]  zero is slashed
[2496.08 --> 2497.28]  and lots of people
[2497.28 --> 2498.00]  prefer dotted
[2498.00 --> 2498.38]  zeros.
[2498.88 --> 2499.88]  So, people
[2499.88 --> 2500.70]  started to adopt
[2500.70 --> 2501.08]  the fonts.
[2501.24 --> 2501.60]  It's really
[2501.60 --> 2502.36]  interesting to see
[2502.36 --> 2503.38]  like this sort of
[2503.38 --> 2504.10]  like open source
[2504.10 --> 2505.48]  movement catching
[2505.48 --> 2506.80]  up into the
[2506.80 --> 2508.30]  space of typography
[2508.30 --> 2508.86]  and fonts.
[2509.00 --> 2509.52]  That's quite
[2509.52 --> 2510.12]  interesting, I
[2510.12 --> 2510.28]  think.
[2510.98 --> 2511.94]  And those
[2511.94 --> 2512.66]  people then put
[2512.66 --> 2513.20]  the fonts on
[2513.20 --> 2514.20]  GitHub somewhere
[2514.20 --> 2516.16]  and one of the
[2516.16 --> 2516.72]  fonts was called
[2516.72 --> 2518.36]  Mench, which was a
[2518.36 --> 2519.24]  variation with the
[2519.24 --> 2520.02]  dotted zero, but it
[2520.02 --> 2520.94]  also did some other
[2520.94 --> 2521.74]  changes that I
[2521.74 --> 2522.68]  didn't like, like it
[2522.68 --> 2523.64]  had bigger angle
[2523.64 --> 2525.38]  brackets, which
[2525.38 --> 2526.20]  kind of looked
[2526.20 --> 2526.44]  weird.
[2526.96 --> 2527.82]  But anyway, some
[2527.82 --> 2530.56]  other guy fixed an
[2530.56 --> 2531.56]  other problem I have
[2531.56 --> 2533.22]  with Menlo, which is
[2533.22 --> 2533.82]  that the line
[2533.82 --> 2535.32]  hates, it's pretty
[2535.32 --> 2536.84]  like dense if you
[2536.84 --> 2537.40]  use it in the
[2537.40 --> 2539.10]  terminal or in
[2539.10 --> 2540.44]  Vim, for example.
[2541.48 --> 2542.56]  So, what he did
[2542.56 --> 2543.66]  is he made a
[2543.66 --> 2544.38]  little improvement
[2544.38 --> 2545.16]  or a little
[2545.16 --> 2545.94]  variance of the
[2545.94 --> 2546.82]  font with bigger
[2546.82 --> 2547.62]  line heights, with
[2547.62 --> 2548.16]  like a small
[2548.16 --> 2549.70]  line height, medium
[2549.70 --> 2550.88]  and large, with
[2550.88 --> 2552.48]  more space between
[2552.48 --> 2552.90]  the lines.
[2553.44 --> 2554.44]  So, I asked that
[2554.44 --> 2556.12]  guy to, hmm, this
[2556.12 --> 2557.08]  looks awesome, I
[2557.08 --> 2557.88]  really like your
[2557.88 --> 2558.92]  medium variation
[2558.92 --> 2560.04]  there, but I
[2560.04 --> 2560.82]  would also like to
[2560.82 --> 2561.56]  have the dotted
[2561.56 --> 2562.30]  zero from the
[2562.30 --> 2562.74]  other font.
[2562.98 --> 2563.76]  And so, he just
[2563.76 --> 2564.52]  put it in and
[2564.52 --> 2565.30]  that's what I'm
[2565.30 --> 2565.98]  using now and
[2565.98 --> 2567.02]  that's what my
[2567.02 --> 2567.60]  blog post is
[2567.60 --> 2567.88]  about.
[2568.12 --> 2568.96]  So, it's
[2568.96 --> 2569.30]  awesome.
[2569.60 --> 2570.12]  Bash or
[2570.12 --> 2570.60]  ZShell?
[2572.26 --> 2572.98]  For me, it's
[2572.98 --> 2574.22]  Bash, but I
[2574.22 --> 2574.86]  haven't had the
[2574.86 --> 2575.82]  time yet to do
[2575.82 --> 2577.54]  ZShell yet, so
[2577.54 --> 2578.62]  maybe I will
[2578.62 --> 2579.26]  switch at some
[2579.26 --> 2579.52]  point.
[2580.62 --> 2581.06]  This is the
[2581.06 --> 2581.56]  part where I
[2581.56 --> 2582.30]  now get to ask
[2582.30 --> 2583.26]  my guests what
[2583.26 --> 2584.78]  got you excited
[2584.78 --> 2585.32]  about the world
[2585.32 --> 2585.92]  of open source
[2585.92 --> 2586.44]  and turned me
[2586.44 --> 2586.88]  on to new
[2586.88 --> 2587.92]  projects to go
[2587.92 --> 2588.34]  and explore.
[2589.26 --> 2590.12]  What got me
[2590.12 --> 2591.28]  turned on about
[2591.28 --> 2591.86]  the world of
[2591.86 --> 2592.24]  open source?
[2592.62 --> 2594.02]  I think at the
[2594.02 --> 2594.78]  time I was
[2594.78 --> 2595.28]  really getting
[2595.28 --> 2595.80]  into open
[2595.80 --> 2596.18]  source, I
[2596.18 --> 2596.62]  didn't even
[2596.62 --> 2597.40]  realize it.
[2598.18 --> 2599.20]  I got into
[2599.20 --> 2599.84]  open source
[2599.84 --> 2600.50]  because I was
[2600.50 --> 2602.52]  researching what
[2602.52 --> 2603.78]  else is out
[2603.78 --> 2604.40]  there except
[2604.40 --> 2605.66]  for like Java
[2605.66 --> 2607.12]  or PHP to
[2607.12 --> 2607.66]  make a web
[2607.66 --> 2608.22]  application.
[2608.68 --> 2609.08]  Because at
[2609.08 --> 2609.62]  that time we
[2609.62 --> 2610.18]  were planning a
[2610.18 --> 2610.80]  web application
[2610.80 --> 2611.28]  that was in
[2611.28 --> 2611.88]  like 2004.
[2613.14 --> 2614.96]  And so, I
[2614.96 --> 2615.54]  just researched
[2615.54 --> 2615.96]  on the internet
[2615.96 --> 2616.58]  and I stumbled
[2616.58 --> 2617.62]  upon this Ruby
[2617.62 --> 2618.46]  and this Rails
[2618.46 --> 2619.58]  thing and that
[2619.58 --> 2620.24]  got me kind of
[2620.24 --> 2621.16]  interested in it
[2621.16 --> 2623.58]  and I checked
[2623.58 --> 2625.12]  out the IRC
[2625.12 --> 2625.90]  channel for it,
[2625.98 --> 2626.32]  asked some
[2626.32 --> 2627.00]  questions and
[2627.00 --> 2627.66]  like three months
[2627.66 --> 2628.22]  later I was on
[2628.22 --> 2628.84]  the core team of
[2628.84 --> 2629.32]  Ruby on Rails.
[2629.50 --> 2630.00]  So, that was
[2630.00 --> 2630.84]  pretty quick.
[2631.10 --> 2632.22]  So, I didn't even
[2632.22 --> 2633.26]  know what happened
[2633.26 --> 2633.94]  there exactly.
[2634.14 --> 2635.96]  But since then I'm
[2635.96 --> 2636.86]  a big fan of
[2636.86 --> 2637.88]  open source and
[2637.88 --> 2639.86]  it's not good for
[2639.86 --> 2640.34]  everything.
[2640.92 --> 2641.58]  For example, I
[2641.58 --> 2642.50]  wouldn't recommend
[2642.50 --> 2643.82]  designing anything
[2643.82 --> 2645.20]  open source, like
[2645.20 --> 2646.06]  visual design or
[2646.06 --> 2646.36]  something.
[2646.36 --> 2647.52]  that just doesn't
[2647.52 --> 2648.04]  work well.
[2648.74 --> 2649.86]  But for code it's
[2649.86 --> 2650.80]  really, really
[2650.80 --> 2651.16]  great.
[2651.50 --> 2652.62]  Especially if you
[2652.62 --> 2653.64]  can find projects
[2653.64 --> 2654.72]  where you have a
[2654.72 --> 2655.98]  benevolent dictator
[2655.98 --> 2657.10]  that really knows
[2657.10 --> 2657.98]  what he or she is
[2657.98 --> 2658.32]  doing.
[2659.20 --> 2660.64]  And if you have
[2660.64 --> 2661.48]  programmers that
[2661.48 --> 2662.72]  just connect to
[2662.72 --> 2663.36]  you on the same
[2663.36 --> 2663.72]  level.
[2664.56 --> 2665.68]  I can remember
[2665.68 --> 2667.18]  having chats in
[2667.18 --> 2667.90]  like the Ruby on
[2667.90 --> 2669.26]  Rails core team
[2669.26 --> 2669.80]  channel.
[2670.94 --> 2672.06]  Very, very
[2672.06 --> 2673.44]  good talk about
[2673.44 --> 2674.06]  stuff that we
[2674.06 --> 2674.92]  wanted to implement
[2674.92 --> 2675.64]  in the framework
[2675.64 --> 2677.62]  and we also
[2677.62 --> 2679.08]  agreed on what
[2679.08 --> 2679.78]  the reaction should
[2679.78 --> 2680.06]  be.
[2681.08 --> 2682.12]  It was actually a
[2682.12 --> 2683.18]  bit scary to find
[2683.18 --> 2684.28]  people from all
[2684.28 --> 2684.98]  over the world to
[2684.98 --> 2686.14]  have exactly those
[2686.14 --> 2686.78]  same thoughts.
[2687.60 --> 2689.24]  But that's what's
[2689.24 --> 2689.72]  happened there.
[2690.14 --> 2691.26]  So, I can only
[2691.26 --> 2691.96]  recommend if you
[2691.96 --> 2694.42]  want to, as a
[2694.42 --> 2694.92]  listener, if you
[2694.92 --> 2696.30]  want to go into
[2696.30 --> 2697.02]  the world of open
[2697.02 --> 2698.08]  source and explore
[2698.08 --> 2698.98]  more and find a
[2698.98 --> 2699.78]  project that you can
[2699.78 --> 2700.42]  actually contribute
[2700.42 --> 2702.02]  to, find something
[2702.02 --> 2702.84]  that you're really,
[2702.96 --> 2704.08]  really excited
[2704.08 --> 2704.48]  about.
[2705.64 --> 2706.26]  that you really,
[2706.38 --> 2708.42]  really want to
[2708.42 --> 2708.98]  make better.
[2709.20 --> 2710.14]  Do not try to get
[2710.14 --> 2711.04]  into a project just
[2711.04 --> 2712.30]  because it doesn't
[2712.30 --> 2712.64]  work.
[2712.78 --> 2714.16]  If you want to go
[2714.16 --> 2714.98]  into a project and
[2714.98 --> 2715.66]  really make it
[2715.66 --> 2716.28]  better, find
[2716.28 --> 2717.78]  something that you're
[2717.78 --> 2718.58]  actually really
[2718.58 --> 2719.26]  excited about.
[2719.36 --> 2720.00]  There's so many
[2720.00 --> 2720.76]  projects out there,
[2720.80 --> 2721.46]  I'm sure there's
[2721.46 --> 2722.16]  something for you.
[2722.24 --> 2722.74]  What's got you
[2722.74 --> 2723.36]  excited that you
[2723.36 --> 2723.98]  just want to play
[2723.98 --> 2724.62]  with when you
[2724.62 --> 2726.36]  have some downtime?
[2728.22 --> 2728.94]  Actually, like,
[2729.00 --> 2729.44]  all sorts of
[2729.44 --> 2731.04]  gadgets and stuff.
[2731.04 --> 2732.02]  like, I just
[2732.02 --> 2733.60]  ordered a drone,
[2734.38 --> 2736.24]  an AR drone,
[2736.86 --> 2738.36]  which I have been
[2738.36 --> 2739.18]  flying around the
[2739.18 --> 2739.44]  office.
[2739.60 --> 2740.22]  It's kind of
[2740.22 --> 2741.14]  dangerous, actually.
[2742.70 --> 2743.74]  But that gets me
[2743.74 --> 2744.00]  excited.
[2744.34 --> 2745.20]  I also recently
[2745.20 --> 2746.76]  completed my project
[2746.76 --> 2747.58]  of building the
[2747.58 --> 2748.80]  Lego Millennium Falcon,
[2748.96 --> 2749.98]  the big one, with
[2749.98 --> 2750.92]  the help of some
[2750.92 --> 2751.24]  friends.
[2751.40 --> 2752.18]  That was quite
[2752.18 --> 2752.84]  awesome, also.
[2753.50 --> 2755.18]  So, I like building
[2755.18 --> 2757.12]  things, and I like
[2757.12 --> 2758.52]  creating things, even
[2758.52 --> 2759.04]  when it's not
[2759.04 --> 2759.54]  programming.
[2759.54 --> 2761.44]  One last question,
[2761.50 --> 2762.42]  I wanted to get an
[2762.42 --> 2763.40]  update on Schnitzel
[2763.40 --> 2763.68]  Conf.
[2765.38 --> 2766.00]  Schnitzel Conf,
[2766.44 --> 2766.72]  yeah.
[2769.18 --> 2770.30]  Amy and me, we
[2770.30 --> 2771.38]  did a conference in
[2771.38 --> 2772.60]  September on
[2772.60 --> 2773.54]  bootstrapping
[2773.54 --> 2775.10]  businesses, especially
[2775.10 --> 2776.70]  web-based businesses
[2776.70 --> 2778.58]  in Vienna, because
[2778.58 --> 2780.40]  the reasoning to do
[2780.40 --> 2780.94]  this is because
[2780.94 --> 2781.88]  there's so many
[2781.88 --> 2782.70]  people out there
[2782.70 --> 2783.32]  that think they
[2783.32 --> 2784.52]  need venture
[2784.52 --> 2786.48]  capital to do
[2786.48 --> 2787.60]  software or
[2787.60 --> 2788.28]  companies or
[2788.28 --> 2788.72]  projects.
[2788.72 --> 2790.06]  that's entirely
[2790.06 --> 2790.72]  not true.
[2790.92 --> 2791.34]  We built
[2791.34 --> 2792.06]  everything we
[2792.06 --> 2793.16]  did without any
[2793.16 --> 2794.44]  venture capital or
[2794.44 --> 2795.94]  third-party money.
[2796.22 --> 2797.14]  It's all our money
[2797.14 --> 2797.56]  in there.
[2798.10 --> 2799.04]  And we weren't
[2799.04 --> 2799.98]  rich before we
[2799.98 --> 2800.62]  started this.
[2800.88 --> 2801.88]  So, we just did
[2801.88 --> 2802.68]  some consulting on
[2802.68 --> 2803.46]  the side and
[2803.46 --> 2804.56]  invested the money
[2804.56 --> 2805.10]  that we earned
[2805.10 --> 2806.66]  there into our
[2806.66 --> 2807.74]  own products, and
[2807.74 --> 2808.86]  that works fine, and
[2808.86 --> 2809.62]  now we can live
[2809.62 --> 2810.14]  with our own
[2810.14 --> 2810.82]  products, which is
[2810.82 --> 2811.08]  awesome.
[2811.08 --> 2812.38]  And I can tell
[2812.38 --> 2813.96]  you that we can
[2813.96 --> 2814.96]  live pretty well
[2814.96 --> 2816.54]  of our own
[2816.54 --> 2816.92]  products.
[2816.92 --> 2818.02]  So, we wanted
[2818.02 --> 2818.72]  to spread this
[2818.72 --> 2819.36]  knowledge because
[2819.36 --> 2820.02]  there's so many
[2820.02 --> 2821.24]  people and
[2821.24 --> 2822.08]  developers and
[2822.08 --> 2822.96]  designers and
[2822.96 --> 2823.84]  entrepreneurs out
[2823.84 --> 2825.52]  there that always
[2825.52 --> 2826.68]  think they need to
[2826.68 --> 2829.22]  live up to some
[2829.22 --> 2831.44]  idea of how it
[2831.44 --> 2832.22]  should be that
[2832.22 --> 2833.30]  someone else told
[2833.30 --> 2833.58]  them.
[2834.10 --> 2835.24]  Like, you have to
[2835.24 --> 2836.58]  go to university and
[2836.58 --> 2837.40]  finish with a
[2837.40 --> 2838.40]  diploma, or you
[2838.40 --> 2839.54]  have to finish high
[2839.54 --> 2840.12]  school even.
[2840.60 --> 2841.98]  You have to do
[2841.98 --> 2842.76]  this, you have to
[2842.76 --> 2844.00]  do that, you have to
[2844.00 --> 2844.88]  take venture capital
[2844.88 --> 2845.76]  money, or otherwise
[2845.76 --> 2846.58]  your company will
[2846.58 --> 2847.34]  fail on the first
[2847.34 --> 2847.56]  day.
[2847.92 --> 2848.86]  It's all bullshit.
[2849.54 --> 2850.30]  It's really, it's
[2850.30 --> 2851.60]  all about doing
[2851.60 --> 2852.28]  your own thing.
[2853.02 --> 2854.08]  If you really want
[2854.08 --> 2854.66]  to do your own
[2854.66 --> 2856.04]  thing, like creating
[2856.04 --> 2856.92]  a product for time
[2856.92 --> 2857.26]  tracking.
[2858.20 --> 2859.00]  Creating a product
[2859.00 --> 2859.62]  for time tracking
[2859.62 --> 2861.16]  that was in a
[2861.16 --> 2862.00]  space where there's
[2862.00 --> 2863.48]  like bazillions of
[2863.48 --> 2864.50]  other products out
[2864.50 --> 2864.76]  there.
[2865.20 --> 2865.84]  But the problem
[2865.84 --> 2866.32]  with those other
[2866.32 --> 2867.12]  products is they're
[2867.12 --> 2867.80]  all not good.
[2868.42 --> 2869.48]  The people that did
[2869.48 --> 2870.00]  those products
[2870.00 --> 2871.28]  obviously don't care
[2871.28 --> 2871.70]  about their
[2871.70 --> 2873.24]  products, or are
[2873.24 --> 2875.02]  just to dump, I
[2875.02 --> 2875.36]  don't know.
[2878.92 --> 2879.80]  Maybe that was a
[2879.80 --> 2880.36]  bit too harsh.
[2883.72 --> 2886.14]  But some of them
[2886.14 --> 2886.98]  actually care, some
[2886.98 --> 2887.66]  of those products are
[2887.66 --> 2888.98]  not bad, but a
[2888.98 --> 2889.66]  freckle is better,
[2889.86 --> 2890.72]  I think, because we
[2890.72 --> 2892.14]  really care about the
[2892.14 --> 2893.92]  user, and that's
[2893.92 --> 2894.60]  our thing.
[2894.88 --> 2896.24]  And we can make
[2896.24 --> 2897.20]  money and a profit
[2897.20 --> 2898.76]  by caring about
[2898.76 --> 2899.12]  users.
[2899.12 --> 2901.12]  And everyone's
[2901.84 --> 2902.52]  happy with that,
[2902.64 --> 2902.86]  you know.
[2902.86 --> 2904.24]  The users win, we
[2904.24 --> 2905.62]  win, perfect.
[2905.76 --> 2906.38]  Any plans to make
[2906.38 --> 2906.94]  this an annual
[2906.94 --> 2907.36]  conference?
[2908.16 --> 2908.84]  Yeah, we're
[2908.84 --> 2910.06]  actually planning a
[2910.06 --> 2911.02]  second edition of
[2911.02 --> 2911.78]  SchnitzelConf right
[2911.78 --> 2912.06]  now.
[2912.18 --> 2913.14]  We're not sure about
[2913.14 --> 2914.34]  which format, you
[2914.34 --> 2915.38]  know, if we do it
[2915.38 --> 2917.12]  annually, or every
[2917.12 --> 2918.30]  half year, or we
[2918.30 --> 2919.70]  change cities, or if
[2919.70 --> 2921.66]  we do like some
[2921.66 --> 2923.50]  sort of mini
[2923.50 --> 2924.26]  conferences in
[2924.26 --> 2925.36]  between, or online
[2925.36 --> 2926.18]  conferences, there's
[2926.18 --> 2926.68]  all sorts of
[2926.68 --> 2927.20]  possibilities.
[2927.40 --> 2928.48]  But we definitely
[2928.48 --> 2930.72]  want to have more
[2930.72 --> 2931.36]  of those
[2931.36 --> 2932.04]  bootstrapping
[2932.04 --> 2932.52]  conferences.
[2932.86 --> 2934.14]  Because we think
[2934.14 --> 2935.20]  bootstrapping is a
[2935.20 --> 2935.86]  really, really good
[2935.86 --> 2936.74]  option for a lot of
[2936.74 --> 2938.24]  people, especially in
[2938.24 --> 2939.44]  the web business with
[2939.44 --> 2941.52]  info products and web
[2941.52 --> 2942.84]  applications as software
[2942.84 --> 2943.38]  as a service.
[2943.38 --> 2944.26]  Because you do not
[2944.26 --> 2945.86]  need much money to get
[2945.86 --> 2946.24]  started.
[2946.24 --> 2947.32]  We started with a
[2947.32 --> 2949.20]  budget of maybe like
[2949.20 --> 2950.14]  a thousand dollars.
[2951.52 --> 2953.40]  Took us two months to
[2953.40 --> 2954.20]  implement the first
[2954.20 --> 2956.24]  version, and we made
[2956.24 --> 2956.86]  money from the
[2956.86 --> 2957.18]  beginning.
[2957.42 --> 2958.62]  So that's totally
[2958.62 --> 2959.36]  possible to do.
[2959.56 --> 2960.18]  Same for info
[2960.18 --> 2960.52]  products.
[2960.52 --> 2961.98]  It's even easier if
[2961.98 --> 2963.16]  you write a PDF about
[2963.16 --> 2963.98]  some topic you really
[2963.98 --> 2964.48]  know well.
[2966.48 --> 2967.00]  Perfect.
[2967.44 --> 2969.54]  People will pry it from
[2969.54 --> 2970.56]  your hands.
[2971.22 --> 2972.24]  They will pay your money
[2972.24 --> 2973.24]  for that because they
[2973.24 --> 2973.74]  want to know.
[2974.88 --> 2976.68]  Right now, if you would
[2976.68 --> 2977.64]  write a PDF about
[2977.64 --> 2979.56]  Node.js, or a PDF about
[2979.56 --> 2981.30]  Zepto, or a PDF about
[2981.30 --> 2983.32]  Vim, for example.
[2983.68 --> 2984.56]  There's no good cheat
[2984.56 --> 2985.34]  sheets about Vim.
[2985.90 --> 2986.64]  Write a good cheat
[2986.64 --> 2987.32]  sheet about Vim.
[2987.32 --> 2988.90]  People will love it, and
[2988.90 --> 2989.56]  people will pay your
[2989.56 --> 2990.10]  money for it.
[2990.64 --> 2991.82]  It's really not that
[2991.82 --> 2993.00]  hard to get started.
[2993.30 --> 2994.26]  And this is the thing we
[2994.26 --> 2995.20]  want to get across at the
[2995.20 --> 2995.66]  conferences.
[2996.54 --> 2997.02]  Good stuff.
[2997.10 --> 2997.54]  Good stuff.
[2997.74 --> 2998.48]  Thanks for joining us
[2998.48 --> 2998.70]  today.
[2999.44 --> 2999.98]  Thank you.
[3000.32 --> 3003.06]  And I hope we get many,
[3003.20 --> 3005.20]  many more podcasts from
[3005.20 --> 3006.20]  you guys, because you
[3006.20 --> 3007.44]  guys are also doing a
[3007.44 --> 3008.16]  pretty awesome job.
[3008.24 --> 3008.86]  Thank you for that.
[3009.06 --> 3009.32]  Thanks.
[3009.40 --> 3009.90]  Appreciate it.
[3009.90 --> 3028.02]  See it in my eyes.
[3028.02 --> 3030.72]  So how could I forget
[3030.72 --> 3035.96]  when I found myself for the
[3035.96 --> 3037.42]  first time?
[3037.42 --> 3041.92]  Safe in your arms at the
[3041.92 --> 3043.42]  dark fashion?
