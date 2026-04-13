[0.00 → 15.96] welcome back everyone this is the change log and I'm your host Adam stekowiak this is episode 162
[15.96 → 22.14] and on today's show we're joined by Brandon Mathis Brandon is the creator of octopuses
[22.14 → 28.38] if you haven't seen octopuses I don't know where you've been at because so many blogs out there
[28.38 → 36.02] right now leverage octopuses well 2.0 octopuses not 3.0 3.0 is a complete rewrite we dive deep
[36.02 → 43.32] into that with this show here uh 2.0 is gone 3.0 is basically out there the announcement hasn't
[43.32 → 46.60] been official there are some things Brandon's working on which you'll hear in this show
[46.60 → 54.34] but 3.0 is basically Jekyll's Ferrari you know, so get excited about this show and what Brandon's
[54.34 → 61.06] working on we have three awesome sponsors code ship dream hosts and top towel our first sponsor
[61.06 → 65.60] is code ship they're you hosted continuous delivery service focusing on speed security
[65.60 → 71.52] and customizability you can set up continuous integration in your app today in a matter of
[71.52 → 77.30] seconds and automatically deploy your code when your tests have passed code ship supports your
[77.30 → 82.70] GitHub and your Bitbucket projects, and you can get started today with code ships free plan
[82.70 → 88.44] should you decide to go with a premium plan you can use our code to save 20 off any plan you choose
[88.44 → 94.58] for three months the code is the changelog podcast head to codeship.com slash the changelog to get
[94.58 → 96.50] started and now on to the show
[96.50 → 109.98] well we're back a long time in the making for this show Brandon have wanted to have you back
[109.98 → 115.50] to talk about octopuses 3.0 I think jarred we've covered octopuses how many times on the on changelog
[115.50 → 122.20] weekly lots of times a couple yeah and every time we do we get tweets and emails and fan mail I get
[122.20 → 128.22] mailed to my house my home address saying more octopuses so Brandon welcome back thanks for uh
[128.22 → 135.50] letting me back yeah octopuses 3.0 how excited are you oh really excited I am a lot of hard work gosh
[135.50 → 139.66] for real I mean it's its not just a lot of hard work it's also been a lot of learning which
[139.66 → 144.82] is the fun part, but you know it's kind of like when i first started working on octopuses it was
[144.82 → 151.38] just some cool thing that I had barely figured out how to do, but you know then uh once people started
[151.38 → 156.20] using it I started to find out um there are a lot of different needs for it and then uh and finally
[156.20 → 162.46] I am able to you know I was able to take time to sit back and say you know if I had any skills what
[162.46 → 168.14] would this look like, and so I spent like two years trying to build those skills and then uh
[168.14 → 172.76] and build what I wanted to make the first time if I knew how to do it and I can see that Brandon
[172.76 → 180.10] mathis.com is still using the original design you had done and this was in Jekyll right this site
[180.10 → 185.06] here oh yeah it's that it is Jekyll that's what got me starting with octopuses, but that is probably
[185.06 → 192.10] using octopuses one um i as I there's not even a post on there announcing octopuses it's just some
[192.10 → 198.12] other project that I released right before it and um that's always kind of um something I am able to
[198.12 → 204.38] appreciate and laugh at myself about I decided at some point that um at this point in my life my code
[204.38 → 209.02] is more valuable than the other things I would write about, and so I've poured a lot of energy into
[209.02 → 215.90] code not building writing yeah making it so that other people can write um you know their sites and
[215.90 → 222.00] you know building nice tools and developing that um I really hope to kind of turn back and
[222.00 → 227.06] write a lot about what I've learned, and you know have a nice blog again but uh I didn't want to
[227.06 → 231.02] distract myself well you got a family you got a full-time job speaking of your full-time job you
[231.02 → 236.44] work at compose formerly Congo HQ so I know we use Congo HQ at pure charity when I worked there
[236.44 → 242.86] um for our Congo hosting which was great um, and you created octopuses six years ago so for everybody
[242.86 → 248.40] listening now catching up saying what the heck octopuses 3.0 what happened to 1.0 and 2.0 well 2.0 is out
[248.40 → 254.60] there and I guess 3.0 is sort of out there we'll hear more from you today um hasn't been talked
[254.60 → 257.16] about quite as much as you just said there because you're not really doing much with your
[257.16 → 263.84] blog and even the latest post on octopress.org isn't quite saying like hey here it is
[263.84 → 269.62] right yeah I have an I have a version of that post in a draft that I'm kind of working on figuring out
[269.62 → 274.06] how I want to do some things you know the um the post that's up there right now is talking about
[274.06 → 278.68] uh it says octopuses 3 is coming and basically i just you know throw all my dirty laundry out there
[278.68 → 285.52] and dissected it and said this is uh this is a is what I did wrong with octopuses 2 um a lot
[285.52 → 291.32] of people are using it and enjoying it and I'm sorry uh for for these mistakes I've made
[291.32 → 294.18] these are the things I've learned this is what I'm bringing that's what happens with open source
[294.18 → 299.42] though you know you uh you know somebody does something good they don't have their full-time
[299.42 → 305.56] to give to it and so you know you either uh get more people involved in your project or you're a
[305.56 → 310.36] one-man show like you've been I think you've had some help too from parker Moore oh yeah you
[310.36 → 314.00] know back and forth with jack and I think you are you're part of the core team with jackal now are
[314.00 → 320.22] you just sort of playing some sort of role in that well no I'm not a core team member I am
[320.22 → 325.12] um a friend of jackal I don't know you know like you say you got a friend of the show or whatever I guess
[325.12 → 330.52] I'm a friend of jackal uh in that way because like for example uh I recently participated in
[330.52 → 334.34] jackal cone which was an online conference right that's awesome and um lots of people were there
[334.34 → 339.56] including tom Preston Warner who created jackal and parker who's the lead maintainer right now and i
[339.56 → 344.54] showed off some of the new stuff I've been building and um you know they were taking questions on
[344.54 → 349.54] twitter and pretty much immediately after I started showing a couple of things tom wrote in saying why isn't
[349.54 → 354.12] this stuff part of core and would you be okay with adding it and I'm like sure dude steal what you want
[354.12 → 363.34] it's MIT I'll help however but yeah you know uh on um the uh tagline for octopus used to be um
[363.34 → 368.60] was it a blogging framework for hackers or something like that something like that yeah yeah which is
[368.60 → 375.12] funny because the somebody posted on hacker news uh when to uh 2.0 came out and um of course i
[375.12 → 378.54] didn't know what hacker news was at the time and I still barely do I don't pay attention to that stuff
[378.54 → 383.50] believe it or not um and some guy accused me of picking that as a tagline just to get on
[383.50 → 391.14] hacker news I'm like dude I don't even know what this is what's going on so but um now the uh the um
[391.14 → 395.92] the tagline I'm playing around with right now which is just it's like a know who cares what you say
[395.92 → 400.86] about something but uh I'm I'm the way I look at octopuses is that it's like jackal's Ferrari
[400.86 → 406.72] so if is jackal had you know or um good job maybe
[406.72 → 413.74] well it's its like an engine it's like jackal can jackal is a lightweight uh sprint runner he's got
[413.74 → 417.30] some skills and stuff but every now, and then he wants to jump into a Ferrari and just you know
[417.30 → 421.30] blast it and so that's kind of what octopuses is about it's like this is the place where
[421.30 → 427.12] jackal feels good um I don't know if that's sensible or not but uh basically um there are a
[427.12 → 432.30] bunch of tools built around jackal and octopuses is just my name for tools that I build to make
[432.30 → 437.50] that ecosystem uh have the things that I want in it, and we can talk about some more of those in a
[437.50 → 441.00] little bit I want to talk a little bit about the history to a degree uh especially which since you
[441.00 → 447.42] just mentioned the name WordPress right so is octopuses a play on that or is you know is that why
[447.42 → 454.84] press is after onto was it a GitHub thing you know everybody assimilates uh onto for something GitHub
[454.84 → 459.96] right so you got I don't know onto is don't they have octagon or is it just Comecon or something like
[459.96 → 464.92] that, but they do onto something all the time there October right October, and then you got
[464.92 → 471.76] onto kit too which is the API kit the API right frameworks and the octagons or their icons yeah
[471.76 → 476.98] they actually say um it for people who are building stuff that goes with the um the GitHub API don't
[476.98 → 482.62] use the name GitHub use the name onto and so uh this actually octopuses doesn't have anything to do
[482.62 → 487.26] with that um I just happen to really like octopuses and um or octopi you can actually say either
[487.26 → 491.76] uh but I was about to correct you, but then you just said you can say either and now I was going
[491.76 → 496.26] to correct him too but I decided I'm so glad I didn't correct you I'm not going to do it well I'm
[496.26 → 503.72] just actually making this up uh so anyway though I thought yeah this was a rage-quitting a WordPress
[503.72 → 510.80] and I thought what would be a cool thing is I just pictured what is now the icon which was or the
[510.80 → 515.24] it's not really an icon the graphic that I use is an octopus uh typing on a typewriter
[515.24 → 520.94] and I got David Latham to do that art uh and actually thinking of David Latham designing
[520.94 → 525.86] that art and having the um uh, and you know and what it was going to look like was a part of me
[525.86 → 529.94] picking the name i just really thought it would be cool to have an octopuses on this old school
[529.94 → 535.94] typewriter so did I see an octopuses or an octopus that's what I meant anyway my autocorrect is like
[535.94 → 539.64] doesn't ever know what I'm trying to talk about well you know it's not in your voice it's on your phone
[539.64 → 546.42] oh the autocorrect yes well i also I guess um yeah I've taught you can teach your computer you
[546.42 → 551.16] can't teach your phone that's right my computer knows what it knows what it's expecting so anyway
[551.16 → 556.86] yeah I was rage-quitting uh WordPress and i just um thought that would be a neat you know it's its
[556.86 → 562.54] such a close word to octopus and um so yeah that's it was just as simple as that so it's more of an
[562.54 → 568.54] affinity towards well I guess anti-affinity to WordPress than it would be an affinity to GitHub
[568.54 → 574.70] right yeah I mean you know i I guess I don't know maybe some of GitHub at the time could have
[574.70 → 579.54] influenced that this was in early 2000 yeah I mean this is sometime in 2009 so really I think I started
[579.54 → 586.18] using GitHub in 2008 maybe um it wasn't I mean it wasn't as eating the world as it is today
[586.18 → 591.78] um, and so i you know looking back i that's how I remember it um it may have also been that GitHub
[591.78 → 595.98] had an October but I don't really remember if they I think it was pretty new since you mentioned
[595.98 → 604.08] dates June 5th 2008 what do you what were you doing that day I was joining GitHub i was like I am
[604.08 → 611.64] so done with subversion I was celebrating I was like what is a branch what how do you what is this merge
[611.64 → 618.90] conflict when did you join jarred GitHub yeah I don't know how do I find out uh you go to your
[618.90 → 625.62] your uh profile page all right cool, so this is what we're going to do here I'll tell you here in a
[625.62 → 631.66] second April 22nd 2008 so you beat Brandon it's like a peeing contest I beat you yeah let's see if
[631.66 → 639.80] let's see if anybody beat me yes March 12th same year so you beat me by a month about they didn't
[639.80 → 647.86] open up until I think January that year it was such unique times too uh brings back memories I remember
[647.86 → 655.06] having a conversation with josh Owens uh co-host of a podcast I ran a while ago called the web 2.0 show
[655.06 → 662.40] if anybody listened to that show I did shout out um we were actually in San Francisco for the web 2.0
[662.40 → 669.20] expo which was super cool back in the day, and we went over to pivotal labs and met up with tom
[669.20 → 674.54] Preston Warner and Chris wallenstroth and sat down and had a face-to-face conversation about GitHub
[674.54 → 680.88] like a month before this so like February time frame crazy that's fine on the show or just
[680.88 → 686.06] for fun no we released the podcast I'll link it up in the show notes it's out there on the web still
[686.06 → 692.54] yet but yeah man i it's just crazy how time flies and six years ago I mean that's that's octopuses six
[692.54 → 699.54] years ago but like GitHub is you know going on what six eight seven eight something like that it
[699.54 → 704.32] was around before I started octopuses because i uh learned some of the initial things that I put
[704.32 → 710.06] into my first version from there uh john long had some rake tasks for uh deploying stuff through sync
[710.06 → 715.22] and I was like no way you can just point sync at a directory and ssh it somewhere this is amazing
[715.22 → 718.94] and you know this is before GitHub pages and stuff and so that was the initial version was just
[718.94 → 726.74] basically my blog fork it and then run some rake tasks yeah for those who want to know the uh
[726.74 → 734.14] I guess the link I'm trying to find it real quick see where is it at okay I can't find it check
[734.14 → 741.28] the show notes it's in this list I just can't seem to scan and find GitHub in this list that's crazy
[741.28 → 746.42] but yeah we um we had some fun going out there and talking to those guys, and it's just been such a
[746.42 → 752.02] ride too for GitHub it's been so long and I guess since we're talking about the past a little bit
[752.02 → 758.32] this isn't your first time on this podcast either brand you've been on the show in its infancy episode
[758.32 → 765.50] 17 where this is episode 162 it might be 163 so if you're listening to this, and it's actually 163
[765.50 → 773.82] sorry but uh it's right in Adam wants to be corrected yeah I'm going to change that but uh yeah
[773.82 → 783.60] but uh episode 17 was March 11th 2010 which you know that's a long time ago man this feels like
[783.60 → 787.70] forever man I feel like we're getting old all the young people listen to this show
[787.70 → 796.30] jeez I just wish I was young again but anyway so octopuses 3.0 that's where we're at now but it
[796.30 → 804.88] began somewhere 1.0 obviously or somewhere around there 2.0 is what I think the website best
[804.88 → 811.72] represents you know or is at least talking about so you got a full-time job this has been like I told
[811.72 → 818.26] jarred in the pre-call like this is your curl we had um jeez what's his name Daniel Steinberg Daniel
[818.26 → 824.12] Steinberg yeah and Daniel Steinberg wrote curl and lib curl, and he's been doing that for how many years
[824.12 → 829.14] 17 years 17 17 years of curl that's right you're complete my sentences and I appreciate that
[829.14 → 835.38] and this dude has been doing that project only consistently for at least two hours a day
[835.38 → 840.82] for 17 years right Brandon like imagine that that's wild is that what octopuses is for you
[840.82 → 846.48] uh it is that right now I mean i I actually do build a lot of other stuff too um right now um another
[846.48 → 854.02] side project is a personal personality profile test that um is yeah I thought it'd be fun to have
[854.02 → 858.26] uh because you know all these pro I love I study personalities I think they're fascinating and the
[858.26 → 863.02] way they work and all the tests out there though are either crappy or you pay to take them
[863.02 → 870.94] and I thought well you know with all I mean I've been studying this stuff for like 14 15 years and um
[870.94 → 875.92] i you know given the kind of questions these things ask it'd be very easy to write my own
[875.92 → 881.06] and then put it on GitHub and have people submit pull requests to improve the questions and stuff
[881.06 → 885.18] and then also for people who are curious about that kind of stuff how that stuff works they can see
[885.18 → 890.28] a really simple test and so there's you know I'm still working on launching it, but stuff like that
[890.28 → 895.10] you know I've got uh also HSL colour picker.com yeah I'm a front end tool, so there's you know there's
[895.10 → 898.64] all kinds of things that i uh that I like to build I guess since you mentioned that we should also
[898.64 → 905.48] mention are you still on the core team of uh compass, so compass has been um end of life
[905.48 → 912.42] and uh Chris is now working did I not hear about that did we miss that did i just make that
[912.42 → 917.84] up uh breaking news here on the change log so i think what's actually happened is
[917.84 → 923.78] uh Chris is moving on to spectacles which is something that is more um I think it's uh written
[923.78 → 932.42] in JavaScript it's around um the uh lib sass stuff with uh node s, and it's its meant to be something
[932.42 → 938.86] that's easier for people to use than compass, and it's kind of a start over and so compass is wow
[938.86 → 944.08] like marginally supported if that right now we should pause your show and talk about this now
[944.08 → 949.80] because I hadn't heard any of this news well you need to talk to Chris then um he's he's uh really
[949.80 → 953.64] he's looking for help he's trying to make you know bring a lot of the stuff in that uh people
[953.64 → 958.88] liked about compass but separate it in a way that isn't uh a whole pile of uh do I want this or not
[958.88 → 963.04] and people you know because the really nice thing about was comp with about compass was how it would
[963.04 → 967.44] integrate into your environment and make it easier for you to you know reference images without
[967.44 → 972.54] having to maintain all the URLs to CDNs and stuff yourself oh just so many cool things that compass
[972.54 → 978.90] does it is uh you know he's trying to bring that to the community who isn't interested in using ruby
[978.90 → 984.12] and so it's called speckle is what he's working on now spectacles I think spectacles yeah all right
[984.12 → 988.84] we'll get in touch Chris now I feel terrible like saying this on recording because I don't know
[988.84 → 994.30] if I'm accurately portraying these things or not this is my you know caveats okay something you
[994.30 → 999.22] heard through the grapevine yes somebody made this up guys I don't even know but anyway so
[999.22 → 1004.34] are you still part of the compass team then even if it's where it's over man I really haven't been
[1004.34 → 1008.94] helping out with that uh for quite a while now um I helped with building the website and some other
[1008.94 → 1014.00] things, and you know some of my early plugins I think maybe got people excited about what it's like
[1014.00 → 1018.60] to do plugins I also wrote a book with win Netherlands and uh Nathan Feigenbaum or
[1018.60 → 1023.34] actually Natalie now Natalie I think it still says Nathan on the cover though um and then uh
[1023.34 → 1030.36] and then Chris as well and so that was my final contribution I think what was that book that was
[1030.36 → 1035.32] called compass in action or sass in sass and compass in action I don't remember I've got a
[1035.32 → 1039.20] Japanese version of it though which is I own the book right here on my bookshelf I let me look back
[1039.20 → 1046.38] here and see if I can see it where that yep there it is got the book yeah i they uh they also
[1046.38 → 1052.98] printed it and translated it in japan, and so they sent me one of those when they did, and it is a way
[1052.98 → 1058.56] better cover it's like all pink and blue and goofy looking, and you know it's just like this thing looks
[1058.56 → 1065.00] awesome looks like it fell out of a 80s anime wow so all that to say is that not only do you have a
[1065.00 → 1074.66] full time at compose have a family and have a life you also do octopuses HSL picker a personality test
[1074.66 → 1081.16] had been a part of the compass team for a bit wrote a book so you're busy right, so this is some reasons
[1081.16 → 1087.92] why 2.0 to 3.0 have been what about a year and a half is two years I'd go with two years I mean
[1087.92 → 1094.58] since I've been working on it in earnest i uh yeah so to answer the question that that seems to
[1094.58 → 1101.92] suggest I am working on this thing like crazy uh it is kind of like uh some people enjoy sports
[1101.92 → 1108.32] uh this is what I enjoy so i you know when I have free time in the evening when I have energy
[1108.32 → 1114.32] um I sit down and I work on this for several hours and just for the safety sake then for those who are
[1114.32 → 1120.32] still trying to catch up with what octopuses is what's the one-liner you know what is octopuses
[1120.32 → 1127.76] octopuses is a collection of tools to make working uh with Jekyll sites better more fun
[1127.76 → 1136.52] and uh it makes me feel good I don't know I don't have a one-liner well octopuses 2.0 is basically
[1136.52 → 1141.10] some guy's Jekyll blog you can fork and modify right that's that's what I called it in my what is wrong
[1141.10 → 1146.50] with me why did I build this post right right right there you go so yeah this is uh this
[1146.50 → 1153.02] is okay so I mean do you want to talk about um what happened here what was going on with the
[1153.02 → 1157.76] transition because it sounds like there were some serious deficiencies um according not according to
[1157.76 → 1165.26] us but according to yourself and what became 2.0 it looks like your octopuses 2.0 surfaces post was
[1165.26 → 1170.06] you know 2011 July 2011 and then octopuses 3 is on its way, so there's some also some time
[1170.06 → 1176.20] about four years in there what, and you call octopuses 3 a complete rewrite so what was so
[1176.20 → 1181.78] wrong uh that it needed a complete rewrite and why is okay so just to be blunt why is it taking so
[1181.78 → 1187.40] long besides all the stuff that we just said about family and job and all that well so when 2 came out
[1187.40 → 1195.72] uh I spent a lot of time just working on 2 I think even in uh let me think uh yeah for like a next
[1195.72 → 1200.20] for about a year and a half I just spent time trying to make it better and um I guess digging
[1200.20 → 1206.10] the hole deeper uh instead of moving on because really what the problem was is it is an it's
[1206.10 → 1212.74] at math as octopuses it is a repo that you fork or uh clone and then run some commands and make it
[1212.74 → 1219.04] your own and push it to your own uh get repository hopefully never fun when people say oh I deleted my
[1219.04 → 1225.62] blog what do i'm like dude uh time machine I don't know um but uh yeah so if it was kind of
[1225.62 → 1230.90] like all set up for you to use a certain way but the know Jekyll has a plugin system that is
[1230.90 → 1235.18] really simple to use if you want to modify your own site there's just a directory called plugins
[1235.18 → 1239.82] in your site source, and you can just drop a ruby file in there to get required uh as long as you're
[1239.82 → 1245.90] you know building it locally if you push it to GitHub pages it won't but if you uh is you're
[1245.90 → 1250.14] building it locally um yeah you can add whatever ruby in there you want, and it's like hey man you
[1250.14 → 1255.04] added this ruby you better believe it's its good, and so I had a bunch of ruby files
[1255.04 → 1259.78] in the plugins' directory that would do all these cool things like uh make it nice for you to write
[1259.78 → 1265.78] code snippets and generate nice HTML around those and um there were some great tasks that did
[1265.78 → 1270.68] uploading and configuring and all this kind of cool things and so you know if you wanted to change
[1270.68 → 1277.02] anything though the problem is you're tracking my repository right and so if I make an update and
[1277.02 → 1280.48] then you want to pull that in you have to deal with merge conflicts that kind of thing was just stupid
[1280.48 → 1284.08] and this is because I didn't know how to build gems and that's one of the reasons why I never used it
[1284.08 → 1288.50] yeah that's the dumb thing about it, I was in the air about that one I mean I was a middleman person
[1288.50 → 1293.00] before I was a Jekyll person and that was one of the reasons why I remember even since you mentioned
[1293.00 → 1300.40] john long earlier he and I worked on the sasway.com together and when we redid the sashay from I think
[1300.40 → 1306.38] it was I forget what it was written in originally, but it's its written in middleman now so that's a
[1306.38 → 1312.42] middleman site and he talked about using author press because you were doing 3.0 and all these new
[1312.42 → 1318.12] things and I'm like yeah you know i just I don't I didn't like how you know how things were so
[1318.12 → 1324.78] fractured you know and how they were so fragile it seemed you know with requests, and you know just
[1324.78 → 1328.74] not pull requests but like merge issues and stuff like that I was like I don't want to deal with that
[1328.74 → 1333.56] yeah it's just stupid I mean like the configuration for your site is uh the underscore
[1333.56 → 1338.74] config YAML file and so if you make changes to that and I'm like oh I should add this new thing or
[1338.74 → 1342.06] you know I want to I want to change the way this plugin works because someone submitted a pull
[1342.06 → 1345.86] request that fixes this other thing and all of a sudden you have to deal with the merge conflicts
[1345.86 → 1351.04] of changes like that as opposed to just you know it being in a gem, and then you have your own
[1351.04 → 1356.76] configuration and stuff like that and I mean this is before gosh it's gotten so much easier to deploy
[1356.76 → 1362.08] ruby gems now, and you know uh bundler is a big part of that you can just say bundler gem and then give
[1362.08 → 1366.74] it a name, and it'll generate a gem scaffold for you and with all kinds of nice defaults and stuff and so
[1366.74 → 1370.74] you just dump your ruby code in there and then run a couple of rate commands, and it ships it up to
[1370.74 → 1375.84] ruby gems, and it's like that simple, and it wasn't that simple at the time and also I wanted to build
[1375.84 → 1380.86] a command line interface and I still needed to learn a lot of rubies I mean I knew enough to write some
[1380.86 → 1387.08] cool plugins and I learned you know I got some insane knowledge of regular expressions but other than
[1387.08 → 1393.36] that uh you know I just didn't have the skills and so um I had a really hard time maintaining that
[1393.36 → 1397.06] and right now there's a bunch of open issues and some of it is just because I think
[1397.06 → 1403.26] the uh clone this and it and then mess with it is really attractive to a lot of people because they
[1403.26 → 1408.80] can see how everything works it's not hidden away in some gem somewhere right and so a lot of people
[1408.80 → 1414.74] used it who were getting to know ruby for the first time or getting to know you know development
[1414.74 → 1418.84] or all kinds of things like it was crazy the number of people that talked to me who this was
[1418.84 → 1424.56] like their intro into the development world, and it was because you just it's so simple you just pull
[1424.56 → 1429.42] it down and there it is, and it works, and you can mess with things and so that had uh that had
[1429.42 → 1434.86] the negative side effect though of attracting a lot of people who didn't really know how development
[1434.86 → 1439.44] works, and so they would submit issues saying oh it'd be cool if you added this thing it'd be cool if
[1439.44 → 1444.28] you added this thing, and so I've got all this code that I can't use or that if I bring it in it breaks
[1444.28 → 1448.78] other people's sites and it just it was horrible to maintain and so there are a lot of good things
[1448.78 → 1455.02] about it, but there were some terrible things about it too yeah i I think when we when I think
[1455.02 → 1460.30] about octopuses think about developer blogs for one and then I feel like it's the know Kubrick
[1460.30 → 1465.96] theme as it is to WordPress which isn't quite relevant now, but it was back in the day so
[1465.96 → 1473.34] people who have you know been using WordPress for a long time uh Kubrick was a really popular theme i
[1473.34 → 1478.58] think it was the first original theme that WordPress recognized as a third party that became an
[1478.58 → 1483.66] official and so if you saw a WordPress site you could easily recognize it was WordPress based
[1483.66 → 1488.86] upon its theme I feel like the same thing with octopuses is that um I don't know how many
[1488.86 → 1493.80] blogs that go out there, and it's like it's its basically the octopuses site as you see it now with
[1493.80 → 1500.42] a slightly different header you know text header or whatever like it's it caught on and there are so
[1500.42 → 1506.12] many sites we link to and change all weekly or just in general that it's its octopuses that's
[1506.12 → 1511.00] yeah it's out there quite a bit and so it's very popular it's its been nice because you know same
[1511.00 → 1515.62] thing happens to me, i if I don't hit stack overflow I frequently hit an octopuses blog looking for
[1515.62 → 1521.24] something and I always try to um find out who you go a little bit inside when that happens oh yeah no
[1521.24 → 1526.46] not only do i not only do I get excited but i also um always try to thank the person uh if they have a
[1526.46 → 1531.00] twitter handle available or something or if they have email but um so it's just like hey man you
[1531.00 → 1536.82] know thanks for uh helping me solve this problem I'm excited to see that smart people like you are
[1536.82 → 1542.08] using octopuses so that was that's always fun so to summarize some of the issues you're trying to
[1542.08 → 1547.90] solve with and jarred's original question was what's what's wrong with 2.0 you know why the full
[1547.90 → 1553.94] rewrite to 3.0, so a lot of the issues are the ray was the way it was originally published was you
[1553.94 → 1558.48] know you had to fork your original version you had to deal with merge conflicts it was just sort
[1558.48 → 1563.46] of messed up gems have gotten a lot easier to publish for ruby uh what was some of the other
[1563.46 → 1567.90] things you mentioned what yeah I will say as a correction you don't actually have to forget a lot
[1567.90 → 1573.68] of people did because I don't think people knew how to use GitHub at the beginning it's like do i if i
[1573.68 → 1578.46] fork this then it's mine, and they didn't really understand it's for contributing um so yeah it was
[1578.46 → 1585.22] I mean it's just it's just a very simple separation of concerns problem that if you build
[1585.22 → 1591.00] an uh one tool that has tons of different code that solves different problems then it's really
[1591.00 → 1594.54] hard to break those apart when you need to figure out what's what's going wrong and so it wasn't
[1594.54 → 1600.00] really testable there were so many challenges in developing a system that was like it all kind
[1600.00 → 1604.68] of works together and if you pull something out you know it wasn't you know it is like if you remove
[1604.68 → 1608.30] one plugin it may break another plugin that was expecting that because they don't have a
[1608.30 → 1612.40] dependency chain they're just ruby files um and so then if you want to unwind something you're like
[1612.40 → 1616.60] where you know you're actually editing all this code to figure out how to remove something and
[1616.60 → 1621.66] that's just terrible so I could go on about the many sins, but it's basically just I wanted to
[1621.66 → 1626.66] summarize what the real problems were so that it was clear so as we step into deeper discussions
[1626.66 → 1633.12] about 3.0 here in just a bit that we can reflect on some of the problems you've already
[1633.12 → 1640.86] illustrated with which is why 3.0 is a rewrite not just a right so as a summary then it's the way
[1640.86 → 1645.66] it was deployed was through git which meant you were tracking all my stuff that's bad git is for
[1645.66 → 1650.84] collaboration it's not for shipping a product that doesn't make any sense um the other problem was
[1650.84 → 1658.88] that it was uh yeah all the pieces kind of were come with the puzzle, and you couldn't really
[1658.88 → 1663.38] take them apart or add to it easily I think those are the main problems with it really
[1663.38 → 1667.70] and cool lets uh let's take a break then real quick we'll do a sponsor break
[1667.70 → 1673.54] and when we come back we'll start diving deeper into octopuses 3.0 so we'll be right back
[1673.54 → 1682.46] DreamHost now has managed VPS hosting built for speed and scalability including solid state drives
[1682.46 → 1688.04] and that's awesome these VPS's are built for open source developers and now include one click
[1688.04 → 1695.16] installs of node.js custom ruby and RVM support speed and more speed is what it's all about
[1695.16 → 1702.64] their VPS servers use SSD hard drives and are 20 faster than traditional SATA drives all virtual
[1702.64 → 1709.82] private servers from DreamHost include SSD storage Ubuntu 1204 LTS web-based control panel
[1709.82 → 1714.92] scalable ram which is super awesome you can go from one gig of ram and easily scale up to eight
[1714.92 → 1721.44] gigs if you need it node.js one click install ruby version manager unlimited bandwidth unlimited hosted
[1721.44 → 1728.92] domains unlimited 24 7 support go check them out and learn more at dreamhost.com slash the changelog
[1728.92 → 1737.22] all right we're back got uh Brandon here jarred gosh man octopuses is uh
[1737.22 → 1742.98] Jekyll's Ferrari I see it right here in the byline now I didn't notice it before but octopuses 3.0
[1742.98 → 1747.80] space hyphen space Jekyll's Ferrari Jekyll's Ferrari
[1747.80 → 1755.40] yep I mean that's just that engine yeah the fun thing is you can click the edit button and type
[1755.40 → 1759.08] whatever you want to so uh a couple of nights ago I was like yeah I'm just going to call it Jekyll's
[1759.08 → 1765.08] Ferrari for a little while well you know hey that's you know that's fine I like that that's cool
[1765.08 → 1773.36] so now you have so octopuses did originate on your user on GitHub now it has its own work so
[1773.36 → 1781.44] GitHub.com slash octopuses onto onto onto p-r-e-s-s in case you did not spell octopuses
[1781.44 → 1789.56] um so let's talk about uh 3.0 what give me the elevator pitch to what's new in 3.0 what is
[1789.56 → 1796.46] 3.0 as compared to 2.0 and all the things we've talked about so far so 3.0 is basically everything
[1796.46 → 1804.04] is shipped as an independent gem that has its own tests that have uh a CLI that kind of ties different
[1804.04 → 1811.68] tools together, and you can, you know use any part you want to without having to adopt a whole system
[1811.68 → 1817.06] and it works with any Jekyll blog there's no uh you have to change how you do things in order to
[1817.06 → 1823.22] adopt octopuses it's you know any Jekyll site can add a plug-in and immediately get the value from it
[1823.22 → 1830.46] so walk me through the getting started then with 3.0 do you create a new Jekyll site do
[1830.46 → 1835.56] you clone something do you install a gem what's the process so yeah you just create a new Jekyll site
[1835.56 → 1840.06] I'm still working on the migration for two so I'm not really ready to talk too much about that I'll tell
[1840.06 → 1845.12] you how hard it is in a little bit if you want but um if you uh is you have a Jekyll site you basically
[1845.12 → 1850.78] just need to install the octopuses gem and that will come with um you know I've broken things out
[1850.78 → 1856.00] a lot there are a lot of separate little pieces and octopuses the main gem doesn't include most of
[1856.00 → 1864.38] the plugins it is mainly a CLI and a few other goodies so um it has an uh it has really nice tools
[1864.38 → 1872.72] for working with posts pages drafts um and deployment and so you can uh you know what one of the things it
[1872.72 → 1877.32] does is kind of like rails generators where you can kind of create a bunch of files that you know
[1877.32 → 1883.98] set up uh pages for you, you can just uh with the octopuses command line you can run a command to
[1883.98 → 1889.30] create a new post or a new page and octopuses introduced this concept of post and page templates
[1889.30 → 1894.68] and so you can actually there's a little templates directory where you can add any kind of file you
[1894.68 → 1900.24] want to and put you know HTML markdown whatever you want and general front matter and when you create
[1900.24 → 1903.92] a new post you can tell it to use a certain template as default, or you can have like let's say you're
[1903.92 → 1908.46] writing sponsored posts you can tell it to use a sponsored template, and it'll generate a new post
[1908.46 → 1913.18] with the name you have and the date and everything and use your template which is just kind of a nice
[1913.18 → 1919.92] thing to have for Jekyll um it also has I like that yeah it's pretty nice uh it just makes things
[1919.92 → 1924.52] faster because you know if you don't if you don't know much about Jekyll you there's like a lot of
[1924.52 → 1928.90] it's file system based and so there is what the whole thing is but a lot of it is particularly
[1928.90 → 1934.42] file system based instead of metadata based so you have a file that is in a specific place in
[1934.42 → 1938.22] a post directory with a date in the file name and all kinds of things in order for Jekyll to
[1938.22 → 1943.00] consider that a post and it and the way it treats it so it kind of just takes care of all that work for
[1943.00 → 1951.90] you also there's go ahead Jekyll added a new concept of drafts in I think 2.0 maybe one I can't remember
[1951.90 → 1956.04] and drafts are cool because they live in a separate drafts directory
[1956.04 → 1962.38] and you can generate your site with drafts, or you know normally generating it doesn't include
[1962.38 → 1966.08] the drafts but if you want to publish a draft you have to move it over to the post directory and
[1966.08 → 1970.98] change a bunch of metadata and do different things and let's say you write a draft three days ago and
[1970.98 → 1977.60] now you have to add a date for it, and you know it's using um ISO 8601 dates and so it's like do i
[1977.60 → 1980.74] really want to type this out, and it's just stuff like that it's like hey a computer can do that for me
[1980.74 → 1987.42] so I added an uh command for creating this thing say octopuses new draft and give it a title and
[1987.42 → 1990.60] it will dump it in your drafts folder you write it do whatever you want, and then you can just say
[1990.60 → 1997.64] octopuses publish, and you can type uh any it's like a search string for uh the title of that draft
[1997.64 → 2001.46] and it will take that draft, and it will convert it into a post and publish it into your post directory
[2001.46 → 2006.56] and you can also unpublish posts so it is works the same way and if you have like let's say you um
[2006.56 → 2013.70] are writing about I don't know cars you can say octopuses unpublish uh cars, and it will show you
[2013.70 → 2018.04] all the posts that have uh the word cars in the title and let you pick the one, and it moves it to
[2018.04 → 2029.20] drafts that's cool yeah I like I remember I guess what has become the CLI before it was a rake file
[2029.20 → 2034.82] you know I remember your deployments and stuff like that and I think you and I had similar ways to deploy
[2034.82 → 2040.34] static file system based sites because I was using middleman I think before I was using serve
[2040.34 → 2046.76] from yet again john long um which actually now that I remember it now that's what the sasway.com
[2046.76 → 2052.78] originally was it was a serve site, and then we moved it to middleman um but I recall like what was
[2052.78 → 2059.70] you know now the CLI I think was just basically a rake file um can you talk a bit about the know i
[2059.70 → 2065.74] guess this process to the CLI that do you mentioned that uh octopuses 3.0 is leveraging
[2065.74 → 2070.92] you know many gems that you may or may not have installed, and you can install one do gems sort
[2070.92 → 2078.40] of come in and add on to the CLI like how expensive is the CLI system you have um so yeah any gem created
[2078.40 → 2084.00] for octopuses can extend the CLI and so for example the deployment gem is separate so octopuses deploy
[2084.00 → 2091.96] is at uh you know GitHub.com slash octopuses slash deploy it has uh all the deployment stuff and the
[2091.96 → 2096.36] reason I did that is I wanted to have those tests handled separately to have a pull request handled
[2096.36 → 2101.54] separately all that kind of thing and so that extends the CLI so you can say octopuses deploy
[2101.54 → 2108.96] unit s3, and it will generate a deployment YAML file for deploying to a s3 system so you can configure it
[2108.96 → 2113.82] for cloud front you can add you know you raws keys or have those be read from your Novara
[2113.82 → 2120.62] um you can say I want to deploy to sync or git based deployment for Heroku or GitHub pages or
[2120.62 → 2126.12] whatever, and it'll generate uh a deployment YAML for you and then when you just run octopuses deploy
[2126.12 → 2131.68] it's you know it's requiring that gem it's looking its extending the CLI and so it recognizes that
[2131.68 → 2136.24] command, and then it finds the deployment YAML and figures out where your settings are and runs all
[2136.24 → 2142.12] this crazy stuff and deploys it and it uh it's its also nice because you can tell it to use a
[2142.12 → 2147.02] specific configuration if you want to deploy to a staging site that maybe you have some on some
[2147.02 → 2152.06] server that's password protected so you can easily show previews to people uh you can do that kind
[2152.06 → 2156.68] of thing with just telling it to use a different configuration than whatever the default is so it
[2156.68 → 2163.84] seems to me like Jenůfa has always been the hacker's blog system right and this seems like octopuses
[2163.84 → 2168.56] takes it like it does make it a Ferrari now that I'm hearing more about this like it definitely
[2168.56 → 2174.24] you know for someone who loves to tinker people that remind me of tinkers is like win uh jarred
[2174.24 → 2178.78] you're a tinkerer man it seems like this is the kind of thing that I'm a tinkerer too but I mean i
[2178.78 → 2183.54] think that i I imagine you and win are like for sure tinkers you love playing with things like that
[2183.54 → 2188.70] and you know you would dig in and start using Jekyll and then start using octopuses and like
[2188.70 → 2193.82] little by little start pulling in different gems into your processes into your system and maybe even
[2193.82 → 2198.88] write your own and leverage the CLI and like this is a hacker's paradise to me, I think let me just
[2198.88 → 2205.50] speak to that real quick here uh I think when I first saw octopuses back in the day it was a
[2205.50 → 2211.76] blogging theme for Jekyll and that wasn't all that attractive to me because like well I can write you
[2211.76 → 2216.34] know I can do a theme and I understand Jekyll and so you know what does it bring besides I really loved
[2216.34 → 2222.46] your code folding thing when you hover over a piece of code, and it unfolds the page so you'd see the
[2222.46 → 2228.54] whole thing that was rad i kind of wanted that on my blog, but this sounds more like I mean man the
[2228.54 → 2232.88] Ferrari thing makes sense and once you have some context because this sounds like a bunch of tools
[2232.88 → 2240.56] sitting on top of Jekyll making it just more uh nice to work with um you have to do less plumbing
[2240.56 → 2244.88] yourself, but then you can build your own tools and integrate them into the system so it almost feels
[2244.88 → 2251.48] like a layer on top um as opposed to just a starter theme I'm curious if there's theming involved as
[2251.48 → 2257.96] well I'm kind of oh we'll get to that I think there is okay oh surprises okay um but yeah this
[2257.96 → 2263.40] this take on it maybe this was what octopuses has been I mean obviously it's a new architecture but
[2263.40 → 2266.80] maybe some of these things were there from the beginning and I just didn't see the light because
[2266.80 → 2271.36] I just thought it was just a blogging theme uh it sounds like either the scope has you know has
[2271.36 → 2277.16] changed or um you're kind of just speaking about parts that maybe I wasn't privy to previously
[2277.16 → 2282.84] also it did have the option to deploy, and it did have new page themes and some of the know or
[2282.84 → 2286.72] um yeah systems it didn't have a emulating system for pages and so if you wanted to
[2286.72 → 2293.34] you know back in 2.0 if you wanted to change what your default uh new post or something looked like
[2293.34 → 2299.14] you had to edit the rake file like its stupid stuff like that, and so I'm you know rebuilding a
[2299.14 → 2304.08] lot of these things and expanding the idea because now I've extracted a lot of this into something
[2304.08 → 2309.88] tiny and I can say I'm going to solve the problem of how do you um you know publish a
[2309.88 → 2314.16] draft like what does that look like what is the best user interface because I could say oh yeah
[2314.16 → 2319.84] if you want to unpublish a post just you know pass the path you can do that it'll accept the path but
[2319.84 → 2324.00] it'll also accept a file name and if it can't find that file it'll search in the post directory
[2324.00 → 2329.54] you know for file names that match that so it's like I'm just thinking what is the nicest user
[2329.54 → 2333.44] interface because that's seen I'm a designer at heart this that's why this has been such a big
[2333.44 → 2340.12] learning process for me um and so a lot of my interest is um making something that feels like
[2340.12 → 2346.86] it respects me as I use it and um and so some of the fun for me is just saying you know what is i
[2346.86 → 2351.44] have this one tiny thing that I'm working on how can I make this as nice as possible and that's also
[2351.44 → 2359.42] why it's taking me a long time yeah, yeah so another cool thing um it's it octopuses isn't just about
[2359.42 → 2365.38] working with your Jekyll site it's also about open source around Jekyll, and so I've written some
[2365.38 → 2372.64] other cool things one is fun uh do you guys ever use um a ruby debugger yeah like a command
[2372.64 → 2381.10] line one sure price I bug uh sound familiar cool so octopuses brings that to Jekyll templates so
[2381.10 → 2388.70] there's an um octopuses uh debugger uh gem that you can install and allows you to I don't know if
[2388.70 → 2393.96] you're familiar with liquid, but it's like moustache percent and then whatever percent moustache so you
[2393.96 → 2400.06] can say you can add a debug tag in a post or page, and you can actually like step through a loop as
[2400.06 → 2404.68] liquid builds your site and so for people who are and if you know goes to the command line so you can
[2404.68 → 2408.34] like test you know local variables you can do all kinds of cool stuff and see what's happening
[2408.34 → 2413.84] and so as you're working on plugins you can use octopuses debugger to say you know what's happening
[2413.84 → 2417.98] here why isn't this freaking working instead of having to like figure out how to you know write
[2417.98 → 2422.28] stuff to a file and then read the files or things are breaking it's just so much easier um there's
[2422.28 → 2430.06] also an under uh on GitHub on math is clash c-l-a-s-h there's an uh gem called clash it has a
[2430.06 → 2435.92] command line, and it's all about a testing framework for Jekyll which I wrote in order to make it a lot
[2435.92 → 2442.02] easier to write these uh all these cool plugins and frameworks and what it does is it uh it has
[2442.02 → 2447.88] its own scaffolding and stuff so you can easily get started with a new uh Jekyll um project so if
[2447.88 → 2453.76] you want to create a gem that adds some nice features to Jekyll you can use clash to build the
[2453.76 → 2461.44] Jekyll site and compare uh generated um pages to whatever your expected is so you just um you know
[2461.44 → 2465.82] set up your plugin let's say it's a liquid tag or something generate your Jekyll site and then say
[2465.82 → 2469.56] okay this is how I expect it to look you just you can run a command that just says accept those
[2469.56 → 2475.54] changes, and it will um create you know test files and stuff that that match how it looks and then
[2475.54 → 2479.62] it'll always it'll run diffs against that stuff and so you'll see these nice little diff outputs when
[2479.62 → 2484.76] you're running it and I test basically everything I've written with that it's pretty cool huh yeah so
[2484.76 → 2492.90] I'm on autopress GitHub.com slash autopress, and it looks like you have dozens of uh repos here
[2492.90 → 2498.46] several pages yeah several pages there's about 30 repos so you got code blocks syntax highlighting
[2498.46 → 2503.80] you got ink which is a core component for building gem-based Jekyll themes little foot fancy footnote
[2503.80 → 2509.72] pop overs with native JavaScript for any Jekyll site all sorts of goodies out here asset pipeline
[2509.72 → 2514.76] yeah hello yep uh so yeah there's other cool stuff social share buttons I'll talk yeah social share
[2514.76 → 2519.48] buttons yes so little foot is a thing I released recently because you probably guys have probably seen
[2519.48 → 2524.88] Bigfoot JS I got Bigfoot on my blog all right so basically I don't want everybody to have
[2524.88 → 2530.54] jQuery who wants to have nice footnotes on their Jekyll site yes and so any Jekyll site you have
[2530.54 → 2538.14] you can just add um octopuses little foot, and it will use all native JavaScript, and it basically does the
[2538.14 → 2542.26] same thing that Bigfoot does oh, and it comes with style sheets and everything that are automatically
[2542.26 → 2546.52] integrated into your site I'm putting that in my blog this weekend yeah check it out it's cool to let me
[2546.52 → 2555.38] know how it goes for you, I will so you're using Jekyll jarred oh yeah okay oh yeah I missed
[2555.38 → 2560.28] that part okay yeah my personal website's been Jekyll and my company's website's a Jekyll site that
[2560.28 → 2564.70] one's on GitHub pages my personal site is just on uh an old dream host account because I don't have
[2564.70 → 2574.36] just because uh but yeah it's been on Jekyll for years, and you know over time i so I heard you
[2574.36 → 2578.72] mentioned Jekyll earlier I just didn't know that you said that your blog was in Jekyll I just guess
[2578.72 → 2583.96] I didn't put two and two together yeah I've been I've been using Jekyll for a while and um you
[2583.96 → 2592.26] know honestly over time it's lost its lustre I sometimes dread aspects of making changes to my
[2592.26 → 2597.76] sites I don't write very often and I try to blame that on Jekyll even though it's not really his fault
[2597.76 → 2603.20] um so some of this stuff in octopuses is really starting to take I like how you both have tickled
[2603.20 → 2608.60] my fancy a little bit what's that the male perspective, and it's a person you both act like
[2608.60 → 2614.66] Jekyll's a person well because he's got a Ferrari and he and he stops me from blogging there you
[2614.66 → 2619.26] go gotta blame somebody I know that he's my way if you're gonna not if you're gonna not blog do it
[2619.26 → 2622.94] on a static site because that's right to worry about having to update things getting hacked so
[2622.94 → 2629.18] speaking of the Adam jarred you pointed out I guess you googled that no so in our back channel
[2629.18 → 2635.04] we were talking previously about uh the web 2.0 show Adam found the link, and he placed it in the
[2635.04 → 2640.98] Skype back channel um and Skype went out, and you know skype tries to get fancy now, and they go out
[2640.98 → 2647.82] and they grab a preview of the page with the page title I hope I'm not saying too much here Adam but
[2647.82 → 2655.62] no it's cool, but it was some uh some old WordPress site I'm assuming yeah it's a WordPress
[2655.62 → 2660.38] I've been meaning to make it static forever now, but it's like the lowest thing on my totem pole to
[2660.38 → 2664.60] to deal with he pasted me a link to it just so we have it for the show notes, and it said buy Cipro
[2664.60 → 2670.50] without prescription oh yeah right in this page title so I said yeah you got hacks this is an
[2670.50 → 2676.84] unmaintained WordPress site it still runs which is great, but it's also that's the problem is it still
[2676.84 → 2683.52] runs right yeah yeah anyway so yeah that's that's that's bad news there so good we did find a link
[2683.52 → 2687.36] to that GitHub show from way back in the day but don't visit the site because you might get malware
[2687.36 → 2694.98] machine no maybe yeah just don't click in the audio files hey my worst ever was um I think some gallery
[2694.98 → 2700.96] plugin for WordPress someone ended up installing some kind of uh backdoor system for hacking banks
[2700.96 → 2707.74] on my shared PHP host so yikes I was like oh okay let's get rid of this thing as quickly as possible
[2707.74 → 2715.42] I do not want to get in big trouble no doubt so uh since we're talking about some of the repos
[2715.42 → 2723.56] on the octopuses org one that I see um that's lacking, and you can tell me why is the docker one
[2723.56 → 2729.70] well is there an image is there not an image as read me oh that's not actually me yet uh that's uh
[2729.70 → 2736.48] Jordan who also works on jackal uh said he wanted to create a docker image for octopuses I said go for
[2736.48 → 2742.26] it so I created him a repo and gave him some permission so oh okay yeah okay so it's its coming
[2742.26 → 2747.04] and it's coming well I see you got to commit here so I got you to blame yeah go ahead blame me I don't
[2747.04 → 2751.96] mind it's all it's all you're not there are plenty of other goodies in there that are worth talking about
[2751.96 → 2756.50] no, no no I'm just no of course well the reason why I say that is because
[2756.50 → 2762.32] only because of the getting started we talked about earlier which is how it how much work it
[2762.32 → 2767.98] takes to get started with the old version of octopuses um you know having ruby not having you
[2767.98 → 2772.02] know all these different scenarios here and docker obviously flattens that playing field quite a bit
[2772.02 → 2776.86] so if there was docker out there and all you had to do was have docker on a machine, and you could
[2776.86 → 2781.84] pretty much have an environment ready to go to run this new octopuses site and really
[2781.84 → 2787.60] make it uh you know a top of the line Ferrari you know yeah the cats working on Jekyll are
[2787.60 → 2793.94] really um excited about getting Jekyll on docker and I think everybody kind of wants to make it so
[2793.94 → 2798.66] much easier to get started with this stuff because i you know I mean a lot of governments use Jekyll for
[2798.66 → 2805.02] their sites, and it would be awesome for people to just want to have a site that they don't have to
[2805.02 → 2810.06] worry about managing an admin interface for and updating stuff like if they just wanted to be really
[2810.06 → 2814.52] simple it'd be great for them to have an easy way to install that I still don't think that docker
[2814.52 → 2818.88] isn't an easy way to do everything yet, but it's getting closer I mean you know it's it is getting
[2818.88 → 2823.54] closer it is getting closer one step I mean one of the reasons I was really excited about building a
[2823.54 → 2828.14] CLI for octopuses is just because that allows people to do all kinds of extra things you know
[2828.14 → 2833.14] it'd be easier to write a GUI or something on top of that anything that can just farm commands out to
[2833.14 → 2840.80] octopuses uh it just opens it up more so um but yeah there's some other cool stuff in here um so
[2840.80 → 2846.90] let's see what are some of your favourites so you're going to tell us which one gave you the most joy
[2846.90 → 2851.14] oh well yeah I'll tell you what the coolest one is it has the least docs right now because actually
[2851.14 → 2855.10] the docs are in another folder they're not in the README um but octopuses inc is freaking awesome
[2855.10 → 2861.14] it is the theming system for Jekyll and the Jekyll maintainers are basically in the have a
[2861.14 → 2866.94] Jekyll talk I think it's like talk.jekyllrb.com um where they're saying yes people should be using
[2866.94 → 2874.46] inc if they want to do Jekyll theming uh, and it's its the main reason that I haven't put the uh
[2874.46 → 2880.84] final um yes uh octopuses 3 is out this is exactly what we should do to use it post up on octopress.org
[2880.84 → 2887.84] um because I'm not quite done and I want to get all the documentation in so um octopuses inc is a
[2887.84 → 2896.28] system for making it really easy to write plugins um for a Jekyll site so it handles the asset pipeline
[2896.28 → 2903.18] management it handles uh it adds CLI commands for working with your plugin so for example on that
[2903.18 → 2908.76] littlefoot.js thing that is built on octopuses inc and when you install that you'll put a
[2908.76 → 2915.20] CSS asset tag and JS asset tag liquid tag on your uh in your head or foot or wherever you want to put
[2915.20 → 2924.20] it and octopuses inc will generate an um fingerprinted uh compressed style sheet in JavaScript
[2924.20 → 2930.54] uh and inject the know script tags and stuff in that place, and it'll put it on your site uh you
[2930.54 → 2936.60] can also manage the compression settings and stuff you can say I want all plugins to generate their own
[2936.60 → 2942.72] uh files so you can troubleshoot stuff really easily, but basically you have uh you know once you
[2942.72 → 2947.72] install that you have any octopuses inc plugin you install automatically gets combined into a
[2947.72 → 2954.98] single um style sheet or JavaScript, and it's based on your gem load order or whatever also uh the
[2954.98 → 2960.68] octopuses asset pipeline adds um adds your own local style sheets and stuff to that asset pipeline
[2960.68 → 2969.10] which is nice but the uh the cool thing also about all this is that um when you're using octopuses inc you
[2969.10 → 2976.68] have each plugin has its own configuration and so you can run like octopuses inc list, and it will show
[2976.68 → 2980.48] you all the plugins you have installed in the command line with information about them and what assets
[2980.48 → 2986.76] they come with so you can include JavaScript style sheets um you can use coffee script or SAS you can do
[2986.76 → 2994.48] uh you know images pages you can use generators that uh can create index pages with pagination
[2994.48 → 2999.68] uh it's all multi-language oh yeah it's another cool one uh octopuses multilingual lets you do
[2999.68 → 3003.68] multi-language just wait there's more yeah I mean there's so there are so many things, and they're all
[3003.68 → 3008.36] really cool like the multi-language stuff is super neat if you have a site that you want to post in
[3008.36 → 3016.10] multiple languages you can have separate feeds separate indexes uh tags indexes uh category index like
[3016.10 → 3021.80] all these kinds of cool things um for it for whatever languages you are uh writing about and um
[3021.80 → 3028.10] let's see uh oh yeah and so with octopuses inc you can also run a command that will generate a
[3028.10 → 3033.20] plugin scaffold that is a gem and all you have to do like if you wanted to put out some JavaScript
[3033.20 → 3037.78] and style sheets like that's that you just want to write a theme or something all you have to do is
[3037.78 → 3042.88] dump those into a JavaScript's directory and a style sheets directory, and then you can bundle up the
[3042.88 → 3046.08] theme and send it and when somebody installs that automatically gets installed to their asset
[3046.08 → 3053.36] pipeline very nice so it's really cool a lot of neat stuff lots of goodies well let's take a break
[3053.36 → 3058.68] here we'll hear from a sponsor uh on the back side of the sponsor break we will talk perhaps about the
[3058.68 → 3064.10] roadmap to 3.0 what steps have been taken what steps still need to be taken maybe we'll try to pin him
[3064.10 → 3069.96] down on a release date for this thing let's take a break, and we'll be right back you've heard me talk
[3069.96 → 3074.94] about top towel several times in this podcast but today is different I've got a special treat for you
[3074.94 → 3082.10] I went out and spoke with a listener who a year ago had never heard of top towel he listened to the
[3082.10 → 3086.64] show just like you're doing right here right now today and heard us talk about top towel and what
[3086.64 → 3092.10] they're all about, and he decided to get in touch, and now he's living the dream as a freelance software
[3092.10 → 3097.10] developer with top towel his name is Daniel Alton and I sat down and I talked with him, I said hey
[3097.10 → 3104.04] what is it that you love most about top towel take a listen well for me the thing about top towel
[3104.04 → 3109.92] which I thought would be very hard for me personally as I transitioned to a more consulting role
[3109.92 → 3117.78] uh was the way I would have access to new clients and what quality of those would be so I found that
[3117.78 → 3122.76] I've had access to awesome clients through top towel, and it hasn't been that hard to find because
[3122.76 → 3129.00] they have a lot of choice and even more than that uh there's enough choice and i I can actually be a
[3129.00 → 3134.56] a little selective about what kinds of things I want to be working on so I use that as a way to
[3134.56 → 3140.08] sort of hone my skills, and you know go towards the technology that I think are worth investing in
[3140.08 → 3145.66] for the future so whether it's you know including new front-end frameworks or doing a little DevOps
[3145.66 → 3151.44] work on the side i I usually am able to find clients who are had the needs of the things I want
[3151.44 → 3158.08] to get better at so that's been that's been truly useful all right that was Daniel Luzon a listener of
[3158.08 → 3164.38] the change log and also a freelance software developer with top towel if you want to follow
[3164.38 → 3173.92] in Daniel's footsteps go to top towel.com slash developers that's t-o-p-t-a-l.com slash developers
[3173.92 → 3178.80] to learn more about what top towels all about and tell them the change log sent you
[3178.80 → 3186.36] all right we are back talking about octopuses with Brandon Mathis Brandon you had on a recent
[3186.36 → 3193.42] blog post on the octopress.org uh an announcement about octopuses 3.0 is coming this was in January
[3193.42 → 3199.30] we're recording this in June still not here that's all right software is hard, and you have been
[3199.30 → 3205.44] releasing all sorts of goodies along the way um, but you also published a release plan and in that plan
[3205.44 → 3212.64] uh you have kind of six steps to a 3.0 release curious where you're at uh with things step one
[3212.64 → 3218.20] was finish octopuses genesis um you had written a migration guide step three was moved the master
[3218.20 → 3224.40] branch to the legacy branch um switch to a GitHub org which you've done that obviously and then new
[3224.40 → 3232.72] doc site and then release octopuses as 3.0 and octopuses inc as 1.0 where you are in that release plan
[3232.72 → 3240.92] uh so basically I am at I still have to move I'm at this octopuses to the octopuses org right now i
[3240.92 → 3246.24] just have two repos and I really don't want to have that old one any more um even though I've always
[3246.24 → 3251.08] been confused about that I wasn't sure which one was the canonical yeah well octopress
[3251.08 → 3256.76] will be the canonical will be yes, but it isn't now well I mean it is for 3.0 the other one is just a
[3256.76 → 3262.08] vestigial uh repo oh so it's only for legacy then right that's and so that'll be a branch or something
[3262.08 → 3267.94] on whatever the current one or on octopress so um I still need to do that and
[3267.94 → 3273.42] it's just kind of one of those things where I want to have the migration guide written and published
[3273.42 → 3278.10] so that when people are like trying to figure out how to clone this thing and run this stuff that
[3278.10 → 3282.70] you know the site needs to be done for that to happen all the stars will turn into hate mail yeah
[3282.70 → 3290.60] right it's uh yeah i have to it's its a little bit um overwhelming uh given the popularity of
[3290.60 → 3295.50] the current version of octopuses trying to make some of these changes and uh I still hear from
[3295.50 → 3299.52] people who are they having no idea that this is happening even though there's a post about I need
[3299.52 → 3307.22] to do a better job of communicating about it but anyway um that's why I'm here so the uh talk about
[3307.22 → 3311.96] the doc site actually is one of the other cool things that I forgot to mention that octopuses CLI does
[3311.96 → 3319.00] um so if you have a bunch of gems installed that are octopuses gems or even if you guys write gems
[3319.00 → 3323.54] and uh you can add a little snippet of code that will register them with documentation
[3323.54 → 3329.56] so you can run octopuses docs from the command line, and it'll launch a Jekyll site that has the
[3329.56 → 3333.94] documentation it'll suck in the README and the changelog, and you can add additional docs pages as
[3333.94 → 3339.54] well for any of the plugins you have installed on your site so you can read without having to go to
[3339.54 → 3343.40] GitHub it's all local you know installed in your gems you can read all the documentation for
[3343.40 → 3348.54] everything installed, and so I'm using that same system of collecting documentation from
[3348.54 → 3355.34] um gems and repositories and stuff for building the site and so everything that you know all of
[3355.34 → 3359.98] the plugins I have their documentation is in the README and some of them if they have additional
[3359.98 → 3364.30] things like you know walkthroughs or things like that they can put that in the uh there are a docs
[3364.30 → 3369.48] directory that octopuses inc uh creates if you're creating an inc plugin, or you can anyway
[3369.48 → 3375.32] those are all like implementation details, but basically you can easily add documentation to
[3375.32 → 3382.06] different gem plugins and that's what uh the new site is going to use and so finishing that is uh
[3382.06 → 3388.56] currently uh happening and I am trying to finish up the new default theme because the power of a
[3388.56 → 3396.10] default theme surprises me as you guys have already mentioned oh yes so I really want to get this to be a
[3396.10 → 3402.68] lot better um to be really nice is it a redesign or a real line oh it's well it's all it's just all
[3402.68 → 3407.52] starting over I mean web development has changed so much you know we're all using SVG stuff or whatever
[3407.52 → 3414.20] now there's just better ways of doing things um, and so I'm trying to embrace a lot of that and
[3414.20 → 3418.38] come up with a nice looking theme that people want to use that has a lot of flexibility you know people
[3418.38 → 3423.36] like these large image headers and stuff like that I want to make it easy to add those to posts and
[3423.36 → 3429.00] it's a lot of it is just kind of deciding you know I've built something that works but i kind of want
[3429.00 → 3434.84] to rip it apart and do it again a little bit which is its you know it reminds it seems like you
[3434.84 → 3442.12] would do that yeah um not in a bad way, but you seem like you have a high threshold for satisfaction
[3442.12 → 3449.50] like you uh you want things to be really, really good and that's good yeah well it's I mean a theme is
[3449.50 → 3455.72] such a hard thing to do it's like I'm combining uh I've written so many special liquid tags just for
[3455.72 → 3462.16] making theming easier things that uh like conditionally render a partial based on some
[3462.16 → 3468.68] configuration um, and you know there are so many different things that happen under the hood in a
[3468.68 → 3474.20] template just to generate good HTML um and getting all of that so that it's easy for somebody to work
[3474.20 → 3477.92] with I'm thinking about how the user will come to this and I don't want them to have to mess with this
[3477.92 → 3484.76] stuff if you have a theme that's been built on octopuses inc you can uh you can run a command
[3484.76 → 3492.80] and it will copy from the gem um all the assets so like the layouts the includes um images anything
[3492.80 → 3499.06] that you know fonts whatever comes with your theme can be copied to an override location in the plugins
[3499.06 → 3503.88] directory of uh the site you're working on, and then you can delete whatever you don't want to override
[3503.88 → 3510.30] but anything that's there will automatically just override your theme uh from the gem and so it makes
[3510.30 → 3513.74] it is really easy to edit these things, and so I'm thinking a lot about if someone does want to edit
[3513.74 → 3517.88] these I want to break them up in a way that's very easy to edit and so there's just there's a lot of
[3517.88 → 3524.08] consideration that goes into just that part let alone the CSS so yeah it's its intense uh but
[3524.08 → 3530.74] this is your own monster though right like you made this monster right it's its as complex as you make it
[3530.74 → 3538.72] well I mean if it's the thing is her it's like a lot of uh, uh and this is the right way to do
[3538.72 → 3544.50] theming especially for a static site this is just a's a really nice way to work with it and the
[3544.50 → 3548.48] burden that I'm putting on myself is setting up a pattern you know I imagine that people are going
[3548.48 → 3553.66] to fork my theme and then ditch the style sheets and write their own or use this as a way of learning
[3553.66 → 3560.68] how to do uh themes for Jekyll yeah, and so I want to really give good patterns to everyone so you know
[3560.68 → 3566.66] as this begins to take off people will say you know oh i can easily create a theme this
[3566.66 → 3570.88] has everything I need except I want to change these things about it and so rather than getting pull
[3570.88 → 3577.50] requests and having to manage you know this one repo that is the only way to do everything uh it's just
[3577.50 → 3583.34] and people can easily fork and create their own stuff and um and release gems for them so yeah
[3583.34 → 3589.42] it's that's I want to have once I have that theme where I like it then I can build the documentation
[3589.42 → 3597.30] I can, you know make the documentation I can make the documentation site use that theme and then I can
[3597.30 → 3601.88] replace the docs as they are now and so that's really what the theme is off the press genesis is
[3601.88 → 3606.24] that right okay so genesis is the theme name I thought that was maybe your code name for
[3606.24 → 3611.26] the core I wasn't sure either yeah yeah that's the theme name I guess this is all new we didn't
[3611.26 → 3616.66] talk about this what's what's genesis oh yeah so genesis I mean you can try using it now it does work
[3616.66 → 3624.16] um, but it's not super well documented but that is you can dig around in the uh that repo I think it's
[3624.80 → 3630.28] October's last genesis theme um, and it will kind of give you an idea of what it's like to build
[3630.28 → 3636.18] something uh for uh Jekyll theming so yeah as a total sidebar
[3636.18 → 3641.16] uh for those listening perhaps when you say when you say octopuses ink it's easy once you read it
[3641.16 → 3645.42] but if you haven't read it makes it sounds like you're starting a corporation around octopuses
[3645.42 → 3649.78] yeah it's like the know that's i-n-k that's not uh ink comma
[3649.78 → 3656.30] yeah yeah I thought of it kind of like you know uh if is an octopus was going to create art it would
[3656.30 → 3664.10] use its ink right kind of cheesy kind of cute I don't know nice both nailed it I embrace it
[3664.10 → 3672.62] so finish the theme octopuses genesis the migration guide it's in progress um so basically I have
[3672.62 → 3677.12] migrated the original doc site to use octopuses 3 I haven't published it from that yet because
[3677.12 → 3683.50] there are some other things I want to change um but the tricky part about explaining to people how
[3683.50 → 3690.90] to migrate is that people if they just use the stock octopuses uh clone, and they add their own
[3690.90 → 3697.26] stuff to if it's super easy especially if they want to ditch the theme uh all I've replaced all
[3697.26 → 3702.76] the plugins that I wrote for the original octopuses with separate gems so they can add what they want
[3702.76 → 3708.04] to use and what they don't, and it won't break but if they made a bunch of changes and their site
[3708.04 → 3714.54] depends on those changes to build then it's like um choose your own adventure pal sorry uh you know
[3714.54 → 3721.04] you I helped you create this monster and I can only apologize um but yeah that it is it's kind of
[3721.04 → 3725.60] there's going to be a golden path that should be simple for anyone um, and you know at the end of the
[3725.60 → 3730.32] day it's all if it's a bunch of markdown files in a post directory, and you just want to migrate your
[3730.32 → 3736.36] content you can just create a new Jekyll site add the theme gem and dump it in there, but you know
[3736.36 → 3740.62] if people got really crazy with ruby, and they wrote tags that depend on weird things like you
[3740.62 → 3744.18] know you just never know what somebody's going to have done and so that part is a little bit daunting
[3744.18 → 3751.00] for me to say uh try this you now and then write me all kinds of email for help well from my
[3751.00 → 3758.06] perspective I think if if you see the octopuses 3.0 is the new better hotness the red Ferrari as
[3758.06 → 3764.16] we talked about you'd want the all the attributes of the red Ferrari you wouldn't want to like you know
[3764.16 → 3768.90] take the skin off the red Ferrari and put it on your jalopy civic anybody's driving a civic out
[3768.90 → 3773.84] there sorry about that but just put a big wing on the back man it'd make it go faster yeah I mean i
[3773.84 → 3779.54] would want to get rid of anything fun I might have done I guess if it's sort of case by case but yeah
[3779.54 → 3783.44] and that's that's a really hard part is you know you write a guide and it and somebody sits there and
[3783.44 → 3786.52] tries it on their site and like why doesn't it work, and they're like well remember two years ago when
[3786.52 → 3794.14] you added this ruby, and you did this thing, and you broke all this stuff well uh yeah so you stand to
[3794.14 → 3799.16] you stand that's why it is a point release too so there are breaking changes oh massive breaking i
[3799.16 → 3805.06] mean nothing about it is similar right so migration guide is in progress to a degree at least you have
[3805.06 → 3811.52] an idea what you want to say right I've written it several times so we're getting there so moving the
[3811.52 → 3817.82] master branch to the legacy branch for maintenance is that that's pretty easy right uh yeah or no that
[3817.82 → 3823.48] should be pretty I mean it's its just a matter of uh creating an uh clean branch and then
[3823.48 → 3830.46] you know adding all the content from the current uh octopuses I'm at Mathis and then just um you
[3830.46 → 3836.24] know GitHub makes it very easy to move one repo to another and the reason I would do that is because
[3836.24 → 3840.40] um you know there are probably tons of links out there pointing people to octopuses, and they're
[3840.40 → 3845.44] pointing them to Mathis octopuses and I want people to find the new good stuff instead of see some
[3845.44 → 3851.94] broken page or see some pages oh go here like it's just, or you know people that are uh they who start it
[3851.94 → 3855.20] because they want to follow it you know maybe they don't know like this is another way to signal to
[3855.20 → 3859.22] them hey this is a new thing, so there's you know that's a perfect point to mention there I think
[3859.22 → 3864.92] say that again because that's that's something I think people will experience where they have a
[3864.92 → 3871.52] popular project on you know on a personal uh user and then move it to an org have you researched this
[3871.52 → 3876.76] a ton like is there a blessed way to do this without losing stars and watchers and redirects and I mean
[3876.76 → 3882.98] I know GitHub makes it easy but is it harder than it seems uh yeah I mean it can be it is just depends
[3882.98 → 3887.54] you know a lot like the thing that I hate about it is that the issues follow you right and there are
[3887.54 → 3891.84] a lot of open issues that I'm just going to go through and close and say this is you know no longer
[3891.84 → 3899.32] supported um and if you want to fork this and maintain the separate thing you know I'm I'm happy
[3899.32 → 3906.44] to encourage you not to do that because it is will only result in pain but uh yeah it will only result in
[3906.44 → 3913.88] pain that's all that's coming from that uh it's yeah so i I think the that's the that's the main
[3913.88 → 3917.96] thing that I don't like about it is all of a sudden I have new issues that I have to go through and
[3917.96 → 3923.96] and you know I try to be i oh gosh I'll say the people who have been using the new stuff have been
[3923.96 → 3928.46] awesome uh people have filed lots of issues there's been lots of pull requests, and it's been so much
[3928.46 → 3935.40] easier to maintain it I've had um you know a lot of help and um it's been really encouraging to see
[3935.40 → 3939.32] how quickly I can get new stuff out and release new versions and not have to worry about breaking
[3939.32 → 3946.70] anybody's stuff um so uh I am already very blessed by the new system with all the separate gems that
[3946.70 → 3952.38] each solve their own little problems and yeah I look forward to more users getting to enjoy that
[3952.38 → 3959.58] so the real time-consuming things then really seem to be obviously wrapping up the theme which we
[3959.58 → 3964.48] realize how important that is the migration guy was super important uh the new doc site which
[3964.48 → 3970.08] leverages genesis so that's sort of the blocker there just talking in terms of agile I guess and
[3970.08 → 3975.70] then uh to top it all off the cherry on the top is release octopuses 3.0 and octopuses inc
[3975.70 → 3981.82] right yeah uh finish all the documentation for octopuses inc um and some of that you know if I have a
[3981.82 → 3986.84] perfect theme that people can use I have some time to explain this documentation yeah I have some
[3986.84 → 3992.76] I mean it has some documentation to it, but it's I want to be able to write guides like that's to me that's
[3992.76 → 3996.78] the higher level documentation explaining what a method does and what commands you can use that's
[3996.78 → 4002.00] great but I want to say to somebody um okay you just started using this first time you have no
[4002.00 → 4007.24] idea what's going on here's a story you can read that will tell you um what you're going to encounter
[4007.24 → 4012.98] and uh you know what you know what you're going to need as you're going to need it so or if you're
[4012.98 → 4015.84] interested in this other thing here's another cool you know people are going to come at this from
[4015.84 → 4022.18] different angles and so finding ways to explain that to them, it's its it's like uh when you have
[4022.18 → 4027.32] a product you have different landing pages to explain to people who are trying to use it for
[4027.32 → 4032.10] different things why they care about it and what features will help them and so that's really kind
[4032.10 → 4038.00] of what I want I wanted to provide documentation that is of that quality well I think this uh the
[4038.00 → 4043.94] release plan talking about that has just perfectly aligned us with the first closing question which
[4043.94 → 4050.00] which to me is everyone listening to this I know there are tons of people out there using octopuses
[4050.00 → 4056.84] you know it I know it uh the stars on GitHub say so as well um but for that caring community both
[4056.84 → 4063.56] users and potentially contributing developers what is the best way to help you move through this
[4063.56 → 4068.88] release plan supports you either you know it could be documentation it could be whatever what are some
[4068.88 → 4073.74] of the ways that people can step up and help with the needs of octopuses right now
[4073.74 → 4082.00] so I think um people who have existing sites the using older versions of octopuses if they
[4082.00 → 4086.86] try to migrate to use the new stuff the the hard thing is because I don't have a theme yet
[4086.86 → 4090.52] it's not like I can tell them use this theme it's like well if you were depending on the old theme if
[4090.52 → 4098.32] that's why you used octopuses then um write some HTML and CSS you know it's that's not a great thing to
[4098.32 → 4102.94] tell them right, so there's that automatically reduces my audience to a large degree of who is
[4102.94 → 4108.56] willing to jump ship and try the new stuff until I have that out there but for those who are just
[4108.56 → 4113.78] interested in Jekyll even um anybody who has if you've had a lightweight octopuses site and you
[4113.78 → 4119.06] want either there are Jekyll themes out there you can use too um but if you want to try the new stuff
[4119.06 → 4127.18] um uh right now dig around on the octopuses org repos and see what's there um you know reach out
[4127.18 → 4131.70] to me if you want to talk I've had a lot of email correspondence with different people who are
[4131.70 → 4137.66] interested in working on different parts uh try things out break things complain about them um you
[4137.66 → 4141.50] know somebody the other day was asking me to add a Google app engine deployment system to octopuses
[4141.50 → 4145.16] deploy and I was like dude send me a pull request I've never used it before but I'm happy to review it
[4145.16 → 4152.18] and try things out um so I've had lots of people try if you are a person who likes to write
[4152.18 → 4156.24] in multiple languages please try octopuses multilingual it makes that so much easier in
[4156.24 → 4163.94] Jekyll um yeah so mainly what I'm looking for is pull requests and issues opened on the new stuff
[4163.94 → 4168.80] and anybody that wants to share what it was like for them to migrate some people have already written
[4168.80 → 4174.62] blog posts about that and those are really helpful too so you do have some people who have
[4174.62 → 4179.68] started to use it but just they've said okay there's no theme yet for it right, and they're
[4179.68 → 4184.26] sort of operating in this unknown world where it's not quite released well they just use their old
[4184.26 → 4187.70] layouts and themes and stuff, and they're just removing they're just removing plugins that they
[4187.70 → 4192.20] don't need anymore because they can use the new ones so uh it's you know a lot of it is just delete
[4192.20 → 4200.62] the plugins from your plugins directory and add some gems and build until it works it's you know
[4200.62 → 4204.08] there you go it's yeah it's a little bit of discovery there which is unfortunate and this
[4204.08 → 4208.28] is why I'm getting away from it and I can't wait till everyone has the awesomeness version
[4208.28 → 4214.16] and this sort of thing doesn't happen anymore so for those listening right now that use octopuses
[4214.16 → 4219.72] and say I haven't migrated but I will right after the show how do I do it what's the first thing
[4219.72 → 4223.32] that I know you may already say it already but what's the first step they could take to take their
[4223.32 → 4227.74] old Jekyll uh their old octopuses ways of doing things how could they move into
[4227.74 → 4233.28] octopuses 3.0 well they can try um installing the octopuses gem and just work with the new
[4233.28 → 4240.92] uh command lines and uh command line tools, so there's a there's a giant markdown README that
[4240.92 → 4248.04] explains everything you can do with the octopuses CLI on uh octopress and um try that stuff
[4248.04 → 4254.16] out and uh you know like I said about the plugins remove the move the old stuff look for the new ones on
[4254.16 → 4262.84] um on the octopuses org so yeah so for those out there who go and do this and try it out
[4262.84 → 4268.38] give Brandon some feedback what's the best way to do it an issue an email a tweet a blog post
[4268.38 → 4274.50] um all yeah I mean all the above create an issue if it makes sense to create an issue uh um issues
[4274.50 → 4278.90] I'm thinking like to give feedback to the rest of the community who might be coming behind them about
[4278.90 → 4283.08] the migration path right yeah so that blog posts are great for that um if they can also
[4283.08 → 4286.70] they want to open an issue for discussion I'm I'm happy to discuss that sort of thing because
[4286.70 → 4292.96] that's totally relevant um but yeah I think one of the better ways to start really is with a new
[4292.96 → 4298.66] vanilla Jekyll site so that I think a lot of octopuses users or not I don't know a lot you know
[4298.66 → 4303.70] that's one thing I have no idea how big the community is because um it's not like a gem where
[4303.70 → 4306.54] you have download numbers, or you have ways of tracking that sort of it so it's a little different
[4306.54 → 4312.80] but I think many people have come to octopuses and don't understand Jekyll, and they don't even
[4312.80 → 4317.08] know they're using Jekyll, or they don't really think about you know how Jekyll does things and so
[4317.08 → 4322.76] I think having a fundamental understanding of Jekyll is way better than being like where's my bloody
[4322.76 → 4328.44] rake task you know like I don't I don't want to if it's a little bit hard for people if they
[4328.44 → 4332.36] have never really seen the Jekyll part of octopuses before and now all of a sudden
[4332.36 → 4337.90] that sort of changes for them um but yeah if you understand what Jekyll is doing then I say start a
[4337.90 → 4344.08] new Jekyll site and start playing with new octopuses plugins for it our next uh closing
[4344.08 → 4348.96] question one everybody loves to answer and loves to hear the answers of is who is your programming
[4348.96 → 4354.70] hero I'm going to have to go so I've thought about this a lot because uh I knew this was going to come on
[4354.70 → 4361.42] when I agreed to be on the show, and so I really think um I'm going to have to say with Chris
[4361.42 → 4369.44] coy around this because uh he's a really nice dude who builds a lot of great stuff and helps
[4369.44 → 4373.62] everyone like he is so good at helping everyone and that he is like very helpful it's just so
[4373.62 → 4378.68] awesome, and you know the times that I've gotten to hang out with him um he's just the sweetest person
[4378.68 → 4387.74] so i i I like what he does for um the front end nerds like me, and you know of course code pin I mean
[4387.74 → 4394.18] that's such a gift like I use that thing so much um actually when I was working on the uh
[4394.18 → 4401.90] code highlighting plugins for octopuses um I was trying some new uh HTML and I wanted to see how
[4401.90 → 4409.24] they work as a know for uh vision impaired users you know can they use screen readers to follow
[4409.24 → 4412.58] the code plugins and some guy was telling me there were some issues with it so i actually
[4412.58 → 4417.72] uh dumped HTML over on code pin and just was really rapidly iterating with him and saying
[4417.72 → 4420.66] you know does this work does this work, and he kept trying it with all of his different uh
[4421.50 → 4428.18] um screen readers, and it was like so useful so yeah Chris coy is doing awesome stuff and um
[4428.18 → 4436.24] totally look up to him uh, so yeah couldn't have picked the uh a better hero I didn't expect you to
[4436.24 → 4440.80] tell him but I really see totally well no i just I wasn't I guess I didn't really have any
[4440.80 → 4446.22] expectations i just yeah I figured which way would you go would you go the designer route or would you
[4446.22 → 4451.70] go the developer route in terms of a hero and Chris is sort of both you know yeah I mean he's he more
[4451.70 → 4455.32] closely aligns with the kind of things that I do actually I got to introduce him to sass which was
[4455.32 → 4461.22] really fun um so that's kind of a little feather in my cap uh but uh yeah anyway he's got the's got
[4461.22 → 4467.22] his um uh he's got his podcast that he does why did I just forget the name of it I'm subscribed
[4467.22 → 4472.16] shop talk thank you I just couldn't, I just need to hear things of some banjo music
[4472.16 → 4477.48] and then I'll remember shop talk show so yeah he's got that he's doing um just he's putting out a lot
[4477.48 → 4483.06] and um you know whenever I'm searching for something about CSS he's got stuff written about it that is
[4483.06 → 4489.92] very helpful to me, you can't do a search for CSS of anything and not somehow land on CSS tricks
[4489.92 → 4496.48] funny aside to that is when we were originally going to do the sassway.com uh we had considered
[4496.48 → 4504.94] uh sass tricks oh, and we even considered like sass hyphen tricks.com it's just like a jab in the
[4504.94 → 4511.22] side no we can no, no it's more of an homage than any oh yeah yeah you know it was never like hey we're
[4511.22 → 4516.76] taking your thunder I mean who could take CSS tricks thunder right um, but it was you know because
[4516.76 → 4523.36] the original tagline for it was like uh which is why we called it the sass way is also an homage to
[4523.36 → 4529.72] the ruby way and the rails way you know and obi and all that good stuff you know, but it was like
[4529.72 → 4534.72] you know you're writing, and you could probably attest to this too Brandon because when we were
[4534.72 → 4539.96] originally trying to like to get people excited about sass it was like we were speaking foreign languages
[4539.96 → 4543.88] and no one understood what the heck we were talking about yeah and I remember talking to you Brandon I was
[4543.88 → 4550.32] like we need to do a sass podcast this is actually just before I think just before we created this
[4550.32 → 4558.04] show the changelog that's crazy wow, wow thinking about that, but it was like you don't have to write
[4558.04 → 4562.50] CSS that hardware any more there's a better way it's called the sass way and so that's that's why
[4562.50 → 4567.46] that's why the name stuck yeah, and then it turns out that eventually CSS tricks also became sass tricks
[4567.46 → 4572.68] because if you're writing a style sheet on there it's probably going to be sad yeah that's right
[4572.68 → 4577.66] that's right well uh Brandon i have to say man it's its always a pleasure to have you on the show
[4577.66 → 4583.30] you have our full support in every way we can uh listeners please help Brandon in any way you can
[4583.30 → 4590.08] if you're an octopuses user or a just a Jekyll user try out octopuses get a Ferrari stop uh driving
[4590.08 → 4598.06] a civic not the Jekyll's a civic without octopuses it's not it's wonderful it's just like it's like
[4598.06 → 4603.58] taking your engine and like putting that after market chip in it right like the stock
[4603.58 → 4608.34] chip is really great, and it'll do great there's an after market chip, and it's totally free that's on
[4608.34 → 4614.18] GitHub well I will say the one of the things that um people will ask is so all this stuff works
[4614.18 → 4617.08] with Jekyll why are you calling it octopuses anymore and I was like wait a minute it always
[4617.08 → 4621.12] worked with Jekyll and there 's's this unfortunate and I talked about this in that post
[4621.12 → 4624.62] there's this unfortunate concept that Jekyll and octopuses are separate communities
[4624.62 → 4632.12] and i so badly want to destroy that um and the reason I'm using octopuses is that I can name
[4632.12 → 4636.08] gems whatever I want to with an octopuses prefix I don't want to use Jekyll prefix and steal stuff
[4636.08 → 4642.84] from them, I don't you know it's its kind of like I get to have you know this is branded uh as something
[4642.84 → 4648.06] that I am building or people who understand uh what it's like to build great stuff on top of Jekyll are
[4648.06 → 4652.98] building you know other people can build an octopuses plugin but um it's uh yeah so that's
[4652.98 → 4657.70] it is as much as I can possibly embrace Jekyll's community that's what octopuses is
[4657.70 → 4664.34] well brain like I said it's an it's great having you on the show um we're here to support however
[4664.34 → 4668.88] we can octopuses seems really awesome I feel far more enlightened now than having you on the show
[4668.88 → 4674.04] talking about it where before I was like what is it how is it gonna work now I totally get it good
[4674.04 → 4679.44] uh jarred and i our lights are on we're we are home so we uh we're excited about it
[4679.44 → 4683.48] uh we do have an upcoming show that's pretty cool the next show we're doing
[4683.48 → 4687.60] is uh is with peter I'm not sure if you're going to say his last name I think it's
[4688.24 → 4696.64] Burgoyne b-o-u-r-g-o-n so I'm going to say Burgoyne uh he wrote this thing called go kid it's its go in
[4696.64 → 4704.24] the modern enterprise as everyone knows uh java is dying or should be dead and go is the new hotness
[4704.24 → 4710.06] and this is a measure to bring uh go into the enterprise and take over the java world so
[4710.06 → 4716.58] there you go kid awesome that's the next show coming up but uh for now let's say goodbye see ya
[4716.58 → 4718.08] bye everyone
[4718.08 → 4722.70] Robin
[4722.70 → 4727.68] so
[4727.68 → 4741.26] yeah
[4741.26 → 4771.24] I love you.
