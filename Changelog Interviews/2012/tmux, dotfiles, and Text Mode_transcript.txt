[0.08 --> 8.56]  The Change Log was brought to you by Pusher, a hosted API that lets you quickly, easily, and securely add scalable real-time functionality to web and mobile apps.
[9.10 --> 18.50]  Check out Pusher's real-time showcase at pusher.com slash showcase to learn how Gauges, CloudApp, Buffer, and many others are using the awesomeness that is Pusher.
[19.12 --> 24.06]  Join the real-time web and get your free API account at pusher.com.
[30.00 --> 43.64]  Welcome to The Change Log, episode 0.7.3.
[44.14 --> 45.18]  I'm Adam Stachowiak.
[45.38 --> 46.26]  And I'm one another one.
[46.44 --> 47.34]  This is The Change Log.
[47.40 --> 49.08]  We cover what's fresh and new and open source.
[49.08 --> 51.76]  If you found us on iTunes, we're also on the web at thechangelog.com.
[52.02 --> 52.80]  We're also up on GitHub.
[53.22 --> 54.80]  Head to github.com slash explore.
[54.88 --> 59.00]  You'll find some trending repos, some feature repos from our blog, as well as the audio podcast.
[59.00 --> 62.08]  And if you're on the Twitter, don't follow Change Log Show anymore.
[62.20 --> 63.82]  Please follow The Change Log.
[63.94 --> 65.00]  And I am Adam Stach.
[65.18 --> 65.78]  And I'm Penguin.
[65.92 --> 67.48]  P-E-N-G-W-Y-N-N.
[68.12 --> 75.40]  One episode this week talked to Brian Hogan and Joshua Clayton about T-MUX and other text mode goodies.
[76.06 --> 78.68]  CLI goodness for the homies that love it.
[79.04 --> 82.08]  Yeah, I'm not sure how valuable this would be for the listeners, but I enjoyed it.
[82.08 --> 87.98]  Just to chat about some ideas on how to pimp out your T-MUX and your text mode apps.
[87.98 --> 90.28]  And I'm using this more and more in my workflow.
[90.66 --> 94.40]  Well, I know the entire team at Pure Charity has been a convert to T-MUX in your workflow.
[94.58 --> 98.76]  So I'm sure that you're ahead of the curve on this and teaching everybody how to use it right.
[99.14 --> 102.38]  Well, you know, I'm just an enthusiast like so many folks.
[102.48 --> 105.64]  But, you know, we're doing pair programming so much since we're a distributed team.
[105.84 --> 114.34]  And T-MUX, it makes it easy just to share those terminals across the wire and stitch together five or six windows into one terminal session.
[114.34 --> 117.04]  And just pair programming like that.
[117.46 --> 120.44]  So not only T-MUX, but you also talked about Vim and some other CLI stuff.
[120.54 --> 120.92]  What else?
[121.12 --> 126.46]  Vim setup, so my Zshell, .files in general, what the best .file repos are out there.
[126.48 --> 131.92]  And some resources to peek at other folks' settings and, you know, kind of roll your own.
[132.46 --> 133.14]  Cool, cool.
[133.28 --> 135.78]  And we also want to thank our sponsor, Pusher.
[135.86 --> 136.56]  They're awesome.
[136.66 --> 137.10]  They're good.
[137.36 --> 139.26]  And, Wynn, I know you use them at Pure Charity.
[139.26 --> 142.50]  Again, we mentioned Pure Charity again, but the real-time web is here.
[143.04 --> 144.56]  We, Goose, use them at Pure Charity.
[144.74 --> 154.64]  Yeah, you know, it's some of our real-time views are things that we build for conferences and interfaces especially that we want to show real-time feedback.
[154.64 --> 156.48]  We're using Pusher, and it's been a great fit.
[156.80 --> 163.06]  And thanks again to the guys at Pusher for building not only a great tool for backing this podcast.
[163.26 --> 164.56]  We certainly appreciate it.
[164.88 --> 165.54]  Yeah, absolutely.
[166.26 --> 167.08]  Well, that's a fun episode.
[167.14 --> 167.72]  Do you want to get to it?
[167.92 --> 168.50]  Let's do it.
[169.26 --> 185.12]  All right, we're chatting today with a couple of Tmux users, Josh Clayton, developer over at ThoughtBot, and Brian Hogan, author, speaker, trainer.
[185.12 --> 187.88]  So, Josh, why don't you introduce yourself for the folks that might not know you?
[188.36 --> 189.60]  All right, my name is Josh Clayton.
[189.90 --> 191.98]  I've been at ThoughtBot for about two and a half years.
[192.80 --> 198.62]  I currently work on Factory Girl, which is a replacement for fixtures in Rails.
[198.62 --> 204.88]  And I'm also a maintainer of Blueprint CSS, which a lot of people are pretty familiar with.
[205.58 --> 207.06]  A lot of Blueprint users.
[207.56 --> 208.20]  Who about you, Brian?
[209.32 --> 210.24]  I'm Brian Hogan.
[210.46 --> 214.16]  I'm an author of a couple of web development books for Pragmatic Bookshelf.
[214.16 --> 218.56]  And I'm an editor there at the Pragmatic Bookshelf.
[218.76 --> 222.44]  And I also do quite a bit of coding and training with Ruby on Rails.
[223.48 --> 223.86]  Awesome.
[224.46 --> 226.24]  So I'm a Tmux noob.
[226.34 --> 228.60]  I've been using it probably not quite a year.
[228.98 --> 230.96]  So how did you guys discover Tmux?
[231.86 --> 232.44]  Go ahead, Josh.
[232.44 --> 235.36]  So, let's see.
[235.40 --> 240.76]  I was using MacVim pretty heavily, about two to, yeah, about two, two and a half years at that point.
[242.24 --> 250.18]  And there wasn't, I wasn't really focused on using a screen or anything like that.
[250.38 --> 252.92]  I, you know, been developing purely in MacVim.
[252.92 --> 256.00]  And then I had switched over to iTerm to run my tests.
[256.30 --> 258.04]  And a lot of it was Command Tab.
[258.14 --> 258.66]  I'm on a Mac.
[258.84 --> 263.30]  So I was just swapping between these two screen, between the two applications.
[263.74 --> 264.84]  And it got really frustrating.
[265.00 --> 269.08]  And I had heard about Screen and played around with it a little bit.
[269.18 --> 274.62]  I didn't particularly care for it because I was so accustomed to using the different splits within Vim.
[274.62 --> 283.22]  And I felt like if I'm going to use a terminal multiplexer, I wanted to use something that would support a different split.
[283.36 --> 293.40]  So I could have Tmux in maybe the upper 75% of my window and then a shell where I could run tests or run a Rails server within the bottom 25%.
[293.40 --> 295.84]  I discovered Tmux through Nick Quaranto.
[296.86 --> 299.98]  And it's been all downhill from there.
[300.08 --> 302.08]  I've been using it for a little over a year and a half now.
[302.08 --> 314.42]  So Tmux, we should say, is a terminal multiplexer to stitch together multiple terminal windows into one iTerm window or terminal app window.
[314.62 --> 316.82]  So, Brian, what are the use cases you're using it for?
[317.10 --> 318.88]  So I'm kind of using it for the same thing.
[319.10 --> 324.86]  I'm doing a lot of work with JavaScript and, well, mostly CoffeeScript and SAS.
[324.86 --> 332.82]  And one of the things that I've got running are just the background jobs for converting the CoffeeScript to SAS and running tests and things like that.
[332.94 --> 342.08]  And so I discovered that by being able to use Vim in the terminal and then being able to split the window into multiple work areas, it really is nice to be able to keep my eye on these different things.
[342.14 --> 343.64]  And so I can switch between different projects.
[343.64 --> 358.26]  And one of the things that I've become very used to with using Tmux is that I can actually create a separate Tmux session for multiple projects and actually stay on the same terminal screen but actually move effortlessly between each one of the projects.
[358.82 --> 367.52]  So if something comes up and I can say, well, I've got to work on this right now, I could just move my existing session and reattach to a different session from the same window.
[367.52 --> 369.16]  It's funny you should mention that.
[369.22 --> 373.52]  I'm using a project called Tmuxinator to enroll different environments.
[374.24 --> 379.06]  And it's kind of like stitching together your own IDE for every particular environment that you're working in.
[379.20 --> 381.30]  I've got day job projects.
[381.40 --> 382.94]  I've got hobby projects.
[383.04 --> 389.36]  I also have one that just has all my task paper Vim to-do lists in a single environment.
[390.28 --> 395.78]  So you've got a book coming out from ProgProg in about a month?
[395.78 --> 396.22]  Yeah.
[397.94 --> 399.26]  It was something that I threw together.
[399.36 --> 403.26]  We have this pragmatic writing challenge that goes on in November.
[403.54 --> 407.92]  We invite everyone in the community who's interested just to come out and write a book over the month.
[408.00 --> 411.72]  It's kind of like the National Writing Month that they do for novels, National Novel Writing Month.
[412.36 --> 419.52]  And so my project was just to throw together this short manual on how to get the best out of Tmux for someone who's never used it before.
[419.52 --> 424.32]  And I was going to self-publish it, and I had written a couple of other books for Prags.
[424.38 --> 430.68]  And I thought, it's so much nicer working with an editor and working with copy editors and getting input from other people.
[431.18 --> 433.92]  And so I pitched it to them knowing that it was a relatively short book.
[433.98 --> 435.96]  It actually is only going to be about 80 pages or so.
[435.96 --> 438.28]  So it was really this targeted, focused book.
[438.80 --> 441.20]  But they liked it, and they decided to pick it up and publish it.
[441.24 --> 442.68]  We're going to do e-book only on that.
[443.22 --> 450.80]  But the idea is that it's just something that will take someone who's never used it before and just give them some guidance on, here's some best practices.
[451.02 --> 452.90]  Here's how you maybe want to customize your configuration.
[453.78 --> 459.68]  And I do talk about Tmuxinator in that as well, as well as actually showing you how to do it from scratch too.
[459.68 --> 462.46]  How many pages did you end up with?
[462.62 --> 464.58]  Yeah, we ended up with just a little bit over 80.
[464.96 --> 465.76]  Just a little bit over 80.
[466.20 --> 474.12]  And we're covering things like pair programming with it and working with the text buffers and doing little tricks like extending it so you can say,
[474.68 --> 478.62]  oh, when I open up a new terminal window, I want Tmux to start instead of my regular terminal.
[479.02 --> 483.10]  Or I want to be able to maximize or minimize pains and things like that.
[483.86 --> 487.82]  So mostly little workflow things that will make your life as a developer easier.
[487.82 --> 497.56]  Speaking of configuration, Josh, your .files, I think, were the starting point for me in jumping into Tmux and configuring it to my needs.
[497.68 --> 501.50]  So what are some of the things that you've done that aren't stocked with Tmux?
[502.72 --> 505.82]  So I use this command called reattach to user namespace.
[506.70 --> 508.18]  It's available on Homebrew.
[508.36 --> 515.22]  It allows for interaction with the Mac's pasteboard.
[515.22 --> 522.52]  Basically, within Tmux, in and of itself, you don't have access to doing pbcopy or pbpaste.
[522.92 --> 526.18]  Those commands are basically a no-go with a stock Tmux.
[526.88 --> 536.30]  Reattach to user namespace is a command that you can run that will basically hook into OSX's bindings for a couple of these programs
[536.30 --> 539.76]  and allow you to copy and paste in and out of Tmux.
[539.76 --> 542.36]  So that's definitely an essential.
[543.30 --> 549.88]  One of the other things I do is I set up the default terminal to support 256 colors.
[550.08 --> 552.14]  That's key, especially if you're using Vim.
[553.60 --> 556.00]  Because with Vim, I mean, I want it to look good.
[556.14 --> 559.74]  If I'm going to be spending 8, 10 hours in an editor every day,
[559.74 --> 566.80]  I want to be able to write code and have it look, you know, if not as good as MacVim, as close as possible.
[567.18 --> 569.82]  So I had actually written a Ruby gem called Palette.
[570.38 --> 576.28]  And what Palette does is it allows you to write Vim color schemes with Ruby,
[576.28 --> 583.92]  and then it will go through and compile both the hex values and the 256 color values
[583.92 --> 594.68]  so that you can basically use, you know, as close to a full color Vim as possible within Vim running in your terminal.
[594.68 --> 600.76]  So one of the things that I see in a lot of Tmux config files out on GitHub,
[601.02 --> 602.32]  it seems like I watch a lot of these,
[603.04 --> 608.18]  the most common thing I see is to bind to screen key bindings.
[608.76 --> 609.88]  Is that irony or what?
[610.46 --> 612.22]  I actually do it.
[612.34 --> 613.34]  There's actually two reasons I do it.
[613.40 --> 616.32]  I actually, on my keyboards, on my Macs and my Linux boxes,
[616.42 --> 619.28]  I have my caps lock key mapped as my control key.
[619.96 --> 621.42]  And so that may my prefix is right,
[621.50 --> 624.80]  my command key for the prefix is right next to each other on the keyboard.
[624.88 --> 627.22]  So it's just caps lock A or control A.
[627.58 --> 629.92]  And that works really well because it's just right there.
[629.96 --> 631.58]  I can keep all my fingers right on that home roll,
[631.68 --> 633.10]  and then the prefix is right next to each other.
[633.34 --> 634.54]  I've tried that a couple of times.
[634.88 --> 638.28]  You find yourself missing caps lock when you need to type all caps?
[639.54 --> 643.18]  You know, those few times when I feel like I want to have some internet nerd rage, then yeah.
[643.38 --> 644.88]  But, you know, normally no.
[645.12 --> 647.16]  Have you bounded to another key as a substitute?
[647.38 --> 648.20]  No, I actually don't bother.
[648.20 --> 649.96]  I don't need to use all caps that often.
[650.04 --> 654.02]  And when I do, it's just I can hold on the space bar or the shift key and it's fine.
[654.70 --> 655.60]  I don't miss it at all.
[656.40 --> 659.72]  Yeah, I was in the exact same boat, and I don't miss it at all either.
[660.98 --> 663.20]  So, Josh, what's in your status bar on Tmux?
[663.88 --> 664.60]  Not a whole lot.
[664.66 --> 668.26]  I've just got the time and date in the lower right,
[668.38 --> 671.06]  and then in the lower left I just have, you know,
[671.08 --> 672.34]  all the different windows that I'm running.
[672.68 --> 674.22]  So nothing too fancy.
[674.22 --> 677.74]  I usually have all the custom stuff within Z shell.
[679.58 --> 684.68]  One of the things that I've added is the Tmuxinator project name to let me know which context I'm in.
[685.64 --> 687.54]  Because I run iTerm2 full screen.
[688.02 --> 688.32]  Yeah.
[688.32 --> 694.22]  So it's nice to go between tabs and iTerm and then to see which context you're in.
[694.32 --> 699.06]  But for those that don't know, explain the difference between panes and windows inside of Tmux.
[699.78 --> 705.00]  Basically, windows are conceptually they're different tabs, I guess.
[705.42 --> 711.36]  And then the panes themselves are the different splits within one tab.
[711.36 --> 717.40]  So if you have a tab, typically I'll have different windows for different projects that I'm working on.
[718.04 --> 722.70]  And then within there I'll have a 75-25 split for Vim.
[722.86 --> 733.12]  And then the lower 25% will be either Z shell or typically I'll run Z shell, rail server, evergreen serve,
[733.12 --> 739.90]  because we're doing a lot of JavaScript testing, and then guard, which we have enabled with Spork.
[740.04 --> 742.96]  So it allows for faster tests.
[744.12 --> 746.12]  We've mentioned iTerm a couple of times.
[746.30 --> 749.00]  And the latest version ships with some Tmux integration.
[749.28 --> 750.06]  Have you guys played with that?
[750.88 --> 755.76]  I played with it for about 10 minutes or so, and then another iTerm update came up and said,
[755.84 --> 757.70]  oh, you've got to recompile your Tmux again for that.
[757.90 --> 759.90]  So I'm like, you know, I'm going to wait a little bit.
[760.94 --> 764.10]  It looks like it's going to be really cool once that all wraps up.
[764.12 --> 766.78]  But right now it seems to be in a lot of flux.
[767.26 --> 771.76]  You know, I was excited when I first heard about it, but I've gotten so used to Tmux key bindings
[771.76 --> 775.68]  that even trying to use the iTerm ones, I'm fumbling about.
[775.68 --> 782.24]  So you were saying that you actually keep everything, you keep your iTerm full screen,
[783.00 --> 784.50]  and I do that too.
[784.64 --> 786.54]  One of the things that a good friend of mine showed me how to do
[786.54 --> 789.68]  was actually put a battery indicator in the Tmux status bar.
[790.60 --> 790.90]  Oh, nice.
[790.90 --> 792.62]  And so I can see where my laptop, you know, if I'm on a laptop, I can see,
[792.68 --> 794.66]  oh, I'm at, say, 17% or whatever.
[794.78 --> 796.34]  I better, you know, I better get going here.
[797.42 --> 798.64]  You shared your .files?
[799.38 --> 803.12]  That's actually, actually, I do have a gist of all my .files for that,
[803.12 --> 806.16]  but also I've got a section of that in the Tmux book too.
[806.82 --> 808.92]  I found it to be one of those things that, hey, this is really cool,
[809.04 --> 811.56]  and it shows off a great example of how you can run an external program
[811.56 --> 812.92]  to results in your status bar.
[813.76 --> 817.36]  And you can set the interval how, I guess, how often that paints, right?
[817.54 --> 817.76]  Yeah.
[818.18 --> 820.30]  Yeah, I mean, the default is like a minute.
[820.44 --> 821.36]  I think it repaints every minute.
[821.42 --> 822.02]  I think it's the default.
[822.78 --> 825.68]  I've got a clock in mind, so I think I'm running it every minute.
[826.00 --> 829.84]  So sometimes you're a minute off, but close enough for government work.
[830.22 --> 830.50]  Right.
[830.50 --> 833.22]  So we were talking before we started recording, Josh,
[833.28 --> 835.00]  about some of your favorite plug-ins.
[835.32 --> 835.98]  What are you pimping?
[836.92 --> 842.82]  So two that I use on a daily basis now are tslime.vim and then vimturbox.
[843.12 --> 844.56]  They're both available on GitHub.
[845.64 --> 849.98]  What tslime allows you to do is basically send various commands
[849.98 --> 852.88]  to a specific Tmux pane.
[852.88 --> 859.38]  So basically when you set it up, you'll tell it to point to, like,
[859.44 --> 866.70]  the factory girl session and then the specific window and then a specific pane.
[867.02 --> 870.34]  And what that allows you to do is use vimturbox.
[870.34 --> 876.38]  And they bind to leader T for you, which, you know, I'm not too much of a proponent for.
[876.56 --> 880.68]  I don't like when plug-ins go through and mess with my key bindings.
[880.78 --> 887.16]  But it'll bind to leader T for you and allow you to run just regular old unit tests
[887.16 --> 888.74]  or you can run cucumber scenarios.
[888.74 --> 894.60]  And then leader capital T will run focus unit tests or a focused scenario.
[895.40 --> 903.70]  So I've seen other vim plug-ins that will allow you to run tests, you know, within vim itself.
[904.24 --> 907.98]  The problem with that, I feel, is a lot of times, especially if there's a failure,
[908.52 --> 912.96]  I want to be able to navigate through that and then edit code while I'm looking at the failure.
[913.84 --> 916.82]  And, you know, the vim plug-ins themselves don't support that.
[916.82 --> 923.64]  When I pipe it to another T-Mux pane, I'm able to navigate and use T-Mux's buffer scrolling
[923.64 --> 929.46]  to go back up, look at the error, and then also interact with the code in vim at the same time.
[929.52 --> 930.88]  And that's really key.
[930.98 --> 937.28]  It's really essential to a very fast workflow feedback loop between writing the test,
[937.36 --> 939.30]  watching them fail, and then getting them to pass.
[939.56 --> 942.10]  You know, that's awesome just even if you're by yourself.
[942.10 --> 948.88]  But what is killer is you can have multiple developers, you know, pairing or even demonstrating code
[948.88 --> 950.90]  to other people on your team.
[951.00 --> 954.58]  I think the first time that I came across T-Mux was a co-worker at HP at the time,
[954.66 --> 958.52]  Justin Smestad, turned me on to it, and it has changed my entire workflow.
[958.68 --> 964.20]  We, on our team at Pure Charity now, pair almost exclusively in T-Mux and vim.
[964.48 --> 965.56]  Is that how you guys are using it too?
[965.56 --> 969.76]  So I can say that was actually my first real exposure to it.
[969.84 --> 973.48]  I had kind of had it on my machine and had played around with it for a while, but I was
[973.48 --> 979.66]  working on a project with a friend of mine, and he said, let's just, you know, pair using
[979.66 --> 980.04]  T-Mux.
[980.12 --> 981.44]  And I thought, okay, that sounds cool.
[981.58 --> 984.54]  And when he actually walked me through it, because he was a much better T-Mux user than
[984.54 --> 988.68]  me, it just blew me away with how cool that was and how productive that was.
[988.70 --> 991.14]  And all we needed was a really simple voice chat running in the background.
[991.24 --> 993.32]  We could do everything else we needed to do inside of that window.
[993.32 --> 998.12]  And that really worked well, especially like on connections where it's, you know, you
[998.12 --> 1001.34]  have lower bandwidth, like a hotel room or things like that, where you may not have the
[1001.34 --> 1002.12]  best internet connection.
[1002.70 --> 1004.50]  And, you know, you can take that a step further.
[1005.08 --> 1011.64]  And I've got this Asus Android tablet here with a keyboard on it, and I can use that to
[1011.64 --> 1014.32]  SSH into a machine somewhere else and continue to work.
[1014.50 --> 1019.42]  So I can keep this really nice, light footprint, keep my environment running and running detached
[1019.42 --> 1023.56]  on this server and then connect into it from an iPad or a other kind of device.
[1023.66 --> 1024.80]  That's really kind of cool as well.
[1025.34 --> 1028.46]  That's why you're spreading the gospel with Derek Bailey on Twitter.
[1028.56 --> 1031.44]  I think it was this morning or yesterday he was asking about pair setups.
[1031.84 --> 1032.04]  Yeah.
[1032.86 --> 1038.68]  Have you guys seen, Derek Bailey, I guess is from Watch Me Code, I should mention for those
[1038.68 --> 1039.70]  that don't know who Derek is.
[1040.40 --> 1042.20]  But have you guys seen pair.io?
[1042.80 --> 1043.06]  Yeah.
[1043.06 --> 1049.06]  So essentially it's setups we're talking about here and moving into the cloud so that you
[1049.66 --> 1054.48]  can unfurl development environments and not be bound by any one user's bandwidth and move
[1054.48 --> 1056.30]  it up into a central location.
[1056.58 --> 1057.96]  It's a fascinating idea.
[1058.50 --> 1064.90]  One of the – there was – the co-authors and I of our Web Development Recipes book did
[1064.90 --> 1071.48]  a presentation at a conference back in October, and it was a four-person talk in front of a
[1071.48 --> 1074.04]  bunch of people, and we actually used Tmux for that.
[1074.12 --> 1078.10]  So we actually had one person's computer sitting up there hooked up to the display, and then
[1078.10 --> 1081.26]  when it was everyone else's turn to show off the different part of the demonstration to
[1081.26 --> 1084.16]  do the live coding, we just – everybody just did it from their own machine.
[1084.26 --> 1085.62]  And it was really kind of an interesting use of Tmux.
[1085.68 --> 1087.16]  We had four people turned into one machine.
[1087.96 --> 1093.38]  You know, I've gotten spoiled having my own .files locally that – I've been bugging our
[1093.38 --> 1099.34]  DevOps guy to get those up into our chef recipes so that our share key bindings are,
[1099.46 --> 1101.16]  you know, moved from environment to environment.
[1101.16 --> 1106.28]  And I noticed at ThoughtBot, Josh, you guys have just a shared .files repo that I guess
[1106.28 --> 1107.68]  everybody contributes to?
[1108.44 --> 1109.24]  Yes, we do.
[1109.50 --> 1112.00]  I – to be completely frank, I don't use it.
[1113.28 --> 1118.84]  Not to say anything – not that I have anything against it, but I had gone through and basically
[1118.84 --> 1125.08]  tweaked my .files, and I continue to tweak it, and it's just a matter of basically going
[1125.08 --> 1128.20]  back through and porting some of those changes over to ThoughtBots.
[1128.20 --> 1135.56]  The biggest thing is using Tim Pope's Pathogen plugin.
[1135.96 --> 1136.22]  Right.
[1136.56 --> 1138.20]  And then using GetSubmodules.
[1138.36 --> 1142.38]  So I have that all set up with Pathogen and Submodules, and I have a custom-rich text to
[1142.38 --> 1145.56]  go through and grab the latest updates for all my Vim plugins.
[1145.70 --> 1147.26]  That's not in the ThoughtBot.files.
[1147.26 --> 1150.22]  And that's probably the biggest reason why I don't currently use it.
[1151.58 --> 1156.78]  You know, Janus was training wheels for me to get into Vim after we did the Vim episode
[1156.78 --> 1157.56]  and the changelog.
[1157.70 --> 1162.34]  And I'm finding after the latest upgrade, I'm very close to just rolling my own with
[1162.34 --> 1164.18]  Pathogen like so many folks are doing now.
[1165.02 --> 1166.30]  Is that how you run it, Brian?
[1166.30 --> 1172.74]  I have actually all my .files are actually on my Dropbox, and then I have them sim-linked
[1172.74 --> 1176.86]  into the actual proper locations on the different computers that I use.
[1177.82 --> 1179.08]  And so, yeah.
[1179.40 --> 1183.80]  And then still on that, I still use Pathogen to manage all the different Vim plugins.
[1185.54 --> 1187.34]  And so it's kind of this hybrid approach.
[1187.46 --> 1190.74]  But at least whenever I go then, whenever a computer I go to, if I've got access to my
[1190.74 --> 1195.60]  Dropbox on there, I've got the most recent version of my Tmux configuration and my Vim configuration.
[1195.60 --> 1199.16]  That's actually coming quite handy where someone will show me this new trick or whatever.
[1199.82 --> 1204.56]  I just do it, and I don't have to go to the other machines and pull things down or sync.
[1204.64 --> 1205.24]  It's there.
[1205.34 --> 1207.00]  It's ready for me as soon as I get to the other machine.
[1208.00 --> 1208.66]  Isn't that neat?
[1209.28 --> 1210.06]  I love that.
[1210.74 --> 1215.82]  You know, we've been talking about Vim for a lot of the episode, and it's a big piece of
[1215.82 --> 1219.42]  how we use Tmux, but I'm sure there's other text mode apps that you guys have plugged
[1219.42 --> 1220.98]  into your Tmux environments.
[1222.36 --> 1223.34]  What's high on your list?
[1223.34 --> 1230.06]  Hi, on my list as of today is actually this Perl script I found this morning called, I
[1230.06 --> 1231.76]  don't know, it's TTYTER.
[1232.12 --> 1233.90]  It's a terminal-based Twitter client.
[1234.08 --> 1238.50]  So I can see the tweets come in, and I can tweet right from a Tmux pane.
[1238.56 --> 1239.16]  That's kind of cool.
[1239.64 --> 1241.04]  Oh, I saw that tweet.
[1241.52 --> 1243.34]  I'm using Earthquake for the same thing.
[1243.50 --> 1243.76]  Okay.
[1244.62 --> 1249.16]  I like this because it was just so tiny and small, and I just couldn't believe that it
[1249.16 --> 1250.74]  was just one little script.
[1251.56 --> 1252.24]  I was like, that's cool.
[1252.24 --> 1254.22]  You guys make use of the Tmux clock?
[1255.02 --> 1255.26]  No.
[1256.20 --> 1257.42]  Actually, you've seen this, right?
[1257.72 --> 1257.90]  Yeah.
[1258.24 --> 1258.48]  Yeah.
[1258.56 --> 1261.80]  I use that a lot when it's basically my away screensaver.
[1262.38 --> 1264.08]  A couple of us are pairing.
[1264.22 --> 1267.60]  I'll let someone know that I've stepped away.
[1267.76 --> 1273.42]  It seems like a big thing on our team is to attach to somebody's Tmux session.
[1273.42 --> 1278.18]  We're pairing, and then when we end the call, they forget to hang up.
[1278.54 --> 1286.66]  And if someone's got a smaller monitor, you see the dotted perimeter around your screen
[1286.66 --> 1286.86]  there.
[1286.98 --> 1290.42]  And so I'm always having to call them back and say, hey, Lego Mago.
[1290.42 --> 1291.18]  Yeah.
[1291.96 --> 1292.28]  Yeah.
[1292.28 --> 1299.04]  I've tried to go down the offline IMAP and MUT route, but I'm still addicted to the Gmail
[1299.04 --> 1300.48]  interface.
[1301.34 --> 1301.46]  Yeah.
[1301.58 --> 1303.18]  And I use all the keyboard shortcuts.
[1303.58 --> 1305.24]  I use Ursi whenever I go on IRC.
[1305.32 --> 1306.00]  I just use Ursi.
[1306.34 --> 1307.22]  I love that.
[1307.66 --> 1311.62]  It's really nice to have it there, right there in a separate window.
[1311.62 --> 1314.82]  I tried MUT myself.
[1315.16 --> 1320.56]  I do use HTOP quite a bit, especially if I'm on a remote server.
[1320.86 --> 1324.62]  I've got one of the pains in Tmux is another environment that I'm keeping an eye on.
[1324.88 --> 1325.20]  Sure.
[1326.02 --> 1329.32]  I've actually been using Alpine for terminal-based mail.
[1329.50 --> 1330.78]  I like that a lot better than MUT.
[1330.82 --> 1333.54]  It's a lot more friendly if you haven't done MUT before.
[1333.84 --> 1335.00]  Alpine is a lot easier to set up.
[1335.06 --> 1336.78]  It's a lot more like Pine, and you get the inboxes.
[1336.86 --> 1338.36]  And it seems to work relatively well with Gmail.
[1338.36 --> 1342.48]  But I've got to admit, sometimes some tasks are just nicer to do in Gmail.
[1343.50 --> 1346.06]  Any other list of plugins there you want to talk about, Josh?
[1346.62 --> 1347.18]  I don't think so.
[1347.30 --> 1350.86]  I did want to talk about an iTerm2.
[1351.24 --> 1359.00]  I've configured it so that I've set scrollback lines to zero, so that if you have your hand
[1359.00 --> 1367.12]  on a mouse and you accidentally scroll up, by default, iTerm will allow you to scroll, and
[1367.12 --> 1368.80]  then it kind of messes with the display.
[1369.40 --> 1375.72]  So I had turned scrollback lines to zero so that you basically can't scroll with a mouse
[1375.72 --> 1377.30]  in iTerm at all.
[1377.64 --> 1378.84]  That's actually a pretty smart move.
[1378.94 --> 1379.38]  I like that.
[1379.86 --> 1381.08]  It just drove me crazy.
[1381.08 --> 1386.26]  I had been flicking around on the mouse, and I kept on scrolling up, and I'm like, I need
[1386.26 --> 1387.40]  to figure out a way to disable it.
[1387.44 --> 1391.88]  And I spent probably five minutes digging through all the preferences in iTerm until I figured
[1391.88 --> 1392.70]  out how to turn it off.
[1392.70 --> 1395.52]  And so here's kind of the million-dollar question.
[1395.68 --> 1399.32]  Do you have the mouse mode stuff turned off in your TMX configuration?
[1400.18 --> 1400.42]  Yeah.
[1400.54 --> 1403.50]  I avoid using the mouse at all costs.
[1403.64 --> 1403.82]  Yeah?
[1403.94 --> 1404.14]  Okay.
[1404.16 --> 1405.36]  Because it just slows me way down.
[1405.54 --> 1406.62]  I'm way faster than a keyboard.
[1407.10 --> 1407.52]  Me too.
[1408.06 --> 1409.84]  And I didn't believe that at first, either.
[1409.90 --> 1414.34]  I was really resistant to that, and so I kept it so I could select panes, and so I could
[1414.34 --> 1418.84]  select, and I could use the mouse wheel to go back into the scroll buffer and enter copy
[1418.84 --> 1419.64]  mode and things like that.
[1419.86 --> 1424.00]  And yeah, it didn't take me more than about, I would say, a couple of hours before I realized
[1424.00 --> 1424.96]  how annoying that was.
[1425.58 --> 1425.74]  Yeah.
[1425.74 --> 1428.74]  I was defeating myself using TMX.
[1430.54 --> 1436.96]  Another thing that I do, there's a select pane command in TMX.
[1436.96 --> 1444.82]  So I've bound CTRL-A to select pane, and then you can pass dash T and then colon dot period,
[1444.90 --> 1446.30]  which will move forward a pane.
[1447.46 --> 1454.30]  So I can press, hold down CTRL and then AA twice while CTRL is pressed down, and it'll
[1454.30 --> 1455.80]  start cycling through all the panes.
[1456.96 --> 1457.44]  Sure.
[1457.44 --> 1460.92]  So especially if there's only two, when I'm going back and forth, it's a lot easier than
[1460.92 --> 1464.50]  pressing the prefix and then J and K to move up and down.
[1465.22 --> 1471.60]  I just use CTRL-A, CTRL-A as my prefix to cycle through, which is back and forth.
[1471.84 --> 1475.42]  One of the default key bindings is prefix O will do that same thing, too.
[1476.74 --> 1479.18]  So I actually have never remapped the one.
[1479.24 --> 1480.38]  I kind of just always used O for that.
[1481.64 --> 1483.62]  I think it's kind of a weird binding, though.
[1483.72 --> 1485.44]  It just doesn't make much sense, but...
[1486.06 --> 1486.30]  Yeah.
[1487.44 --> 1491.52]  Another thing that I use is a prefix and then left and right curly.
[1492.18 --> 1492.40]  Yeah.
[1492.98 --> 1497.54]  And that will go through and it'll swap the content of each pane.
[1499.02 --> 1501.38]  So a lot of times if I have...
[1501.38 --> 1508.04]  You know, I always run a 75-25 split for Vim and then my shell.
[1508.82 --> 1514.48]  So if I go down into my shell and I run some tests, or if I run tests through Vim with Vim
[1514.48 --> 1519.12]  Turbux, a lot of times what I'll want to do is I'll want to see the output on a bigger screen
[1519.12 --> 1521.06]  or on a bigger area of my screen.
[1521.28 --> 1528.72]  So I'll use the prefix and then the curly brackets to swap those panes so that I have 75% of my
[1528.72 --> 1531.94]  viewing area is now able to look at the failing tests.
[1531.94 --> 1536.00]  So another common case is looking at a diff before I commit.
[1536.48 --> 1536.72]  Sure.
[1536.72 --> 1540.36]  So I just moved that up there so that I have a lot more screen real estate to figure out
[1540.36 --> 1545.36]  what changed and get a full context of what's going on.
[1545.58 --> 1548.32]  It sounds very similar to something that I've started doing lately.
[1548.52 --> 1553.90]  It was actually the last thing that I added to the Teamworks book was basically the concept
[1553.90 --> 1558.96]  of being able to maximize and minimize a pane and just with a little bit of trickery with
[1558.96 --> 1562.18]  creating a new window and then doing some swap pane.
[1562.72 --> 1563.60]  I create a new window.
[1563.80 --> 1567.06]  I have a little script that creates a new window and then swaps the panes from the new
[1567.06 --> 1567.80]  window into the other one.
[1567.86 --> 1571.22]  So you actually can just use a key binding to go up and now the whole pane, a little tiny
[1571.22 --> 1574.24]  pane becomes a full screen pane and you can use prefix down to push it back in.
[1574.98 --> 1579.00]  And it works in a lot of situations as long as you don't switch windows too much.
[1579.56 --> 1582.44]  If you switch windows, then of course, it's going to rely on last pane.
[1582.44 --> 1586.38]  So, but it's nice for the situations where I ran the test and, oh, wow, look at that
[1586.38 --> 1588.72]  stack trace and just, okay, up arrow.
[1588.86 --> 1590.88]  Oh, now I got the full screen down arrow and now it goes back.
[1591.30 --> 1591.90]  Oh, that's great.
[1592.18 --> 1593.40]  You guys nesting Teamworks at all?
[1594.18 --> 1594.50]  No.
[1594.90 --> 1595.22]  No.
[1596.46 --> 1600.06]  I've tried that a couple of times when I posted to our chat room the other day, Teamworks
[1600.06 --> 1604.08]  inception, three Teamworks status bar stacked up.
[1604.42 --> 1605.22]  It's kind of confusing.
[1605.90 --> 1606.14]  Yeah.
[1606.16 --> 1611.64]  I made the mistake of trying to run screen within Teamworks and that was just, that was a
[1611.64 --> 1612.28]  big mess too.
[1612.44 --> 1616.96]  I don't know if they fixed that, but basically there was no way to send, if the prefixes
[1616.96 --> 1620.98]  are the same, there's no way to send a prefix to screen versus sending it to Teamworks and
[1620.98 --> 1622.24]  it was just a mess.
[1622.88 --> 1625.82]  There's the, yeah, I'm not sure how that works because I can get to work with Vim.
[1625.98 --> 1631.26]  I use, cause I use the, I use, you know, control A for my prefix and there's the, there's a
[1631.26 --> 1634.96]  configuration line you can add to the, to your configuration that actually sends the
[1634.96 --> 1636.66]  prefix through to the other app.
[1636.66 --> 1637.92]  Oh, no kidding.
[1638.26 --> 1638.50]  Yeah.
[1638.56 --> 1642.30]  It's, um, and it works, it doesn't work for, for me, it doesn't seem to, on my machine,
[1642.30 --> 1646.48]  it doesn't seem to work for like control A beginning of line and bash, but it does seem
[1646.48 --> 1648.36]  to work to send it through to Vim and other programs.
[1648.78 --> 1649.10]  Huh.
[1649.10 --> 1654.02]  But, um, it's, it's, uh, it's not bind prefix.
[1654.10 --> 1660.54]  I can't remember what it is off the top of my head, but it's, um, it's pretty cool.
[1660.62 --> 1663.44]  Cause that's actually, it's a, it's purpose for being there is for that.
[1663.44 --> 1670.10]  Are you guys always on the lookout for new config options on GitHub dot files or how do you
[1670.10 --> 1671.50]  find new things to try with TMux?
[1671.72 --> 1677.06]  I'm, I'm, I'm definitely into looking for things on, on people's GitHub, um, uh, GitHub repos
[1677.06 --> 1681.20]  for their dot files just because there's just some little neat little things that are these
[1681.20 --> 1683.42]  little one-offs that you never really think of.
[1683.78 --> 1687.98]  Uh, like one that I found, uh, one of the other ones I found from front of mine was just
[1687.98 --> 1692.38]  taking whatever's in the buffer and on, it only works on Mac cause you have the open
[1692.38 --> 1695.54]  command, but taking whatever's in the buffer and passing it to open.
[1695.54 --> 1698.08]  So you can pop open a web browser based off a link you just copied.
[1698.46 --> 1702.68]  Just little things like that where it's, oh, I can leverage all these different little
[1702.68 --> 1705.46]  features of TMux that, that you don't really realize are there.
[1705.46 --> 1710.06]  I mean, you can take the entire contents of a pane and dump it to the, you know, and dump
[1710.06 --> 1714.42]  it to a text file, for example, or, and so those kinds of things become really interesting
[1714.42 --> 1718.04]  when you mix them with different Unix tools and you can just grab out little parts of the,
[1718.16 --> 1719.70]  of the line or whatever you're looking for.
[1720.44 --> 1720.80]  Um.
[1720.80 --> 1725.24]  Who's got some of the best that file repos that you've seen on GitHub or elsewhere?
[1726.84 --> 1729.54]  I, I can't remember off top of my head.
[1729.68 --> 1734.98]  There's, there's been some really interesting cases where I've found, um, just by searching
[1734.98 --> 1740.36]  for like TMux conf and GitHub, I found people's, people's configurations buried within other
[1740.36 --> 1741.02]  projects.
[1741.18 --> 1744.72]  Let's be like, and it's like, wow, there's some really neat stuff in here.
[1745.22 --> 1747.28]  Zach Coleman's got a, uh, a good one.
[1747.28 --> 1752.56]  Um, and even a blog article, uh, it's been, I guess, a couple of years now, uh, dot files
[1752.56 --> 1757.20]  are meant to be formed and, uh, Holman dot files is a good one on, on, uh, GitHub.
[1757.66 --> 1758.70]  There's another one.
[1758.78 --> 1761.44]  Let me find who owns this one.
[1761.44 --> 1769.04]  Because I just know that their, uh, GitHub username is four initials, SKWP, Jan Pritzker.
[1770.08 --> 1775.06]  So SKWP dot files is a, uh, this is a very opinionated setup.
[1775.12 --> 1781.10]  It's got a lot of good, uh, Vim and, and, um, other config pieces in here, but it's, it's
[1781.10 --> 1781.86]  very opinionated.
[1781.86 --> 1788.08]  It does some, uh, you mentioned earlier, Josh, uh, don't be, uh, setting my, my key bindings.
[1788.16 --> 1792.22]  He's got some very opinionated key bindings in here, but I've found a lot of, uh, nuggets
[1792.22 --> 1794.40]  going through his, his dot files here.
[1794.52 --> 1799.34]  I'm, I'm convinced of the statement that if you don't think that your dot files are the
[1799.34 --> 1801.96]  best ones out there, you're doing, you're doing something wrong.
[1803.10 --> 1804.96]  You know, that's a good way to look at it.
[1804.96 --> 1808.80]  So a lot of my dot files actually spawned from, uh, Joe Ferris.
[1808.80 --> 1813.70]  He's a, he's a thought bot CTO it's, they spawned from his dot files, but at the end
[1813.70 --> 1818.40]  of the day, I ended up scrapping most of what was in there and just going through and finding
[1818.40 --> 1822.98]  the little nuggets because, you know, a lot of the stuff that he was doing, I either didn't
[1822.98 --> 1823.60]  find necessary.
[1823.76 --> 1824.86]  I didn't understand what was going on.
[1824.94 --> 1830.16]  And I, I noticed that a lot of, uh, a lot of things that I had in there were slowing,
[1830.16 --> 1832.72]  um, slowing my interactions down.
[1832.72 --> 1839.50]  And there was some plugin from Vim, uh, that slowed my Vim autocomplete down very significantly.
[1840.18 --> 1844.42]  So I definitely encourage everybody to go through and, you know, have their own dot
[1844.42 --> 1848.22]  files and just pull in little bits and pieces from everyone else's.
[1848.56 --> 1853.02]  Yeah, that's exactly like, and that's actually one of the things that I, I always kind of
[1853.02 --> 1857.06]  caution people about when they want to move the T-mox is, you know, don't just take some
[1857.06 --> 1858.26]  dot file and copy it in.
[1858.26 --> 1861.62]  And I mean, really, you're going to want to figure out what works for you and, and, and
[1861.62 --> 1863.32]  at least, at least to build it up.
[1863.32 --> 1865.36]  So you understand what every one of those lines in there is doing.
[1865.42 --> 1868.70]  Cause I, I've seen, I've seen, I've seen people get so frustrated with things.
[1868.70 --> 1873.22]  I've seen people get so frustrated with things like, like, like Janice or, uh, you know,
[1873.22 --> 1876.44]  just any of these other pre-can things with Vim and they'll just get so frustrated with
[1876.44 --> 1876.78]  Vim.
[1877.44 --> 1881.52]  And, and that's a shame because there's a lot of really cool things that an editor like Vim
[1881.52 --> 1882.64]  or something has to offer.
[1882.86 --> 1884.12]  The same thing goes with Zshell.
[1884.12 --> 1889.42]  There's the, uh, Oh, my Zshell that, that repository in GitHub is very popular.
[1889.60 --> 1894.06]  And I'm not saying that it's bad or anything, but a lot of times if you don't understand what's
[1894.06 --> 1898.50]  going on and in the dot files, you know, you're, you're probably going to end up shooting yourself
[1898.50 --> 1899.62]  in the foot at some point or another.
[1899.96 --> 1904.76]  I use Oh, my Zshell and I've, I've scaled it back to just a few plugins that I don't want
[1904.76 --> 1909.94]  to recreate, but, uh, you know, you really need to understand what's going on under the
[1909.94 --> 1911.48]  hood or you're going to drive yourself crazy.
[1911.80 --> 1912.16]  Exactly.
[1912.16 --> 1915.62]  You mentioned colors early, earlier in the conversation.
[1916.30 --> 1921.00]  Um, I forget even where I cargo culted this, but there's a function, a color function that
[1921.00 --> 1928.12]  I got, uh, from some blog posts that basically enumerates and shell from one to zero to two
[1928.12 --> 1930.24]  five and outputs the colors.
[1930.58 --> 1937.54]  Um, and I think I spent a Thanksgiving evening, uh, you know, just customizing my, uh, my T-Mux
[1937.54 --> 1940.40]  color scheme based on, uh, that function output.
[1940.40 --> 1945.34]  But, you know, just even one of you mentioned earlier, you're staring at this thing all day
[1945.34 --> 1945.58]  long.
[1945.62 --> 1946.72]  You might as well make it your home.
[1946.72 --> 1951.40]  Have you guys had any problems with, uh, on Mac OS copying out of T-Mux?
[1951.40 --> 1956.36]  That's one of the things that, uh, Josh was talking about with, um, like with the, the reattached
[1956.36 --> 1960.74]  to user session using that wrapper script to, so at least you can pipe to PB copy and PB paste
[1960.74 --> 1966.12]  and you can actually create key bindings and T-Mux to take your, um, your copy buffer and
[1966.12 --> 1968.46]  paste it into the actual system clipboard.
[1968.46 --> 1972.22]  Uh, and if you're using Linux, you can use X clip for that or some similar programs.
[1972.22 --> 1976.48]  But, um, one of the things that I learned after talking with my, talking to my buddy,
[1976.66 --> 1983.14]  uh, uh, my buddy, Chris Johnson was that if you, uh, just use the meta key or the option
[1983.14 --> 1988.18]  key in your, uh, in iTerm, uh, you can actually just copy that way.
[1988.58 --> 1991.12]  That's what I've started doing since I've found out that trick as well.
[1991.24 --> 1993.28]  It's, um, does it do multiple lines?
[1993.50 --> 1995.36]  And that, that can be unfortunate sometimes.
[1995.70 --> 1998.20]  You might get line, you might get the line numbers in your Vim or something too.
[1998.20 --> 2001.86]  So, uh, just going to copy everything, but at least, you know, if you need to copy something
[2001.86 --> 2004.00]  quickly, sometimes that's faster.
[2005.08 --> 2005.52]  Yeah.
[2005.54 --> 2009.80]  With the, uh, reattached to user namespace that does actually work with the clipboard
[2009.80 --> 2010.62]  and Vim as well.
[2011.02 --> 2011.28]  Yeah.
[2011.34 --> 2019.86]  So if you set clipboard to unnamed, then you can copy and paste within, uh, Vim and it'll
[2019.86 --> 2023.14]  write to your, uh, right to the system clipboard as well.
[2023.14 --> 2030.22]  Talking about a place to find great dot files.
[2030.36 --> 2033.66]  Of course, GitHub is out there, but have you guys seen dot share dot it?
[2034.72 --> 2035.82]  No, I've not heard of that.
[2036.46 --> 2037.26]  Oh yeah.
[2037.48 --> 2038.48]  I've heard of that.
[2038.60 --> 2040.14]  Let me share this in our chat real quick.
[2040.14 --> 2042.74]  There's a teamux category.
[2042.82 --> 2046.44]  It doesn't have much in there right now, but what I do like about dot share it, it has
[2046.44 --> 2049.98]  a, um, has some screenshots.
[2050.20 --> 2054.30]  So if you have a teamux config, it's kind of hard to visualize sometimes what these changes
[2054.30 --> 2058.70]  will do, especially if it's a visual change and they have screenshots in that you can see.
[2059.62 --> 2064.34]  This is something that you want to, uh, pick up and put it in your own config file.
[2064.34 --> 2069.48]  It seems like a lot of folks on this side are big into Arch Linux, which I personally have not used.
[2070.10 --> 2074.72]  A lot of the screenshots on this side have a lot of text mode, uh, MP3 players and things.
[2074.80 --> 2082.32]  We talked about different text mode, uh, apps to be on the Twitter client and email, um, purely
[2082.32 --> 2087.24]  using teamux for development or any sort of entertainment apps.
[2087.24 --> 2091.30]  I've used piano bar with it and it works great.
[2092.52 --> 2096.90]  So piano bar is a, is a interface to Pandora for anyone that's not heard of it.
[2098.02 --> 2105.14]  I've used that one and there's a, uh, on homebrew, there's a command line interface for last FM as
[2105.14 --> 2105.42]  well.
[2106.28 --> 2110.34]  It seems like I've been using audio a lot and it requires flash for playback.
[2110.78 --> 2115.44]  Um, but when I do want to listen to last FM, I'm using that within teamux.
[2115.44 --> 2121.66]  It's got a nice color coded, um, output to the, uh, command line.
[2121.80 --> 2127.74]  And what I love about being in terminal mode and now teamux has kind of enabled me to wrap
[2127.74 --> 2128.56]  all these apps together.
[2128.66 --> 2129.76]  You mentioned Mac Vim earlier.
[2130.32 --> 2135.60]  I got tired of having to keep my color schemes in sync between the terminal and Mac Vim.
[2135.64 --> 2138.20]  And now that it's terminal Vim, it's just, you know, there.
[2138.20 --> 2145.32]  I never, um, I had actually used Vim back when I was in college and I used it for a few
[2145.32 --> 2147.98]  years as I was doing some Oracle database things.
[2148.44 --> 2151.34]  And I actually never used Mac Vim ever.
[2151.44 --> 2154.00]  I had always, every time I used Vim, it would always be terminal Vim.
[2154.66 --> 2158.26]  And so I couldn't, for me, I could never figure out what the benefit of Mac Vim was.
[2158.26 --> 2161.76]  Um, I, and some, some people tell me that I missed out.
[2161.90 --> 2164.58]  It was, it was a great thing, but I find it really interesting now that people are moving
[2164.58 --> 2165.48]  back towards that.
[2165.56 --> 2170.98]  Now things like teamux becoming more, more, um, I would say popular with the, at least
[2170.98 --> 2171.94]  with the crowd I run with.
[2172.46 --> 2175.96]  It's just nice to have your environment on every machine that you want to climb onto,
[2176.06 --> 2176.28]  you know?
[2176.68 --> 2179.32]  So Brian, the book drops the 29th of February.
[2179.68 --> 2180.46]  I think so.
[2181.00 --> 2182.60]  Um, they're around there.
[2183.36 --> 2185.28]  I'm writing a book myself and know how that goes.
[2185.60 --> 2186.58]  It's fun, isn't it?
[2186.58 --> 2188.52]  It's a, it's a process.
[2188.66 --> 2194.24]  You know, uh, at some point I'd love to have a show just on nothing but, uh, uh, book
[2194.24 --> 2198.78]  workflow when it comes to, you know, writing about these open source topics and how antiquated
[2198.78 --> 2200.16]  the publishing industry tends to be.
[2200.22 --> 2202.44]  I know PragProg is probably ahead of the curve.
[2202.92 --> 2206.64]  I, I couldn't, I couldn't imagine working with any other publisher, honestly.
[2207.50 --> 2209.36]  So I'll leave my name.
[2209.36 --> 2210.26]  Can't say enough good things.
[2210.36 --> 2211.74]  Can't say enough good things about them.
[2211.74 --> 2214.64]  So I've got a lot of great titles out there.
[2214.84 --> 2215.96]  And the name of the book again is.
[2215.96 --> 2220.46]  Well, we're actually going to call this just TMUX, um, productive mouse free development,
[2221.26 --> 2222.66]  productive mouse free development.
[2223.06 --> 2224.16]  Be sure to look for that.
[2224.38 --> 2225.56]  Thanks guys for joining us.
[2225.60 --> 2230.62]  It's been fun to talk about TMUX and in text mode, and I'll be keeping an eye on your doc
[2230.62 --> 2230.94]  files.
[2231.16 --> 2231.90]  Thanks for having me.
[2232.26 --> 2232.50]  Thanks.
[2232.54 --> 2233.28]  This has been a lot of fun.
[2233.28 --> 2251.76]  See it in my eyes.
[2251.76 --> 2252.52]  This has been a lot of fun.
[2252.52 --> 2258.90]  Lets go to railroad media toward the world.
[2258.94 --> 2261.06]  Great 4 интер jealous stuff.
[2261.36 --> 2265.20]  Also, partial information to our channel.
[2265.20 --> 2266.92]  ...and the dark fashions...
