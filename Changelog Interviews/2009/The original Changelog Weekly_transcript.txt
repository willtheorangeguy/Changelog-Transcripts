[0.00 --> 19.60]  Welcome to The Change Log, episode 0.0.2.
[19.80 --> 21.88]  Today is November 25th, 2009.
[22.38 --> 23.82]  I am Adam Stachowiak.
[24.22 --> 25.10]  And I'm Wyn Netherland.
[25.10 --> 29.44]  So what is at thechangelog.com right now, Wyn?
[29.44 --> 31.32]  About five stories right now.
[31.80 --> 33.92]  But no, we've got a nice little Tumblog set up on Tumblr.
[34.36 --> 47.54]  We thought, hey, in the interest of iterating on this deal and starting small and letting it organically grow or organically die, whatever the case may be, to kind of leverage some of the free tools out there.
[47.54 --> 52.20]  And we've got a Tumblog set up that has some nifty GitHub integration.
[52.20 --> 64.54]  So when you post a link to a GitHub repo and tag it as GitHub, I can automatically pull in the watchers and fork statistics for that repo.
[65.02 --> 70.20]  Now, that's pretty cool because I see underscore.js listed there and jam it.
[70.24 --> 72.38]  And they both have the watchers.
[72.46 --> 73.32]  And that's real time, right?
[73.32 --> 74.46]  It is real time.
[74.56 --> 76.38]  And it's about four or five lines of jQuery.
[76.98 --> 82.62]  And got the idea from GitHub's new version 2 of their API at develop.github.com.
[83.74 --> 90.54]  And they've got some advanced features that require authentication, API keys, all that good stuff.
[90.70 --> 98.86]  But this was pretty straightforward, the public information that you can get with just an unauthenticated call via a jQuery callback.
[99.40 --> 100.00]  Very simple.
[100.46 --> 101.12]  Very cool, though.
[101.12 --> 103.98]  How long did it take you?
[104.90 --> 107.12]  That feature, probably an hour.
[107.42 --> 112.16]  And that's probably most of them was fighting spelling issues.
[112.74 --> 113.20]  Oh, boy.
[113.34 --> 114.14]  So you're a bad speller?
[114.58 --> 124.92]  Those are always fun when you're depending on a CSS class and either CSS for markup or in jQuery for your selectors to act on a particular element.
[125.22 --> 127.82]  And you're wondering why in the heck it's not coming back.
[127.92 --> 129.92]  And you figure out you've got a misspelling in your selector.
[129.92 --> 131.02]  That's the thing about jQuery.
[131.12 --> 139.98]  If you've done any JavaScript development, and I'm sure you've run into this down, if you misspell that selector, it doesn't throw any sort of error or anything.
[140.16 --> 141.12]  It just nothing happens.
[141.72 --> 142.86]  Well, it doesn't know what's the target.
[143.24 --> 143.66]  I know.
[143.78 --> 146.04]  But, I mean, it's gracefully just eating the error.
[146.46 --> 149.34]  So you're left to pull your hair out.
[149.34 --> 155.90]  In this whole changelog, the changelog, changelog show setup, I've probably misspelled change.
[156.40 --> 159.94]  I've actually dropped the E off the end of change about a dozen times so far.
[159.94 --> 160.94]  So don't feel bad.
[161.44 --> 162.00]  That's okay.
[162.18 --> 163.74]  You're still learning how to spell squirrel.
[164.16 --> 169.86]  Tune in to Adam's latest episode of the Web 2.0 show for a more in-depth look at how to spell font squirrel.
[170.80 --> 171.04]  Yeah.
[171.60 --> 173.50]  It's actually not the latest because I'm quick like that.
[173.50 --> 176.20]  It's actually the episode previous to the latest.
[176.48 --> 176.78]  Uh-oh.
[176.84 --> 177.38]  I'm behind.
[177.64 --> 178.12]  You are.
[178.54 --> 179.70]  I'm kind of like I'm behind on your blog.
[179.78 --> 180.72]  I can't keep up with your blog.
[183.02 --> 186.54]  Endless stream of information from Wynn's mind into the blog.
[187.90 --> 188.30]  Jeez.
[188.30 --> 191.04]  So anyways, what's our lineup?
[192.08 --> 193.12]  The lineup this week.
[193.16 --> 196.26]  Let's start with a couple of projects from Document Cloud.
[196.72 --> 200.22]  They kind of burst on the scene a couple of weeks ago with underscore.js.
[200.74 --> 201.40]  Have you seen this?
[201.60 --> 201.80]  Yeah.
[202.02 --> 202.16]  Yeah.
[202.66 --> 208.52]  Pretty cool little JavaScript framework that are billing themselves as the tie to jQuery's tux.
[209.64 --> 211.08]  I think that's a good way of putting it.
[211.34 --> 211.88]  Yeah, I like that.
[212.24 --> 213.18]  You know, I'm a Rubyist.
[213.40 --> 214.20]  I know you are too.
[214.90 --> 215.72]  Oh, somewhat.
[216.42 --> 217.58]  I work in the Ruby land.
[217.58 --> 219.06]  I play one on radio.
[219.70 --> 219.86]  Right.
[221.18 --> 227.38]  So, you know, if you come from Ruby and you dive back into the client side JavaScript,
[227.94 --> 232.28]  you miss a lot of those convenience functions for arrays and collections and things that you get from Ruby.
[232.56 --> 238.94]  Like, you know, first and last and unique and flatten.
[239.38 --> 244.14]  Those just things we take for granted that make arrays in Ruby so sweet.
[244.48 --> 246.50]  This project aims to add those back.
[246.50 --> 248.58]  You know, really kind of fills a gap.
[249.16 --> 253.98]  If you ever worked with Prototype.js, they have a lot of those features built into that JavaScript framework.
[254.12 --> 260.66]  And that was one of the things that I noticed coming to jQuery from Prototype was just kind of the lack of array support.
[260.78 --> 266.44]  There's some rudimentary array support in there around their wrap set for DOM elements and things.
[266.44 --> 268.82]  But on the array side, it's kind of lacking.
[269.82 --> 274.86]  And underscore does a good job of grafting on some of those methods.
[275.68 --> 279.14]  You can check it out at documentcloud.github.com slash underscore.
[280.50 --> 281.44]  Very nice.
[282.10 --> 283.42]  Nicely styled document.
[284.68 --> 285.62]  Documentation as well.
[286.02 --> 286.24]  Yeah.
[286.60 --> 289.34]  Comment on that when we first found this project.
[289.34 --> 292.34]  That's the simplicity of that document.
[292.68 --> 294.38]  That design for that page.
[295.12 --> 298.88]  I'm noticing something, too, on their readme at the GitHub repo.
[300.26 --> 303.72]  They either stole it directly from Handcrafted or they're just that cool.
[303.82 --> 304.48]  I don't know which.
[304.90 --> 305.98]  But if you're looking at the readme.
[306.28 --> 307.70]  The same ASCII art for the logo?
[308.00 --> 308.30]  Yeah.
[308.54 --> 310.00]  I think it's the same exact font.
[310.00 --> 314.28]  I think they just had to copy.
[314.80 --> 317.94]  Maybe they're just, yeah, I guess when you're that good, copy it, right?
[320.76 --> 321.24]  Yeah.
[321.28 --> 325.74]  One other cool feature that underscore has is templating.
[326.52 --> 326.96]  Oh?
[327.36 --> 329.36]  I've seen this in a couple other frameworks.
[329.82 --> 331.30]  Never had a real use for it.
[331.40 --> 339.54]  I guess I've always been, my pattern has always been to create markup on the server and then send that down to the client where I can.
[339.54 --> 349.74]  But, you know, there's instances when you build a lot of elements on the fly on the client that you would just like to specify a template and have JavaScript do the heavy lifting for you.
[349.80 --> 352.14]  And this allows the ability to do that.
[352.48 --> 363.94]  And the syntax for binding variables within those templates is very familiar if you know ASP or Ruby, the ERB syntax with the less than percent equal syntax.
[364.14 --> 364.46]  Right.
[364.72 --> 366.50]  I know you're such a big ERB fan.
[366.74 --> 367.06]  Oh, yeah.
[367.06 --> 370.16]  You saw my tweets today, right?
[370.44 --> 371.24]  I did about Hamill.
[371.64 --> 371.98]  Yeah.
[373.18 --> 374.76]  It's like going back in time.
[375.74 --> 376.32]  I did.
[376.42 --> 388.38]  I really hated it because as I take a big squig of my coffee at 9 o'clock, 930 at night, I was really PO'd that I had to take this beautiful Hamill view.
[388.38 --> 392.96]  And if you don't know what Hamill is, tune into the previous episodes of this.
[393.10 --> 396.92]  But, you know, I hated it.
[396.98 --> 398.08]  It was a beautiful Hamill view.
[398.14 --> 400.50]  I had to go and put an ERB.
[400.60 --> 402.80]  And I felt like it was like it was really, really painful.
[404.14 --> 404.98]  I was upset.
[404.98 --> 406.38]  I feel your pain.
[406.68 --> 407.40]  I feel your pain.
[407.84 --> 408.48]  So, templating.
[409.76 --> 413.04]  Templating is a nice way to just specify a template.
[413.04 --> 424.84]  So, I guess the use case would be, let's say you had a list of elements and you needed to bind an unordered list, a set of LI elements for each item in an array.
[424.84 --> 432.12]  Then you could just specify a template that had placeholders in there for the variables coming from your JavaScript object.
[432.82 --> 438.90]  And you would just call underscore dot template, pass in your data, and pass in your template.
[439.50 --> 448.40]  And you get a nice HTML fragment for your LI elements to put in the list.
[448.50 --> 448.84]  Pretty cool.
[449.36 --> 450.28]  Well, that's not really that bad.
[450.36 --> 454.34]  If you're following a certain convention, you're not really like creating content.
[454.34 --> 457.46]  You're just frameworking your HTML markup.
[457.86 --> 458.22]  That's right.
[458.68 --> 459.20]  That's right.
[459.50 --> 460.36]  Which isn't a bad thing.
[460.48 --> 461.16]  Saving time.
[461.86 --> 463.30]  Another cool feature is chaining.
[463.82 --> 465.80]  So, do a lot of jQuery, Adam?
[466.50 --> 466.90]  Yeah.
[467.04 --> 467.22]  Yeah.
[467.30 --> 467.66]  Fair bit.
[468.32 --> 484.20]  So, one of the coolest things that most people like when they come to jQuery is the chaining where you can, you know, the wrap set is returned at the end of every method call so that you can just keep chaining methods together like add class, append, remove, things like that.
[484.20 --> 484.38]  Right?
[484.38 --> 484.50]  Right.
[484.50 --> 484.90]  Right.
[485.66 --> 487.24]  Underscore supports that as well.
[487.42 --> 495.76]  So, you can call underscore, pass in your object call dot chain, and then you can call sort map first value.
[496.72 --> 509.58]  And essentially, you queue up these method calls, and then when you call dot value at the end, it executes it and passes you back a value so you can chain up multiple method calls in a row.
[509.66 --> 510.50]  It's really, really neat.
[511.18 --> 511.48]  Hmm.
[511.48 --> 522.92]  You know, when we discovered our second project, Jamit, I remember this past week clicking on the link, and my first was kind of taken aback.
[523.08 --> 526.50]  I was like, somebody ripped off Document Cloud's excellent documentation site.
[526.80 --> 527.76]  I just changed it to blue.
[527.76 --> 533.34]  Then I got to looking a little closer and found out this is another project from Document Cloud.
[534.20 --> 534.80]  We're excited.
[534.88 --> 537.80]  We're going to talk to these guys, I believe, next week.
[538.20 --> 538.44]  Yeah.
[539.16 --> 541.54]  Upcoming show, so be sure and tune in for that.
[541.54 --> 550.56]  But Jamit is, as they call it, an industrial strength asset packaging plug-in for Rails.
[550.56 --> 567.24]  And so essentially what this is, if you've used asset packager or other plug-ins in the Rails space, it's a way to tidy up and compress and concatenate those JavaScript plug-ins, you know, all those jQuery plug-ins that you use.
[567.46 --> 568.58]  Yeah, I've used it, yeah.
[569.16 --> 575.08]  And it gives you one, you know, or a couple of files to download, one JavaScript file, one CSS file.
[575.08 --> 589.88]  This aims to do the same thing there, but also build in a couple of new features, like gzipping, which is zipping up those assets and serving them compressed over the wire.
[589.98 --> 592.06]  So you're actually sending less bytes over the wire.
[593.00 --> 597.26]  Most modern browsers support unzipping those on the fly, so it really cuts down on bandwidth.
[597.26 --> 606.30]  All right, so you're probably making the Yahoo YSlow people that really cling to those rule sets that Yahoo put out there really, really happy.
[606.50 --> 609.82]  I'm hopeful I can score an A on my website with that YSlow score now.
[610.10 --> 611.28]  That's hard.
[611.82 --> 612.36]  I know.
[612.48 --> 614.04]  It's like, hey, I'm a C+.
[614.04 --> 614.42]  Sweet.
[614.42 --> 614.46]  Sweet.
[615.66 --> 630.74]  So the other big feature is something that was new to me, and that's embedding your image assets within your style sheet using either the data URI method or the MHTML image embedding method.
[631.10 --> 631.52]  Oh, wow.
[632.10 --> 634.86]  This is really space-age material right here.
[635.26 --> 643.24]  This allows you to take all those binary assets and essentially embed them in your style sheet, which I have mixed feelings about.
[643.24 --> 651.34]  I guess the proof's in the pudding, but I want to play with this particular plug-in and see if there's any gotchas.
[651.56 --> 655.18]  It's just my gut feel tells me that's a little too cool for school.
[655.30 --> 655.70]  How about you?
[655.92 --> 658.70]  Well, when we talk to them, I'm sure that they'll give us a good reason why.
[658.92 --> 662.08]  Every time you do something like this, you're always solving some sort of problem.
[662.30 --> 669.36]  So I can only imagine they would take the time to do it either because it's just that cool to do for one or they really needed it.
[669.36 --> 673.70]  So I'm really curious to see what kind of solution, what they were trying to solve by doing that.
[675.00 --> 676.98]  I look forward to speaking with those guys.
[677.38 --> 679.82]  In terms of mixed feelings, whatever works.
[680.32 --> 683.10]  I think in today's web, we've got so stuck.
[683.20 --> 684.22]  It's good to have conventions.
[684.44 --> 686.48]  It's good to have web standards.
[686.82 --> 688.02]  It's good to have these things.
[688.14 --> 691.92]  But at the same time, they do put you in a box, and sometimes it's nice to break out.
[692.88 --> 693.32]  That's true.
[693.72 --> 694.20]  That's true.
[694.20 --> 696.08]  All righty.
[697.16 --> 698.74]  Next up, Google Go.
[699.76 --> 701.90]  So you've got some exciting news about this particular one.
[702.26 --> 702.44]  Yeah.
[702.70 --> 703.62]  Scored an interview with them.
[704.70 --> 708.34]  I'm looking forward to it because I want to understand exactly what this thing is.
[708.46 --> 708.74]  Yeah.
[708.90 --> 709.86]  Everybody's talking about it.
[710.16 --> 710.34]  Yeah.
[710.40 --> 711.04]  A lot of people are.
[711.16 --> 712.66]  It came out, what, a week and a half ago?
[713.04 --> 713.72]  Yeah, it did.
[713.92 --> 721.04]  And it's supposed to be kind of a cross between a dynamic programming language and a statically tight programming language.
[721.82 --> 723.48]  I hear they have a bias against Windows.
[723.48 --> 724.28]  They do.
[724.60 --> 725.00]  They do.
[726.28 --> 727.26]  From the FAQ.
[727.34 --> 729.76]  Let me pull that up and give that a go.
[731.00 --> 734.14]  We understand that a significant fraction of computers in the world run Windows.
[734.34 --> 736.54]  It would be great if those computers could run Go programs.
[736.70 --> 740.26]  However, the Go team is small, and we don't have the resources to do a Windows port at the moment.
[741.24 --> 741.70]  So, wow.
[741.86 --> 743.88]  Significant fraction of computers in the world run Windows.
[743.96 --> 744.80]  Did you know about this, Adam?
[745.32 --> 746.38]  Yeah, I didn't.
[746.44 --> 748.56]  I thought it was a fairly large fraction.
[749.98 --> 752.50]  I need to know how significant it is.
[752.50 --> 754.28]  I need to start doing some testing in IE.
[754.66 --> 754.98]  Yeah.
[755.64 --> 762.46]  Well, you know, maybe it also ties into the fact that, you know, Chrome OS is coming out, and it's really hitting hard with the netbooks.
[762.46 --> 775.20]  And it's, you know, I watched, this is going to go off topic for just a second, but I watched the video on Chrome OS today, and I was like, why would I want to use this, and what's so cool about it?
[775.20 --> 784.40]  And really, it takes everything away about the operating system that is the operating system and just trims it down to the browser and getting it on the internet, which is what you most want to do.
[784.76 --> 789.18]  Well, I watched this video, and then I installed some software, and I had to restart.
[789.18 --> 798.28]  And I was really, really excited to get back to work because, you know, I was just so desperate to take that Hamill and put it and take it and turn it into ERB.
[798.80 --> 798.94]  Sure.
[799.10 --> 803.56]  I was really racing fast to restart this computer and get back into my dev mode.
[803.56 --> 805.70]  And I swear, it took me forever.
[806.86 --> 807.64]  Ten minutes?
[808.62 --> 812.26]  Either it's my MacBook or something, I don't know.
[812.50 --> 814.06]  But I felt the pain.
[814.30 --> 819.46]  So maybe it's something to do with the Chrome OS coming out and all that.
[819.96 --> 821.92]  Chrome OS does look promising as well.
[822.28 --> 823.68]  It's one to keep on the radar.
[824.06 --> 825.98]  Gruber had, did you ever read Daring Fireball?
[826.38 --> 826.92]  A little bit, yeah.
[826.92 --> 835.90]  Yeah, he had an interesting comment this past week saying that it probably is a better fit for a second machine, which I totally can see that.
[836.48 --> 838.66]  And I think that is the use case for a lot of these netbooks.
[838.88 --> 840.46]  You know, it's your travel machine.
[840.58 --> 844.00]  It's not necessarily your main productivity unit.
[844.48 --> 844.72]  Right.
[844.86 --> 848.36]  I like to just have the opportunity to go get a netbook.
[848.46 --> 849.80]  I haven't really had a need for one.
[849.84 --> 853.80]  I guess if I'm traveling, a netbook would be nice.
[853.80 --> 859.48]  You know, I don't know that I could get used to the small screen.
[859.58 --> 861.18]  Everybody talks about the small form factor.
[861.86 --> 867.08]  And this, as I'm playing with my iPhone in my other hand, which has an extremely small screen.
[867.84 --> 880.14]  But as far as a netbook, you know, I just, there's sometimes even when 1,400 pixels isn't wide enough for me and having something significantly less than that, I'm not sure how productive I could be with it.
[881.30 --> 881.66]  Yeah.
[881.66 --> 887.60]  I wasn't really a big fan of, that's why I never really buckled down and bought a regular old MacBook.
[888.34 --> 895.60]  Because I always thought if I'm going to spend the money on a computer, I'm going to spend the money on something with at least, you know, at least a 15-inch screen.
[896.08 --> 898.06]  You know why I did the original MacBook?
[899.18 --> 900.00]  The keyboard.
[901.58 --> 905.26]  I love the flat keys on the original MacBook.
[905.26 --> 910.14]  For some reason, I just, you know, it felt more comfortable to me when I'm typing.
[910.94 --> 916.18]  And I was so tickled when the new MacBook line, MacBook Pro line came out with the same flat keys.
[917.62 --> 919.86]  So I went and bought me one of those bad boys.
[922.34 --> 922.74]  Cool.
[923.20 --> 924.26]  What's, uh, what's...
[924.26 --> 929.46]  Right.
[930.42 --> 931.72]  What's going on with browsers?
[931.90 --> 934.32]  I mean, we're on the, on the talk of Chrome OS.
[934.44 --> 935.14]  What about Firefox?
[936.54 --> 940.38]  Firefox dropped beta 2 of 3.6.
[941.04 --> 941.74]  Why should we care?
[943.20 --> 946.54]  Because as web developers, it's got some cool new features.
[946.92 --> 947.12]  Oh?
[947.82 --> 949.38]  You know you love new CSS features.
[949.68 --> 950.02]  Yeah.
[950.18 --> 950.78]  Why not?
[951.92 --> 953.28]  Just give me more to do.
[953.64 --> 956.18]  More things to plug in there that don't work in IE.
[956.56 --> 956.96]  Right.
[957.28 --> 962.44]  This is your chance to thumb IE in the eye and say, take that, Mr. IE user.
[963.22 --> 965.52]  You can't do background sizes.
[965.52 --> 969.20]  And you can't do linear gradients and radial gradients.
[969.86 --> 971.50]  You can't do multiple background images.
[972.42 --> 973.16]  Things of that sort.
[973.16 --> 978.62]  There's also new font face support for the W-O-F-F format.
[978.92 --> 979.38]  Heard of this one?
[979.76 --> 980.88]  Also known as WAF.
[981.48 --> 982.04]  WAF.
[983.14 --> 989.80]  Yeah, that same podcast you referenced earlier with Font Scroll, me and Ethan Dunn, we talked about that stuff.
[990.06 --> 992.12]  Is there an L-E-T-L-D?
[993.02 --> 993.78]  Top level domain?
[994.68 --> 997.38]  I'm waiting for somebody to register waffle.com.
[997.54 --> 998.32]  Oh, yeah.
[998.32 --> 999.32]  And rival Font Squirrel.
[999.32 --> 1003.88]  There's nothing but WAF format fonts.
[1005.10 --> 1005.96]  We'll see.
[1006.18 --> 1007.00]  Only time we tell.
[1009.16 --> 1010.88]  Somebody's on Domainer as we speak.
[1012.54 --> 1015.18]  HTML5 video now supports poster frames in Firefox.
[1015.84 --> 1023.50]  So that's pretty cool that you can specify what image will be the poster frame, which is that little thumbnail that you see when the video is about to start.
[1023.50 --> 1029.36]  You can also do multiple file uploads with the HTML input element.
[1030.20 --> 1031.66]  So I'm not sure how they're swinging that.
[1031.74 --> 1034.54]  Normally that's something you've got to resort to Flash to do.
[1034.96 --> 1036.92]  You ever cut up one of those?
[1039.30 --> 1039.70]  No.
[1039.90 --> 1040.66]  No, not too often.
[1040.80 --> 1042.42]  I was never much of a Flash guy.
[1042.42 --> 1063.26]  Yeah, it's usually – I'm not either, but it's usually the best way to handle that because I know you're a user experience guy, and it's always a pain to let a user upload their three files just to tell them, hey, after you sat there and watched this thing for 30 minutes that they're not the right format.
[1063.26 --> 1064.52]  I do like that.
[1064.84 --> 1068.92]  If you're talking about the Flash, you're talking about the upload progress Flash stuff?
[1068.92 --> 1069.66]  Exactly, yeah.
[1069.66 --> 1070.48]  Yeah, yeah, I like that.
[1070.70 --> 1072.62]  I've never implemented one of those, but those are very cool.
[1073.04 --> 1078.02]  It looks like this is now baked into the browser, that type of functionality, which hopefully that'll be another thing.
[1078.40 --> 1087.20]  That's the sort of thing that you would expect should be part of the browser and not have to rely on third-party plug-ins to something so basic.
[1088.00 --> 1089.08]  Yeah, that's silly.
[1089.08 --> 1092.48]  I would have just imagined that it should be part of the browser, but it's not.
[1092.48 --> 1092.50]  Yeah.
[1093.14 --> 1095.16]  Well, that is it for the changelog this week.
[1097.42 --> 1101.22]  No, actually, we should pop one more in there, shouldn't we?
[1101.34 --> 1108.52]  When we were talking about that CSS stuff, we were going to talk about something very, very cool that got lots and lots of press this past couple days.
[1108.72 --> 1111.26]  Oh, Brandon Mathis' fancy buttons.
[1111.70 --> 1111.86]  Yeah, yeah.
[1112.46 --> 1113.10]  That is cool.
[1113.18 --> 1113.74]  Have you used it?
[1114.34 --> 1122.04]  No, I haven't made any use of it, but I've seen a demonstration of it firsthand, and I think, you know,
[1122.04 --> 1128.38]  Brandon is a very smart guy when it comes to using Sass and using Compass in the right ways.
[1129.36 --> 1132.76]  And I think it's really cool because it changes the luminosity.
[1132.76 --> 1144.80]  It has failover or, like, fallback support for that same blog post you referenced with Squeegee using a PNG with luminosity and whatnot.
[1147.12 --> 1148.48]  It's really a cool thing.
[1148.60 --> 1153.74]  Like, you just pop in one color, and it sets the border color, the hover color, the active state color of the button.
[1153.74 --> 1158.92]  And it's really, really got a lot of nice features, so I can see why he's got a lot of traffic about it.
[1159.12 --> 1167.06]  I was checking out another one of Brandon's Sass plugins that you had pointed me to this weekend about using CSS sprites.
[1167.62 --> 1167.86]  Oh, yeah.
[1168.34 --> 1171.24]  Implemented a CSS sprite on the changelog icons.
[1171.36 --> 1175.74]  If you go out to the changelog.com and you'll see the icons that we have for each post,
[1175.74 --> 1180.76]  that's a CSS sprite, which is essentially, you know, one big image for all of your icons.
[1180.88 --> 1186.74]  And then you specify which icon you want to load based on background position,
[1187.50 --> 1189.62]  and that cuts down on network transfers.
[1190.08 --> 1195.68]  And Brandon had a cool plugin to do this with Compass that I'm anxious to use in my next Compass project.
[1196.56 --> 1198.74]  Too bad we didn't get a chance to use it on the changelog,
[1198.74 --> 1206.18]  but it is another promising Compass plugin from Mr. Mathis.
[1207.34 --> 1208.16]  Mr. Mathis.
[1208.18 --> 1209.96]  He's got lots of stuff going into Compass Core.
[1211.24 --> 1215.94]  Between that, some of his work with colors, the Compass Colors extension,
[1217.92 --> 1219.24]  he's doing pretty well.
[1219.56 --> 1220.18]  Busy man.
[1220.64 --> 1221.56]  Busy, busy, busy.
[1222.28 --> 1223.08]  All right, what else we got?
[1223.18 --> 1223.60]  Is that it?
[1223.70 --> 1224.24]  Is that the show?
[1224.48 --> 1225.20]  I think that's it.
[1225.24 --> 1226.36]  A short Thanksgiving week.
[1226.74 --> 1227.54]  Well, there you go.
[1227.54 --> 1231.94]  Well, in a few days we'll be talking to Google and talking to Rob about Go.
[1232.14 --> 1233.28]  That should be an awesome conversation.
[1233.40 --> 1236.06]  We'll definitely come back and spread some good love in there.
[1236.32 --> 1237.62]  Enjoy that show.
[1238.26 --> 1241.82]  And we'll have the week after that talking to Doc McCloud,
[1241.94 --> 1244.06]  and we'll get some of those questions we brought up earlier answered.
[1245.06 --> 1245.44]  Absolutely.
[1245.96 --> 1246.32]  Absolutely.
[1247.52 --> 1248.08]  All righty.
[1249.00 --> 1250.18]  Happy Thanksgiving, everyone.
[1250.50 --> 1251.18]  Take care.
[1251.18 --> 1251.22]  Take care.
[1251.22 --> 1259.58]  Thank you for listening to this edition of The Changelog.
[1260.38 --> 1264.30]  Be sure to tune in weekly for what's fresh and new in open source.
[1265.52 --> 1270.36]  Also, visit thechangelog.com to follow along, subscribe to the feed, and more.
[1270.54 --> 1271.60]  Thank you for listening.
[1271.60 --> 1272.74]  We'll see you.
[1293.22 --> 1295.22]  Bye.
[1295.34 --> 1297.14]  Bye.
[1297.30 --> 1301.42]  Bye.
