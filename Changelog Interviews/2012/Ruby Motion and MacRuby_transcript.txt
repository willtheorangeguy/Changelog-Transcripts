[0.00 --> 17.92]  Welcome to the ChangeLog episode 0.8.2.
[18.08 --> 19.12]  I'm Adam Stachowiak.
[19.28 --> 20.20]  And I'm Wynne Netherland.
[20.38 --> 21.34]  This is the ChangeLog.
[21.40 --> 23.10]  We cover what's fresh and new and open source.
[23.58 --> 26.64]  If you found us on iTunes, we're also up in the web at thechangelog.com.
[26.72 --> 27.58]  We're also up on GitHub.
[27.58 --> 29.34]  Head to GitHub.com slash explore.
[29.44 --> 33.28]  You'll find some Trinity repos, some feature repos from our blog, as well as the audio podcast.
[33.70 --> 36.80]  And if you're on Twitter, follow the ChangeLog and me, Adam Stach.
[37.14 --> 39.38]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[40.12 --> 43.94]  Speaking of up on GitHub, I've moved on up to GitHub as about a month ago.
[44.16 --> 45.58]  Yeah, you're a GitHub-er now.
[45.76 --> 46.40]  I'm a GitHub-er.
[46.48 --> 51.02]  This is the first show we've put together since I made that move, so I'm not trying to keep any secrets or anything.
[51.16 --> 56.06]  But it's the first time that we've had the opportunity to announce that, so I'm excited to be over at GitHub.
[56.06 --> 57.40]  We don't keep secrets around here.
[57.78 --> 61.28]  Now, speaking of new faces, Sam Sophus has joined us.
[61.42 --> 64.06]  This is his first episode to join us on air.
[64.14 --> 68.42]  He's been blogging over at thechangelog.com for a couple of months on iOS and Coco.
[68.86 --> 71.28]  Sam's a really talented iOS developer.
[71.44 --> 73.40]  He's also got a new app that we want to plug coming out.
[73.88 --> 74.64]  It's called Cheddar.
[74.94 --> 76.18]  It's at cheddarapp.com.
[76.24 --> 80.18]  It's got a web app and an iOS iPhone app as well.
[80.18 --> 86.38]  And it syncs via Pusher, who's been supporters of the show recently.
[86.38 --> 92.78]  And your to-do list just gets updated in real time directly from the web to your phone.
[92.78 --> 95.22]  I love the fact that he actually used Pusher, too.
[95.38 --> 101.22]  It's nice to not so much get a great sponsor, but also to see how it could be used in such an awesome way.
[101.72 --> 102.66]  We've both been using Cheddar.
[102.76 --> 103.70]  I've been really impressed with it.
[104.14 --> 106.56]  It's got some open-source byproducts as well.
[106.66 --> 108.06]  He's got a Pusher library called Bully.
[108.60 --> 108.90]  Oh, wow.
[108.90 --> 109.90]  It's pretty cool.
[110.02 --> 110.58]  Check that out.
[110.58 --> 115.20]  This week we talked to Laurent Sancinetti from MacRuby and RubyMotion.
[115.60 --> 119.68]  And Sam grilled him on some of the finer points of memory management.
[120.02 --> 123.82]  I'd say he actually did quite a good job with this first time out on the podcast, too.
[124.12 --> 127.94]  You know, just having the background of Coco as well as Ruby was a really good fit.
[128.20 --> 131.50]  Sam was playing the part of the expert, and I was just the fanboy as usual.
[131.58 --> 132.10]  Teeing him up.
[132.92 --> 133.32]  Exactly.
[133.78 --> 134.28]  Fun episode.
[134.38 --> 134.94]  Should we get to it?
[135.10 --> 135.64]  Let's do it.
[140.58 --> 150.02]  We're chatting today with Laurent Sancinetti, the developer of RubyMotion and MacRuby before
[150.02 --> 150.30]  that.
[150.54 --> 155.06]  So why don't you expand on that, Laurent, and give yourself an introduction for our listeners?
[155.90 --> 156.28]  Hi.
[156.44 --> 157.66]  Well, thanks for inviting me.
[158.60 --> 167.22]  Yeah, so my name is Laurent Sancinetti, and I was the creator, and I'm still the main developer
[167.22 --> 168.46]  and maintainer of MacRuby.
[168.46 --> 173.96]  MacRuby is a Ruby implementation on top of core OS X technologies.
[174.80 --> 179.26]  And I worked on MacRuby when I was working at Apple.
[179.76 --> 186.80]  So I worked at Apple for about seven years on various things, from OS X to iLife to a lot
[186.80 --> 188.34]  of scripting technologies.
[189.04 --> 190.60]  And MacRuby was one of my projects there.
[191.24 --> 194.16]  And recently, I left Apple to do a startup.
[194.16 --> 197.38]  And so I created a startup a few months ago.
[197.70 --> 199.96]  And the first product is called RubyMotion.
[200.66 --> 205.12]  And RubyMotion is a port of MacRuby for iOS.
[205.46 --> 209.68]  So it allows you to do iOS applications using Ruby.
[210.94 --> 213.52]  And that's all about me, I guess.
[213.52 --> 217.00]  So I'm a long-time Ruby enthusiast.
[217.42 --> 219.90]  And so that's why I really want...
[219.90 --> 224.20]  I'm currently working on pushing Ruby on areas where it has never been yet.
[224.84 --> 230.18]  And iOS is probably the best place for Ruby to exist right now.
[230.18 --> 233.22]  We definitely want to jump into RubyMotion.
[233.52 --> 238.24]  But just to keep this, I guess, chronological, let's talk about MacRuby first and how that
[238.24 --> 239.26]  project came about.
[241.18 --> 243.18]  So MacRuby was...
[244.10 --> 245.16]  So that's a good question.
[245.30 --> 245.86]  If we...
[245.86 --> 247.64]  We can take a history course.
[247.64 --> 253.92]  And if we go back to Lopert, so it was 10.6, if I'm not mistaken.
[254.18 --> 255.18]  No, sorry, 10.5.
[256.36 --> 262.98]  And for 10.5, I was responsible for the integration of Ruby in OS X.
[262.98 --> 270.16]  And so we pushed a new Ruby implementation, which was 1.8.6, which was, at that time, the
[270.16 --> 270.80]  latest version.
[271.00 --> 272.14]  We pushed RubyGems.
[272.66 --> 275.06]  And we also pushed Rails on the system.
[275.30 --> 277.20]  And we pushed RubyCoco.
[277.64 --> 279.26]  And RubyCoco was a bridge.
[280.46 --> 287.00]  Well, it's still a bridge between the Objective C runtime and the C Ruby runtime, which are
[287.00 --> 288.62]  two different programming languages.
[288.62 --> 294.76]  And the goal of RubyCoco was to be a framework that lets you write Mac applications using Ruby.
[295.82 --> 296.98]  But it's a bridge.
[297.28 --> 302.80]  So the problem of RubyCoco is that it has a lot of performance issues and a lot of stability
[302.80 --> 303.38]  problems.
[303.38 --> 309.46]  Because as a bridge, it has to make sure that it has to keep track of two separate object
[309.46 --> 310.66]  models at the same time.
[311.44 --> 318.70]  So for instance, using RubyCoco, you have two different set of classes that exist at the
[318.70 --> 319.76]  same time in your application.
[319.76 --> 325.00]  When you want to use an Objective C class from Ruby, the bridge has to create a fake class
[325.00 --> 326.22]  and forward all the messages.
[326.94 --> 328.30]  So it has a lot of problems.
[328.70 --> 332.90]  And I was chatting with our vice president at the time.
[333.90 --> 335.52]  His name is Bertrand Serlet.
[335.52 --> 343.62]  And he had this idea of why don't you just re-host Ruby on top of the Objective C runtime.
[343.92 --> 347.34]  This way, you don't need to bridge classes and objects anymore.
[347.50 --> 352.22]  You would have a fully native implementation of Ruby, but on top of the same runtime.
[352.50 --> 354.34]  And you would eliminate all the problems.
[354.34 --> 361.74]  And that was, I think, in November 2008, 2004, sorry, or 2005.
[361.88 --> 362.64]  I don't even remember.
[363.26 --> 366.02]  And during the Christmas break, I started hacking on it.
[366.86 --> 368.76]  And it turns out that it was working.
[369.04 --> 372.72]  So I went back to him and I say, well, it's working.
[373.32 --> 375.24]  So should we keep this project?
[375.30 --> 376.24]  And he says, yes, sure.
[376.34 --> 377.04]  Let's go ahead.
[377.04 --> 379.26]  And we picked the name MacRuby.
[379.42 --> 380.62]  And then MacRuby was born.
[382.36 --> 384.22]  So that's the story of MacRuby.
[384.80 --> 388.94]  And MacRuby was maintained at Apple for four years, I think.
[389.56 --> 392.00]  So it was one of my side projects at Apple.
[392.60 --> 397.06]  And the last year and a half, it was my main project at Apple.
[397.26 --> 402.28]  Because MacRuby was used by Apple on a few products.
[402.28 --> 407.92]  And on Lion, actually, some functionality of Lion is written in MacRuby.
[408.10 --> 411.30]  So we really had to make sure that it was working fine.
[412.88 --> 418.48]  So what point did you, I guess, envision in the next phase of that and porting it to iOS
[418.48 --> 420.32]  and what later became RubyMotion?
[421.90 --> 431.12]  Well, so when Lion was about to ship, it was clear that Apple was not interested in maintaining MacRuby anymore.
[431.12 --> 434.30]  So they asked me to work on different projects.
[435.00 --> 440.70]  Then I was a bit sad because MacRuby was really growing.
[440.96 --> 443.92]  And it has a wonderful community around the project.
[444.34 --> 446.24]  So I really didn't want to leave the project.
[446.48 --> 447.50]  So I thought about it.
[447.60 --> 452.26]  And then I realized that in order to keep working on MacRuby,
[452.40 --> 454.10]  one thing I could do is push it on iOS.
[455.92 --> 458.56]  Because this wasn't something Apple was interested to sponsor.
[458.56 --> 462.34]  So I decided to leave the company and do the startup.
[463.70 --> 468.34]  And right now it works because it allows me to keep working on the MacRuby code base
[468.34 --> 472.32]  while I'm making a living out of it.
[472.44 --> 474.26]  So it seems to be working.
[474.26 --> 479.54]  So how much of RubyMotion came from MacRuby?
[479.62 --> 485.72]  I know it uses MacRuby, but obviously there's a lot of stuff to make RubyMotion possible.
[486.46 --> 488.98]  So I'd be interested to hear about that relationship.
[488.98 --> 494.32]  So the runtime is shared across RubyMotion and MacRuby.
[494.96 --> 497.34]  Other than that, everything has been rewritten.
[497.80 --> 500.46]  For instance, RubyMotion comes with its own compiler.
[501.26 --> 506.00]  So it provides static compilation from Ruby code into optimized machine code,
[506.46 --> 509.40]  while MacRuby uses a just-in-time compiler.
[509.40 --> 513.58]  And I had to write static compiler for RubyMotion
[513.58 --> 517.20]  because there is no way you can do just-in-time compilation iOS.
[518.08 --> 520.96]  There is no way to actually create memory pages
[520.96 --> 523.72]  and mark them as executable on iOS devices.
[523.94 --> 526.34]  It's forbidden for security reasons.
[526.64 --> 528.84]  So I had to work around that.
[529.20 --> 535.24]  And also some bits of the runtime have been optimized for iOS constraints.
[535.24 --> 541.16]  And also the memory model is different on RubyMotion
[541.16 --> 544.48]  because we cannot use the Objective-C garbage collector
[544.48 --> 546.32]  because it doesn't exist on iOS.
[546.74 --> 553.22]  So I had to write my own model around the same principle as Arc,
[554.00 --> 557.02]  the latest memory model of Objective-C.
[557.62 --> 562.48]  So besides these differences, the code base is about the same.
[562.48 --> 566.88]  I'd like to draw a contrast, I guess, to some of the other tools in this space.
[566.98 --> 568.70]  And I know architecturally they're quite different,
[568.84 --> 573.16]  but just to give folks a kind of a feel for where RubyMotion fits in.
[573.30 --> 578.20]  So RubyMotion, I guess, in some ways could be compared to Titanium
[578.20 --> 580.94]  from AppCelerator and possibly MonoTouch.
[581.54 --> 584.26]  Would you care to kind of break down its differences architecturally?
[584.26 --> 588.92]  So I don't think it's comparable to Titanium or AppCelerator
[588.92 --> 595.24]  in the sense that RubyMotion lets you go directly into the iOS SDK APIs.
[595.84 --> 597.50]  And also it gives you a binary at the end,
[597.60 --> 599.62]  which is pretty much the same as an Objective-C binary
[599.62 --> 602.42]  when you look at the binary differences.
[602.84 --> 606.32]  So it uses the same runtime as Objective-C apps.
[606.42 --> 608.82]  It uses the same APIs as Objective-C apps.
[608.82 --> 611.28]  So it's more close to MonoTouch.
[611.84 --> 615.58]  MonoTouch is doing the same thing that RubyMotion does, but for C Sharp.
[616.76 --> 620.16]  And on the same side, I think that I'm not very familiar,
[620.28 --> 625.80]  but I think that Titanium is actually using JavaScript to bridge into the...
[625.80 --> 626.10]  That's right.
[626.44 --> 630.14]  And so it's not the same thing because it's using a different runtime.
[630.38 --> 632.88]  It's actually bridging objects and classes,
[633.20 --> 636.06]  and it's creating APIs for the SDK APIs
[636.06 --> 637.42]  so that you can use them in JavaScript.
[638.22 --> 640.74]  While in RubyMotion, when you...
[640.74 --> 645.20]  For instance, when you can create a class that inherits from UI view,
[645.98 --> 647.52]  and it's going to create...
[647.52 --> 651.10]  The class you create in Ruby is going to be an Objective-C class directly
[651.10 --> 652.98]  that inherits from UI view,
[652.98 --> 659.96]  so there are no bridging things that are being made up under the contains.
[660.38 --> 662.00]  So it's really a native solution.
[662.00 --> 669.64]  So I was reading in the RubyMotion docs that you can create a Ruby method
[669.64 --> 672.96]  that's callable from Objective-C, which is really awesome.
[673.38 --> 677.28]  Can you talk a little bit about the language additions and such you've added in RubyMotion?
[677.28 --> 683.46]  So these language additions have been introduced in MacRuby,
[683.58 --> 685.56]  so they are not new in RubyMotion.
[687.48 --> 688.28]  The thing is that...
[688.92 --> 692.20]  So if we go back to Blubboard and to Ruby Coco,
[693.28 --> 694.12]  in Ruby Coco,
[694.52 --> 698.92]  the only way to define an Objective-C selector in Ruby
[698.92 --> 703.88]  was to replace the semicolons with underscore characters.
[703.88 --> 709.44]  So for instance, you would do def, insert object underscore,
[710.40 --> 712.32]  add index underscore,
[712.78 --> 714.70]  then open parenthesis and your arguments.
[715.22 --> 716.56]  So that wasn't very natural.
[717.28 --> 720.26]  And I thought about that a lot when I started MacRuby,
[720.92 --> 722.66]  and I came up with this syntax.
[723.30 --> 725.74]  Then I had a couple discussions with Matt,
[726.38 --> 727.32]  the author of Ruby,
[727.32 --> 735.72]  and we came up that it was pretty the best solution,
[736.24 --> 740.48]  the best syntax that we could play.
[742.16 --> 745.38]  So we used that.
[745.60 --> 746.16]  We introduced...
[746.16 --> 747.84]  So this syntax was introduced in MacRuby,
[748.20 --> 751.54]  and it was picked up with RubyMotion after.
[751.54 --> 755.50]  So that's not a new extension.
[757.00 --> 759.44]  But basically, we extend the Ruby language
[759.44 --> 763.26]  so that you can define Objective-C selectors in Ruby,
[763.74 --> 766.34]  and that you can also call Objective-C selectors
[766.34 --> 767.44]  using the same syntax.
[767.98 --> 770.58]  We should mention that RubyMotion is not open source,
[770.70 --> 772.42]  although this week,
[772.60 --> 775.74]  you've open sourced part of the tool chain,
[775.86 --> 776.98]  the command line tool chain.
[777.14 --> 777.82]  Let's talk a bit about,
[777.82 --> 781.58]  maybe as far as feature parity of developing Cocoa apps
[781.58 --> 785.32]  in Xcode versus the experience in RubyMotion.
[786.36 --> 786.88]  Yeah.
[787.22 --> 788.10]  So, yeah.
[788.22 --> 789.82]  So we...
[789.82 --> 790.40]  So, yeah.
[790.46 --> 793.88]  Last week, we open sourced the build system of RubyMotion.
[794.70 --> 797.26]  So the community is growing so fast,
[797.34 --> 800.00]  and it's actually trying to extend the platform
[800.00 --> 802.58]  so quickly that it was inevitable
[802.58 --> 803.90]  to open source these parts.
[804.68 --> 805.24]  And right now,
[805.24 --> 809.14]  I think there are over five pull requests on GitHub already
[809.14 --> 811.48]  about extending the build system,
[811.60 --> 812.84]  so it was definitely a good idea.
[814.08 --> 818.72]  But if we compare RubyMotion with Objective-C and Xcode,
[818.84 --> 820.34]  I guess that was the question,
[821.06 --> 823.70]  it's definitely a different experience.
[823.88 --> 824.46]  In RubyMotion,
[824.64 --> 826.08]  you do everything in the terminal
[826.08 --> 827.60]  using a command line.
[827.60 --> 831.20]  So you keep using your favorite text editor,
[831.94 --> 834.88]  Vim or TextMate or Sublim Text,
[835.04 --> 835.80]  or even Redcar,
[835.90 --> 836.82]  which is actually great.
[837.66 --> 839.64]  You keep using your favorite text editor,
[839.80 --> 841.76]  and you use the terminal for everything else.
[842.42 --> 843.50]  Creating projects,
[844.06 --> 844.94]  building projects,
[845.48 --> 847.20]  reading your projects in the simulator,
[848.20 --> 851.48]  sending your projects to your iOS device,
[851.70 --> 852.50]  iPhone or iPad,
[852.50 --> 856.08]  or even creating IP archives
[856.08 --> 857.98]  so that you can send them to the App Store.
[858.10 --> 859.54]  Everything is done from the command line.
[859.72 --> 861.30]  It's always one command that you type.
[861.90 --> 865.76]  So it's very different from this Xcode environment
[865.76 --> 868.66]  where you do everything inside the same window,
[869.34 --> 871.36]  and you type your code inside the same window,
[871.46 --> 872.78]  you get debugging.
[872.78 --> 877.06]  So it's a bit different.
[877.84 --> 878.58]  I think the main,
[878.92 --> 880.52]  probably the biggest difference so far
[880.52 --> 881.52]  is that in RubyMotion,
[882.14 --> 883.58]  when you type Rake,
[883.76 --> 884.26]  by default,
[884.38 --> 886.78]  it starts the simulator with your project,
[887.38 --> 889.80]  and there is an interactive console
[889.80 --> 891.60]  that shows up by default.
[891.92 --> 892.96]  It's called Repo,
[893.48 --> 895.24]  and you can type expressions there
[895.24 --> 897.48]  that are actually interpreted in real time
[897.48 --> 898.92]  inside your application,
[899.16 --> 899.98]  running on the simulator.
[900.72 --> 901.86]  So this is really something
[901.86 --> 903.36]  that is very different from Xcode
[903.36 --> 904.62]  because Xcode doesn't have
[904.62 --> 906.96]  this kind of interactive way
[906.96 --> 909.02]  of communicating with your application yet.
[909.68 --> 910.34]  So in RubyMotion,
[910.50 --> 911.20]  you can, for instance,
[911.42 --> 914.32]  select elements from the simulator
[914.32 --> 915.72]  using your mouse
[915.72 --> 917.58]  and maintaining the command key.
[918.04 --> 920.56]  Then it creates a new context,
[921.10 --> 922.68]  a new shell context inside Repo,
[923.22 --> 923.86]  and from there,
[923.98 --> 925.18]  you can type expressions
[925.18 --> 926.52]  like you can change the frame,
[926.64 --> 928.56]  you can change the background view,
[928.76 --> 929.88]  you can create new views.
[929.88 --> 932.36]  So it's actually very interesting
[932.36 --> 933.92]  to first,
[934.04 --> 936.52]  to introspect all the APIs of iOS
[936.52 --> 939.70]  because you can try APIs
[939.70 --> 941.58]  using the console.
[941.74 --> 942.30]  It's really nice.
[943.18 --> 943.74]  And also,
[943.92 --> 944.86]  it's actually very cool
[944.86 --> 945.96]  to debug your application.
[946.74 --> 948.04]  So when there is something going wrong,
[948.16 --> 948.66]  you can know,
[949.46 --> 950.10]  you can, for instance,
[950.18 --> 951.60]  connect to a specific view,
[951.68 --> 952.96]  and then you can type expressions there,
[953.02 --> 955.48]  and you can try to fix the bug in real time.
[955.48 --> 956.72]  And then once you're happy,
[957.16 --> 959.58]  you can copy-paste the code back to your editor.
[960.10 --> 961.84]  It was interesting seeing the,
[961.88 --> 962.46]  I guess,
[962.52 --> 964.24]  mixed reactions to RubyMotion
[964.24 --> 965.46]  from Objective-C developers.
[965.70 --> 966.64]  So, Sam,
[966.70 --> 968.22]  you are an Objective-C developer.
[968.40 --> 969.98]  What has been your impression of the Repo?
[969.98 --> 970.26]  It's, like,
[971.20 --> 972.46]  mind-blowingly fantastic.
[973.80 --> 974.96]  Coming from Objective-C,
[975.04 --> 975.24]  like,
[975.58 --> 977.06]  only working with Xcode and such,
[977.14 --> 977.32]  like,
[977.86 --> 979.24]  I was trying to add some custom fonts
[979.24 --> 980.44]  to a RubyMotion application,
[980.44 --> 982.36]  and normally I would just, like,
[983.14 --> 984.34]  because the font names are, like,
[984.82 --> 985.92]  kind of arbitrary
[985.92 --> 987.16]  depending on which font you're using,
[987.24 --> 987.60]  so I was, like,
[988.20 --> 989.54]  I usually go in AppDelegate
[989.54 --> 989.98]  and, like,
[990.34 --> 991.28]  log all the fonts
[991.28 --> 992.00]  and, like,
[992.26 --> 993.36]  find which one it is.
[993.40 --> 993.64]  And I was, like,
[993.64 --> 993.96]  oh, wait,
[994.06 --> 994.78]  I have a console.
[994.90 --> 995.68]  And I went in, like,
[996.10 --> 996.62]  UI font,
[996.74 --> 997.56]  like, family names,
[997.62 --> 997.96]  and, like,
[998.32 --> 998.92]  there they are.
[998.94 --> 999.24]  And I was, like,
[999.56 --> 1000.66]  this is fantastic.
[1002.20 --> 1002.50]  Like,
[1002.94 --> 1004.10]  I don't think, like,
[1004.24 --> 1005.04]  Objective-C developers
[1005.04 --> 1007.28]  really know what they're missing out on
[1007.28 --> 1009.62]  because the only console
[1009.62 --> 1010.38]  we're really used to
[1010.38 --> 1010.80]  is, like,
[1010.84 --> 1011.50]  setting a breakpoint
[1011.50 --> 1012.10]  and then, like,
[1012.60 --> 1013.74]  GDB or LLDB,
[1013.78 --> 1013.94]  like,
[1014.02 --> 1015.00]  because it really worked that well.
[1015.24 --> 1016.88]  And, yeah,
[1016.94 --> 1017.44]  it's, like,
[1018.00 --> 1019.96]  people should, like,
[1020.00 --> 1020.72]  be really excited
[1020.72 --> 1021.88]  to play with it.
[1023.22 --> 1024.40]  Another thing that's, like,
[1024.92 --> 1025.68]  super amazing
[1025.68 --> 1027.14]  that I was, like,
[1027.64 --> 1028.46]  really happy about,
[1029.04 --> 1030.16]  I put the fonts
[1030.16 --> 1031.48]  in my resources directory
[1031.48 --> 1031.90]  and, like,
[1031.94 --> 1033.10]  the build system automatically
[1033.10 --> 1035.14]  added the info plist stuff
[1035.14 --> 1035.60]  for me,
[1035.84 --> 1037.82]  which is really awesome.
[1037.98 --> 1038.56]  So, good work.
[1038.56 --> 1040.00]  Yeah,
[1040.06 --> 1041.38]  we tried to,
[1041.92 --> 1043.36]  the build system
[1043.36 --> 1044.64]  was really designed
[1044.64 --> 1045.48]  so that it fixed
[1045.48 --> 1046.60]  everything by default.
[1046.80 --> 1047.84]  You don't need to specify
[1047.84 --> 1049.64]  information.
[1049.98 --> 1051.04]  It tries to be smart.
[1051.48 --> 1052.02]  And sometimes
[1052.02 --> 1053.22]  it tries to be too smart.
[1053.62 --> 1053.64]  So,
[1054.28 --> 1055.12]  we need to,
[1055.52 --> 1056.42]  there are a few things
[1056.42 --> 1057.46]  that we should pretty fix.
[1057.58 --> 1058.06]  But, yeah,
[1058.18 --> 1059.86]  that's the main idea
[1059.86 --> 1060.80]  behind the build system.
[1060.80 --> 1061.36]  Yeah,
[1061.38 --> 1062.62]  that's actually my favorite part
[1062.62 --> 1063.74]  of Ruby Motion
[1063.74 --> 1065.14]  is how, like,
[1065.76 --> 1066.44]  easy that is
[1066.44 --> 1066.92]  versus, like,
[1066.94 --> 1067.46]  dealing with
[1067.46 --> 1068.42]  all these dialogues
[1068.42 --> 1068.98]  in Xcode
[1068.98 --> 1070.52]  and build configurations.
[1070.90 --> 1071.30]  And, yeah,
[1071.32 --> 1072.30]  it's really fantastic.
[1072.88 --> 1073.14]  Laurent,
[1073.22 --> 1074.24]  would you consider yourself
[1074.24 --> 1075.72]  just a tools developer
[1075.72 --> 1076.88]  or are you an end-user
[1076.88 --> 1077.72]  developer as well?
[1077.80 --> 1077.90]  I mean,
[1077.92 --> 1078.38]  are you scratching
[1078.38 --> 1079.06]  your own itch
[1079.06 --> 1079.66]  when you're building
[1079.66 --> 1080.20]  these features
[1080.20 --> 1081.26]  or are you listening
[1081.26 --> 1081.68]  to feedback
[1081.68 --> 1082.42]  from others
[1082.42 --> 1082.88]  in the community?
[1084.46 --> 1084.94]  Well,
[1085.08 --> 1086.58]  that's a good question.
[1086.58 --> 1086.98]  Well,
[1088.06 --> 1088.56]  personally,
[1088.72 --> 1090.24]  I'm a programming language
[1090.24 --> 1090.80]  enthusiast,
[1090.94 --> 1092.70]  so my favorite
[1092.70 --> 1093.70]  things to do
[1093.70 --> 1094.24]  is designing
[1094.24 --> 1095.16]  programming languages.
[1095.80 --> 1096.28]  So,
[1096.34 --> 1096.88]  I really like
[1096.88 --> 1097.46]  learning new
[1097.46 --> 1098.22]  programming languages
[1098.22 --> 1098.92]  and trying,
[1099.06 --> 1099.98]  I've been designing
[1099.98 --> 1100.84]  my own language
[1100.84 --> 1102.04]  since a couple years.
[1102.66 --> 1103.82]  But this is really
[1103.82 --> 1104.94]  what excites me the most.
[1105.40 --> 1105.68]  Now,
[1105.76 --> 1106.34]  in Ruby Motion,
[1106.50 --> 1106.96]  what I like
[1106.96 --> 1107.70]  is that I can keep
[1107.70 --> 1109.70]  working on the project
[1109.70 --> 1110.62]  I created at Apple.
[1110.98 --> 1112.00]  And this is a code base
[1112.00 --> 1113.26]  I'm very familiar with.
[1114.02 --> 1115.74]  But I'm not super interested
[1115.74 --> 1116.46]  in working on
[1116.46 --> 1116.88]  applications.
[1117.32 --> 1118.30]  I prefer to work
[1118.30 --> 1119.02]  on runtimes,
[1119.94 --> 1120.64]  compilers,
[1122.14 --> 1124.00]  garbage collectors,
[1124.20 --> 1124.80]  this kind of thing.
[1124.80 --> 1125.10]  So,
[1126.02 --> 1127.60]  working on Ruby Motion
[1127.60 --> 1128.66]  lets me work
[1128.66 --> 1129.80]  on compilers.
[1130.10 --> 1130.12]  So,
[1130.28 --> 1130.82]  this is really
[1130.82 --> 1131.22]  the area
[1131.22 --> 1133.36]  I'm very excited about.
[1133.86 --> 1134.60]  But I'm not
[1134.60 --> 1135.86]  super excited about
[1135.86 --> 1136.98]  using Ruby Motion
[1136.98 --> 1138.00]  to write applications.
[1139.10 --> 1139.96]  You mentioned
[1139.96 --> 1141.32]  community growth
[1141.32 --> 1141.86]  is one reason
[1141.86 --> 1142.72]  why you open sourced
[1142.72 --> 1143.76]  the tool chain.
[1144.16 --> 1145.26]  This is a unique project
[1145.26 --> 1145.72]  in that you've got
[1145.72 --> 1146.38]  a couple of different
[1146.38 --> 1147.40]  dimensions in which
[1147.40 --> 1148.18]  the community grows.
[1148.30 --> 1149.04]  You've got not only
[1149.04 --> 1150.32]  the Ruby gems
[1150.32 --> 1151.36]  for the Ruby community,
[1151.50 --> 1152.74]  but also Cocoa Pods,
[1152.74 --> 1153.20]  which we've had
[1153.20 --> 1154.80]  on the show previously
[1154.80 --> 1157.66]  for Cocoa Framework.
[1157.80 --> 1157.98]  So,
[1158.36 --> 1159.40]  do you see
[1159.40 --> 1160.10]  explosive growth
[1160.10 --> 1161.10]  on both of those
[1161.10 --> 1161.84]  angles?
[1163.22 --> 1163.94]  Probably,
[1164.16 --> 1164.28]  yeah.
[1164.76 --> 1165.04]  So,
[1165.22 --> 1165.92]  I think there are
[1165.92 --> 1166.72]  over 100
[1166.72 --> 1169.24]  open source projects
[1169.24 --> 1170.28]  related to Ruby Motion
[1170.28 --> 1170.66]  and GitHub.
[1170.66 --> 1172.12]  and most of them
[1172.12 --> 1173.44]  are sample code.
[1173.54 --> 1174.68]  But there are
[1174.68 --> 1175.82]  quite a few libraries
[1175.82 --> 1176.64]  that are growing.
[1177.64 --> 1178.44]  Libraries around
[1178.44 --> 1179.04]  UIKit,
[1179.16 --> 1179.68]  CoreData,
[1180.36 --> 1180.92]  OpenGL,
[1181.76 --> 1182.60]  and various
[1182.60 --> 1183.58]  third-party libraries
[1183.58 --> 1184.92]  like Cocoa 2D,
[1185.44 --> 1186.04]  Cocoa 2D,
[1186.14 --> 1186.30]  sorry,
[1186.52 --> 1187.68]  or the Parse SDK,
[1187.92 --> 1188.58]  Facebook SDK.
[1188.58 --> 1189.24]  So,
[1189.76 --> 1191.32]  we are starting
[1191.32 --> 1191.80]  to see
[1191.80 --> 1194.14]  an ecosystem
[1194.14 --> 1194.82]  that's growing
[1194.82 --> 1195.62]  around libraries
[1195.62 --> 1196.30]  for Ruby Motion.
[1197.04 --> 1197.84]  And so far,
[1197.92 --> 1198.86]  people are
[1198.86 --> 1200.26]  making gems
[1200.26 --> 1202.22]  for these libraries.
[1203.26 --> 1204.38]  And Cocoa Pods
[1204.38 --> 1204.72]  has been,
[1205.26 --> 1205.82]  Cocoa Pods
[1205.82 --> 1206.24]  right now
[1206.24 --> 1206.92]  is being used
[1206.92 --> 1207.68]  to bridge,
[1208.18 --> 1209.32]  actually to vendor
[1209.32 --> 1210.58]  third-party
[1210.58 --> 1211.10]  Object.E.C.
[1211.10 --> 1211.50]  libraries
[1211.50 --> 1212.58]  inside your project.
[1213.26 --> 1213.86]  But I've been
[1213.86 --> 1215.26]  talking to the
[1215.26 --> 1216.00]  Cocoa Pods author,
[1216.16 --> 1216.66]  which is actually
[1216.66 --> 1217.34]  a friend of mine,
[1218.38 --> 1219.00]  and he's my
[1219.00 --> 1219.74]  personal hero.
[1219.94 --> 1220.14]  So,
[1220.44 --> 1221.44]  if Eloy
[1221.44 --> 1222.00]  is listening
[1222.00 --> 1222.78]  to that podcast,
[1223.42 --> 1223.98]  he will know that.
[1224.32 --> 1224.94]  But we've been
[1224.94 --> 1225.70]  chatting about that,
[1225.70 --> 1227.50]  and there is
[1227.50 --> 1228.58]  probably a way
[1228.58 --> 1229.24]  that we can use
[1229.24 --> 1229.78]  Cocoa Pods
[1229.78 --> 1231.80]  to also include
[1231.80 --> 1233.22]  pure Ruby
[1233.22 --> 1233.74]  extensions
[1233.74 --> 1234.92]  for Ruby Motion.
[1235.62 --> 1235.90]  So,
[1235.98 --> 1236.60]  we don't know yet
[1236.60 --> 1237.94]  where the community
[1237.94 --> 1238.42]  would go,
[1238.96 --> 1240.04]  but I think
[1240.04 --> 1240.70]  that if we can
[1240.70 --> 1241.40]  use the same
[1241.40 --> 1243.78]  package system
[1243.78 --> 1244.70]  for everything,
[1244.94 --> 1245.48]  that's pretty
[1245.48 --> 1245.94]  going to be
[1245.94 --> 1247.12]  the best solution,
[1247.30 --> 1248.52]  and the simplest
[1248.52 --> 1249.02]  solution,
[1249.14 --> 1249.36]  at least,
[1249.52 --> 1250.50]  for Ruby Motion.
[1251.84 --> 1252.28]  So,
[1252.40 --> 1252.58]  Sam,
[1252.66 --> 1253.56]  you're both
[1253.56 --> 1254.46]  an Objective-C
[1254.46 --> 1255.44]  developer and a Rubyist.
[1255.56 --> 1256.42]  How do you see
[1256.42 --> 1257.34]  Ruby Motion
[1257.34 --> 1258.34]  changing the way
[1258.34 --> 1259.18]  that you tackle
[1259.18 --> 1259.72]  applications?
[1260.38 --> 1262.12]  It's interesting,
[1262.82 --> 1264.00]  because as an
[1264.00 --> 1264.74]  Objective-C developer,
[1264.96 --> 1265.64]  there's all these
[1265.64 --> 1266.46]  tools like
[1266.46 --> 1267.70]  Titanium and such,
[1267.92 --> 1269.18]  and looking at
[1269.18 --> 1269.46]  those,
[1269.56 --> 1269.78]  it's like,
[1269.84 --> 1269.94]  well,
[1270.00 --> 1270.44]  this is just
[1270.44 --> 1270.72]  like,
[1270.72 --> 1272.26]  a silly bridge
[1272.26 --> 1272.70]  that doesn't
[1272.70 --> 1273.24]  work that well,
[1273.32 --> 1274.48]  or generates
[1274.48 --> 1275.04]  all this code
[1275.04 --> 1275.46]  that runs in
[1275.46 --> 1275.84]  a WebView,
[1276.02 --> 1277.08]  or whatever,
[1277.32 --> 1279.32]  and I've been
[1279.32 --> 1280.12]  opposed to all
[1280.12 --> 1280.64]  these sort of
[1280.64 --> 1281.32]  tools that do
[1281.32 --> 1281.90]  anything except
[1281.90 --> 1282.50]  Objective-C,
[1283.18 --> 1283.78]  but that's why
[1283.78 --> 1284.40]  Ruby Motion's
[1284.40 --> 1284.92]  so interesting,
[1285.06 --> 1285.40]  because it's
[1285.40 --> 1285.70]  actually,
[1285.94 --> 1286.00]  like,
[1286.70 --> 1287.66]  makes a good
[1287.66 --> 1287.98]  binary,
[1288.20 --> 1288.68]  and it's not
[1288.68 --> 1290.20]  just writing
[1290.20 --> 1290.90]  Objective-C or
[1290.90 --> 1291.42]  WebViews.
[1293.00 --> 1293.38]  I don't know,
[1293.42 --> 1293.90]  it's interesting.
[1295.08 --> 1295.72]  It's something
[1295.72 --> 1297.00]  that I didn't
[1297.00 --> 1297.52]  want to like
[1297.52 --> 1297.98]  at first,
[1298.08 --> 1299.24]  but I really
[1299.24 --> 1299.82]  like it a lot.
[1300.72 --> 1301.70]  So,
[1301.70 --> 1301.92]  Laurent,
[1302.04 --> 1302.60]  do you consider
[1302.60 --> 1303.54]  this a gateway
[1303.54 --> 1304.70]  drug to Coco
[1304.70 --> 1305.36]  for folks that
[1305.36 --> 1305.94]  may not know
[1305.94 --> 1306.62]  Objective-C?
[1306.74 --> 1307.16]  Do you see it
[1307.16 --> 1307.78]  as an intermediate
[1307.78 --> 1308.20]  step,
[1308.24 --> 1308.56]  or is this
[1308.56 --> 1309.64]  something that
[1309.64 --> 1310.92]  you hope folks
[1310.92 --> 1311.42]  will camp out
[1311.42 --> 1312.02]  in for a while
[1312.02 --> 1312.60]  and just build
[1312.60 --> 1313.48]  robust applications
[1313.48 --> 1314.06]  in Ruby Motion?
[1314.06 --> 1316.12]  Yeah,
[1316.16 --> 1316.58]  that's a good
[1316.58 --> 1316.98]  question.
[1316.98 --> 1318.04]  I think that
[1318.04 --> 1319.38]  Ruby Motion
[1319.38 --> 1320.04]  is definitely
[1320.04 --> 1321.28]  a gateway
[1321.28 --> 1321.92]  to iOS
[1321.92 --> 1322.80]  for people
[1322.80 --> 1323.26]  who are not
[1323.26 --> 1323.86]  familiar with
[1323.86 --> 1324.02]  C.
[1324.84 --> 1325.66]  And the
[1325.66 --> 1325.98]  problem with
[1325.98 --> 1326.56]  Objective-C
[1326.56 --> 1327.02]  is really
[1327.02 --> 1327.70]  that it's
[1327.70 --> 1328.30]  a C-based
[1328.30 --> 1328.74]  language,
[1328.92 --> 1329.38]  and most
[1329.38 --> 1330.80]  programmers
[1330.80 --> 1331.44]  these days
[1331.44 --> 1332.86]  don't know
[1332.86 --> 1333.40]  about C,
[1333.50 --> 1333.96]  so when they
[1333.96 --> 1334.96]  pick Objective-C,
[1335.52 --> 1336.20]  they have all
[1336.20 --> 1336.74]  sorts of
[1336.74 --> 1337.52]  problems
[1337.52 --> 1338.02]  trying to
[1338.02 --> 1338.44]  figure out
[1338.44 --> 1338.80]  what the
[1338.80 --> 1339.42]  pointer is,
[1339.42 --> 1342.48]  so all
[1342.48 --> 1342.96]  the C
[1342.96 --> 1345.06]  background
[1345.06 --> 1345.66]  that comes
[1345.66 --> 1346.46]  with when
[1346.46 --> 1346.72]  you use
[1346.72 --> 1347.28]  Objective-C,
[1347.36 --> 1347.64]  they really
[1347.64 --> 1347.92]  have an
[1347.92 --> 1348.22]  issue
[1348.22 --> 1351.02]  to actually
[1351.02 --> 1351.76]  be comfortable
[1351.76 --> 1352.36]  with that.
[1352.96 --> 1353.78]  But Ruby
[1353.78 --> 1354.24]  Motion is
[1354.24 --> 1354.74]  very different,
[1354.94 --> 1355.48]  so they
[1355.48 --> 1356.86]  just need to
[1356.86 --> 1357.46]  learn how to
[1357.46 --> 1358.08]  read Objective-C
[1358.08 --> 1358.56]  interface,
[1358.70 --> 1359.04]  which is
[1359.04 --> 1360.28]  like one
[1360.28 --> 1360.80]  person of
[1360.80 --> 1361.26]  the language,
[1361.40 --> 1361.66]  and then
[1361.66 --> 1362.40]  they are
[1362.40 --> 1362.62]  set,
[1362.68 --> 1362.88]  they can
[1362.88 --> 1363.26]  use all
[1363.26 --> 1363.68]  the APIs
[1363.68 --> 1364.56]  and they
[1364.56 --> 1364.90]  can build
[1364.90 --> 1365.24]  stuff.
[1366.42 --> 1366.64]  So I
[1366.64 --> 1366.86]  think that
[1366.86 --> 1367.20]  Ruby Motion
[1367.20 --> 1367.80]  is definitely
[1367.80 --> 1368.50]  a good way
[1368.50 --> 1368.82]  to get
[1368.82 --> 1369.14]  new
[1369.14 --> 1369.68]  programmers
[1369.68 --> 1370.48]  inside
[1370.48 --> 1371.24]  the
[1371.24 --> 1371.50]  iOS
[1371.50 --> 1372.00]  community.
[1372.62 --> 1373.26]  And I'm
[1373.26 --> 1373.90]  currently in
[1373.90 --> 1374.22]  discussions
[1374.22 --> 1374.62]  with a
[1374.62 --> 1374.86]  few
[1374.86 --> 1377.44]  teaching
[1377.44 --> 1377.90]  groups
[1377.90 --> 1379.16]  around the
[1379.16 --> 1379.38]  globe
[1379.38 --> 1379.82]  that are
[1379.82 --> 1380.52]  teaching
[1380.52 --> 1380.90]  iOS,
[1381.34 --> 1381.76]  and they
[1381.76 --> 1382.06]  are very
[1382.06 --> 1382.34]  interested
[1382.34 --> 1382.74]  in using
[1382.74 --> 1383.24]  Ruby Motion
[1383.24 --> 1384.30]  in that
[1384.30 --> 1384.62]  way,
[1384.88 --> 1385.50]  so that
[1385.50 --> 1386.10]  they can
[1386.10 --> 1386.46]  get new
[1386.46 --> 1386.86]  programmers
[1386.86 --> 1387.20]  on the
[1387.20 --> 1387.44]  platform
[1387.44 --> 1388.18]  more quickly
[1388.18 --> 1390.12]  instead of
[1390.12 --> 1390.68]  actually teaching
[1390.68 --> 1391.22]  them C and
[1391.22 --> 1391.78]  Objective-C.
[1392.48 --> 1392.88]  But at the
[1392.88 --> 1393.40]  same time,
[1393.54 --> 1394.22]  I think that
[1394.22 --> 1394.82]  right now,
[1394.84 --> 1395.20]  Ruby Motion
[1395.20 --> 1395.68]  is very
[1395.68 --> 1395.98]  young,
[1396.14 --> 1397.24]  and I
[1397.24 --> 1397.62]  think it's
[1397.62 --> 1399.24]  only a
[1399.24 --> 1399.88]  month old.
[1400.42 --> 1400.82]  But in
[1400.82 --> 1401.38]  the future,
[1402.00 --> 1402.46]  there will
[1402.46 --> 1402.94]  probably be
[1402.94 --> 1404.22]  mature DSLs,
[1404.32 --> 1404.88]  domain-specific
[1404.88 --> 1406.16]  languages that
[1406.16 --> 1406.54]  run Ruby
[1406.54 --> 1407.88]  Motion that
[1407.88 --> 1408.62]  will let you
[1408.62 --> 1409.60]  write applications
[1409.60 --> 1410.52]  in a very
[1410.52 --> 1411.12]  short amount
[1411.12 --> 1411.84]  of Ruby
[1411.84 --> 1412.20]  code.
[1412.68 --> 1413.18]  Right now,
[1413.22 --> 1413.44]  when you
[1413.44 --> 1414.14]  look at the
[1414.14 --> 1414.56]  Ruby Motion
[1414.56 --> 1414.88]  app,
[1415.38 --> 1415.96]  you can see
[1415.96 --> 1416.46]  calls to
[1416.46 --> 1416.90]  the iOS
[1416.90 --> 1417.30]  SDK.
[1418.60 --> 1419.20]  And people
[1419.20 --> 1419.48]  say,
[1419.56 --> 1419.64]  well,
[1419.66 --> 1420.12]  it looks like
[1420.12 --> 1420.72]  Objective-C,
[1420.84 --> 1421.40]  and that's
[1421.40 --> 1421.62]  true,
[1421.72 --> 1422.22]  we use the
[1422.22 --> 1422.72]  same APIs.
[1422.72 --> 1423.82]  And the
[1423.82 --> 1424.44]  power of
[1424.44 --> 1425.40]  iOS are in
[1425.40 --> 1425.86]  the APIs,
[1426.04 --> 1426.30]  not the
[1426.30 --> 1426.64]  language,
[1427.20 --> 1427.68]  of course.
[1428.26 --> 1428.92]  But I
[1428.92 --> 1429.40]  think that in
[1429.40 --> 1429.82]  the future,
[1429.94 --> 1430.42]  we will see
[1430.42 --> 1431.88]  mature libraries
[1431.88 --> 1432.82]  around UIKit
[1432.82 --> 1433.36]  and CoreData
[1433.36 --> 1433.94]  and everything.
[1434.66 --> 1435.38]  And I
[1435.38 --> 1435.64]  think you
[1435.64 --> 1436.10]  will definitely
[1436.10 --> 1436.72]  be able to
[1436.72 --> 1437.36]  write a full
[1437.36 --> 1437.64]  fledged
[1437.64 --> 1439.10]  application just
[1439.10 --> 1439.58]  by using
[1439.58 --> 1440.20]  these libraries.
[1441.08 --> 1442.14]  And from
[1442.14 --> 1443.16]  there, if you
[1443.16 --> 1443.46]  can, for
[1443.46 --> 1444.06]  instance, write
[1444.06 --> 1445.00]  a real app in
[1445.00 --> 1447.06]  less than 100
[1447.06 --> 1447.62]  lines of
[1447.62 --> 1449.22]  Ruby, I
[1449.22 --> 1449.72]  don't think
[1449.72 --> 1450.10]  that Ruby
[1450.10 --> 1450.66]  Motion would
[1450.66 --> 1451.54]  be a gate
[1451.54 --> 1452.12]  rate drag
[1452.12 --> 1452.50]  anymore,
[1453.10 --> 1453.78]  because people
[1453.78 --> 1454.18]  will probably
[1454.18 --> 1454.80]  stick to Ruby
[1454.80 --> 1455.40]  Motion for
[1455.40 --> 1455.88]  everything.
[1457.02 --> 1457.36]  When you
[1457.36 --> 1457.88]  can write an
[1457.88 --> 1458.44]  application in
[1458.44 --> 1459.50]  100 lines,
[1459.68 --> 1460.20]  would you,
[1460.82 --> 1461.94]  I don't know,
[1461.98 --> 1462.50]  rewrite it in
[1462.50 --> 1463.08]  Objective-C?
[1463.66 --> 1464.34]  Probably not,
[1464.42 --> 1464.96]  because the
[1464.96 --> 1465.60]  less lines you
[1465.60 --> 1466.94]  write, the
[1466.94 --> 1467.56]  less bugs you
[1467.56 --> 1469.06]  introduce, the
[1469.06 --> 1469.86]  code is more
[1469.86 --> 1470.88]  maintainable, it's
[1470.88 --> 1471.70]  easier to write,
[1471.84 --> 1472.48]  easier to read,
[1472.62 --> 1472.98]  easier to
[1472.98 --> 1473.36]  maintain.
[1474.12 --> 1475.18]  So that will
[1475.18 --> 1475.78]  probably be the
[1475.78 --> 1476.48]  killer feature of
[1476.48 --> 1476.90]  Ruby Motion.
[1477.46 --> 1478.12]  Right now,
[1478.20 --> 1478.78]  Ruby Motion is
[1478.78 --> 1479.54]  very young, but
[1479.54 --> 1480.64]  the community is
[1480.64 --> 1481.46]  growing so fast,
[1481.46 --> 1482.72]  and I think
[1482.72 --> 1483.14]  it's probably a
[1483.14 --> 1483.52]  matter of
[1483.52 --> 1484.30]  months until
[1484.30 --> 1485.16]  we see mature
[1485.16 --> 1485.78]  libraries.
[1487.64 --> 1487.78]  Yeah.
[1488.44 --> 1488.94]  You know, I
[1488.94 --> 1489.40]  try to get out
[1489.40 --> 1489.82]  of the echo
[1489.82 --> 1490.52]  chamber of the
[1490.52 --> 1491.14]  Ruby community
[1491.14 --> 1491.68]  in which I
[1491.68 --> 1493.16]  live, but the
[1493.16 --> 1493.76]  Ruby angle
[1493.76 --> 1494.54]  aside, it's
[1494.54 --> 1495.14]  kind of hard
[1495.14 --> 1497.62]  to downplay the
[1497.62 --> 1498.48]  importance of a
[1498.48 --> 1499.74]  command line,
[1500.12 --> 1501.24]  tool chain, and
[1501.24 --> 1501.62]  a REPL.
[1502.70 --> 1503.26]  Those are two
[1503.26 --> 1504.10]  things that Xcode
[1504.10 --> 1504.74]  just really doesn't
[1504.74 --> 1505.32]  have today.
[1505.58 --> 1506.10]  Oh yeah, and
[1506.10 --> 1507.20]  we have much
[1507.20 --> 1507.94]  more features in
[1507.94 --> 1509.44]  the pipeline for
[1509.44 --> 1510.70]  Ruby Motion and
[1510.70 --> 1511.04]  the REPL.
[1511.18 --> 1511.64]  So right now
[1511.64 --> 1512.24]  it's very
[1512.24 --> 1513.76]  simple, but in
[1513.76 --> 1514.16]  the next few
[1514.16 --> 1515.00]  weeks we'll
[1515.00 --> 1515.96]  start introducing
[1515.96 --> 1516.62]  new features,
[1516.92 --> 1518.08]  and I think it's
[1518.08 --> 1518.56]  probably going to
[1518.56 --> 1519.06]  excite more
[1519.06 --> 1519.36]  people.
[1520.26 --> 1520.64]  So let's check
[1520.64 --> 1521.80]  Twitter for some
[1521.80 --> 1522.34]  questions.
[1523.52 --> 1524.00]  Sam, what do
[1524.00 --> 1524.36]  we got?
[1525.62 --> 1527.78]  So Ryan
[1527.78 --> 1529.90]  Farnall, I'm
[1529.90 --> 1530.40]  probably saying
[1530.40 --> 1530.80]  his name wrong,
[1531.66 --> 1533.12]  he asks, any
[1533.12 --> 1533.64]  chance a good
[1533.64 --> 1534.16]  debugger is
[1534.16 --> 1534.74]  coming to
[1534.74 --> 1535.64]  complement the
[1535.64 --> 1536.02]  REPL for
[1536.02 --> 1536.34]  debugging?
[1536.98 --> 1537.46]  And definitely
[1537.46 --> 1537.84]  coming from
[1537.84 --> 1538.32]  Objective-C,
[1538.44 --> 1538.68]  this is
[1538.68 --> 1539.32]  something that
[1539.32 --> 1540.90]  I'm just
[1540.90 --> 1541.22]  used to
[1541.22 --> 1541.70]  thinking in
[1541.70 --> 1542.58]  breakpoints and
[1542.58 --> 1542.84]  such.
[1543.86 --> 1544.42]  So yeah, this
[1544.42 --> 1545.12]  is pretty
[1545.12 --> 1545.44]  interesting.
[1546.04 --> 1546.52]  Yeah, so
[1546.52 --> 1547.46]  yeah, the
[1547.46 --> 1547.86]  debugger is
[1547.86 --> 1548.16]  definitely
[1548.16 --> 1548.50]  coming.
[1549.42 --> 1549.80]  So it
[1549.80 --> 1550.10]  will be
[1550.10 --> 1550.80]  first integrated
[1550.80 --> 1551.16]  into the
[1551.16 --> 1552.76]  simulator, and
[1552.76 --> 1553.46]  then we will
[1553.46 --> 1554.00]  try to
[1554.00 --> 1554.58]  integrate it
[1554.58 --> 1555.64]  on the
[1555.64 --> 1556.06]  device.
[1556.34 --> 1556.94]  So it
[1556.94 --> 1557.40]  will first
[1557.40 --> 1557.94]  come for
[1557.94 --> 1558.76]  the simulator.
[1559.64 --> 1559.80]  Are you
[1559.80 --> 1560.12]  thinking it
[1560.12 --> 1560.34]  will work
[1560.34 --> 1560.82]  similar to
[1560.82 --> 1561.78]  the Rails
[1561.78 --> 1562.20]  debugger?
[1562.36 --> 1562.80]  Just adding
[1562.80 --> 1563.58]  the debugger
[1563.58 --> 1563.90]  call?
[1564.68 --> 1565.20]  Or if you
[1565.20 --> 1565.76]  can say?
[1565.76 --> 1566.72]  No, it
[1566.72 --> 1566.94]  will be
[1566.94 --> 1567.40]  more like
[1567.40 --> 1567.84]  GDB.
[1568.20 --> 1568.64]  So you
[1568.64 --> 1569.26]  start the
[1569.26 --> 1569.68]  repo, then
[1569.68 --> 1569.92]  you can
[1569.92 --> 1570.46]  break on,
[1571.04 --> 1571.34]  there will
[1571.34 --> 1571.60]  be a
[1571.60 --> 1572.30]  break method
[1572.30 --> 1572.90]  on kernel
[1572.90 --> 1573.80]  that lets
[1573.80 --> 1574.20]  you break
[1574.20 --> 1574.42]  on a
[1574.42 --> 1574.74]  specific
[1574.74 --> 1575.42]  method or
[1575.42 --> 1576.14]  a file
[1576.14 --> 1576.42]  line.
[1577.40 --> 1577.60]  So it
[1577.60 --> 1579.02]  will definitely
[1579.02 --> 1580.14]  feel like
[1580.14 --> 1580.68]  GDB or
[1580.68 --> 1582.02]  LLDB or
[1582.02 --> 1583.56]  any debugger
[1583.56 --> 1584.02]  that you
[1584.02 --> 1584.66]  get used
[1584.66 --> 1585.34]  to.
[1585.90 --> 1586.56]  So would
[1586.56 --> 1586.82]  you be able
[1586.82 --> 1587.34]  to debug
[1587.34 --> 1587.80]  on the
[1587.80 --> 1588.16]  device?
[1589.00 --> 1589.68]  Not the
[1589.68 --> 1590.44]  first iteration
[1590.44 --> 1591.14]  of the
[1591.14 --> 1591.56]  debugger.
[1592.46 --> 1592.90]  But we
[1592.90 --> 1594.26]  will
[1594.26 --> 1596.42]  make sure
[1596.42 --> 1596.74]  that the
[1596.74 --> 1597.76]  repo works
[1597.76 --> 1598.04]  on the
[1598.04 --> 1598.70]  device also
[1598.70 --> 1599.02]  in the
[1599.02 --> 1599.30]  future.
[1600.10 --> 1600.44]  Very cool.
[1601.12 --> 1601.32]  Andrew
[1601.32 --> 1601.92]  Nesbitt wants
[1601.92 --> 1602.32]  to know,
[1602.56 --> 1603.18]  will improvements
[1603.18 --> 1603.62]  in Ruby
[1603.62 --> 1604.22]  Motion like
[1604.22 --> 1604.52]  the repo
[1604.52 --> 1605.42]  be backported
[1605.42 --> 1605.92]  to Mac
[1605.92 --> 1606.22]  Ruby?
[1608.68 --> 1609.16]  So,
[1609.56 --> 1609.90]  well,
[1610.10 --> 1611.34]  there is
[1611.34 --> 1611.72]  already a
[1611.72 --> 1612.18]  repo in
[1612.18 --> 1612.42]  Mac
[1612.42 --> 1612.62]  Ruby.
[1612.82 --> 1613.20]  It's called
[1613.20 --> 1613.86]  Mac IRB.
[1614.84 --> 1615.42]  And you
[1615.42 --> 1615.78]  can type
[1615.78 --> 1616.20]  expressions
[1616.20 --> 1616.52]  there.
[1617.52 --> 1617.90]  There is
[1617.90 --> 1618.42]  no way
[1618.42 --> 1618.94]  yet to,
[1619.20 --> 1619.36]  well,
[1619.54 --> 1619.88]  you don't
[1619.88 --> 1620.18]  have the
[1620.18 --> 1620.76]  view selector
[1620.76 --> 1621.12]  thing.
[1621.12 --> 1623.62]  I mean,
[1623.82 --> 1625.14]  to select
[1625.14 --> 1625.40]  a view
[1625.40 --> 1626.04]  using your
[1626.04 --> 1626.40]  mouse.
[1626.56 --> 1626.86]  It doesn't
[1626.86 --> 1627.52]  work in
[1627.52 --> 1628.06]  Mac IRB,
[1628.20 --> 1629.58]  but besides
[1629.58 --> 1630.00]  that,
[1630.18 --> 1631.12]  everything else
[1631.12 --> 1631.38]  is there.
[1631.56 --> 1631.96]  So there
[1631.96 --> 1632.28]  is no
[1632.28 --> 1632.62]  really,
[1633.36 --> 1633.72]  I'm not
[1633.72 --> 1634.20]  sure if
[1634.20 --> 1635.32]  you would
[1635.32 --> 1636.18]  really be
[1636.18 --> 1636.92]  needing that.
[1637.60 --> 1637.96]  Especially
[1637.96 --> 1638.90]  since in
[1638.90 --> 1639.54]  MacRuby,
[1639.72 --> 1640.46]  you use
[1640.46 --> 1641.10]  Xcode for
[1641.10 --> 1641.58]  everything.
[1643.16 --> 1643.44]  MacRuby
[1643.44 --> 1643.90]  doesn't have
[1643.90 --> 1644.48]  the command
[1644.48 --> 1645.22]  line interface
[1645.22 --> 1645.76]  that Ruby
[1645.76 --> 1646.34]  Motion has.
[1646.60 --> 1647.30]  So to
[1647.30 --> 1647.64]  create a
[1647.64 --> 1647.94]  MacRuby
[1647.94 --> 1648.28]  project,
[1648.56 --> 1649.18]  you use
[1649.18 --> 1649.76]  Xcode and
[1649.76 --> 1650.06]  you use
[1650.06 --> 1650.96]  IB to
[1650.96 --> 1653.54]  do your
[1653.54 --> 1654.32]  user interface.
[1654.52 --> 1654.68]  So you
[1654.68 --> 1655.08]  probably don't
[1655.08 --> 1656.50]  need the
[1656.50 --> 1657.00]  REPL that
[1657.00 --> 1657.34]  much.
[1657.50 --> 1657.94]  But you
[1657.94 --> 1658.92]  also have
[1658.92 --> 1659.98]  Mac IRB.
[1660.82 --> 1661.74]  And if
[1661.74 --> 1662.20]  you look at
[1662.20 --> 1662.50]  GitHub,
[1662.70 --> 1663.02]  you will see
[1663.02 --> 1663.28]  that there
[1663.28 --> 1663.84]  are various
[1663.84 --> 1666.32]  REPL for
[1666.32 --> 1666.86]  MacRuby.
[1667.06 --> 1667.72]  Some of
[1667.72 --> 1668.04]  them are
[1668.04 --> 1668.56]  actually Coco
[1668.56 --> 1668.88]  apps,
[1669.96 --> 1670.58]  which is
[1670.58 --> 1671.22]  good since
[1671.22 --> 1673.24]  it's actually
[1673.24 --> 1673.84]  using the
[1673.84 --> 1674.34]  run loop
[1674.34 --> 1674.84]  of Coco
[1674.84 --> 1675.88]  so that you
[1675.88 --> 1676.20]  can actually
[1676.20 --> 1676.92]  connect the
[1676.92 --> 1677.74]  REPL to
[1677.74 --> 1678.70]  your MacRuby
[1678.70 --> 1679.02]  app and
[1679.02 --> 1679.64]  type expressions
[1679.64 --> 1679.98]  there.
[1679.98 --> 1680.76]  And you
[1680.76 --> 1682.66]  don't
[1682.66 --> 1682.88]  actually
[1682.88 --> 1684.08]  block the
[1684.08 --> 1684.56]  main thread
[1684.56 --> 1687.02]  of the
[1687.02 --> 1687.48]  REPL when
[1687.48 --> 1687.78]  you type
[1687.78 --> 1688.14]  expressions.
[1688.44 --> 1689.10]  But besides
[1689.10 --> 1689.48]  that, I
[1689.48 --> 1689.78]  don't think
[1689.78 --> 1690.36]  that the
[1690.36 --> 1690.76]  REPL should
[1690.76 --> 1691.26]  be ported.
[1692.26 --> 1692.60]  Can you
[1692.60 --> 1693.44]  talk a little
[1693.44 --> 1693.92]  bit about
[1693.92 --> 1695.70]  how your
[1695.70 --> 1696.52]  version of
[1696.52 --> 1697.08]  memory management
[1697.08 --> 1697.56]  is different
[1697.56 --> 1699.06]  from the
[1699.06 --> 1700.20]  Objective-C
[1700.20 --> 1700.54]  ones we're
[1700.54 --> 1701.06]  used to
[1701.06 --> 1702.16]  versus
[1702.16 --> 1702.72]  retainer?
[1702.84 --> 1703.34]  Obviously, it's
[1703.34 --> 1703.90]  very different
[1703.90 --> 1704.58]  from manual
[1704.58 --> 1705.10]  memory management,
[1705.30 --> 1705.74]  but how it
[1705.74 --> 1706.16]  differs from
[1706.16 --> 1707.46]  ARC or the
[1707.46 --> 1707.88]  Coco garbage
[1707.88 --> 1708.34]  collection on
[1708.34 --> 1708.62]  the Mac?
[1709.20 --> 1709.76]  Yeah, so
[1709.76 --> 1710.36]  the memory
[1710.36 --> 1710.80]  medal of
[1710.80 --> 1711.36]  RubyMotion is
[1711.36 --> 1711.96]  very simple.
[1712.64 --> 1714.40]  So it's
[1714.40 --> 1714.98]  almost the
[1714.98 --> 1715.38]  same as
[1715.38 --> 1717.08]  ARC, except
[1717.08 --> 1718.12]  that it's
[1718.12 --> 1718.44]  done at
[1718.44 --> 1718.70]  runtime.
[1719.50 --> 1719.84]  So the
[1719.84 --> 1720.06]  runtime
[1720.06 --> 1720.76]  automatically
[1720.76 --> 1721.28]  inserts
[1721.28 --> 1721.86]  return and
[1721.86 --> 1722.30]  release and
[1722.30 --> 1722.94]  auto-release
[1722.94 --> 1723.86]  calls for
[1723.86 --> 1725.54]  you when
[1725.54 --> 1725.96]  your application
[1725.96 --> 1726.40]  starts.
[1726.68 --> 1727.70]  So that's
[1727.70 --> 1729.42]  exactly how
[1729.42 --> 1731.20]  RubyMotion
[1731.20 --> 1731.62]  works.
[1732.26 --> 1732.58]  And right
[1732.58 --> 1733.44]  now it's
[1733.44 --> 1733.78]  extremely
[1733.78 --> 1734.54]  simple, but
[1734.54 --> 1735.56]  I'm working
[1735.56 --> 1735.94]  on a new
[1735.94 --> 1737.26]  version, which
[1737.26 --> 1737.70]  will ship
[1737.70 --> 1738.06]  in a few
[1738.06 --> 1738.60]  months, that
[1738.60 --> 1739.08]  will be more
[1739.08 --> 1740.82]  deterministic, and
[1740.82 --> 1741.58]  that will also
[1741.58 --> 1742.24]  be able to
[1742.24 --> 1743.10]  detect cycles.
[1744.62 --> 1745.02]  So when, for
[1745.02 --> 1745.44]  instance, you
[1745.44 --> 1746.18]  have an object
[1746.18 --> 1746.56]  that has
[1746.56 --> 1747.10]  reference to
[1747.10 --> 1748.92]  another one, and
[1748.92 --> 1750.16]  right now both
[1750.16 --> 1750.82]  objects are going
[1750.82 --> 1751.70]  to leak because
[1751.70 --> 1754.66]  they use the
[1754.66 --> 1755.44]  reference kind of
[1755.44 --> 1756.18]  one, both of
[1756.18 --> 1757.72]  them, so both
[1757.72 --> 1758.24]  objects will
[1758.24 --> 1758.40]  leak.
[1758.48 --> 1759.16]  But in the
[1759.16 --> 1759.86]  near future, my
[1759.86 --> 1760.40]  goal is to
[1760.40 --> 1761.04]  introduce a
[1761.04 --> 1761.96]  system that
[1761.96 --> 1763.38]  lets you
[1763.38 --> 1765.12]  have cycles,
[1765.12 --> 1766.10]  and that
[1766.10 --> 1767.18]  doesn't force
[1767.18 --> 1768.36]  you to
[1768.36 --> 1768.94]  think about
[1768.94 --> 1769.16]  them.
[1769.72 --> 1770.44]  So I don't
[1770.44 --> 1770.92]  want to
[1770.92 --> 1771.64]  introduce weak
[1771.64 --> 1772.52]  references in
[1772.52 --> 1773.10]  RubyMotion,
[1773.78 --> 1774.20]  because I
[1774.20 --> 1775.40]  think that it
[1775.40 --> 1777.98]  actually breaks
[1777.98 --> 1778.66]  the whole idea
[1778.66 --> 1779.58]  of automatic
[1779.58 --> 1780.34]  memory management
[1780.34 --> 1780.74]  system.
[1781.28 --> 1781.72]  You shouldn't
[1781.72 --> 1782.14]  need to think
[1782.14 --> 1783.02]  about weak
[1783.02 --> 1783.54]  references.
[1783.90 --> 1784.14]  You should
[1784.14 --> 1785.04]  just use
[1785.04 --> 1786.76]  Ruby and
[1786.76 --> 1787.06]  don't think
[1787.06 --> 1787.46]  about that.
[1787.58 --> 1788.22]  So I really
[1788.22 --> 1789.64]  want the
[1789.64 --> 1790.20]  memory system
[1790.20 --> 1790.96]  to be able to
[1790.96 --> 1791.74]  deal with
[1791.74 --> 1792.58]  cycles and
[1792.58 --> 1793.22]  automatically
[1793.22 --> 1794.92]  clear objects
[1794.92 --> 1795.98]  that have
[1795.98 --> 1798.32]  cycle references.
[1798.60 --> 1798.96]  Especially if
[1798.96 --> 1800.60]  you could have
[1800.60 --> 1801.16]  like if you
[1801.16 --> 1802.48]  call a block
[1802.48 --> 1803.16]  on an object
[1803.16 --> 1803.90]  and then
[1803.90 --> 1804.46]  reference that
[1804.46 --> 1804.92]  object in the
[1804.92 --> 1806.00]  block, breaking
[1806.00 --> 1806.64]  those would
[1806.64 --> 1807.42]  solve like,
[1807.96 --> 1808.52]  save a ton of
[1808.52 --> 1809.08]  typing, at least
[1809.08 --> 1809.74]  in Objective-C
[1809.74 --> 1810.18]  land, so
[1810.18 --> 1811.06]  that would be
[1811.06 --> 1811.82]  fantastic in
[1811.82 --> 1812.24]  Ruby as
[1812.24 --> 1812.42]  well.
[1813.54 --> 1813.98]  Yeah.
[1814.36 --> 1814.60]  Yeah, yeah.
[1816.24 --> 1816.84]  That was a
[1816.84 --> 1817.26]  great question
[1817.26 --> 1818.20]  by Owen, I
[1818.20 --> 1819.26]  guess, O,
[1819.60 --> 1820.56]  from the
[1820.56 --> 1820.78]  Twitter.
[1821.44 --> 1821.88]  Up next,
[1822.06 --> 1822.74]  Anil wants
[1822.74 --> 1823.18]  to know,
[1823.34 --> 1824.08]  personally,
[1824.08 --> 1824.60]  Laurent, what
[1824.60 --> 1825.18]  tools do
[1825.18 --> 1825.82]  you use
[1825.82 --> 1826.98]  when you
[1826.98 --> 1827.34]  develop?
[1827.86 --> 1829.82]  Oh, so I
[1829.82 --> 1832.06]  use GDB and
[1832.06 --> 1832.38]  VI.
[1833.58 --> 1834.06]  So I
[1834.06 --> 1835.18]  actually, I'm
[1835.18 --> 1835.98]  a weird person,
[1836.12 --> 1836.88]  but I actually
[1836.88 --> 1837.72]  live in GDB.
[1838.74 --> 1839.72]  So GDB is
[1839.72 --> 1840.68]  my terminal,
[1841.64 --> 1842.08]  and I type
[1842.08 --> 1842.76]  expressions there.
[1842.86 --> 1843.62]  I use GDB as
[1843.62 --> 1844.62]  a repo for
[1844.62 --> 1847.12]  C, and I
[1847.12 --> 1847.90]  start programs
[1847.90 --> 1848.60]  in GDB, and
[1848.60 --> 1850.62]  I build
[1850.62 --> 1851.64]  everything using
[1851.64 --> 1851.94]  GDB.
[1852.74 --> 1854.42]  So I'm a
[1854.42 --> 1855.58]  weird person.
[1855.74 --> 1855.92]  I do
[1855.92 --> 1856.64]  everything inside
[1856.64 --> 1856.98]  the same
[1856.98 --> 1858.02]  terminal, and
[1858.02 --> 1858.46]  then I use
[1858.46 --> 1859.24]  MacVim for
[1859.24 --> 1860.36]  the code
[1860.36 --> 1860.64]  edition.
[1860.88 --> 1861.30]  I'm a big
[1861.30 --> 1861.62]  fan of
[1861.62 --> 1861.80]  Vim.
[1861.88 --> 1862.20]  I've been
[1862.20 --> 1863.02]  using VI
[1863.02 --> 1864.80]  for more
[1864.80 --> 1865.16]  than 10
[1865.16 --> 1865.68]  years, so
[1865.68 --> 1866.48]  my brain is
[1866.48 --> 1868.74]  completely, I
[1868.74 --> 1868.98]  don't know,
[1869.06 --> 1869.52]  fucked up.
[1870.00 --> 1870.54]  Sorry about
[1870.54 --> 1870.78]  that.
[1871.26 --> 1872.06]  So I can't
[1872.06 --> 1872.58]  use anything
[1872.58 --> 1872.96]  else than
[1872.96 --> 1873.24]  VI.
[1873.42 --> 1873.72]  Sorry.
[1873.96 --> 1874.50]  So it's
[1874.50 --> 1875.18]  all VI
[1875.18 --> 1876.22]  and GDB.
[1876.22 --> 1877.28]  Do you
[1877.28 --> 1877.50]  have any
[1877.50 --> 1878.22]  plans for
[1878.22 --> 1880.86]  support with
[1880.86 --> 1881.72]  instruments or
[1881.72 --> 1882.44]  building your
[1882.44 --> 1882.92]  own profiling
[1882.92 --> 1883.88]  tools for
[1883.88 --> 1884.44]  RubyMotion?
[1885.14 --> 1885.94]  Yeah, definitely.
[1886.36 --> 1887.16]  So we'll be
[1887.16 --> 1887.56]  coming with
[1887.56 --> 1888.24]  something soon.
[1889.80 --> 1890.70]  To be honest,
[1890.74 --> 1891.12]  I don't know
[1891.12 --> 1892.30]  yet what the
[1892.30 --> 1892.96]  plan will be,
[1893.46 --> 1893.96]  but we
[1893.96 --> 1894.64]  definitely need
[1894.64 --> 1895.82]  to have a
[1895.82 --> 1896.74]  profiling story
[1896.74 --> 1898.48]  around RubyMotion.
[1899.12 --> 1900.26]  I know that
[1900.26 --> 1900.94]  Forks have
[1900.94 --> 1901.66]  been able to
[1901.66 --> 1902.36]  use instruments
[1902.36 --> 1903.12]  to profile
[1903.12 --> 1903.94]  RubyMotion apps,
[1903.94 --> 1905.34]  and right
[1905.34 --> 1906.32]  now there
[1906.32 --> 1906.80]  is no way
[1906.80 --> 1907.30]  to see
[1907.30 --> 1911.64]  the Ruby
[1911.64 --> 1912.56]  traces when
[1912.56 --> 1914.42]  you hold
[1914.42 --> 1916.98]  the reference
[1916.98 --> 1917.24]  to an
[1917.24 --> 1917.74]  object and
[1917.74 --> 1918.40]  you see the
[1918.40 --> 1918.92]  backtrace of
[1918.92 --> 1919.38]  the allocation.
[1920.18 --> 1920.74]  I don't think
[1920.74 --> 1921.42]  it shows the
[1921.42 --> 1922.02]  Ruby trace
[1922.02 --> 1925.22]  yet, but I
[1925.22 --> 1925.58]  think there is
[1925.58 --> 1926.04]  a way to do
[1926.04 --> 1926.24]  that.
[1926.40 --> 1927.28]  So we'll
[1927.28 --> 1928.12]  try to support
[1928.12 --> 1928.86]  instruments because
[1928.86 --> 1929.30]  it's probably the
[1929.30 --> 1930.70]  best profiler
[1930.70 --> 1931.86]  that exists on
[1931.86 --> 1932.42]  the Mac yet.
[1932.94 --> 1933.26]  But at the
[1933.26 --> 1933.74]  same time,
[1933.74 --> 1934.12]  I would
[1934.12 --> 1934.64]  really want
[1934.64 --> 1935.10]  to have a
[1935.10 --> 1935.76]  profiler on
[1935.76 --> 1936.02]  the command
[1936.02 --> 1936.36]  line,
[1937.50 --> 1937.92]  something that
[1937.92 --> 1939.04]  you could just
[1939.04 --> 1939.56]  run your
[1939.56 --> 1940.38]  application using
[1940.38 --> 1941.50]  Rake, and
[1941.50 --> 1942.12]  then it would
[1942.12 --> 1943.32]  automatically do
[1943.32 --> 1944.82]  a memory
[1944.82 --> 1945.52]  profiling and
[1945.52 --> 1946.20]  CPU profiling
[1946.20 --> 1946.88]  for you, and
[1946.88 --> 1947.26]  then you would
[1947.26 --> 1948.72]  get some
[1948.72 --> 1949.88]  results back
[1949.88 --> 1950.24]  into the
[1950.24 --> 1950.50]  terminal.
[1951.26 --> 1951.60]  I would
[1951.60 --> 1952.04]  really want
[1952.04 --> 1952.60]  to have a
[1952.60 --> 1953.42]  terminal version
[1953.42 --> 1953.78]  also.
[1954.58 --> 1954.70]  It would be
[1954.70 --> 1955.02]  really neat
[1955.02 --> 1955.34]  if there was
[1955.34 --> 1955.98]  something like
[1955.98 --> 1958.30]  in Rails 3.2,
[1958.36 --> 1959.34]  they added the
[1959.34 --> 1959.80]  slow query
[1959.80 --> 1960.64]  profiler, so if
[1960.64 --> 1961.84]  anything takes
[1961.84 --> 1962.46]  a long time in
[1962.46 --> 1963.08]  development, it
[1963.08 --> 1964.52]  automatically logs
[1964.52 --> 1965.04]  and warns you
[1965.04 --> 1965.70]  that something's
[1965.70 --> 1967.58]  slow, that might
[1967.58 --> 1968.10]  be a neat
[1968.10 --> 1968.88]  addition.
[1976.60 --> 1977.38]  So, Laurent, I
[1977.38 --> 1977.70]  just want to
[1977.70 --> 1978.46]  applaud you on, I
[1978.46 --> 1979.04]  guess, the business
[1979.04 --> 1979.34]  model.
[1979.46 --> 1979.98]  I think we get
[1979.98 --> 1980.44]  spoiled in the
[1980.44 --> 1981.94]  open source world
[1981.94 --> 1983.22]  to expect everything
[1983.22 --> 1985.40]  just to be handed
[1985.40 --> 1987.20]  over, the source
[1987.20 --> 1987.66]  included.
[1987.66 --> 1989.76]  I appreciate the
[1989.76 --> 1990.30]  way that you've
[1990.30 --> 1991.24]  open sourced what
[1991.24 --> 1992.52]  you could, but I
[1992.52 --> 1993.12]  was one of the
[1993.12 --> 1994.24]  first customers on
[1994.24 --> 1995.94]  the first day, even
[1995.94 --> 1998.94]  before I knew how, I
[1998.94 --> 2000.94]  guess, how much
[2000.94 --> 2002.08]  utility I would get
[2002.08 --> 2002.90]  out of RubyMotion.
[2003.10 --> 2004.86]  I just, I've been a
[2004.86 --> 2005.80]  fan of the work you've
[2005.80 --> 2006.52]  done on MacRuby and
[2006.52 --> 2007.26]  just wanted to support
[2007.26 --> 2007.76]  that effort.
[2008.20 --> 2009.16]  How have you been,
[2009.56 --> 2011.30]  have you been
[2011.30 --> 2012.10]  received, I guess, in
[2012.10 --> 2012.94]  that business model in
[2012.94 --> 2013.68]  the community?
[2014.66 --> 2016.46]  Well, first, I
[2016.46 --> 2017.02]  would like to thank
[2017.02 --> 2017.82]  you for purchasing
[2017.82 --> 2018.36]  RubyMotion.
[2019.42 --> 2020.60]  It's really nice and
[2020.60 --> 2021.92]  it's really, it's
[2021.92 --> 2022.72]  greatly appreciated.
[2023.42 --> 2024.36]  But so far, the
[2024.36 --> 2025.16]  community is great.
[2025.96 --> 2028.02]  I was also a bit
[2028.02 --> 2028.76]  worried about that
[2028.76 --> 2030.48]  because I'm a free
[2030.48 --> 2031.36]  software activist.
[2032.72 --> 2035.22]  So, it's really
[2035.22 --> 2036.08]  tough for me to do
[2036.08 --> 2036.80]  a proprietary
[2036.80 --> 2037.74]  development right
[2037.74 --> 2037.96]  now.
[2039.54 --> 2040.62]  But so far, the
[2040.62 --> 2041.34]  community is actually
[2041.34 --> 2042.18]  accepting the project
[2042.18 --> 2042.76]  very well.
[2043.68 --> 2046.24]  And the thing is
[2046.24 --> 2047.12]  that I've been
[2047.12 --> 2047.72]  thinking about this
[2047.72 --> 2048.72]  a lot and I don't
[2048.72 --> 2049.48]  think other way
[2049.48 --> 2051.74]  than charging
[2051.74 --> 2052.94]  customers for using
[2052.94 --> 2053.44]  RubyMotion.
[2054.22 --> 2055.32]  I could do the
[2055.32 --> 2056.12]  project open source
[2056.12 --> 2056.80]  but I would need to
[2056.80 --> 2057.64]  find a company to
[2057.64 --> 2058.58]  sponsor the work.
[2059.54 --> 2060.28]  And the problem
[2060.28 --> 2061.14]  with that is that
[2061.14 --> 2063.62]  you always need to
[2063.62 --> 2064.54]  find a sponsor and
[2064.54 --> 2065.78]  sponsors tend to
[2065.78 --> 2067.02]  stop sponsoring you
[2067.02 --> 2067.88]  at some point.
[2068.76 --> 2069.92]  And it's really a
[2069.92 --> 2070.10]  problem.
[2070.24 --> 2071.30]  And I had the same
[2071.30 --> 2072.06]  experience in the
[2072.06 --> 2072.34]  past.
[2072.34 --> 2073.62]  And also, if you
[2073.62 --> 2074.32]  look at popular
[2074.32 --> 2075.22]  open source projects
[2075.22 --> 2076.24]  right now, the
[2076.24 --> 2077.10]  contributors are
[2077.10 --> 2077.72]  actually being
[2077.72 --> 2078.28]  sponsored by
[2078.28 --> 2078.78]  companies.
[2079.48 --> 2080.18]  And sometimes they
[2080.18 --> 2080.94]  stop sponsoring
[2080.94 --> 2081.36]  them and they
[2081.36 --> 2081.94]  need to find a
[2081.94 --> 2083.26]  new company.
[2083.50 --> 2084.72]  And they actually
[2084.72 --> 2086.32]  jam ships from one
[2086.32 --> 2086.94]  company to another
[2086.94 --> 2087.22]  one.
[2087.74 --> 2088.78]  And right now, the
[2088.78 --> 2090.92]  economy is actually
[2090.92 --> 2092.20]  very bad for other
[2092.20 --> 2092.96]  companies, I think.
[2092.96 --> 2104.44]  people can trust in
[2104.44 --> 2105.28]  writing their apps.
[2106.28 --> 2107.60]  And so I want to
[2107.60 --> 2108.30]  keep working on
[2108.30 --> 2109.06]  Macroby for at least
[2109.06 --> 2109.66]  five years and
[2109.66 --> 2110.30]  maintain it.
[2110.90 --> 2112.20]  And I don't see any
[2112.20 --> 2112.84]  other way than
[2112.84 --> 2114.88]  actually charging the
[2114.88 --> 2115.88]  users so that they
[2115.88 --> 2117.44]  can actually get
[2117.44 --> 2118.46]  maintenance and
[2118.46 --> 2119.28]  software updates and
[2119.28 --> 2119.68]  so forth.
[2120.48 --> 2123.50]  So I really want
[2123.50 --> 2124.30]  to open source as
[2124.30 --> 2124.88]  many things as
[2124.88 --> 2126.54]  possible because I'm
[2126.54 --> 2127.60]  a huge free software
[2127.60 --> 2128.06]  activist.
[2129.38 --> 2130.56]  But until I find
[2130.56 --> 2131.72]  another solution, I'm
[2131.72 --> 2132.82]  afraid that parts of
[2132.82 --> 2133.50]  William Motion will
[2133.50 --> 2135.76]  be proprietary, will
[2135.76 --> 2136.48]  be closed source.
[2136.48 --> 2138.06]  Now, in both of
[2138.06 --> 2138.90]  those models, both the
[2138.90 --> 2139.92]  corporate sponsorship
[2139.92 --> 2140.84]  model, I mean, you've
[2140.84 --> 2142.00]  got politics in play
[2142.00 --> 2143.18]  with the corporate
[2143.18 --> 2143.68]  interests.
[2143.96 --> 2145.24]  But in this model,
[2145.92 --> 2146.88]  you're kind of the,
[2147.24 --> 2148.00]  you know, you've got to
[2148.00 --> 2148.86]  do everything in the
[2148.86 --> 2149.48]  vertical.
[2149.72 --> 2151.02]  You've got to have a
[2151.02 --> 2152.24]  nice design website.
[2152.48 --> 2153.42]  You've got to sell the
[2153.42 --> 2153.74]  thing.
[2153.92 --> 2155.26]  How much support have
[2155.26 --> 2156.38]  you gotten on that
[2156.38 --> 2156.92]  aspect of it?
[2156.98 --> 2157.48]  And have you had to
[2157.48 --> 2158.22]  pay for all of those
[2158.22 --> 2159.60]  services up front?
[2161.10 --> 2161.50]  Yes.
[2161.62 --> 2164.50]  So, yeah, so you're
[2164.50 --> 2165.92]  exactly right that doing
[2165.92 --> 2166.70]  a startup is very
[2166.70 --> 2166.96]  tough.
[2167.88 --> 2168.92]  I'm actually doing
[2168.92 --> 2169.72]  three jobs at the
[2169.72 --> 2169.92]  moment.
[2170.20 --> 2170.86]  It's very funny.
[2171.46 --> 2172.82]  So I do marketing, I do
[2172.82 --> 2174.06]  support, and then I do
[2174.06 --> 2174.86]  engineering.
[2175.20 --> 2176.20]  I mean, working on
[2176.20 --> 2176.66]  William Motion.
[2177.32 --> 2179.34]  But I'm currently, I
[2179.34 --> 2180.92]  we generated enough
[2180.92 --> 2181.88]  revenue so that I can
[2181.88 --> 2182.74]  actually hire people.
[2183.40 --> 2185.66]  So I will have up very
[2185.66 --> 2187.80]  soon on the platform
[2187.80 --> 2188.80]  and on the support and
[2188.80 --> 2189.60]  the marketing side.
[2190.58 --> 2191.94]  And besides that, I'm
[2191.94 --> 2192.72]  actually doing okay.
[2192.84 --> 2194.22]  So it's not that much
[2194.22 --> 2195.90]  of work.
[2197.26 --> 2198.58]  So I think it's doing,
[2198.72 --> 2199.80]  I'm doing fine right
[2199.80 --> 2200.06]  now.
[2201.06 --> 2202.68]  What are your thoughts
[2202.68 --> 2206.02]  on bringing some of the
[2206.02 --> 2208.00]  build system and such to
[2208.00 --> 2211.00]  MacRuby on the Mac and
[2211.00 --> 2213.72]  kind of the other pieces of
[2213.72 --> 2214.82]  Ruby Motion that aren't
[2214.82 --> 2215.68]  iOS specific?
[2215.68 --> 2218.68]  So the first, the first
[2218.68 --> 2220.26]  thing I want to backport to
[2220.26 --> 2221.34]  MacRuby is the memory
[2221.34 --> 2221.70]  model.
[2223.00 --> 2224.56]  Because the, the object
[2224.56 --> 2225.66]  you see garbage collector
[2225.66 --> 2227.64]  that MacRuby is using is
[2227.64 --> 2229.26]  being deprecated in, in
[2229.26 --> 2229.78]  Mountain Lion.
[2230.46 --> 2231.34]  So it means that in
[2231.34 --> 2232.92]  Mountain Lion plus one,
[2233.50 --> 2234.38]  which will probably be
[2234.38 --> 2235.42]  released in two years,
[2236.00 --> 2237.86]  it will disappear from,
[2237.86 --> 2238.64]  from OS X.
[2238.98 --> 2242.06]  So we need to replace the
[2242.06 --> 2243.22]  memory model of MacRuby
[2243.22 --> 2243.96]  or something else.
[2244.52 --> 2246.24]  So I'm currently trying
[2246.24 --> 2248.40]  to find out if I can
[2248.40 --> 2249.82]  backport the Ruby
[2249.82 --> 2252.80]  Motion memory, memory
[2252.80 --> 2253.94]  model to MacRuby.
[2255.14 --> 2256.10]  So it's not that easy,
[2256.26 --> 2257.56]  it's not as easy because
[2257.56 --> 2259.74]  MacRuby is used more
[2259.74 --> 2260.70]  widely than Ruby
[2260.70 --> 2261.06]  Motion.
[2262.04 --> 2263.20]  MacRuby is not only
[2263.20 --> 2264.68]  about Cocoa apps.
[2265.24 --> 2266.68]  People use it outside
[2266.68 --> 2267.34]  Cocoa.
[2267.54 --> 2268.64]  So outside the run
[2268.64 --> 2269.52]  loop, the Cocoa run
[2269.52 --> 2269.76]  loop.
[2269.76 --> 2271.56]  So I really need to
[2271.56 --> 2272.44]  find a solution that
[2272.44 --> 2273.34]  works in all the
[2273.34 --> 2275.58]  scenarios where MacRuby
[2275.58 --> 2276.28]  is being used.
[2276.94 --> 2279.42]  So I'm, I'm, I'm still
[2279.42 --> 2281.22]  thinking about that with
[2281.22 --> 2282.28]  the rest of the MacRuby
[2282.28 --> 2283.26]  developer team.
[2283.66 --> 2285.28]  But this will probably be
[2285.28 --> 2287.78]  the first thing that we
[2287.78 --> 2289.00]  backport from Ruby
[2289.00 --> 2290.12]  Motion to MacRuby.
[2291.34 --> 2292.82]  The, the, the command
[2292.82 --> 2294.12]  line interface is pretty
[2294.12 --> 2296.24]  nice to have, but right
[2296.24 --> 2297.84]  now the, the priority is
[2297.84 --> 2299.82]  is actually replacing the
[2299.82 --> 2300.46]  garbage collector.
[2302.46 --> 2303.30]  That makes sense.
[2304.58 --> 2305.38]  Well, I have a couple
[2305.38 --> 2306.40]  feature requests.
[2306.50 --> 2308.08]  I'll just fire them off.
[2309.66 --> 2310.96]  It would be really
[2310.96 --> 2311.90]  fantastic if you could
[2311.90 --> 2314.44]  write static libraries or
[2314.44 --> 2317.14]  frameworks in Ruby
[2317.14 --> 2318.90]  Motion, especially like if
[2318.90 --> 2320.78]  I'm transitioning a large
[2320.78 --> 2321.66]  project to Ruby Motion,
[2321.76 --> 2322.52]  it'd be great if I could
[2322.52 --> 2325.56]  write pieces instead of
[2325.56 --> 2326.54]  just replacing all of the
[2326.54 --> 2327.44]  Objective-C all at once
[2327.44 --> 2328.30]  because that'd be a ton of
[2328.30 --> 2329.30]  work for a larger project.
[2331.60 --> 2333.76]  So I'm sure that's like
[2333.76 --> 2334.98]  lower on your priority list,
[2335.14 --> 2337.10]  but that would be really
[2337.10 --> 2337.40]  awesome.
[2337.84 --> 2339.10]  People have been asking if,
[2339.22 --> 2341.18]  if we can add support,
[2341.92 --> 2343.90]  support for Ruby Motion
[2343.90 --> 2345.24]  Code inside existing
[2345.24 --> 2346.08]  Xcode Objective-C
[2346.08 --> 2346.42]  project.
[2346.96 --> 2348.20]  And I think that's, that's
[2348.20 --> 2349.00]  probably what you want,
[2349.06 --> 2349.28]  right?
[2350.08 --> 2350.52]  Right, right.
[2350.52 --> 2352.40]  And yeah, so we, we
[2352.40 --> 2354.08]  probably do something in
[2354.08 --> 2356.16]  this area, but it's pretty,
[2356.24 --> 2357.26]  it's not very, it's not
[2357.26 --> 2358.08]  high on the to-do list
[2358.08 --> 2360.08]  right now because we, we
[2360.08 --> 2361.68]  want to focus on using
[2361.68 --> 2364.00]  Ruby Motion for, to do,
[2364.06 --> 2364.74]  to do everything.
[2364.96 --> 2366.10]  I mean, using Ruby Motion
[2366.10 --> 2367.32]  to start an application.
[2368.32 --> 2369.90]  But we will, we will
[2369.90 --> 2372.30]  probably find a way to, to,
[2372.40 --> 2373.16]  so that you can use Ruby
[2373.16 --> 2374.32]  Motion inside existing
[2374.32 --> 2375.02]  projects.
[2375.02 --> 2378.26]  Can you chat about, um,
[2379.02 --> 2379.74]  testing for a minute?
[2380.00 --> 2380.84]  That was one of the things
[2380.84 --> 2382.52]  that made me, um, really
[2382.52 --> 2383.42]  excited about Ruby Motion
[2383.42 --> 2384.32]  because as Objective-C
[2384.32 --> 2386.42]  developers, people rarely
[2386.42 --> 2388.06]  test, or if anything, it's
[2388.06 --> 2389.38]  just unit tests and never
[2389.38 --> 2390.74]  anything beyond that.
[2391.28 --> 2392.42]  Can you talk about the, the
[2392.42 --> 2393.30]  testing support in Ruby
[2393.30 --> 2393.54]  Motion?
[2395.68 --> 2397.54]  So the testing support is
[2397.54 --> 2399.58]  actually very, uh, naive
[2399.58 --> 2400.24]  right now.
[2400.86 --> 2403.16]  So we, Ruby Motion comes
[2403.16 --> 2405.00]  with a bacon, which is
[2405.02 --> 2406.54]  I think, a RSpec clone.
[2406.88 --> 2408.04]  So I'm not familiar with
[2408.04 --> 2408.40]  testing.
[2409.08 --> 2410.26]  So I'm afraid I'm, I'm not
[2410.26 --> 2412.04]  a big user of testing in
[2412.04 --> 2414.54]  Ruby, but, uh, bacon is a,
[2414.54 --> 2416.14]  is a clone of RSpec, but
[2416.14 --> 2417.02]  it's, it's a simplistic
[2417.02 --> 2418.92]  clone of RSpec, so the
[2418.92 --> 2420.24]  code base, uh, is only one
[2420.24 --> 2422.24]  file and Ruby Motion
[2422.24 --> 2423.56]  ships with, uh, bacon.
[2424.94 --> 2426.52]  And by default, when you
[2426.52 --> 2427.70]  create an application, you
[2427.70 --> 2428.70]  get a spec directory.
[2429.24 --> 2430.88]  And from there, you can
[2430.88 --> 2432.90]  write, uh, bacon specs.
[2432.90 --> 2435.34]  I think that by default,
[2435.42 --> 2436.48]  there is only one spec.
[2436.58 --> 2438.22]  It checks that there is a
[2438.22 --> 2440.02]  UI window inside your UI
[2440.02 --> 2440.50]  application.
[2441.38 --> 2442.82]  And I think, yeah, by
[2442.82 --> 2443.80]  default, if you type break
[2443.80 --> 2446.00]  spec, it runs a spec and you
[2446.00 --> 2447.60]  get an error because we
[2447.60 --> 2448.96]  don't create a UI window by
[2448.96 --> 2450.04]  default when you create a
[2450.04 --> 2450.54]  project.
[2450.54 --> 2453.02]  So that, that's the first
[2453.02 --> 2454.26]  spec that we have and it
[2454.26 --> 2454.96]  fails by default.
[2455.10 --> 2456.26]  So I think that it conforms
[2456.26 --> 2457.60]  to the test driven
[2457.60 --> 2458.04]  development.
[2459.14 --> 2460.26]  You need to create a window
[2460.26 --> 2461.28]  and then run the spec again
[2461.28 --> 2462.38]  and then it will pass.
[2463.42 --> 2465.04]  And then it's up to you and
[2465.04 --> 2466.28]  you can write any spec you
[2466.28 --> 2466.54]  want.
[2466.90 --> 2469.68]  And so far, um, I, I've, I've
[2469.68 --> 2470.98]  not seen a lot of, um,
[2470.98 --> 2472.12]  project that I've been using,
[2472.12 --> 2475.52]  uh, uh, the specs, um, yet.
[2476.10 --> 2477.80]  But, uh, one thing I saw is
[2477.80 --> 2479.80]  that some, uh, there is a,
[2479.80 --> 2481.02]  there is a game, a gem that
[2481.02 --> 2482.14]  you can install that will
[2482.14 --> 2484.12]  actually, uh, colorize the
[2484.12 --> 2485.36]  output, the output of
[2485.36 --> 2485.92]  rake spec.
[2486.28 --> 2487.48]  So you get, for instance,
[2487.58 --> 2489.18]  green stuff for the spec
[2489.18 --> 2491.52]  that pass and red stuff when
[2491.52 --> 2492.52]  there is a problem.
[2493.30 --> 2495.74]  And I suspect that, uh, in
[2495.74 --> 2497.42]  that, in that gem, there are
[2497.42 --> 2499.66]  samples of various Ruby
[2499.66 --> 2501.08]  motion apps that actually have
[2501.08 --> 2502.50]  more, more detailed specs.
[2504.00 --> 2505.28]  It'd be interesting to see,
[2505.38 --> 2507.08]  um, support for the
[2507.08 --> 2507.62]  instruments.
[2507.80 --> 2509.18]  Like UI automation stuff,
[2509.18 --> 2511.94]  um, in Ruby instead of
[2511.94 --> 2512.78]  JavaScript.
[2513.12 --> 2513.90]  Cause that's what, uh,
[2513.90 --> 2514.86]  instruments requires you to
[2514.86 --> 2515.06]  write.
[2515.76 --> 2517.26]  Um, surely that's a ton of
[2517.26 --> 2517.74]  work, but.
[2518.04 --> 2519.42]  Uh, actually we have, uh,
[2519.42 --> 2520.58]  someone is working on that
[2520.58 --> 2521.02]  right now.
[2521.70 --> 2523.64]  So, uh, he's working on
[2523.64 --> 2523.84]  that.
[2523.98 --> 2525.80]  And so he's having issues,
[2525.80 --> 2527.50]  uh, connecting to
[2527.50 --> 2528.00]  instruments.
[2528.00 --> 2529.40]  So I'm, I'm trying to help
[2529.40 --> 2531.26]  him, but I think there
[2531.26 --> 2532.00]  will be, there will be
[2532.00 --> 2532.86]  something, there will be
[2532.86 --> 2533.70]  some sort of announcement
[2533.70 --> 2535.96]  around that in probably the
[2535.96 --> 2536.56]  next few days.
[2536.56 --> 2538.34]  So for folks that might not
[2538.34 --> 2539.58]  be, uh, privy to this
[2539.58 --> 2541.12]  ecosystem, I guess it would
[2541.12 --> 2543.36]  be kind of a fit for say
[2543.36 --> 2545.70]  cucumber for Ruby motion to
[2545.70 --> 2546.44]  use a bad analogy.
[2547.38 --> 2548.44]  It's, it'd be similar to
[2548.44 --> 2549.48]  like capy bear or something
[2549.48 --> 2551.02]  because it simulates, um,
[2551.44 --> 2553.18]  touches and like entering
[2553.18 --> 2554.62]  text in text fields and such.
[2554.62 --> 2557.42]  Um, and then you can see the
[2557.42 --> 2559.36]  result or like query the UI and
[2559.36 --> 2560.84]  see the state of things.
[2561.28 --> 2561.68]  So.
[2563.30 --> 2563.66]  Yeah.
[2564.48 --> 2565.64]  A lot of exciting stuff
[2565.64 --> 2566.52]  happening with Ruby motion.
[2566.64 --> 2567.34]  I want to thank you for your
[2567.34 --> 2568.04]  time, Laurent.
[2568.40 --> 2570.10]  And, uh, we look forward to
[2570.10 --> 2571.36]  those announcements that are
[2571.36 --> 2571.76]  forthcoming.
[2572.24 --> 2573.52]  Well, thank you very much for
[2573.52 --> 2574.44]  having invited me.
[2574.44 --> 2576.76]  Thank you.
[2577.40 --> 2578.40]  Bye.
[2579.12 --> 2579.20]  Bye.
[2579.20 --> 2579.50]  Bye.
[2579.50 --> 2579.90]  Bye.
[2580.38 --> 2580.40]  Bye.
[2580.40 --> 2581.16]  Bye.
[2582.46 --> 2583.58]  Bye.
[2583.72 --> 2584.24]  Bye.
[2584.78 --> 2585.76]  Bye.
[2585.86 --> 2586.26]  Bye.
[2586.28 --> 2586.74]  Bye.
[2587.04 --> 2587.16]  Bye.
[2587.16 --> 2587.50]  Bye.
[2587.68 --> 2587.74]  Bye.
[2587.92 --> 2588.06]  Bye.
[2588.26 --> 2588.78]  Bye.
[2589.00 --> 2589.80]  Bye.
[2589.86 --> 2590.90]  Bye.
[2590.90 --> 2591.40]  Bye.
[2591.94 --> 2592.08]  Bye.
[2592.18 --> 2593.08]  Bye.
[2593.10 --> 2593.94]  Bye.
[2594.08 --> 2594.16]  Bye.
[2594.40 --> 2595.02]  Bye.
[2595.22 --> 2596.16]  Bye.
[2596.58 --> 2597.26]  Bye.
[2598.06 --> 2598.58]  Bye.
[2598.60 --> 2599.62]  Bye.
[2599.62 --> 2600.48]  Bye.
[2600.68 --> 2601.28]  Bye.
[2601.28 --> 2601.56]  Bye.
[2601.66 --> 2602.04]  Bye.
[2602.04 --> 2602.08]  Bye.
[2602.08 --> 2602.40]  Bye.
[2602.42 --> 2602.78]  Bye.
[2602.86 --> 2603.12]  Bye.
[2603.14 --> 2603.60]  Bye.
