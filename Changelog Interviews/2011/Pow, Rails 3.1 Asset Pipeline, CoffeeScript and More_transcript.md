[0.00 --> 3.26]  This week's episode is brought to you by SkyBalloon, makers of Capture.
[3.66 --> 6.54]  Capture is a video record button for your iPhone home screen.
[6.98 --> 11.58]  We've all had those moments of frustration waiting for the iPhone's default camera to initialize,
[12.00 --> 16.82]  only then to realize we're in the wrong mode and we need to switch and wait again.
[17.70 --> 20.98]  Capture solves that problem by being a dedicated video recording app.
[21.42 --> 24.50]  It's just 99 cents and is available on the App Store.
[24.50 --> 30.20]  Go to skyballoonstudio.com slash capture for a download link and also a cute video promo.
[45.60 --> 48.98]  Welcome to the ChangeLog episode 0.6.4.
[49.14 --> 50.24]  I'm Adam Stachowiak.
[50.46 --> 51.36]  And I'm Wyn Netherland.
[51.36 --> 52.54]  This is the ChangeLog.
[52.54 --> 54.32]  We cover what's fresh and new and open source.
[54.50 --> 57.94]  If you found us on iTunes, we're also on the web at thechangelog.com.
[58.34 --> 59.44]  We're also up on GitHub.
[59.86 --> 61.68]  Head to github.com slash explore.
[61.78 --> 66.70]  You'll find some trending repos, some feature repos from the blog, as well as our audio podcasts.
[66.88 --> 69.36]  And if you're on Twitter, follow ChangeLog Show.
[69.98 --> 70.94]  And me, Adam Stach.
[71.22 --> 73.88]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[74.62 --> 75.76]  Fun episode this week.
[75.84 --> 77.54]  Talk to Sam Stevenson over at 37signals.
[77.80 --> 81.54]  He's the guy behind PAL and PrototypeJS.
[82.54 --> 85.36]  And a bunch of other fun stuff.
[85.50 --> 89.72]  It helps sling the code behind the 37signals Basecamp mobile application.
[89.94 --> 96.04]  Talked a bit about Synco, which is the framework that they hope to extract out of that application.
[96.58 --> 98.20]  Everybody's wanting the deets on.
[98.96 --> 101.24]  And I bet you were excited to hear his thoughts on CoffeeScript.
[101.24 --> 107.82]  Oh, CoffeeScript and how it plays into the Rails 3.1 asset pipeline, which we had a number of questions on.
[107.92 --> 113.96]  Hopefully, we can save some folks some, I guess, knuckle scraping, as it were.
[114.20 --> 114.68]  There you go.
[114.76 --> 119.54]  Everybody that's been playing with Rails 3.1 has been having a time of it with the asset pipeline.
[119.82 --> 121.86]  It's lightly documented, but very powerful.
[122.32 --> 122.78]  Absolutely.
[123.34 --> 126.58]  And next week, we'll be out in Dallas at the Big D Conference.
[126.58 --> 136.50]  Yeah, if you're out at the Big Design Conference here in Big D, I guess it's Friday and Saturday of this week, July 15th and 16th.
[136.74 --> 137.18]  Say hello.
[137.38 --> 141.90]  I'll be presenting on Accelerated Style Sheets with a friend of the show, Nathan Smith.
[142.54 --> 146.32]  I hate to say the 960 guy, but that's his claim to fame.
[146.40 --> 148.20]  But he's a JavaScripter in his own right.
[148.60 --> 149.16]  There you go.
[149.26 --> 150.06]  And he's a good one, too.
[150.12 --> 155.18]  He's got a lot of fun projects at DappJS, which we used at our daily gig, too.
[155.18 --> 155.86]  That's true.
[155.98 --> 157.06]  DappJS is fun.
[157.44 --> 161.56]  He's got a lot of formalized JS, I guess, is the other one that's really big, too.
[161.86 --> 163.12]  What doesn't he have?
[163.64 --> 164.50]  That is true.
[164.74 --> 165.28]  That is true.
[165.62 --> 167.32]  But this isn't a Nathan Smith episode.
[167.46 --> 168.64]  Check out a different episode for that.
[169.82 --> 170.80]  Fun episode this week.
[170.86 --> 171.40]  Should we get to it?
[171.52 --> 172.14]  Let's do it.
[172.14 --> 190.16]  We're chatting today with Sam Stevenson from 37signals and purveyor of PAL, Prototype, JS, and some other frameworks.
[190.52 --> 194.92]  So, Sam, why don't you introduce yourself a little bit about what you do at 37signals?
[194.92 --> 199.66]  Hey, so I do a little bit of everything at 37signals.
[202.06 --> 204.92]  Well, you're like a designer and a coder, right?
[205.44 --> 206.10]  No, no, no.
[206.14 --> 207.40]  Just a programmer here.
[209.02 --> 209.74]  Let's see.
[211.34 --> 213.92]  You did a good introduction for me.
[215.86 --> 220.24]  I'll just say what technologies you work with.
[220.24 --> 220.92]  All right.
[221.98 --> 226.30]  Yeah, so I'm a Ruby and JavaScript programmer at 37signals.
[227.14 --> 229.26]  I've been here since 2005.
[230.36 --> 232.50]  I was an early contributor to Rails.
[233.70 --> 237.10]  Created Prototype in early 2005.
[237.72 --> 243.88]  And since then, I've done some other stuff, including Sprockets, PAL,
[243.88 --> 250.58]  and a couple of smaller projects like Stitch and Exec.js.
[250.90 --> 252.26]  You've got quite the lineup.
[252.58 --> 255.84]  And, you know, we're probably going to end up splitting this into two episodes.
[256.04 --> 261.62]  So if you're listening to this and we don't cover one of your favorite libraries that you like of Sam's,
[261.70 --> 265.92]  then stay tuned to either part one or come back for part two or come back to part one
[265.92 --> 268.70]  and circle back and catch the rest of this.
[269.18 --> 270.76]  Plus, you do some awesome show notes, too.
[270.82 --> 272.00]  So I don't have a problem with that.
[272.30 --> 273.32]  They shouldn't have a problem with that.
[273.32 --> 274.74]  We have the best show notes in the business.
[275.18 --> 275.74]  That's what we heard.
[276.10 --> 281.76]  So, Sam, the reason that you came to mind most recently was PAL.
[281.90 --> 283.52]  Adam and I are big fans of PAL.
[283.52 --> 286.08]  Tell us a little bit about PAL and how it came about.
[286.28 --> 286.70]  That's awesome.
[286.88 --> 293.60]  So PAL was, like all good open source projects, a product of frustration.
[293.60 --> 298.92]  At 37signals, we have something like 20 applications.
[299.56 --> 304.06]  And each one needs to run at its own domain name.
[305.20 --> 310.48]  And most of the applications scope accounts by subdomain.
[310.48 --> 320.36]  So it's important to have, in the past, we would have huge host files set up so we could test things out in development.
[320.84 --> 329.34]  And every time you'd set up a new machine, it was a hassle to get all the apps installed and then to get the host file set up and everything.
[329.34 --> 332.46]  So I thought, surely there's a better way.
[332.46 --> 346.46]  And at the time, I was playing around with Node.js and CoffeeScript and just sort of came up with this really quick and dirty thing that spawned.
[346.46 --> 349.16]  It would automatically spawn Unicorn.
[350.86 --> 355.62]  And my coworker, Josh Peake, took a look at it and said, that's shit.
[356.18 --> 366.58]  And pulled that out and came up with this really awesome library called Knack, which is a Node.js adapter to Rack.
[367.66 --> 373.36]  And from there, we continued to build PAL out and added the cool DNS stuff to it.
[373.36 --> 378.96]  And it's been a big time saver for us all here at 37.
[379.48 --> 385.54]  So when I'm describing PAL to newcomers, I guess I'm drawing a comparison a lot of times to Passenger.
[385.62 --> 386.46]  I'm not sure if that's fair.
[386.56 --> 387.56]  Were you using Passenger?
[388.00 --> 390.24]  Yeah, that's what most of us were using before.
[390.36 --> 392.46]  Some of us were using Nginx also.
[392.98 --> 400.98]  The problem with Passenger for me was having now in this kind of hybrid mode where all of us are running multiple Rubies for the most part.
[400.98 --> 405.58]  It was just a problem running multiple Ruby installations with your Passenger setup.
[405.82 --> 407.08]  But PAL supports that, right?
[407.22 --> 407.52]  Definitely.
[407.74 --> 409.12]  And that was kind of an accident.
[409.88 --> 411.68]  It's a result of the way Knack works.
[413.48 --> 421.14]  But it's right around the time that this was coming to fruition, we started experimenting with using different versions of Ruby in our apps.
[421.14 --> 424.66]  And now we do have some apps on 1.9.
[425.40 --> 427.62]  Previously, we were all re.
[428.46 --> 433.72]  But, yeah, so it's great that it just works with RVM and Bundler.
[435.44 --> 437.32]  And for the most part, everything just works.
[438.56 --> 440.70]  What was the inspiration, I guess, for using the dev domain?
[440.78 --> 442.40]  Were you guys using that prior?
[442.40 --> 450.74]  We were actually using the test domain, which I think some RFC recommends you use for internal things.
[451.80 --> 456.96]  And then when Josh went to work at GitHub, he said that they were using dev internally.
[458.28 --> 461.74]  And at the time, there was no way to configure it.
[462.18 --> 464.08]  We later added an option to configure it.
[464.08 --> 473.96]  But I thought dev was more intention-revealing than test because it's about your development environment, not your test environment.
[476.20 --> 477.86]  I'm using a gem called Powder.
[478.68 --> 481.70]  It's kind of a command-line interface for configuring PAL.
[481.84 --> 482.34]  Yeah, yeah.
[482.36 --> 482.74]  I've used it.
[483.30 --> 484.42]  I have used Powder.
[484.94 --> 487.30]  It's sort of the missing command-line utility.
[487.60 --> 488.06]  It's great.
[488.06 --> 494.60]  So Node.js under the hood, which you mentioned CoffeeScript, but is it entirely CoffeeScript?
[494.84 --> 497.78]  Or as a JavaScript guy, do you sling any JavaScript in there?
[498.18 --> 504.90]  I personally love CoffeeScript and hope to never have to write JavaScript again.
[506.26 --> 509.74]  So as much of it is CoffeeScript as possible.
[510.64 --> 514.84]  The creator of Prototype.js hopes to never write JavaScript again.
[514.84 --> 520.00]  Well, I mean, when you're writing CoffeeScript, you are indeed writing JavaScript.
[520.94 --> 525.60]  But the nice part about CoffeeScript is that it's the good parts of JavaScript.
[526.24 --> 528.20]  And you're kind of sheltered from everything else.
[529.20 --> 531.02]  And it's just a much more pleasant environment.
[532.18 --> 532.86]  It's funny, actually.
[532.94 --> 536.14]  I'm in the process of learning JavaScript, and you don't want to write it anymore.
[538.32 --> 538.72]  Yeah.
[540.48 --> 543.94]  It's, you know, CoffeeScript just makes it so much better.
[543.94 --> 548.06]  So for someone who doesn't know JavaScript well, or say they're a front-end developer,
[548.28 --> 555.42]  and they want to do more snazzy stuff with their HTML and CSS, you know, saying you want
[555.42 --> 557.48]  to write CoffeeScript means no JavaScript.
[557.66 --> 561.68]  How do you propose someone who's just learning the language in general to jump into this?
[561.86 --> 566.96]  Should they jump into CoffeeScript and go shorthand, or should they camp out in JavaScript and
[566.96 --> 567.68]  learn that first?
[567.80 --> 569.10]  You should learn JavaScript first.
[569.60 --> 572.40]  When you're writing CoffeeScript, you're still working with JavaScript.
[572.40 --> 574.14]  The object model is the same.
[575.98 --> 580.52]  It's, you know, it's still closures and functions and prototypes all the way through.
[580.92 --> 587.74]  But the key difference to me is that when I look at a piece of JavaScript code, I see
[587.74 --> 593.26]  parentheses and braces and semicolons and line noise.
[593.72 --> 596.30]  And when I look at CoffeeScript, I can see the code that I've written.
[596.30 --> 604.84]  And when I'm writing CoffeeScript, I'm still sort of thinking in JavaScript, but I just have
[604.84 --> 605.42]  to type less.
[605.42 --> 612.06]  One of the digs on CoffeeScript, and I must disclose I'm a big CoffeeScript fan, but one
[612.06 --> 616.98]  of the digs on CoffeeScript is just the debugging overhead of matching source line with output
[616.98 --> 617.38]  line.
[617.54 --> 621.08]  Have you run into any problems or you ever got into code where it's just hard to debug?
[621.08 --> 626.96]  I find it's pretty easy to map up the source lines, especially since it doesn't mangle your
[626.96 --> 628.38]  variable names or anything like that.
[629.32 --> 635.72]  And for the most part, it's a one-to-one mapping between source lines in CoffeeScript and source
[635.72 --> 636.36]  lines in JavaScript.
[638.94 --> 641.84]  Command F is your friend there.
[641.84 --> 647.02]  But just for the most part, it has not been a problem for me.
[647.72 --> 648.98]  This sounds disjointed.
[649.24 --> 652.28]  In post, we had a little hiccup with our network connection.
[652.38 --> 654.44]  We were chatting about debugging CoffeeScript.
[654.72 --> 656.78]  So what's been your experience, Sam?
[658.04 --> 666.90]  So a lot of people mentioned that they're skeptical about debugging compiled CoffeeScript code because
[666.90 --> 668.22]  the line numbers don't match up.
[668.22 --> 675.38]  And in my experience, this hasn't really been a problem because CoffeeScript is good about
[675.38 --> 676.94]  not mangling your variable names.
[678.24 --> 684.74]  And for the most part, you get a one-to-one mapping between CoffeeScript source line and
[684.74 --> 685.74]  JavaScript source line.
[686.26 --> 692.42]  So even if the numbers don't match up, it's very easy to Command F and find where you were
[692.42 --> 692.94]  in the file.
[693.78 --> 697.74]  You know, when Jeremy came out with CoffeeScript, one of the very first things he did was, I
[697.74 --> 702.26]  guess, port underscore to Coffee just as a one-to-one comparison.
[702.48 --> 705.12]  Have you played around with porting prototype at all?
[705.48 --> 705.66]  No.
[705.88 --> 707.74]  So I don't actually...
[707.74 --> 709.58]  I haven't worked on prototype in a couple of years.
[709.92 --> 712.50]  I passed that off to the core team a while ago.
[713.98 --> 720.18]  But that underscore example is a beautiful example of what you can do when you go from
[720.18 --> 721.38]  JavaScript to CoffeeScript.
[721.38 --> 728.60]  So before we leave prototype, there were some questions on Twitter about the future of prototype.
[729.12 --> 733.36]  And one user actually said in this age of jQuery.
[733.54 --> 734.92]  Are we in the age of jQuery?
[735.22 --> 736.52]  We definitely are, yeah.
[737.60 --> 740.12]  Is that your go-to framework these days?
[740.12 --> 748.92]  So we'll continue using prototype for our existing applications at 37signals because we have quite
[748.92 --> 754.86]  a bit of code written on that and it wouldn't really make a lot of sense to rewrite it all.
[755.62 --> 758.32]  But for new applications, we are going to be using jQuery, yeah.
[758.98 --> 762.50]  What are some of the most adventurous things you've done with jQuery so far as a company,
[762.60 --> 763.64]  maybe even individually?
[763.64 --> 771.18]  I think the real win is that designers can pick it up and easily prototype stuff just by putting
[771.18 --> 775.12]  together a few plugins and writing just a small amount of code.
[775.38 --> 776.70]  So it's great for that.
[776.88 --> 786.44]  And then when it's time to build it out more fully, it works about the same as any other JavaScript library.
[788.28 --> 793.38]  So what's your take on the latest, I guess, desktop in the JavaScript community around micro frameworks?
[793.64 --> 800.56]  Whether or not we need these monolithic libraries or kind of the Unix best of breed off-the-shelf micro frameworks?
[801.24 --> 802.66]  I like the idea.
[804.00 --> 814.32]  We have had experience with Zepto and Underscore and Backbone when we built our Basecamp mobile application.
[815.60 --> 816.70]  And Zepto is wonderful.
[816.70 --> 834.36]  I think the idea of taking an API and then targeting it to a specific class of browser is great for times when you're constrained on processing speed and data transfer.
[834.36 --> 846.12]  And then things like Underscore and Backbone are great too because they're just really simple ideas distilled down to single-purpose libraries.
[846.12 --> 855.28]  You know, last year we went over at Texas JavaScript and we had an interview with John Rezek who is the creator of jQuery, which you just talked about.
[855.98 --> 859.76]  And he was kind of prepping everybody with all the different browsers and all the different platforms.
[860.02 --> 863.38]  And in his talk he had said the mobile web is here and it was last year.
[863.42 --> 868.68]  And we were still not quite there yet, but a whole year later, are we at the mobile web?
[868.68 --> 872.56]  I'm not quite sure how to answer that.
[873.12 --> 878.96]  I think we're living in a WebKit world in mobile and it's wonderful.
[881.20 --> 887.78]  And I think there's some interesting things about doing mobile development right now.
[888.28 --> 894.60]  You can, for the most part, if you're targeting a smartphone, there's a high chance it's running a WebKit browser.
[894.60 --> 908.06]  And there's a high chance that it has relatively recent hardware, probably more recent than you can assume for people with desktop machines because of the way mobile contracts work.
[909.44 --> 915.36]  So I think it's great that we're seeing the hardware get faster and faster.
[916.60 --> 921.58]  WebKit get more and more features, bringing it closer to parity with desktop browsers.
[921.58 --> 927.14]  And it's really exciting to work on mobile apps, mobile web apps.
[928.34 --> 935.64]  The reason I ask that question in that kind of sense is because I know that I'm probably an edge case in this scenario, but I'm on Twitter a lot.
[935.70 --> 940.00]  I'm on some sort of application on my iPhone or a mobile device.
[940.52 --> 943.72]  And the links I click, they tend to go to websites in general.
[943.86 --> 947.56]  So those websites are either designed for or planned for mobile experiences.
[947.80 --> 950.18]  And the most often cases, they're not.
[950.18 --> 952.74]  And the times they are, I'm really happy as a user.
[953.12 --> 961.76]  But as a developer, I just wonder that as more and more people on the mobile platforms, I mean, you guys did the HTML5 version of Basecamp.
[961.88 --> 964.20]  So that's got to at least say something for mobile web.
[964.86 --> 965.32]  Yeah, definitely.
[966.46 --> 971.86]  I think the experience can be good whether or not you do a specific mobile version.
[971.86 --> 976.70]  There are a few things you can tweak to just make things more readable.
[978.56 --> 983.46]  But I use an iPhone, and I'm really happy with the way mobile Safari works.
[983.80 --> 994.84]  So John Gruber recently called out the Basecamp mobile app saying that if you're going to do a mobile web app, then don't try to mimic native applications.
[995.00 --> 996.44]  Just build something altogether web.
[996.44 --> 997.72]  Is that what you guys set out to do?
[998.22 --> 1002.26]  We definitely wanted it to feel like a web app.
[1003.10 --> 1013.58]  And I think that's important because when you choose not to do that, you end up having to replicate native functionality,
[1013.78 --> 1019.20]  or you end up trying to replicate native functionality with tools that can be slow or primitive.
[1019.20 --> 1027.56]  And this is what we've seen in the past with libraries that try to emulate native scrolling behavior, for example.
[1028.04 --> 1034.20]  So one thing we did in Basecamp mobile was we just decided that the content is going to be on the page,
[1034.26 --> 1036.32]  and the page is going to be what scrolls.
[1037.62 --> 1043.48]  And I think that worked out really nicely for us because the end result was the app felt very fluid.
[1043.48 --> 1051.18]  It felt like a web page still, and we missed not being able to have that fixed header at the top or the bottom.
[1051.44 --> 1052.88]  But in the end, it didn't really matter.
[1053.72 --> 1060.90]  So in the latest iOS beta, leaks have shown that position fix now works as expected.
[1061.38 --> 1061.46]  Yeah.
[1061.58 --> 1070.16]  You can dock those toolbars at the top or bottom just like you would expect them to behave instead of docking to the viewport rather than to the document.
[1070.16 --> 1080.74]  What other gaps do you see that need to be filled before you can really get a true immersive web experience versus what you would have to go to a native app to get?
[1080.96 --> 1085.90]  I'm super excited about the overflow scroll changes in iOS.
[1087.22 --> 1093.68]  One thing that I would like to see is support for uploading files.
[1093.68 --> 1103.84]  So on iOS, you cannot actually trigger, you know, there's no file system, user-visible file system, so you can't really open a file dialog.
[1105.10 --> 1110.86]  And so they just disable the input file elements.
[1111.56 --> 1115.54]  But it would be really nice if you could just choose a picture from your photo library, for example.
[1115.54 --> 1119.56]  You know, I do quite a bit of mobile development myself.
[1119.70 --> 1127.54]  And on iOS, you've got the screen density differences between the older iPhones and the iPads and then the iPhone 4 and the Retina display.
[1128.50 --> 1138.02]  Recently jumped into Android development and was just shocked at, you know, the matrix of screen sizes and screen resolutions.
[1138.18 --> 1140.10]  It's almost like a Microsoft product, you know.
[1140.22 --> 1140.62]  No kidding.
[1140.62 --> 1141.02]  Matrix.
[1143.30 --> 1149.18]  So what does that leave us from a front-end developer perspective of making sense of all that?
[1149.26 --> 1154.54]  Is this something we're going to deal with or are we going to have tools around that to make loading different resolutions easier?
[1154.54 --> 1159.20]  So what we did in Basecamp Mobile was we used double-size assets for everything.
[1160.16 --> 1162.10]  And they just scaled down automatically.
[1163.26 --> 1164.92]  And that seemed to work pretty well.
[1165.06 --> 1169.48]  So we went with the iPhone 4 resolution on all images.
[1170.62 --> 1172.18]  You know, which is kind of counterintuitive.
[1172.36 --> 1182.80]  We have been, I think, led down this track of WAP and older mobile technologies where you had to keep it as lean as you could because the bandwidth and processor was the problem.
[1182.80 --> 1189.06]  And as you mentioned earlier, you know, these are computers in our pockets that, you know, would have taken up rooms 20 years ago, right?
[1189.56 --> 1196.44]  So is there anything that maybe conventional wisdom that you debunked as you developed this app?
[1197.40 --> 1198.66]  Let me think about that for a minute.
[1200.62 --> 1203.38]  Well, let me put that another way.
[1203.50 --> 1209.10]  Is there gains that you thought, you know, weren't that important that turned out to be big?
[1209.20 --> 1210.80]  I mean, what are the bottlenecks?
[1210.88 --> 1213.06]  Is it number of assets and network calls?
[1213.14 --> 1214.30]  Is it size of assets?
[1214.30 --> 1221.50]  I think it was memory for us, really.
[1222.30 --> 1224.26]  Number of DOM elements on the page.
[1224.68 --> 1234.64]  And especially when you get into things like turning on hardware acceleration for certain elements, they use up more memory and they take longer to render.
[1234.64 --> 1245.08]  But the best part of all this is, you know, it just reinforces the idea that progressive enhancement is alive and well on the mobile web.
[1245.08 --> 1258.08]  Because we built this app, again, you know, all using our iPhones and test it routinely against Android and web OS and BlackBerry devices.
[1258.08 --> 1270.62]  And in the end, when it came to time to polish everything up and make sure we had a good experience on all the browsers, it was mostly just a matter of turning certain things off on the older browsers.
[1271.44 --> 1275.74]  Was the mobile app a complete 37Signals team effort or just a couple of you working on this?
[1275.74 --> 1282.40]  Yeah, it was me, Josh Peek, who no longer works with us, and Jason Zimdars as the designer.
[1283.06 --> 1284.50]  No, Jason in Oklahoma City?
[1284.68 --> 1285.56]  Yeah, that's right.
[1286.20 --> 1290.36]  So how does a project like that, I guess, get in the pipeline at 37Signals?
[1290.42 --> 1291.72]  What's your workflow?
[1291.98 --> 1301.06]  Do you prototype a couple of things and then go to Jason and DHH and say, hey, look what we have?
[1301.08 --> 1303.42]  Or is this something that you plan for it out in the future?
[1303.42 --> 1313.68]  It can work that way, but the way this particular project worked is that we all knew that we wanted a mobile version of Basecamp and our customers were asking for it.
[1314.42 --> 1321.06]  And so it was just a matter of balancing that with all the other things that we can do on all of our other projects with our limited team size.
[1321.06 --> 1336.30]  And eventually it became a priority, and we put some time aside to – we thought that we might be building more than just – more mobile apps than just Basecamp.
[1336.30 --> 1346.90]  So we took a little bit of time to do a tech investigation and just play around and see what we could build without really building anything.
[1348.32 --> 1350.14]  And we were happy with how that turned out.
[1351.12 --> 1354.40]  And so then we went full in on the Basecamp mobile project.
[1354.40 --> 1362.92]  There's another buzzword that kind of jumps in the playing field these days coined by – I think it was Paul Irish, wasn't it, Wyn?
[1363.74 --> 1364.58]  Responsible Web Design?
[1365.10 --> 1366.04]  That will be in the show notes.
[1366.28 --> 1366.80]  There you go.
[1366.80 --> 1372.92]  And Wyn and I, not long ago, we started this new gig together called Pure Charity.
[1373.50 --> 1378.70]  And we kind of took the mobile form factor approach first.
[1378.96 --> 1384.84]  So design for mobile first and then went up to the desktop, and we actually ended up using Adapt.js for it.
[1384.90 --> 1386.12]  And it was kind of sweet how it worked out.
[1386.24 --> 1390.26]  But in general, like yourself, what is the approach that you guys take?
[1390.28 --> 1391.58]  Do you take a mobile approach first?
[1391.58 --> 1395.82]  Or in general with your side projects, do you take a mobile approach first and then design the desktop version?
[1395.96 --> 1398.28]  And do you have the same markup?
[1398.44 --> 1402.84]  What are some of the different trends you go down towards actually designing an interface for it?
[1403.26 --> 1404.90]  We are right now desktop first.
[1405.04 --> 1406.24]  That may change in the future.
[1407.62 --> 1409.48]  But we focus on the desktop browser.
[1410.72 --> 1417.08]  And then we try to do things to make it work as nicely as possible and as many devices as possible.
[1417.08 --> 1434.36]  And then in some cases where we have a lot of people who need to use, for example, Basecamp on the go, need to check in on their to-do lists, their projects via email and stuff like that.
[1434.50 --> 1439.32]  Then we make the decision to go through and do like a full mobile version.
[1439.32 --> 1446.46]  But we have played around with the responsive design for an internal application.
[1446.80 --> 1448.28]  And we really liked that as well.
[1448.90 --> 1455.26]  I think that's a great sort of a judo way to make a mobile app.
[1455.96 --> 1462.94]  And being that you guys are the kings of frameworks, do you plan to use an existing framework, say like less, I think, what was it called?
[1462.94 --> 1469.68]  When less – it's not less JS or less like the SAS less kind of thing.
[1469.88 --> 1471.92]  It's the less web framework.
[1472.14 --> 1472.40]  Less CSS?
[1473.40 --> 1474.02]  No, no, no.
[1474.42 --> 1476.46]  The less framework.
[1476.70 --> 1479.94]  That's actually what it's called, less framework for lessframework.com.
[1480.02 --> 1482.56]  Do you actually plan to use a framework that's out there, do you think?
[1482.56 --> 1493.08]  Or is this something that you guys would take a look at and say, okay, we can probably do this a little bit better and actually create a usable framework to attack responsive web design?
[1493.92 --> 1495.04]  I'm not actually sure.
[1496.70 --> 1499.12]  I haven't personally worked on that.
[1499.32 --> 1504.00]  I've just seen the way it works on the phone and in the browser in this particular application.
[1505.24 --> 1506.90]  I'm not familiar with the less framework.
[1507.90 --> 1510.02]  I think the approach is simple enough.
[1510.20 --> 1511.84]  It's adaptive more or less.
[1511.84 --> 1523.76]  It starts out with some sort of framework where desktop version has 12 columns, mobile version has three, and they're using some sort of media queries or JavaScript to make that adjustment on the fly.
[1524.38 --> 1532.60]  I think in general we would probably keep that in-house and just use the stuff that CSS gives us, so the viewport queries.
[1533.14 --> 1539.26]  So several folks on the Twitter were asking about your various frameworks, and one of them was Cinco.
[1539.54 --> 1540.16]  What is Cinco?
[1540.16 --> 1546.46]  Cinco is what we came up with when we built Basecamp Mobile.
[1547.70 --> 1554.78]  And it exists right now only inside Basecamp Mobile, so it has not been fully extracted yet.
[1555.76 --> 1559.76]  And we sort of made the mistake of talking about it before it was ready to be released.
[1559.76 --> 1567.86]  And so now lots of people are sort of tapping their fingers and asking, when is it going to be done?
[1568.68 --> 1571.60]  I think ThinkVitamin fueled that buzz a little while back.
[1572.06 --> 1572.22]  Yeah.
[1572.22 --> 1577.36]  So right now it doesn't exist in a form outside of Basecamp Mobile.
[1578.44 --> 1580.68]  It's something that I hope to get to this year.
[1582.14 --> 1587.28]  But right now I've got a couple other projects that I'm working on wrapping up.
[1589.02 --> 1590.54]  Can you talk about the internals at all?
[1590.54 --> 1590.98]  Yeah.
[1590.98 --> 1591.02]  Yeah.
[1591.20 --> 1603.86]  It's built with Stitch, Backbone, CoffeeScript, Underscore, Septo.
[1603.86 --> 1610.18]  And we use JSDOM for testing.
[1610.84 --> 1620.78]  So by way of Stitch, you can actually load the application inside a node process, look it up to JSDOM, and write your tests that way.
[1621.16 --> 1623.62]  And that was really great for us.
[1623.62 --> 1630.26]  So Stitch for the uninitiated is a CommonJS, I guess, stitcher together for the browser?
[1630.44 --> 1630.64]  Right.
[1630.84 --> 1636.76]  It basically works like nodes require a function.
[1638.14 --> 1647.28]  You give it a set of paths, and it pulls in all the source code in those paths and puts them together in a single JavaScript file.
[1648.34 --> 1651.22]  And each of your source files becomes a CommonJS module.
[1651.22 --> 1654.26]  That would be a nice segue to Sprockets.
[1654.72 --> 1655.04]  Right.
[1655.70 --> 1658.82]  So it's new in Rails 3.1.
[1658.90 --> 1663.08]  So I guess the Rails 3.1 asset pipeline is based on Sprockets, is that right?
[1663.22 --> 1663.70]  That's correct.
[1664.42 --> 1672.58]  So one of the questions off of Twitter this afternoon was, how does the Sprockets approach differ from, say, Jamit?
[1672.58 --> 1682.34]  So Sprockets was originally created in, I think, 2008, 2009 maybe.
[1683.12 --> 1687.36]  And we needed it internally at 37.
[1687.90 --> 1697.92]  We have all these applications, and we needed to share common plugins across them, JavaScript plugins.
[1697.92 --> 1700.78]  And there was no really good way to do that.
[1703.40 --> 1712.14]  So I came up with Sprockets, which was a JavaScript packager that basically let you put code.
[1712.24 --> 1713.30]  It gave you a load path.
[1714.58 --> 1718.18]  You could have code live in vendor, for example.
[1718.18 --> 1727.24]  So we could have JavaScript plugins in their own separate Git repositories and then have them versioned specifically for each app.
[1727.88 --> 1729.78]  But in general, all share the same code.
[1731.36 --> 1737.36]  And we've been using that internally for, well, ever since then.
[1737.36 --> 1741.58]  I think it didn't really catch on.
[1742.18 --> 1746.04]  I probably didn't do a good job of explaining exactly why it's useful.
[1748.50 --> 1756.90]  And then Jamit came out a little bit later and took a more straightforward approach.
[1758.24 --> 1763.62]  You could enumerate your files, and it also handled CSS as well as JavaScript.
[1763.62 --> 1767.84]  And it's a really nice app.
[1768.24 --> 1769.78]  Sorry, a really nice plugin.
[1772.08 --> 1781.48]  So the new version of Sprockets came from our desire to want to bring this load path idea to Rails assets.
[1782.84 --> 1785.86]  And Josh Peek and I have been working on it for a while.
[1785.86 --> 1798.10]  But it's a rewrite of the original version of Sprockets that extends the load path idea to all types of assets.
[1798.44 --> 1807.04]  So JavaScript, CSS, images, Flash movies, MP3 files, whatever you want to serve.
[1807.04 --> 1820.10]  You can keep these files in, for example, a Ruby gem, which you can then keep under version management with Bundler in your application.
[1821.46 --> 1823.92]  And then pull them right into your app.
[1825.28 --> 1829.70]  So I think that's the biggest advantage of Sprockets.
[1829.70 --> 1839.96]  Other things that it does that Jamit does not do, it will automatically compile CoffeeScript code to JavaScript.
[1841.16 --> 1847.96]  It also automatically compiles SAS or SCSS or LESS to CSS.
[1847.96 --> 1855.64]  And I'm not sure if Jamit does anything with images or not.
[1856.22 --> 1861.18]  But with Sprockets, you can read those in as a data URI.
[1862.78 --> 1866.98]  Sprockets lets you add ERB interpolation to source files.
[1868.12 --> 1877.14]  So you can pull any image asset in from anywhere in your load path and get it as a data URI string.
[1877.96 --> 1878.88]  So that's pretty handy.
[1879.88 --> 1884.72]  So basically it pulls assets out of the public folder, makes them first class citizens the application, I guess.
[1884.86 --> 1885.08]  Exactly.
[1885.08 --> 1888.54]  In development mode, it enumerates all of them in the head.
[1888.60 --> 1891.48]  But in production mode, it concatenates them into one package?
[1891.48 --> 1894.30]  So by default, it concatenates everything all the time.
[1895.18 --> 1899.92]  There is a debug mode, which you can use in development if you want everything split out.
[1899.92 --> 1909.58]  So for CoffeeScript, what are you depending on to concatenate those files, the low-level Coffee compiler to stitch those together?
[1909.84 --> 1926.00]  We actually – Josh Peek and I have a project called ExecJS, which lets you bridge various JavaScript runtimes to Ruby.
[1926.00 --> 1942.40]  And since the CoffeeScript compiler is written in JavaScript, we basically just pull in the browser version of the CoffeeScript compiler, which lives in the CoffeeScript gem, and then invoke it with ExecJS.
[1942.40 --> 1949.42]  And ExecJS is cool because it will automatically pick the best runtime that you have installed.
[1950.32 --> 1958.00]  And by default, if you're on Windows or OS X, you have a JavaScript runtime available, and it will shell out to that.
[1958.84 --> 1960.90]  You can also install Node, and it will use that.
[1960.90 --> 1967.02]  And there's a great project called the Ruby Racer, which embeds V8 into Ruby.
[1968.28 --> 1969.04]  From Charles Lowell?
[1969.34 --> 1971.36]  That's correct, and it's an excellent project.
[1972.08 --> 1974.28]  And it will prefer that if you have it installed.
[1974.28 --> 1989.98]  So this CoffeeScript support, I guess, was the shot around the world back in April with Josh's famous commit on Rails 3 that included CoffeeScript and unfurled that massive comment thread on GitHub.
[1990.18 --> 1994.12]  Who got dibs on, I guess, checking that in?
[1994.14 --> 1997.84]  Did you guys discuss it, or it was just his turn to make that commit?
[1997.84 --> 2008.28]  Oh, yeah, that was – it was, I think, a long time coming, but Josh just finally did it, and it was fun to see the reaction to that.
[2009.34 --> 2011.76]  It's a very polarizing reaction.
[2011.86 --> 2013.94]  People either love CoffeeScript or hate it.
[2014.50 --> 2017.02]  It's great because it's just a line in a gem file, really.
[2017.94 --> 2025.62]  But it's a default, and I guess it's what – the defaults that Rails encourages tend to catch on.
[2025.62 --> 2026.44]  Yeah, they're blessings.
[2027.84 --> 2037.40]  Although they always don't always win out in the ends, I guess, CO, so prototype and via jQuery, right?
[2037.40 --> 2038.24]  Yep, yep.
[2039.12 --> 2041.14]  But opinions change over time, so.
[2041.98 --> 2047.52]  And I think that's what makes a great framework that's malleable and can change as our aesthetics change.
[2047.64 --> 2052.44]  So what other types of assets can we serve out of the assets folder?
[2052.44 --> 2056.48]  You mentioned JavaScript and CSS, of course, also images.
[2056.48 --> 2065.00]  But what about something – could we serve pretty much anything out of this with the tilt gem to be able to take markdown files and have HTML come out the other end?
[2065.08 --> 2066.26]  So that's a good question.
[2067.54 --> 2075.02]  Sprockets does use tilt internally, but it doesn't expose all of the built-in handlers.
[2075.02 --> 2088.06]  But you could certainly – it's extendable, so you could certainly write your own engine to use if you wanted to serve markdown files from Sprockets.
[2089.54 --> 2091.60]  I actually saw an interesting project.
[2091.70 --> 2092.94]  I'll try to get the link for you guys.
[2092.94 --> 2107.82]  Someone was working on this project that compiled a certain type of source file to JavaScript processing commands, which would then in turn render an image.
[2108.46 --> 2119.18]  So he was writing processing source as Sprockets source files, which when you request result in like a ping image being generated.
[2119.18 --> 2120.58]  So I thought that was really cool.
[2121.74 --> 2124.38]  I guess the boundaries are really limitless here.
[2124.48 --> 2126.82]  You could do the same thing with CSS sprites, right?
[2127.28 --> 2127.46]  Yeah.
[2130.34 --> 2134.20]  There's no good solution for CSS sprites in Sprockets yet.
[2135.04 --> 2139.88]  You can do data URIs in line, but hopefully somebody will figure that out.
[2139.88 --> 2148.84]  You know, I'm using it – I guess I should say we use it with Compass on the edge with Sass.
[2149.02 --> 2157.84]  I'm not using the application CSS manifest as much, just using Compass's built-in packaging because we're big Sass and Compass fans.
[2158.02 --> 2161.56]  But Compass also has its own spriting built in with Lemonade.
[2161.74 --> 2163.88]  I'm anxious to see how that shakes out.
[2164.06 --> 2165.48]  Yeah, maybe we can get that to play together.
[2165.70 --> 2166.26]  That would be nice.
[2166.26 --> 2166.86]  Absolutely.
[2167.06 --> 2169.80]  I know Chris Epstein's been working hard on that.
[2170.10 --> 2170.36]  Definitely.
[2170.52 --> 2171.00]  He's a great guy.
[2172.08 --> 2172.96]  Talking about that.
[2174.30 --> 2182.62]  So the learning curve for Sprockets, I guess, for the Rails 3 asset pipeline has been a steep one for me, and I've been in Rails since 2006.
[2183.68 --> 2185.14]  Is it a lack of documentation?
[2185.46 --> 2188.44]  Is it just a totally new way of looking at how we do our assets?
[2188.44 --> 2194.26]  Or what seems to be the, I guess, the stumbling block for Rails devs?
[2194.26 --> 2203.74]  Yeah, I'm working on the manual this week, and it's been a real challenge for me to explain Sprockets.
[2204.04 --> 2207.28]  It seems like something that should be simple to explain.
[2208.38 --> 2212.02]  But I think the difficulty is that it does three main things.
[2212.02 --> 2214.56]  It gives you the load path.
[2215.56 --> 2216.94]  It gives you the processing.
[2217.86 --> 2224.54]  So turning CoffeeScript or less files into the correct compiled output.
[2224.88 --> 2228.44]  And it also does dependency management.
[2229.22 --> 2237.40]  So it does hook in also to the Rails image tag helpers as well and serves those out of assets instead of out of public?
[2237.40 --> 2237.88]  Right.
[2237.88 --> 2238.24]  Right.
[2238.38 --> 2249.58]  So the way that works is Sprockets is actually you create a Sprockets environment for your application, and that's actually a rack app.
[2249.82 --> 2252.16]  So it gets mounted at slash assets.
[2253.40 --> 2259.52]  And so you can just request any asset in the load path after slash assets, and it's served on the fly.
[2259.52 --> 2264.32]  And if that asset has dependencies, those dependencies come in for it.
[2264.48 --> 2266.46]  So it implicitly creates bundles.
[2267.32 --> 2272.08]  So if we wanted to serve those, I guess, statically on a read-only file system such as Heroku,
[2272.72 --> 2280.78]  and take those out of public assets instead of dynamically hitting Rails, what are options for setups like that?
[2280.78 --> 2288.52]  When you go to deploy, there's a deploy task that will actually copy everything in your load path over to public.
[2290.10 --> 2296.20]  You can also put it behind a caching proxy, and everything should just work.
[2296.30 --> 2297.60]  Sprockets sets all the right headers.
[2298.34 --> 2305.86]  Now, one of my favorite parts about this conversation is just thinking about the – I guess what I bumped into recently was the asset pipeline,
[2305.86 --> 2310.28]  and I was calling things from Compass, and things just weren't working out well.
[2310.48 --> 2315.88]  And I think it's just probably in that middle ground where maybe it's not all fleshed out.
[2316.14 --> 2322.16]  In Rails 3.1, is this asset pipeline and some of the stuff you're talking about, is it all kind of finalized yet?
[2322.52 --> 2325.60]  I think the overall design is finalized, yeah.
[2327.68 --> 2330.90]  We need a bunch of people banging on it and filing bug reports.
[2331.44 --> 2332.16]  And how do they do that?
[2332.16 --> 2340.72]  Because, I mean, we've hit some bugs, and I know Chris, we mentioned before, Chris, I've seen on Compass is a big cheerleader for us,
[2340.84 --> 2348.34]  and the leader for us, and doing good work on Compass, and helping us with a number of SaaS things in general,
[2348.42 --> 2351.90]  but also Compass and CSS frameworking of all sorts.
[2352.04 --> 2356.94]  And this is something to win, and I use, and that was a bug that we recently kind of – I don't know if it's a bug or not,
[2356.94 --> 2364.76]  but basically in Compass you have this variable that they call us at the image path that you can set.
[2364.98 --> 2369.60]  And I wasn't getting – I wasn't sure where to put stuff, basically.
[2369.92 --> 2372.54]  You know, static assets like images and whatnot.
[2373.24 --> 2378.84]  It's been, I guess, hard finding the right cocktail of edge gems.
[2378.84 --> 2385.20]  Sometimes, anytime something's, you know, pre-release, finding the right version of SaaS and Compass, and then as well.
[2385.58 --> 2385.90]  Right.
[2386.24 --> 2388.68]  Yeah, it's been a shaky road.
[2389.10 --> 2396.92]  So when you say people need to file bugs and tickets and help you hit and bang on Rails 3.1, where can they feed back to you guys?
[2397.34 --> 2399.06]  The best place is the Rails bug tracker.
[2399.06 --> 2406.72]  And if it's not really a Rails issue, then we can redirect it to the right place.
[2407.60 --> 2418.04]  I guess one of the most exciting aspects of the asset pipeline is that now plug-ins and gems and bundles of application
[2418.04 --> 2427.18]  can hook into the Rails asset pipeline and provide assets without the need to run a rake task
[2427.18 --> 2430.22]  and copy those over to your public folder in some sort of generator, right?
[2430.40 --> 2431.88]  Yeah, and I think that's going to be huge.
[2432.32 --> 2438.64]  We already have been making good use of the Rails PJX plugin, which does just this.
[2439.28 --> 2441.42]  And it's actually written in CoffeeScript, which is cool.
[2441.58 --> 2444.78]  I came across this feature with the Formtastic Form Builder plugin.
[2445.82 --> 2455.24]  Prior to Rails 3.1, you had to run a rake task to copy their assets, their baseline assets, their style sheets, into the public folder.
[2455.24 --> 2458.48]  But now they can just take it into the asset pipeline and serve those.
[2458.52 --> 2461.64]  There's no need to do that, which is really cool.
[2461.72 --> 2465.90]  But it also begs the question, as more and more code is coming from gems,
[2466.58 --> 2475.80]  are we losing anything to, I guess, obscurity or magic in gain of this convenience?
[2476.66 --> 2477.72]  I don't know about that.
[2477.72 --> 2484.28]  It does seem a little weird to me that we're packaging assets or non-Ruby code in gems.
[2485.28 --> 2488.04]  But it's the tool that we have right now.
[2488.62 --> 2491.68]  I guess the takeaway is to always look at the gem source.
[2492.40 --> 2492.56]  Yeah.
[2492.56 --> 2499.24]  I think in the early days of Rails, before we even moved to gems for our plugin management,
[2499.52 --> 2502.56]  everything was script plugin install.
[2503.16 --> 2503.40]  Right.
[2503.48 --> 2504.86]  It was pulling from subversion, right?
[2505.38 --> 2507.50]  And unfurling these things down in the plugin folder.
[2507.56 --> 2508.46]  And it was right there in the project.
[2508.70 --> 2514.64]  And still people didn't open those folders and see exactly what this plugin was doing.
[2514.88 --> 2517.70]  They read a readme and said, hey, it does exactly what I want it to do.
[2517.70 --> 2526.20]  But even more so, when we moved to gem files or gem packages to manage these dependencies,
[2526.46 --> 2529.10]  it became even more of a black hole.
[2529.22 --> 2532.92]  And I'm just surprised how many Ruby devs don't go to the source and check it out.
[2533.46 --> 2534.84]  Yeah, it can be.
[2535.52 --> 2538.44]  The great thing is that you don't have to use a gem.
[2539.18 --> 2541.16]  It's a convenient way to distribute stuff.
[2541.28 --> 2545.28]  But you can also just check something out into the vendor directory.
[2545.28 --> 2549.28]  Sprockets will automatically look there for...
[2549.80 --> 2552.90]  It'll look for asset subdirectories inside that.
[2553.82 --> 2560.26]  There's also a vendor assets JavaScript's directory, too, which is where it's a great place to put,
[2560.34 --> 2562.18]  for example, all your jQuery plugins.
[2563.14 --> 2563.84]  So what's the benefit?
[2564.18 --> 2568.44]  Last week's episode, or I guess last episode has been a couple of weeks ago.
[2568.44 --> 2576.16]  So we talked to the guys over at CDNJS and talked about more and more JavaScript frameworks moving up to the content delivery networks.
[2576.72 --> 2582.90]  And so it's kind of a lateral move than bundling all your frameworks together.
[2583.16 --> 2593.46]  Have you noticed any gains in serving jQuery off of a CDN and just bundling your application assets versus bundling that version of jQuery in with your assets?
[2593.46 --> 2599.30]  There is some contention about this, but I feel like bundling everything in a single asset is the way to go.
[2600.50 --> 2611.14]  And, you know, you can also break that down a level further by grouping all your framework libraries together in one bundle
[2611.14 --> 2617.32]  and then all your application code in another bundle, which Sprockets lets you do pretty easily since everything is a bundle.
[2617.32 --> 2623.34]  But I don't really know if CDNs are worth it for most people.
[2624.38 --> 2630.92]  Maybe if you have a public site where you serve a lot of traffic on the front page.
[2631.50 --> 2636.88]  But for most applications, the bundle is requested once and then it's cached.
[2636.88 --> 2648.88]  So if you're not a regular on the show or listener of the show, you probably don't know that we have a running drinking game with the words Hamill and Sass on the show.
[2649.02 --> 2651.96]  I haven't mentioned Hamill yet.
[2652.14 --> 2654.20]  Maybe we'll later in the episode.
[2654.56 --> 2654.76]  Cheers.
[2655.42 --> 2655.68]  Cheers.
[2655.68 --> 2665.06]  I wanted to know how important was Sass's embracing of this new SCSS syntax?
[2665.72 --> 2670.10]  How critical of a factor was that in getting Sass support in Rails 3.1?
[2671.10 --> 2672.06]  I'm not sure.
[2672.42 --> 2679.20]  I can say that the big thing that excites me about Sass is support for nesting.
[2679.20 --> 2686.74]  And I know a lot of people use the advanced features like mix-ins and things like that.
[2686.94 --> 2690.54]  But just having nesting is such a huge improvement.
[2691.50 --> 2696.42]  And the fact that it's backwards compatible with your existing CSS really helps, I think.
[2697.60 --> 2700.98]  So it's going to be good to just spread this to as many people as possible.
[2701.80 --> 2707.94]  You know, we use gems to kind of package up our patterns and share them across applications with Compass.
[2707.94 --> 2715.50]  And you mentioned doing that with now your JavaScript assets and even your CSS assets and have those being served out of gems.
[2715.62 --> 2724.66]  And I think what excites me about that is, you know, we've kind of had this dual world set up between kind of client-side code and server-side code.
[2724.70 --> 2732.72]  And every time that there's an advancement on the client-side, then those static assets have to kind of migrate their way over and be versioned separately than the server-side code.
[2732.72 --> 2740.28]  But now, you know, if I want to take Adapt.js and turn it into, you know, an asset pipeline component, right?
[2740.46 --> 2742.72]  Now I can say, well, I'm just using Adapt.js version XYZ.
[2743.36 --> 2753.54]  And I know I'm getting the static asset that came from that without having to really worry about going back to the source, copying the static asset over, and always maintaining that versioning myself.
[2754.12 --> 2755.24]  Yeah, I think it's going to be a big win.
[2755.24 --> 2758.72]  And I'm excited to see what kind of stuff people are going to package up to.
[2759.10 --> 2772.00]  So I think there's some interesting opportunities for Rails plugins that also provide maybe just a small JavaScript asset, a small CSS file, or a couple of images.
[2772.68 --> 2777.86]  I want to circle back to PAL just for a moment and about a couple of aspects of PAL that I found intriguing.
[2777.86 --> 2788.84]  So I think one of the things that struck me when I came across the project, other than the great domain name PAL.cx, was how well-designed the website was.
[2789.06 --> 2792.66]  So give a shout-out to the artist behind this design.
[2793.24 --> 2800.88]  Jamie DeHansen at 37signals did an amazing job of explaining PAL visually.
[2800.88 --> 2810.82]  I had been talking to him for a while about, you know, I'd like to do a website, but I'm not sure how to make it interesting.
[2811.46 --> 2815.88]  And he had the great idea of making it about superheroes.
[2816.82 --> 2825.16]  So he did some really great drawings and then made the website sort of look like a newsprint piece of paper.
[2825.16 --> 2831.64]  Were you surprised by how quickly the adoption rate took off for PAL?
[2832.26 --> 2833.12]  Absolutely, yeah.
[2833.86 --> 2835.48]  It felt good.
[2835.64 --> 2838.30]  It felt like we really struck a chord with people.
[2840.18 --> 2844.60]  So I noticed the annotated source code, this seems to be a trend.
[2844.88 --> 2846.46]  I guess you used Docco for this?
[2846.56 --> 2848.72]  We used Docco, which is a wonderful tool.
[2848.72 --> 2856.04]  So it strikes me as just the right level of documentation for source.
[2856.34 --> 2857.14]  Absolutely, yeah.
[2857.28 --> 2865.46]  And I think the big one for Docco is that you can, in languages that are maybe a little bit twisted up,
[2865.92 --> 2870.44]  like are not languages but environments, like Node, where everything is asynchronous,
[2871.62 --> 2876.34]  you can very clearly explain your intent alongside the code.
[2876.34 --> 2879.30]  And I found it interesting.
[2879.96 --> 2883.92]  I didn't start out – PAL started out without any documentation,
[2884.36 --> 2887.22]  and then I went through and added the Docco stuff later.
[2888.36 --> 2894.84]  And I thought it was fascinating the way that it actually changed the code.
[2896.60 --> 2898.80]  As I would go through and document things,
[2899.34 --> 2902.16]  I would run into cases where they're too hard to explain.
[2902.16 --> 2906.98]  Something was too hard to explain or looked too awkward.
[2908.04 --> 2912.16]  And so I'd refactor it to be more linear, more narrative,
[2912.68 --> 2919.56]  and it matched up with the documentation and, in the end, seemed so much nicer.
[2920.44 --> 2923.78]  And I think that's half of the benefit of Docco.
[2923.78 --> 2928.30]  And the other half is that it makes it so much easier for anyone to come into the project
[2928.30 --> 2932.28]  and understand what's going on and contribute to change.
[2933.62 --> 2934.66]  You know, that's so right.
[2934.80 --> 2938.24]  I do a lot of titanium development in CoffeeScript.
[2938.94 --> 2941.08]  And when folks are coming to the project,
[2941.30 --> 2944.20]  I feel like there are certain aspects of the project that I want to document.
[2944.36 --> 2947.36]  But I want to make it part of the source code.
[2947.36 --> 2952.72]  But a lot of times the Java Doc format or those other formats are just verbose
[2952.72 --> 2955.58]  and using, you know, at tags and at params and, you know,
[2955.60 --> 2960.12]  just especially a dynamic language like JavaScript or Ruby.
[2960.32 --> 2964.94]  It just feels weird putting a lot of, you know, structure to your documentation.
[2965.10 --> 2969.56]  So sometimes more structure to your docs than you do your actual code.
[2969.68 --> 2973.10]  What makes this such a great project is it just reads it out of the comments,
[2973.10 --> 2976.78]  puts it over on the left-hand side in the left margin,
[2976.78 --> 2978.02]  and then you see the code on the right.
[2978.10 --> 2980.04]  But the other cool thing is it uses Markdown.
[2980.28 --> 2982.12]  So you can use Markdown inside of your comments,
[2982.28 --> 2984.68]  and you get a nice formatted set of docs.
[2984.96 --> 2986.94]  So this is actually the first time I'm hearing of this, though.
[2986.98 --> 2988.68]  So where did Docco come from?
[2989.62 --> 2992.08]  Or do I not spend enough time in source code and reading comments?
[2992.54 --> 2993.94]  It's a Jeremy Ashkenas joint.
[2994.10 --> 2996.82]  It's inspired by Rocco or Shaco, or is it the other way around?
[2997.00 --> 2999.70]  No, Docco came first, and then the others followed.
[3000.90 --> 3004.70]  So Rocco is the Ruby version, and Shaco is the...
[3004.70 --> 3006.82]  Docco is for shell scripts, I believe.
[3007.38 --> 3007.66]  Gotcha.
[3007.92 --> 3008.08]  Yeah.
[3009.12 --> 3012.24]  And so this is exclusive to Ruby, or is this just...
[3012.24 --> 3013.28]  So Rocco is for Ruby.
[3013.40 --> 3016.42]  I believe Docco is for JavaScript and CoffeeScript only, right?
[3016.50 --> 3022.10]  Or is it just you get CoffeeScript for free because it comes with JavaScript, right?
[3022.16 --> 3022.34]  Right.
[3022.38 --> 3023.36]  It's written in CoffeeScript.
[3024.10 --> 3026.54]  I've only used it with CoffeeScript.
[3026.54 --> 3028.16]  I believe it works with JavaScript as well.
[3029.04 --> 3030.84]  It's just such a beautifully simple idea.
[3031.16 --> 3034.02]  I think the implementation is under 100 lines of code, too.
[3034.02 --> 3035.38]  So what's up for POW?
[3035.46 --> 3040.34]  Anything on the roadmap that are bugs you'd like to squash or features you'd like to add?
[3040.82 --> 3042.26]  I'm pretty happy with it right now.
[3043.16 --> 3048.48]  One thing I would like to do when I have the time, or if anyone is motivated,
[3049.58 --> 3052.70]  I'd really like to see it running other languages.
[3052.70 --> 3069.70]  The Rack protocol is so similar to Python's Whiskey and Perl's PSGI that it seems like a no-brainer to support those languages as well.
[3069.70 --> 3076.72]  Rupac G., fan of the show, asked me on Twitter today, why no support for PHP?
[3076.92 --> 3078.24]  You want to support PHP and PAL?
[3078.60 --> 3082.88]  No, actually, you can install the Rack Legacy gem.
[3084.34 --> 3085.62]  I love the name of that gem.
[3087.32 --> 3088.48]  It's pretty opinionated.
[3088.48 --> 3099.48]  But it actually will shell out to the PHP CGI binary to run PHP files and then serve them up as Rack responses.
[3100.12 --> 3103.94]  So you can use that if you want to access PHP through PAL.
[3104.78 --> 3106.34]  So that's your dream, Adam.
[3106.40 --> 3107.92]  You can get your WordPress and your Rails out.
[3107.92 --> 3108.32]  There you go.
[3108.48 --> 3109.82]  I like playing with WordPress, too.
[3109.92 --> 3112.00]  You know, it's open source, right?
[3112.60 --> 3113.26]  It's good stuff.
[3113.30 --> 3113.60]  That's true.
[3114.40 --> 3116.06]  I can't knock those, but it's a good one.
[3116.56 --> 3118.42]  You know, we actually have one more question, actually.
[3118.50 --> 3125.80]  This is something that's come up to me quite a bit, too, which is LuckyDev, at LuckyDev, says,
[3126.08 --> 3129.98]  will JavaScript become the mainstream server-side language like Ruby on Rails?
[3130.34 --> 3133.50]  I mean, we're going on a trend where Node.js is used for more often.
[3133.50 --> 3138.18]  There's a lot more happening in the JS world since it's on all platforms, basically.
[3138.36 --> 3138.88]  What do you think?
[3139.82 --> 3142.66]  There's no question it's going to become more and more popular.
[3143.60 --> 3147.04]  I don't have a crystal ball, though.
[3147.66 --> 3150.04]  But you do my prototype, so.
[3151.44 --> 3159.04]  I certainly enjoy writing things, writing server-side things in Node.
[3159.98 --> 3165.46]  And I think the dream is to have an end-to-end JavaScript application, right?
[3165.46 --> 3171.06]  Like you have your front-end in JavaScript and your back-end in JavaScript, and you're sharing models between them.
[3171.06 --> 3173.48]  And I don't know if we'll ever get there.
[3173.48 --> 3179.98]  But as with all things in the web world, it's a slow march.
[3181.02 --> 3183.76]  And it'll be interesting to see how it plays out.
[3183.76 --> 3192.08]  You know, I guess Node, if it did anything, was call home the JavaScript diaspora from around the world.
[3193.28 --> 3193.46]  Right?
[3193.52 --> 3201.82]  All of these JavaScript coders were kind of embedded in the other server frameworks, and now they have rallied around this server framework.
[3201.82 --> 3214.20]  But as someone who writes JavaScript and JavaScript well and CoffeeScript and Evidently well and Ruby extremely well, if you were sitting down and you could pick any language to write a particular project, which one would you choose on syntax alone?
[3215.32 --> 3217.82]  It really depends on the project.
[3218.88 --> 3226.06]  But, gosh, there are a lot of things that I prefer now about CoffeeScript than Ruby.
[3227.76 --> 3228.28]  Comprehensions?
[3228.28 --> 3230.84]  Not so much comprehensions.
[3231.20 --> 3234.28]  I actually like the significant white space.
[3234.78 --> 3236.38]  I like not having to write end.
[3237.84 --> 3240.20]  I like that every line of code is significant.
[3242.04 --> 3246.24]  And I just like the simplicity of the language.
[3247.82 --> 3248.66]  I'm kind of the same way.
[3248.72 --> 3250.70]  If you write something, you want it to mean something.
[3250.70 --> 3251.26]  Yeah.
[3251.54 --> 3255.92]  A curly brace or a semicolon, it's the same thing with SCSS and SAS.
[3256.42 --> 3259.94]  And that's probably where Wynn and I probably, Wynn writes CoffeeScript, though, and I don't.
[3260.10 --> 3266.84]  But, you know, it's kind of where I can meet with you on there and say that I agree that writing code that doesn't actually do something sucks.
[3267.48 --> 3267.74]  Yeah.
[3268.22 --> 3269.18]  I feel the same way.
[3269.18 --> 3273.06]  I love the terseness, and don't get me wrong, it's one of my favorite features.
[3273.24 --> 3275.24]  But, I mean, CoffeeScript adds a lot to JavaScript.
[3276.12 --> 3277.26]  It's not hard stuff.
[3277.32 --> 3278.62]  It just removes a lot of tedium.
[3278.74 --> 3281.92]  And one of those things is the existential operator, right?
[3282.16 --> 3296.90]  Being able to put a chain of dot notation method calls or property calls with a question mark in front of the dot and know that in a safe way you're going to go down five levels deep is just awesome.
[3296.90 --> 3301.94]  The existential operator is beautiful, and it's definitely one of those things that I wish I had in Ruby.
[3303.30 --> 3307.00]  Still trying to figure out why I love white space so much, and I still don't sling Python.
[3308.32 --> 3319.02]  You know, the thing that bothers me about Python is that it has seemingly arbitrary restrictions on what you can do independent of white space.
[3319.20 --> 3326.22]  So, like, you can't have more than one expression inside a closure, I believe.
[3326.90 --> 3330.26]  That may not be accurate anymore, but I know at one time that was the case.
[3331.10 --> 3333.88]  And CoffeeScript has no such restrictions.
[3334.98 --> 3343.66]  So, you can break out of the white space model if you need to using semicolons.
[3343.66 --> 3355.44]  There's also something really handy called the then keyword, which lets you join two white space-sensitive lines on a single line.
[3356.30 --> 3360.88]  It basically is the exact – it parses the same way as a new line plus an indent.
[3360.88 --> 3366.24]  So, anytime you write a new line plus an indent, you can also just write then.
[3368.48 --> 3371.88]  So, it's really that flexibility, I think, that's powerful about CoffeeScript.
[3371.88 --> 3380.28]  Yeah, I was asking you earlier about JavaScript and CoffeeScript, but is there anywhere that somebody can learn JavaScript and CoffeeScript kind of in parallel?
[3382.40 --> 3385.00]  Is there any good recipe for learning those two in parallel?
[3385.28 --> 3397.80]  Just kind of being sure of what JavaScript does obviously is a good thing as a programmer, but at the same time, you don't want to just learn JavaScript blindly and not know where it maps to CoffeeScript or vice versa.
[3397.80 --> 3400.40]  That's hard for me to answer.
[3402.76 --> 3403.44]  I don't know.
[3403.54 --> 3407.28]  Trevor Burnham's CoffeeScript book from the Pragmatic Programmers is excellent.
[3408.58 --> 3419.18]  It's not really – it assumes you know JavaScript, but it also takes you through using the language on the server side and in the browser.
[3419.40 --> 3421.90]  So, I think it gives you a good overview of everything you can do with it.
[3422.48 --> 3423.10]  It's a great read.
[3423.16 --> 3424.16]  I highly recommend that book.
[3424.16 --> 3438.18]  So, as a company, obviously, I think everyone would be safe to say that 37Signals wasn't exactly founded on open source, but it's certainly a big piece of the company and the culture.
[3439.44 --> 3447.78]  Why do you think beyond, I guess, the obvious answer, which is what Rails has done for the company, why do you think open source is so important to the company?
[3448.80 --> 3450.30]  I think that's exactly it.
[3450.30 --> 3464.54]  We can put out code that is useful to us that raises the bar and get people using it, and we get our bug fixes for free and our R&D.
[3467.12 --> 3469.24]  It's just a powerful thing to do.
[3469.24 --> 3477.04]  So, I think that should be the primary motivator for anyone who wants to get into open source, too.
[3478.20 --> 3486.62]  Well, this is the part of the show that we normally ask a couple of closing questions, and since you admit that you haven't caught an episode, we'll catch you blind here.
[3486.62 --> 3497.54]  So, what is on your open source radar if you have a Saturday afternoon and you're just hacking for the pure joy of it, although it sounds like you do a lot of that at your day job?
[3498.38 --> 3500.66]  What's got you excited that you just can't wait to play with?
[3502.50 --> 3503.10]  Oh, man.
[3503.22 --> 3509.32]  I'm going to sound like an idiot if I answer this honestly because I've pretty much just been focused on my own stuff.
[3509.32 --> 3512.84]  And that's perfectly fine.
[3512.96 --> 3514.00]  A lot of folks have said that.
[3514.04 --> 3514.24]  Yeah.
[3519.50 --> 3523.42]  Which of your projects are you looking to show the most love?
[3523.42 --> 3541.96]  I definitely want to get Sprockets out, the 2-0 final release, and then I would like to give Pal a little bit of love and then hopefully start on Cinco.
[3543.64 --> 3546.50]  If you had to, I guess, look back at your...
[3546.50 --> 3547.38]  How old are you, by the way?
[3547.70 --> 3548.26]  Just curious.
[3549.02 --> 3549.88]  I'm 27.
[3550.08 --> 3550.44]  27.
[3550.44 --> 3552.06]  Okay, so you're almost winning as age.
[3552.06 --> 3554.62]  I'm 32 when you're, what, 41?
[3554.90 --> 3555.50]  I'm 35.
[3558.64 --> 3565.54]  If you had to look back on your history of being a programmer or working at 37 Signals, who do you look to as a hero in your world?
[3565.60 --> 3566.26]  Who do you look up to?
[3566.34 --> 3568.74]  Who do you aspire to be more like?
[3568.80 --> 3570.62]  Or who would you even like to pair a program with?
[3570.62 --> 3585.06]  So David Heinemeyer Hansen was extremely influential in getting me interested in actually contributing to open source projects.
[3585.06 --> 3591.08]  So I have him to thank for that in the early days of Rails.
[3594.92 --> 3605.48]  I've done a lot of work with Josh Peek, who is an amazing programmer, and I feel like we think the same way about a lot of problems.
[3605.48 --> 3609.86]  He's been very fun to work with.
[3609.86 --> 3620.44]  And Jeremy Ashkenaz is who I consider to be the model open source programmer.
[3620.44 --> 3628.14]  He's been very influential for me lately.
[3629.42 --> 3642.42]  If you follow any of his projects and you read the bug tracker, you can see how clearly and concisely and definitively he makes decisions.
[3642.42 --> 3648.80]  And it's something you don't always see in the open source world, but it's very refreshing.
[3649.30 --> 3654.52]  And I hope to one day manage my projects as well as he does.
[3656.66 --> 3658.50]  So DHH, who was the second one?
[3659.38 --> 3659.92]  Josh Peek.
[3660.12 --> 3660.78]  Josh Peek.
[3661.04 --> 3663.56]  So the two of your heroes are fellow co-workers.
[3664.58 --> 3665.08]  That's correct.
[3665.20 --> 3668.84]  I don't work with Josh anymore, but we worked together for a time.
[3668.84 --> 3670.98]  That's got to be kind of fun.
[3671.14 --> 3676.36]  I mean, it's not the dream, though, to work with whom or have worked with whom you look up to.
[3677.16 --> 3680.30]  And I mean, that's the whole point anyways, is success breeds success.
[3680.96 --> 3681.32]  Absolutely.
[3683.08 --> 3684.30]  You mentioned Jeremy.
[3684.44 --> 3685.80]  I'm convinced that he's a Cylon.
[3687.76 --> 3696.46]  He's always around in the IRC channels, day or night, answering questions and turning out more code than the rest of us.
[3696.46 --> 3708.02]  And, you know, you would just assume, pardon me, you just assume that he's going to be holed up in a cave somewhere to turn out this much software, much less, you know, open source software.
[3708.24 --> 3709.76]  But, you know, he's very approachable.
[3709.88 --> 3712.24]  And you ask him a question in the IRC, and he's instantaneous.
[3713.00 --> 3715.38]  I feel like he may be operating at a higher plane of existence.
[3716.48 --> 3717.06]  That's true.
[3717.06 --> 3719.88]  Well, thanks, Sam, so much.
[3720.30 --> 3721.70]  Little technical hiccups.
[3721.80 --> 3723.06]  Hopefully they'll come through editing okay.
[3723.94 --> 3730.90]  But so glad you joined us to talk about POW and Prototype and Sprockets and Rails 3.1 and the whole lineup.
[3731.16 --> 3732.56]  Well, thank you guys so much for having me.
[3732.56 --> 3740.80]  You're welcome.
[3740.80 --> 3744.76]  Listen to the podcast.
[3746.44 --> 3749.62]  One of the podcasts.
[3752.46 --> 3753.98]  One of the numerals.
[3756.22 --> 3756.76]  You're welcome.
