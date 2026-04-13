[0.00 --> 18.20]  Welcome to the ChangeLog episode 0.2.3.
[18.46 --> 19.54]  I'm Adam Stachowiak.
[19.72 --> 20.58]  And I'm Wynne Nevely.
[20.76 --> 21.70]  This is the ChangeLog.
[21.76 --> 23.72]  We cover what's fresh and new in the world of open source.
[24.10 --> 27.08]  If you found us on iTunes, we're also on the web at thechangelog.com.
[27.30 --> 28.28]  We're also up on GitHub.
[28.28 --> 32.50]  If you go there, you'll see some trending repos, some feature repos from the blog,
[32.58 --> 33.76]  as well as the audio podcast.
[34.26 --> 38.46]  We're also on Twitter, so follow us with changelogshow, not the changelog.
[38.58 --> 40.08]  And I am Adam Stach.
[40.32 --> 42.64]  And I am Penguin, P-E-N-G-W-Y-N-N.
[43.22 --> 46.68]  I'm fresh back from Oklahoma City, Red Dirt RubyConf.
[47.10 --> 48.36]  Yeah, it's a lot of fun up there, I bet, huh?
[48.74 --> 49.28]  Yeah, it was.
[49.32 --> 50.24]  A lot of smart folks.
[50.34 --> 53.58]  Got to see a keynote from Jim Wyrick and Dave Thomas.
[53.80 --> 54.16]  Oh, yeah.
[54.16 --> 58.32]  A couple of guys that have forgotten more Ruby than I'll ever learn.
[59.22 --> 60.72]  A lot of JavaScript going on, too.
[60.78 --> 65.56]  Interviewed Charles Lowell, a.k.a. Cowboy D on Twitter and GitHub, about Ruby Racer.
[65.98 --> 67.24]  He's got some exciting projects here.
[67.84 --> 70.48]  Yeah, some embedded JavaScript within Ruby.
[71.14 --> 74.68]  One embeds the, I guess Ruby Racer embeds the Google V8 engine,
[74.68 --> 78.44]  and Ruby Racer embeds Mozilla's Racer.
[78.44 --> 79.60]  I know JavaScript engine.
[80.82 --> 84.42]  I have to apologize up front for the audio of this interview.
[84.86 --> 85.86]  We did it live.
[85.96 --> 86.88]  We'll do it live!
[87.14 --> 88.60]  Okay, go, Riley.
[88.98 --> 89.20]  Yeah.
[89.28 --> 90.92]  We did it live there at the conference.
[91.46 --> 93.44]  And, you know, live events are always fun.
[94.48 --> 96.56]  Yeah, there's always some sort of glitch you've got to deal with,
[96.66 --> 99.70]  and quality of the audio is always one that goes first.
[99.70 --> 104.94]  So please excuse that, but otherwise it's a fun episode, commute-friendly format this week.
[105.50 --> 106.52]  A couple of programming notes.
[106.60 --> 111.02]  We'll be at Texas JavaScript on the 5th of next month, 5th of June, in Austin, Texas.
[111.22 --> 112.04]  Great lineup there.
[112.48 --> 112.64]  Yeah.
[112.84 --> 114.68]  Also be at Less Conflict on this month as well.
[114.74 --> 117.04]  Next week, as a matter of fact, out in Atlanta, Georgia.
[117.24 --> 117.80]  Is that next week?
[117.82 --> 119.78]  I thought it was 3010 that you were going out there.
[119.78 --> 120.40]  Yeah, yeah, yeah.
[120.64 --> 122.36]  Well, yeah, it's 100 years from now, right?
[122.50 --> 123.10]  Well, millennium.
[123.56 --> 124.20]  Millennium for now.
[124.52 --> 124.96]  Either way.
[125.06 --> 125.34]  Either way.
[125.36 --> 125.96]  It's in the future.
[125.96 --> 128.30]  But lots and lots of fun, but yeah.
[128.30 --> 130.94]  You have a DeLorean you're going to get out there?
[131.20 --> 131.96]  I think so, yeah.
[132.00 --> 135.20]  I'm going to get to 85 and zing my butt over to Atlanta.
[135.90 --> 137.52]  Let me know how the future turns out, buddy.
[137.86 --> 138.30]  Will do.
[138.88 --> 139.16]  Cool.
[139.46 --> 140.48]  Let's get to this episode.
[154.48 --> 157.02]  Episode 0.2.3 of The Change Log.
[157.02 --> 158.16]  I'm your host of Wayne Nettler.
[158.28 --> 162.24]  We're joined today by Charles Lowell and Greg Pollack from Ruby 5.
[162.98 --> 164.98]  Greg, why don't you, I mean, excuse me.
[165.02 --> 166.58]  Charles, introduce yourself.
[166.80 --> 168.78]  Tell the folks who you are and why I should care.
[169.52 --> 170.86]  My name is Charles Lowell.
[171.06 --> 176.14]  I work with Frontside Software, and we build user interfaces for a variety of platforms.
[176.92 --> 179.06]  That's what we do a lot on Ruby.
[180.04 --> 180.88]  Lots of Ruby.
[180.88 --> 182.50]  Tell us about the Ruby racer.
[183.36 --> 188.08]  The Ruby racer is the VA JavaScript integer embedded in the Ruby.
[188.50 --> 194.74]  So what it means, the fact is that you can evaluate JavaScript from inside Ruby.
[194.74 --> 199.10]  You can call Ruby functions from inside JavaScript.
[200.88 --> 201.32]  Okay.
[201.72 --> 202.82]  This is Greg, by the way.
[203.52 --> 206.26]  Yeah, you know, I did a presentation earlier today.
[206.66 --> 213.28]  But as a Ruby developer, you know, I can look at this, and I totally see the value in being able to write Ruby to test my JavaScript.
[213.28 --> 224.14]  And sorry, it sounds ignorant, but what I really like to learn more about are some, like, use cases where I really might want to write, you know, Ruby that writes JavaScript, JavaScript that writes Ruby.
[224.56 --> 225.40]  What are some use cases?
[225.54 --> 228.16]  Where might this be really useful that it's not totally obvious?
[228.76 --> 230.10]  So you can do things.
[230.34 --> 239.68]  One of the examples I gave was if you have templates, for example, if you want to evaluate on the server and on the client,
[239.68 --> 246.24]  if that template image was written in JavaScript, then you can evaluate them in both places.
[246.56 --> 253.32]  And so you're not going to do it in yourself, either with the templates or with the actual code that evaluates the templates, if that makes sense.
[253.42 --> 255.64]  So these templates you're talking about, something like Mustache.js?
[256.10 --> 256.44]  Yes.
[257.00 --> 257.26]  Yes.
[257.36 --> 260.24]  For the folks that may not be aware, who's used Mustache.js?
[261.26 --> 261.92]  A few hands.
[261.96 --> 264.22]  Why don't you give the folks some background on what this is?
[264.26 --> 265.86]  Has anyone used Mustache.rb?
[265.86 --> 272.90]  Have they used this technique where you use them in concert, where you use the same templates on the client and server?
[273.72 --> 273.92]  Okay.
[274.06 --> 282.00]  So Mustache is a templating engine that has both an implementation in JavaScript and an implementation in Ruby, but it has the same syntax.
[282.34 --> 287.58]  If you use one implementation with the same syntax, that would guarantee to get the exact same result.
[287.58 --> 293.52]  Why is an interpreter like this, I guess, required to that sort of thing?
[294.44 --> 308.54]  Well, because if you're, like I said, if you're using the exact same implementation, like suppose you want to extend your syntax, right?
[308.54 --> 316.00]  If you're going to have to do that, if you're using two different languages, two different implementations, you're going to have to change both implementations.
[316.22 --> 322.00]  So a change here is going to be recognized twice.
[322.32 --> 325.70]  If you have a bird environment, it's going to be recognized and triplicate.
[325.70 --> 334.92]  So if you can bring the exact same implementation to all your different runtimes, then you're cutting that out of the equation.
[335.76 --> 344.20]  So in the case of a template rendering, the one way maybe you can look at this is, like, you would normally have to do all the template rendering on the server side,
[344.28 --> 349.34]  but maybe you could save some CPU cycles by pushing that off to your clients, letting the clients do the work,
[349.68 --> 353.86]  and using the same format, the same language.
[353.86 --> 356.66]  Absolutely, and you're just sending data to the client.
[356.80 --> 359.70]  You're not actually, you know, you're not sending display data.
[359.96 --> 362.40]  You're sending the data to the vendor on the client.
[363.16 --> 368.22]  So earlier today you said that sending HTML over the wire was an abomination, I believe.
[368.40 --> 373.18]  A certain Rubyist out there took issue with this.
[373.58 --> 375.90]  He'll remain nameless for this three-annuals GLV.
[376.64 --> 381.04]  So why don't you explain to Glenn what you did by that?
[381.04 --> 388.20]  To clarify, HTML itself is not an abomination, but using it as a data structure is an abomination.
[388.36 --> 390.42]  Now his question was, isn't this what the browser does?
[392.08 --> 397.18]  Well, for the browser, you know, one person's code is another person's data, and so forth.
[397.26 --> 399.94]  I mean, it's the browser's job to use it as data to render.
[399.94 --> 402.42]  But from our perspective, it's a view.
[402.78 --> 406.94]  And using a view to house data, to me, is a smell.
[407.14 --> 411.28]  So for those that didn't catch the talk, you're proposing an alternative that sends what?
[411.86 --> 413.54]  Just JSON, pure JSON.
[413.92 --> 416.96]  Or, you know, something else if that strikes your fancy.
[418.34 --> 419.32]  Can I ask a question?
[419.66 --> 420.84]  Sure, a question from the audience.
[420.84 --> 432.32]  Well, you work for Google.
[432.54 --> 433.16]  I mean, come on.
[433.22 --> 436.56]  You've seen the banana and the potato chips and everything like that.
[436.60 --> 438.74]  It shouldn't matter in the age of Chrome.
[440.00 --> 443.68]  So the question was the performance impact of each approach, right?
[444.26 --> 444.54]  Right.
[444.54 --> 453.84]  It might be slightly less performant, although, honestly, I have not noticed that rendering it on the client is less performant.
[453.90 --> 459.82]  I mean, not so much that it would actually even cause me to investigate, I suppose.
[460.62 --> 462.72]  So ironically, the question was from a Googler.
[464.22 --> 468.56]  And in Ruby Racer, you're actually embedding Google's V8 engine.
[468.82 --> 469.10]  Yes.
[469.54 --> 473.48]  So this is one of those few gems out there that actually requires Python.
[473.48 --> 476.04]  Yes, it requires Python to build.
[476.52 --> 482.86]  So you don't actually ever see it, but when you're installing, in its current form, it does take a while.
[483.68 --> 486.00]  And then it says compiling native extensions.
[486.18 --> 486.94]  This might take a while.
[487.02 --> 494.00]  It's actually using Python and SCONS, which is what V8 uses for its build system, to build the V8 binary.
[497.70 --> 498.62]  So, yeah, it does.
[499.00 --> 502.70]  I think you need Python 2.4 or greater to install this gem.
[503.48 --> 509.18]  Talk a minute about consuming this particular project.
[509.52 --> 516.74]  So you can evaluate JavaScript context by passing a Ruby object, or you can have a Ruby object be the context.
[516.92 --> 517.12]  Yes.
[517.12 --> 526.80]  So you can actually, if you have any arbitrary Ruby instance, you can set up your JavaScript context so that that Ruby instance is the global object.
[527.28 --> 532.68]  So any properties that that Ruby object has are global properties.
[533.14 --> 536.56]  Any methods that it has are global functions.
[536.56 --> 545.52]  And so, for example, if you could actually have a browser object that had a window property and a document property and, you know, an embedded DOM and so forth,
[545.58 --> 553.38]  and that would be kind of how you would implement a browser in Ruby, or at least the skeleton of one.
[553.38 --> 560.24]  So if you have a Ruby object as a global JavaScript value, does Douglas Crockford still cry?
[563.24 --> 565.52]  You'd have to ask Douglas about that.
[566.20 --> 567.44]  Back to templating for a second.
[568.88 --> 569.44]  MustacheJS.
[569.44 --> 573.60]  You mentioned any other templating engines out there that are your favorites?
[574.14 --> 577.42]  JSON template is one that I like very much.
[577.54 --> 582.22]  It's a very functional style templating system.
[583.12 --> 585.20]  And that also is, I believe, from Google.
[585.92 --> 587.56]  Any love for underscore JS?
[588.52 --> 589.98]  You know, I have never used it.
[591.12 --> 591.64]  Blasphemy.
[592.22 --> 593.68]  Smack me on the hands of the ruler.
[593.68 --> 595.96]  Check out episode five with Jeremy Ashkenos.
[596.36 --> 598.00]  I can't pronounce his name correctly.
[598.00 --> 607.04]  One of the things you mentioned on your readme here is that RubyRacer is designed to let you evaluate JavaScript as safely as possible
[607.04 --> 609.74]  unless you tell it to do something more dangerous.
[610.12 --> 612.20]  Can you talk a little bit about what you might use this for?
[612.98 --> 618.82]  Well, by default, when you instantiate a JavaScript context in the RubyRacer,
[619.00 --> 622.14]  you don't have anything except for the standard JavaScript objects.
[622.32 --> 626.96]  So even though it's possible to call Ruby code, you can't.
[626.96 --> 631.10]  You have to explicitly inject into that context the code which you can call.
[631.90 --> 638.82]  And that's important because one of the primary uses of JavaScript is to safely evaluate untrusted code,
[638.90 --> 640.10]  just like you do on the browser.
[640.80 --> 643.44]  And so it's important that by default it be safe.
[643.76 --> 647.64]  So once you start exposing bits of your application via JavaScript,
[648.28 --> 651.18]  in other words, making Ruby classes and Ruby functions available,
[651.18 --> 656.24]  then you do so at your own peril and you need to make sure that those functions are safe.
[656.98 --> 659.04]  So that's what I'm getting at.
[659.12 --> 660.80]  By default, it is safe.
[661.12 --> 666.18]  So you could almost use it to expose some sort of API that allows people to write JavaScript,
[666.40 --> 668.34]  which gets evaluated server-side?
[668.34 --> 668.78]  Yes.
[668.78 --> 669.18]  Yes.
[669.98 --> 672.10]  It gets evaluated as Ruby.
[672.36 --> 677.30]  So even though it looks like you're calling JavaScript, you're actually calling Ruby.
[677.56 --> 677.96]  Interesting.
[678.10 --> 684.52]  So this might be used for some sort of API where people have to write some sort of JavaScript code.
[684.68 --> 686.06]  JavaScript code is kind of universal.
[686.34 --> 688.36]  People have to write really complex code,
[688.44 --> 692.74]  which then gets evaluated on your proprietary lock-behind-closed-door server
[692.74 --> 694.28]  that they couldn't be running on their own.
[694.28 --> 698.56]  And this would be a way to allow them to write some pretty sophisticated API logic.
[699.08 --> 699.44]  Precisely.
[699.44 --> 707.02]  It allows you to provide an API that allows users of that API to extend it
[707.02 --> 710.38]  and use it in ways that you had not foreseen.
[710.90 --> 718.32]  In the same way that the browser allows servers to program it to make it do new and interesting things,
[718.84 --> 723.10]  things that have taken us to really advance the state of the art
[723.10 --> 724.52]  in the last five years or so.
[725.62 --> 728.18]  And so to give a concrete example,
[728.30 --> 731.78]  and another one that I showed here that we've used it for is to actually,
[732.44 --> 734.02]  for an image server.
[734.48 --> 739.32]  So being able to pull down images and then have a set of JavaScript functions
[739.32 --> 744.96]  that actually are bound to Ruby functions that modify the image before it's returned
[744.96 --> 749.20]  so you can enhance the image in pretty much arbitrary ways
[749.20 --> 752.66]  or any arbitrary combination of the primitives that you provide on that server.
[753.10 --> 753.50]  That's cool.
[753.72 --> 756.06]  One other web service that reminds me of,
[756.12 --> 760.76]  there was a voice over IP web service that we were working with at NV Labs for a while
[760.76 --> 765.40]  where basically you had to write code and then either you could upload to the server
[765.40 --> 768.32]  or you specified, you know, go to this URL, download this code,
[768.38 --> 771.28]  and we'll execute it using our voice over IP servers
[771.28 --> 774.22]  and whatever happens happens after that point.
[774.68 --> 777.46]  And they were trying to, they actually had like a Ruby implementation.
[777.46 --> 780.56]  This is, I think, the Trobo API, which we'll talk about,
[780.84 --> 782.32]  which we'll talk about in Ruby 5 this week.
[783.82 --> 786.58]  And so they tried to implement in different languages.
[786.70 --> 789.22]  You could write in Ruby, you could write in Python, you could write in JavaScript,
[790.04 --> 792.16]  and they did a couple other languages maybe.
[792.32 --> 796.68]  But it kind of makes sense that JavaScript seems to be sort of that standard library
[796.68 --> 802.24]  that if you're going to support a language that gets interpreted by your application server side,
[802.24 --> 803.26]  it seems to be the standard.
[803.50 --> 808.02]  And I totally see the value in being able to specify, you know,
[808.04 --> 809.94]  have a sort of sandbox, so to speak.
[810.12 --> 812.68]  It sandboxes your Ruby code so that, you know,
[812.72 --> 816.44]  you can let people run JavaScript against it without having to worry about them doing anything dangerous.
[816.80 --> 820.24]  Yeah, it's a super lightweight virtual machine in a box, basically,
[820.40 --> 821.86]  that you can take with you wherever you go.
[822.40 --> 824.84]  And it's light by purpose.
[824.84 --> 831.84]  I mean, there's only nine standard objects in the JavaScript library or standard constructors.
[832.24 --> 836.56]  You know, you can fit all of them on your two hands, and that's a feature.
[838.22 --> 839.48]  So JavaScript everywhere.
[839.64 --> 844.58]  Someone made the comment in one of the talks today that C was the lingua franca of computing,
[844.72 --> 845.84]  especially in the Unix world.
[846.44 --> 851.10]  And I think perhaps JavaScript may be unseating it at some point.
[851.22 --> 853.08]  You know, it's not as entrenched on the server,
[853.24 --> 856.36]  but with the rise of Node.js and some of these server-side frameworks,
[856.46 --> 861.72]  it seems like everybody is using JavaScript these days in places that we normally didn't use it before.
[861.72 --> 864.16]  How many folks are using JavaScript in their applications?
[865.88 --> 867.52]  How many folks in pretty much the whole room?
[867.58 --> 869.06]  How many folks are using it server-side?
[870.22 --> 871.68]  Oh, wow, more hands than you think.
[872.28 --> 875.52]  Talk a minute about what makes JavaScript special
[875.52 --> 880.78]  and why JavaScript is the renaissance of JavaScript in the last couple of years.
[880.78 --> 887.40]  I mean, I honestly don't know if I'm qualified to talk to the renaissance of JavaScript on the server-side,
[887.64 --> 891.66]  because from my perspective, I like to use it for its original purpose,
[891.80 --> 895.88]  which is a language for embedding and providing safe interfaces.
[895.88 --> 905.38]  So, I mean, while I think that Node is interesting and the CommonJS movement is useful,
[905.66 --> 907.02]  and that the project is useful,
[907.64 --> 914.98]  for me, that part of JavaScript is just not as interesting, frankly,
[915.18 --> 916.80]  just because it's yet another language
[916.80 --> 919.80]  and doesn't bring along all the things that I think really make,
[920.14 --> 923.08]  don't really highlight the things that I think make JavaScript really special.
[923.08 --> 926.76]  And that is the fact that you can completely control the environment.
[927.00 --> 928.58]  You can control its heap size.
[928.68 --> 932.84]  You can control how the instructions get executed,
[933.18 --> 938.72]  and you can embed other interfaces into it safely.
[939.98 --> 941.24]  You know, it's not just on the server.
[941.34 --> 942.32]  It's on the client as well.
[942.80 --> 948.28]  Just in my brief career, I guess I've been doing web development for about 12 years now,
[948.32 --> 952.58]  and it seems like that early on, I guess we were shackled to the DOM, right?
[952.58 --> 955.64]  And so JavaScript was something that we handled with kind of like hazmat gloves,
[955.68 --> 959.08]  and we had all these server-side routines that created the JavaScript for us.
[960.04 --> 962.46]  Whereas, you know, in the last few years,
[962.54 --> 965.08]  basically since prototype and since jQuery came along,
[965.60 --> 971.08]  there's been this sort of rebirth of JavaScript development.
[971.30 --> 974.56]  I think we're finding a lot of the things that we like about Ruby
[974.56 --> 976.48]  are things we like about JavaScript as well.
[976.48 --> 977.08]  Absolutely.
[977.44 --> 978.04]  Absolutely.
[980.10 --> 985.46]  Talk a minute about Ruby Rhino and how it relates to Ruby Racer.
[985.70 --> 990.90]  So the Ruby Rhino is the JRuby counterpart to the Ruby Racer.
[991.42 --> 995.72]  And as the name might imply, rather than being based on the V8 JavaScript interpreter,
[995.86 --> 999.08]  it's based on the Mozilla Rhino JavaScript interpreter.
[999.08 --> 1006.00]  I've taken some care to make them API compatible so that you can, but there,
[1006.26 --> 1010.04]  I'm going to say there is some discrepancy in the API,
[1010.20 --> 1015.80]  but the idea is that you can use the exact same code in the JRuby application
[1015.80 --> 1022.38]  with a little bit of glue to bootstrap and say, okay, I'm using the Rhino, not the Racer.
[1022.38 --> 1026.70]  So, but starting from there, being able to run the exact same code.
[1027.40 --> 1029.16]  Forget for a moment that we have a Googler in the room.
[1029.24 --> 1031.38]  What's the main differences between the two?
[1033.32 --> 1034.32]  V8 and Rhino.
[1034.42 --> 1034.64]  Okay.
[1034.96 --> 1037.22]  Well, the main difference from my perspective,
[1037.52 --> 1041.18]  obviously one being written in C and the other in Java,
[1041.76 --> 1047.78]  is that probably the most important is that the V8 is not multi-threaded.
[1047.78 --> 1053.22]  So, if you're going to be using it in a multi-threaded app,
[1053.54 --> 1058.80]  you're going to have to lock the interpreter with basically a global interpreter lock.
[1058.90 --> 1064.86]  V8 has the same thing as Ruby and Python and all that good stuff.
[1065.30 --> 1068.56]  Whereas Rhino is multi-threaded.
[1069.00 --> 1073.06]  You can enter context from all different threads.
[1073.38 --> 1075.78]  The threading is really great on the Java platform.
[1075.78 --> 1080.46]  So, that's probably the biggest difference for me.
[1081.16 --> 1086.26]  And then, obviously, with the Ruby Rhino, you get Java integration inside your JavaScript,
[1086.48 --> 1088.62]  as well as from Ruby, because you're using J-Ruby.
[1089.42 --> 1091.22]  This is an abbreviated version of the show.
[1091.28 --> 1095.18]  Since we have the second podcast to record, this is usually where we ask,
[1095.34 --> 1098.10]  and I'll put you on the spot, since I don't think we've got a single episode of the change log.
[1098.20 --> 1101.38]  But this is normally we ask the folks, what's in your open source radar,
[1101.50 --> 1104.10]  or what projects other than the ones we just talked about, have you excited?
[1104.10 --> 1106.30]  Which ones have me excited?
[1107.50 --> 1112.16]  Gosh, well, I've been looking at env.js.
[1112.28 --> 1113.56]  I don't know if anybody's ever heard of that,
[1113.64 --> 1118.72]  but that's basically a complete DOM implementation in JavaScript
[1118.72 --> 1123.92]  that is somewhat cross-platform.
[1123.92 --> 1131.12]  So, you can, with just a little bit of native code, whether that's root,
[1131.26 --> 1137.74]  and by native I mean native platform, it can be Ruby, Java, or C,
[1137.98 --> 1141.68]  you can have a DOM implementation up and running.
[1142.24 --> 1145.02]  So, I think that's really, really interesting.
[1145.18 --> 1148.74]  And that lets you do more simulated browser stuff.
[1148.74 --> 1154.44]  So, if you want to do screen scraping and, like, complex interaction with websites programmatically,
[1154.52 --> 1162.54]  that plays a big part, along with, you know, unit testing, your JavaScript code.
[1162.54 --> 1170.18]  I'm also looking at JS DOM, which is another nascent implementation.
[1170.40 --> 1176.76]  It's not quite nearly as far along, but is, shows some promise in terms of being maybe a little bit more flexible.
[1176.76 --> 1179.52]  So, let's see, what else?
[1185.10 --> 1187.62]  I say, you have to just look what I'm following on GitHub.
[1189.12 --> 1190.46]  That's the best place to check it out.
[1190.86 --> 1194.78]  The GitHub page is github.com forward slash cowboy bean.
[1195.28 --> 1197.14]  So, you also have your own podcast?
[1197.54 --> 1197.80]  Yes.
[1197.92 --> 1198.58]  You want to plug in?
[1198.74 --> 1199.40]  Oh, absolutely.
[1199.40 --> 1207.24]  I have the drunkandretired.com podcast, so you can go to drunkandretired.com.
[1208.04 --> 1209.16]  It's not drunk and tired.
[1209.30 --> 1210.20]  I actually tried that earlier.
[1210.34 --> 1210.72]  I didn't catch it.
[1210.80 --> 1211.64]  It's not drunk and tired.
[1212.22 --> 1213.38]  That's a totally different site.
[1213.72 --> 1218.22]  That we try to do every week with my good friend, Michael Cote from RedMonk.
[1218.94 --> 1220.16]  So, you should check it out.
[1220.26 --> 1220.86]  Talking about?
[1221.08 --> 1221.36]  Yes.
[1221.68 --> 1224.84]  Well, talking pretty much about life, the universe, and everything.
[1225.20 --> 1227.62]  Our motto is it's better than half the stuff out there.
[1228.22 --> 1229.10]  That's our motto.
[1229.40 --> 1229.70]  Cool.
[1231.84 --> 1232.56]  Thanks for joining us.
[1238.32 --> 1241.30]  Thank you for listening to this edition of The Change Log.
[1242.38 --> 1249.08]  Point your browser to tale.thechangelog.com to find out what's going on right now in open source.
[1250.30 --> 1255.80]  Also, be sure to head to github.com forward slash explore to catch up on trending and feature repos,
[1255.80 --> 1258.84]  as well as the latest episodes of The Change Log.
[1258.84 --> 1271.96]  Safe in your arms as if the passion show was mine alone.
[1271.96 --> 1281.74]  Open, open, open, open, open for us to try.
[1281.74 --> 1294.82]  Bring it back, bring it back to open, open, open for us to try.
[1294.82 --> 1296.48] BC tratarplus.com forward slash Lubbock.com forward slash north of the share.
[1296.48 --> 1296.92]  Traveler.com forward slash three languages.
[1312.70 --> 1313.14]  Thank you.
