[0.00 → 12.18] This is JS Party, your weekly celebration of JavaScript and the web.
[12.80 → 18.94] Thanks as always to our partners at Vastly for shipping all of our pods superfast all around the world.
[19.40 → 21.70] Check them out at Fastly.com.
[22.42 → 29.88] And to our friends at Fly, post your app servers and database close to your users, no ops required.
[30.00 → 31.98] Learn more at Fly.io.
[32.48 → 35.56] Okay, hey, it is party time, you all.
[45.58 → 48.36] Hello, JS Party people.
[49.04 → 52.90] Welcome to this week's fun party about the web.
[53.02 → 53.46] I'm K-Ball.
[53.54 → 54.52] I'm your host this week.
[54.52 → 59.10] And I am joined by the one, the only, Nick Needed.
[59.10 → 60.48] Oh, HOI, HOI.
[60.76 → 61.36] How's it going, K-Ball?
[61.74 → 63.08] It's going good.
[63.20 → 69.92] Well, and that one only is important for this episode because we're doing an episode spotlight
[69.92 → 76.76] on Nick or rather on Nick's toolbox because you all may have heard us in previous episodes
[76.76 → 79.20] kind of reference a lot of the tools that he does.
[79.78 → 82.64] Nick publishes his.files on GitHub.
[82.64 → 87.86] And so I think Jared and I both just pull down his tooling configs and run them locally.
[88.02 → 93.32] And I understand maybe 30% of what it's doing and kind of go from there.
[93.64 → 99.32] But today, we're going to just kind of dig around and understand what are the ways, what
[99.32 → 100.84] are all the tools that you've put together?
[101.02 → 102.06] How do you configure them?
[102.12 → 103.14] How do you think about them?
[103.48 → 105.32] And what is and isn't working the way you want?
[105.56 → 106.84] But yeah, let's start.
[107.22 → 108.92] Maybe let's actually start with those.files.
[108.92 → 111.02] So do you want to share what goes into your.files?
[111.14 → 113.38] What do you configure every time you go to a new machine?
[114.12 → 114.28] Yeah.
[114.54 → 119.92] So it started with just a place to put my Vim RC way back in the day.
[120.00 → 122.90] I think 2011 was my first commit to it.
[123.14 → 127.54] I had been using Vim before that, but I wanted to have something more consistent.
[128.08 → 133.52] And it was actually mine because I think I was using one of my college teachers, Vim RC.
[134.08 → 138.10] And it even had like the abbreviations for his name in there.
[138.10 → 140.34] So if I typed a certain sequence, it would just type his name.
[141.28 → 144.06] But I wanted my own, my own abbreviations.
[144.62 → 151.90] But what goes in there today are my now Neovim config files, my ZSH config files, tmux config.
[152.70 → 157.52] Oh, and I have a brew file in there as well to kind of manage what I, by default, one installed
[157.52 → 158.10] from homebrew.
[158.10 → 165.80] And then just a random assortment of bash scripts that I find are useful or other tooling, like
[165.80 → 168.34] smaller tools that aren't necessarily like vital.
[168.56 → 173.14] Although I guess they kind of are in a lot of ways, but things like ridge, like setting
[173.14 → 176.36] up a config for that and, and other things.
[176.86 → 178.12] Let's start with homebrew.
[178.72 → 183.44] What are the things that you consider essential to install on your new machine?
[183.44 → 186.92] Well, there are 64 things listed in that file.
[188.84 → 194.92] No, the file is 64 lines long, but it's not all, all that because a brew file is a Ruby
[194.92 → 195.38] file.
[195.56 → 197.12] And so you can put some Ruby in there.
[197.20 → 200.16] So I do have one check where I check if it's a Mac.
[200.16 → 207.30] I've somewhat loosely tried to maintain compatibility with non-Mac, specifically Linux systems.
[208.28 → 215.60] And so when I'm on a Mac, I specifically want things like Kitty and Image Optum.
[216.00 → 217.52] I don't know why I want that anymore.
[218.16 → 223.68] But the 1Password CLI and other like font specific like Mac fonts.
[223.68 → 230.86] So I try and install my fonts from there, like JetBrains Mono and a Nerd Symbols font as
[230.86 → 231.14] well.
[231.72 → 232.14] What's Kitty?
[232.48 → 233.62] Kitty is a terminal.
[234.02 → 239.30] Sorry, I was just reading down my list, and it's a terminal emulator for all platforms,
[239.66 → 244.28] but I shouldn't have said it because I don't actually use it anymore.
[244.40 → 249.32] And I might not use it anymore because I found another terminal emulator that I really like.
[249.56 → 249.90] Okay.
[249.90 → 253.58] What are the criteria by which you're judging your terminal emulators?
[254.08 → 255.00] It's got to be fast.
[255.36 → 260.98] That's why I don't use iTerm2 anymore because if you spend all day in a terminal and specifically,
[261.30 → 265.26] I know I'm going to get a lot of hate for this, but specifically if you use ligatures,
[265.60 → 269.84] iTerm2 becomes very slow because it's not GPU rendering that anymore.
[270.36 → 271.78] And so there are other terminals.
[272.06 → 277.58] Specifically, there's Kitty, Alacrity, and Western that are fast.
[277.58 → 280.60] They're GPU accelerated, and they work really well.
[280.60 → 286.58] And in the case of the one that I switched to, which is Western, it's got a lot of nifty
[286.58 → 288.86] things that it just does by default out of the box.
[289.02 → 290.44] And I really like that.
[290.44 → 298.26] Specifically, one thing that I thought was awesome with Kitty that I didn't see with Alacrity was the ability to use one font,
[298.26 → 304.88] but not have to patch that font to add in the nerd icons, because that's just an annoying process, you know?
[304.88 → 309.98] And so I wanted to be able to like to have a different font for all the nerd ones.
[310.72 → 314.32] And with Alacrity, last I checked, you couldn't do that.
[314.50 → 322.62] With Kitty, you can just set a symbol map for all UTF-8 symbols in this range, use this font, and then everything else use a different font.
[322.82 → 326.08] And you can do a similar thing in the settings of iTerm2 as well.
[326.08 → 329.64] In Western, the nerd fonts are just built in.
[329.84 → 332.30] So when you try and use those symbols, they just work.
[332.40 → 333.98] And you can install your own over it if you want.
[334.10 → 338.08] But by default, it will fall back to not just rendering like a blank square.
[338.22 → 339.74] It will render the font.
[340.00 → 340.90] And that's really awesome.
[341.14 → 348.42] So it just like takes some of that mental load of having to maintain that configuration out.
[348.66 → 349.64] And I really like that.
[350.04 → 351.38] Okay, I'm going to ask the dumb question.
[351.54 → 352.44] What are nerd fonts?
[353.02 → 354.14] I'm glad you asked.
[354.14 → 360.70] So a lot of times if you look at someone's like setup, their Vim RC or their like Vim running or anything like that,
[360.72 → 363.70] and you'll see like the file drawer on the left side usually.
[364.06 → 367.08] And in the file drawer, you'll see things like a folder icon.
[367.14 → 368.32] And they might have several different versions.
[368.32 → 370.94] They might have like a folder icon and an open folder icon.
[371.60 → 378.38] And then if they're working in like a React project, all .TSX or JSX files might have the React symbol next to them.
[378.80 → 383.46] So these are like basic things that you'd expect in like a GUI editor like VS Code.
[383.46 → 399.46] Well, we get that by placing a symbol right there and then using a special font that has been patched with these special characters to actually render that in the terminal so that we get all of that GUI goodness textually.
[399.82 → 401.76] And you can map your own as well, you said?
[401.76 → 404.70] You can map different symbols to different things.
[405.16 → 409.02] And you probably could modify your own or like create your own custom font and do that.
[409.22 → 409.86] I haven't done that.
[410.08 → 417.22] I'm just wondering, like, can you do essentially Slack emojis for your terminal where it's just whatever image you put it in there and there you go.
[417.22 → 425.06] No, it can't be like, they're not very sophisticated images and like in terms of like having a lot of colour or anything to them like that.
[425.12 → 429.36] They're like very much like a single colour and relatively simple.
[429.56 → 437.60] But you can, like it adds a lot for me being able to look over on the left and see, oh, there's a TS file or there's a node modules directory or whatever.
[437.60 → 440.18] And it kind of helps to just visually separate things out.
[440.18 → 441.48] Okay, cool.
[441.68 → 443.26] So that's your terminal emulator.
[443.60 → 444.08] You're doing that.
[444.16 → 448.44] And you mentioned you have ZishConfig, and you've got a bunch of bash scripts.
[448.60 → 450.58] So like how, let's work our way one step up.
[450.64 → 453.58] So how are you configuring the interactions in your terminal?
[454.00 → 454.38] Sure.
[454.62 → 461.30] Well, before I switch off of Western, I want to say one more thing that really drew me to that editor or that emulator.
[461.60 → 465.92] And that is the ability to style it like in different ways.
[465.92 → 469.68] Like all of these editor or terminal emulators have like different themes built in.
[469.68 → 474.06] Kitty has like a whole kitten framework where you can install themes from it and all these plugins and stuff.
[474.48 → 481.94] With Western, it's got a really easy configuration that's in Lua and you can like set gradients and stuff.
[482.02 → 489.98] So I've got a very dark terminal with just an ever so slight blue gradient that kind of happens in the middle somewhere.
[490.04 → 490.96] And it's super subtle.
[491.14 → 494.08] Like I don't want it to be something that you notice all the time.
[494.66 → 496.86] But it's there, and it's really cool.
[498.44 → 499.18] All right.
[499.18 → 499.58] Okay.
[499.82 → 500.82] So Z shell.
[501.22 → 501.60] Yeah.
[501.80 → 505.44] I started using that before it was the default on macOS.
[505.72 → 506.68] Now it's the default.
[506.96 → 510.48] And now I feel like I'm fine with that decision.
[510.80 → 514.46] I was going to say, you don't feel like you need to find some other shell.
[515.08 → 516.36] Now I need to move to fish.
[516.74 → 522.54] No, I just have configured a lot of the good fishiness over in Z shell.
[522.78 → 524.72] And I guess I'm there for now.
[524.82 → 525.56] I really like it.
[525.56 → 532.26] I haven't really looked at switching, but specifically the things that I like about it are the ability to have like an async prompt.
[532.26 → 538.80] And so the way that I separate it out is I just I want it to be pretty minimal with just like the current path that I'm at.
[538.80 → 542.50] I don't need to know that I'm an ANSI at whatever the name of this computer is.
[542.50 → 544.40] Like all of that stuff is.
[544.40 → 546.10] You're able to track your identity.
[546.30 → 549.56] You don't have multiple identities you're swapping between as you move around your.
[550.10 → 552.54] I might, but they're very good at keeping track of themselves.
[552.54 → 559.48] No, I just want to know like where I'm at in the directory structure, like what project I'm in specifically.
[559.98 → 561.54] And I have that on one line.
[561.66 → 563.70] You can have multiple lines for your prompt.
[564.00 → 565.06] So I have that on one line.
[565.06 → 568.30] And then below that, I just have like a single, I think like a triangle character.
[568.30 → 570.86] And that's my like, that's where I'm going to start typing.
[571.24 → 575.54] But then I also take advantage of the R prompt, which is the ability to put something on the right side.
[575.54 → 581.96] And over there, I have that asynchronously updating with my get status.
[582.48 → 588.80] And the asynchronous part is important because it's doing a lot of like checking every time of like, oh, you know, get diff.
[588.98 → 590.18] See if there's anything changed.
[590.26 → 590.92] What's changed.
[591.08 → 594.58] And then it relays that to different nerd symbols that it will put up there.
[594.82 → 597.16] So like a plus minus if I have modifications.
[597.94 → 600.02] An up arrow if I have commits that I haven't pushed.
[600.38 → 602.80] A down arrow if I have commits that I haven't pulled.
[603.12 → 605.52] And an up down arrow if I'm out of sync.
[606.10 → 607.26] And then there are other ones as well.
[607.26 → 608.54] Like if I've deleted a file.
[609.28 → 611.58] But all of that can be slow.
[611.84 → 613.46] And it can slow down your terminal tremendously.
[614.20 → 624.34] But luckily, it's pretty easy to create a way to asynchronously hook into that and update that after the script is run so that you don't slow down the terminal at all.
[624.56 → 626.62] And it will just come in when it's ready.
[626.98 → 627.20] All right.
[627.34 → 628.36] So, okay.
[628.46 → 629.22] We're moving up.
[629.30 → 630.12] So now you're in shell.
[630.40 → 630.58] Yep.
[630.84 → 633.52] What different, you mentioned like you install ridge.
[633.52 → 637.40] And what other like shell commands are core for your configuration?
[637.90 → 638.06] Yeah.
[638.44 → 640.72] Ridge is core, I think.
[641.10 → 643.82] Because it's like that's the way that I search for things.
[643.82 → 645.34] And I use that in and out of them.
[645.34 → 653.54] And like it's just a really nice enhancement to grew that's very similar to ACK or the Silver Surfer.
[654.00 → 655.34] I can't remember what it was called.
[655.40 → 661.62] But anyway, it's very similar to those where it's like a better grew that adds in the ability to like do specific filtering.
[661.62 → 668.44] Like I can say I want to ridge inside all the TypeScript files for this string or whatever.
[668.58 → 671.58] And then I can give it like a path to only this subset of files or whatever.
[672.12 → 675.00] But you can also do like a dash capital T flag.
[675.00 → 683.02] And I can say like I want to do all lowercase t TS files and then dash T for spec.
[683.24 → 689.00] And that means look for all TypeScript files but specifically ignore all that end in .spec.TSX.
[689.70 → 690.88] So I don't want to look in tests.
[691.06 → 693.90] I just want to look in source files and then find this.
[694.52 → 695.54] And I can do a lot of that.
[695.66 → 700.10] And like that spec part is not like a standard thing that you can search for.
[700.10 → 706.22] But luckily ridge has a config file that you can create where you can create your own file types in there.
[706.32 → 714.32] And so that I can say spec equals any file that ends in .spec.ts, .spec.js, .spec.TSX, etc.
[714.62 → 721.34] And can really like hone in on what I want to specifically be able to filter on, which is really nice.
[722.06 → 728.20] Another tool that I use is it's called FZF, or it's basically a fuzzy finder.
[728.20 → 732.40] And I don't use it directly, I guess.
[732.56 → 745.10] I have it installed and configured with my shell so that when I'm typing something like a command and I hit control T, I can fuzzy find from there.
[745.18 → 752.20] So if I need to find like from the current directory that I'm in a specific file to like to give the file path to that, to like some command,
[752.20 → 765.26] I can just hit control T, and it will let me fuzzy find recursively down the directory structure from where I'm currently at to find that path, which is really nice and easy to be able to fill in those paths.
[765.56 → 774.64] And then at the same time, I can hit command R, sorry, control R to I'm like doing the math in my head because I have it mapped to caps lock.
[774.64 → 775.50] Oh, yeah, yeah, yeah.
[775.90 → 780.76] I also find like my fingers have interpreted things and my brain doesn't even know what it is anymore.
[780.90 → 781.06] Yeah.
[781.18 → 783.16] So like there'll be things where I'm like, what is that?
[783.24 → 784.76] Okay, I've got to actually do it.
[784.92 → 787.78] And then like, oh, that's the key combination.
[787.90 → 789.02] My fingers have learned.
[789.66 → 790.02] Yeah.
[790.44 → 795.86] But that is an important thing is the first thing I do on any computer is map caps lock to control.
[796.02 → 797.82] And I just do that through the macOS settings.
[797.82 → 799.48] But anyway, I'm hitting that.
[799.58 → 808.64] And if I hit control R, then that lets me use FZF to fuzzy find within my terminal history.
[808.86 → 811.88] And so I can go back and find a specific command that I ran.
[812.32 → 819.88] That's super helpful when I'm running like Docker commands or other ones where I just, you know, it's a long string of stuff and I don't remember exactly.
[819.98 → 821.64] So I'll be just fuzzy find for it and get it.
[822.48 → 823.98] I want to dive into that.
[824.04 → 825.72] So you use caps lock for your control?
[825.72 → 827.60] Not what do you use for escape?
[827.82 → 828.26] Escape.
[828.74 → 829.24] All right.
[830.06 → 831.20] And you're a Vim user.
[831.34 → 833.44] So your pinky must be like long.
[834.04 → 835.34] It is.
[835.54 → 836.00] Yes.
[836.30 → 837.94] I'm also a Tmux user.
[838.16 → 841.98] So and I remap their prefix from control B to control A.
[842.14 → 845.80] So then it's caps lock A, and they're right next to each other, which makes it really easy.
[846.56 → 850.28] But yes, that's another thing that I observed about myself, I guess.
[850.32 → 851.94] I didn't even like really realize it.
[851.94 → 856.30] But when I type, I can't believe that I'm going to admit this on a podcast.
[856.30 → 859.58] But when I type, I don't have to look at the keyboard at all.
[859.72 → 860.98] And I'm pretty fast.
[861.74 → 869.20] But for a majority of it, I'm only using on each hand my thumb, my index finger and my middle finger.
[869.40 → 869.88] What?
[869.88 → 871.02] I know.
[871.80 → 872.60] It's embarrassing.
[873.06 → 874.32] Thumb, index, middle finger.
[874.44 → 877.46] So you're like basically Treeing it, except with your thumbs as well.
[877.84 → 878.12] Yes.
[879.70 → 881.26] I just lost all credibility.
[881.48 → 881.90] I'm sorry.
[882.30 → 889.36] So then how much of your keyboard have you mapped in different ways to, shall we say, how would I put this?
[889.44 → 892.00] Cover for your handicap there of your missing fingers?
[892.00 → 894.32] That's it.
[894.48 → 895.96] I'm pretty fast with it.
[896.30 → 897.86] But yeah, I don't know.
[897.92 → 898.52] I need to learn.
[898.70 → 900.38] I need to like to take the time to do it.
[900.58 → 908.16] And I even want to like, I want to play with one of those like ergonomic, like super split keyboards, you know, where they're like on each side.
[908.16 → 911.90] And your hands can be like six feet apart, and you just start typing.
[912.20 → 914.02] I want to do that, and I want to be good at it.
[914.02 → 923.30] So I just need to like actually sit down and do the hard work of like getting into that flow where you're not even thinking about the keys anymore.
[923.64 → 925.12] So you brought up Tmux.
[925.52 → 934.30] Are we ready to move up to that layer in your tool chest or are there more command line tools that you rely heavily on?
[934.78 → 940.84] I think that those are probably, yeah, those are probably the biggest ones.
[940.84 → 946.12] Oh, the other one that I guess I would throw in there is one called, it's either called Oxide or Oxide.
[946.94 → 952.12] But it's a really cool tool that just lets me hit Z instead of like CD.
[952.34 → 962.38] So like, you know, when I open up a new fresh terminal and I want to CD into my project, I would have to like to know, oh, I put them in an in my home directory in a slash developer directory.
[962.78 → 967.34] And then inside of like, you know, whatever project I work on inside of that.
[967.34 → 969.86] And I'd have to know all of that.
[969.98 → 983.14] But instead I can just type Z and I can type like Z dot, and it will go like look through my history of Zing around and see, oh, last time you did that, you accepted going to your dot files, which is in this directory.
[983.14 → 984.24] And it just like takes me there.
[984.52 → 986.52] And so it's just like a shortcut of like.
[986.64 → 987.28] Oh, interesting.
[987.28 → 992.40] Because I will like to write aliases into my bash or Z-star-c or whatever.
[992.54 → 996.84] But this is basically like dynamic aliasing for your directory structure.
[997.10 → 997.46] Interesting.
[997.70 → 998.00] Exactly.
[998.20 → 999.08] It's really nice.
[999.30 → 999.50] All right.
[999.52 → 1006.30] So I'm up to three tools so far that I'm not using out of your configuration yet that I need to like to learn.
[1006.44 → 1008.04] Let's see how many we get to by the end.
[1008.20 → 1008.48] Awesome.
[1008.92 → 1013.00] For those keeping track, the ones that I've definitely, I need to get up on ridge.
[1013.14 → 1014.42] I think that looks great.
[1014.42 → 1020.04] I think I am using some amount of FZF, fuzzy finding, but I need to like to dig a little further into that.
[1020.24 → 1026.18] And Z-oxide now, which that sounds like it's probably easier to learn and immediate benefits.
[1026.58 → 1026.70] Yeah.
[1026.92 → 1029.10] You set it up, and you forget that it's there.
[1029.18 → 1033.32] All you have to do is like remember to press Z instead of CD and you're there.
[1033.44 → 1033.76] Amazing.
[1033.78 → 1034.74] So it's really easy.
[1039.96 → 1040.74] I'm Jared.
[1040.88 → 1043.02] And this is a changelog news break.
[1043.02 → 1048.86] Device Script is Microsoft's new TypeScript programming environment for microcontrollers.
[1049.44 → 1060.16] It's designed for low power, low flash, low memory embedded projects and has all the familiar syntax and tooling of TypeScript, including the NPM ecosystem for distributing packages.
[1060.80 → 1063.24] This project has a lot of devs excited.
[1063.24 → 1067.02] Jonathan Berry says, quote, dope.
[1067.02 → 1068.54] TypeScript for hardware.
[1069.08 → 1073.80] Always glad to see these attempts at bringing web technologies to embedded systems and see what sticks.
[1074.18 → 1076.24] Even when they don't, they inspire innovation.
[1077.52 → 1082.64] Zach Silver says, quote, this is so much better than MicroPython.
[1082.64 → 1089.22] And Andrea Guiamarchi says, quote, this is the first Esperanto competitor.
[1089.48 → 1091.22] And I think it's going to be huge.
[1091.22 → 1096.78] You just heard one of our five top stories from Monday's changelog news.
[1097.36 → 1109.50] Subscribe to the podcast to get all the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[1109.50 → 1113.38] Once again, that's changelog.com slash news.
[1117.38 → 1118.18] All right.
[1118.30 → 1119.88] So moving up into Tmux then.
[1120.08 → 1127.86] Let's maybe quick do the breakdown of Tmux for those who aren't already drinking the Kool-Aid of the Tmux world.
[1128.88 → 1131.38] So Tmux stands for terminal multiplexer.
[1131.38 → 1139.36] And what it does is it's an application like a TUI, a terminal UI application that you can run inside your terminal.
[1140.18 → 1143.66] And when you run it, effectively nothing changes.
[1143.78 → 1147.04] You just get into another space depending on how you have it configured.
[1147.44 → 1152.20] But now you have these superpowers where you're actually running a terminal inside Tmux.
[1152.42 → 1156.14] And Tmux gives you windowing ability, and it gives you panes.
[1156.14 → 1165.98] And so depending on how you have it configured, I actually have mine configured to not show the menu bar, the Tmux status bar, until I have two windows and then it will show.
[1166.72 → 1175.16] But once you get in, you'll have that terminal window or the menu bar and that will show you like a window, and then you'll have a single pane inside that window.
[1175.42 → 1176.34] And you can do things.
[1176.34 → 1182.96] And then you can hit different prefixes or commands that you set up in your Tmux config to split that.
[1182.96 → 1195.08] So if you needed to, you know, have your editor running in one terminal, and you wanted to open another terminal to run your tests, for me, I just hit prefix, which is caps lock A or control A and then pipe.
[1195.20 → 1197.22] And that would open a vertical split.
[1197.42 → 1201.04] So on the right side now, I could just start running tests and I could see them over there.
[1201.52 → 1207.04] If I wanted a horizontal split, I just hit prefix dash and I get a horizontal split.
[1207.04 → 1210.28] And I can have infinite splits within my windows.
[1210.46 → 1214.88] And then if I want, I can move and have another set of windows and just switch between those.
[1215.02 → 1222.98] And you can copy and paste between them and do all sorts of fun stuff without your fingers ever having to leave the keyboard, unless you're only using three fingers on each hand for some reason.
[1223.94 → 1225.04] Never live this down.
[1225.94 → 1227.44] I'm going to tease you about it forever.
[1227.66 → 1227.76] No.
[1228.46 → 1228.90] Yeah.
[1229.00 → 1229.94] No, it's phenomenal.
[1230.04 → 1231.36] And that prefix is configurable.
[1231.36 → 1231.66] Right.
[1231.72 → 1237.76] Because like I already had, my fingers were already pre-programmed with control A for other things from terminal days.
[1237.88 → 1240.18] So I remapped it to control G and learned.
[1240.28 → 1241.14] Ah, nice.
[1241.54 → 1242.88] By default, it's control B.
[1243.58 → 1246.98] So that's just a little farther away, especially when you're only using three fingers.
[1247.88 → 1256.46] So yeah, it's control A is the prefix that screen uses, which is another like competitor to Tmux.
[1257.04 → 1259.30] And I like that prefix better.
[1259.30 → 1261.04] So I use the screen prefix.
[1261.04 → 1262.90] I remapped it when I was using screen too.
[1263.32 → 1263.52] Yeah.
[1263.66 → 1264.18] Oh, nice.
[1265.54 → 1267.94] But yeah, it's a really great way.
[1268.04 → 1277.42] And this is like what really like starts getting us into what TJ Decries would call like your personal developer environment.
[1277.42 → 1283.42] Like I'm running Vim and, you know, Vim and Neovim both have like built-in terminals.
[1283.42 → 1286.44] And you can do all of this stuff now straight in Vim.
[1286.44 → 1296.44] But having it kind of outside of that is really nice because I get to configure, and I can have like Vim just be like a pain in this custom bespoke editor that I'm creating.
[1296.44 → 1298.72] And then I can have splits that I open.
[1298.72 → 1300.14] And I tend to just open them dynamically.
[1300.14 → 1310.38] But you could script them out to say like when I'm working on this project, I want, you know, a 60% view in here and a 20% like vertical terminal.
[1310.38 → 1312.18] And then I want a small one at the bottom.
[1312.18 → 1314.22] And I just have these three that I can go through.
[1314.22 → 1316.16] So you can script all of that out.
[1316.46 → 1318.40] I'm more fluid, and I'm just like, oh, I need one.
[1318.46 → 1318.90] I'll make one.
[1319.44 → 1320.18] And so I do that.
[1321.00 → 1325.66] I have my prefixes set to like switch between panes.
[1325.72 → 1326.56] I just hit prefix.
[1326.56 → 1331.50] So control A and then H, J, K, or L to move between them all, which is like really easy.
[1332.78 → 1342.68] And the other really cool thing that you can do with it is you can hit prefix Z to full screen one of the panes.
[1342.68 → 1345.24] So it'll take up the full screen and hide the rest of them.
[1345.40 → 1346.44] And they're still there.
[1346.44 → 1349.40] And you can just like switch back to them or hit prefix Z again.
[1349.48 → 1352.00] And you can resize them dynamically and all those things.
[1352.18 → 1352.30] Yep.
[1352.46 → 1356.26] And I'm totally not afraid to have mouse mode like set up and everything.
[1356.42 → 1359.60] So like I will just grab a border with my mouse and start dragging it.
[1359.80 → 1361.20] Like totally fine with that.
[1361.48 → 1370.10] The ability to move around these panes and all of that just using the keyboard and stuff is honestly, that's the thing that has kept me from trying to switch to VS Code.
[1370.44 → 1372.12] Because VS Code, like.
[1372.68 → 1376.90] You can set it up with, you know, Vim key bindings for within a file.
[1377.44 → 1384.50] But navigating across different files and moving things and like I want these two files visible, and I want to swap between them, and then I want to do all these different things.
[1384.62 → 1386.20] Like you got to bring your mouse into play.
[1386.32 → 1387.70] And why do we want to use our mouse?
[1387.80 → 1390.76] Like mouse, my server, that slows you down.
[1391.22 → 1391.38] Yeah.
[1391.38 → 1393.32] Yeah, definitely.
[1393.32 → 1395.26] I tend to have.
[1395.26 → 1399.30] So I use three fingers on the keyboard.
[1399.30 → 1402.66] And then on the right side, I've got an Apple Magic mouse.
[1403.26 → 1404.62] And I just use that.
[1405.16 → 1406.30] I'm totally fine with it.
[1406.32 → 1407.04] I don't use it a ton.
[1407.10 → 1412.70] So maybe I don't realize the ergonomic like issues that this mouse has.
[1412.70 → 1417.72] But then on the left side, I've got an external Apple trackpad.
[1417.72 → 1425.24] And so just depending on whatever hand is free, whatever three fingers are free, I just move to the right or to the left and use that.
[1425.36 → 1428.96] And I'm pretty good with using the trackpad with my left hand or my right hand.
[1429.54 → 1430.86] And same with the mouse.
[1430.86 → 1433.94] Three fingers that makes me think.
[1434.12 → 1442.14] You know how like athletes that have a lateral sport like it's baseball or whatever, they have like one arm that's super buff and the other one is like.
[1442.26 → 1446.80] But I'm just imagining your hands with like your thumb and your first two fingers like really muscular.
[1446.80 → 1449.54] And then these like atrophied ring and pinky fingers.
[1452.96 → 1455.78] I'm trying to think if there's anything that I really use my pinky.
[1456.02 → 1457.48] I mean, I do.
[1457.84 → 1459.22] No, I don't.
[1459.24 → 1459.94] No, never mind.
[1459.94 → 1466.54] It's hard because I don't look at it, you know, so I have to like look and like pretend to do something to actually see.
[1467.98 → 1471.26] Another cool thing about Tmux and this is like one of the best parts.
[1471.38 → 1475.22] So I guess I'll say this, and then I'll get into the way that I use Tmux.
[1475.64 → 1482.40] But the cool thing is that your terminal then is running inside Tmux, not inside your terminal emulator.
[1483.16 → 1485.46] And it doesn't happen very often anymore.
[1485.46 → 1492.76] But one thing that used to be super common in the past was like your terminal emulator might just crash, or you might accidentally hit command Q and close it.
[1492.86 → 1497.04] And you just, you know, closed Vim, and then you got all these swap files and all that stuff.
[1497.04 → 1502.16] The really cool thing with this is if you kill your terminal, if your terminal crashes, whatever.
[1502.84 → 1506.58] Oh, well, open up a new terminal and hit Tmux attach, and you are right back.
[1506.96 → 1508.46] Everything is just as you left it.
[1508.56 → 1508.64] Yeah.
[1508.66 → 1510.18] It's a client server setup, right?
[1510.18 → 1514.34] So the terminals themselves are running on a server that's just kind of happening on your computer.
[1514.34 → 1520.20] And then what you're seeing in your terminal itself is a client to that that's attached.
[1520.72 → 1521.12] Exactly.
[1521.34 → 1523.88] And so if it dies, I mean, your terminals are safe.
[1523.96 → 1524.62] They're on the server.
[1524.96 → 1525.20] Yep.
[1525.80 → 1530.94] And that enables me like it's not associated with any specific terminal window.
[1530.94 → 1533.12] And so on really cool thing.
[1533.26 → 1543.02] Well, two things, actually, if you're ever in a situation where you're presenting like up on stage, you can actually like to attach to the same Tmux session twice.
[1543.22 → 1553.78] And so you could have like on your separate monitor, which is the projector, a terminal window and have another one locally and just look at the one on your computer and not have to like to look back behind you and see what you're typing and all of that.
[1553.78 → 1558.72] You can have them identical and mirrored and just see exactly what you're doing.
[1558.72 → 1563.46] And that is actually another really cool way to like pair with people.
[1563.58 → 1571.82] I've never done this, but in theory, it's awesome because you could just have someone SSH into your machine and Tmux attached to the same thing.
[1571.90 → 1573.46] And then you're both editing in the same place.
[1573.60 → 1582.64] The downside of it is even if they're a Vim user, which is like less and less likely, like it's such a personal editor with personal key bindings.
[1582.64 → 1584.28] You've configured it your way.
[1584.58 → 1584.88] Yes.
[1584.98 → 1587.18] And that configuration lives on the server, right?
[1587.18 → 1591.00] Like you can't have different clients that are configured different way talking to the same.
[1591.46 → 1591.60] Right.
[1592.06 → 1592.34] Yeah.
[1592.72 → 1605.60] But yeah, no, this, this environment, I remember years ago, probably a decade ago now, I may or may not have spilled coffee on my laptop and did not have a laptop, but I had a Chromebook.
[1605.60 → 1622.74] And so I set up a little virtual machine somewhere so I could continue doing development while I got my, my main laptop repaired and being used to everything lives in your terminal, and you move around meant that that was not that much less productive than having a local development environment.
[1622.88 → 1627.74] The biggest challenge was dealing with static assets, trying to add static assets and things like that.
[1627.74 → 1634.34] But yeah, but yeah, I mean, you can do this in a virtual server somewhere and connect multiple people at the same time.
[1634.42 → 1635.06] It's pretty neat.
[1635.30 → 1635.52] Yeah.
[1635.90 → 1637.36] And just that like ability.
[1637.36 → 1646.96] And this is something that I actually use a lot more is I only like, as far as personal machines go, I only have a desktop Mac.
[1647.06 → 1658.34] I have a Mac studio, which is not very portable, but I do have an iPad and there are terminal emulators for the iPad where I can SSH into my studio and then hit Tmux attach.
[1658.50 → 1662.32] And I'm right back to the same exact setup on my iPad.
[1662.32 → 1667.00] Now, do you have a keyboard or somehow typing with three fingers means typing on the iPad feels okay?
[1667.58 → 1667.94] Yes.
[1668.30 → 1668.68] No, no.
[1668.72 → 1676.42] I do have a, I have the keyboard folio case or whatever, their magic keyboard case, which is fine, except it doesn't have an escape key.
[1676.56 → 1680.56] And I, on my iPad, I also map caps lock to control.
[1680.82 → 1682.38] So I need to.
[1682.50 → 1683.62] So how do you get out of Vim?
[1684.26 → 1684.74] You're stuck.
[1684.84 → 1685.58] You can never quit.
[1686.24 → 1687.44] I actually map.
[1687.44 → 1690.78] Uh, so control and then open square bracket.
[1691.10 → 1696.32] It will send escape, but also I have mapped, uh, in my dot files, um, JK.
[1696.54 → 1699.92] If I hit JK while I'm in insert mode really fast, that escapes as well.
[1700.02 → 1700.56] Just kidding.
[1700.62 → 1701.18] I'm out of here.
[1703.32 → 1703.96] All right.
[1704.04 → 1705.42] Anything else on Tmux?
[1705.48 → 1707.20] You wanted to dive into how you use it then.
[1707.42 → 1707.72] Yes.
[1707.72 → 1710.14] So there are different ways that you can use it.
[1710.24 → 1714.68] And I guess I didn't realize this for almost a decade because I just use it the way I use it.
[1714.74 → 1715.20] And that's it.
[1715.20 → 1721.92] I may have still not realized this, but the way I tend to do it is like, if I'm working,
[1722.10 → 1725.54] you know, for, for a client, or I was a consultant for a lot of years.
[1725.54 → 1730.70] So I had like different clients that I'd work with, and I would basically open up a new Tmux
[1730.70 → 1732.08] session for every client.
[1732.56 → 1736.82] And every client might have, I might have multiple repositories that I'm working in.
[1736.94 → 1742.34] And so those each individual repository would end up being its own window inside that client
[1742.34 → 1742.82] session.
[1742.82 → 1745.60] And then I could have splits associated with that.
[1745.60 → 1752.20] And I could always full screen them or, um, or, or not, uh, within each set of within
[1752.20 → 1752.78] each window.
[1753.18 → 1759.92] But I was recently talking to a guy named Josh Made sky, and he was showing me his setup and
[1759.92 → 1764.00] he actually runs a single Tmux session per project.
[1764.00 → 1767.02] So if he was working on his dot files, that would be a single Tmux session.
[1767.32 → 1772.60] And he has it scripted out to where it opens up immediately one window that is the Vim window.
[1772.80 → 1775.14] And he uses a nerd font to put that as the name.
[1775.28 → 1776.68] So it looks like the Vim logo.
[1776.68 → 1784.10] And then it would open up like a, a lazy get in another window and a like a, uh, just a terminal
[1784.10 → 1785.96] for him to run commands in, in another window.
[1785.96 → 1787.48] And he could switch between all of those.
[1787.82 → 1789.48] And that's, that was fascinating.
[1789.48 → 1794.08] Like just the, the different ways to think about doing it, you know, how you, how you break
[1794.08 → 1797.00] it down, and you could have a lot of structure to it, or you could have no structure, or you
[1797.00 → 1802.46] could just kind of on the fly configure it or split and create new sessions and windows
[1802.46 → 1802.98] as you go.
[1803.52 → 1803.62] Yeah.
[1803.82 → 1808.66] Well, and I think that's what makes this interesting because as we've been talking about a lot of
[1808.66 → 1814.74] these, like your Fish setup, your Tmux setup, we're probably about to get into your Vim setup.
[1814.74 → 1819.88] Like these are general purpose tools that you can configure to suit you.
[1821.08 → 1823.54] So let's talk about Vim.
[1823.82 → 1831.24] Let's talk about, or Neovim, the potential elephant here, you know, the editor par, whatever.
[1831.24 → 1837.72] Like the bar against which all of these newfangled editors, uh, try to strive and fail.
[1838.02 → 1843.30] Can you share how you have configured Neovim and how it works for you?
[1843.74 → 1844.10] Yes.
[1844.66 → 1853.24] So my repo is over 10 years old now, and it's got a lot of history along with that, but I
[1853.24 → 1859.52] did switch probably in 2016 or 2017 to Neovim from straight Vim and haven't looked back.
[1859.52 → 1861.92] It's really, really nice specifically.
[1861.92 → 1867.02] Like once you get your head around Lua, you never want to write Vim script again.
[1867.22 → 1870.28] Lua is so nice, and it's such like a fun language.
[1870.28 → 1874.14] And like, you know, now that I know Lua, I can also configure Was term with Lua.
[1874.28 → 1880.62] And like, it is a very portable language that is used in more places than just one place where
[1880.62 → 1881.66] Vim script is used.
[1881.66 → 1886.90] So, uh, it has a lot more incentive to, to be learned rather than the other one.
[1887.00 → 1892.98] But, um, yeah, I have gone through a lot of iterations about how to properly configure
[1892.98 → 1897.02] Vim, uh, and specifically how to lay, lay everything out.
[1897.02 → 1901.10] But I do like in my dot files, put it everything inside a config.
[1901.10 → 1904.48] And then for Neovim, it's in an in Vim directory under that.
[1904.66 → 1907.30] And that's the XDG config home.
[1907.52 → 1912.44] And so when my dot files get installed, the installer script will put everything from the
[1912.44 → 1913.52] config directory in there.
[1913.60 → 1916.98] It will sim link that into a config, a dot config directory in the home directory.
[1916.98 → 1922.24] And that's how I like to tie into the system and make sure everything is where it needs to
[1922.24 → 1922.48] be.
[1922.72 → 1925.30] But that's really nice because then everything just exists in there.
[1925.38 → 1929.02] You create an unit.Lua and your code exists in there.
[1929.32 → 1931.42] I wanted to check.
[1931.78 → 1941.54] I have 2,600 lines of code in my dot files directory and almost 1,500 of that is Lua with another
[1941.54 → 1943.70] 150 being Vim script.
[1943.70 → 1949.94] And so a significant portion of my entire setup is dedicated to Vim or specifically Neovim.
[1950.50 → 1952.64] Yeah, it's, uh, it's really great.
[1952.70 → 1954.54] What do you want to know about, about the config?
[1955.12 → 1960.14] Well, I guess first off, let's talk about, you know, especially for people coming from,
[1960.14 → 1963.14] um, VS Code or something like that.
[1963.18 → 1969.38] What is going to feel similar in terms of configuring Vim versus how you might configure VS Code and
[1969.38 → 1971.76] put plugins in there and what's going to be very different.
[1971.76 → 1975.16] Yeah, it's going to be very jarring, very jarringly different.
[1975.46 → 1978.56] I've only ever used VS Code, like very sparingly.
[1978.72 → 1984.16] I've never really dug into the, the config and all of that, but it has a pretty solid
[1984.16 → 1989.20] GUI around like their Jason configs for everything, um, which is really nice.
[1989.22 → 1990.60] And then they have like the marketplace.
[1990.66 → 1992.76] That's just, you know, a tab within the editor.
[1992.84 → 1994.94] So you can go install plugins and all of that.
[1994.94 → 1997.36] We have a similar thing in that.
[1997.36 → 2001.04] It's not entire, not at all similar in Neovim.
[2001.50 → 2005.28] First off, Vim doesn't really come with its own plugin manager.
[2005.40 → 2008.00] You have to select one and then install it.
[2008.04 → 2012.40] And there are ways like the one I'm using is called lazy.vim.
[2012.68 → 2015.66] It's a really nice new plugin manager.
[2015.66 → 2016.62] That's all written in Lua.
[2016.62 → 2020.30] And the way that I install it is it basically installs itself.
[2020.42 → 2022.66] It does like a quick check to see if it already exists.
[2022.82 → 2025.08] And if it doesn't, then it goes and fetches it.
[2025.28 → 2026.60] And then it will maintain itself.
[2026.60 → 2031.22] Like with it, it'll use lazy to maintain lazy and update lazy, which is really cool.
[2031.34 → 2038.38] But then it gives you a really easy way to just configure a table in Lua with all the
[2038.38 → 2039.62] plugins that you might use.
[2039.62 → 2042.46] So it makes that really nice and easy.
[2043.18 → 2047.56] And I think I have 70 plugins installed.
[2048.58 → 2051.00] Yeah, I'm not afraid of plugins.
[2051.34 → 2054.74] Well, so that's too many for us to break down one by one.
[2054.80 → 2057.90] Do you want to like to give us the classes of plugins that you're using?
[2058.28 → 2058.52] Yeah.
[2058.90 → 2061.90] And just to clarify myself, it's 83.
[2062.04 → 2062.92] I have 83 installed.
[2064.84 → 2066.12] All right, there you go.
[2066.58 → 2067.66] So yeah, I have lazy.
[2067.66 → 2071.80] That's like an essential one, obviously, because it's how I configure all the other plugins.
[2072.64 → 2077.80] And then from within there, I've got pretty much like the essentials one.
[2077.88 → 2080.56] And this one has had a lot of iteration for me around it.
[2080.84 → 2084.34] Our Neovim comes with its own language server client.
[2084.52 → 2089.14] So it knows how to talk to LSPs like the TypeScript TS server.
[2089.42 → 2090.72] There's a Lua one.
[2090.86 → 2091.76] There's one for Rust.
[2091.90 → 2094.22] There's one for all sorts of different languages.
[2094.22 → 2099.20] There's one for Tailwind to help you autocomplete Tailwind classes, which is just it alone is
[2099.20 → 2103.22] wanting me to make me like adopt Tailwind everywhere because it's just so nice.
[2103.28 → 2103.92] It makes it so nice.
[2104.20 → 2109.96] But anyway, the main thing there is like you want to have all of this intelligence that
[2109.96 → 2111.54] you get from VS Code out of the box.
[2111.54 → 2117.14] And Neovim has the capabilities built in, but they have a separate plugin that they maintain
[2117.14 → 2121.78] called LSP Config that you use to configure the LSP.
[2122.02 → 2126.12] And then this way you can tell it what language servers you want to use and how to configure
[2126.12 → 2127.56] them, how to send things to them.
[2127.68 → 2131.78] When they receive specific messages, you can override what they do with that.
[2131.78 → 2138.12] So if it's asking for like formatting or if it's asking for a signature line, you can
[2138.12 → 2142.68] like get in there, and you could call the original thing and modify it in some way or do your
[2142.68 → 2143.18] own thing.
[2143.18 → 2144.82] Like you can really tie in at any level.
[2145.12 → 2150.42] But the one thing that the LSP Config does not do is it does not actually install any of
[2150.42 → 2151.54] the LSPs for you.
[2151.62 → 2155.98] Those are separate things, usually like node modules that you have to install, like TypeScript
[2155.98 → 2157.80] or any of those.
[2158.48 → 2161.36] And so you need a way to manage that.
[2161.90 → 2168.52] And for that, there's another plugin called Mason that will manage your language servers
[2168.52 → 2172.20] and your formatters and your linters and all of that.
[2173.14 → 2178.94] And so you can configure that to go through and install, and I can just type a colon Mason
[2178.94 → 2184.08] capital M and see all the installed language servers that I have.
[2184.08 → 2189.58] And it will also show me like right now, Lua language server and Rust Analyzer and Emma
[2189.58 → 2191.58] Lint all have new versions available.
[2191.58 → 2195.10] So I can go update those, and it can do that all on its own.
[2195.16 → 2199.36] I just hit capital U to update, and it's going to update all three of those.
[2199.80 → 2203.02] And that's a really nice and easy way to do that.
[2203.22 → 2207.34] But then another thing that you probably want from VS Code is completion, right?
[2207.36 → 2212.02] You want to be able to start typing and have it know what a what signature this function
[2212.02 → 2217.10] has and help you to autocomplete that in different ways or to show you, oh, you're trying to
[2217.10 → 2218.66] access these this object.
[2218.76 → 2220.58] Well, here are the properties that actually exist on that.
[2220.70 → 2223.58] And so you can be assured of what you're actually using.
[2223.58 → 2232.28] So for that, you configure Vim comp or CMP, which will give you completion, and you can set up
[2232.28 → 2234.80] like specifically how it does all of that completion.
[2235.36 → 2238.06] What with like what sources it's going to pull from.
[2238.16 → 2241.94] You can have it pull from the LSP, like what the LSP is returning.
[2242.16 → 2246.84] You can have it pull from other places like file system.
[2246.84 → 2251.20] If it looks like you're typing a file path, start completing a file path from where you're
[2251.20 → 2252.62] at or any of that.
[2252.96 → 2255.08] You can have it complete from other buffers that are open.
[2255.82 → 2262.00] And then just from there's actually one for tailwind as well to help you autocomplete
[2262.00 → 2263.08] tailwind classes.
[2263.44 → 2264.52] So that's really nice.
[2265.04 → 2267.14] But all of that is configured through Mason.
[2267.46 → 2270.00] And so Mason manages all of that.
[2270.28 → 2273.30] But then you can also have Mason tie into the LSP config.
[2273.30 → 2278.00] And then there's an another plugin, another set of plugins called null LS.
[2278.58 → 2283.20] And what null LS will do is it will take things that aren't language servers and it will give
[2283.20 → 2288.50] expose them as language servers so that you can use them through the language server protocol
[2288.50 → 2288.80] thing.
[2289.20 → 2291.08] And that's things like ESLint.
[2291.58 → 2293.12] That's things like Prettier.
[2293.54 → 2297.32] And so you can set up Prettier to be the formatter when you whenever you call the format
[2297.32 → 2301.56] function from within the LSP, send that to Prettier and do all of that.
[2301.56 → 2308.22] And so like that has been the biggest like source of change and confusion for my setup
[2308.22 → 2310.90] specifically in the last year, probably.
[2310.90 → 2315.72] It's like I want the LSP and I had it configured one way, and then it's like, oh, I don't want
[2315.72 → 2317.40] to maintain all of these language servers.
[2317.68 → 2318.88] So I want Mason.
[2319.10 → 2322.44] But then, oh, like what's the difference between Mason and LLS?
[2322.80 → 2325.84] Oh, but then what's the difference between Mason, LLS and LSP config?
[2326.06 → 2329.56] And then there's like plugins that tie them all together, too.
[2329.56 → 2331.70] So that's how you get to 84 plugins.
[2332.54 → 2332.98] Right.
[2336.04 → 2342.70] So I think what's interesting here is kind of what a rabbit hole it is and how far down
[2342.70 → 2349.42] you can go, and you can start digging deeper and deeper into fine-tuning your configuration.
[2349.42 → 2356.20] So let me just kind of ask, like, if you were to sum up the amount of time you've put into
[2356.20 → 2361.50] configuring this as compared to like the time that it saves you, what's winning?
[2362.34 → 2365.18] Oh, definitely the time I put in configuring this.
[2365.40 → 2365.90] Absolutely.
[2367.02 → 2368.58] And like I'm ruined.
[2368.78 → 2369.94] I can't use another editor.
[2370.06 → 2373.58] I've tried, but I'm stuck here, and I really like it.
[2373.58 → 2380.52] It does sometimes get really like frustrating when like, you know, things change, plugins
[2380.52 → 2383.12] change, and then it's like, oh, that's deprecated.
[2383.20 → 2384.04] That no longer exists.
[2384.08 → 2387.68] And you have to like you want to start your day coding, but you, you know, you ran lazy
[2387.68 → 2393.48] update, and now you can't even code because your editor is broken and no one's going to
[2393.48 → 2396.66] help you fix it because it's so bespoke to you.
[2396.66 → 2403.68] So, and, uh, that's where it can start getting really frustrating, but overall, like I spend
[2403.68 → 2408.46] like the other funny thing that I say a lot is like, I spend a lot of time trying to make
[2408.46 → 2410.84] the, um, Neo Vim be VS Code.
[2411.50 → 2413.76] And for the most part, it works really well.
[2413.82 → 2417.22] It's much faster, and I get what I want out of it.
[2417.22 → 2421.82] I even have a like another big plugin that I use all the time and have for over a year
[2421.82 → 2423.64] is copilot.in vim.
[2423.64 → 2428.18] And it's a an official GitHub plugin that gives me copilot right within Neo Vim.
[2428.66 → 2433.70] And that's really nice because then I can, I get some of those features, but I will say
[2433.70 → 2442.12] that one of the things that really like has me question whether like a terminal, like a
[2442.12 → 2447.86] terminal UI, uh, editor like this can keep up are all the specifically all the AI
[2447.86 → 2453.62] features that are coming to VS Code or from third parties that if they want to get
[2453.64 → 2458.00] their stuff in front of you, like I was just listening to the, the changelog anthology
[2458.00 → 2463.58] episode from, I think OS con where they were talking to someone from, oh, what's that?
[2463.86 → 2467.32] I can't remember the name of the company, but source graph, I think.
[2467.94 → 2473.90] And, uh, they were talking about some AI thing that can be, it can know about your code without
[2473.90 → 2476.64] being specifically trained on your code or your documents.
[2476.64 → 2479.80] And so it's like all completely private and like, that's really cool.
[2480.32 → 2484.72] Well, they did mention specifically that a new Vim plugin would be coming.
[2484.86 → 2486.02] So that's cool.
[2486.02 → 2487.34] But will everybody have that?
[2487.44 → 2489.00] That's like a big thing.
[2489.00 → 2496.26] I mean, I think there's enough weight in the community, like at least for the next 20 years
[2496.26 → 2498.46] until we all die off, right?
[2498.46 → 2504.78] There's all of us old school hackers who are stuck in Vim, but we've managed to accumulate
[2504.78 → 2509.42] enough influence that, you know, these companies want to, want to cater to us a little bit.
[2509.46 → 2512.36] So we talk about them on podcasts and that sort of thing.
[2513.92 → 2514.90] Keep that rolling.
[2515.12 → 2517.20] We need a new generation of Neovim users.
[2517.20 → 2517.56] Yeah.
[2517.70 → 2518.14] Yeah.
[2518.24 → 2520.74] And I, I totally think that like, it's capable of it.
[2520.74 → 2525.94] Like another thing that you see a lot or that that's like coming down is like, uh, I think
[2525.94 → 2530.70] in, in GitHub X, there's a like copilot chat where you can actually like chat with your
[2530.70 → 2535.16] code base and have, you know, a ChatGPT style interface to that.
[2535.40 → 2541.00] And what Vim has, like, if you, if you use like one of the main plugins that I use is called
[2541.00 → 2542.94] telescope by TJ Decries.
[2542.94 → 2549.04] And it's a fuzzy finder that, that uses diagram under the covers, or I configure it to, uh,
[2549.04 → 2551.60] but it opens up like a floating window right in my editor.
[2551.74 → 2558.58] And you could have similar floating windows open that have chats directly to some AI or
[2558.58 → 2558.84] another.
[2558.84 → 2561.62] And so I think that it's totally capable of it.
[2561.92 → 2566.18] And it's just going to be fascinating to see how far the community pushes things like
[2566.18 → 2566.44] that.
[2566.44 → 2572.26] So speaking of tools that have plugin interfaces and that are very community driven, another
[2572.26 → 2574.00] one I've heard you talk about is Obsidian.
[2574.60 → 2575.08] Yes.
[2575.54 → 2577.84] Do you want to dive into that?
[2578.26 → 2579.22] Yeah, absolutely.
[2579.46 → 2583.80] Before we get into there, one thing we haven't talked about that, I don't know if a Nick Needed
[2583.80 → 2587.24] tooling interview would be complete without is...
[2587.24 → 2588.44] His beloved TypeScript.
[2588.44 → 2594.02] Do you do anything other than like, that's what I use for software?
[2594.18 → 2597.04] Like, is there any configuration I should know about that you're doing here?
[2597.54 → 2598.80] Not really.
[2599.50 → 2606.36] Really the only thing that I do that is custom that I actually, um, TJ helped me set up when
[2606.36 → 2614.70] I was on his, his stream, his Twitch stream once is this custom like TypeScript LSP, like
[2614.70 → 2619.22] override that I do is if you're like saying go to reference, and you want to like specifically
[2619.22 → 2621.18] like, or go to the definition of a file.
[2621.28 → 2622.44] So I hit GD for that.
[2622.50 → 2627.38] If I'm like on a function and I want to go see how that function's implemented, but it's
[2627.38 → 2631.52] like a third party function or maybe the types are separated or something like that.
[2631.52 → 2636.80] What it'll do is it'll open up a quick fix window that has everywhere that that's listed.
[2636.94 → 2639.82] So it could have the function definition, but then it'll also have the type definition
[2639.82 → 2640.94] for it and all of that.
[2641.34 → 2642.66] And I usually don't want that.
[2642.74 → 2646.68] So if there's more than one exam, uh, more than one solution, I just ask it to give me
[2646.68 → 2651.96] the first one, which is usually the, the actual definition of it and not the types, but that's
[2651.96 → 2654.62] really the only TypeScript specific thing that I do, I think.
[2654.96 → 2655.20] Okay.
[2655.68 → 2656.22] All right.
[2656.30 → 2657.48] So Obsidian.
[2657.80 → 2660.00] Yes, it is an amazing tool.
[2660.00 → 2666.74] I have always like strive to be a good note taker and to have a lot of, uh, well thought
[2666.74 → 2667.30] out notes.
[2667.50 → 2674.60] And I read the book, um, how to take smart notes, which like talks about like the Zettelkasten
[2674.60 → 2676.00] system and all of that.
[2676.00 → 2680.74] And I really came around to liking that specifically for like book notes and things like that, like
[2680.74 → 2685.02] notes on something that I'm studying or, or getting something out of.
[2685.02 → 2690.46] And that's a really cool framework, but I have like played around with several editors.
[2690.62 → 2695.38] I think that definitely like the first one out of college that I started using, or maybe
[2695.38 → 2697.14] inside of college was Evernote.
[2697.30 → 2701.76] I think everyone used Evernote at some point, and it was a pretty good editor or a pretty
[2701.76 → 2703.34] good text notes app.
[2703.34 → 2710.36] But like the thing that I never could get my head around, I just hated was the WYSIWYG
[2710.36 → 2711.04] style of it.
[2711.38 → 2715.74] I just don't like WYSIWYG because like, you know, if you're moving around, you're trying
[2715.74 → 2721.16] to go fast, and you get caught in some like formatting glitch where it thinks that you
[2721.16 → 2722.22] still want italic or not.
[2722.22 → 2724.26] Like it's just so annoying.
[2724.50 → 2725.04] I hate that.
[2725.04 → 2729.08] So I moved over to one called bear, I think after that.
[2729.36 → 2733.52] And then I looked at quiver was amazing.
[2733.90 → 2740.40] It was like a specifically a note app for developers, but they never really had last.
[2740.54 → 2745.08] I checked a like mobile version, and I was like, I want my notes available on mobile somehow.
[2745.56 → 2750.70] And so then I got caught up in notion and notion is really cool.
[2750.70 → 2756.28] It like flips everything on its head and everything is a table, and you can have like tables inside
[2756.28 → 2760.90] of tables and tables that relate to other tables and build these like views out of those tables
[2760.90 → 2764.72] to have different pages or different dashboards for how you look at them.
[2765.10 → 2765.92] So cool.
[2766.20 → 2772.68] But the problem is it's in their whatever proprietary format, how they store all of those.
[2772.94 → 2774.52] So if you're trying to export it, it's a nightmare.
[2774.72 → 2779.42] And so I really wanted something that I could have more control over, especially if like,
[2779.42 → 2783.92] you don't know if a tool like notion's gotten a lot more popular since then, but you
[2783.92 → 2785.20] don't know if it's going to die ever.
[2785.40 → 2789.14] And you don't, I don't want it to, but if it did, there goes all your notes, right?
[2789.14 → 2790.50] Because they won't export really well.
[2791.36 → 2797.30] And so then I started hearing about this tool called obsidian, and I heard, Oh, it's just
[2797.30 → 2798.26] all Markdown files.
[2798.26 → 2799.02] And that's really cool.
[2799.18 → 2800.58] The only problem is it's hideous.
[2800.88 → 2802.26] I'm like, well, that's out.
[2802.32 → 2802.94] I don't want to do that.
[2802.96 → 2803.78] I'm a Mac user.
[2803.86 → 2805.58] Everything has to be beautiful and immaculate.
[2807.58 → 2808.04] Get it?
[2808.04 → 2808.98] A Mac you let.
[2809.42 → 2812.56] Uh, there's got to be a sound effect for that.
[2812.66 → 2814.04] You did not just say that.
[2816.10 → 2821.70] And so I didn't look at it for a long time and I kept going with obsidian or sorry with
[2821.70 → 2822.04] notion.
[2822.04 → 2828.96] And then finally, like, I just like got so overwhelmed in the I got to the point where
[2828.96 → 2833.08] everything in notion in my notion database was a single table.
[2833.08 → 2838.42] And I just had different views on that table for how I like separated things out or looked
[2838.42 → 2843.54] at things, but effectively everything was in one table, and it was like unmanageable.
[2843.98 → 2846.08] And so I was like, let me just look at something else.
[2846.08 → 2847.44] And I finally like brought up obsidian.
[2847.44 → 2851.70] And I think at this point they started supporting custom themes for it.
[2851.78 → 2853.94] And so you could make it look a little more pretty.
[2854.68 → 2859.58] And I just fell in love, like from the start, because it is 100% markdown.
[2859.78 → 2861.06] You create a vault.
[2861.38 → 2864.70] A vault is a folder on your Mac somewhere or on your computer.
[2864.70 → 2867.72] And inside that folder is a dot obsidian directory.
[2868.20 → 2870.44] And that's how it denotes itself as a vault.
[2870.92 → 2874.62] But every file that you put in there is now part of your vault.
[2874.80 → 2879.36] And that every, when you create a new file in obsidian, it puts a markdown file in that
[2879.36 → 2879.64] folder.
[2880.22 → 2881.38] And you know what you can do with that?
[2881.46 → 2884.62] You can back that folder up to get, you can sync it with Dropbox.
[2884.70 → 2886.28] You can put it in an iCloud.
[2886.50 → 2889.08] You can use their syncing system, which I actually do use.
[2889.62 → 2892.60] And at the end of the day, it is a folder of Markdown.
[2892.82 → 2894.22] And you know what else you can do with that?
[2894.64 → 2896.58] You can script it outside of obsidian.
[2897.04 → 2902.12] You can use things like hazel to go find, you know, or like automatically place notes
[2902.12 → 2905.76] in there to go clean up notes that maybe are titled untitled.
[2905.86 → 2906.48] That's what I do.
[2907.48 → 2910.98] Because I, you know, accidentally created them or created them and then didn't actually use
[2910.98 → 2911.26] them.
[2911.40 → 2912.60] And so it just cleans them up.
[2912.90 → 2914.96] You can run scripts in them.
[2915.02 → 2916.18] You can add your own scripts.
[2916.18 → 2920.12] You can do anything like that because it's just a folder of markdown files.
[2920.12 → 2924.90] And then on top of that, you can add plugins right within obsidian.
[2925.04 → 2926.82] There are third-party plugins available for that.
[2927.38 → 2928.00] Do they use Lua?
[2928.72 → 2930.00] No, they use TypeScript.
[2930.34 → 2931.08] Oh, even better.
[2931.20 → 2931.44] Yeah.
[2931.44 → 2939.76] I have 52 plugins inside of obsidian, but they're all pretty basic plugins for the most part.
[2939.86 → 2944.56] And probably 90% of them I don't actually use, but I tried them and haven't uninstalled them
[2944.56 → 2944.96] yet.
[2944.96 → 2946.72] But they're really nice.
[2947.00 → 2952.66] And like the way that it does, it's linking like the way, or the way that is really kind
[2952.66 → 2956.00] of pushes you into, you don't have to do it this way.
[2956.34 → 2961.70] But like the really nice thing with obsidian is you pretty much everything that I put in
[2961.70 → 2963.34] there has no structure to it.
[2963.38 → 2967.56] I don't put specific files in specific folders or anything like that.
[2967.56 → 2974.26] I just throw them in there and their linking ability is so good that that is kind of how
[2974.26 → 2975.50] I structure everything.
[2975.62 → 2979.38] So if I need like a collection of notes, I'll create a document that has links to all of
[2979.38 → 2979.92] the other notes.
[2979.92 → 2982.08] And that is like a collection that I have.
[2982.34 → 2986.76] And then they have this graph view that will show you like a constellation of all the
[2986.76 → 2988.72] notes and how they're actually related to each other.
[2988.72 → 2992.70] And you can set, like you can view it from the perspective of an individual note.
[2992.80 → 2996.42] So this note connects to these five notes, and you can see it right there.
[2996.42 → 3000.34] And I have that just automatically every time I open a file in the right sidebar at the
[3000.34 → 3003.44] bottom, it just shows me the local graph, which is really cool.
[3003.44 → 3008.70] So I can like immediately see what's all connected to it and how this idea relates to that idea
[3008.70 → 3014.14] or, you know, this step, this action item that I took in this meeting note, you know, relates
[3014.14 → 3016.42] to Docker or whatever I'm talking about.
[3016.78 → 3018.64] And so that's really cool.
[3018.64 → 3025.38] And a nice, easy way to sort the notes without the mental overhead of where does this note go?
[3025.38 → 3026.74] What does it look like?
[3026.94 → 3028.20] How does it fit in?
[3028.58 → 3030.28] Just create them and throw them in there.
[3030.36 → 3030.92] It's all good.
[3031.74 → 3031.98] All right.
[3032.08 → 3036.96] So we've talked about quite a bit of tooling, and we've come up to this layer of note-taking.
[3037.30 → 3041.64] You know, we started very down in the, you know, what are the command line tools you install
[3041.64 → 3043.72] in your shell and all of that and kind of worked our way up.
[3044.56 → 3051.62] Any tools that are a key part of your daily or weekly process that we haven't talked about?
[3051.62 → 3053.32] Yes, absolutely.
[3053.76 → 3057.30] And I'm glad you asked because I was going to say once we, we broke out of the terminal,
[3057.94 → 3063.20] but the terminal is in a window, and now we moved over to Obsidian, which is in another
[3063.20 → 3063.64] window.
[3063.88 → 3065.38] But how do I manage those windows?
[3065.38 → 3069.64] I've had a long, fun journey with that.
[3070.02 → 3076.12] And I've used tools like Room and I can't remember the names of all the other ones
[3076.12 → 3076.54] that I've used.
[3076.78 → 3084.00] Magnet, all of these like snap to grid window managers that Mac, that everyone creates for
[3084.00 → 3085.42] Mac because Mac won't ship their own.
[3085.42 → 3090.54] And I finally settled on one that I actually really like a lot.
[3090.64 → 3092.32] And it's called Rabbi.
[3093.02 → 3098.60] Rabbi is, I don't know if it stands for anything, but it's a tiling window manager that works
[3098.60 → 3099.84] specifically for macOS.
[3100.70 → 3102.06] And it's really nice.
[3102.14 → 3108.38] You install it from homebrew, and then you start, you say brew services, start Rabbi, turn
[3108.38 → 3108.72] it is on.
[3108.80 → 3112.74] And it just starts sorting your windows and puts everything in a perfect graph.
[3112.74 → 3117.50] And then you can configure that with Lua to say like, oh, on every window I want, you
[3117.50 → 3119.40] know, this amount of padding between them.
[3119.52 → 3122.22] So you have like nice lines between everything.
[3122.58 → 3127.64] And when you create a new window, it will, the other windows will resize to place that
[3127.64 → 3131.90] window in its own box, and you can move them around, and you can do all of this from the
[3131.90 → 3132.38] keyboard.
[3132.90 → 3137.78] And when you close a window, the other windows resort to fill back up the space.
[3137.78 → 3140.32] So you're always using all the space allotted to you.
[3140.32 → 3145.86] And as windows come in and leave, everything is readjusting and sorting itself, which is
[3145.86 → 3146.32] really cool.
[3146.92 → 3151.56] There is only one downside to it, and I'm actually not using it, but there's a lot more that it
[3151.56 → 3155.60] can do where it can do like automatically, like moving windows from one screen to another.
[3155.84 → 3159.32] I actually have three screens here, so that would be really nice, but I can't use it.
[3159.32 → 3164.00] And it can do things like it can like to shade the windows that are not active in different
[3164.00 → 3168.34] colours so that they kind of fade out, and you're more focused on the window that you're actually
[3168.34 → 3169.18] interacting with.
[3169.30 → 3174.76] I can't use that either because to be able to do that, it would have to hook more deeply
[3174.76 → 3179.24] into the dock code, like the macOS dock code.
[3179.24 → 3185.20] And in order to do that, you actually need to disable system integrity protection on your
[3185.20 → 3185.48] Mac.
[3186.20 → 3191.00] And I'm not brave enough to really trust this app to do that.
[3191.14 → 3193.32] So I just don't do it.
[3193.86 → 3195.86] You don't want to know the chaos that is my windows.
[3196.04 → 3199.22] I don't use a tool for this right now.
[3199.26 → 3203.58] I might have to try you by, but I understand that hesitancy.
[3203.58 → 3204.58] Yeah, yeah.
[3204.80 → 3210.42] But it's really cool, like being able to move things around like that and sort things.
[3210.62 → 3215.40] Another tool that I've been using that is kind of a switch up over the last, I guess,
[3215.48 → 3218.46] decade, I have been an Alfred user for probably 10 years.
[3218.68 → 3224.88] Alfred's like a command space, like fuzzy find open apps or like that's the main thing you
[3224.88 → 3225.02] do.
[3225.08 → 3229.64] You hit command space and then type whatever, like by default on Mac that opens spotlight
[3229.64 → 3230.62] and then you can open things.
[3230.62 → 3232.72] But Alfred gives you a little bit more.
[3232.94 → 3237.24] And just recently I made the switch to one called Ray cast.
[3237.94 → 3241.68] And Ray cast is actually pretty cool in that it does all of that.
[3241.74 → 3244.16] But all the plugins, there are a lot of plugins for it.
[3244.26 → 3245.56] They're all written in TypeScript.
[3245.78 → 3250.88] And so it's really easy to like to dig into them and to use them or create your own, which I
[3250.88 → 3253.30] haven't done, but aspirationally, I like that.
[3254.06 → 3259.14] And, you know, I have like plugins for it that is connected to GitHub.
[3259.14 → 3264.48] So I can just like to pull up a quick list of my PRs or I can see the status of my PR without
[3264.48 → 3265.50] actually having to open it.
[3265.58 → 3267.68] I can just see it in a floating window quickly.
[3268.00 → 3268.88] Same thing with Jira.
[3269.18 → 3270.50] Same thing with Obsidian.
[3270.66 → 3274.90] Like you can quickly tie into all of these tools right from one tool.
[3274.90 → 3277.58] And then it's got a lot of built-in stuff as well.
[3277.58 → 3281.86] I used to use Text Expander, but this has its own kind of snippets built in.
[3281.94 → 3283.56] It has a clipboard manager built in.
[3283.70 → 3288.32] It has window management built in so that you can like to set up key bindings to automatically
[3288.32 → 3290.80] move windows around if you're not using something like you buy.
[3291.14 → 3291.96] So that's really cool.
[3291.96 → 3298.30] And in the latest one, like as of a couple of weeks ago, they have a pro version now,
[3298.34 → 3304.24] which is appealing to me specifically because it syncs all the settings between Macs.
[3304.40 → 3308.84] And so I can have the same settings on my work Mac and on my personal Mac.
[3309.12 → 3316.38] But then it also has a built-in AI too, which is just a ChatGPT 3.5, but it's actually kind
[3316.38 → 3316.60] of cool.
[3316.60 → 3322.54] I have it set up to where I hit option space, it opens up a window right there, and I can
[3322.54 → 3327.12] immediately start typing and ChatGPT 3.5 is superfast at responding.
[3327.34 → 3331.66] So if I just need like a quick answer on something or a quick question or a quick, like, here's
[3331.66 → 3334.68] something I want to say, but take all the snark out of it or something like that.
[3334.80 → 3339.68] It's really nice to be able to, to just like quickly get to that without having to, to go
[3339.68 → 3341.28] to the, to the site and all of that.
[3341.38 → 3342.98] So I really like that.
[3343.04 → 3345.46] And I think I'm going to stick with Ray cast for a while.
[3345.46 → 3353.16] And then the only other tool I use like daily is Omni Focus.
[3353.76 → 3355.74] That is what I use for tasks.
[3356.04 → 3360.58] So I don't, I try not to keep any tasks in Obsidian because it's not good at surfacing
[3360.58 → 3366.56] those to me, but like a dedicated to-do manager is essential and one that works well on the
[3366.56 → 3372.08] iPhone as well so that I can see exactly what I can plan my day from my phone.
[3372.20 → 3373.80] That's like the main thing I want to be able to do.
[3373.80 → 3378.30] Does Omni Focus let you interact back and forth with Obsidian in some way?
[3378.36 → 3381.04] Because I, I am used to keeping a lot of to-do's in my notes, but you're right.
[3381.12 → 3382.04] It's not ideal for that.
[3382.40 → 3383.34] Yeah, it does.
[3383.54 → 3389.68] Maybe not in that specific way, but Omni has their, this whole automation framework that
[3389.68 → 3393.74] they've built, and it's specifically built in JavaScript so that you can do all of this
[3393.74 → 3396.14] scripting on your Mac in JavaScript.
[3396.14 → 3399.36] And the nice thing is because they control it, it's also built in.
[3399.44 → 3402.68] So if you set up a script, it's also set up on the phone.
[3403.12 → 3407.74] One that I have specifically set up that I wrote custom is in my position at work.
[3407.74 → 3410.34] I have a lot of pull requests that I need to review.
[3410.34 → 3415.98] And I think that GitHub is totally falling over in like letting me manage that in any
[3415.98 → 3416.72] meaningful way.
[3416.80 → 3421.76] The notifications tab is just not super great because I'm notified for everything.
[3422.00 → 3424.62] And so I wanted a way to like filter that down.
[3424.62 → 3430.80] And so I wrote a quick graph SL query to the GitHub API that like fetches everything where
[3430.80 → 3437.58] not just I'm set up as a reviewer, but where I'm specifically mentioned as a reviewer, like
[3437.58 → 3441.08] because I'm brought in as a reviewer because of the code owners files a lot.
[3441.62 → 3445.62] And a lot of it is like depend on crap that I don't care about.
[3446.08 → 3448.86] And so I just want to be able to like filter through that noise.
[3448.86 → 3453.92] And like, I can say like, I can even give it like a, a list of like approved people like,
[3453.92 → 3458.02] oh, if this person creates a pull request, and I'm somehow, whether it's directly or
[3458.02 → 3461.26] indirectly listed, put that like grab that.
[3461.58 → 3466.36] And then all of that, I can just push a button in Omni Focus, and it goes out to GitHub, gets
[3466.36 → 3466.72] all of that.
[3466.82 → 3473.18] And then it creates a bunch of to-do's right in Omni Focus with links out to the PRs so that
[3473.18 → 3477.34] I can just go through that from one area, check them off as I go and keep track of what
[3477.34 → 3478.48] I've done and what I haven't done.
[3479.56 → 3479.92] Amazing.
[3480.70 → 3481.32] All right.
[3481.32 → 3488.60] Well, I think then we are at the end of our episode, digging through Nick Niece's toolbox.
[3489.30 → 3490.10] Thank you, Nick.
[3490.42 → 3490.84] Thank you.
[3491.12 → 3496.88] I have a long list of things I want to try now, and I was already using a lot of your stuff.
[3497.04 → 3498.58] So like, yeah, blown away.
[3498.70 → 3502.70] So if you're listening to this, do you want more things like this?
[3502.94 → 3506.52] Would this, is this a the type of episode you'd like to see turned into a series?
[3506.60 → 3509.18] Do we want to dig through a bunch of other people's toolboxes?
[3509.18 → 3510.32] Let us know.
[3510.60 → 3511.88] You can let us know in the Slack channel.
[3512.16 → 3516.50] You can let us know by commenting on this episode on changelog.com, however you want.
[3516.58 → 3521.82] But let us know if, would you like to have digging through toolboxes as a series on JS
[3521.82 → 3522.08] Party?
[3522.18 → 3525.72] We can, we can make this a recurring or this could be a one-off because I don't know if
[3525.72 → 3530.36] anybody's toolbox is quite going to match the level of detail that Nick Niece has.
[3530.70 → 3531.80] I can think of quite a few.
[3532.36 → 3532.94] It'd be fun.
[3532.94 → 3533.78] All right.
[3534.02 → 3536.22] That is it for today's JS Party.
[3536.54 → 3537.70] So thank you all.
[3537.96 → 3541.96] And let's keep having a party on the web.
[3552.22 → 3557.68] If you like this style episode where we dig through a specific developer's toolbox, let
[3557.68 → 3559.16] us know in the comments.
[3559.16 → 3562.80] And also let us know who you'd like us to talk to next.
[3563.54 → 3568.32] There's a link in your show notes to leave a comment or join changelog's community Slack.
[3568.62 → 3569.64] It's totally free.
[3569.96 → 3573.82] Head to jsparty.fm slash community and sign up today.
[3574.46 → 3578.96] Thanks once again to our partners for helping us bring you awesome pods each and every week.
[3579.68 → 3584.26] Shout out to Fastly.com, Fly.io, and Typesense.org.
[3584.26 → 3590.28] Thanks to our beat master in residence, the mysterious BMC, for producing every beat you
[3590.28 → 3592.40] hear on all changelog podcasts.
[3593.00 → 3596.54] That is all for now, but we'll party with you again next week.
[3596.54 → 3596.56] We'll be right back.
[3596.56 → 3597.06] We'll be right back.
[3597.06 → 3597.72] We'll be right back.
[3597.72 → 3598.60] We'll be right back.
[3598.60 → 3604.14] We'll be right back.
