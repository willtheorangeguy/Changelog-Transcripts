[0.00 → 18.80] vim the final frontier sorry that's so lame I've just always wanted to do that lets run it back
[18.80 → 29.54] vim a modal text editor from 1991 with roots in vi that go back to 1976 that's 45 years ago and
[29.54 → 35.84] yet here we are in 2021 30 years after vim's initial release, and it's still used and loved by
[35.84 → 40.68] nerds around the world you can't even really call it a comeback because it's been popular for years
[40.68 → 47.28] on this special episode of the changelog we thought it would be fun to hear a bit of vim's story from
[47.28 → 53.60] the mouths of its users so i gathered some friends new and old and asked them to tell me all about vim
[53.60 → 58.96] and why they love it thank you to our friends at source graph for partnering with us to make this
[58.96 → 65.10] episode interruption free teams with large code bases and many repos struggle with the usefulness
[65.10 → 70.54] that grew and command shift f offer they need a better way to search and discover all their code
[70.54 → 75.70] and open source dependencies they need source graph point source graph at the repos you work with
[75.70 → 82.28] stored in any code host then start searching stay in flow and find your answers quickly try source graph
[82.28 → 89.04] at info dot source graph dot com slash changelog all right let's meet our guests starting with Julia
[89.04 → 97.76] Evans I'm Julia I've been using vim for i think 17 years and i am a programmer and i currently for a
[97.76 → 104.00] living write comics about programming hi I'm drew Neal you may know me as the voice of vim casts i also
[104.00 → 111.50] wrote practical vim and modern vim and aside from my sort of vim work I'm a web developer by day and i
[111.50 → 117.46] also do um uh sort of related to all the vim casts and books and so on i do training sessions about vim
[117.46 → 123.82] so um I've been using vim since about 2008 something like that i think I'm Gary Bernhardt the thing people
[123.82 → 128.78] are most likely to know me from is a lightning talk called was which is almost 10 years old now
[128.78 → 134.28] right now I'm working on execute program which is an interactive learning program that's kind of
[134.28 → 139.94] unique in that we mix lots of real code examples in with explanations all running in your browser
[139.94 → 145.42] real code examples in the browser I've been using vim for about 15 years since 2006 i was an Emacs user
[145.42 → 150.20] before that and then before that you know Visual Studio and sort of more mainstream windows kinds
[150.20 → 155.04] of editors and i also went back and forth between Emacs and vim a number of times in the early days so i
[155.04 → 159.52] have a lot of sorts of comparison reference points there I'm sub Hinton i do software development
[159.52 → 166.62] professionally and also in my spare time as a hobby i most frequently work in Golang ruby JavaScript but
[166.62 → 171.62] i kind of like to do a little bit of everything from the top of the stack right down to almost the
[171.62 → 177.92] bare metal not quite assembly and i switched to using vim around four years ago one thing that has
[177.92 → 184.94] always fascinated me is how people come to select their tools techniques programming languages and so on
[184.94 → 190.64] as a developer your text editor is one of the most important choices you make because you use it all
[190.64 → 197.20] day every day it is the primary interface to the work that you do i learned vim not because i chose to
[197.20 → 203.52] but by dictate my programming teacher in college was a staunch vim proponent and forced us to write
[203.52 → 209.68] all of our programs shed into a Linux machine using vim i kind of hated him for it at the time but i
[209.68 → 214.78] definitely appreciate it in retrospect shout out to john Clark if he's out there listening i
[214.78 → 219.64] remember him once saying PICO is a totally fine editor if you're writing emails to your grandma
[219.64 → 226.34] if you're writing code you better be using vim so that is how i came to know vim here's how drew got
[226.34 → 233.66] started switching jobs i was at a job where we all used max and back than uh we were a rails shop and
[233.66 → 240.00] everyone was using TextMate and i switched to a job where it was all Linux workstations and TextMate
[240.00 → 244.48] didn't run on Linux so i had to pick another editor uh i think the ones i was considering at
[244.48 → 251.48] the time were Emacs vim and edit i think and yeah i think um it was a small company, but there were a
[251.48 → 255.72] fair few vim users so i thought well if i start using vim I've got a few more people i can ask
[255.72 → 261.52] questions of so that was kind of what got me into vim and i knew at the time i was aware that vim had
[261.52 → 266.14] perfect support for rails which is what i was mainly working with at the time mainly thanks to
[266.14 → 271.92] Tim pope who created the rails. Vim plugin way back um so in some ways that was sort of the
[271.92 → 277.02] gateway drug to vim coming from a rails background i think vim was quite, quite popular
[277.02 → 281.94] with rails developers at the time so it kind of felt like a natural step it's funny how the social not
[281.94 → 288.42] social pressure but just like the social environment around you helped make that decision yeah yeah that's
[288.42 → 293.26] true i mean i could have moved to a job where there were i don't know five Emacs users and
[293.26 → 298.68] two vim users and uh it would have worked out differently we'll be all watching Emacs casts yeah
[298.68 → 305.48] while drew's experience may be somewhat common Gary came to vim from a completely different angle
[305.48 → 312.30] and while i hadn't considered it before i have to say it's a compelling reason for me and i don't know
[312.30 → 320.94] how common this is but for me, it was motivated by fear of RSI injury programming long term is dangerous
[320.94 → 325.62] for your hands fortunately not the rest of you for your hands and your wrists totally dangerous and
[325.62 → 330.62] i wanted to keep programming for many more decades so i was using Emacs a lot of cording in Emacs a lot
[330.62 → 338.02] of control shift control alt shift and vim has basically none of that and that for me is the
[338.02 → 342.48] most important difference between vim and other editors it's input efficiency in terms of keystrokes
[342.48 → 348.64] and a really easy way to sort of see a summary of that is in vim i almost never hit control
[348.64 → 353.46] i never hit alt if there are keystrokes that require alt i don't even know them and i rarely
[353.46 → 360.52] hit shift, so most of my editing is normal mode which is the mode that vim boots up in and just
[360.52 → 366.40] hitting the letter keys to do things in punctuation and that is very different from any kind of remotely
[366.40 → 372.02] quote-unquote mainstream editor did you know that going into it or did you do someone say vim's great
[372.02 → 378.16] for RSI or how did you know that uh i had a bit of a scare is what caused me to take that path and
[378.16 → 382.32] it turned out i think honestly i probably just overused a muscle or something it was sore which
[382.32 → 386.78] is a common yeah way to think you have RSI when you don't um so that went away, but you know having
[386.78 → 392.42] had that scare i thought if that was is that was my RSI coming in permanently it would change my life
[392.42 → 397.06] right i mean it's its a major thing so i decided to do something about it and vim is what i did
[397.06 → 402.02] Julia has been using vim for so long that she couldn't even remember what initially drew her in
[402.02 → 407.60] sub was also well aware of the editor for a while, but she only dove in somewhat recently I've always
[407.60 → 414.50] sort of messed around with rented Linux VPS's and when it's your own box you tend to do all the dodgy
[414.50 → 420.50] stuff you know like you do all the cowgirl stuff on the servo like you modify your nginx config live
[420.50 → 425.32] and things like that and usually that's done in a shell session so really the most practical
[425.32 → 430.52] options that you have are something like NATO or Max or vim or vi, and it's installed out of the box
[430.52 → 436.10] on so many Linux machines and so it's just always there and so usually i would pick it up if i needed
[436.10 → 440.80] to use it, and it was usually within that that context of just like messing around in Linux without
[440.80 → 446.80] some kind of display drivers or GUI to be honest nothing about the experience itself made me want to
[446.80 → 452.32] pick it up you know i knew how to go into insert mode and get out of insert mode and sometimes
[452.32 → 456.94] depending on the machine you could actually get away with using the arrow keys instead of j and k and
[456.94 → 461.98] things like that I'd been curious and felt that it was valuable to learn properly and i knew other
[461.98 → 466.92] developers and colleagues who used it but i just never really felt motivated enough at the time which
[466.92 → 471.64] is why i really only picked it up four years ago sub said something interesting there that i heard from
[471.64 → 478.06] others as well she said it's installed out of the box on so many Linux machines it's just always there
[478.06 → 482.74] that is definitely a strength, and it turns out it's one of the things that sub loves the most
[482.74 → 487.94] about vim because of the ubiquity you end up in the scene from Jurassic Park where it's like this is
[487.94 → 491.68] i know this and so you know if you have to do something really quickly on a Raspberry Pi or
[491.68 → 495.20] something you're just like oh i I know this I can just do this really quickly and women it's great
[495.20 → 499.76] and so that's the dream what I also like about it is that because it is on everything it can be as
[499.76 → 505.02] simple or customized as you like the biggest sort of personal virtue for me about it is that
[505.02 → 511.20] I have a terrible short-term memory find it very difficult to hold a buffer in my head of like
[511.20 → 515.32] what code I need to write next sometimes I have to pseudocode things out just so I remember the
[515.32 → 519.50] steps of like what I'm doing if it's complex and even just changing your mind about something and
[519.50 → 524.02] rewriting it getting the code out of my brain and onto the screen in front of me like as fast as
[524.02 → 529.36] possible actually really helps me not be so overloaded, and it's actually far less exhausting for me
[529.36 → 537.58] and because vim is designed to train your muscle memory to do very efficient you know shortcuts to
[537.58 → 542.64] make changes in your code it is very targeted towards that as compared to kind of clicking around
[542.64 → 547.32] with a mouse or just having like maybe some a smaller amount of shortcuts it's designed in a way to just
[547.32 → 552.76] help you achieve that much faster and I'm not really one of those productivity porn people but when
[552.76 → 559.04] you pitch it in the case of just finding coding far less frustrating it's been hugely valuable for me in that
[559.36 → 564.54] I guess one of the things I love most about it is the grammar the um slightly funky way of doing
[564.54 → 570.14] things where like in most text editors you select some text usually by like clicking with the
[570.14 → 575.66] mouse or double-clicking or whatever and then having selected the text you then run some operation on it
[575.66 → 580.22] whether that's just deleting it or wrapping it with something or whatever whereas in vim it's kind of
[580.22 → 584.02] the other way around you start by saying I'm going to delete something, and then you say what you're going
[584.02 → 588.60] to delete so it's a little bit back to front, and it very much feels like a grammar it's like
[588.60 → 594.34] you know you have in spoken languages you have ways that you can assemble you know the verbs and
[594.34 → 600.26] the nouns and so on and with vim you have these operators and these motions and I just love the
[600.26 → 605.18] fact that there's sort of an infinite space of combinations I love the fact that you can install
[605.18 → 610.58] install plugins that add new operators or that add new motions or new text objects and I always feel
[610.58 → 614.70] like that's kind of like we've got our fixed grammar, and it's just like we're adding vocabulary
[614.70 → 620.74] further expanding the space of operations that can be performed vim is complicated there's a lot of
[620.74 → 626.84] stuff in there but the thing that makes vim is normal mode the letter keys do things without
[626.84 → 632.80] modifiers it's such a simple thing but everything that is sort of special about vim for me stems
[632.80 → 638.94] directly from that when you first open up a file with vim typing on your keyboard won't insert any
[638.94 → 644.30] characters that's because you're in normal mode like Gary was talking about normal mode is for doing
[644.30 → 650.72] non-character insertion things moving your cursor copying and pasting lines manipulating text that's
[650.72 → 655.34] already there normal stuff like that if you want to insert characters you have to switch to insert
[655.34 → 661.38] mode this causes confusion to new vim users because it's backwards from what's expected it can make you
[661.38 → 666.38] feel dumb because here you are in a text editor, and you can't even get the thing to edit any text
[666.38 → 671.20] but it is one of those things that makes vim and once you grok it, it actually makes a lot of
[671.20 → 676.54] sense drew struggled with this concept like most of us do, but he came up with a great analogy for vim's
[676.54 → 680.82] different modes that may help you make more sense of it the point where it starts to make sense really
[680.82 → 687.60] is when you accept the modal nature of vim and for me, I feel like the point where it started making
[687.60 → 694.46] sense was kind of where I started to see those trips into insert mode and back out again as being well I draw
[694.46 → 699.96] an analogy with the way a painter works I like to compare normal mode which is the default mode in
[699.96 → 704.44] vim as being just like a painter with you know their paintbrush not touching the canvas whereas
[704.44 → 709.84] in insert mode it's like your paintbrush is touching the canvas and if you think of every little trip into
[709.84 → 714.76] insert mode as being like a brush stroke then that sort of modal nature starts to really make sense
[714.76 → 720.42] and a couple of things that made that make sense to me was one realizing the way the undo command works
[720.42 → 725.96] you know if you make a trip into insert mode you type some text you pop back into normal mode that's
[725.96 → 732.38] one little undoable chunk of work whereas in most text editors where you're generally in something
[732.38 → 739.56] like insert mode you can type like one word, or you can type a sentence, and then you can hit the undo key
[739.56 → 746.88] and how much text it's going to raise is a little bit of a don't quite know it's like fuzzy yeah it's
[746.88 → 751.28] fuzzy there's its a little bit like having some sort of auto save feature that says okay every time
[751.28 → 755.74] you've paused for more than two seconds we're going to auto save a similar sort of idea where if you've
[755.74 → 760.72] paused for a certain amount of time maybe we'll put in a little undo stop or wherever you call it and
[760.72 → 765.16] some text editors don't do that at all you just hit undo, and it'll undo everything since I don't know
[765.16 → 769.28] you moved your cursor or something like that and at that point where i sort of realized okay I'm kind of
[769.28 → 773.76] thinking about this as like little chunks of undoable changes, and it really started to feel like brush
[773.76 → 778.36] strokes, and it started to feel like the idea of being in insert mode by default just felt wrong
[778.36 → 782.42] it's like well of course the painter doesn't have their paintbrush touching the canvas all the time
[782.42 → 787.58] that's just weird so having that sort of um being able to think in modes just made everything feel
[787.58 → 792.24] natural and from there I mean at that point you've still got a lot of vim to learn but at least your
[792.24 → 798.26] sort of patterns of thought are aligned with vim's ways of making you do things normal mode and insert
[798.26 → 804.24] mode aren't the only modes in town vim's visual mode is great for selecting multiple characters
[804.24 → 811.00] lines or blocks of text and then performing some operation on that selection I love visual mode I use
[811.00 → 816.32] it all the time and so does Julia yeah I love visual mode one of my favourite things about visual mode
[816.32 → 821.24] is do you know how you can go into visual mode and then do like colon exclamation mark and then type
[821.24 → 827.40] Unix command, and it'll pipe the stuff you selected into that command and then replace it with the
[827.40 → 833.36] output of the command no I didn't know that I think that sounds spectacular it's spectacular so
[833.36 → 837.10] sometimes I'll have like a list that I want to sort, and so I'll just select it all and do like
[837.10 → 842.70] colon exclamation mark sort, and then it'll sort it in my editor I don't need to go anywhere i I was
[842.70 → 846.68] making some like shell scripts I wanted them to have like fancy headings so like I wrote a python
[846.68 → 852.10] script to generate the headings and then I piped it into the script in vim I don't know I don't use that
[852.10 → 856.78] so often but every time I use it I'm so happy I've never done that I mean I definitely knew about the
[856.78 → 861.42] execution of like a shell script you know from the command prompt but I didn't know you could
[861.42 → 865.64] whatever was selected in visual mode would go into that as an argument that's pretty sweet yeah and
[865.64 → 870.38] that's the joy of vim right is that like all of us use it like you don't you all find out stuff you
[870.38 → 876.66] didn't know another joy of vim is that it's extremely customizable and has inspired a rich
[876.66 → 882.76] plugin community some people really get into plugins I install a lot of plugins I'm not going to lie
[882.76 → 889.94] how many oh I don't know 40 or 50 I think probably more surely there you can whittle down
[889.94 → 893.78] and give me some of your must-haves like what are your favourite plugins what should people be checking
[893.78 → 900.70] out well probably on everyone's list I think is surround. Vim by Tim pope that feels so it feels so
[900.70 → 905.80] impish that i kind of can't believe that it's not the default like core vim feels like that fits
[905.80 → 910.58] very nicely with the whole vim grammar and adds a very useful set of operations for you know
[910.58 → 914.74] deleting surrounding things adding surrounding things changing surrounding things it all feels
[914.74 → 921.48] very impish another one by Tim pope that I use a lot is fugitive which adds like git functionality
[921.48 → 927.26] and I love the way that just gets out of your way it's its there when you need it like if I want
[927.26 → 934.24] to do a git blame I can pull up git blame uh I don't want to have like git blame being sort of echoed on
[934.24 → 939.50] the line that my cursor is on all the time I find that really distracting and annoying yeah i like
[939.50 → 944.52] knowing that I can get to the information and git really easily and fugitive lets me do that here's
[944.52 → 951.04] a really tiny one that i I really enjoy using it's called exchange you can kind of take two pieces
[951.04 → 955.72] of code and just swap them I find that really, really useful it's something i I really miss when I don't
[955.72 → 962.00] have it I really like sort of adding new vocabulary to vim's grammar so uh my favourite way of doing that
[962.00 → 969.62] is by adding like custom text objects and there's a plugin by kana Datsun called vim text user and
[969.62 → 975.00] that's a kind of meta plugin it's like a framework for adding more text objects so if you go to that
[975.00 → 979.92] the GitHub page for that there's a page on the wiki where he links to lots of other custom text objects
[979.92 → 986.32] that people have added and also in the space of like adding vocabulary that fits into the grammar
[986.32 → 992.90] I really miss having an operator for toggling comments uh that's again that's something that's
[992.90 → 997.58] not really built into vim I've tended to use commentary which is again by Tim pope but there
[997.58 → 1001.16] are others out there I'm not sure if that's the best one to use at the moment but again that lets
[1001.16 → 1007.12] you do sort of an operator and then specify like a paragraph or a line or a function or whatever and
[1007.12 → 1013.32] it will comment it or uncomment it I find that really, really useful, but others like to keep it a
[1013.32 → 1019.32] little bit more out of the box I'm actually not a huge plugin user and people do still get kind of
[1019.32 → 1024.18] pushy with me, I made the mistake of sharing my vim RC once on GitHub and somebody pre-requested me
[1024.18 → 1032.78] adding a new plugin and I was like that's just so out of context really weird and very just jarring
[1032.78 → 1036.74] trying to think of a world equivalent of that it's almost like you're at a restaurant and someone just
[1036.74 → 1041.00] walks up and puts some food on your plate or something yeah it's like you'd like this you should you
[1041.00 → 1046.02] should try I really like it exactly have the croissants here put this croissant on your plate
[1046.02 → 1052.70] eat that's fantastic analogy I love that such a weird thing to do yeah, and so I think people
[1052.70 → 1056.64] are like disappointed that you know I don't use a lot of plugins, and they're trying to help so I do
[1056.64 → 1062.08] use some basic plugins and my plugins in my personal time vary greatly from the plugins I use for work
[1062.08 → 1066.94] which is actually a fascinating distinction you know at home I have some basic plugins which are
[1066.94 → 1072.74] nerd tree so that I have a file browser and that's pretty ubiquitously used in the vim community
[1072.74 → 1078.14] um and I have some code syntax highlighters which you know your sort of take for granted that you get
[1078.14 → 1082.40] them out of the box with things like sublime text and stuff like that, but you know if you want something
[1082.40 → 1087.64] specific like JSX for example like vims not going to know what JSX was vim was written a long time ago
[1087.64 → 1092.48] um and so you do have to sometimes install custom things for react and view and like it's an it's
[1092.48 → 1097.38] definitely like a front-end problem right um and I'm assuming rust has the same thing um and then
[1097.38 → 1103.24] what else do I have very small list vim airline and that's mostly just trying to give nice aesthetics
[1103.24 → 1109.10] to my code editor so I'm excited to use it uh, and it is it's its pretty uh functional as well just
[1109.10 → 1113.82] gives you a nice looking status bar um I use git gutter and git gutter essentially it does what it
[1113.82 → 1119.00] says on the tin it gives you sort of get hints and things in the gutter next to your line numbers
[1119.00 → 1123.30] like which lines you've added which ones you've modified which ones are staged stuff like that
[1123.30 → 1129.04] cool so I want something really, really minimal um a lot of people really love vim fugitive which is
[1129.04 → 1133.64] this kind of kitchen sink git plugin right it's like never leave vim and do all the git things
[1133.64 → 1138.26] inside yeah it's amazing and a lot of people really love that paradigm of never leave vim and I get it
[1138.26 → 1141.84] because if you hand it on the keyboard the whole time, and you're not switching context it is actually
[1141.84 → 1147.18] a really nice feeling, but it's just too heavy and i just I can't justify it you know I still like to have
[1147.18 → 1152.50] a separate terminal pain next to me via tmux to like do stuff in there and mess around same so i
[1152.50 → 1156.54] just use git gutter because it's minimal, and it gives me exactly the information that I want to
[1156.54 → 1162.78] know on the fly which is very, very helpful to me and I use Ctrl p as my fuzzy search which uh
[1162.78 → 1166.60] admittedly is not super performant in really large code bases, but it works perfectly fine for me
[1166.60 → 1173.00] personally and then at work I basically run ale which is like hooks into language engines and allows
[1173.00 → 1177.54] you to do things like you know linting within vim and highlighting certain lines that are wrong and
[1177.54 → 1183.08] having explanations as to why um and like auto formatting and that kind of thing so vim ale is
[1183.08 → 1187.68] fantastic because it supports different languages, and it's particularly good with typescript so a lot
[1187.68 → 1193.90] of people at my job we have like a special internal documentation page on getting vim working with all of
[1193.90 → 1199.98] our stuff because VS Code is kind of like the unofficially you know embraced uh editor and they always
[1199.98 → 1206.96] recommend installing ale for that reason so I do tend to run a heavier set of plugins at work just
[1206.96 → 1213.16] because it's just there's more complexity that I deal with in my day-to-day if size's non-work setup
[1213.16 → 1220.12] sounds minimal to you, you might describe Gary's as bare bones I do use a few plugins but I'm also
[1220.12 → 1227.08] firmly on the side of avoiding them as much as you can especially as a beginner what you don't want to do
[1227.08 → 1231.68] is start with 50 vim plugins because then you're not learning vim you're learning this mess of
[1231.68 → 1237.86] plugins it doesn't match you know any other given vim user so today I use exactly eight plugins six of
[1237.86 → 1243.22] those are for language support so very basic stuff like syntax highlighting showing type errors and
[1243.22 → 1248.28] typescript that kind of stuff one of them is my colour scheme so pretty boring and then the eighth one
[1248.28 → 1253.58] is like my one indulgence which is a plugin that slightly tweaks the way that search highlighting works
[1253.58 → 1260.66] but that's it so except language support I'm basically using bog-standard vim with
[1260.66 → 1266.76] the exception to my vim RC which adds a few things the one plugin that I would recommend even a brand
[1266.76 → 1274.18] new vim user use is some kind of fuzzy file finder AZF is a very popular one very widely supported a lot
[1274.18 → 1278.66] it'll be easy to get support I use one called select that I wrote myself you can try that if you
[1278.66 → 1283.04] want I like its matching but of course it doesn't have all the support of something like AZF, but you do
[1283.04 → 1286.28] want something like that if you're coming from another editor, or otherwise you will be
[1286.28 → 1292.46] frustrated Gary mentioned his vim RC if you're not familiar that's vim's configuration file which
[1292.46 → 1297.88] people also tweak to the hilt and often share online for others to take as inspiration or sometimes
[1297.88 → 1305.08] copy whole cloth my vim RC has a section titled basic editing configuration and if you're just
[1305.08 → 1310.50] starting, and you want a slightly more sort of modern take on vim config you could copy just that section
[1310.50 → 1313.80] not my whole vim RC you don't want the whole thing but just the basic editing configuration
[1313.80 → 1321.28] and that will change some of the defaults that are honestly old and not desirable nowadays, but it's
[1321.28 → 1325.78] still pretty small it's under 100 lines including comments I don't actually know what setting in my
[1325.78 → 1330.56] vim RC does this but I know that when I open a file it goes to where I was the last time I was in
[1330.56 → 1336.02] that file like it jumps to my last position and I really love that even like the column in the line
[1336.02 → 1340.76] I think the column definitely the line yeah and maybe the column I'm not so bothered honestly
[1340.76 → 1345.56] sure even if it's not but yeah definitely at least the line and I just love that feeling of like
[1345.56 → 1351.58] if I accidentally close a file and I open it I can just like undo you know even if I already close the
[1351.58 → 1357.30] editor is your vim RC out there so we could link it it's its out there yeah it's really extremely
[1357.30 → 1362.04] based on this thing called basic. Vim which I would probably recommend using over my vim RC because
[1362.04 → 1368.62] mine mostly has extra garbage in it in addition to what's in their like I think basic. Vim is good
[1368.62 → 1372.70] and my stuff just has some nonsense that i added in there
[1372.70 → 1381.64] many vim users will lug their must-have plugins and their personalized config with them to every
[1381.64 → 1386.94] machine they use but that desire to have your vim set up with you wherever you go extends even
[1386.94 → 1394.36] further vim mode is a thing this is where other editors' productivity programs and web apps mirror
[1394.36 → 1399.58] vim's command mode in an attempt to make the vim faithful feel more comfortable in a different
[1399.58 → 1406.16] environment you'll find vim mode in sublime text VS Code and even Emacs then there's Valium a Google
[1406.16 → 1410.78] Chrome extension which lets you browse the web like it's vim and of course web apps like Gmail
[1410.78 → 1419.28] twitter and Trello make extensive use of vim's h j k and l navigation keys some people love it
[1419.28 → 1425.92] others not so much, but it's definitely a phenomenon worth knowing about here's Gary's take on vim mode
[1425.92 → 1432.84] i used a couple of Emacs vim minor modes in the old times so i learned their strengths and weaknesses i
[1432.84 → 1439.02] used some kind of browser vim thing a while back it was I think before Valium found it to be kind of
[1439.02 → 1442.88] buggy because the browser was never designed to do that right and I've tried vim emulations in a few
[1442.88 → 1449.64] graphical editors but all of those it took me only a couple of minutes to hit a number of things that were
[1449.64 → 1454.04] missing you know and that's because i know vim proper so well i want weird stuff like if it doesn't
[1454.04 → 1459.96] have colon g or whatever I'm going to be frustrated now with that said a good vim emulation will get you
[1459.96 → 1465.36] the ergonomic benefits of vim which i think are the most important benefits you will have less risk to
[1465.36 → 1470.88] your hands and your wrists and if you don't know vim proper then you can use an emulation and get
[1470.88 → 1475.54] those benefits and not be frustrated but if you are an expert vim user you're probably going to miss all
[1475.54 → 1480.46] the things that aren't there and when you think about what vim is it makes sense that the emulations
[1480.46 → 1487.56] are always lacking because vim is about 400 000 lines of c code i checked before we started recording and
[1487.56 → 1491.36] it was written over three decades and then there's all the vim script on top of that like that is a lot of
[1491.36 → 1495.96] code it's not just a couple dozen normal mode commands that you can implement in a little
[1495.96 → 1500.74] plug-in and then be done so those couple dozen normal mode commands will get you a lot of the
[1500.74 → 1505.12] ergonomic benefit, but it's still it's not vim and the better you know vim the less that's going to
[1505.12 → 1509.56] satisfy you i know that built into Facebook and built into Twitter because it's built by nerds
[1509.56 → 1514.10] you know you can actually use JK to flip through tweets and like post that's cool i already know how to
[1514.10 → 1518.38] use voiceover on Mac the screen reader because you know i am like a big accessibility advocate
[1518.38 → 1523.20] and that to me is just how you write non-broken software you make it accessible, and you test it
[1523.20 → 1527.22] so to me like I'm much more i think I'm much more productive in that because that's what it was sort
[1527.22 → 1530.46] of designed for whereas i think that a lot of these things are kind of this weird kind of shim
[1530.46 → 1536.06] and it doesn't make a lot of sense vs code feels terrible in vim mode for me, i don't know why i
[1536.06 → 1539.80] think it's just because it's just nowhere near as responsive and so you know you're hitting JK and
[1539.80 → 1544.48] you're just like it doesn't feel the same it feels like someone's kind of pretending and pulling the
[1544.48 → 1548.90] the ropes behind the scenes so um i kind of just abandoned that and i was like if I'm going to use
[1548.90 → 1555.26] vs code I'm going to lead into the vs code paradigm I've used a mode and i think I've used it in vs code
[1555.26 → 1561.36] I've used it in Adam I've used it in sublime I've used it in telly j oh wow and i found it fine like
[1561.36 → 1565.12] because i don't know how to type otherwise like it doesn't work for me, you know
[1565.12 → 1570.94] um so when i use those editors always the first thing i do is i install the vim mode yeah like i liked it
[1570.94 → 1576.38] one thing that i find really charming about vim is like in my email i can do like j and k to go
[1576.38 → 1581.82] between my emails like i think you find like little tiny bits of vim support in like lots of places and
[1581.82 → 1586.10] it feels like you're like a secret club do you know totally like in the club because you just
[1586.10 → 1590.68] like try it out, and then it works, and you're like oh wow, thank you fast mail so i like that's nice
[1590.68 → 1594.82] so that's funny because that's actually a prerequisite for me using a mail app
[1594.82 → 1601.04] is that kind of nav because once i think Gmail did it maybe not first but the first place i felt
[1601.04 → 1606.34] it i was like oh i can actually just use vim navigation to navigate and then i wanted to use
[1606.34 → 1610.94] although i hate Gmail's interface altogether but i like that aspect of it i want to use a native mac
[1610.94 → 1616.10] client or something it's like the built-in mail app for mac can't get it done oh no which makes sense
[1616.10 → 1620.16] like macOS style things, and so i go shopping for these other things and like it has to have like
[1620.16 → 1624.26] that's the first thing i test like can I use j and k to go up and down a list no okay you're not
[1624.26 → 1629.10] going to be my mail client cancel so I'm with you and i feel like remember the milk supported it
[1629.10 → 1633.40] back in the day i mean remember the milk is still around right but like i feel like once i used it
[1633.40 → 1637.68] and it supported it and i was like oh wow like i don't know it is kind of like an insider nerd club
[1637.68 → 1641.64] you're like oh you're one of us you know like whoever writes this is one of us and i like the
[1641.64 → 1647.18] software a little bit more because they like it yeah that's cool one place where i definitely expect
[1647.18 → 1653.96] to have impish key bindings is in Gmail actually uh you can use j and k to navigate up and down
[1653.96 → 1659.08] in your inbox i think it's enter to open even once you're looking at a message you can press j to
[1659.08 → 1663.32] go to the next message or k to go to the previous message i might have that back to front i think x
[1663.32 → 1669.30] will archive a message things like that it's reminiscent of vim definitely inspired by and
[1669.30 → 1673.94] yeah i was setting up a new Gmail account the other day and hot keys weren't turned on and i felt quite
[1673.94 → 1679.30] at sea without them so that is one where i feel i depend on them that's funny because Julia said the
[1679.30 → 1684.32] exact same thing and I'm in the exact same way really so we're three for three on people that
[1684.32 → 1689.42] like vim style navigation in email I'll take it anywhere any website that has it I'm always
[1689.42 → 1693.26] pleasantly surprised I'm like hey you can, you know yeah they do this i think twitter even does it
[1693.26 → 1697.00] although i don't really use it there yeah for some reason i don't feel like a tweet has been selected
[1697.00 → 1700.74] you know I'm just kind of scrolling yeah but i think you can actually select a tweet and go
[1700.74 → 1706.62] JK up and down through them if you so fancy yeah yeah it's always fun to find vim in weird
[1706.62 → 1712.24] places and the more you look, the more you will find vim or things that smell like it all over the
[1712.24 → 1718.84] place but why we've talked about aspects of vim that these four love but i also asked them
[1718.84 → 1725.52] specifically why exactly they think vim is so stinking popular i think that once you start feeling
[1725.52 → 1731.62] the benefits of using vim it becomes very sticky for you, i mean you said that you still juggled the
[1731.62 → 1737.30] two different code editors right and so something changed but you're still hanging on to it and i think
[1737.30 → 1741.58] that actually says a lot um so i think it has that sticky factor once you start using it um
[1741.58 → 1745.88] the pessimistic take on this is that maybe it's some cost fallacy, and you're like well I've invested
[1745.88 → 1749.68] so much in this i don't want to let it go i don't want to like to forget all my shortcuts right that's a
[1749.68 → 1753.28] good take yeah, and it's also the ubiquity as we talked about that seems to be my favourite word for
[1753.28 → 1760.44] this particular recording its persistence as a tool on Unix machines to get work done i like that it's
[1760.44 → 1764.72] just become traditionally part of the toolbox everywhere but even in like a modern context so
[1764.72 → 1769.16] consider like you're booting up a vanilla Raspberry Pi it's a pain in the butt to have to use like
[1769.16 → 1774.62] get a keyboard and a mouse and a monitor and do all that kind of thing and so even just flashing
[1774.62 → 1782.28] Raspbian on a NSW card booting it up you throw it on your network on a switch you shell in, and you're
[1782.28 → 1786.68] writing code right and so you can just like get started with vim, and you're just not conserving a lot
[1786.68 → 1791.92] of resources on things like IOT devices because again it's very performant, and so i think there's
[1791.92 → 1796.40] a lot of modern context for using vim which is why it's stuck around, and it's just nice to not have
[1796.40 → 1802.70] to use like an entire VNC server and like get yourself a GUI in order to boot something up that is
[1802.70 → 1809.02] more of like a modern code editor if that makes sense and then the last thing I will say is that
[1809.02 → 1815.96] you have to admit it kind of still has that really cool like Hollywood hacker movie aesthetic vibes to
[1815.96 → 1821.44] it is right like you feel cool when you're using it because there are those leet connotations around
[1821.44 → 1826.22] it whether that's fair or not fair and so sometimes it just feels kind of nice to just use
[1826.22 → 1830.58] your terminal and not have anything else open right, and you just live in the dream, so this is all very
[1830.58 → 1835.78] opinionated it's not objective in any shape or form, but that's how I feel about it, you know
[1835.78 → 1842.14] vim is the best text editor that anyone ever wrote that was widely used but I mean that in a more
[1842.14 → 1847.04] narrow way than it probably sounds so every editor is going to be good at something right there's a
[1847.04 → 1851.94] reason that every editor was written even like NATO was written because it's small and easy to install
[1851.94 → 1857.32] right if you want to spend your whole career customizing an editor to match you exactly you
[1857.32 → 1861.84] probably want Emacs if you want really deep language support with automated refactorings and debuggers
[1861.84 → 1867.00] and all that you probably want a full-on IDE if you want a text editor that is extremely efficient
[1867.00 → 1872.44] at editing text and maybe not quite as good at some other things as other editors might be then vim is
[1872.44 → 1877.06] the best solution and there's really not any kind of runner-up for editing efficiency unless it's
[1877.06 → 1880.62] something that it looks a lot like vim that's why it's still popular that's why it's been popular for
[1880.62 → 1887.56] 50 years is because it's so efficient and anything that approaches it basically looks like vim has a
[1887.56 → 1892.68] lot going for it ubiquity a powerful grammar that builds on itself it's hackable there's a huge
[1892.68 → 1898.14] community around it, but it's not all rainbows and unicorns I just had to ask these four what
[1898.14 → 1903.64] frustrates them the most about vim what don't they like about it here's drew one of the things I think
[1903.64 → 1909.16] vim doesn't do very well is you know having files that have more than one language in them something
[1909.16 → 1915.70] like a HTML file with uh you know a bit of CSS and a bit of JavaScript mixed in it's quite a common
[1915.70 → 1921.66] scenario these days I mean vim does support it you can have you know you can have JavaScript syntax
[1921.66 → 1927.66] highlighting for the script tags inside a HTML file but I think the way vim has this idea of like
[1927.66 → 1933.44] file type plugins this idea of it's very easy to create a mapping in vim and if you create that mapping
[1933.44 → 1938.94] in a file type plugin you can say okay well this mapping will only be applied to vim if you're editing
[1938.94 → 1944.02] a JavaScript file which is really neat but it kind of forces vim's hand a little bit because when I think
[1944.02 → 1948.50] back to TextMate which I don't know how many people are using TextMate today but I know that
[1948.50 → 1954.90] TextMate got a lot of things right and when I think sublime came out and when VS Code came out they said
[1954.90 → 1960.04] okay well we support TextMate grammars or TextMate themes or whatever it just it's a way of having a
[1960.04 → 1965.22] new editor just suddenly look like it's got lots of plugins already written for it right one of the
[1965.22 → 1969.86] things I remember from my TextMate days is that it has this idea of scopes I think that was the
[1969.86 → 1975.80] terminology it used where it's very much not just looking at the current file but looking at the
[1975.80 → 1980.72] cursor position within the file, and you could have some sort of some sort of command that would
[1980.72 → 1986.98] run, and it would do something differently if it was in a JavaScript scope versus a HTML scope I might
[1986.98 → 1991.68] be misremembering the way that that feature worked, but that was kind of how I remember it and it
[1991.68 → 1996.76] meant that you could have you know a mapping that did one thing if you were in the HTML part of a file
[1996.76 → 2001.08] and a different thing if you were in the JavaScript part of a file and I think the way that vim is so
[2001.08 → 2007.08] focused on like file type plugins slightly just makes that awkward to do I'm sure it's not impossible
[2007.08 → 2014.38] but it doesn't feel like vim is aligned well for files that contain more than one language what
[2014.38 → 2019.82] frustrates you Julia the configuration like I don't understand a lot of the stuff in my vim config
[2019.82 → 2025.58] you know like you have like n no remap like what is it like i kind of know what it means what's I mean
[2025.58 → 2032.82] like you're trying to I know it means you're mapping like an um shortcut to something else like
[2032.82 → 2038.86] you like I might be like I have one that's like a leader in to like to remove highlights if I've searched
[2038.86 → 2044.06] for something, and it was highlighted and I want to highlight it right but um like I don't know what
[2044.06 → 2050.64] the no remap thing is about but I know that I see it all the time I definitely have it in my vim config
[2050.64 → 2054.82] and I definitely don't know what it means and specifically uh and like that's a little
[2054.82 → 2058.46] frustrating you know like it never really feels good when you have stuff on your computer that
[2058.46 → 2061.70] you use all the time when you don't know what it means anything else that frustrates you about it
[2061.70 → 2068.88] I think for a long time I didn't have paste working like vim didn't interfere with my system clipboard
[2068.88 → 2073.46] and I found that frustrating and then one day I figured out how to do it, and it was like life
[2073.46 → 2077.96] changing, and now it does and I'm just really happy um but I'm still literally surprised every time I can do
[2077.96 → 2082.68] that even though I've had it for years now it didn't work long enough that you were trained
[2082.68 → 2087.06] in to believe, and it won't work so when it does, it surprise you yeah oh I was going to say maybe
[2087.06 → 2091.34] one more thing I find frustrating actually which is that I think the default way vim is set up like
[2091.34 → 2095.86] whenever I use vim on not my computer it doesn't have my config, and they're just like some things
[2095.86 → 2102.78] about vim's default like it doesn't do like indenting you know like if you're editing a function
[2102.78 → 2110.86] on a server which you shouldn't be, but then you are or I am you know um and then like I entered
[2110.86 → 2115.00] new line, and then it goes back to the beginning of line so like indenting it nicely stuff like that
[2115.00 → 2120.78] Gary I'm pretty good at complaining so I'll limit myself to just one thing vim script to understand
[2120.78 → 2126.52] vim's relationship to its scripting language let me contrast with emacs is more is almost like
[2126.52 → 2132.80] an operating system that happens to ship with an editor and long-term Emacs users will effectively
[2132.80 → 2137.26] end up rewriting parts of that editor sometimes, but it's still Emacs because the layers underneath
[2137.26 → 2141.92] are still Emacs so Emacs lisp is a whole programming language it was designed to be a programming
[2141.92 → 2146.88] language vim is not like this at all vim was designed to be a text editor it had a configuration
[2146.88 → 2152.18] language that configuration language grew over time to acquire normal programming constructs and that is
[2152.18 → 2156.36] what we call vim script so it's a hodgepodge, and it wasn't sort of designed all at once
[2156.36 → 2161.24] and it's I don't think it's controversial to say its kind of a mess so that is the most
[2161.24 → 2166.64] frustrating part of vim for me, and it also is one of the reasons that I avoid configuration when I can
[2166.64 → 2173.52] I have a very sort of mostly stock vim configuration despite 15 years and vim script is why
[2173.52 → 2180.58] sub shared two frustrations one social and one technical by far the most frustrating for me is
[2180.58 → 2185.82] again like it's outside the editor itself it's the community and the culture around vim can be very
[2185.82 → 2190.64] friendly I want to qualify that first right and there's a lot of people that are really enthusiastic
[2190.64 → 2196.12] and happy to help you, but then there's also kind of the dark side in that i call it you know
[2196.12 → 2202.16] of the vim community which is that there can be a lot of dogma and some very bombastic culture you
[2202.16 → 2206.66] know it becomes like competitive it's like who knows the most amount of shortcuts who can customize this to
[2206.66 → 2212.10] be like the ultimate elite editor and the dogma around you know like even just like fuzzy
[2212.10 → 2217.00] finding search tools you know the amount of people that have like piled on me because of
[2217.00 → 2220.86] because I use Ctrl p, and they think that that's too slow and I should be using these other things
[2220.86 → 2226.28] it's really frustrating it's its like any other hobby that you see people get enthusiastic about
[2226.28 → 2232.04] sometimes they don't know how to sort of control those emotions or to understand that people come into
[2232.04 → 2237.92] that hobby or that code editor with completely different motivations to them and to just maybe
[2237.92 → 2243.52] consider that there are those differences so I feel like vim doesn't do the best job at selling
[2243.52 → 2249.12] itself as it is we've talked about how you know it has a rep for having a steep learning curve and
[2249.12 → 2254.30] um this just adds extra awkwardness around the tool to people getting started with it right like you
[2254.30 → 2257.84] almost don't want to say I'm starting with vim because you just know there's going to be a deluge of
[2257.84 → 2262.80] overwhelming unsolicited advice that is absolutely not helpful to people when they're getting started
[2262.80 → 2268.28] um and so that's one thing that disappoints me a little bit and I definitely don't feel
[2268.28 → 2274.32] like being on this vim episode is fascinating to me because I don't consider myself part of the
[2274.32 → 2279.00] community even though I've had perfect interactions with people such as Tim pope he's
[2279.00 → 2284.56] fantastic he's like written some of the most prolific vim plugins out there, and he's he's great um
[2284.56 → 2288.66] I've had a really great experience working with him, he's even poor requested one of my vim plugins and
[2288.66 → 2294.16] it's its awesome but uh those experiences tend to be few and far between for me so but I did want to
[2294.16 → 2301.04] sort of give a call-out to somebody who is really great at this when you are talking about vim itself
[2301.04 → 2305.62] when you're working with it, I still you know my touch typing is still not perfect right um and so
[2305.62 → 2310.96] sometimes I'll just accidentally hit a key I didn't mean to and when you're typing as fast as you are
[2310.96 → 2316.34] you'll just see something very dramatic happen in vim you have absolutely no idea which key you hit and
[2316.34 → 2320.72] how to actually cancel that because if you don't know what you did you don't know how to rescue it
[2320.72 → 2325.40] so um sometimes it can be frustrating because all of a sudden it'll just kind of like it'll be like a
[2325.40 → 2330.30] record scratch moment for you when you're in the middle of flow and um just trying to get back to
[2330.30 → 2335.80] where you were is annoying I think that gets better with practice um but I think everyone's done that
[2335.80 → 2340.84] thing where you accidentally toggle caps lock if you haven't sort of remapped your caps lock key which is
[2340.84 → 2346.54] I'm sure why a lot of people do this you toggle caps lock you hit k because you're just trying to
[2346.54 → 2350.80] go up a line you're trying to move your cursor in the file up a line and then all of a sudden you
[2350.80 → 2356.90] have this the whole screen goes blank, and then you've accidentally hit like the jump to the man
[2356.90 → 2361.38] page for this specific you know thing right, and usually you're just writing arbitrary code so there
[2361.38 → 2366.04] is no man page for the word that your cursor is on, and it starts yelling at you that it can't find
[2366.04 → 2371.10] it, and you're just like I don't where is my code where did it go where did you take me give it back
[2371.10 → 2376.52] um and so there are some of those kind of jarring moments that sometimes happen um and I think that
[2376.52 → 2382.26] obviously they get less and less frequent but for me, I still sometimes frustrate myself in that way
[2382.26 → 2386.00] you can really do a lot of damage with the efficiency of the program if that makes sense
[2386.00 → 2391.24] for me, it's always accidentally getting into macro recording mode it's like I'm trying to hit tab
[2391.24 → 2395.48] q yeah I hit q on accident I'm like tabbing and I hit q a couple of times and all of a sudden I'm
[2395.48 → 2399.28] recording things that I don't want to be recording I'm like uh how do I stop this yeah I've like
[2399.28 → 2405.04] recorded things for an entire half hour I sometimes swear so you hit q again to toggle it off and
[2405.04 → 2410.36] then you kind of go into a new buffer, and you hit play to see what you were recording because it's
[2410.36 → 2413.92] quite amusing there are definitely times on my twitch stream where people like Susie are recording
[2413.92 → 2419.94] right now because it's just like in the corner of my little status bar but yeah I think that tab versus
[2419.94 → 2424.62] q thing is very common too, and it's exactly the same frustration right totally there you have it
[2424.62 → 2430.78] a few vim frustrations and of course the learning curve is a big one for many folks the question is
[2430.78 → 2436.04] should you learn vim today maybe you gave it a try once and got stuck should you give it another go
[2436.04 → 2442.26] Gary shared some excellent reasons why that might just be the case I absolutely would recommend it i
[2442.26 → 2446.62] also would recommend people not to beat themselves up over it if they decide they don't like it like
[2446.62 → 2450.68] there's kind of this weird sort of you know you have to use the hard thing, or you're not you're not
[2450.68 → 2454.88] a real programmer or whatever don't worry about any of that but give it a try and I can name three
[2454.88 → 2460.58] different reasons to do it and I think all of them are sufficient on their own so first RSI it'll
[2460.58 → 2464.72] prevent injury it's a really important thing as a programmer if you want to make a career out of
[2464.72 → 2470.50] this the second is speed vim is unambiguously faster than other editors it's not even remotely
[2470.50 → 2475.42] controversial to say that, but the question of course is going to be whether you value speed over
[2475.42 → 2479.46] what you may be giving up things like deep language support from something like Visual Studio
[2479.46 → 2484.50] or a JetBrains IDE or whatever so you're making a trade-off there but for me speed is even
[2484.50 → 2488.58] sufficient on its own because every time you have to stop and like slowly make some edits is a chance
[2488.58 → 2492.26] for you to forget what you were doing to lose the state in your brain, and maybe you're like eight
[2492.26 → 2496.70] levels deep in your stack, and you're going to start losing those levels right if you have to get
[2496.70 → 2503.48] distracted it's also just fun honestly to be fast, and then the third reason is that vim unlike most
[2503.48 → 2507.88] other editors is not going to go away the vim keystrokes in particular, so many people have them
[2507.88 → 2512.72] so deep in their brains that 30 years from now you will absolutely be able to get an editor that has
[2512.72 → 2516.44] those keystrokes I don't know whether it'll be vim I don't know whether Bram Molina will be
[2516.44 → 2521.34] maintaining it, but you will be able to use those keystrokes so any of those for me is sufficient
[2521.34 → 2525.74] especially for the last one if you think about the timeline just for me right 15 years at the
[2525.74 → 2530.14] beginning of that time TextMate was just becoming popular then it was sublime text was cool
[2530.14 → 2535.56] then atom was cool then VS Code was cool a lot of people switched between two of those three of
[2535.56 → 2539.38] those maybe all four of those and that whole time I was just getting better and better and better at
[2539.38 → 2544.12] vim, and you multiply that out by the length of a career use vim for 40 years you're going to be
[2544.12 → 2548.10] so good at it by the end, and it's still going to be totally relevant I think
[2548.10 → 2558.06] as a companion to this episode we have three YouTube videos of our guests timing with me to
[2558.06 → 2563.66] give you a taste of what their vim life looks like links to those videos are in your show notes if
[2563.66 → 2569.42] you've never given vim a serious try hopefully this episode of the changelog convinced you it's worth
[2569.42 → 2575.96] your while how to go about learning vim is another conversation in and of itself drew and SU's both
[2575.96 → 2582.28] recommended vim adventures which has been described as Zelda meets text editing i know it had
[2582.28 → 2587.72] you at Zelda unfortunately Julia doesn't have any vim related zines for you but Gary does plan to make
[2587.72 → 2593.48] a vim course real soon now we also have a channel in our slack dedicated to vim I encourage you to join
[2593.48 → 2599.12] the community which is totally free at changelog.com slash community and hop in that channel there's lots
[2599.12 → 2604.16] of friendly and vim passionate folks in there the channel is called vim party so you know it's good
[2604.16 → 2609.10] we put a lot of love into this episode so if you enjoyed it and want to hear more like this
[2609.10 → 2613.76] please let us know post it on Twitter submit it to hacker news and Reddit tell your programming
[2613.76 → 2618.34] pair it's a must-listen write a reaction blog whatever is your pleasure we love hearing from
[2618.34 → 2623.64] you special thanks to source graph once again for helping us ship this interruption free to break
[2623.64 → 2628.58] master cylinder for all the beats to Adam Stokowski for his storytelling and production skills
[2628.58 → 2634.20] and to our very special guests Julia Evans drew Neil such Hinton and Gary Bernhardt you all are awesome
[2634.20 → 2639.64] if this is your first time listening don't forget to subscribe at changelog.com and if you love our
[2639.64 → 2645.12] work support us directly by joining changelog plus that'll get you closer to the metal and make
[2645.12 → 2651.84] the ads disappear check it out at changelog.com slash plus I'm jarred Santa, and we'll talk to you next time
[2651.84 → 2653.84] more
[2681.84 → 2683.92] Altering
[2683.92 → 2687.00] 解
[2687.00 → 2692.92] 解
[2692.92 → 2694.04] 解
[2694.04 → 2694.60] 解
[2694.60 → 2694.88] 解
[2694.88 → 2695.00] 解
[2695.00 → 2695.66] 解
[2695.66 → 2696.16] 解
[2696.16 → 2696.42] 解
[2696.42 → 2696.56] 解
[2696.56 → 2697.62] 解
[2697.62 → 2698.66] 解
[2698.66 → 2698.88] 解
[2698.88 → 2699.54] 解
[2699.54 → 2700.66] 解
[2700.66 → 2700.72] 解
[2700.72 → 2701.68] 解
[2701.68 → 2702.08] 解
[2702.08 → 2702.58] 解
[2702.58 → 2702.72] 解
[2702.72 → 2703.64] 解
[2703.64 → 2704.88] 解
[2704.88 → 2705.78] 解
[2705.78 → 2706.06] 解
[2706.06 → 2708.24] 解
[2708.24 → 2708.62] 解
[2708.62 → 2710.36] 解
[2710.36 → 2711.48] 解
[2711.48 → 2711.50] 解
