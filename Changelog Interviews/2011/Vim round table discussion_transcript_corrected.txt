[0.00 → 18.08] Welcome to the Changelog episode 0.5.6.
[18.38 → 19.36] I'm Adam Stachowiak.
[19.86 → 20.70] And I'm Wynne Netherlands.
[20.82 → 21.80] This is the Changelog.
[21.84 → 23.52] We cover what's fresh and new and open source.
[23.86 → 26.94] If you found us on iTunes, we're also on the web at thechangelog.com.
[27.04 → 28.10] We're also up on GitHub.
[28.10 → 29.52] At thegetup.com.
[30.02 → 35.08] You'll find some trending repos, some feature repos from the blog, as well as our audio podcasts.
[35.30 → 36.96] If you're on Twitter, follow Changelog Show.
[37.34 → 38.50] And me, Adam Stack.
[38.88 → 41.32] And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.90 → 42.76] Fun episode this week.
[42.88 → 44.38] Talked to some masters of Vim.
[44.64 → 50.70] We talked to Drew over at Vim cast, Tim Pope from Hash rocket, and Yehuda of Janus fame.
[51.66 → 52.24] Nice lineup.
[52.80 → 53.76] Nice lineup indeed.
[53.76 → 58.94] Talking everybody's favourite cutting-edge 1960s technology, Dr. Nick said.
[59.36 → 60.16] There you go.
[60.46 → 62.28] So it seems to be the hot editor.
[62.68 → 64.30] I know there's some Emacs lovers out there.
[64.64 → 65.14] Save your email.
[66.00 → 73.66] But Vim seems to be what everybody that is waiting on the heralded TextMate 2.0 is waiting on.
[73.80 → 74.72] They're switching over to Vim.
[75.06 → 75.48] Oh, boy.
[75.54 → 77.12] Yeah, I don't even want to talk about TextMate.
[77.90 → 79.52] That's a bad subject.
[79.52 → 81.88] I'm a TextMate user.
[81.98 → 82.68] I know that you are, too.
[83.34 → 86.48] A lot of people are switching over to Sublime, but it's not open source.
[86.78 → 89.44] So really, I don't want to talk about it on this podcast.
[89.84 → 90.44] Yeah, that's right.
[90.90 → 93.40] But everybody's wanting to try Vim, as am I.
[93.48 → 101.52] So we figured we'd have some experts and talk about setups and macros and kind of the history of how they got into Vim.
[101.62 → 102.50] It was fascinating, I thought.
[102.78 → 103.04] Yeah.
[103.84 → 105.80] We'll be at RedDirtRubicoff next week.
[105.80 → 111.66] Plug that one more time before we head up to Oklahoma, Oklahoma City, April 21st, 22nd.
[111.92 → 115.90] We're going to be talking Ruby, Rails, JavaScript, and doing some Titanium training.
[116.12 → 120.42] So if you haven't got your ticket yet, and you want to go, be sure and get it for the sellout.
[120.86 → 121.94] Fun episode this week.
[121.98 → 122.64] Should we get to it?
[122.90 → 123.36] Let's do it.
[123.36 → 132.86] All right.
[132.90 → 137.36] We're chatting today with some Vim experts on everybody's favourite command line text editor.
[137.52 → 140.50] So before we jump into Vim, let's get some introductions.
[140.78 → 142.02] So Drew, you're up first.
[142.10 → 145.14] Why don't you introduce yourself and a little bit about how you came to Vim.
[145.86 → 146.12] Hi.
[146.18 → 146.96] My name is Drew Neal.
[147.30 → 149.30] And oh, God, how did it start?
[149.30 → 157.18] I used to use TextMate, and then I switched to Vim when I started working at a company where I had to use Linux.
[157.36 → 158.62] I no longer had access to a Mac.
[159.04 → 162.80] So I could have gone with edit, but I chose Vim.
[163.62 → 169.90] I'd kind of been toying with it for a long time before that, but this just gave me the push.
[170.24 → 172.14] So I started using Vim full-time.
[172.14 → 178.54] And, you know, it took me a while, but eventually I started to really love it.
[178.74 → 183.62] And I wanted to start sharing with people the tricks that I was learning.
[183.76 → 188.10] So I started the Vim cast's blog and podcast.
[189.16 → 191.00] And so that's why I'm here today.
[191.68 → 193.34] We'll jump into Vim cast in just a moment.
[193.68 → 193.90] Tim?
[194.66 → 198.86] I started using Vim about a decade ago when Emacs was a little too hard for me.
[199.70 → 202.24] Since then, I've taken the writing plugins.
[203.12 → 207.56] People probably know, but I've written Rails. Vim, Fugitive, Surround, several others,
[207.72 → 213.42] and maintain several dozen runtime files that ship with Vim.
[214.42 → 217.90] And Yehuda, you are, I guess, shying away from the Vim expert label.
[217.90 → 220.00] But for those that don't know you, who are you?
[220.56 → 221.16] I'm Yehuda.
[221.16 → 226.48] I work on a bunch of open source projects, probably most notably jQuery and Rails.
[226.92 → 229.88] My day job these days is mostly working on the Sprout Core framework.
[231.50 → 234.54] I, like a lot of other people, use TextMate for a while.
[235.06 → 240.58] And I'm also not a person who switched to Vim because I wanted to be able to, like,
[240.64 → 241.92] as a station to a server and use it.
[242.20 → 247.42] I was frustrated by a bunch of limitations in TextMate that I eventually stopped talking
[247.42 → 248.88] myself out of as being limitations.
[248.88 → 254.30] And I saw a bunch of people working productively in Vim, tried a lot, many times to use it,
[254.68 → 259.58] and was frequently told that I needed to, like, dive in, go cold turkey, etc.
[260.24 → 264.72] And that never worked for me because I was never willing to give up, like, two weeks to
[264.72 → 265.10] learn Vim.
[265.42 → 269.70] And I eventually decided that the way I would learn Vim is to pretend it was TextMate and
[269.70 → 271.90] turn on all the things that let you do that.
[271.90 → 273.94] And it was actually extremely smooth.
[274.28 → 278.84] Like, within an hour, I was, like, approximately as productive as I was on TextMate.
[279.06 → 284.90] And as a person who hacks tools and likes to customize my environment, I quickly got into
[284.90 → 289.42] building plugins, or sorry, using plugins.
[289.70 → 292.12] And then I ended up saying, like, oh, this seems like a problem.
[292.24 → 294.40] Everybody wants to have plugins.
[294.50 → 296.10] And I guess everyone uses T-Pope stuff.
[296.18 → 297.78] But there are a few other things that I care about.
[297.78 → 301.10] Plus, I am, like, doing a few different things than Tim is.
[301.16 → 303.44] So there are these plugins that I want.
[303.60 → 306.12] And, oh, wouldn't it be great if everyone in my office could use the same thing?
[306.18 → 310.12] So I ended up building a distribution of common plugins that I now maintain.
[310.72 → 312.80] We're going to jump into those plugins just a moment.
[312.94 → 316.80] But a couple episodes ago, we had Dr. Nick from Engine Yard on the podcast.
[317.08 → 320.58] And he says he prefers TextMate instead of 1960s technology.
[320.76 → 322.20] So, Drew, what would you say to Dr. Nick?
[324.22 → 326.26] Well, I guess he probably uses Unix, though, doesn't he?
[327.78 → 327.90] Yeah.
[328.58 → 328.94] Touché.
[329.82 → 331.16] Also, how old...
[331.16 → 333.38] Vim isn't that old.
[334.30 → 337.66] Like, I guess what I would...
[337.66 → 339.58] What is the distinction between VI and Vim?
[339.58 → 345.56] Yeah, like, Vim is a tool that has been around for a while, like a lot of other tools, like Lisp or whatever.
[345.78 → 349.94] But that doesn't mean that, like, when they created it, then the next year they were like, I guess we're done.
[350.06 → 350.50] No more.
[350.72 → 350.88] Right?
[350.88 → 352.40] It obviously continues to be developed.
[352.40 → 358.44] So I, in general, people, like, I think that's a good laugh line that people say about a lot of things.
[358.84 → 364.42] But it's always a kind of weird laugh line because all it really means is that people have been working on it for a long time.
[365.02 → 368.02] It doesn't actually mean that it's out of date or anything like that.
[368.02 → 370.52] So, Tim, you mentioned Emacs.
[371.46 → 372.26] So what...
[372.26 → 375.50] Usually that's the equivalence, and maybe it's a false equivalence that people present.
[375.66 → 377.06] Are you a Vim or Emacs guy?
[377.14 → 378.88] Then, you know, kind of snicker if you're a text mate guy.
[378.96 → 380.22] So you mentioned Emacs.
[380.54 → 382.30] What's the difference between Emacs and Vim for you?
[384.20 → 386.66] Nowadays it's mostly about the modal editing.
[386.92 → 390.42] Just once you get into that mindset, it's hard to go back.
[390.42 → 396.20] At the time, my difficulty approaching it was mostly just because you had to learn Lisp at the same time.
[396.28 → 400.22] And I always found myself editing my.Emacs file in another editor just when I'd get stuck.
[401.32 → 403.76] So, Drew, what was the motivation behind Vim cast?
[406.12 → 415.30] Well, when I switched to Vim, Yehuda's Janus plugin, or distribution, rather, wasn't available.
[415.30 → 418.28] So I spent... I don't know.
[418.38 → 423.76] I mean, it was a couple of months while I was sort of trying out plugins, discarding them, trying out something else.
[423.96 → 425.42] Just, you know, just trying to get comfortable.
[426.92 → 433.34] So, you know, for people starting out today, they can try out Janus and just have this really easy step to Vim.
[434.18 → 435.30] But at the time, it was...
[436.26 → 440.08] I'd constantly be searching the web and trying to find stuff about Vim.
[440.08 → 449.16] And there's a lot of good stuff out there all over the place, but I couldn't really find any one place that gave a lot of, you know, a lot of the answers that I was looking for.
[450.14 → 454.46] So I started Vim casts to try to be that place, basically.
[456.54 → 459.02] So that was the motivation behind it, really.
[459.12 → 460.08] I just...
[460.08 → 466.24] Oh, well, I suppose the other thing is that there are some things about learning to use a text editor
[466.24 → 470.56] that I think don't work so well as a blog post.
[471.44 → 478.70] It's, you know, when it comes to learning to code, you can check out someone's open source project and you can study it.
[478.86 → 482.30] You can use it as reading matter, and you can see why they're doing certain things.
[482.58 → 485.60] And it doesn't matter what text editor or IDE they were using.
[486.10 → 492.48] If someone designs a class in a particular way, it's going to end up having those lines of code, regardless of which editor they used.
[492.48 → 502.28] There's something about the process of going from an idea to, you know, a piece of code.
[504.14 → 505.14] It's very transient.
[505.48 → 507.60] You don't see the actual process of editing.
[508.42 → 514.80] And so people can be extremely productive with their editors, but unless someone actually sees them doing these little tricks and tips,
[515.38 → 516.84] they could die with them, you know.
[516.84 → 523.36] So the screencast format really works for showing how Vim works because there's just things which,
[523.80 → 525.84] to describe it in a blog post would just...
[526.44 → 528.76] It would just be really difficult to write, and it would be difficult to read.
[529.58 → 533.30] But in 15 seconds, you can show something and people just get it.
[533.80 → 535.28] So I kind of...
[535.28 → 540.88] I know when I've picked a good topic when I go to write up the show notes and there's almost nothing for me to write
[540.88 → 544.36] because it's just, you know, just watch the screencast.
[544.46 → 545.64] I can't really describe this.
[545.64 → 548.08] I highly recommend those screencasts.
[548.22 → 550.18] Also, the peep code video.
[550.30 → 552.48] But you mentioned blog posts a couple of times.
[552.64 → 555.94] So Yehuda, you've got one that says anyone that tried to...
[555.94 → 558.60] I guess everyone who tried to convince me to use Vim was wrong.
[558.70 → 559.36] What do you mean by that?
[559.90 → 561.62] Yeah, I guess that was a troll title.
[564.02 → 569.56] So like I said before, I repeatedly found myself frustrated with TextMate
[569.56 → 574.88] and repeatedly was told by other people to use either Emacs or Vim
[574.88 → 583.88] and repeatedly was told by Vim people that I need to like turn off the arrow keys and learn to like to do it correctly, quote unquote.
[583.88 → 588.36] And I think that there's probably like from a pure perspective, that's probably correct.
[588.36 → 594.48] I think if you're willing to do that, like if you could go to a two-week training seminar where they're like,
[594.58 → 596.90] all you're going to do is use Vim, I think that's probably right.
[597.36 → 602.80] But I think like a lot of people, I use my editor for my day-to-day work and I can't just be like,
[602.88 → 605.78] oh, I guess the next two weeks I'll get nothing done because I'll be learning my editor.
[605.78 → 613.20] So I routinely would try them and like get told by people that I was doing it wrong
[613.20 → 616.78] and like just be like, forget it, I don't have time right now, I'm just going to go back to TextMate
[616.78 → 618.80] despite the things that I found frustrating about it.
[619.66 → 624.52] And I eventually was just like, no, I'm just going to not, I'm going to pretend it's TextMate.
[624.60 → 628.48] I'm going to, I don't really care about productivity right now,
[628.54 → 631.66] I care about being able to write code because I have a job.
[631.66 → 636.04] And once I did that, I realized that it was very easy.
[636.60 → 639.30] It was like, Vim, editors are editors, right?
[639.34 → 642.68] So you have to sort of understand that there's this modal concept,
[643.18 → 646.48] but actually you could live in insert mode a lot for a while
[646.48 → 650.34] before you need to learn that there's like this other mode.
[651.00 → 653.12] And it wasn't very hard.
[653.54 → 657.94] So I wrote the post mostly out of frustration, like I am now a couple of weeks in, and it wasn't hard.
[657.94 → 660.18] And why did everyone, why did it feel so hard?
[660.18 → 664.70] Everybody in the world who thinks it's hard, like it actually turns out to not be hard.
[665.62 → 670.62] You know, one of the things that I love about TextMate is just the ecosystem of bundles that are around it.
[670.90 → 673.96] And, you know, I think TextMate 2 has become the next Duke Nuke.
[674.16 → 679.24] So one of the things that appealed to me was having my editor on any platform,
[679.24 → 680.94] but I'm going to miss all those bundles.
[681.08 → 684.02] So Tim, when you set out on this Vim approach,
[684.14 → 688.10] what was the plug-in landscape, and what was the first plug-in you wrote?
[688.10 → 695.30] Um, I started fooling around with writing like syntax highlighting files and simple stuff early on,
[695.38 → 698.58] but I didn't really get into it until I found Rails.
[698.84 → 701.50] And then I went and checked, is there a plug-in for Rails?
[701.60 → 702.14] No, there's not.
[702.24 → 704.76] I came back a month later, so it went, and I was like, well, I got to write it myself.
[705.08 → 708.90] So 5,000 lines later, we've got Rails. Vim.
[708.90 → 714.06] So Yehuda, how much of Tim's plug-ins have made it into Janus?
[714.16 → 716.16] I think, like, almost all of them.
[716.22 → 720.28] Anyone that I didn't put initially, I think Pathogen is the only one that,
[721.00 → 723.82] mostly because I'm being lazy, isn't in there yet.
[723.98 → 730.44] But I keep, mostly because switching to Pathogen will require some, like, large changes to the system.
[730.44 → 736.42] But, um, pretty much anything that anybody uses that's useful has been submitted as a patch and accepted.
[737.00 → 740.06] Uh, there's a bunch of other stuff that is more complicated, like Nerd tree.
[740.10 → 745.98] Like, I have a fork of Nerd tree that I hacked up to, like, look prettier and feel, work more like how I wanted it to.
[746.52 → 752.80] Um, and I guess the thing about, about Vim plug-ins is that they're sort of like Rails plug-ins
[752.80 → 755.82] in that Tim's work really well together because he uses all of them.
[755.82 → 760.80] Uh, but half the work of making a plug-in work well inside of Janus is just like,
[760.88 → 761.88] okay, I've inserted it.
[761.92 → 763.92] It now does not, it now breaks some other plug-in.
[764.38 → 765.34] Can I fix that?
[765.40 → 766.02] Can I remove it?
[766.06 → 767.28] Maybe there's a configuration option.
[767.52 → 773.62] So, uh, Janus to me is sort of like, it is like Rails itself in that it's,
[773.80 → 775.88] it's just trying to make sure that everything is integrated well.
[776.14 → 779.16] It's, it's not so much about, like, there is a certain amount of, like,
[779.16 → 783.36] which alignment plug-in is the best plug-in or which tab completion plug-in is the best plug-in
[783.36 → 785.68] and we, you know, move on until we find the right one.
[785.82 → 788.62] But then there's also, like, how do we make it work well with Nerd Tree?
[788.72 → 789.88] It's like a big part of it.
[789.90 → 791.30] Or how do we make it work well with Command-T?
[792.50 → 797.38] So Janus is geared primarily towards OS X and Mac Vim, but it does work on Linux, correct?
[797.78 → 801.84] Um, I don't know if that's, so, the answer is supposed to be yes.
[802.10 → 805.66] But I, uh, Carl recently tried it on Linux and was like, this doesn't work at all.
[805.66 → 809.18] So I think there's probably some bug that makes it not work.
[809.60 → 812.64] And, uh, that will be addressed rapidly.
[812.64 → 816.98] I, uh, Carl is, is a person who is using Vim because he wants to use it on Linux.
[817.12 → 819.62] So making it work on Linux is a priority right now.
[820.82 → 821.98] It initially did.
[822.66 → 824.42] So something broke somewhere along the line.
[825.56 → 828.66] So, Drew, where do you get ideas for Vim cast episodes?
[828.66 → 838.88] Just through, uh, through using it, um, uh, you know, I'll, uh, I'll spot, spot myself doing something and say, ah, that's, uh, that's useful.
[838.88 → 840.42] And it's maybe not obvious.
[840.42 → 843.12] So, uh, I should do a screencast about it.
[844.04 → 849.92] Um, uh, when I started out, I, I was determined not to do stuff on plugins.
[849.92 → 854.46] Because I think there's so much that you need to learn about the, the core functionality.
[855.26 → 863.04] Uh, so the first, uh, gosh, I'm trying to think the first time I covered a plugin was maybe episode 29 or even 30 or something.
[863.42 → 866.74] Um, up until then it was all core functionality.
[867.36 → 869.58] Uh, so that's how I started out.
[869.92 → 877.14] Um, but lately I've, uh, I've started writing a book about Vim, um, which is going to be published by the Pragmatic Programmers.
[877.14 → 881.32] And my focus there is to, to focus on core Vim functionality.
[881.32 → 889.62] So as long as I'm writing this book, all of my ideas about, uh, working with the core functionality, the editor, they're going into the book rather than into the screencast.
[889.62 → 894.20] So lately I've, I've started sort of drawing up a list of the plugins that I find really useful.
[894.20 → 897.96] And I want to, um, to, you know, show people how I use them.
[898.34 → 907.10] So, um, yeah, I've, I've got a big list of, uh, of ideas and, uh, I just sort of pick whichever one, um, I feel like doing at the time usually.
[907.68 → 909.94] So I know that Tim and Yehuda are both Subsists.
[910.32 → 914.22] Um, hopefully I'm not boxing them in with that term, but how about you?
[914.58 → 915.56] Yeah, I'm a Rubbish too.
[917.04 → 923.16] Um, though lately I've been using JavaScript more, um, pretty much full-time in fact.
[923.16 → 931.16] So, um, yeah, but I, I, I mean, one of the reasons I chose Vim, I think, uh, rails. Vim certainly had something to do with it.
[931.16 → 937.40] Uh, it just, it's, uh, it's so useful, uh, when you're working on a rails project.
[937.40 → 942.30] So, um, yeah, I, I think interestingly, so I am also in the same position.
[942.30 → 944.20] I, I do a lot of Ruby.
[944.20 → 948.18] I write Ruby pretty much every day, but I spend a lot more time with JavaScript these days.
[948.18 → 954.38] And it seems like the eco, the ecosystem around Ruby probably because of Tim is a lot more robust.
[954.38 → 962.56] Like there are issues like you delete a line in the JavaScript mode, and it like takes a second because there's some bug somewhere in one of the canonical JavaScript plugins.
[962.56 → 981.04] So, um, maybe JavaScript just needs a JavaScript Tim or maybe, but, but at the end of the day, like Vim is nice because it, it has all these plugins, but there's definitely like differences in quality between things that are heavily maintained by a community of users.
[981.04 → 984.90] And like things that are there, you know, like people like me, I use Ruby.
[984.96 → 985.72] I also use JavaScript.
[985.88 → 986.88] I want it to work with Vim.
[986.98 → 988.96] So I make it work somehow.
[989.30 → 990.20] That's not as good.
[990.20 → 996.32] So how much easier or more difficult is it to write a plugin for Vim as opposed to TextMate?
[997.76 → 999.60] If you're asking me, I don't, I don't know.
[999.68 → 1001.02] I've never written a TextMate plugin.
[1001.40 → 1003.00] So I can, I can answer that, actually.
[1003.16 → 1007.20] Uh, I think it's, it is harder, but you can do more.
[1007.46 → 1010.54] So TextMate is basically, it's very like Unity.
[1010.62 → 1011.62] There's like input output.
[1011.82 → 1019.08] You just do your thing, and you like shell out essentially the programs, and it's your access to what is going on in the editor is very weak.
[1019.08 → 1022.72] But that limitation, I think, encourages creativity.
[1022.72 → 1028.92] So people like work around it in creative ways where Vim's plugins are extremely powerful.
[1030.00 → 1035.74] And, uh, it, and you can even like to write them in Ruby if you want it like, and, and still have access to the editor context.
[1035.74 → 1041.24] So you can do it in TextMate, but then you're like shelling out to a Ruby process and like looking at environment variables.
[1041.24 → 1044.54] And, and Vim like gives you a runtime that is sensible.
[1045.24 → 1045.60] Awesome.
[1046.08 → 1052.88] But because there are more things going on, it's, if you, all you ever did was TextMate plugins, you'll perhaps be a little lost.
[1053.08 → 1060.60] And I think the universe could use a like how to write a TextMate, uh, Vim plugin tutorial that is better than what exists right now.
[1060.78 → 1063.32] Maybe I just haven't seen it, and it's awesome and it exists.
[1063.32 → 1079.34] Are you guys, uh, Vim colour, um, I guess customizers or, um, do you have a preference for your favourite, uh, syntax highlighting in Vim as opposed to your regular terminal?
[1081.60 → 1084.04] I, I use my own Vivid Chalk.
[1084.22 → 1086.82] It's based on that vibrant ink for TextMate.
[1086.82 → 1100.10] So Janus ships with IR Black, which I like a lot mainly because it, uh, I think there's a, a few of them like this, but, um, IR Black does a good job of making it not look like you're in a Text Mode editor.
[1100.10 → 1105.10] And I actually like the fact that Janus makes it feel more, you know, more modern.
[1106.04 → 1111.66] But I saw there was some, uh, new theme that was posted on Hacker News that actually looked like it might be better.
[1111.78 → 1113.88] And I wanted to try it out and see if it's better.
[1113.88 → 1116.78] Was that Solarized?
[1118.20 → 1118.48] Yes.
[1118.84 → 1119.24] Solarized.
[1119.38 → 1119.74] Exactly.
[1119.92 → 1120.80] I've been trying that one out.
[1121.12 → 1126.78] I need to try it out and like for a couple of days and see if it, if it's like obviously bad or obviously better.
[1127.54 → 1139.72] You know what, uh, impressed me about Solarized was the fact that it kind of turned the theme sideways where usually you pick your editor, or you pick your product and then you, you pick from themes that were available for that.
[1139.72 → 1139.92] Right.
[1140.00 → 1141.98] Where Solarized is kind of the opposite approach.
[1141.98 → 1145.80] It's all these different programs bundled together in one theme.
[1146.26 → 1146.64] Yeah.
[1146.68 → 1152.12] And it seems like he spent a lot of time thinking about the theory behind it in ways that seemed sensible to me when I read his post.
[1152.12 → 1160.56] So, Drew, Ryan Bates over at Rails cast, um, I know his TextMate theme got popular because he used it in his, his, uh, screencast.
[1160.68 → 1162.00] So what about Vim cast?
[1162.08 → 1162.76] Do you have your own?
[1163.08 → 1167.42] Um, I've been using the Blackboard theme, which, uh, there's a few out there.
[1167.52 → 1171.14] It was the theme that I used when I used TextMate and I just got used to it.
[1171.14 → 1175.68] So when I switched to Vim, I, um, I looked around, and I think there were a few ports out there.
[1175.78 → 1178.58] I picked one of them, and I've, I've been customizing it for myself.
[1179.30 → 1185.50] Um, I just use it because I like it and, uh, it looks, well, like I say, it was the one that I used in TextMate.
[1185.50 → 1198.58] Um, although lately, I mean, one of the things that people often say, um, at conferences when people put up, uh, code snippets in their slides, if they use a dark background, quite often it's very, very difficult to read for the people in the audience.
[1198.90 → 1212.74] So I think it's really important to have a light theme, even if you don't like using a light theme from day to day, just to have a light theme that you, you know, is there, and you know you can switch it on, uh, if you're at a conference, and you're, you're live demoing something or something like that.
[1212.74 → 1222.20] Um, so, um, one of the one of the light themes that I liked in TextMate was called Mac Classic and, uh, I ported that one over to, um, to Vim.
[1222.90 → 1238.42] And, uh, in fact, I've, I've tended to use that one more, um, than Blackboard, uh, just because it was kind of, while something like that is a work in progress, suddenly you'll find yourself working on a, uh, a file with a syntax that you don't use maybe day to day, and you realize, oh, this, this one really needs some attention.
[1238.42 → 1246.48] So, um, if you're developing a colour theme, it's perfect to just use it all the time, um, so that you become aware of the, the, the gaps.
[1247.22 → 1249.68] You know, when I'm coding, I prefer a dark theme as well.
[1249.80 → 1261.46] Um, but I'm also writing a book and when I'm, uh, writing in Markdown large chunks of text for the book, I really prefer a white background or a light background just because it's easier on the eyes when I'm doing, uh, non-coding work.
[1261.50 → 1263.84] How about you when you're writing, uh, for Prorogue?
[1263.84 → 1273.30] Mm. Uh, yeah, I use a light theme as well. Um, when I'm, when I'm writing, uh, pages of text, uh, I, I agree. It just, it just feels, feels better somehow.
[1273.84 → 1283.42] One of the things that, um, the, the chap behind Solarized said, he said, you know, when you're outdoors reading a book, you've got white, uh, white pages with black text.
[1283.58 → 1288.42] And generally you don't go out and sit in direct sunlight. That's, that's normally too bright and too much contrast.
[1288.42 → 1296.54] Normally you'll, uh, you'll try and find a shady spot so that, uh, effectively it lowers the contrast. You end up with the shadow on the page. It's no longer pure white.
[1297.04 → 1304.62] So, uh, one of the principles behind Solarized is to lower that contrast and make it more like, yeah, reading a book in the shade rather than in the, in the bright sunlight.
[1305.12 → 1311.50] So, um, I've, uh, in the last few days I've switched to Solarized, and I've, uh, I've been enjoying it. I like the look of it.
[1311.50 → 1330.20] Um, look at this, uh, light yellow background, which I find quite uplifting. Um, there's, there are a few things that, uh, that don't quite, um, I guess, you know, uh, just a few gaps. Um, but, uh, I guess they'll, they'll be taken care of in time. So.
[1330.20 → 1343.38] So, uh, I think you said something that sounded right to me that like crystallized something that I've been thinking, which is, I think it's easier to get good contrast in a dark, dark colour.
[1343.62 → 1349.42] So when I'm writing code, it actually is important for me to see like that is a variable, that is a class, that is a method, right? That is a string.
[1349.42 → 1357.52] So I want something that enables me to have a lot of colours where, uh, on a light background, you get much better contrast.
[1357.52 → 1366.20] So it's good for like writing big blocks of text, like if I'm writing a blog post or something, but it's much worse for writing code for me because there's only like a few colours.
[1366.38 → 1372.54] You have to make the call, the text dark, right? So then you're like dark red and dark blue and dark, whatever. Right.
[1372.54 → 1377.24] And, but you can't really have a lot of different colours. And so it becomes less useful.
[1377.24 → 1389.06] So I agree. And I also agree that at conferences, because of the contrast issue, it is like way more important to be able to have your text be readable than to have it be like, this is a string. It is a green.
[1389.90 → 1391.88] Any sprout core plugins for them?
[1392.26 → 1399.86] Someone actually just posted to the mailing list about that. There aren't, uh, again, I, to me, a higher priority than that would be making the JavaScript one's work.
[1399.86 → 1406.66] Like there's massive indentation issues. There's some like weird performance stuff, maybe related to JS Lint, but I, I have doubts.
[1407.24 → 1413.82] Um, sprout core itself is very, there are the sorts of the same things that you could do with rails.
[1413.82 → 1424.98] Like I am in a controller now, so I can do certain things, and you can have snippets and all that, but, um, there is enough pain in the Vim JavaScript experience right now that I would, if I was going to spend time on it, I would work on that.
[1424.98 → 1429.66] Um, but I, I think there has been enough interest in it that I think it will probably happen.
[1429.66 → 1432.16] Yeah. Like specifics, sprout core stuff.
[1433.48 → 1444.22] One of the interesting things happening for, for, well, for all JavaScript development, uh, not just in Vim at the moment, you know, the, the guys at Mozilla are behind this, um, what's it called?
[1444.88 → 1451.70] JS C tags, uh, which is, I think it runs on node or, uh, runs on V8 through node.
[1451.70 → 1462.70] Um, and, uh, that allows, well, basically C tags has been around for a long time, and it's got support for a lot of languages, but it's always been terrible at introspecting on, on JavaScript code.
[1462.70 → 1468.68] Cause you know, the, the language is so sort of free and there are so many ways you can define a function and add things to a namespace.
[1468.68 → 1472.80] And, uh, JS C tags understands almost all of them.
[1472.94 → 1476.32] I think it passes most of the tests that I've thrown at it.
[1476.88 → 1479.30] Uh, so yeah, I'm, I'm excited about seeing that.
[1479.30 → 1491.14] Um, uh, I think the way you should think about JavaScript is that every large framework is basic, is its own language because there's no, there is no yet class API in JavaScript.
[1491.14 → 1497.74] So, um, you actually want something that's, that knows that SC.object.extend is a class, right?
[1497.74 → 1502.48] And it's, it's, you could try to introspect like JS.toolkit tries to figure it out.
[1502.56 → 1510.20] But at the end of the day in JS.toolkit, you have to say like scope blah, because it doesn't know that that's a class, and it can only guess so much.
[1510.20 → 1510.44] Right.
[1510.46 → 1521.04] So I, the way I would think I would want there to be a C tags for Sprout core or a C tags for Moo tools because you want something that is like has deeper, you're essentially building a language on top of job.
[1521.04 → 1521.88] It's like Lisp, right?
[1521.88 → 1526.98] Uh, it's like common, it's like clause, uh, what Sprout core or Moo tools or whatever are.
[1526.98 → 1532.10] So you want something that is more than just like, I see a bunch of functions and they're keys.
[1532.10 → 1533.28] So probably that's a class.
[1533.36 → 1536.56] Maybe you want something that knows what Sprout core is.
[1537.48 → 1543.60] So we had Ilya Gloria on the show recently and told him that we're going to be talking about Vim.
[1543.72 → 1546.90] So, um, he reminded me of his excellent site, Vim Golf.
[1546.90 → 1551.56] So wanted to throw it out there and see if you guys have used Vim Golf and maybe what your high scores are.
[1553.00 → 1553.96] Yeah, I've used it.
[1553.96 → 1555.70] Um, I'm not very good at it, actually.
[1556.76 → 1560.32] Uh, I think it's an amazing site.
[1560.32 → 1575.46] I, um, I haven't, uh, dipped into the source code to find out how he's done it, but it just, uh, it just kind of strikes me as magic the way you just, uh, fire it up and it, uh, tracks all your keystrokes and, and reports them back to his, uh, his web services.
[1575.46 → 1576.58] It's, it's brilliant.
[1576.58 → 1577.12] It's great fun.
[1577.32 → 1581.14] And I've, I've learned a lot from seeing the way other people tackle these problems.
[1581.82 → 1584.46] So I actually, I actually, sorry, proceed.
[1585.40 → 1585.76] Yeah.
[1585.80 → 1592.52] Oh, I was just going to say, just like, just like, you know, code golf, you end up doing things that you would never do ordinarily.
[1592.52 → 1597.22] Um, and I think sometimes minimizing the number of keystrokes, uh, I don't know.
[1597.34 → 1600.28] You have to think really hard about coming up with a good Vim Golf solution.
[1600.94 → 1612.02] Um, uh, whereas I think in general day-to-day usage, you just want, you just want your fingers to act on, on, um, on your thought and for the thing to happen.
[1612.02 → 1614.48] And I, I don't really care if it takes five keystrokes instead of three.
[1615.02 → 1621.06] Um, it, it's more important for me that it's repeatable, um, with the dot command, for example, or, or something like that.
[1621.12 → 1626.82] So, uh, um, I've definitely, definitely got entertainment from it, and I've, I've picked up a few tricks.
[1627.44 → 1637.50] Uh, but I think, uh, when you look at a solution that someone uses, it's, it's very much kind of influenced by the golfing mindset of trying to minimize your keystrokes.
[1638.14 → 1639.92] Uh, it's probably not something you do in the real world.
[1639.92 → 1642.70] Yeah, I, I sort of have the same approach to coding.
[1642.82 → 1653.34] I, I have so much available RAM before I start swapping in my brain and trying to remember more than a few key combinations is, is not, doesn't work for me.
[1653.40 → 1655.30] It basically makes me a worse coder.
[1655.66 → 1659.50] Um, so to the extent that I can like to get muscle memory, that's great.
[1659.50 → 1664.40] And that those things are very, very important to the extent that I have to be like, how do I do that thing again?
[1664.88 → 1669.36] Um, that, that actually is worse for me than just like doing it longhand.
[1669.36 → 1673.26] And I will often do things longhand or like to get into a pattern.
[1673.26 → 1677.88] Like I use, um, visual block mode a lot because I know how to do it, right?
[1677.88 → 1678.72] I know how to use it.
[1679.02 → 1686.34] And even though I'm sure like every time I do it, somebody's like, oh, you can actually just type in like these five keystrokes, and it will do the whole thing you just did in 10.
[1686.40 → 1691.92] And it doesn't like, I don't, I don't have the space in my brain to remember all those things, which may be me.
[1691.96 → 1693.84] This is why I don't think I'm a Vim expert, actually.
[1693.84 → 1699.58] Um, and I, I also, I'm not very good at Vim golf and, but I'm, I actually hadn't looked at it in a while.
[1699.58 → 1707.46] And I see he added your ability to see other people's answers, which was not there in the initial release, which makes it more interesting to me in general.
[1707.46 → 1719.24] It's almost like a refactor my code, but, uh, you know, as you said, some of these, um, solutions get a bit esoteric, but I guess as long as it's your own process, it's not that bad.
[1719.24 → 1731.14] You know, sometimes, uh, less is not, uh, more when it comes to code, like in Ruby inline procs and things sometimes get a bit, you know, hard to read if you don't exactly know what's going on under the hood.
[1731.24 → 1733.74] But for keystrokes, I guess you're the only one consuming them.
[1733.96 → 1734.32] Yeah.
[1734.36 → 1739.32] And I think, uh, in particular, I think it is probably the case that it's a very personal thing.
[1739.32 → 1742.94] I think people who are like, you should do, you know, you should use this code motion.
[1744.20 → 1752.40] I, I think different people have a different tolerance for memorization and also a different, a different amount of utility from repetition.
[1753.10 → 1755.28] So Vim is nice.
[1755.34 → 1756.60] It gives you a lot of tools.
[1756.76 → 1759.28] It's, it's very much like Ruby and not Python in that way.
[1759.32 → 1760.64] It gives you like a million ways to do it.
[1760.94 → 1765.34] And I, I feel as long as you're productive in it, you're happy.
[1765.50 → 1765.90] It's good.
[1765.90 → 1769.80] I guess I should ask your favourite terminal that you're running Vim in.
[1771.78 → 1774.50] I use ESH, but I use Mac Vim.
[1774.94 → 1777.12] So, I mean, not your shell, but, uh, you're using Mac Vim.
[1777.22 → 1777.36] Yeah.
[1777.36 → 1779.48] You're not using a term or a built-in terminal.
[1780.08 → 1780.48] No.
[1780.58 → 1788.90] And I, I actually, uh, so again, I think this makes me a heretic, but I, I like, I like hitting Apple S to save things.
[1789.36 → 1793.26] Um, so I, I, I of course know how to do the other, the right way.
[1793.26 → 1793.52] Right.
[1793.52 → 1799.36] But, um, I actually like, this is sort of an answer to the like 1960s browser thing.
[1799.36 → 1799.60] Right.
[1800.38 → 1806.60] I think Mac Vim actually solves a bunch of things that are kind of annoying about Vim for day-to-day usage.
[1806.60 → 1808.04] And so I like it.
[1808.06 → 1810.88] And I tend to not just be like, oh, I guess I'm in the terminal.
[1810.96 → 1812.80] I can just type in Vim, and now I'm in Vim.
[1812.80 → 1814.50] I tend to want to use Mac Vim.
[1815.78 → 1816.96] So that's actually a great point.
[1817.06 → 1819.58] I work with Nathan Smith, the 960 grid system guy.
[1819.78 → 1825.12] And, uh, so one of the things that we were talking about in moving to Vim, because a couple of guys on the team are, are Vim guys.
[1825.12 → 1833.06] And he said, you know what, then what I do with my, uh, OCD command S twice on every, every time I want to reload and save the page.
[1833.06 → 1834.60] So I guess we have an answer for him.
[1835.32 → 1835.70] Mac Vim.
[1836.52 → 1844.88] I figure there's like, I guess that there's utility in memorizing or, or knowing that, or having a muscle memory of colon W.
[1844.88 → 1849.78] But I already have like 20 years of muscle memory on Apple S.
[1849.88 → 1855.90] And I really don't see the utility of memorizing that and memorizing a different thing for Vim specifically.
[1856.76 → 1858.46] I would second that, actually.
[1858.84 → 1859.36] Exactly.
[1859.58 → 1862.86] I, um, uh, I think Vim is very much set up.
[1863.18 → 1871.48] Uh, it encourages you if you are creating your own mappings, it encourages you not to use, um, modifier keys like the command key and the control key.
[1871.48 → 1880.84] Uh, but I think there are cases where, um, it's much better to do that, particularly, uh, well, the example of hitting command S twice.
[1881.50 → 1888.00] Um, anything where you need to do something many times, I think it's much better to create, uh, a mapping that uses a modifier key.
[1888.12 → 1892.88] One, one that springs to mind that I use actually is, uh, you know, when you press J, it moves you down a line.
[1893.62 → 1898.48] And normally you would expect it to move down a display line, but Vim always moves down by a numbered line.
[1898.48 → 1908.44] So if you have, um, a long paragraph that's wrapped, say it's, it's five lines long, and it's wrapped, and you press the J key, it'll move you down to the line below rather than moving you down.
[1908.82 → 1910.00] So I'm not describing that well.
[1910.04 → 1915.22] It'll move you onto the blank line below the paragraph rather than moving onto the line of text below the line of text.
[1915.32 → 1919.18] It's especially bad if you have, if you're like writing paragraphs of text.
[1919.18 → 1922.74] Yeah, it's, it's quite, quite infuriating.
[1922.92 → 1931.06] And the, the Vim, um, it, it does have the option to let you move down by a display line rather than a numbered line, but you have to hit GJ.
[1931.74 → 1936.94] And I find that if I needed to move down five, uh, five lines, basically that's 10 keystrokes.
[1937.06 → 1938.62] It's GJ, GJ, GJ, GJ.
[1939.14 → 1941.26] Um, hammering, it's like doing a drum roll.
[1941.26 → 1947.24] And I find it really easy to accidentally hit GJ or, you know, it's just, it's really easy to mess up.
[1947.30 → 1948.86] And in that case, um, I've got it set up.
[1948.92 → 1954.12] So I just hold down command and hit J, and it does the, the display lines rather than the numbered lines.
[1954.24 → 1966.36] So that's, that's one case where I think the, the Vim, um, custom of always, always typing, um, typing something that sounds like a word rather than doing a modifier key mapping.
[1966.84 → 1970.32] I think that's one case where it's much better to use a modifier key.
[1970.32 → 1977.86] Another one I, another one I use a lot is I, there's a port of the text mate indenting and out denting blocks of code thing.
[1978.00 → 1984.58] So instead of doing double right angle, you do command right bracket.
[1984.92 → 1987.54] I don't, I can't say this out loud at all.
[1987.68 → 1988.32] That's horrible.
[1988.58 → 1993.82] But, um, so I, for the first like two months I used Vim, I didn't know about it.
[1993.82 → 1997.06] And I was just using the bracket, the angle brackets and I got good at it.
[1997.06 → 1999.42] Like I'm reasonable, especially once I learned about period.
[1999.42 → 2005.02] But there, it's actually not, like, it's annoying that when you do that, you like to lose what was highlighted.
[2005.32 → 2006.56] Often you want to do something with it.
[2006.74 → 2009.56] And I just like how the text mate one works better.
[2009.76 → 2011.82] And of course you can implement it in Vim and it is.
[2011.90 → 2013.10] So I just, I use that a lot.
[2013.74 → 2018.44] And yeah, I basically, I feel like the wrong case for modifier keys is when you're in certain mode.
[2018.76 → 2021.44] In insert mode, modifier keys are just like craziness.
[2021.44 → 2026.22] But in move mode and like a visual block mode, it's good.
[2026.90 → 2030.58] Tim, you have a favourite set of modifier keys or tricks?
[2031.72 → 2034.16] Um, I'm kind of a curmudgeon in that regard.
[2034.34 → 2040.54] I've, I've, I've got a few, I mean, basically stuff I've learned since switching, switching to a Mac.
[2040.54 → 2047.60] So like when I, when I run my test, I hit command R, but I learned colon W about 10 years ago, and it's so hardwired now.
[2047.90 → 2048.30] Yeah.
[2048.34 → 2049.62] So that's, that's actually what I mean.
[2049.64 → 2053.96] I think like it's good for everyone to have their, their own muscle memory.
[2053.96 → 2065.96] I think, I actually think it's bad for the Vim community to be like, I guess there's not really a Vim community, but it's bad for like people who are helping people learn Vim to be like, you have command colon W.
[2066.06 → 2066.94] That's how you have to do it.
[2067.02 → 2068.80] Or like whatever the things are.
[2068.98 → 2076.42] I think it's better for people to learn their own path because everyone's different, which makes me sound like a hippie, but that's not really what I mean.
[2076.98 → 2080.60] Anybody use VI mode for their terminal when they're just messing around the shell?
[2081.02 → 2082.64] I can't stand VI mode.
[2082.64 → 2082.92] Yeah.
[2083.72 → 2084.12] Yeah.
[2084.22 → 2086.64] Without, without, I mean, I don't get anything I like from Vim.
[2086.68 → 2087.70] I don't get a colon line.
[2087.78 → 2088.86] I can't colon S anything.
[2089.32 → 2090.92] I can't even tell which mode I'm in.
[2091.14 → 2091.32] So.
[2091.86 → 2092.00] Yeah.
[2092.04 → 2093.44] The only thing is I get confused.
[2093.44 → 2098.60] So I learned all the Emacs combos, not from Emacs, but from Bash.
[2098.74 → 2103.98] And so I'm like pretty used to them and, but I'm losing my muscle memory from them because I use Vim so much now.
[2104.36 → 2107.78] Where before TextMate is like very Emacs-y in terms of key combinations.
[2108.62 → 2110.22] So it's just sometimes weird context.
[2110.22 → 2113.80] I've actually mapped those in insert mode and command line mode in my Vim.
[2113.90 → 2114.86] That's my habit.
[2114.96 → 2118.48] I still have control B and control F, control A, control E.
[2118.58 → 2122.16] Those I use regularly in Vim.
[2122.16 → 2128.16] How would the world be different if DHH's original Rails screencast had been done in Vim?
[2128.16 → 2135.06] I think TextMate has a property of being like zero seconds to pick up like Rails, actually.
[2136.38 → 2141.90] And I think Vim is like, we see a lot of adoption now because Rails is maturing.
[2142.54 → 2146.02] So there's like, I don't think that many people actually use Vim.
[2146.28 → 2148.16] Like let's say there's two million Rails developers.
[2148.52 → 2151.48] I don't think like any noticeable percentage of those people actually use Vim.
[2151.48 → 2158.70] But I think among the people, like the growing up maturing community of Rails, we're like moving into more mature tools.
[2158.70 → 2165.68] So Yehuda is, you know, his reputation comes from being on the core team of Rails and jQuery.
[2165.94 → 2173.74] And Tim, the outcry on Twitter when I put out the call for Vim guys was great with your screen name.
[2173.96 → 2177.70] I guess you may have a Vim tattoo or something or maybe just your plugins that you have reputation.
[2177.70 → 2184.88] But I wanted to know, Drew, does every Brit just automatically go into voiceover and screencast work?
[2185.00 → 2189.04] I mean, how does your accent translate into street cred?
[2191.56 → 2194.04] It's been quite surprising to learn that people like my voice.
[2195.94 → 2199.84] I mean, just like everyone, I don't like my own voice.
[2199.98 → 2203.52] You know, when I hear it coming back to me, I'm like, well, do I sound like that?
[2203.52 → 2207.90] But, yeah, it's quite strange.
[2208.06 → 2213.80] People seem to like my voice, which I guess is good.
[2214.16 → 2216.94] And I'm just trying to make the most of that by doing more screencasts.
[2217.12 → 2222.26] So I guess the reason I got into screencasting is that I love teaching.
[2224.28 → 2227.28] And it's a good way to reach an audience.
[2227.28 → 2237.92] And I really, I don't know, I really enjoy it when there's something that's difficult and which, you know, you invest some time getting your head around it,
[2238.48 → 2244.32] communicating that to people who haven't invested that time, making it easier for them to reach that point of understanding.
[2244.50 → 2245.56] I get a real kick out of that.
[2245.68 → 2248.92] So I do it because I enjoy teaching.
[2249.04 → 2251.00] I think that's the main reason.
[2251.00 → 2254.78] And Vim is such a it's famously difficult to pick up.
[2254.94 → 2258.52] And so there's a lot of meat there for me to get into.
[2259.62 → 2262.64] I'll put you guys on the spot real quick with a couple of closing questions.
[2262.78 → 2274.36] So first, any command line hacks or other tool chain tips that you'd like to share with our listeners as far as creating code?
[2274.36 → 2278.26] One stupid simple one that I was reminded of earlier.
[2278.66 → 2286.30] I don't like VI bindings in the command line, but you can bind, I think it's bound by default in Bash, and I've bound it in Z shell as well.
[2286.76 → 2290.18] Control X, control E to open an editor to edit the current command line.
[2290.34 → 2298.90] So if I'm trying to do something a little fancier when editing and I want a real editor, I use that fairly regularly.
[2298.90 → 2306.82] So I actually find it somewhat surprising that Ruby minus E and associate like Ruby minus P are not more commonly used.
[2307.78 → 2310.14] Half of why people use Perl is because of those things.
[2310.34 → 2313.12] And Matt's like dutifully copied the exact API from Perl.
[2313.70 → 2317.32] And so I am often like piping things to Ruby minus E, blah, blah, blah.
[2317.74 → 2319.70] And I think I may be the only one.
[2319.90 → 2324.90] Like when I found out about minus P, which is like a printing thing, I was surprised.
[2325.72 → 2328.64] Like I had never heard of it and I like asked people about it and nobody knows about it either.
[2328.64 → 2336.62] So I would just say like if you're going to use grew, and you're like, oh, I don't really know that API, you know Ruby's regular expression syntax.
[2336.80 → 2337.84] So just use Ruby minus E.
[2338.14 → 2338.62] It's fine.
[2338.82 → 2339.44] It will work great.
[2340.36 → 2344.14] I've got one not for the regular command line, but for Vim's command line.
[2344.30 → 2347.06] Lately I've been using more and more the control R.
[2347.88 → 2349.98] Opens up the next key that you press.
[2350.14 → 2352.94] It'll paste from the register of the key that you press.
[2353.52 → 2355.44] So I've been using this more and more lately.
[2355.44 → 2362.12] So you can, in particular, if you do control R slash, slash is the register that contains your last search pattern.
[2362.46 → 2364.06] And I've been finding that really useful lately.
[2364.26 → 2368.52] So the other one is control R, control W will paste the word under your cursor.
[2369.56 → 2374.06] I just really, really been enjoying that lately.
[2374.86 → 2375.26] Neat.
[2375.26 → 2377.76] One last question.
[2378.72 → 2380.04] And this is really going to put you on the spot.
[2380.76 → 2381.80] Who's your programming hero?
[2383.52 → 2385.96] So I think Max is underrated or maybe not.
[2386.04 → 2388.04] Maybe he's, he's rated well.
[2388.04 → 2396.00] So I, Max, there are a bunch of things that Max had written and was interviewed on circa 2003.
[2397.32 → 2400.82] I keep meaning to like to put a blog post up that has a list of them.
[2401.26 → 2406.88] But Max around that time, like elucidated a lot of things about Ruby.
[2406.88 → 2412.82] And some of them are like, he says like optimize for programmer happiness or like for humans or whatever.
[2413.14 → 2414.82] And I think it's like a catchphrase now.
[2414.90 → 2416.28] People who know Ruby now know it.
[2416.38 → 2418.62] But he actually enumerated exactly what it means.
[2418.84 → 2424.28] And I, I found the way he talks about it to be very useful for designing other things.
[2424.28 → 2426.22] For like working on Rails or Sprout core.
[2426.32 → 2427.68] Like how should you think about the problem?
[2428.18 → 2430.14] And I, I do think he's underrated.
[2430.14 → 2435.64] I guess I'll have to go with Linus Torvalds.
[2435.76 → 2437.52] I mean, he's changed my life twice over an hour.
[2437.62 → 2438.92] First with Linux, then with GID.
[2439.02 → 2441.16] It's just, when does he start?
[2444.40 → 2445.86] I don't know if I have a hero.
[2451.14 → 2452.08] It's okay to say no.
[2452.14 → 2457.26] The reason I start asking that question is because it's just one of, our field changes so fast.
[2457.26 → 2466.20] And it's one of those things where, you know, baseball players and other occupations have someone to look up to even from an early age.
[2466.42 → 2473.84] And, you know, computing is one of those things that sometimes you get into later in life, and you really don't have that role model as you come up through the ranks.
[2474.34 → 2479.46] I think it's still plausible to like have Kernighan and Ritchie as role models.
[2480.00 → 2486.56] People who were role models in the 60s are still very relevant.
[2487.26 → 2488.26] Indeed.
[2488.94 → 2489.70] Well, thanks, guys.
[2489.86 → 2491.18] Appreciate the time.
[2491.26 → 2496.62] And I know that I'm continuing on my own personal discovery with Vim as a lot of the listeners are.
[2496.74 → 2499.18] And so hopefully we're smarter for it.
[2499.62 → 2499.96] Awesome.
[2500.16 → 2500.84] Thank you very much.
[2500.84 → 2514.02] We'll see you next time.
[2514.06 → 2514.12] Thank you.
[2514.26 → 2514.54] Music.
[2514.54 → 2518.22] notify you.
[2518.22 → 2519.76] Music.
